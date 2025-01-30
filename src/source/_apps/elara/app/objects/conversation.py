"""
objects.conversation
--------------------

Object for managing conversation chat history.
"""
# Standard Library Modules
import datetime
import json
import logging
import os
import typing

# Application Modules
import constants
import loader
import exceptions


logger                          = logging.getLogger(__name__)


class Conversation:
    """
    Application conversations. Object for loading and persisting messages to the chat history, and updating persona memories.

    .. important::

        Conversation is implemented as a singleton to prevent concurrent writes to the a persona's chat history and memories.
        
    """
    # Class properties
    convo_config                : dict = { }
    """Conversation configuration."""
    convo                       : dict = { }
    """Conversation history."""
    directory                   : str = None
    """Conversation data directories."""
    extension                   : str = None
    """Conversation data extensions."""
    inst                        : typing.Self = None
    """Singleton instance."""
    schema                      : dict = { }
    """Schema skeleton for new conversation data structures."""
    _zone                       : datetime.timezone = None

    # Conversation properties
    _prop_hist                  = constants.ConvoProps.HISTORY.value
    _prop_mem                   = constants.ConvoProps.MEMORY.value
    _prop_msg                   = constants.ConvoProps.MESSAGE.value
    _prop_name                  = constants.ConvoProps.NAME.value
    _prop_schema                = constants.ConvoProps.SCHEMA_FILENAME.value
    _prop_time                  = constants.ConvoProps.TIMESTAMP.value
    _prop_zone                  = constants.ConvoProps.TIMEZONE_OFFSET.value


    def __init__(self, directory: str, extension: str, convo_config: dict):
        """
        Initialize the Conversation object. The schemas for the ``dirs`` and ``ext`` arguments are given below,

        :param directory: Directory containing conversation data.
        :type dirs: `str`
        :param extension: File extension for conversation data.
        :type extension: `str`
        :param convo_config: Conversation configuration properties
        :type convo_config: `dict`
        """
        self.directory          = directory
        self.extension          = extension
        self.convo_config       = convo_config
        self.schema             = self._schema()
        self.convo              = self._convo()
        self._zone              = datetime.timezone(datetime.timedelta(
            hours               = self.convo_config.get(self._prop_zone)
        ))


    def __new__(self, *args, **kwargs) -> typing.Self:
        """
        Create Conversation singleton.
        """
        if not self.inst:
            self.inst           = super(Conversation, self).__new__(self)
        return self.inst
    

    def _write(self, persona: str) -> None:
        """
        Persist a conversation property for a persona.

        :param persona: Persona whose data is being persisted.
        :type persona: `str`
        """
        file                    = "".join([persona, self.extension])
        file_path               = os.path.join(self.directory, file)
        
        try:
            with open(file_path, 'w') as f:
                json.dump(self.convo[persona], f)

        except Exception as e:
            logger.error(f"Error persisting {persona} conversation history: {e}")


    def _schema(self) -> dict:
        """
        Load a conversation schema from file.

        :returns: Dictionaryschema for new conversation.
        :rtype: `dict`
        """
        schema_filename         = self.convo_config[self._prop_schema]
        schema_file             = "".join([schema_filename, self.extension])
        schema_path             = os.path.join(self.directory, schema_file)
        
        payload                 = loader.json_file(schema_path)

        if payload:
            return payload 

        raise exceptions.DataNotFoundError(schema_path)
        

    def _convo(self) -> dict:
        """
        Traverse the conversation directory and read the contents into data structure.

        :returns: A dictionary containing the parsed data.
        :rtype: `dict`
        """
        raw                     = { }
        for root, _, files in os.walk(self.directory):
            for file in files:
                persona, ext    = os.path.splitext(file)

                if ext != self.extension or \
                    persona == self.convo_config[self._prop_schema]:
                    continue

                file_path       = os.path.join(root, file)
                raw[persona]    = loader.json_file(file_path)
        
        return raw


    def _timestamp(self) -> str:
        """
        Generates a timestamp in MM-DD HH:MM EST 24-hour format.
        """
        now                     = datetime.datetime.now(self._zone) 
        return now.strftime("%m-%d %H:%M")


    def clear(self, persona: str) -> None:
        """
        Remove a persona's conversation history and memories.

        :param persona: Persona to be cleared.
        :type persona: `str`
        """
        logger.warning(
            f"Clearing {persona}'s conversation history and memories.")
        self.convo[persona]     = self.schema
        self._write(persona)
        return


    def get(self, persona: str) -> dict:
        """
        Return current persona.

        :param persona: Persona with which the prompter is conversing.
        :type persona: `str`
        """
        if persona not in self.convo.keys():
            raise exceptions.DataNotFoundError(persona)
        return self.convo[persona]
    

    def update(self, persona: str, name: str, message: str, 
               memory: str | None = None, persist: bool = True) -> dict:
        """
        Update and persist conversation properties.

        :param persona: Persona with which the prompter is conversing.
        :type persona: `str`
        :param name: Name of the speaker (prompter or persona).
        :type name: `str`
        :param message: Conversation string 
        :type messagge: `str`
        :param memory: Memory string
        :type memory: `str`
        :returns: Full conversation history
        :rtype: `dict`
        """
        if not message:
            logger.warning("Cannot update conversation with an empty message.")
            return
        
        if persona not in self.convo.keys():
            logger.warning(
                f"No data found for {persona}, defaulting to new schema")
            self.convo[persona] = self.schema

        self.convo[persona][self._prop_hist].append({ 
            self._prop_name     : name,
            self._prop_msg      : message,
            self._prop_time     : self._timestamp()
        })
        
        if memory is not None:
            self.convo[persona][self._prop_mem] \
                                = memory

        if persist:
            self._write(persona)

        return self.convo[persona]


    def vars(self, persona: str) -> dict: 
        """
        Return current persona formatted for templating.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        if persona not in self.convo.keys():
            logger.warning(
                f"No data for {persona} found, defaulting to new schema.")
            return self.schema
        
        return self.convo[persona]