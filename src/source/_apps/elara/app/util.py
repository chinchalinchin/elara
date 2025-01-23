"""
util.py
-------

Static application utilties.
"""

# Standard Library Modules
import logging
import typing

logger = logging.getLogger(__name__)

TYPE_MAP = {
    "str": str, 
    "int": int,
    "float": float, 
    "bool": bool
}

def map(
    type_string: str
) -> typing.Union[str, int, float, bool]:
    """
    Maps type strings to Python types.
    
    :param type_string: String containing a Python data type.
    :type type_string: str
    :returns: Python type that corresponds to input string.
    :rtype: typing.Union[str, int, float, bool]
    """

    if type_string not in TYPE_MAP:
        raise ValueError(f"Invalid type: {type_string}")
    
    return TYPE_MAP[type_string]

def validate(
    value: typing.Any
) -> typing.Union[str, int, float, bool ]:
    """
    Validate the data type of a value.

    :param value: The value to be validated.
    :type value: typing.Any
    :returns: Validated value.
    :rtype: typing.Union[str, int, float, bool]
    """
    if isinstance(value, int):
        try:
            return int(value)
        except ValueError:
            logger.error(f"Invalid value type: {value} not a integer")

    elif isinstance(value, float):
        try: 
            return float(value)
        except ValueError:
            logger.error(f"Invalid value type: {value} not a float")
    
    elif isinstance(value, str):
        if value.lower() == "true":
           return True
        if value.lower() == "false":
           return False
        return value
    
    return None

def merge(
    dict1: dict, 
    dict2: dict
) -> dict:
    """
    Recursively merges two dictionaries using the union operator (|).

    :param dict_1: First dictionary to merge.
    :type dict_1: dict 
    :param dict_2: Second dictionary to merge.
    :type dict_2: dict 
    """
    if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
        return dict2  # Or handle as an error, depending on your needs

    result = dict1 | dict2
    for key in result.keys():
        if key in dict1 and key in dict2:
            result[key] = merge(dict1[key], dict2[key])
    return result