""" 
objects.directory
-----------------

Object for managing local directories and filesystems
"""
# Standard Library Modules
import os
import subprocess
import logging 

logger = logging.getLogger(__name__)

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
    directory = None
    summary_file = None
    summary_includes = None
    summary_directives = None

    def __init__(
        self,
        directory : str,
        summary_file : str,
        summary_includes : list,
        summary_directives: dict
    ):
        """
        Initialize Directory object.
        """
        self.directory = directory
        self.summary_file = summary_file
        self.summary_includes = summary_includes
        self.summary_directives = summary_directives
    
    def _extensions(self):
        """
        Returns all valid extensions
        """
        return [
            k for k in self.summary_directives.keys()
        ] + self.summary_includes

    def summary(self):
        output_file = os.path.join(self.directory, self.summary_file)

        if not os.path.isdir(self.directory):
            raise SummarizeDirectoryNotFoundError(
                f"{self.directory} does not exist."
            )

        try:
            # @DEVELOPMENT
            #   Hey, Milton, the client wants us to refactor this.
            #   They don't like making the application dependent on the `tree`
            #   application. They want to generate a data structure that
            #   represents the structure of ``directory`` as a dict, then
            #   they want to update the application to use this output 
            #   to render the ``data/templates/review.rst`` template.
            #   In other words, instead of injecting the raw ``tree``
            #   output into the template, they want to format the directory
            #   structure and then modify the template to generate the 
            #   git summary more gracefully. 
            #
            #   
            #   The development team is pulling their hair out trying to
            #   figure out how to implement this. We need your skill, Milton!
            #
            # tree_output = directory_tree(directory)
            tree_output = subprocess.check_output(
                ["tree", "-n", self.directory], 
                text=True
            )
        except FileNotFoundError:
            raise TreeCommandNotFoundError(
                "The 'tree' command was not found. Please install it."
            )
        except subprocess.CalledProcessError as e:
            raise TreeCommandFailedError(
                f"The 'tree' command returned a non-zero exit code: {e.returncode}"
            )
        
        dir_summary  = {
            "directory": os.path.basename(self.directory),
            "tree": tree_output,
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

                directive = ext in self.summary_directives.keys()

                try:
                    with open(file_path, "r") as infile:
                        data = infile.read()

                    if directive:
                        dir_summary["files"] += [{
                            "type": "code",
                            "data": data,
                            "lang": self.summary_directives[ext],
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