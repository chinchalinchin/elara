
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
import app as apps
import schemas
import util
import objects.cache as cache
import objects.config as conf
import objects.context as cont
import objects.conversation as convo
import objects.directory as directory
import objects.persona as persona
import objects.model as model
import objects.repository as repository
import objects.template as template
import objects.terminal as terminal


class ArgFactory:
    """
    TODO: explain
    """
    arguments                   : schemas.Arguments | None = None
    """Factory's arguments"""
    argument_config             : conf.Config | None = None
    """Application argument configuration"""


    def __init__(self, rel_dir : str = "data/config", filename : str = "args.json") -> None:
        """
        :param rel_dir: Directory relative to the application directory that contains the application configuration data.
        :type rel_dir: `str`
        :param filename: Name of the argument configuration file.
        :type filename: `str`
        """
        app_dir                 = pathlib.Path(__file__).resolve().parent
        self.config             = conf.Config(
                                    os.path.join(app_dir, rel_dir, filename))


    def with_cli_args(self) -> typing.Self:
        """
        Initialize and parse command line arguments. Append the result to the factory's arguments.

        :returns: Self with updated `arguments`.
        :rtype: `typing.Self`
        """
        parser                  = argparse.ArgumentParser(
            description         = self.config.get("help.parser")
        )
    
        subparsers              = parser.add_subparsers(
            dest                = 'operation', 
            help                = self.config.get("help.subparser")
        )

        arg_schema              = self.config.get("arguments")

        for op_config in self.config.get("interface.operations"):
            op_parser           = subparsers.add_parser(
                name            = op_config["name"],
                help            = op_config["help"]
            )
            for op_arg_key in op_config["arguments"]:
                # filter arguments by 'name' to retrieve correct schema
                op_arg_schema   = (arg for arg in arg_schema if op_arg_key == arg["name"])
                op_arg          = next(op_arg_schema, {})
                if any(
                    k not in self.config.get("fields") 
                    for k in op_arg.keys()
                ):
                    continue
                
                if "action" in op_arg.keys():
                    op_parser.add_argument(*op_arg["syntax"],
                        dest    = op_arg["dest"],
                        help    = op_arg["help"],
                        action  = op_arg["action"]
                    )
                    continue

                if "nargs" in op_arg.keys():
                    op_parser.add_argument(
                        nargs   = op_arg["nargs"],
                        default = op_arg["default"],
                        dest    = op_arg["dest"],
                        help    = op_arg["help"],
                        type    = util.map(op_arg["type"])
                    )
                    continue
                
                op_parser.add_argument(*op_arg["syntax"],
                    default     = op_arg["default"],
                    dest        = op_arg["dest"],
                    help        = op_arg["help"],
                    type        = util.map(op_arg["type"])
                )

        parsed_args             = vars(parser.parse_args())

        self.arguments          = schemas.Arguments(**parsed_args)
        return self


    def build(self) -> schemas.Arguments:
        """
        Retrieve factory constructed application arguments.

        :returns: Application arguments.
        :rtype: `schemas.Arguments`operation_name
        """
        return self.arguments


