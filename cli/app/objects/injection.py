""" 
objects.context
---------------

Object for managing external contextualization data.
"""
# Standard Library Modules
import os
import logging 

# Application Modules
import properties
import loader


logger                          = logging.getLogger(__name__)


class Injection:
    """"
    
    """
    directory                   : str = None
    """Directory containing injction data"""
    extension                   : str = None
    """Extension of injection data files"""
    injections                  : dict = {}
    """External injections"""

    # Injection properties
    _prop_poem                  = properties.InjectionProps.POEMS.value
    _prop_prof                  = properties.InjectionProps.PROOFS.value
    _prop_quot                  = properties.InjectionProps.QUOTES.value


    def __init__(self, directory: str, extension: str) -> None:
        """
        Initialize `Injection` object.

        :param persona: Initial persona for model to assume. 
        :type persona: `str`
        :param directory: Directory containing persona data.
        :type directory: `str`
        :param extension: File extension of persona data.
        :type extension: `str`
        :param persona_config: Persona configuration.
        :type persona_config: `dict`
        :param context: Location of context file
        :type context: `str`
        """
        self.directory          = directory
        self.extension          = extension
        self._load()

        
    def _load(self) -> None:
        """
        Load injections from data directory.
        """
        raw = {}

        for root, _, files in os.walk(self.directory):
            for file in files:
                i_type, ext     = os.path.splitext(file)

                if ext !=  self.extension:
                    continue

                file_path       = os.path.join(root, file)

                raw[i_type] = loader.json_file(file_path)
        self.injections         = raw

        return


    def get(self):
        """
        TODO
        """
        return self.injections