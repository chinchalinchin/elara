""" # objects.persona
Object for managing Persona initialization.
"""
# Standard Library Modules
import os
import json

# Application Modules 
import conf 

class Persona:
    current = None
    instance = None
    personas = None

    def __init__(
        self, 
        current,
        tune_dir = conf.PERSIST["DIR"]["TUNING"],
        sys_dir = conf.PERSIST["DIR"]["SYSTEM"],
        tune_ext = ".json",
        sys_ext = ".txt"
    ):
        self.current = current
        self.personas = { }
        self._load(
            tune_dir, tune_ext, 
            sys_dir, sys_ext
        )

    def __new__(
        self,
        *args, 
        **kwargs
    ):
        if not self.instance:
            self.instance = super(
                Persona, 
                self
            ).__new__(self)
        return self.instance
    
    def _load(
        self, 
        tune_dir, 
        tune_ext,
        sys_dir,
        sys_ext
    ):
        """Load Personas"""
        for root, _, files in os.walk(tune_dir):
            for file in files:
                if os.path.splitext(file)[1] !=  tune_ext:
                    continue

                persona = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    payload  = json.load(f)

                self.personas[persona] = {}
                self.personas[persona]["TUNING"] = payload
    
        for root, _, files in os.walk(sys_dir):
            for file in files:
                if os.path.splitext(file)[1] !=  sys_ext:
                    continue

                persona = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    payload  = f.read()

                self.personas[persona]["SYSTEM"] = payload

    def update(self, persona):
        self.current = self.personas[persona] 

    def get(self):
        return self.current
