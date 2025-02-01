
"""
factory.py
----------

Factory object for building application objects.
"""
# Standard Library Modules
import argparse
import logging
import os
import pathlib
import typing

# Application Modules
import app as apps
import constants
import exceptions
import schemas
import util
import objects.cache as cache
import objects.config as conf
import objects.conversation as convo
import objects.directory as directory
import objects.injection as inject
import objects.model as model
import objects.persona as persona
import objects.printer as printer
import objects.repository as repository
import objects.template as template
import objects.terminal as terminal


logger                          = logging.getLogger(__name__)


class ArgFactory:
    """
    Factory for construcing the application arguments via different entrypoints.
    """
    arguments                   : schemas.Arguments | None = None
    """Factory's arguments"""
    argument_config             : conf.Config | None = None
    """Application argument configuration"""

    # Argument Propeties
    ## COMMAND LINE PARSERS
    _prop_parh                  : str = constants.CommandLineProps.PARSER_HELP.value
    _prop_subh                  : str = constants.CommandLineProps.SUBPARSER_HELP.value
    _prop_subd                  : str = constants.CommandLineProps.SUBPARSER_DEST.value
    _prop_args                  : str = constants.CommandLineProps.ARGUMENTS.value
    _prop_oper                  : str = constants.CommandLineProps.OPERATIONS.value
    _prop_fiel                  : str = constants.CommandLineProps.FIELDS.value
    _prop_name                  : str = constants.CommandLineProps.NAME.value
    ## COMMAND LINE ARGUMENTS
    _prop_help                  : str = constants.CommandLineProps.HELP.value
    _prop_synt                  : str = constants.CommandLineProps.SYNTAX.value
    _prop_dest                  : str = constants.CommandLineProps.DEST.value
    _prop_acti                  : str = constants.CommandLineProps.ACTION.value
    _prop_narg                  : str = constants.CommandLineProps.NARGS.value
    _prop_defa                  : str = constants.CommandLineProps.DEFAULT.value
    _prop_type                  : str = constants.CommandLineProps.TYPE.value 


    def __init__(self, rel_dir : str = "data/config", filename : str = "args.json") -> None:
        """
        Initialize an ArgFactory object.

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
            description         = self.config.get(self._prop_parh)
        )
    
        subparsers              = parser.add_subparsers(
            dest                = self._prop_subd, 
            help                = self.config.get(self._prop_subh)
        )

        arg_schema              = self.config.get(self._prop_args)

        for op_config in self.config.get(self._prop_oper):
            op_parser           = subparsers.add_parser(
                name            = op_config[self._prop_name],
                help            = op_config[self._prop_help]
            )
            for op_arg_key in op_config[self._prop_args]:
                # filter arguments by 'name' to retrieve correct schema
                op_arg_schema   = (arg for arg in arg_schema if op_arg_key == arg[self._prop_dest])
                op_arg          = next(op_arg_schema, {})
                if any(
                    k not in self.config.get(self._prop_fiel) 
                    for k in op_arg.keys()
                ):
                    continue
                
                if self._prop_acti in op_arg.keys():
                    op_parser.add_argument(*op_arg[self._prop_synt],
                        dest    = op_arg[self._prop_dest],
                        help    = op_arg[self._prop_help],
                        action  = op_arg[self._prop_acti]
                    )
                    continue

                if self._prop_narg in op_arg.keys():
                    op_parser.add_argument(
                        nargs   = op_arg[self._prop_narg],
                        default = op_arg[self._prop_defa],
                        dest    = op_arg[self._prop_dest],
                        help    = op_arg[self._prop_help],
                        type    = util.map(op_arg[self._prop_type])
                    )
                    continue
                
                op_parser.add_argument(*op_arg[self._prop_synt],
                    default     = op_arg[self._prop_defa],
                    dest        = op_arg[self._prop_dest],
                    help        = op_arg[self._prop_help],
                    type        = util.map(op_arg[self._prop_type])
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
    Factory for managing the application object initialization.
    """
    app                         : apps.App | None = None
    """Factory's application."""
    app_dir                     : str | None = None
    """Directory containing application."""


    # Factory Properties
    ## AUTHENTICATION
    _prop_auth_gem              = constants.FactoryProps.AUTH_GEMINI.value
    _prop_auth_vcs              = constants.FactoryProps.AUTH_VCS.value
    ## DIRECTORIES
    _prop_dir_data              = constants.FactoryProps.DIR_DATA.value
    _prop_dir_injs              = constants.FactoryProps.DIR_INJECTIONS.value
    _prop_dir_pers              = constants.FactoryProps.DIR_PERSONA.value
    _prop_dir_thrd              = constants.FactoryProps.DIR_THREADS.value
    _prop_dir_temp              = constants.FactoryProps.DIR_TEMPLATES.value
    ## FILES 
    _prop_file_cach             = constants.FactoryProps.FILE_CACHE.value
    ## EXTENSIONS
    _prop_ext_injs              = constants.FactoryProps.EXT_INJECTIONS.value
    _prop_ext_temp              = constants.FactoryProps.EXT_TEMPLATES.value
    _prop_ext_thrd              = constants.FactoryProps.EXT_THREADS.value
    _prop_ext_pers              = constants.FactoryProps.EXT_PERSONA.value
    ## OBJECTS
    _prop_obj_conv              = constants.FactoryProps.OBJECT_CONVO.value
    _prop_obj_dir               = constants.FactoryProps.OBJECT_DIR.value
    _prop_obj_per               = constants.FactoryProps.OBJECT_PERSONA.value
    _prop_obj_mod               = constants.FactoryProps.OBJECT_MODEL.value
    _prop_obj_term              = constants.FactoryProps.OBJECT_TERMINAL.value
    _prop_obj_repo              = constants.FactoryProps.OBJECTS_REPOSITORY.value
    ## EXTERNAL SERVICES
    _prop_vcs                   = constants.FactoryProps.VCS.value          
    ## LOGS
    _prop_log_dir               = constants.LogProps.DIRECTORY.value
    _prop_log_file              = constants.LogProps.FILE.value


    def __init__(self, rel_dir : str = "data/config", filename : str = "app.json") -> None:
        """
        Initialize a new application factory object.

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
    

    def log_file(self) -> str:
        """
        Return the location of the application log file.

        :returns: Log file path.
        :rtype: `str`
        """
        return self._path([ self._prop_log_dir, self._prop_log_file ])


    def with_cache(self) -> typing.Self:
        """
        Initialize and append a `objects.cache.Cache` object to the factory's `app.App` object.

        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        logger.debug("Initializing application cache...")

        self.app.cache          = cache.Cache(
                                    self._path([self._prop_dir_data, self._prop_file_cach]))
        return self 
    

    def with_conversations(self) -> typing.Self:
        """
        Initialize and append a `objects.conversation.Conversation` object to the factory's `app.App` object. 

        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        logger.debug("Initializing application conversations...")

        self.app.conversations  = convo.Conversation(
            directory           = self._path([self._prop_dir_thrd]),
            extension           = self.app.config.get(self._prop_ext_thrd),
            convo_config        = self.app.config.get(self._prop_obj_conv)
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
        if not arguments.directory:
            logger.warning("Directory missing from arguments, ignoring initialization.")
            return self 
        
        self.app.directory      = directory.Directory(
            directory           = arguments.directory,
            directory_config    = self.app.config.get(self._prop_obj_dir)
        )
        return self 
    

    def with_injections(self) -> typing.Self:
        """
        Initialize and append a `objects.context.Context` object to the factory's `app.App` object.

        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        logger.debug("Initializing application context...")

        self.app.injections     = inject.Injection(
            directory           = self._path([self._prop_dir_injs]),
            extension           = self.app.config.get(self._prop_ext_injs)
        )
        return self
    
    
    def with_model(self) -> typing.Self: 
        """
        Initialize and append a `objects.model.Model` object to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        models                  = None
        if self.app.cache:
            models              = self.app.cache.get(constants.CacheProps.MODELS.value)

        self.app.model          = model.Model(self.app.config.get(self._prop_obj_mod), models) 

        if self.app.model.refresh:
            self.app.cache.update(**self.app.model.vars())

        return self


    def with_personas(self) -> typing.Self:
        """
        Initialize and append `objects.persona.Persona` to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if self.app.cache is None:
            raise exceptions.FactoryError("Cache must be initialized before Personas!")

        self.app.personas       = persona.Persona(
            persona             = self.app.cache.get(constants.CacheProps.CURRENT_PERSONA.value),
            persona_config      = self.app.config.get(self._prop_obj_per),
            directory           = self._path([self._prop_dir_pers]),
            extension           = self.app.config.get(self._prop_ext_pers),
        )
        return self
    

    def with_templates(self) -> typing.Self:
        """
        Initialize and append a `objects.template.Template` object to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype:`typing.Self`
        """
        self.app.templates      = template.Template(
            directory           = self._path([self._prop_dir_temp]),
            extension           = self.app.config.get(self._prop_ext_temp)
        )
        return self
    

    def with_terminal(self) -> typing.Self:
        """
        Initialize and append a `objects.terminal.Terminal` object to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype:`typing.Self`
        """
        self.app.terminal       = terminal.Terminal(
            terminal_config     = self.app.config.get(self._prop_obj_term)
        )
        return self


    def with_repository(self, arguments: schemas.Arguments) -> typing.Self:
        """
        Initialize and append a `objects.repo.Repo` object to the factory's `app.App` object. 
        
        :returns: Self with updated application attribute.
        :rtype: `typing.Self`
        """
        if not arguments.has_vcs_args():
            logger.warning("No repository arguments provided, skipping initialization")
            return self 
                
        if self.app.config.get(self._prop_vcs) is None:
            raise exceptions.VCSBackendError("VCS backend not set.")
        
        if self.app.config.get(self._prop_vcs) == constants.VersionControl.GITHUB.value \
            and not self.app.config.get(self._prop_auth_vcs):
            raise exceptions.VCSCredentialsError(
                "VCS credentials not set for GitHub backend.")
    
        self.app.repository     = repository.Repo(
            repository_config   = self.app.config.get(self._prop_obj_repo),
            repository          = arguments.repository,
            owner               = arguments.owner
        )

        return self
   
    
    def build(self, arguments: schemas.Arguments = None) -> apps.App :
        """
        Retrieve factory constructed application.

        :returns: Factory constructed application.
        :rtype: `app.App`
        """
        # Raise 
        try:
            self.app.validate(arguments)
        except exceptions.FactoryError as e:
            logger.error(f"Factory Error:\n\n{e}")
        return self.app