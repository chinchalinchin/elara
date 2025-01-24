
# Standard Library Modules
import argparse
import dataclasses
import logging
import os
import pathlib
import typing

# Application Modules
import util
import objects.cache as cache
import objects.config as config
import objects.conversation as conversation
import objects.directory as directory
import objects.language as language
import objects.persona as persona
import objects.model as model
import objects.repo as repo
import objects.template as template
import objects.terminal as terminal

@dataclasses.dataclass
class App:
    """
    Data structure for managing application objects.
    """
    arguments : argparse.Namespace
    cache : cache.Cache
    config : config.Config
    conversations: conversation.Conversation
    directory: directory.Directory | None
    language: language.Language
    logger : logging.Logger
    model : model.Model
    personas : persona.Persona
    repository: repo.Repo | None
    templates : template.Template
    terminal : terminal.Terminal

@dataclasses.dataclass
class Output:
    """
    Data structure for managing application output
    """
    prompt : str | None
    response : str
    summary: str | None
    vcs : str | None

class AppFactory:
    app : App                           = None
    """Factory's application."""
    app_dir : str                       = None
    """Directory containing application."""
    config_file : str                   = None
    """Full path of the application's configuration file."""

    def __init__(
        self,
        rel_dir : str                   = "data",
        filename : str                  = "config.json"
    ):
        """
        Initialization a new application factory object.

        :param rel_dir: Directory relative to the application directory that contains the application data.
        :type rel_dir: str
        :param filename: Name of the application configuration file.
        :type filename: str
        """
        self.app_dir                    = pathlib.Path(__file__).resolve().parent
        self.config_file                = os.path.join(self.app_dir, rel_dir, filename)
        self.app                        = App()
        self.app.config                 = config.Config(
            config_file                 = self.config_file
        )

        if self.app.config.get("GEMINI.KEY"):
            raise ValueError("GEMINI_KEY environment variable not set.")


    def _path(self, parts)              -> str:
        return os.path.join(
            self.app_dir,
            *[self.app.config.get(p) for p in parts ]
        )
    

    def with_cache(self)                -> typing.Self:
        """
        Initialize and append a objects.cache.Cache object to the factory's app.App object.

        :returns: Updated self.
        :rtype: typing.Self
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initializing application cache...")

        cache_file                      = self._path([
            "TREE.DIRECTORIES.DATA",
            "TREE.FILES.CACHE"
        ])

        self.app.cache                  = cache.Cache(
            cache_file                  = cache_file
        )
        return self 
    

    def with_cli_args(self)             -> typing.Self:
        """
        Initialize and append argparse.Namespace obejct to the factory's app.App object.

        :returns: Updated self.
        :rtype: typing.Self
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initailizing application command line arguments...")

        parser                          = argparse.ArgumentParser(
            description                 = self.config.get("INTERFACE.HELP.PARSER")
        )
    
        subparsers                      = parser.add_subparsers(
            dest                        = 'operation', 
            help                        = self.app.config.get("INTERFACE.HELP.SUBPARSER")
        )

        for op_config in self.app.config.get("INTERFACE.OPERATIONS"):
            op_parser                   = subparsers.add_parser(
                name                    = op_config["NAME"],
                help                    = op_config["HELP"]
            )
            for op_arg in op_config["ARGUMENTS"]:
                if any(
                    k not in self.app.config.get("INTERFACE.FIELDS") 
                    for k in op_arg.keys()
                ):
                    continue

                if "ACTION" in op_arg.keys():
                    op_parser.add_argument(*op_arg["SYNTAX"],
                        dest            = op_arg["DEST"],
                        help            = op_arg["HELP"],
                        action          = op_arg["ACTION"]
                    )
                    continue

                if "NARGS" in op_arg.keys():
                    op_parser.add_argument(
                        nargs           = op_arg["NARGS"],
                        default         = op_arg["DEFAULT"],
                        dest            = op_arg["DEST"],
                        help            = op_arg["HELP"],
                        type            = util.map(op_arg["TYPE"])
                    )
                    continue
                
                op_parser.add_argument(*op_arg["SYNTAX"],
                    default             = op_arg["DEFAULT"],
                    dest                = op_arg["DEST"],
                    help                = op_arg["HELP"],
                    type                = util.map(op_arg["TYPE"])
                )

        self.app.arguments              = parser.parse_args()

        return self
    

    def with_conversations(self)        -> typing.Self:
        """
        Initialize and append objects.conversation.Conversation to 
        :returns: Updated self.
        :rtype: typing.Self
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initializing application conversations...")

        hist_dir                        = self._path(["TREE.DIRECTORIES.HISTORY"])
        mem_dir                         = self._path(["TREE.DIRECTORIES.MEMORY"])
        self.app.conversations          = conversation.Conversation(
            hist_dir                    = hist_dir,
            hist_ext                    = self.app.config.get("TREE.EXTENSIONS.CONVERSATION"),
            mem_dir                     = mem_dir,
            mem_ext                     = self.app.config.get("TREE.EXTENSIONS.MEMORY"),
            converse_config             = self.app.config.get("CONVERSE.CONFIG")
        )
        return self
    
    def with_directory(self)            -> typing.Self:
        if self.app.arguments is None:
            raise ValueError("Arguments must be initialized before Repository!")
        
        arguments                       = vars(self.app.arguments)

        if "directory" in arguments:
            self.app.directory          = directory.Directory(
                directory               = self.app.arguments.directory,
                summary_file            = self.app.config.get("TREE.FILES.SUMMARY"),
                summary_config          = self.app.config.get("SUMMARIZE.CONFIG")
            )
        return self 
    
    def with_language(self)             -> typing.Self:
        lang_dir                        = self._path(["TREE.DIRECTORIES.LANGUAGE"])
        self.app.language               = language.Language(
            directory                   = lang_dir,
            extension                   = self.app.config.get("TREE.EXTENSIONS.LANGUAGE"),
            enabled                     = self.app.config.language_modules()
        )
        return self
    

    def with_logger(self) -> typing.Self:
        log_file                        = self._path([
            "TREE.DIRECTORIES.LOGS",
            "TREE.FILES.LOGS"
        ])

        self.app.logger                 = util.logger(
            file                        = log_file,
            level                       = self.app.config.get("LOGS.LEVEL"),
            schema                      = self.app.config.get("LOGS.SCHEMA")
        )
        return self
    

    def with_model(self) -> typing.Self: 
        self.app.model                  = model.Model(
            api_key                     = self.app.config.get("GEMINI.KEY"),
            default_model               = self.app.config.get("GEMINI.DEFAULT"),
            tuning                      = self.app.config.get("TUNING.ENABLED")
        ) 
        return self

    def with_personas(self) -> typing.Self:
        if self.app.cache is None:
            raise ValueError("Cache must be initialized before Personas!")
        
        tune_dir                        = self._path(["TREE.DIRECTORIES.TUNING"])
        sys_dir                         = self._path(["TREE.DIRECTORIES.SYSTEM"])
        context_file                    = self._path([
            "TREE.DIRECTORIES.DATA",
            "TREE.FILES.CONTEXT"
        ])
        self.app.personas               = persona.Persona(
            current_persona             = self.app.cache.get("currentPersona"),
            persona_config              = self.app.config.get("PERSONA"),
            context_file                = context_file,
            tune_dir                    = tune_dir,
            tune_ext                    = self.app.config.get("TREE.EXTENSIONS.TUNING"),
            sys_dir                     = sys_dir,
            sys_ext                     = self.app.config.get("TREE.EXTENSIONS.SYSTEM")
        )
        return self
    
    def with_templates(self) -> typing.Self:
        temp_dir                        = self._path([
            "TREE.DIRECTORIES.TEMPLATES"
        ])

        self.app.templates              = template.Template(
            directory                   = temp_dir,
            extension                   = self.app.config.get("TREE.EXTENSIONS.TEMPLATE")
        )
        return self
    
    def with_terminal(self) -> typing.Self:
        self.app.terminal               = terminal.Terminal(
            terminal_config             = self.app.config.get("TERMINAL")
        )
        return self

    def with_repository(self) -> typing.Self:
        if self.app.arguments is None:
            raise ValueError("Arguments must be initialized before Repository!")
        
        arguments                       = vars(self.app.arguments)

        if "repository" in arguments and "owner" in arguments:
            if self.app.config.get("REPO.VCS") is None:
                raise ValueError("VCS backend not set.")
            
            if self.app.config.get("REPO.VCS") == "github" \
                and not self.app.config.get("REPO.AUTH.CREDS"):
                raise ValueError("VCS_TOKEN environment variable not set for github VCS.")
        
            self.app.repository         = repo.Repo(
                repository              = self.app.arguments.repository,
                owner                   = self.app.arguments.owner,
                vcs                     = self.app.config.get("REPO.VCS"),
                auth                    = self.app.config.get("REPO.AUTH"),
                backends                = self.app.config.get("REPO.BACKENDS")
            )

        return self
    
    def build(self):
        return self.app