""" # objects.conversation
Object for managing conversation chat history.
"""
# Standard Library Modules
import os

# Application Modules
import conf 

class Conversation:
    data = None
    dir = None
    ext = None
    hist = { }
    inst = None

    def __init__(
        self, 
        dir = conf.PERSIST["DIR"]["HISTORY"],
        ext = ".json"
    ):
        """
        Initialize Conversation object.
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
        if not self.instance:
            self.instance = super(
                Conversation, 
                self
            ).__new__(self, *args, **kwargs)
        return self.instance
    
    def _load(self):
        """
        Load Conversation history.
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

    def _persist(self, persona):
        file = ".".join([persona, self.ext])
        file_path = os.path.join(self.dir, file)
        with open(file_path, 'a') as f:
            f.write(self.hist[persona])
        return 
    
    def get(self, persona):
        """
        Return Conversation history.
        """
        return self.hist[persona]
    
    def update(self, persona, name, text):
        """
        Update Conversation history.
        """
        self.hist[persona] += [{ 
            "name": name,
            "text": text
        }]
        self._persist(persona)
        return self.hist[persona]
