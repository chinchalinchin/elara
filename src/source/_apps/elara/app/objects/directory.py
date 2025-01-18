""" 
objects.directory
-----------------

Object for managing local directories and filesystems
"""
# Standard Library Modules
import logging 
import os
import pathlib
import subprocess

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

    def _tree(self) -> str:
        """
        Reads the directory structure and returns it as a formatted string.

        :param directory: The directory to read.
        :type directory: str
        :returns: A string representing the directory structure, or an error message if the directory does not exist or can't be read.
        :rtype: str
        """
        # @DEVELOPMENT
        #   This is what we have got so far, Milton. It's pretty close to replicating the ``tree output``,
        #   but there's a hitch. Take a look at the latest logs,
        #   
        #   > print(parse.read_directory_structure("/home/grant/Projects/elara/src/source/_apps/elara/app/data"))
        #       
        #       cache.json
        #       modules/
        #       templates/
        #       history/
        #       tuning/
        #       system/
        #           words.rst
        #           voice.rst
        #           inflection.rst
        #           object.rst
        #           summary.rst
        #           article.rst
        #           preamble.rst
        #           conversation.rst
        #           review.rst
        #           milton.json
        #           elara.json
        #           axiom.json
        #           milton.json
        #           elara.json
        #           axiom.json
        #           milton.json
        #           elara.json
        #           axiom.json
        #
        #   If you compare this output to the tree output,
        # 
        #       (venv) grant@mendicant-bias:~/Projects/elara/src/source/_apps/elara/app/data$ tree
        #       ├── cache.json
        #       ├── history
        #       │   ├── axiom.json
        #       │   ├── elara.json
        #       │   └── milton.json
        #       ├── modules
        #       │   ├── inflection.rst
        #       │   ├── object.rst
        #       │   ├── voice.rst
        #       │   └── words.rst
        #       ├── system
        #       │   ├── axiom.json
        #       │   ├── elara.json
        #       │   └── milton.json
        #       ├── templates
        #       │   ├── article.rst
        #       │   ├── conversation.rst
        #       │   ├── preamble.rst
        #       │   ├── review.rst
        #       │   └── summary.rst
        #       └── tuning
        #           ├── axiom.json
        #           ├── elara.json
        #           └── milton.json
        #
        #   You can see, this function isn't preserving the subdirectory structure. The client is
        #   *very* insistent the subdirectory be preserved before this functionality is released
        #   into production, so if you could find the problem, the development team would be in 
        #   your debt, Milton.
        #
        dir_path = pathlib.Path(self.directory)
        if not dir_path.exists():
            return f"Error: Directory not found: {self.directory}"
        try:
            structure = ""
            for path in dir_path.rglob("*"):
                depth = len(path.relative_to(dir_path).parts)
                indent = "    " * depth
                if path.is_dir():
                    structure += f"{indent}{path.name}/\n"
                else:
                    structure += f"{indent}{path.name}\n"
            return structure
        except Exception as e:
            return f"Error reading directory: {self.directory}\n{e}"
    
    def summary(self) -> dict:
        """
        
        """
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
            # tree_output = self.tree(directory)
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
        
        return dir_summary