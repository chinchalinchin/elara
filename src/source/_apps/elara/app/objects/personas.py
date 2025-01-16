""" # objects.persona
Object for managing Persona initialization and data.
"""
# Standard Library Modules
import os
import json

# Application Modules 
import conf 

class Personas:
    current = None
    """Current persona"""
    inst = None
    """Singleton instance"""
    personas = None
    """Persona metadata"""

    def __init__(
        self, 
        current = conf.PERSONAS["DEFAULTS"]["CHAT"],
        tune_dir = conf.CACHE["DIR"]["TUNING"],
        sys_dir = conf.CACHE["DIR"]["SYSTEM"],
        tune_ext = ".json",
        sys_ext = ".json"
    ):
        """
        Initialize *Personas* object.

        :param current: Initial persona for model to assume. Defaults to the value of the ``GEMINI_PERSONA`` environment variable.
        :type current: str
        :param tune_dir: Directory containing tuning data. Defaults to ``data/tuning``
        :type tune_dir: str
        :param tune_ext: Extension for tuning data. Defaults to ``.json``.
        :param sys_ext: Extension for the system instructions data. Defaults to ``.txt``
        """
        self.current = None
        self.personas = { }
        self._load(
            tune_dir, tune_ext, 
            sys_dir, sys_ext,
            current
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
                Personas, 
                self
            ).__new__(self)
        return self.inst
    
    def _load(
        self, 
        tune_dir : str , 
        tune_ext : str,
        sys_dir : str,
        sys_ext : str,
        current : str
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

        self.current = self.personas[persona]

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
    
    def tuning(self) -> list:
        """
        Get persona tuning data.

        :returns: Persona tuning data.
        :rtype: list(dict)
        """
        return self.current["TUNING"]
    
    def system(self) -> str:
        """
        Get persona system instructions.

        :return: Persona system instructions
        :rtype: str
        """
        return self.current["SYSTEM"]
    
    def all(self) -> list:
        """
        Get all personas.

        :returns: Persona names
        :rtype: list
        """
        return [ k for k in self.personas.keys() ]
