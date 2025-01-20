""" 
objects.directory
-----------------

Object for managing local directories and filesystems
"""
# Standard Library Modules
import logging 
import os
import pathlib

logger = logging.getLogger(__name__)

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
    directory = None
    """Local directory"""
    summary_config = None
    """Summarize function configuration"""
    summary_file = None
    """Summary file location"""

    def __init__(
        self,
        directory : str,
        summary_file : str,
        summary_config : dict
    ):
        """
        Initialize Directory object.
        
        :param dictectory: The location of the directory.
        :type directory: str
        :param summary_file: File to which the summary will be written.
        :type summary_file: str
        :param summary_config: Summary funcion configuration.
        :type summary_config: dict
        """
        self.directory = directory
        self.summary_config = summary_config
        self.summary_file = summary_file

    def _extensions(self):
        """
        Returns all valid extensions
        """
        return [
            k for k in self.summary_config["DIRECTIVES"].keys()
        ] + self.summary_config["INCLUDES"]

    def _tree(self) -> str:
        """
        Reads the directory structure and returns it as a formatted string.

        :param directory: The directory to read.
        :type directory: str
        :returns: A string representing the directory structure, or an error message if the directory does not exist or can't be read.
        :rtype: str
        """
        # @OPERATIONS
        #   Milton, this function is catching *.pyc files. The client
        #   wants to add an `IGNORE` property to `data/config.json` that
        #   configures which files the directory summaries ignore. We 
        #   need to make sure we aren't printing binary files, like .pyc!
        dir_path = pathlib.Path(self.directory)
        if not dir_path.exists():
            return f"Error: Directory not found: {self.directory}"
        try:
            structure = ""
            for path in sorted(dir_path.rglob("*")):
                depth = len(path.relative_to(dir_path).parts)
                indent = "    " * depth
                if path.is_dir():
                    structure += f"{indent}{path.name}/\n"
                elif path.suffix not in self.summary_config["EXCLUDES"]:
                    structure += f"{indent}{path.name}\n"
            return structure
        except Exception as e:
            return f"Error reading directory: {self.directory}\n{e}"
    
    def summary(self) -> dict:
        """
        Generate a dictionary summary of a directory

        :returns: Dictionary summary of a directory
        :rtype: dict
        """
        if not os.path.isdir(self.directory):
            raise SummarizeDirectoryNotFoundError(
                f"{self.directory} does not exist."
            )
        
        dir_summary  = {
            "directory": os.path.basename(self.directory),
            "tree": self._tree(),
            "files": []
        }

        # Use `os.walk` to recursivle scan sub-directories.
        for root, _, files in os.walk(self.directory):
            # traverse files in alphabetical order
            files.sort()
            for file in files:
                base, ext = os.path.splitext(file)

                if ext not in self._extensions() \
                    or base == self.summary_file:
                    continue

                file_path = os.path.join(root, file)

                directive = ext in self.summary_config["DIRECTIVES"].keys()

                try:
                    with open(file_path, "r") as infile:
                        data = infile.read()

                    if directive:
                        dir_summary["files"] += [{
                            "type": "code",
                            "data": data,
                            "lang": self.summary_config["DIRECTIVES"][ext],
                            "name" : os.path.relpath(file_path, self.directory)
                        }]
                        continue

                    dir_summary["files"] += [{
                        "type": "raw",
                        "data": data,
                        "name": os.path.relpath(file_path, self.directory)
                    }]

                except Exception as e:
                    logger.error(F"Error reading file {file_path}: {e}")
                    continue
        
        return dir_summary