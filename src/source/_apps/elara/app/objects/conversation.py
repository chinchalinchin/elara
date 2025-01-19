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

logger = logging.getLogger(__name__)

class Conversation:
    dir = None
    """History directory"""
    ext = None
    """History file extension"""
    hist = { }
    """Chat history"""
    inst = None
    """Singleton instance"""
    tz_offset = None
    """Timezone offset"""

    def __init__(
        self, 
        dir = None,
        ext = None,
        tz_offset = None
    ):
        """
        Initialize Conversation object.

        :param dir: Directory containing chat history. Defaults to ``data/history``.
        :type dir: str
        :param ext: File extension for chat history. Defaults to ``.json``.
        :type ext: str
        """
        self.dir = dir
        self.ext = ext
        self.tz_offset = tz_offset
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
            ).__new__(self, *args, **kwargs)
        return self.inst
    
    def _load(self):
        """
        Load Conversation history from file.
        """
        
        for root, _, files in os.walk(self.dir):
            for file in files:
                if os.path.splitext(file)[1] != self.ext:
                    continue

                persona = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                    if content:
                        payload  = json.loads(f)
                    else: 
                        payload = { "payload": [] }
                    self.hist[persona] = payload["payload"]
                except (FileNotFoundError, json.JSONDecodeError) as e:
                    logger.error(f"Error loading conversation history: {e}")
                    self.hist[persona] = []

    def _persist(
        self, 
        persona : str
    ) -> None:
        """
        Save Persona Conversation history to file.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        file = "".join([persona, self.ext])
        file_path = os.path.join(self.dir, file)
        payload = { "payload": self.hist[persona] }
        with open(file_path, 'w') as f:
            return json.dump(payload, f)
        return None
    
    def _timestamp(self):
        """
        Generates a timestamp in MM-DD HH:MM EST 24-hour format.
        """
        now = datetime.datetime.now(
            datetime.timezone(
                datetime.timedelta(
                    hours=self.tz_offset
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
        if persona not in self.hist.keys():
            raise ValueError(f"Persona {persona} conversation history not found.")
        return self.hist[persona]
    
    def update(
        self, 
        persona : str, 
        name : str, 
        text : str
    ) -> dict:
        """
        Update Conversation history and CACHE to file.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        :param name: Name of the chatter (prompter or persona).
        :type name: str
        :param text: Chat message.
        :type text: str
        :returns: Full chat history
        :rtype: dict
        """
        if persona not in self.hist.keys():
            self.hist[persona] = []

        self.hist[persona].append({ 
            "name": name,
            "text": text,
            "timestamp": self._timestamp()
        })
        self._persist(persona)
        return self.hist[persona]

    def vars(
        self,
        persona: str
    ) -> dict: 
        """
        Return current persona formatted for templating.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        if persona not in self.hist.keys():
            raise ValueError(f"Persona {persona} conversation history not found")
        
        return {
            "history": self.hist[persona]
        }