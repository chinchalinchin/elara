""" objects.cache
Object for managing application data.
"""

import conf 
import json

class Cache:
    instance = None
    data = None
    file = None

    def __init__(
        self, 
        file = conf.PERSIST["FILE"]["CACHE"]
    ):
        self.file = file
        self._load()

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        if not self.instance:
            self.instance = super(Cache, self).__new__(self, *args, **kwargs)
        return self.instance
    
    def _load(self):
        """Loads the tuned model cache from the JSON file."""
        try:
            with open(self.file, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data  = {
                "baseModels": conf.MODEL["BASE_MODELS"],
                "tunedModels": [],
                "currentModel": conf.MODEL["BASE_MODELS"][0]["path"],
                "tuningModel": conf.DEFAULTS["SOURCE"],
                "template": {
                    "currentPersona": conf.DEFAULTS["PERSONA"],
                    "currentPrompter": conf.DEFAULTS["PROMPTER"]
                }
            }

    def get(self):
        return self.data
    
    def save(self, cache):
        """Saves the tuned model cache to the JSON file."""
        self.data = cache
        with open(self.file, "w") as f:
            json.dump(cache, f, indent=4)
