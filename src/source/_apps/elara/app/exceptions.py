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