"""
util.py
-------

Static application utilities.
"""
# Standard Library Modules
import logging
import typing
import re


logs                        = logging.getLogger(__name__)


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
