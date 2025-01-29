""" 
objects.context
---------------

Object for managing external contextualization data.
"""
# Standard Library Modules
import os
import json
import logging 

# Application Modules
import constants


logger                          = logging.getLogger(__name__)


class Context:
    """"
    
    """
    directory                   : str = None
    """Directory containing context data"""
    extension                   : str = None
    """Extension of context data files"""
    context                     : dict = {}
    """External context"""

    # Persona properties
    _prop_poem                  = constants.ContextProps.POEMS.value
    _prop_prof                  = constants.ContextProps.PROOFS.value
    _prop_quot                  = constants.ContextProps.QUOTES.value


    def __init__(self, directory: str, extension: str) -> None:
        """
        Initialize Context object.

        :param persona: Initial persona for model to assume. 
        :type persona: `str`
        :param directory: Directory containing persona data.
        :type directory: `str`
        :param extension: File extension of persona data.
        :type extension: `str`
        :param persona_config: Persona configuration.
        :type persona_config: `dict`
        :param context: Location of context file
        :type context: str
        """
        self.directory          = directory
        self.extension          = extension
        self._context()


    def _context(self) -> None:
        """
        Load context configuration from application directory.
        """
        raw = {}
        for root, _, files in os.walk(self.directory):
            for file in files:
                con_type, ext   = os.path.splitext(file)

                if ext !=  self.extension:
                    continue

                file_path       = os.path.join(root, file)

                try:
                    with open(file_path, "r") as f:
                        content = f.read()

                    if content:
                        payload = json.loads(content)
                    else: 
                        logger.warning(
                            f"No data found for {con_type} context, initializing empty schema.")
                        payload = {}

                    raw[con_type] = payload

                except (FileNotFoundError, json.JSONDecodeError) as e:
                    logger.error(
                        f"Error loading JSON from {file_path}: {e}")
                    raw[con_type] = {}
                    
                except Exception as e:
                    logger.error(
                        f"An unexpected error occurred loading {file_path}: {e}")
                    raw[con_type] = {}

        self.context            = raw
        return

                
    def vars(self, context_keys: dict) -> dict:
        """"
        Takes a dictionary of context keys and converts it into a dictionary of raw context. As an example,

        .. code-block::

            context_keys            = {
                constants.ContextProps.POEMS.value : [ "id_a" ],
                constants.ContextProps.PROOFS.value: [ "id_b" ],
                constants.ContextProps.QUOTES.value: [ "id_c" ]
            }

        This method will take each value and convert it into a block of context. It will return a dictionary with the same keys.

        :param context_keys: Dictionary of context keys, keyed by context type.
        :type context_keys: `dict`
        :returns: Dictionary of context data, keyed by context type.
        :rtype:`dict`
        """
        res                     = {}
        for con_type, type_keys in context_keys.items():
            if con_type not in self.context.keys():
                logger.warning(f"Invalid context type: {con_type}")
                continue 

            res[con_type]       = []
            for con_key in type_keys:
                if con_key not in self.context[con_type].keys():
                    logger.warning(f"Invalid context key {con_key} for {con_type}.")
                    continue

                res[con_type].append(self.context[con_type][con_key])

        return { "context": res }
