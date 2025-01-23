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
import util 

logger = logging.getLogger(__name__)

class Conversation:
    hist_dir = None
    """History directory"""
    mem_dir = None
    """Memory directory"""
    hist_ext = None
    """History file extension"""
    mem_ext = None 
    """Memory file extension"""
    convo = { }
    """Chat history"""
    inst = None
    """Singleton instance"""
    converse_config = {}
    """Conversation configuration."""

    def __init__(
        self, 
        hist_dir : str,
        mem_dir: str,
        hist_ext: str,
        mem_ext: str,
        converse_config : dict,
    ):
        """
        Initialize Conversation object.

        :param hist_dir: Directory containing chat history.
        :type hist_dir: str
        :param hist_ext: File extension for chat history.
        :type hist_ext: str
        """
        self.hist_dir = hist_dir
        self.hist_ext = hist_ext
        self.mem_dir = mem_dir
        self.mem_ext = mem_ext
        self.converse_config = converse_config
        self._load()

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        """
        Create Conversation singleton.
        """
        if not self.inst:
            self.inst = super(
                Conversation, 
                self
            ).__new__(self)
        return self.inst
    
    @staticmethod
    def _process(
        dir : str, 
        ext : str, 
        prop: str,
        default : typing.Any,
        temp : str = "_new"
    ) -> dict:
        raw = { }
        for root, _, files in os.walk(dir):
            for file in files:
                persona = os.path.splitext(file)[0]
                ext = os.path.splitext(file)[1]

                if ext != ext or persona == temp:
                    continue

                persona = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)
                raw[persona] = { }

                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                    if content:
                        payload  = json.loads(content)
                    else: 
                        payload = { "payload": default }

                    raw[persona][prop] = payload["payload"]
                except (FileNotFoundError, json.JSONDecodeError) as e:
                    logger.error(f"Error loading JSON data: {e}")
                    raw[persona][prop] = default
                except Exception as e:
                    logger.error(f"An unexpected error occurred while loading from {file_path}: {e}")
                    raw[persona][prop] = default
        
        return raw

    def _load(self):
        """
        Load Conversation history from file.
        """
        
        history = self._process(
            dir = self.hist_dir, 
            ext = self.hist_ext,
            prop = "history",
            default = [ ]
        )
        memories = self._process(
            dir = self.mem_dir, 
            ext = self.mem_ext,
            prop = "memories",
            default = {
                "sequence": [],
                "feedback": None
            } 
        )
        self.convo = util.merge(history, memories)

    def _persist(
        self, 
        persona : str
    ) -> None:
        """
        Save Persona Conversation history to file.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        file = "".join([persona, self.hist_ext])
        file_path = os.path.join(self.hist_dir, file)
        payload = { "payload": self.convo[persona]["history"] }
        try:
            with open(file_path, 'w') as f:
                json.dump(payload, f)
        except Exception as e:
            logger.error(f"Error persisting conversation history for {persona}: {e}")
            return None
        
        file = "".join([persona, self.mem_ext])
        file_path = os.path.join(self.mem_dir, file)
        payload = { "payload": self.convo[persona]["memories"] }
        try:
            with open(file_path, 'w') as f:
                json.dump(payload, f)
        except Exception as e:
            logger.error(f"Error persisting memories for {persona}: {e}")
            return None
    
        return None
    
    def _timestamp(self):
        """
        Generates a timestamp in MM-DD HH:MM EST 24-hour format.
        """
        now = datetime.datetime.now(
            datetime.timezone(
                datetime.timedelta(
                    hours=self.converse_config["TIMEZONE_OFFSET"]
                )
            )
        ) 
        return now.strftime("%m-%d %H:%M")

    def get(
        self, 
        persona : str
    ) -> dict:
        """
        Return current persona.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        if persona not in self.convo.keys():
            raise ValueError(f"Persona {persona} conversation history not found.")
        return self.convo[persona]
    
    def update(
        self, 
        persona : str, 
        name : str, 
        msg : str,
        memory: str | None = None,
        feedback: str | None = None,
        persist: bool = True
    ) -> dict:
        """
        Update Conversation history and CACHE to file.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        :param name: Name of the chatter (prompter or persona).
        :type name: str
        :param msg: Chat message.
        :type msg: str
        :param mem: Memory string
        :type msg: str
        :returns: Full chat history
        :rtype: dict
        """
        if persona not in self.convo.keys():
            self.convo[persona] = {}
            self.convo[persona]["history"] = []
            self.convo[persona]["memories"] = {}
            self.convo[persona]["memories"]["sequence"] = []
            self.convo[persona]["memories"]["feedback"] = None

        self.convo[persona]["history"].append({ 
            "name": name,
            "msg": msg,
            "timestamp": self._timestamp()
        })
        
        if memory is not None:
            self.convo[persona]["memories"]["sequence"].append({
                "memory": memory
            })

        if feedback is not None:
            self.convo[persona]["memories"]["feedback"] = feedback

        if persist:
            self._persist(persona)

        return self.convo[persona]

    def vars(
        self,
        persona: str
    ) -> dict: 
        """
        Return current persona formatted for templating.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        if persona not in self.convo.keys():
            logger.error(f"Persona {persona} conversation history not found")
            return {
                "history": [],
                "memories": {}
            }
        
        return {
            "history": self.convo[persona]["history"],
            "memories": self.convo[persona]["memories"]
        }