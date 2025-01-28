
"""
factory.py
----------

Factory object for building application objects.
"""
# Standard Library Modules
import argparse
import os
import pathlib
import typing

# Application Modules
import util
import app as apps
import objects.cache as cache
import objects.config as config
import objects.conversation as convo
import objects.directory as directory
import objects.language as language
import objects.persona as persona
import objects.model as model
import objects.repository as repository
import objects.template as template
import objects.terminal as terminal


class AppFactory:
    app                             : apps.App | None = None
    """Factory's application."""
    app_dir                         : str | None = None
    """Directory containing application."""
    config_file                     : str | None = None
    """Full path of the application's configuration file."""


    def __init__(self, rel_dir : str = "data", filename : str = "config.json") -> None:
        """
        Initialization a new application factory object.

        :param rel_dir: Directory relative to the application directory that contains the application data.
        :type rel_dir: str
        :param filename: Name of the application configuration file.
        :type filename: str
        """
        self.app_dir                = pathlib.Path(__file__).resolve().parent
        self.config_file            = os.path.join(self.app_dir, rel_dir, filename)
        self.app                    = apps.App()
        self.app.config             = config.Config(self.config_file)

        if not self.app.config.get("GEMINI.KEY"):
            raise ValueError("GEMINI_KEY environment variable not set.")


    def _path(self, parts: list) -> str:
        """
        Append the application directory to a list of relative paths. 
        
        :param parts: List of configuration paths to append to application directory.
        :type parts: list
        :returns: System formatted path.
        :rtype: str
        """
        return os.path.join(self.app_dir, 
            *[self.app.config.get(p) for p in parts ]
        )
    

    def with_cache(self) -> typing.Self:
        """
        Initialize and append a `objects.cache.Cache` object to the factory's `app.App` object.

        :returns: Updated self.
        :rtype: typing.Self
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initializing application cache...")

        cache_file              = self._path([ "TREE.DIRECTORIES.DATA", "TREE.FILES.CACHE"])
        self.app.cache          = cache.Cache(cache_file)
        return self 
    

    def with_cli_args(self) -> typing.Self:
        """
        Initialize and append `argparse.Namespace` object to the factory's `app.App` object.

        :returns: Updated self.
        :rtype: typing.Self
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initailizing application command line arguments...")

        parser                  = argparse.ArgumentParser(
            description         = self.app.config.get("INTERFACE.HELP.PARSER")
        )
    
        subparsers              = parser.add_subparsers(
            dest                = 'operation', 
            help                = self.app.config.get("INTERFACE.HELP.SUBPARSER")
        )

        arg_schema              = self.app.config.get("INTERFACE.ARGUMENTS")

        for op_config in self.app.config.get("INTERFACE.OPERATIONS"):
            op_parser           = subparsers.add_parser(
                name            = op_config["NAME"],
                help            = op_config["HELP"]
            )
            for op_arg_key in op_config["ARGUMENTS"]:
                op_arg          = arg_schema.get(op_arg_key)
                
                if any(
                    k not in self.app.config.get("INTERFACE.FIELDS") 
                    for k in op_arg.keys()
                ):
                    continue
                
                if "ACTION" in op_arg.keys():
                    op_parser.add_argument(*op_arg["SYNTAX"],
                        dest    = op_arg["DEST"],
                        help    = op_arg["HELP"],
                        action  = op_arg["ACTION"]
                    )
                    continue

                if "NARGS" in op_arg.keys():
                    op_parser.add_argument(
                        nargs   = op_arg["NARGS"],
                        default = op_arg["DEFAULT"],
                        dest    = op_arg["DEST"],
                        help    = op_arg["HELP"],
                        type    = util.map(op_arg["TYPE"])
                    )
                    continue
                
                op_parser.add_argument(*op_arg["SYNTAX"],
                    default     = op_arg["DEFAULT"],
                    dest        = op_arg["DEST"],
                    help        = op_arg["HELP"],
                    type        = util.map(op_arg["TYPE"])
                )

        self.app.arguments              = parser.parse_args()

        return self
    

    def with_conversations(self) -> typing.Self:
        """
        Initialize and append a `objects.conversation.Conversation` object to the factory's `app.App` object. 

        :returns: Updated self.
        :rtype: `typing.Self`
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initializing application conversations...")

        dirs                            = self._path(["TREE.DIRECTORIES.THREADS"])
        extension                       = self.app.config.get("TREE.EXTENSIONS.THREADS")

        self.app.conversations          = convo.Conversation(
            directory                   = dirs,
            extension                   = extension,
            convo_config                = self.app.config.get("OBJECTS.CONVERSATION")
        )
        return self
    

    def with_directory(self)            -> typing.Self:
        """
        Initialize and append a `objects.directory.Directory` object to the factory's `app.App` object. 
        
        :returns: Updated self.
        :rtype: `typing.Self`
        """
        if self.app.arguments is None:
            raise ValueError("Arguments must be initialized before Repository!")
        
        if "directory" not in vars(self.app.arguments) and self.app.logger:
            self.app.logger.warning("Directory missing from arguments, ignoring initialization.")
            return self 
        
        self.app.directory          = directory.Directory(
            directory               = self.app.arguments.directory,
            summary_file            = self.app.config.get("TREE.FILES.SUMMARY"),
            summary_config          = self.app.config.get("FUNCTIONS.SUMMARIZE")
        )
        return self 
    

    def with_language(self)             -> typing.Self:
        """
        Initialize and append a `objects.conversation.Conversation` object to the factory's `app.App` object. 
        
        :returns: Updated self.
        :rtype: `typing.Self`
        """
        self.app.language               = language.Language(
            directory                   = self._path(["TREE.DIRECTORIES.LANGUAGE"]),
            extension                   = self.app.config.get("TREE.EXTENSIONS.LANGUAGE"),
            enabled                     = self.app.config.language_modules()
        )
        return self
    

    def with_logger(self)               -> typing.Self:
        """
        Initialize and append `logging.Logger` to the factory's `app.App` object. 
        
        :returns: Updated self.
        :rtype: typing.Self
        """
        log_file                        = self._path([
            "TREE.DIRECTORIES.LOGS",
            "TREE.FILES.LOG"
        ])

        self.app.logger                 = util.logger(
            file                        = log_file,
            level                       = self.app.config.get("LOGS.LEVEL"),
            schema                      = self.app.config.get("LOGS.SCHEMA")
        )
        return self
    

    def with_model(self)                -> typing.Self: 
        """
        Initialize and append a `objects.model.Model` object to the factory's `app.App` object. 
        
        :returns: Updated self.
        :rtype: `typing.Self`
        """
        self.app.model                  = model.Model(
            api_key                     = self.app.config.get("GEMINI.KEY"),
            default_model               = self.app.config.get("GEMINI.DEFAULT"),
            tuning                      = self.app.config.get("GEMINI.TUNING.ENABLED")
        ) 
        return self


    def with_personas(self)             -> typing.Self:
        """
        Initialize and append `objects.persona.Persona` to the factory's `app.App` object. 
        
        :returns: Updated self.
        :rtype: typing.Self
        """
        if self.app.cache is None:
            raise ValueError("Cache must be initialized before Personas!")

        self.app.personas               = persona.Persona(
            persona                     = self.app.cache.get("current_persona"),
            persona_config              = self.app.config.get("OBJECTS.PERSONA"),
            directory                   = self._path(["TREE.DIRECTORIES.PERSONAS"]),
            extension                   = self.app.config.get("TREE.EXTENSIONS.PERSONAS"),
            context                     = self._path(["TREE.DIRECTORIES.DATA", "TREE.FILES.CONTEXT"])
        )
        return self
    

    def with_templates(self)            -> typing.Self:
        """
        Initialize and append a `objects.template.Template` object to the factory's `app.App` object. 
        
        :returns: Updated self.
        :rtype:`typing.Self`
        """
        self.app.templates              = template.Template(
            directory                   = self._path(["TREE.DIRECTORIES.TEMPLATES"]),
            extension                   = self.app.config.get("TREE.EXTENSIONS.TEMPLATES")
        )
        return self
    

    def with_terminal(self)             -> typing.Self:
        """
        Initialize and append a `objects.terminal.Terminal` object to the factory's `app.App` object. 
        
        :returns: Updated self.
        :rtype:`typing.Self`
        """
        self.app.terminal               = terminal.Terminal(
            terminal_config             = self.app.config.get("OBJECTS.TERMINAL")
        )
        return self


    def with_repository(self)           -> typing.Self:
        """
        Initialize and append a `objects.repo.Repo` object to the factory's `app.App` object. 
        
        :returns: Updated self.
        :rtype: typing.Self
        """
        if self.app.arguments is None:
            raise ValueError("Arguments must be initialized before Repository!")
        
        arguments                       = vars(self.app.arguments)

        if "repository" in arguments and "owner" in arguments:
            if self.app.config.get("OBJECTS.REPO.VCS") is None:
                raise ValueError("VCS backend not set.")
            
            if self.app.config.get("OBJECTS.REPO.VCS") == "github" \
                and not self.app.config.get("OBJECTS.REPO.AUTH.CREDS"):
                raise ValueError(
                    "REPO_AUTH_CREDS environment variable not set for github VCS.")
        
            self.app.repository         = repository.Repo(
                repository_config       = self.app.config.get("OBJECTS.REPO"),
                repository              = self.app.arguments.repository,
                owner                   = self.app.arguments.owner
            )

        return self
   
    
    def build(self)                     -> apps.App :
        return self.app