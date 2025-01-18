""" 
objects.directory
-----------------

Object for managing local directories and filesystems
"""
# Standard Library Modules
import os
import pathlib
import subprocess

class TreeCommandNotFoundError(Exception):
    """
    Raised when the 'tree' command is not found.
    """
    pass

class TreeCommandFailedError(Exception):
    """
    Raised when the 'tree' command returns a non-zero exit code.
    """
    pass

class SummarizeDirectoryNotFoundError(Exception):
    """
    Raised when the ``directory`` passed to the ``summarize()`` function does not exist
    """
    pass

class MiltonIsADoodyHead(Exception):
    """
    Raised when Milton is a doody head.
    """
    pass

class Directory:

    def __init__(
        self
    ):
        """
        Initialize Model object.
        """
        # TODO: do something
        return