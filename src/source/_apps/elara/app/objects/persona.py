""" 
objects.persona
---------------

Object for managing Persona initialization and data.
"""
# Standard Library Modules
import os
import json
import logging 

# Application Modules
import constants
import exceptions
import util

logger                              = logging.getLogger(__name__)


class Persona:
    directory                       : str = None
    """Directory containing persona data"""
    extension                       : str = None
    """Extension of persona data files"""
    context                         : str = None
    """Location of external context file"""
    current                         : str = None
    """Current persona"""
    personas                        : dict = {}
    """Persona metadata"""
    persona_config                  : dict = {}
    """Persona configuration"""
    schema                          : dict = {}
    """Schema for persona data"""

    # Persona properties
    _prop_tune                      = constants.PersonaProps.TUNING.value
    _prop_syst                      = constants.PersonaProps.SYSTEM_INSTRUCTION.value
    _prop_cont                      = constants.PersonaProps.CONTEXT.value
    _prop_func                      = constants.PersonaProps.FUNCTIONS.value
    _prop_tool                      = constants.PersonaProps.TOOLS.value
    _prop_gene                      = constants.PersonaProps.GENERATION_CONFIG.value
    _prop_safe                      = constants.PersonaProps.SAFETY_SETTINGS.value
    _prop_schema                    = constants.PersonaProps.SCHEMA_FILENAME.value


    def __init__(self, persona: str, persona_config: dict, 
                 directory: str, extension: str, context: str) -> None:
        """
        Initialize Persona object.

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
        self.current                    = persona
        self.directory                  = directory
        self.extension                  = extension
        self.context                    = context
        self.personas                   = { }
        self.persona_config             = persona_config
        self.schema                     = self._schema()
        self._personas()
        self._context()


    def _schema(self) -> dict:
        """
        Load a persona schema from file.

        :returns: Dictionaryschema for new conversation.
        :rtype: `dict`
        """
        schema_filename                 = self.persona_config[self._prop_schema]
        schema_file                     = "".join([schema_filename, self.extension])
        schema_path                     = os.path.join(self.directory, schema_file)
        
        try:
            with open(schema_path, "r") as f:
                content                 = f.read()

            if content:
                payload                 = json.loads(content)
                return payload

            raise exceptions.DataNotFoundError(schema_path)
            
        except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
            raise ValueError(f"Error loading JSON at {schema_path}: {e}")


    def _personas(self) -> None:
        """
        Load persona data from directory
        """
        raw = {}
        for root, _, files in os.walk(self.directory):
            for file in files:
                persona, ext            = os.path.splitext(file)

                if ext !=  self.extension or \
                    persona == self.persona_config[self._prop_schema] :
                    continue

                file_path               = os.path.join(root, file)
                raw[persona]            = { }

                try:
                    with open(file_path, "r") as f:
                        content         = f.read()

                    if content:
                        payload         = json.loads(content)
                    else: 
                        logger.warning(
                            f"No data found for {persona}, applying new schema.")
                        payload         = self.schema

                    raw[persona]        = payload

                except (FileNotFoundError, json.JSONDecodeError) as e:
                    logger.error(
                        f"Error loading JSON from {file_path}: {e}")
                    raw[persona]        = self.schema
                    
                except Exception as e:
                    logger.error(
                        f"An unexpected error occurred loading {file_path}: {e}")
                    raw[persona]        = self.schema

        self.personas                   = raw
        return

                
    def _context(self) -> None:
        """
        Apply contextual configuration to personas.

        :param context_file: Location of the context file.
        :type context_file: `str`
        """
        with open(self.context, "r") as f: 
            context                     = json.load(f)

        for persona in self.personas.keys():
            context_config              = self.personas[persona][self._prop_cont]

            for con_type, con_keys in context_config.items(): 
                
                self.personas[persona][self._prop_cont][con_type] \
                                        = []

                for con_key in con_keys: 
                    context_plugin         = context[con_type.upper()][con_key]

                    self.personas[persona][self._prop_cont][con_type]\
                                            .append(util.lower(context_plugin))
        return
    

    def vars(self, persona: str = None) -> dict:
        """
        Get a dictionary of the persona configuration for templating.
        
        :param persona: Persona whose properties are to be retrieved.
        :type persona: `str`
        :returns: A dictionary of the persona configuration.
        :rtype: `dict`
        """
        if persona is None:
            return self.personas.get(self.current)
        
        return self.personas.get(persona)
    


    def update(self, persona: str = None) -> dict:
        """
        Switch the current persona.

        :param persona: New persona to assume, e.g. ``elara`` or ``axiom``.
        :type persona: str
        :returns: New persona metadata
        :rtype: dict
        """
        if persona is None:
            persona                     = self.current

        if self.personas.get(persona) is not None:
            self.current                = persona

        return self.current


    def get(self, attribute: str, persona: str = None) -> dict:
        """
        Get a persona's attribute. Attributes are given in the following list,

        - system
        - tuning
        - tools
        - functions
        - safety_settings
        - generation_config
        - context

        :param persona: Persona whose attribute is to be retrieved. If no persona is provided, the current persona will be used.
        :type persona: `str`
        :param attribute: Persona attribute to retrieve.
        :type attribute: `str`
        :returns: Persona attribute metadata
        :rtype: `dict`
        """
        buffer                          = self.personas.get(persona)
        if persona is None or buffer is None:
            return self.personas.get(self.current).get(attribute)
        return buffer.get(attribute)


    def function(self, func: str = None) -> dict:
        """
        Get the persona name associated with an application function.

        :param func: Name of the application function.
        :type func: str
        :returns: Persona metadata
        :rtype: dict
        """
        for name, persona in self.personas.items():
            if func in persona[self._prop_func]:
                return name
            
        return self.current


    def all(self) -> list:
        """
        Get all personas.

        :returns: Persona names
        :rtype: list
        """
        return [ k for k in self.personas.keys() ]
