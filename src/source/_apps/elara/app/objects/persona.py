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
import util

logger                                      = logging.getLogger(__name__)

class Persona:
    current                                 = None
    """Current persona"""
    inst                                    = None
    """Singleton instance"""
    personas                                = {}
    """Persona metadata"""
    functional_structures                   = {}
    """Structured output for functions"""

    def __init__(
        self, 
        current_persona                     : str,
        persona_config                      : dict,
        context_file                        : str,
        tune_dir                            : str,
        sys_dir                             : str,
        tune_ext                            : str,
        sys_ext                             : str
    ):
        """
        Initialize Persona object.

        :param current_persona: Initial persona for model to assume. 
        :type current_persona: str
        :param persona_config: Persona configuration.
        :type persona_config: dict
        :param tune_dir: Directory containing tuning data.
        :type tune_dir: str
        :param tune_ext: File xtension for tuning data.
        :type tune_ext: str
        :param sys_dir: Directory containg system instructions.
        :type sys_dir: str
        :param sys_ext: File extension for the system instructions data.
        :type sys_ext: str
        """
        self.current                        = current_persona
        self.personas                       = { }
        self._load(
            persona_config                  = persona_config, 
            context_file                    = context_file, 
            tune_dir                        = tune_dir, 
            tune_ext                        = tune_ext, 
            sys_dir                         = sys_dir, 
            sys_ext                         = sys_ext
        )

    def __new__(
        self,
        *args, 
        **kwargs
    ):
        """
        Create *Personas* singleton.
        """
        if not self.inst:
            self.inst                       = super(
                Persona, 
                self
            ).__new__(self)
        return self.inst
    
    @staticmethod
    def _process(
        dir : str, 
        ext : str,
        prop : str,
        default : str,
        temp : str = "_new"
    ):
        """
        """
        raw = {}
        for root, _, files in os.walk(dir):
            for file in files:
                persona, ext                = os.path.splitext(file)

                if ext !=  ext or persona == temp:
                    continue

                file_path                   = os.path.join(root, file)
                raw[persona]                = { }

                try:
                    with open(file_path, "r") as f:
                        content             = f.read()

                    if content:
                        payload             = json.loads(content)
                    else: 
                        payload             = { "payload": default }

                    raw[persona][prop]      = payload["payload"]

                except (FileNotFoundError, json.JSONDecodeError) as e:
                    logger.error(
                        f"Error loading JSON data from {file_path}: {e}"
                    )
                    raw[persona][prop]      = default
                    
                except Exception as e:
                    logger.error(
                        f"An unexpected error occurred while loading from {file_path}: {e}"
                    )
                    raw[persona][prop]      = default
        return raw

                
    def _load(
        self, 
        persona_config                      : dict,
        context_file                        : str, 
        tune_dir                            : str , 
        tune_ext                            : str,
        sys_dir                             : str,
        sys_ext                             : str,
    )                                       -> None:
        """
        Load *Personas* into runtime.

        :param tune_dir: The directory containing the tuning data.
        :type tune_dir: str
        :param tune_ext: The file extension for the tuning data.
        :type tune_ext: str
        :param sys_dir: The directory containing the system instructions data.
        :type sys_dir: str
        :param sys_ext: The file extension for the system instructions data.
        :type sys_ext: str
        :param current: Persona to initialize
        :type current: str
        """
        tuning                              = self._process(
            dir                             = tune_dir, 
            ext                             = tune_ext,
            prop                            = "tuningData",
            default                         = []
        )
        system                              = self._process(
            dir                             = sys_dir, 
            ext                             = sys_ext,
            prop                            = "systemInstruction",
            default                         = []
        )

        self.personas                       = util.merge(
            dict1                           = tuning, 
            dict2                           = system
        )

        with open(context_file, "r") as f: 
            context                         = json.load(f)

        for persona in self.personas.keys():
            key                             = persona.upper()

            self.personas[persona][
                "generationConfig"
            ]                               = util.lower(persona_config[key]["GENERATION_CONFIG"])
            self.personas[persona][
                "safetySettings"
            ]                               = util.lower(persona_config[key]["SAFETY_SETTINGS"])
            self.personas[persona][
                "tools"
            ]                               = persona_config[key]["TOOLS"]
            self.personas[persona][
                "functions"
            ]                               = persona_config[key]["FUNCTIONS"]
            
            self.personas[persona][
                "context"
            ]                               = {}

            for c_key, c_value in util.lower(persona_config[key]["CONTEXT"]).items(): 
                self.personas[persona][
                    "context"
                ][c_key]                    = []

                for c_index in c_value: 
                    self.personas[persona]["context"][c_key].append(
                        util.lower(
                            d               = context[c_key.upper()][c_index]
                        )
                    )
        return None
    
    def vars(
        self, 
        persona                             : str
    )                                       -> dict:
        """
        Get a dictionary of the persona configuration for templating.
        
        :returns: A dictionary of the persona configuration.
        :rtype: dict
        """
        return self.personas.get(persona)
    
    def update(
        self, 
        persona                             : str
    )                                       -> dict:
        """
        Switch the current persona.

        :param persona: New persona to assume, e.g. ``elara`` or ``axiom``.
        :type persona: str
        :returns: New persona metadata
        :rtype: dict
        """
        if self.personas.get(persona) is not None:
            self.current                    = persona
        return self.current

    def get(
        self,
        attribute                           : str,
        persona                             : str = None,
    ) -> dict:
        """
        Get a persona's attribute. Attributes are given in the following list,

        - systemInstruction
        - tuningData
        - tools
        - safetySettings
        - generationConfig

        :param persona: Persona to retrieve. If no persona is provided, the current persona will be returned.
        :type persona: str
        :returns: Persona metadata
        :rtype: dict
        """
        buffer                              = self.personas.get(persona)
        if persona is None or buffer is None:
            return self.personas.get(self.current).get(attribute)
        return buffer.get(attribute)

    def function(
        self, 
        func                            : str = None
    )                                   -> dict:
        """
        Get the persona name associated with an application function.

        :param func: Name of the application function.
        :type func: str
        :returns: Persona metadata
        :rtype: dict
        """
        for name, persona in self.personas.items():
            if func in persona["functions"]:
                return name
            
        return self.current

    def all(self)                       -> list:
        """
        Get all personas.

        :returns: Persona names
        :rtype: list
        """
        return [ k for k in self.personas.keys() ]
