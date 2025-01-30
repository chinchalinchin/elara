""" 
objects.context
---------------

Object for managing external contextualization data.
"""
# Standard Library Modules
import os
import logging 

# Application Modules
import constants
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

    # Persona properties
    _prop_poem                  = constants.InjectionProps.POEMS.value
    _prop_prof                  = constants.InjectionProps.PROOFS.value
    _prop_quot                  = constants.InjectionProps.QUOTES.value


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

        self.injection          = raw

        return

                
    def vars(self, injection_keys: dict) -> dict:
        """"
        Takes a dictionary of injection keys and converts it into a dictionary of injection content. As an example,

        .. code-block::

            context_keys            = {
                constants.InjectionProps.POEMS.value : [ "id_a" ],
                constants.InjectionProps.PROOFS.value: [ "id_b" ],
                constants.InjectionProps.QUOTES.value: [ "id_c" ]
            }

        This method will take each value and convert it into a block of injection. It will return a dictionary with the same keys.

        :param context_keys: Dictionary of injection keys, keyed by injection type.
        :type context_keys: `dict`
        :returns: Dictionary of injection data, keyed by injection type.
        :rtype:`dict`
        """
        res                     = {}
        for i_type, i_keys in injection_keys.items():
            if i_type not in self.injections.keys():
                logger.warning(f"Invalid injection type: {i_type}")
                continue 

            res[i_type]         = []
            for i_key in i_keys:
                if i_key not in self.injections[i_type].keys():
                    logger.warning(f"Invalid injection key {i_key} for {i_type}.")
                    continue

                res[i_type].append(self.injections[i_type][i_key])

        return { constants.TemplateVars.INJECT.value: res }
