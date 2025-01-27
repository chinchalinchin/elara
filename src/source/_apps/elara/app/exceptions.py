"""
exceptions.py
-------------

Application exceptions.
"""

class SummarizeDirectoryNotFoundError(Exception):
    """
    Raised when the ``directory`` passed to the ``directory.Directory.summarize()`` function does not exist
    """
    pass

class VCSRequestError(Exception):
    """
    Raised when an API request to the VCS backend failes.
    """
    pass