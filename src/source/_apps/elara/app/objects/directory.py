""" 
objects.directory
-----------------

Object for managing local directories and filesystems
"""
# Standard Library Modules
import logging 
import os
import pathlib
import traceback

# Application Modules
import exceptions 


logger = logging.getLogger(__name__)


class Directory:
    directory                           = None
    """Local directory"""
    summary_config                      = None
    """Summarize function configuration"""
    summary_file                        = None
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
        self.directory                  = directory
        self.summary_config             = summary_config
        self.summary_file               = summary_file

    def _extensions(self):
        """
        Returns all valid extensions
        """
        return [
            k 
            for k 
            in self.summary_config.get("DIRECTIVES").keys()
        ] + self.summary_config.get("INCLUDES").get("EXT")

    def _tree(self) -> str:
        """
        Reads the directory structure and returns it as a formatted string.

        :param directory: The directory to read.
        :type directory: str
        :returns: A string representing the directory structure, or an error message if the directory does not exist or can't be read.
        :rtype: str
        """
        dir_path = pathlib.Path(self.directory)
        if not dir_path.exists():
            raise ValueError(f"Error: Directory not found: {self.directory}")
        
        try:
            structure                   = ""

            for path in sorted(dir_path.rglob("*")):
                depth                   = len(path.relative_to(dir_path).parts)
                indent                  = "    " * depth

                if path.is_dir():
                    structure           += f"{indent}{path.name}/\n"

                elif path.suffix not in self.summary_config.get("EXCLUDES").get("EXT"):
                    structure           += f"{indent}{path.name}\n"

            return structure
        except Exception as e:
            raise ValueError(f"Error reading {self.directory}:\n{e}:\n\n{traceback.format_exc()}")
    
    def summary(self) -> dict:
        """
        Generate a dictionary summary of a directory

        :returns: Dictionary summary of a directory
        :rtype: dict
        """
        if not os.path.isdir(self.directory):
            raise exceptions.DirectoryNotFoundError(
                f"{self.directory} does not exist."
            )
        
        dir_summary                     = { }
        dir_summary["summary"]          = {
            "directory"                 : os.path.basename(self.directory),
            "tree"                      : self._tree(),
            "files"                     : []
        }

        for root, _, files in os.walk(self.directory): # Use `os.walk` to recursivle scan sub-directories.
            
            files.sort() # traverse files in alphabetical order
            for file in files:
                if file in self.summary_config.get("EXCLUDES").get("FILE"):
                    continue

                base, ext               = os.path.splitext(file)

                if ext not in self._extensions() \
                    or base == self.summary_file:
                    continue

                file_path               = os.path.join(root, file)
                directive               = ext in self.summary_config.get("DIRECTIVES").keys()

                try:
                    with open(file_path, "r") as infile:
                        data            = infile.read()

                    if directive:
                        dir_summary["summary"]["files"] += [{
                            "type"      : "code",
                            "data"      : data,
                            "lang"      : self.summary_config.get("DIRECTIVES").get(ext),
                            "name"      : os.path.relpath(file_path, self.directory)
                        }]
                        continue

                    dir_summary["summary"]["files"] += [{
                        "type"          : "raw",
                        "data"          : data,
                        "name"          : os.path.relpath(file_path, self.directory)
                    }]
                except FileNotFoundError as e:
                    logger.error(F"Error reading file {file_path}: {e}")
                    continue

                except PermissionError as e:
                    logger.error(F"Permission error reading file {file_path}: {e}")
                    continue
                
                except Exception as e:
                    logger.error(F"An unexpected error occurred while reading {file_path}: {e}")
                    continue
        
        return dir_summary