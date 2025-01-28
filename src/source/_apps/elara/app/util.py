"""
util.py
-------

Static application utilities.
"""
# Standard Library Modules
import ast
import logging
import typing
import re


logs                        = logging.getLogger(__name__)


def sanitize(s: str) -> str:
    """
    Sanitize a string of escape characters.
    """
    # @DEVELOPMENT
    #   This is where we have to clean up Milton's mess. 
    #   (I bet you he complains about the regex...)
    return re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]", "", s)


def lower(d: dict) -> dict:
    """
    Convert the keys of a dictionary to lowercase.

    :param d: Dictionary with string keys.
    :type d: `dict`
    :returns: Dictionary with lowercase keys.
    :rtype: `dict`
    """
    return { k.lower(): v for k, v in d.items() }


def map(typed_string: str) -> typing.Any:
    """
    Maps type strings to Python types.
    
    :param type_string: String containing a Python data type.
    :type type_string: `str`
    :returns: Python type that corresponds to input string.
    :rtype: `typing.Any`
    """
    types                   = {
      'str'                 : str,
      'dict'                : dict,
      'list'                : list,
      'int'                 : int,
      'float'               : float,
      'bool'                : bool,
      'set'                 : set
    }
    if typed_string not in types.keys():
        return None

    return types[typed_string]    
    

def unnest(keys: list, target: dict, default: typing.Any = None) -> typing.Any:
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


def nest(keys: list, target: dict, value: typing.Any) -> None:
    """
    Recursively sets a value in a nested dictionary.
    """
    for k in keys[:-1]:
        if k not in target:
            target[k]       = {}
        target              = target[k]
    target[keys[-1]]        = value
    return target


def merge(d1: dict, d2: dict) -> dict:
    """
    Recursively merges two dictionaries using the union operator (|).

    :param d1: First dictionary to merge.
    :type d1: dict 
    :param d2: Second dictionary to merge.
    :type d2: dict 
    """
    if not isinstance(d1, dict):
        raise ValueError("d1 is not a dictionary!")
    
    if not isinstance(d2, dict):
        raise ValueError("d2 is not a dictionary!")

    result                  = d1 | d2

    for key in result.keys():
        if key in d1 and key in d2:
            result[key]     = merge(d1[key], d2[key])
            
    return result


def logger(schema : str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
           file: str = None, level: str = "INFO")  -> logging.Logger:
    """
    Configure application logging

    :param schema: Schema for logs
    :type schema: `str`
    :param file: Location of log file, if logs are to be written to file.
    :type file: `str`
    :param level: Level of logs to capture.
    :type level: `str`
    """
    logger                  = logging.getLogger()

    if level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        logger.setLevel(level)
    else:
        logger.setLevel("INFO") 

    formatter               = logging.Formatter(schema)

    if file is not None:
        file_handler        = logging.FileHandler(file)
        file_handler.setLevel(level) 
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler         = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
