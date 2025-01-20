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
    value_type = type(value)

    if value_type == int:
        try:
            return int(value)
        except ValueError:
            logger.error(f"Invalid value type: {value} not a integer")

    elif value_type == float:
        try: 
            return float(value)
        except ValueError:
            logger.error(f"Invalid value type: {value} not a float")
    
    elif value_type == bool:
        return value.lower() == "true"
    
    elif value_type:
        return value
    
    return None