"""
loader.py
---------

Module for loading files.
"""
# Standard Library Modules
import json
import logging 
import typing


logger              = logging.getLogger(__name__)


def raw_file(path, default : typing.Any = None) -> typing.Any:
    """
    Load text from file.

    :param path: File path.
    :type path: `str`
    :returns: Raw file text
    :rtype: `str`
    """
    try:
        with open(path, "r") as infile:
            data    = infile.read()

        return data
    
    except FileNotFoundError as e:
        logger.error(F"Error reading file {path}: {e}")
        return default

    except PermissionError as e:
        logger.error(F"Permission error reading file {path}: {e}")
        return None
    
    except Exception as e:
        logger.error(F"An unexpected error occurred while reading {path}: {e}")
        return None
    

def json_file(path: str, default:dict = {}) -> dict:
    """
    Load a JSON from file.

    :param path: File path of JSON.
    :type path: `str`
    :returns: JSON
    :rtype: `dict`
    """
    content         = raw_file(path)

    try:
        if content:
            return json.loads(content)
        logger.warning(
            f"No data found injection, initializing empty object.")
        return default

    except json.JSONDecodeError as e:
        logger.error(
            f"Error loading JSON from {path}: {e}")
        return default