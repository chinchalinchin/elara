"""
objects.language
----------------

Object for Language module parsing and loading. Language modules are plugins for the prompt instructions.
"""

# Standard Library Modules
import os
import logging

logger = logging.getLogger(__name__)

class Language:
    modules = { }
    """Language modules"""
    directory = None
    """Directory containg Language modules"""
    extension = None
    """File extension of Language modules"""

    def __init__(
        self, 
        enabled                             : list, 
        directory                           : str,
        extension                           : str
    ):
        """
        Initialize new Persona Language with a set of modules. Language modules are given below,

        - object
        - voice
        - inflection
        - words

        :param enabled: List of enabled Language modules
        :type enabled: list
        :param directory: Directory containing Language modules. Defaults to ``data/modules``.
        :type directory: str
        :param ext: File extension of Language modules. Defaults to ``.rst``.
        :type ext: str
        """
        self.directory                      = directory
        self.extension                      = extension
        self._load(enabled)

    
    def __iter__(self):
        for k, v in self.modules: 
            yield (k, v)


    def _load(
        self, 
        enabled
    ):
        """
        Load enabled Language modules.

        :param enabled: List of enabled Language modules.
        :type enabled: list
        """
        
        for root, _, files in os.walk(self.directory):
            for file in files:
                module, ext                 = os.path.splitext(file)

                if ext != self.extension:
                    continue

                if module not in enabled:
                    continue

                file_path                   = os.path.join(root, file)

                try:
                    with open(file_path, "r") as f:
                        payload             = f.read()

                    if payload:
                        self.modules[module]= payload
                    else: 
                        logger.warning(f"No content found in {module} language module.")

                except Exception as e:
                    logger.error(f"Error loading language module {file_path}: {e}")
                    continue

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

    def vars(self) -> dict:
        """
        Returns all Language modules, formatted for templating.

        :returns: Dictionary of RST documents.
        :rtype: dict
        """
        if len(self.modules) > 0:
            return {**{ "language": True }, **self.modules}
        return { }
    
    def list_modules(self) -> list:
        """
        Returns a list of Language module names.

        :returns: List of modules.
        :rtype: list
        """
        return [ k for k in self.modules.keys() ]