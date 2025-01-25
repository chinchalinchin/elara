"""
objects.config
--------------

Object for managing application configuration.
"""

import json 
import logging
import os
import typing

logger                                      = logging.getLogger(__name__)

HIDE                                        = ["GEMINI", "REPO"]
"""Configuration properties that should be hidden from logging due to their sensitive nature."""


class Config:
    """
    Application configuration. Loads values from the ``data/config.json`` and then applies environment variable overrides.
    """

    data                                    = None
    """Config data"""
    
    file                                    = None
    """Location of Config file"""


    def __init__(self, 
        config_file                         : str
    )                                       -> None:
        """
        Initialize Config class object.

        :param config_file: Location of application configuration file.
        :type config_file: str
        """
        self.file                           = config_file
        self._load()
        self._override()


    def _load(self)                         -> None:
        """
        Load in configuration data from file.
        """
        try:
            with open(self.file, "r") as f:
                content                     = f.read()

            if content:
                self.data                   = json.loads(content)
                return 
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Application configuration not found: {e}!")

        raise ValueError("Application configuration is empty!")


    def _override(self)                     -> None:
        """
        Override configuration with environment variables, if applicable.
        """
        env_overrides                       = self.data["OVERRIDES"]

        for key, env_var in env_overrides.items():
            default                         = self.unnest(key.split("."), self.data)
            value                           = self._env(env_var, default)
            
            if value != default:
                self.nest(key.split("."), self.data, value)


    @staticmethod
    def _env(
        env_var                             : str, 
        default                             : str
    )                                       -> typing.Any:
        """
        Pull environment variables and parse into Python data structures.

        :returns: Parsed environment variable or default value.
        :rtype: `typing.Any`
        """
        value = os.environ.get(env_var)

        if value is not None:

            if isinstance(default, bool):
                return value.lower() == "true"
            
            if isinstance(default, int):
                try:
                    return int(value)
                
                except ValueError:
                    logger.error(
                        f"Environment variable {env_var} must be int! Using default value."
                    )
                    return default
            
            if isinstance(default, float):
                try:
                    return float(value)
                
                except ValueError:
                    logger.error(
                        f"Environment variable {env_var} must be float! Using default value."
                    )
                    return default 
                
            return value
        return default 
    
    
    @staticmethod
    def unnest(
        keys                                : list, 
        target                              : dict,
        default                             : typing.Any = None
    )                                       -> typing.Any:
        """
        Recursively retrieves a value from a nested dictionary.

        :param keys: List of keys to traverse in dictionary tree.
        :type keys: `list`
        :param target: Dictionary to traverse.
        :type target: `dict`
        :param default: Default value to set for endpoint.
        :type default: `typing.Any`
        :returns: Value found at node or default value.
        :rtype: `typing.Any`
        """
        for k in keys:
            if isinstance(target, dict) and k in target:
                target                      = target[k]
            else:
                return default
        return target
    

    @staticmethod
    def nest(
        keys                                : list, 
        target                              : dict,
        value                               : typing.Any
    )                                       -> None:
        """
        Recursively sets a value in a nested dictionary.
        """
        for k in keys[:-1]:
            if k not in target:
                target[k]                   = {}
            target                          = target[k]
        target[keys[-1]]                    = value


    def vars(self)                          -> dict:
        """
        Get a dictionary of the application configuration for templating.

        :returns: A dictionary of the application configuration.
        :rtype: dict
        """
        return { k: v for k,v in self.data.items() if k not in HIDE }
    

    def save(self)                          -> bool:
        """
        Saves the cache to the JSON file in ``data`` directory.

        :returns: Flag signalling if save was successful.
        :rtype: `bool`
        """
        try:
            with open(self.file, "w") as f:
                json.dump(self.data, f, indent=4)
            return True
        
        except Exception as e:
            logger.error(f"Error saving config: {e}")
            return False
    

    def get(self, 
        key                                 : str, 
        default                             : str = None
    )                                       -> str:
        """
        Retrieve an application configuration property.

        :param key: Property to retrieve.
        :type key: str
        :param default: Default value if no property is found.
        :type default: str
        :returns: Application property.
        :rtype: str
        """
        keys                                = key.split(".")
        return self.unnest(keys, self.data, default)


    def set(self, 
        key                                 : str, 
        value                               : str
    )                                       -> None:
        """
        Set an application configuration property.

        :param key: Property to set.
        :type key: str
        :param value: Value to which the property should be set.
        :type value: str
        """
        keys                                = key.split(".")
        self.nest(keys, self.data, value)


    def update(self, **kwargs)              -> None:
        """
        Update the Config using keyword arguments. Key must exist in Config to be updated.
        """
        for key, value in kwargs.items():
            if key not in self.data:
                continue 

            if isinstance(self.data[key], list) and isinstance(value, list):
                self.data[key].extend(value)
                continue 

            if isinstance(self.data[key], dict) and isinstance(value, dict):
                self.data[key].update(value)
                continue

            self.data[key] = value


    def tuning_enabled(self):
        """
        Returns a bool flag signaling models should be tuned.
        """
        return self.get("MODEL.TUNING") == "enabled"


    def language_modules(self):
        """
        Return a list of enabled Language modules.
        """
        modules = self.get("LANGUAGE.MODULES")

        if any(v for v in modules.values()):
            return [ k.lower() for k,v in modules.items() if v ]
        
        return []