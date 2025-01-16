""" # objects.language
Object for Language module parsing and loading. Language modules are plugins for the persona's model.
"""

# Standard Library Modules
import os

# Application Modules
import conf 

class Language:
    inst = None
    """Singleton instance"""
    modules = { }
    """Language modules"""
    dir = None
    """Directory containg Language modules"""
    ext = None
    """File extension of Language modules"""

    def __init__(
        self, 
        enabled: list, 
        dir = conf.CACHE["DIR"]["MODULES"],
        ext = conf.LANGUAGE["EXTENSION"]
    ):
        """
        Initialize new Persona Language with a set of modules. Language modules are given below,

        - object
        - voice
        - inflection
        - words

        :param enabled: List of enabled Language modules
        :type enabled: list
        :param dir: Directory containing Language modules. Defaults to ``data/modules``.
        :type dir: str
        :param ext: File extension of Language modules. Defaults to ``.rst``.
        """
        self.dir = dir
        self.ext = ext
        self._load(enabled)

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        """
        Create Language singleton.
        """
        if not self.inst:
            self.inst = super(
                Language, 
                self
            ).__new__(self)
        return self.inst
    
    def _load(
        self, 
        enabled
    ):
        """
        Load enabled Language modules.

        :param enabled: List of enabled Language modules.
        :type enabled: list
        """
        
        for root, _, files in os.walk(self.dir):
            for file in files:
                if os.path.splitext(file)[1] != self.ext:
                    continue

                if os.path.splitext(file)[0] not in enabled:
                    continue

                module = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    payload  = f.read()
                
                self.modules[module] = payload

    def get_module(
        self, 
        module : str
    ) -> str:
        """
        Get enabled Language module.

        :param module: Language module to retrieve.
        :type module: str
        :returns: RST document containing Language module.
        :rtype: str
        """
        return self.modules[module]

    def get_modules(self) -> dict:
        """
        Returns all Language modules, formatted for templating.

        :returns: Dictionary of RST documents.
        :rtype: dict
        """
        if len(self.modules) > 0:
            return {**{
                "language": True
            }, **self.modules}
        return self.modules
    
    def list_modules(self) -> list:
        """
        Returns a list of Language module names.
nsion
        :returns: List of modules.
        :rtype: list
        """
        return [ k for k in self.modules.key() ]