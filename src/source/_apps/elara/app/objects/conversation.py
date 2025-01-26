"""
objects.conversation
--------------------

Object for managing conversation chat history.
"""
# Standard Library Modules
import enum
import datetime
import json
import logging
import os
import typing

# Application Modules
import util 

logger = logging.getLogger(__name__)

class ConvoProps(enum.Enum):
    """
    Conversation property key enumeration.
    """
    # Internal Properties
    HISTORY                                     = "history"
    MEMORIES                                    = "memories"
    MEMORY                                      = "memory"
    SEQUENCE                                    = "sequence"
    FEEDBACK                                    = "feedback"
    MESSAGE                                     = "msg"
    TIMESTAMP                                   = "timestamp"
    NAME                                        = "name"
    # Configuration Properties
    SCHEMA_FILENAME                             = "SCHEMA_FILENAME"


class Conversation:
    """
    Application conversations. Object for loading and persisting messages to the chat history, and updating persona memories.

    .. important::

        Conversation is implemented as a singleton to prevent concurrent writes to the a persona's chat history and memories.
    """
    convo_config                                = { }
    """Conversation configuration."""
    convo                                       = { }
    """Conversation history."""
    dirs                                        = None
    """Conversation data directories."""
    exts                                        = None
    """Conversation data extensions."""
    inst                                        = None
    """Singleton instance."""
    schemas                                     = { }
    """Schema skeletons for new conversation data structures."""

    def __init__(
        self, 
        dirs                                    : str,
        exts                                    : str,
        convo_config                            : dict,
    ):
        """
        Initialize Conversation object.

        .. note::

            dirs = {
                f"{conversation.ConvoProps.HISTORY}": "history directory",
                f"{convversation.ConvoProps.MEMORY}": "memory directory"
            }

        :param dirs: Directories 
        :param hist_ext: File extension for chat history.
        :type hist_ext: str
        """
        self.dirs                               = dirs
        self.exts                               = exts
        self.convo_config                       = convo_config
        self._load()


    def __new__(self, *args, **kwargs):
        """
        Create Conversation singleton.
        """
        if not self.inst:
            self.inst                           = super(Conversation, self).__new__(self)
        return self.inst
    

    def _schema(self,
        prop                                    : ConvoProps
    ):
        schema_filename                         = self.convo_config[ConvoProps.SCHEMA_FILENAME.value]
        schema_file                             = "".join([
                                                    schema_filename,
                                                    self.exts[prop]
                                                ])
        schema_path                             = os.path.join(
                                                    self.dirs[prop], 
                                                    schema_file
                                                )
        
        try:
            with open(schema_path, "r") as f:
                content                         = f.read()

            if content:
                payload                         = json.loads(content)

            else: 
                raise ValueError(f"No schema found at {schema_path}")
            
            return payload["payload"]

        except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
            raise ValueError(f"Error loading JSON schema {schema_path}")


    def _write(self,
        persona                                 : str,
        prop                                    : ConvoProps
    )                                           -> None:
        """
        Persist a conversation property for a persona.

        :param persona: Persona whose data is being persisted.
        :type persona: str
        :param prop: Property of persona that is being persisted.
        :type: `conversation.ConvoProps`
        """
        file                                    = "".join([
                                                    persona, 
                                                    self.exts[prop]
                                                ])
        
        file_path                               = os.path.join(
                                                    self.dirs[prop], 
                                                    file
                                                )
        
        payload                                 = util.payload(
                                                    self.convo[persona][prop]
                                                )
        
        try:
            with open(file_path, 'w') as f:
                json.dump(payload, f)

        except Exception as e:
            logger.error(f"Error persisting {prop} for {persona}: {e}")


    def _process(self,
        prop                                    : ConvoProps,
    )                                           -> dict:
        """
        Traverse the conversation property directory and read the contents into a data structure.

        :param prop: Conversation property to read.
        :type: `conversation.ConvoProps`
        :returns: A dictionary containing the parsed data.
        :rtype: `dict`
        """
        raw                                     = { }
        for root, _, files in os.walk(self.dirs[prop]):
            for file in files:
                persona, ext                    = os.path.splitext(file)

                if ext != self.exts[prop] or \
                    persona == self.convo_config[ConvoProps.SCHEMA_FILENAME.value]:
                    continue

                file_path                       = os.path.join(root, file)
                raw[persona]                    = { }

                try:
                    with open(file_path, "r") as f:
                        content                 = f.read()

                    if content:
                        payload                 = json.loads(content)

                    else: 
                        payload                 = util.payload(self.schemas[prop])

                    raw[persona][prop]          = payload["payload"]

                except (FileNotFoundError, json.JSONDecodeError) as e:
                    logger.error(f"Error loading JSON data: {e}")
                    raw[persona][prop]          = self.schemas[prop]

                except Exception as e:
                    logger.error(
                        f"An unexpected error occurred while loading from {file_path}: {e}"
                    )
                    raw[persona][prop]          = self.schemas[prop]
        
        return raw


    def _load(self):
        """
        Load Conversation history from file.
        """

        self.schemas[ConvoProps.HISTORY.value]  = self._schema(
            prop                                = ConvoProps.HISTORY.value
        )

        self.schemas[ConvoProps.MEMORIES.value] = self._schema(
            prop                                = ConvoProps.MEMORIES.value
        )

        history                                 = self._process(
            prop                                = ConvoProps.HISTORY.value,
        )

        memories                                = self._process(
            prop                                = ConvoProps.MEMORIES.value,
        )

        self.convo                              = util.merge(
            dict1                               = history, 
            dict2                               = memories
        )


    def _persist(self, 
        persona                                 : str
    )                                           -> None:
        """
        Save Persona Conversation history to file.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """

        self._write(
            persona                             = persona,
            prop                                = ConvoProps.HISTORY.value
        )
        
        self._write(
            persona                             = persona, 
            prop                                = ConvoProps.MEMORIES.value
        )
    

    def _timestamp(self):
        """
        Generates a timestamp in MM-DD HH:MM EST 24-hour format.
        """
        delta                                   = datetime.timedelta(
            hours                               = self.convo_config.get("TIMEZONE_OFFSET")
        )
        zone                                    = datetime.timezone(
            offset                              = delta
        )
        now                                     = datetime.datetime.now(
            tz                                  = zone
        ) 
        return now.strftime("%m-%d %H:%M")


    def clear(self,
        persona                                 : str
    )                                           -> None:
        """
        Remove a persona's conversation history and memories.

        :param persona: Persona to be cleared.
        :type persona: str
        """
        self.convo[persona][ConvoProps.HISTORY.value] \
                                                = self.schemas[ConvoProps.HISTORY.value]
        self.convo[persona][ConvoProps.MEMORIES.value] \
                                                = self.schemas[ConvoProps.MEMORIES.value] 
        self._persist(persona)


    def get(self, 
        persona                                 : str
    )                                           -> dict:
        """
        Return current persona.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        if persona not in self.convo.keys():
            raise ValueError(f"Persona {persona} conversation history not found.")
        return self.convo[persona]
    

    def update(self, 
        persona                                 : str, 
        name                                    : str, 
        msg                                     : str,
        memory                                  : str | None = None,
        feedback                                : str | None = None,
        persist                                 : bool = True
    ) -> dict:
        """
        Update and persist conversation properties.

        :param persona: Persona with which the prompter is conversing.
        :type persona: `str`
        :param name: Name of the speaker (prompter or persona).
        :type name: `str`
        :param msg: Chat message.
        :type msg: `str`
        :param memory: Memory string
        :type memory: `str`
        :returns: Full chat history
        :rtype: `dict`
        """
        if persona not in self.convo.keys():
            self.convo[persona][ConvoProps.HISTORY.value] \
                                                = self.schemas[ConvoProps.HISTORY.value]
            self.convo[persona][ConvoProps.MEMORIES.value] \
                                                = self.schemas[ConvoProps.MEMORIES.value] 

        self.convo[persona][ConvoProps.HISTORY.value].append({ 
            ConvoProps.NAME.value               : name,
            ConvoProps.MESSAGE.value            : msg,
            ConvoProps.TIMESTAMP.value          : self._timestamp()
        })
        
        if memory is not None:
            self.convo[persona][ConvoProps.MEMORIES.value][ConvoProps.SEQUENCE.value].append({
                ConvoProps.MEMORY.value         : memory
            })

        if feedback is not None:
            self.convo[persona][ConvoProps.MEMORIES.value][ConvoProps.FEEDBACK.value] \
                                                = feedback

        if persist:
            self._persist(persona)

        return self.convo[persona]


    def vars(self,
        persona                                 : str
    )                                           -> dict: 
        """
        Return current persona formatted for templating.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        if persona not in self.convo.keys():
            logger.error(f"Persona {persona} conversation history not found")
            return {
                ConvoProps.HISTORY.value        : self.schemas[ConvoProps.HISTORY.value],
                ConvoProps.MEMORIES.value       : self.schemas[ConvoProps.MEMORIES.value]
            }
        
        return self.convo[persona]