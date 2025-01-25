"""
util.py
-------

Static application utilities.
"""
# Standard Library Modules
import logging
import typing

TYPE_MAP                                = {
    "str"                               : str, 
    "int"                               : int,
    "float"                             : float, 
    "bool"                              : bool
}


def payload(a: typing.Any):
    return { "payload": a }


def lower(d: dict)                      -> dict:
    """
    Convert the keys of a dictionary to lowercase.

    :param d: Dictionary with string keys.
    :type d: `dict`
    :returns: Dictionary with lowercase keys.
    :rtype: `dict`
    """
    return { k.lower(): v for k, v in d.items() }

def map(
    type_string: str
) -> typing.Union[str, int, float, bool]:
    """
    Maps type strings to Python types.
    
    :param type_string: String containing a Python data type.
    :type type_string: `str`
    :returns: Python type that corresponds to input string.
    :rtype: `typing.Union[str, int, float, bool]`
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
            raise ValueError(f"Invalid value type: {value} not a integer")

    elif isinstance(value, float):
        try: 
            return float(value)
        except ValueError:
            raise ValueError(f"Invalid value type: {value} not a float")
    
    elif isinstance(value, str):
        if value.lower() == "true":
           return True
        if value.lower() == "false":
           return False
        return value
    
    return None


def merge(
    dict1                               : dict, 
    dict2                               : dict
)                                       -> dict:
    """
    Recursively merges two dictionaries using the union operator (|).

    :param dict_1: First dictionary to merge.
    :type dict_1: dict 
    :param dict_2: Second dictionary to merge.
    :type dict_2: dict 
    """
    if not isinstance(dict1, dict):
        raise ValueError("dict1 is not a dictionary!")
    
    if not isinstance(dict2, dict):
        raise ValueError("dict2 is not a dictionary!")

    result                              = dict1 | dict2

    for key in result.keys():
        if key in dict1 and key in dict2:
            result[key]                 = merge(dict1[key], dict2[key])
            
    return result


def logger(
    file                                : str = None,
    level                               : str = "INFO",
    schema                              : str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)                                       -> logging.Logger:
    """
    Configure application logging

    :param file: Location of log file, if logs are to be written to file.
    :type log_file: str
    :param app: Dictionary containing application configuration.
    :type app: dict
    """
    logger                              = logging.getLogger()

    if level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        logger.setLevel(level)
    else:
        logger.setLevel("INFO") 

    formatter                           = logging.Formatter(schema)

    if file is not None:
        file_handler                    = logging.FileHandler(file)
        file_handler.setLevel(level) 
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler                     = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
