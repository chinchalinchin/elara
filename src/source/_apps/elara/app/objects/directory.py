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
import constants
import exceptions 
import loader


logger                          = logging.getLogger(__name__)


class Directory:
    """
    TODO: explain
    """
    directory                   = None
    """Local directory"""
    directory_config            = None
    """Directory summary configuration"""

    # Directory Properties
    ## Summary Properties
    _prop_sum                   = constants.DirectoryProps.SUMMARY.value
    _prop_sum_root              = constants.DirectoryProps.SUMMARY_DIRECTORY.value
    _prop_sum_tree              = constants.DirectoryProps.SUMMARY_TREE.value
    _prop_sum_files             = constants.DirectoryProps.SUMMARY_FILES.value
    _prop_sum_type              = constants.DirectoryProps.SUMMARY_TYPE.value
    _prop_sum_data              = constants.DirectoryProps.SUMMARY_DATA.value
    _prop_sum_lang              = constants.DirectoryProps.SUMMARY_LANGUAGE.value
    _prop_sum_name              = constants.DirectoryProps.SUMMARY_NAME.value
    ## Configuration Properties
    _prop_sum_directives        = constants.DirectoryProps.SUMMARY_DIRECTIVES.value
    _prop_sum_includes          = constants.DirectoryProps.SUMMARY_INCLUDES.value
    _prop_sum_excludes          = constants.DirectoryProps.SUMMARY_EXCLUDES.value
    _prop_sum_ext               = constants.DirectoryProps.SUMMARY_EXCLUDE_EXT.value
    _prop_sum_file              = constants.DirectoryProps.SUMMARY_EXCLUDE_FILE.value
    _prop_sum_dir               = constants.DirectoryProps.SUMMARY_EXCLUDE_DIR.value

    def __init__(self, directory : str, directory_config : dict) -> None:
        """
        Initialize Directory object.
        
        :param dictectory: The location of the directory.
        :type directory: `str`
        :param directory_config: Summary funcion configuration.
        :type directory_config: dict
        """
        self.directory          = directory
        self.directory_config   = directory_config

    def _extensions(self):
        """
        Returns all valid extensions
        """
        return [
            k for k in self.directory_config.get(self._prop_sum)\
                                                .get(self._prop_sum_directives)\
                                                .keys()
        ] + self.directory_config.get(self._prop_sum)\
                                    .get(self._prop_sum_includes)\
                                    .get(self._prop_sum_ext)

    def _tree(self) -> str:
        """
        Reads the directory structure and returns it as a formatted string.

        :returns: A string representing the dir_ectory structure, or an error message if the directory does not exist or can't be read.
        :rtype: `str`
        """
        dir_path                = pathlib.Path(self.directory)

        if not dir_path.exists():
            raise ValueError(f"Error: Directory not found: {self.directory}")
        
        excludes_exts           = self.directory_config.get(self._prop_sum)\
                                                        .get(self._prop_sum_excludes)\
                                                        .get(self._prop_sum_ext)
        
        excludes_dirs           = self.directory_config.get(self._prop_sum)\
                                                        .get(self._prop_sum_excludes)\
                                                        .get(self._prop_sum_dir)
        try:
            structure           = ""
            for path in sorted(dir_path.rglob("*")):
                if any(part in excludes_dirs for part in path.parts):
                    continue 

                depth           = len(path.relative_to(dir_path).parts)
                indent          = "    " * depth

                if path.is_dir():
                    structure   += f"{indent}{path.name}/\n"

                elif path.suffix not in excludes_exts:
                    structure   += f"{indent}{path.name}\n"

            return structure
        
        except Exception as e:
            raise ValueError(
                f"Error reading {self.directory}:\n{e}:\n\n{traceback.format_exc()}")
    

    def summary(self) -> dict:
        """
        Generate a dictionary summary of a directory

        :returns: Dictionary summary of a directory
        :rtype: `dict`
        """
        if not os.path.isdir(self.directory):
            raise exceptions.DirectoryNotFoundError(
                f"{self.directory} does not exist."
            )
        
        dir_summary             = { }

        dir_summary[self._prop_sum] = {
            self._prop_sum_root : os.path.basename(self.directory),
            self._prop_sum_tree : self._tree(),
            self._prop_sum_files: []
        }

        file_excludes           = self.directory_config.get(self._prop_sum)\
                                                        .get(self._prop_sum_excludes)\
                                                        .get(self._prop_sum_file)
        
        directives              = self.directory_config.get(self._prop_sum)\
                                                        .get(self._prop_sum_directives)\
                                                        .keys()
        
        excludes_dirs           = self.directory_config.get(self._prop_sum)\
                                                        .get(self._prop_sum_excludes)\
                                                        .get(self._prop_sum_dir)
        i = 1
        # Use `os.walk` to recursivle scan sub-directories.
        for root, _, files in os.walk(self.directory): 
            if any(d in root for d in excludes_dirs):
                    continue 
            # traverse files in alphabetical order
            files.sort()
            
            for file in files:
                if file in file_excludes:
                    continue

                ext             = os.path.splitext(file)[1]

                if ext not in self._extensions():
                    continue

                file_path       = os.path.join(root, file)
                directive       = ext in directives

                data            = loader.raw_file(file_path)

                if not data:
                    continue 
                
                if directive:
                    dir_summary[self._prop_sum][self._prop_sum_files] += [{
                        self._prop_sum_type     
                                : "code",
                        self._prop_sum_data
                                : data,
                        self._prop_sum_lang
                                : self.directory_config.get(self._prop_sum)\
                                                        .get(self._prop_sum_directives)\
                                                        .get(ext),
                        self._prop_sum_name
                                : os.path.relpath(file_path, self.directory)
                    }]
                    continue

                dir_summary[self._prop_sum][self._prop_sum_files] += [{
                    self._prop_sum_type
                                : "raw",
                    self._prop_sum_data
                                : data,
                    self._prop_sum_name
                                : os.path.relpath(file_path, self.directory)
                }]
                
        
        return dir_summary