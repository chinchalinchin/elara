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
import properties
import exceptions
import loader


logger                              = logging.getLogger(__name__)


class Persona:
    directory                       : str = None
    """Directory containing persona data"""
    extension                       : str = None
    """Extension of persona data files"""
    current                         : str = None
    """Current persona"""
    personas                        : dict = {}
    """Persona metadata"""
    persona_config                  : dict = {}
    """Persona configuration"""
    populated                       : bool = False
    """Flag for injection population"""
    schema                          : dict = {}
    """Schema for persona data"""

    # Persona properties
    _prop_tune                      = properties.PersonaProps.TUNING.value
    _prop_syst                      = properties.PersonaProps.SYSTEM_INSTRUCTION.value
    _prop_func                      = properties.PersonaProps.FUNCTIONS.value
    _prop_tool                      = properties.PersonaProps.TOOLS.value
    _prop_gene                      = properties.PersonaProps.GENERATION_CONFIG.value
    _prop_safe                      = properties.PersonaProps.SAFETY_SETTINGS.value
    _prop_schema                    = properties.PersonaProps.SCHEMA_FILENAME.value
    _prop_context                   = properties.PersonaProps.CONTEXT.value
    _prop_inject                    = properties.PersonaProps.INJECTIONS.value

    def __init__(self, persona: str, persona_config: dict, 
                 directory: str, extension: str) -> None:
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
        self.current                = persona
        self.directory              = directory
        self.extension              = extension
        self.personas               = { }
        self.persona_config         = persona_config
        self.schema                 = self._schema()
        self._personas()


    def _schema(self) -> dict:
        """
        Load a persona schema from file.

        :returns: Dictionaryschema for new conversation.
        :rtype: `dict`
        """
        schema_filename             = self.persona_config[self._prop_schema]
        schema_file                 = "".join([schema_filename, self.extension])
        schema_path                 = os.path.join(self.directory, schema_file)
        
        try:
            with open(schema_path, "r") as f:
                content             = f.read()

            if content:
                payload             = json.loads(content)
                return payload

            raise exceptions.DataNotFoundError(schema_path)
            
        except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
            raise ValueError(f"Error loading JSON at {schema_path}: {e}")


    def _personas(self) -> None:
        """
        Load persona configuration from application directory.
        """
        for root, _, files in os.walk(self.directory):
            for file in files:
                persona, ext        = os.path.splitext(file)

                if ext !=  self.extension or \
                    persona == self.persona_config[self._prop_schema] :
                    continue

                file_path           = os.path.join(root, file)
                self.personas[persona] \
                                    = loader.json_file(file_path, self.schema)
        return


    def populate(self, injections, persona):
        """
        Populate persona injections.

        :param injections:
        :type injections: `dict`
        :param persona:
        :type persona: `str`
        """
        if self.populated:
            return 
        
        inject_keys                 = self.personas[persona][
                                        self._prop_context][self._prop_inject]

        for i_type, i_keys in inject_keys.items():
            inject_buffer           = []

            for i, content in injections[i_type].items():
                if i in i_keys:
                    inject_buffer.append(content)

            self.personas[persona][self._prop_context][self._prop_inject][i_type]\
                                    = inject_buffer

        self.populated              = True
        return 
    

    def vars(self, persona: str = None) -> dict:
        """
        Get a dictionary of the persona configuration for templating.
        
        .. note::

            This method filters out a persona's context keys. Before injected the context keys into a template, they must be converted into raw context using the `objects.context.Context` class.

        :param persona: Persona whose properties are to be retrieved.
        :type persona: `str`
        :returns: A dictionary of the persona configuration.
        :rtype: `dict`
        """
        if persona is None or not self.personas.get(persona):
            persona                 = self.current
        
        return self.personas.get(persona)


    def update(self, persona: str = None) -> dict:
        """
        Switch the current persona.

        :param persona: New persona to assume, e.g. ``elara`` or ``axiom``.
        :type persona: str
        :returns: New persona metadata
        :rtype: dict
        """
        if persona is None or self.personas.get(persona):
            persona                 = self.current

        if self.personas.get(persona) is not None:
            self.current            = persona

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
        if persona is None or self.personas.get(persona) is None:
            return self.personas.get(self.current).get(attribute)
        return self.personas.get(persona).get(attribute)


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