# Standard Library Modules
import json
import logging 
import typing

logger              = logging.getLogger(__name__)


def raw_file(path) -> typing.Union[str | None]:
    try:
        with open(path, "r") as infile:
            data        = infile.read()

        return data
    
    except FileNotFoundError as e:
        logger.error(F"Error reading file {path}: {e}")
        return None

    except PermissionError as e:
        logger.error(F"Permission error reading file {path}: {e}")
        return None
    
    except Exception as e:
        logger.error(F"An unexpected error occurred while reading {path}: {e}")
        return None
    

def json_file(path: str) -> dict:
    try:
        with open(path, "r") as f:
            content = f.read()

        if content:
            return json.loads(content)
        logger.warning(
            f"No data found injection, initializing empty schema.")
        return {}

    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(
            f"Error loading JSON from {path}: {e}")
        return {}
        
    except Exception as e:
        logger.error(
            f"An unexpected error occurred loading {path}: {e}")
        return {}