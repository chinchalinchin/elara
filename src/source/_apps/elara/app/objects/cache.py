""" 
objects.cache
-------------

Object for managing application data.
"""

import json
import logging
import typing

logger                                      = logging.getLogger(__name__)

class Cache:
    """
    Application cache. Loads and persists frequently accessed application properties.
    """
    
    inst                                    = None
    """Singleton instance"""
    data                                    = None
    """Cache data"""
    file                                    = None
    """Location of Cache file"""

    def __init__(
        self, 
        cache_file                          : str
    )                                       -> None:
        """
        Initialize Cache.

        :param file: Location of Cache file. Defaults to ``data/cache.json``.
        :type file: str
        """
        self.file                           = cache_file
        self._load()


    def __new__(self, *args, **kwargs)      -> typing.Self:
        """
        Create a Cache singleton.
        """
        if not self.inst:
            self.inst                       = super(
                t                           = Cache, 
                obj                         = self
            ).__new__(self)
        return self.inst
    

    @staticmethod
    def _fresh()                            -> dict:
        """
        Create a fresh Cache from an empty schema.
        """
        return {
            "currentModel"                  :  None,
            "currentPersona"                : None,
            "currentPrompter"               : None,
            "tunedModels"                   : [],
            "tuningModel"                   : None
        }
    
    
    def _load(self)                         -> None:
        """
        Loads the cache from the JSON file.
        
        """
        try:
            with open(self.file, "r") as f:
                content                     = f.read()
            if content:
                self.data                   = json.loads(content)
            else:
                self.data                   = self._fresh()
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading cache: {e}")
            self.data                       = self._fresh()


    def vars(self)                          -> dict:
        """
        Retrieve the entire cache, ready for templating.

        :returns: A dictionary of key-value pairs.
        :rtype: dict
        """
        return self.data
    

    def get(self, 
        attribute                           : str
    )                                       -> str:
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
        try:
            return self.data[attribute]
        except KeyError:
            logger.error(f"KeyError: Attribute {attribute} not found")
            return None


    def update(self, **kwargs)              -> bool:
        """
        Update the Cache using keyword arguments. Key must exist in Cache to be updated.
        """
        updated = False
        for key, value in kwargs.items():
            if key not in self.data:
                continue 

            if isinstance(self.data[key], list) and isinstance(value, list):
                updated                     = True
                self.data[key].extend(value)
                continue 

            if isinstance(self.data[key], dict) and isinstance(value, dict):
                updated                     = True
                self.data[key].update(value)
                continue 

            updated                         = True
            self.data[key]                  = value
            
        return updated


    def save(self)                          -> bool:
        """
        Saves the cache to the JSON file in ``data`` directory.
        """
        try:
            with open(self.file, "w") as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Error saving cache: {e}")
            return False
            
    
    def base_models(self, 
        path : bool                         = True
    )                                       -> list:
        """
        Retrieve the base Gemini models. 

        :param path: If ``path=True`` the full model name will be returned. If ``path=False``, the short name of the model will be returned.
        :type path: bool
        """
        if "baseModels" not in self.data:
            return []
        
        if path:
            return [ model["path"] for model in self.data["baseModels"] ]
        
        return [ model["tag"] for model in self.data["baseModels"] ]


    def tuned_personas(self)                -> list:
        """
        Retrieve all tuned Persona Models.
        """
        return [ m for m in self.data["tunedModels"] ]


    def is_tuned(self, 
        persona                             : str
    )                                       -> bool:
        """
        Determine if Persona has been tuned or not.
        
        :param persona: Persona that needs to be tuned.
        :type persona: str
        :returns: A flag that signals if a Persona has already been tuned.
        :rtype: bool
        """
        return len([ 
            m for m in self.data["tunedModels"] if m["name"] == persona 
        ]) > 0