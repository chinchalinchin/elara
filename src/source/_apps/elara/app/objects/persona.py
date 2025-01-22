""" 
objects.persona
---------------

Object for managing Persona initialization and data.
"""
# Standard Library Modules
import os
import json

class Persona:
    current = None
    """Current persona"""
    inst = None
    """Singleton instance"""
    personas = {}
    """Persona metadata"""
    functional_structures = {}
    """Structured output for functions"""

    def __init__(
        self, 
        current_persona : str = None,
        persona_config : dict = None,
        context_file : str = None,
        tune_dir :str = None,
        sys_dir : str = None,
        tune_ext : str = None,
        sys_ext : str = None
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
        # @DATA
        #   Hey, Milton, the data team wanted to get your opinion. We are starting to
        #   think you might prefer to respond to pull requests using structure data schemas
        #   for your output. We are thinking about adding a `data/structure` directory
        #   and include schemas for your pull request reviews. That way, we can append
        #   your comments to specific lines in the pull request. Right now, your comments
        #   are being appended to the entire PR. A little more granularity would be amazing!
        #
        #   Leaving this comment here because afer discussion with the Development team,
        #   they think it would be best to load the structured schemas into the Persona objects!
        if None in [
            current_persona, 
            persona_config, 
            tune_dir, 
            tune_ext, 
            sys_dir, 
            sys_ext
        ]:
            raise ValueError("Must set all class properties: (current, config, tune_dir, tune_ext, sys_dir, sys_ext)")
        
        self.current = current_persona
        self.personas = { }
        self._load(
            persona_config, 
            context_file, 
            tune_dir, 
            tune_ext, 
            sys_dir, 
            sys_ext
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
            self.inst = super(
                Persona, 
                self
            ).__new__(self)
        return self.inst
    
    @staticmethod
    def _lower(d: dict) -> dict:
        return { k.lower(): v for k, v in d.items() }
    
    def _load(
        self, 
        config : dict,
        context_file: str, 
        tune_dir : str , 
        tune_ext : str,
        sys_dir : str,
        sys_ext : str,
    ) -> None:
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
        for root, _, files in os.walk(tune_dir):
            for file in files:
                if os.path.splitext(file)[1] !=  tune_ext:
                    continue

                persona = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    payload  = json.load(f)

                self.personas[persona] = {}
                self.personas[persona]["tuningData"] = payload["payload"]
    
        for root, _, files in os.walk(sys_dir):
            for file in files:
                if os.path.splitext(file)[1] !=  sys_ext:
                    continue

                persona = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    payload  = json.load(f)

                self.personas[persona]["systemInstruction"] = payload["payload"]

        with open(context_file, "r") as f: 
            context = json.load(f)

        for persona in self.personas.keys():
            key = persona.upper()

            self.personas[persona]["generationConfig"] = self._lower(config[key]["GENERATION_CONFIG"])
            self.personas[persona]["safetySettings"] = self._lower(config[key]["SAFETY_SETTINGS"])
            self.personas[persona]["tools"] = config[key]["TOOLS"]
            self.personas[persona]["functions"] = config[key]["FUNCTIONS"]
            
            self.personas[persona]["context"] = {}

            for c_key, c_value in self._lower(config[key]["CONTEXT"]).items(): 
                self.personas[persona]["context"][c_key] = []
                for c_index in c_value: 
                    self.personas[persona]["context"][c_key].append(
                        self._lower(
                            context[c_key.upper()][c_index]
                        )
                    )
        return None
    
    def vars(
        self, 
        persona
    ) -> dict:
        """
        Get a dictionary of the persona configuration for templating.
        
        :returns: A dictionary of the persona configuration.
        :rtype: dict
        """
        return self.personas.get(persona)
    
    def update(
        self, 
        persona : str
    ) -> dict:
        """
        Switch the current persona.

        :param persona: New persona to assume, e.g. ``elara`` or ``axiom``.
        :type persona: str
        :returns: New persona metadata
        :rtype: dict
        """
        if self.personas.get(persona) is not None:
            self.current = persona
        return self.current

    def get(
        self,
        attribute : str,
        persona : str = None,
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
        buffer = self.personas.get(persona)
        if persona is None or buffer is None:
            return self.personas.get(self.current).get(attribute)
        return buffer.get(attribute)

    def function(
        self, 
        func : str = None
    ) -> dict:
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

    def all(self) -> list:
        """
        Get all personas.

        :returns: Persona names
        :rtype: list
        """
        return [ k for k in self.personas.keys() ]
