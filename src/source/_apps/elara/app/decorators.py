# Standard Library Imports
import logging 
import time
import traceback
import typing

# External Libraries
import requests

# Application Modules
import exceptions


logger                      = logging.getLogger(__name__)


def backoff(service: str ="github", max_retries: int = 3) -> typing.Any:
    """
    Wrap a service call in exponential backoff error handling.

  :param callable: Service call function.
  :type callable: `typing.Callable`
  :param service: Name of the service being wrapped.
  :type service: `str`
  :param max_retries: Number of calls to make before failing the request. Defaults to 3.
  :type max_retries: `int`
    """
    def caller(func):
        def wrapper(*args, **kwargs):  # Add *args and **kwargs here
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)  # Pass args and kwargs to callable
                except requests.exceptions.RequestException as e:
                    if attempt < max_retries - 1:
                        wait    = 2 ** attempt
                        logger.warning(f"Request failed, retrying in {wait} seconds:\n\n{e}")
                        time.sleep(wait)
                    else:
                        logger.error(
                            f"Request failed after {max_retries} attempts:\n\n{e}\n\n{traceback.format_exc()}")
                        return {
                            "service":          {
                                "name"          : service,
                                "body"          : e.response.text,
                                "status"        : "failure"
                            }
                        }
                        
                except Exception as e:
                    logger.error(
                        f"An unexpected error occurred:\n\n{e}\n\n{traceback.format_exc()}")
                    raise exceptions.VCSRequestError("Request failed")
        return wrapper
    return caller