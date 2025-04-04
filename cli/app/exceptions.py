"""
exceptions.py
-------------

Application exceptions.
"""


class MissingArgument(Exception):
    """
    Raised when a function is missing a required argument.
    """
    pass


class ObjectNotInitialized(Exception):
    """
    Raised when a function requires an object that has not been initialized and injected into the application object.
    """
    pass


class DirectoryNotFoundError(Exception):
    """
    Raised when a directory does not exist
    """
    pass


class DataNotFoundError(Exception):
    """
    Raised when application data is not present.
    """
    pass 


class VCSRequestError(Exception):
    """
    Raised when an API request to the VCS backend fails.
    """
    pass


class VCSBackendError(Exception):
    """
    Raised when the VCS backend is not set to a valid value.
    """
    pass


class VCSCredentialsError(Exception):
    """
    Raised when the application cannot find the VCS credentials for the backend.
    """
    pass


class GeminiAPIKeyError(Exception):
    """
    Raised when the application cannot find the API Key for Gemini.
    """
    pass


class GeminiResponseFailure(Exception):
    """
    Raised when the Gemini Model fails to generate a response.
    """

class FactoryError(Exception):
    """
    Raised when a Factory cannot construct an object.
    """
    pass