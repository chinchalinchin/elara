""" # objects.language
Object for Language module parsing and loading. Language modules are plugins for the persona's model.
"""

# Standard Library Modules
import os

# Application Modules
import conf 

class Language:
    instance = None
    modules = None
    directory = None
    extension = None

    def __init__(
        self, 
        enabled, 
        directory = conf.PERSIST["DIR"]["MODULES"],
        extension = conf.LANGUAGE["EXTENSION"]
    ):
        """
        Initialize new Persona Language.
        """
        self.directory = directory
        self.extension = extension
        self._load(enabled)

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        """
        Create Language singleton.
        """
        if not self.instance:
            self.instance = super(
                Language, 
                self
            ).__new__(self, *args, **kwargs)
        return self.instance
    
    def _load(
        self, 
        enabled
    ):
        """
        Load enabled Language modules.
        """
        
        for root, _, files in os.walk():
            for file in files:
                if os.path.splitext(file)[1] != self.extension:
                    continue

                if os.path.splitext(file)[0] not in enabled:
                    continue

                module = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    payload  = f.read()
                
                self.modules[module] = payload

    def get_module(self, module):
        """
        Get enabled Language modules.
        """
        return self.modules[module]

    def get_modules(self):
        return self.modules
    
    def list_modules(self):
        return [ k for k in self.modules.key() ]