"""
objects.config
--------------

Object for managing application configuration.
"""
# Standard Library Modules
import json 
import logging
import os
import typing

# Application Modules
import properties


logger                          = logging.getLogger(__name__)


class Config:
    """
    Application configuration. Loads values from the ``data/config.json`` and then applies environment variable overrides.
    """

    data                        : dict = {}
    """Config data"""
    file                        : str = None
    """Location of Config file"""


    # Configuration Properties
    _prop_over                  = properties.ConfigProps.OVERRIDES.value


    def __init__(self, config_file: str, override: bool = True) -> None:
        """
        Initialize Config class object.

        :param config_file: Location of the configuration file.
        :type config_file: str
        :param override: Flag to apply environment variable overrides.
        :type override: `bool`
        """
        self.file               = config_file
        self._load()

        if override:
            self._override()


    def _load(self) -> None:
        """
        Load in configuration data from file.
        """
        try:
            with open(self.file, "r") as f:
                content         = f.read()

            if content:
                self.data       = json.loads(content)
                return 
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Application configuration not found: {e}!")

        raise ValueError("Application configuration is empty!")


    def _override(self, delimiter : str = ".") -> None:
        """
        Override configuration with environment variables, if applicable.
        
        :param delimiter: Mark separating nested properties.
        :type delimiter: `str`
        """
        if self._prop_over not in self.data.keys():
            return 
        
        env_overrides           = self.data[self._prop_over]

        for key, env_var in env_overrides.items():
            default             = self._unnest(key.split(delimiter), self.data)
            value               = os.environ.get(env_var, default)
            
            if value != default:
                self._nest(key.split(delimiter), self.data, value)


    @staticmethod       
    def _unnest(keys: list, target: dict, default: typing.Any = None) -> typing.Any:
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
                target          = target[k]
            else:
                return default
        return target


    @staticmethod
    def _nest(keys: list, target: dict, value: typing.Any) -> None:
        """
        Recursively sets a value in a nested dictionary.
        """
        for k in keys[:-1]:
            if k not in target:
                target[k]       = {}
            target              = target[k]
        target[keys[-1]]        = value
        return target
    

    def save(self) -> bool:
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
    

    def get(self, key: str, default: str = None, delimiter : str= "." ) -> str:
        """
        Retrieve an application configuration property.

        :param key: Property to retrieve.
        :type key: `str`
        :param default: Default value if no property is found.
        :type default: `str`
        :param delimiter: Mark separating nested properties.
        :type delimiter: `str`
        :returns: Application property.
        :rtype: `str`
        """
        keys                    = key.split(delimiter)
        return self._unnest(keys, self.data, default)


    def set(self, key: str, value: str, delimiter : str = ".") -> dict:
        """
        Set an application configuration property.

        :param key: Property to set.
        :type key: `str`
        :param value: Value to which the property should be set.
        :type value: `str`
        :param delimiter: Mark separating nested properties.
        :type delimiter: `str`
        """
        keys                    = key.split(delimiter)
        self.data               = self._nest(keys, self.data, value)
        return self.data
    
    