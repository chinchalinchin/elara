""" # objects.conversation
Object for managing conversation chat history.
"""
# Standard Library Modules
import os

# Application Modules
import conf 

class Conversation:
    dir = None
    """History directory"""
    ext = None
    """History file extension"""
    hist = { }
    """Chat history"""
    inst = None
    """Singleton instance"""

    def __init__(
        self, 
        dir = conf.PERSIST["DIR"]["HISTORY"],
        ext = ".json"
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

                with open(file_path, "r") as f:
                    payload  = f.read()
                
                self.hist[persona] = payload

    def _persist(
        self, 
        persona : str
    ) -> None:
        """
        Save Persona Conversation history to file.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        file = ".".join([persona, self.ext])
        file_path = os.path.join(self.dir, file)
        with open(file_path, 'a') as f:
            f.write(self.hist[persona])
        return 
    
    def get(
        self, 
        persona : str
    ) -> dict:
        """
        Return Persona Conversation history, formatted for templating.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        """
        return {
            "history": self.hist[persona]
        }
    
    def update(
        self, 
        persona : str, 
        name : str, 
        text : str
    ) -> dict:
        """
        Update Conversation history and persist to file.

        :param persona: Persona with which the prompter is conversing.
        :type persona: str
        :param name: Name of the chatter (prompter or persona).
        :type name: str
        :param text: Chat message.
        :type text: str
        :returns: Full chat history
        :rtype: dict
        """
        self.hist[persona] += [{ 
            "name": name,
            "text": text
        }]
        self._persist(persona)
        return self.hist[persona]
