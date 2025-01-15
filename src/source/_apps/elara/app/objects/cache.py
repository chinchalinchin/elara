""" objects.cache
Object for managing application data.
"""

import conf 
import json

class Cache:
    inst = None
    """Singleton instance"""
    data = None
    """Cache data"""
    file = None
    """Location of Cache file"""

    def __init__(
        self, 
        file = conf.PERSIST["FILE"]["CACHE"]
    ):
        """
        Initialize Cache.

        :param file: Location of Cache file. Defaults to ``data/cache.json``.
        :type file: str
        """
        self.file = file
        self._load()

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        """
        Create a Cache singleton.
        """
        if not self.inst:
            self.inst = super(
                Cache, 
                self
            ).__new__(self, *args, **kwargs)
        return self.inst
    
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

    def get(self, attribute):
        """
        Retrieve attributes from the Cache. Cache keys are given below,

        - tuningModel
        - currentModel
        - currentPrompter
        - currentPersona
        - tunedModels
        - basedModels

        :param attribute: Key to retrieve from the Cache.
        :type attribute: str
        """
        return self.data[attribute]

    def update(self, **kwargs):
        """
        Update the Cache using keyword arguments. Key must exist in Cache to be updated.
        """
        for key, value in kwargs.items():
            if key not in self._data:
                continue 

            if isinstance(self._data[key], list):
                self._data[key].extend(value)
                continue

            self._data[key] = value 
    
    def save(self):
        """
        Saves the cache to the JSON file in ``data`` directory.
        """
        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=4)
        return True
    
    def base_models(self, path=True):
        """
        Retrieve the base Gemini models. 

        :param path: If ``path=True`` the full model name will be returned. If ``path=False``, the short name of the model will be returned.
        """
        if path:
            return [ model["path"] for model in self.data["baseModels"] ]
        return [ model["tag"] for model in self.data["baseModels"] ]
    
    def tuned_personas(self):
        """
        Retrieve all tuned Persona Models.
        """
        return [ m for m in self.data["tunedModels"] ]

    def is_tuned(self, persona):
        """
        Determine if Persona has been tuned or not.
        
        :param persona: Persona that needs to be tuned.
        :type persona: str
        :returns: A flag that signals if a Persona has already been tuned.
        :rtype: bool
        """
        return len([ 
            m 
            for m 
            in self.data["tunedModels"] 
            if m["name"] == persona 
        ]) > 0