"""
exceptions.py
-------------

Application exceptions.
"""

class DirectoryNotFoundError(Exception):
    """
    Raised when the ``directory`` passed to the ``directory.Directory`` object does not exist
    """
    pass


class DataNotFoundError(Exception):
    """
    Raised when application data is not present.
    """
    pass 


class VCSRequestError(Exception):
    """
    Raised when an API request to the VCS backend failes.
    """
    pass