class AppFactory:
    """
    TODO: explain
    """
    app                         : apps.App | None = None
    """Factory's application."""
    app_dir                     : str | None = None
    """Directory containing application."""

    def __init__(self, rel_dir : str = "data/config", filename : str = "app.json") -> None:
        """
        Initialization a new application factory object.

        :param rel_dir: Directory relative to the application directory that contains the application configuration data.
        :type rel_dir: `str`
        :param filename: Name of the application configuration file.
        :type filename: `str`
        """
        self.app_dir            = pathlib.Path(__file__).resolve().parent
        self.app                = apps.App()
        self.app.config         = conf.Config(
            config_file         = os.path.join(self.app_dir, rel_dir, filename)
        )

    def _path(self, parts: list) -> str:
        """
        Append the application directory to a list of relative paths. 
        
        :param parts: List of configuration paths to append to application directory.
        :type parts: list
        :returns: System formatted path.
        :rtype: str
        """
        return os.path.join(self.app_dir, 
            *[self.app.config.get(p) for p in parts ])
    

    def with_cache(self) -> typing.Self:
        """
        Initialize and append a `objects.cache.Cache` object to the factory's `app.App` object.

        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initializing application cache...")

        self.app.cache          = cache.Cache(
                                    self._path([ "TREE.DIRECTORIES.DATA", "TREE.FILES.CACHE" ]))
        return self 
    

    def with_context(self) -> typing.Self:
        """
        Initialize and append a `objects.context.Context` object to the factory's `app.App` object.

        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initializing application context...")

        self.app.context        = cont.Context(
            directory           = self._path([ "TREE.DIRECTORIES.CONTEXT" ]),
            extension           = self.app.config.get("TREE.EXTESIONS.CONTEXT")
        )
        return self
    

    def with_conversations(self) -> typing.Self:
        """
        Initialize and append a `objects.conversation.Conversation` object to the factory's `app.App` object. 

        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if self.app.logger is not None:
            self.app.logger.debug("Initializing application conversations...")

        self.app.conversations  = convo.Conversation(
            directory           = self._path([ "TREE.DIRECTORIES.THREADS" ]),
            extension           = self.app.config.get("TREE.EXTENSIONS.THREADS"),
            convo_config        = self.app.config.get("OBJECTS.CONVERSATION")
        )
        return self
    

    def with_directory(self, arguments: schemas.Arguments) -> typing.Self:
        """
        Initialize and append a `objects.directory.Directory` object to the factory's `app.App` object. 
        
        :param arguments: Application arguments.
        :type arguments: `schemas.Arguments`
        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if not arguments.has_dir_args() and self.app.logger:
            self.app.logger.warning("Directory missing from arguments, ignoring initialization.")
            return self 
        
        self.app.directory      = directory.Directory(
            directory           = arguments.directory,
            directory_config    = self.app.config.get("OBJECTS.DIRECTORY")
        )
        return self 
    

    def with_logger(self) -> typing.Self:
        """
        Initialize and append `logging.Logger` to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        self.app.logger         = util.logger(
            file                = self._path([ "TREE.DIRECTORIES.LOGS", "TREE.FILES.LOG" ]),
            level               = self.app.config.get("LOGS.LEVEL"),
            schema              = self.app.config.get("LOGS.SCHEMA")
        )
        return self
    

    def with_model(self) -> typing.Self: 
        """
        Initialize and append a `objects.model.Model` object to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if not self.app.config.get("GEMINI.KEY"):
            raise ValueError("GEMINI_KEY environment variable not set.")

        self.app.model          = model.Model(self.app.config.get("OBJECTS.MODEL")) 
        return self


    def with_personas(self) -> typing.Self:
        """
        Initialize and append `objects.persona.Persona` to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if self.app.cache is None:
            raise ValueError("Cache must be initialized before Personas!")

        self.app.personas       = persona.Persona(
            persona             = self.app.cache.get("current_persona"),
            persona_config      = self.app.config.get("OBJECTS.PERSONA"),
            context             = self._path([ "TREE.DIRECTORIES.CONTEXT" ]),
            directory           = self._path([ "TREE.DIRECTORIES.PERSONAS" ]),
            extension           = self.app.config.get("TREE.EXTENSIONS.PERSONAS"),
        )
        return self
    

    def with_templates(self) -> typing.Self:
        """
        Initialize and append a `objects.template.Template` object to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype:`typing.Self`
        """
        self.app.templates      = template.Template(
            directory           = self._path([ "TREE.DIRECTORIES.TEMPLATES" ]),
            extension           = self.app.config.get("TREE.EXTENSIONS.TEMPLATES")
        )
        return self
    

    def with_terminal(self) -> typing.Self:
        """
        Initialize and append a `objects.terminal.Terminal` object to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype:`typing.Self`
        """
        self.app.terminal       = terminal.Terminal(
            terminal_config     = self.app.config.get("OBJECTS.TERMINAL")
        )
        return self


    def with_repository(self, arguments: schemas.Arguments) -> typing.Self:
        """
        Initialize and append a `objects.repo.Repo` object to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if not arguments.has_vcs_args():
            raise ValueError("VCS arguments must before creating a Repository object!")
        
        if self.app.config.get("OBJECTS.REPO.VCS") is None:
            raise ValueError("VCS backend not set.")
        
        if self.app.config.get("OBJECTS.REPO.VCS") == "github" \
            and not self.app.config.get("OBJECTS.REPO.AUTH.CREDS"):
            raise ValueError(
                "REPO_AUTH_CREDS environment variable not set for github VCS.")
    
        self.app.repository     = repository.Repo(
            repository_config   = self.app.config.get("OBJECTS.REPO"),
            repository          = arguments.repository,
            owner               = arguments.owner
        )

        return self
   
    
    def build(self) -> apps.App :
        """
        Retrieve factory constructed application.

        :returns: Factory constructed application.
        :rtype: `app.App`
        """
        return self.app