""" 
objects.cache
-------------

Object for managing application data.
"""
# Standard Library Modules
import json
import logging
import typing

# Application Modules
import properties


logger                              = logging.getLogger(__name__)


class Cache:
    """
    Application cache. Loads and persists frequently accessed application properties.

    .. important::

        The Cache class is implemented as a singleton to prevent concurrent writes to the cache file.
    """
    
    inst                            = None
    """Singleton instance"""
    data                            = None
    """Cache data"""
    file                            = None
    """Location of Cache file"""

    # Cache Properties
    _prop_mod                       = properties.CacheProps.CURRENT_MODEL.value
    _prop_per                       = properties.CacheProps.CURRENT_PERSONA.value
    _prop_pro                       = properties.CacheProps.CURRENT_PROMPTER.value
    _prop_src                       = properties.CacheProps.TUNING_MODEL.value
    _prop_mods                      = properties.CacheProps.MODELS.value

    def __init__(self, cache_file: str) -> None:
        """
        Initialize Cache.

        :param file: Location of Cache file. Defaults to ``data/cache.json``.
        :type file: str
        """
        self.file                   = cache_file
        self._load()


    def __new__(self, *args, **kwargs) -> typing.Self:
        """
        Create a Cache singleton.
        """
        if not self.inst:
            self.inst               = super(Cache, self).__new__(self)
        return self.inst
    

    def _fresh(self) -> dict:
        """
        Create a fresh Cache from an empty schema.
        """
        return {
            self._prop_mod          : None,
            self._prop_per          : None,
            self._prop_pro          : None,
            self._prop_mods         : [],
            self._prop_src          : None
        }
    
    
    def _load(self) -> None:
        """
        Loads the cache from the JSON file.
        
        """
        try:
            with open(self.file, "r") as f:
                content             = f.read()
            if content:
                self.data           = json.loads(content)
            else:
                logger.warning("Cache empty! Initializing new cache...")
                self.data           = self._fresh()
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading cache: {e}")
            self.data               = self._fresh()


    def vars(self) -> dict:
        """
        Retrieve the entire cache, ready for templating.

        :returns: A dictionary of key-value pairs.
        :rtype: dict
        """
        return self.data
    

    def get(self, attribute: str) -> str:
        """
        Retrieve attributes from the Cache. Cache properties are enumerated through `properties.CacheProp` enum.

        :param attribute: Key to retrieve from the Cache.
        :type attribute: str
        """
        try:
            return self.data[attribute]
        except KeyError:
            logger.error(f"KeyError: Attribute {attribute} not found")
            return None


    def update(self, **kwargs) -> bool:
        """
        Update the Cache using keyword arguments. Key must exist in Cache to be updated.
        """
        updated                     = False
        for key, value in kwargs.items():
            if key not in self.data.keys():
                logger.warning("Non-existent cache key!")
                continue 

            if isinstance(self.data[key], list) and isinstance(value, list):
                updated             = True
                self.data[key].extend(value)
                logger.info(f"Updating {key} = {value}")
                continue 

            if isinstance(self.data[key], dict) and isinstance(value, dict):
                updated             = True
                self.data[key].update(value)
                logger.info(f"Updating {key} = {value}")
                continue 

            updated                 = True
            self.data[key]          = value
            logger.info(f"Updating {key} = {value}")
            
        if updated:
            logger.info("Saving cache!")
            self.save()

        return updated


    def save(self) -> bool:
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
            
    
    def tuned_personas(self) -> list:
        """
        Retrieve all tuned Persona Models.
        """
        return [ m for m in self.data[self._prop_tun] ]


    def is_tuned(self, persona: str) -> bool:
        """
        Determine if Persona has been tuned or not.
        
        :param persona: Persona that needs to be tuned.
        :type persona: str
        :returns: A flag that signals if a Persona has already been tuned.
        :rtype: bool
        """
        return len([ 
            m for m in self.data[self._prop_tun] if m[
                properties.ModelProps.NAME.value
            ] == persona 
        ]) > 0