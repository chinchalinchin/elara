"""
objects.config
--------------

Object for managing application configuration.
"""

import json 
import logging
import os

logger = logging.getLogger(__name__)

class Config:
    inst = None
    """Singleton instance"""
    data = None
    """Config data"""
    file = None
    """Location of Config file"""

    def __init__(
        self, 
        config_file : str
    ):
        """
        Initialize Config class object.

        :param config_file: Location of application configuration file.
        :type config_file: str
        """
        self.file = config_file
        self._load()
        self._override()

    def __new__(
        self, 
        *args, 
        **kwargs
    ):
        """
        Create Config singleton.
        """
        if not self.inst:
            self.inst = super(
                Config, 
                self
            ).__new__(self)
        return self.inst

    def _load(self):
        """
        Load in configuration data from file.
        """
        try:
            with open(self.file, "r") as f:
                content = f.read()
            if content:
                self.data = json.loads(content)
            else:
                self.data = {}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading config file: {e}")
            self.data = {}

    def _override(self):
        """
        Override configuration with environment variables, if applicable.
        """
        env_overrides = self.data["OVERRIDES"]
        for key, env_var in env_overrides.items():
            default = self.unnest(key.split("."), self.data)
            value = self.env(env_var, default)
            if value != default:
                self.nest(key.split("."), self.data, value)

    @staticmethod
    def env(key, default):
        value = os.environ.get(key)
        if value is not None:
            if isinstance(default, bool):
                return value.lower() == "true"
            if isinstance(default, int):
                try:
                    return int(value)
                except ValueError:
                    return default
            return value
        return default 
    
    @staticmethod
    def unnest(
        keys: list, 
        target : dict,
        default=None
    ):
        """
        Recursively retrieves a value from a nested dictionary.
        """
        for k in keys:
            if isinstance(target, dict) and k in target:
                target = target[k]
            else:
                return default
        return target
    
    @staticmethod
    def nest(
        keys: list, 
        target: dict,
        value
    ):
        """
        Recursively sets a value in a nested dictionary.
        """
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value

    def vars(self) -> dict:
        """
        Get a dictionary of the application configuration for templating.

        :returns: A dictionary of the application configuration.
        :rtype: dict
        """
        # Filter out attributes with sensitive values!
        return { 
            k: v 
            for k,v 
            in self.data.items()
            if k not in ["GEMINI", "REPO"]
        }
    
    def save(self):
        """
        Saves the cache to the JSON file in ``data`` directory.
        """
        try:
            with open(self.file, "w") as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Error saving config: {e}")
            return False
    
    def get(
        self, 
        key : str, 
        default : str =None
    ) -> str:
        """
        Retrieve an application configuration property.

        :param key: Property to retrieve.
        :type key: str
        :param default: Default value if no property is found.
        :type default: str
        :returns: Application property.
        :rtype: str
        """
        keys = key.split(".")
        return self.unnest(keys, self.data, default)

    def set(
        self, 
        key : str, 
        value : str
    ):
        """
        Set an application configuration property.

        :param key: Property to set.
        :type key: str
        :param value: Value to which the property should be set.
        :type value: str
        """
        keys = key.split(".")
        self.nest(keys, self.data, value)

    def update(self, **kwargs):
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
            continue

    def tuning_enabled(self):
        """
        Returns a bool flag signaling models should be tuned.
        """
        return self.get("MODEL.TUNING") == "enabled"

    def language_modules(self):
        """
        Return a list of enabled Language modules.
        """
        modules = self.data["LANGUAGE"]["MODULES"]
        if any(v for v in modules.values()):
            return [
                k.lower()
                for k,v
                in modules.items()
                if v
            ]
        return []