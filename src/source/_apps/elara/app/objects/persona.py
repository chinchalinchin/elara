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
    personas = None
    """Persona metadata"""

    def __init__(
        self, 
        current = None,
        config = None,
        tune_dir = None,
        sys_dir = None,
        tune_ext = None,
        sys_ext = None
    ):
        """
        Initialize Persona object.

        :param current: Initial persona for model to assume. Defaults to the value of the ``GEMINI_PERSONA`` environment variable.
        :type current: str
        :param tune_dir: Directory containing tuning data. Defaults to ``data/tuning``
        :type tune_dir: str
        :param tune_ext: Extension for tuning data. Defaults to ``.json``.
        :param sys_ext: Extension for the system instructions data. Defaults to ``.txt``
        """
        if None in [current, config, tune_dir, tune_ext, sys_dir, sys_ext]:
            raise ValueError("Must set all class properties: (current, config, tune_dir, tune_ext, sys_dir, sys_ext)")
        
        self.current = None
        self.personas = { }
        self._load(
            current,
            config,
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
    
    def _load(
        self, 
        current : str,
        config : str,
        tune_dir : str , 
        tune_ext : str,
        sys_dir : str,
        sys_ext : str
    ):
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
                self.personas[persona]["TUNING"] = payload["payload"]
    
        for root, _, files in os.walk(sys_dir):
            for file in files:
                if os.path.splitext(file)[1] !=  sys_ext:
                    continue

                persona = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    payload  = json.load(f)

                self.personas[persona]["SYSTEM"] = payload["payload"]

        for persona in self.personas.keys():
            key = persona.upper()
            self.personas[persona]["GENERATION_CONFIG"] = config[key]["GENERATION_CONFIG"]
            self.personas[persona]["SAFETY_SETTINGS"] = config[key]["SAFETY_SETTINGS"]
            self.personas[persona]["TOOLS"] = config[key]["TOOLS"]
            self.personas[persona]["FUNCTIONS"] = config[key]["FUNCTIONS"]

        self.current = current

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
        self.current = self.personas[persona] 
        return self.current

    def get(self) -> dict:
        """
        Get current persona.

        :returns: Persona metadata
        :rtype: dict
        """
        return self.current
    
    def function(
        self, 
        func : str = None
    ) -> dict:
        """
        
        """
        for p in self.personas:
            if func in p["FUNCTIONS"]:
                return p
        return self.current

    def tuning(
        self,
        persona : str = None
    ) -> list:
        """
        Get persona tuning data.

        :param persona: Persona whose tuning data is to be retrieved. If no persona is provided, the current persona's tuning data will be returned.
        :type persona: str
        :returns: Persona tuning data.
        :rtype: list(dict)
        """
        if persona is None:
            return self.current["TUNING"]
        return self.personas[persona]["TUNING"]

    def system(
        self,
        persona : str = None
    ) -> str:
        """
        Get persona system instructions.

        :param persona: Persona whose system instructions are to be retrieved. If no persona is provided, the current persona's system instructions will be returned.
        :type persona: str
        :return: Persona system instructions
        :rtype: str
        """
        if persona is None:
            return self.current["SYSTEM"]
        return self.personas[persona]["SYSTEM"]
    
    def generation_config(
        self,
        persona : str = None
    ) -> str:
        """
        Get persona generation config.

        :param persona: Persona whose system instructions are to be retrieved. If no persona is provided, the current persona's system instructions will be returned.
        :type persona: str
        :return: Persona system instructions
        :rtype: str
        """
        if persona is None:
            return self.current["GENERATION_CONFIG"]
        return self.personas[persona]["GENERATION_CONFIG"]
    
    def safety_settings(
        self,
        persona : str = None
    ) -> str:
        """
        Get persona system instructions.

        :param persona: Persona whose system instructions are to be retrieved. If no persona is provided, the current persona's system instructions will be returned.
        :type persona: str
        :return: Persona system instructions
        :rtype: str
        """
        if persona is None:
            return self.current["SAFETY_SETTINGS"]
        return self.personas[persona]["SAFETY_SETTINGS"]
    
    def tools(
        self,
        persona : str = None
    ) -> str:
        """
        Get persona system instructions.

        :param persona: Persona whose system instructions are to be retrieved. If no persona is provided, the current persona's system instructions will be returned.
        :type persona: str
        :return: Persona system instructions
        :rtype: str
        """
        if persona is None:
            return self.current["TOOLS"]
        return self.personas[persona]["TOOLS"]
    
    
    def all(self) -> list:
        """
        Get all personas.

        :returns: Persona names
        :rtype: list
        """
        return [ k for k in self.personas.keys() ]
