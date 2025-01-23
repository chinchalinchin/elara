""" 
main.py
-------

Module for command line interface.
"""
# Standard Library Modules
import argparse
import logging
import os
import pathlib
import pprint
import typing

# Application Modules
import app
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

class App(typing.TypedDict):
    """
    Data structure for managing application objects.
    """
    ARGUMENTS : argparse.Namespace
    CACHE : cache.Cache
    CONFIG : config.Config
    CONVERSATIONS: conversation.Conversation
    DIRECTORY: directory.Directory | None
    LANGUAGE: language.Language
    LOGGER : logging.Logger
    MODEL : model.Model
    PERSONAS : persona.Persona
    REPO: repo.Repo | None
    TEMPLATES : template.Template

class Output(typing.TypedDict):
    """
    Data structure for managing application output
    """
    RESPONSE : str
    PROMPT : str
    SUMMARY : str | None
    VCS : str | None

def logger(
    application                         : App,
    file                                : str = None
)                                       -> logging.Logger:
    """
    Configure application logging

    :param file: Location of log file, if logs are to be written to file.
    :type log_file: str
    :param app: Dictionary containing application configuration.
    :type app: dict
    """
    logger                              = logging.getLogger() 
    level                               = application["CONFIG"].get("LOGS.LEVEL")
    schema                              = application["CONFIG"].get("LOGS.SCHEMA") 

    if level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        logger.setLevel(level)
    else:
        logger.setLevel("INFO") 

    formatter                           = logging.Formatter(schema)

    if file is not None:
        file_handler                    = logging.FileHandler(file)
        file_handler.setLevel(level) 
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


    console_handler                     = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def output(
    application                         : App,
    out                                 : Output,
    suppress_prompt                     : bool = True
):
    """
    Write output to appropriate location. Output should follow the format,

    .. code-block:: python

        out                             = {
            "prompt"                    : "words",
            "response"                  : "words",
            "summary"                   : "words",
            "vcs"                       : "words"
        }

    :param application:
    :type application: App
    :param out: application output to be written.
    :type out: 
    :
    """
    arg_map                             = vars(application["ARGUMENTS"])
    to_file                             = "output" in arg_map.keys() and arg_map.get("output")
    to_screen                           = "show" in arg_map.keys() and arg_map.get("show")
    prompt                              = "prompt" in out.keys() and arg_map.get("prompt")
    response                            = "response" in out.keys()
    summary                             = "summary" in out.keys()
    vcs                                 = "vcs" in out.keys()

    if to_file:
        with open(arg_map["output"], "w") as outfile:
            if prompt: 
                outfile.write(out["prompt"])
            if response:
                outfile.write(out["response"])
            if summary: 
                outfile.write(out["summary"])

    if to_screen:
        if summary:
            print(out["summary"])

        if prompt and not suppress_prompt:
            print(
                application["CONFIG"].get("OUTPUT.PROMPT").format(
                    content             = out["prompt"]
                )
            )

        if response:
            print(
                application["CONFIG"].get("OUTPUT.RESPONSE").format(
                    content             = out["response"]
                )
            )

        if vcs:
            print(out["vcs"])


def args(configuration : config.Config) -> argparse.Namespace:
    """
    Parse and format command line arguments.

    :returns: Parsed arguments.
    :rtype: argparse.Namespace
    """
    parser                              = argparse.ArgumentParser(
        description                     = configuration.get("INTERFACE.HELP.PARSER")
    )
    
    subparsers                          = parser.add_subparsers(
        dest                            = 'operation', 
        help                            = configuration.get("INTERFACE.HELP.SUBPARSER")
    )

    for op_config in configuration.get("INTERFACE.OPERATIONS"):
        op_parser                       = subparsers.add_parser(
            name                        = op_config["NAME"],
            help                        = op_config["HELP"]
        )
        for op_arg in op_config["ARGUMENTS"]:
            if any(k not in [ 
                "DEFAULT", 
                "DEST", 
                "HELP", 
                "SYNTAX", 
                "ACTION", 
                "NARGS",
                "TYPE"
            ] for k in op_arg.keys()):
                continue

            if "ACTION" in op_arg.keys():
                op_parser.add_argument(*op_arg["SYNTAX"],
                    dest                = op_arg["DEST"],
                    help                = op_arg["HELP"],
                    action              = op_arg["ACTION"]
                )
                continue

            if "NARGS" in op_arg.keys():
                op_parser.add_argument(
                    nargs               = op_arg["NARGS"],
                    default             = op_arg["DEFAULT"],
                    dest                = op_arg["DEST"],
                    help                = op_arg["HELP"],
                    type                = util.map(op_arg["TYPE"])
                )
                continue
            
            op_parser.add_argument(*op_arg["SYNTAX"],
                default                 = op_arg["DEFAULT"],
                dest                    = op_arg["DEST"],
                help                    = op_arg["HELP"],
                type                    = util.map(op_arg["TYPE"])
            )

    return parser.parse_args()


def configure(application : App) -> dict:
    """
    Parses and applies configuration settings.

    :param app: Dictionary containing application configuration.
    :type app: dict
    :returns: Dictionary containing the current configuration
    """
    config                              = {}

    if application["ARGUMENTS"].config:
        for item in application["ARGUMENTS"].config:
            if "=" not in item:
                application["LOGGER"].error(f"Invalid configuration format: {item}. Expected key=value.")
                continue
            
            key, value                  = item.split("=", 1)

            if key not in application["CONFIG"].data:
                application["LOGGER"].error(f"Invalid configuration key: {key}. Key not in configuration.")
                continue

            validated_value             = util.validate(value)

            if validated_value is None:
                application["LOGGER"].error(f"Invalidate configuration type: {key}={value}")
                continue 

            config[key]                 = validated_value

    if config:
        application["CONFIG"].update(**config)
        application["CONFIG"].save()
        application["LOGGER"].info(f"Updated configuration with: {config}")
        return config
    
    application["LOGGER"].warning("No configuration pairs provided.")
    return config


def init(
    data_dir                            : str = "data",
    config_file                         : str = "config.json"
)                                       -> App:
    """
    Initialize the application.

    :returns: Application configuration.
    :rtype: dict
    """
    application                         = {}
    app_dir                             = pathlib.Path(__file__).resolve().parent

    ################################################################################
    #                       APPLICATION CONFIGURATION                              #
    ################################################################################
    config_filepath                     = os.path.join(app_dir, data_dir, config_file)
    application["CONFIG"]               = config.Config(
        config_file                     = config_filepath
    )

    if not application["CONFIG"].get("GEMINI.KEY"):
        raise ValueError("GEMINI_KEY environment variable not set.")

    ################################################################################
    #                          APPLICATION LOGGING                                 #
    ################################################################################
    log_rel_path                        = application["CONFIG"].get("TREE.DIRECTORIES.LOGS")
    log_file                            = application["CONFIG"].get("TREE.FILES.LOG")
    log_filepath                        = os.path.join(app_dir, log_rel_path, log_file)
    application["LOGGER"]               = logger(
        application                     = application,
        file                            = log_filepath
    )

    ################################################################################
    #                       APPLICATION ARGUMENTS                                  #
    ################################################################################
    application["LOGGER"].debug("Initializing arguments...")
    application["ARGUMENTS"]            = args(
        configuration                   = application["CONFIG"]
    )

    ################################################################################
    #                         APPLICATION CACHE                                    #
    ################################################################################
    application["LOGGER"].debug("Initializing application cache...")
    cache_rel_path                      = application["CONFIG"].get("TREE.DIRECTORIES.DATA")
    cache_file                          = application["CONFIG"].get("TREE.FILES.CACHE")
    cache_filepath                      = os.path.join(app_dir, cache_rel_path, cache_file)
    application["CACHE"]                = cache.Cache(
        cache_file                      = cache_filepath
    )

    # Write arguments to cache
    application["LOGGER"].debug("Writing command line arguments to cache...")
    update_event                        = False
    arguments                           = vars(application["ARGUMENTS"])
    for k, v in arguments.items():
        if k in application["CACHE"].vars():
            if v is None:
                v = application["CACHE"].get(k)

            update_event                = application["CACHE"].update(**{
                k                       : v
            }) or update_event

    if update_event:
        application["CACHE"].save()

    ################################################################################
    #                       APPLICATION LANGUAGE                                   #
    ################################################################################
    application["LOGGER"].debug("Initializing language modules...")
    lang_rel_path                       = application["CONFIG"].get("TREE.DIRECTORIES.LANGUAGE")
    lang_dir                            = os.path.join(app_dir, lang_rel_path)
    application["LANGUAGE"]             = language.Language(
        directory                       = lang_dir,
        extension                       = application["CONFIG"].get("TREE.EXTENSIONS.LANGUAGE"),
        enabled                         = application["CONFIG"].language_modules()
    )

    ################################################################################
    #                       APPLICATION TEMPLATES                                  #
    ################################################################################
    application["LOGGER"].debug("Initializing application templates...")
    temp_rel_path                       = application["CONFIG"].get("TREE.DIRECTORIES.TEMPLATES")
    temp_dir                            = os.path.join(app_dir, temp_rel_path)
    application["TEMPLATES"]            = template.Template(
        directory                       = temp_dir,
        extension                       = application["CONFIG"].get("TREE.EXTENSIONS.TEMPLATE")
    )

    ################################################################################
    #                          APPLICATION MODEL                                   #
    ################################################################################
    application["LOGGER"].debug("Initializing Gemini Model...")
    application["MODEL"]                = model.Model(
        api_key                         = application["CONFIG"].get("GEMINI.KEY"),
        default_model                   = application["CONFIG"].get("GEMINI.DEFAULT"),
        tuning                          = application["CONFIG"].get("TUNING.ENABLED")
    )

    ################################################################################
    #                         APPLICATION PERSONAS                                 #
    ################################################################################
    application["LOGGER"].debug("Initializing personas...")
    tune_rel_path                       = application["CONFIG"].get("TREE.DIRECTORIES.TUNING")
    sys_rel_path                        = application["CONFIG"].get("TREE.DIRECTORIES.SYSTEM")
    context_file                        = application["CONFIG"].get("TREE.FILES.CONTEXT")
    tune_dir                            = os.path.join(app_dir, tune_rel_path)
    sys_dir                             = os.path.join(app_dir, sys_rel_path)
    context_filepath                    = os.path.join(app_dir, data_dir, context_file)
    application["PERSONAS"]             = persona.Persona(
        current_persona                 = application["CACHE"].get("currentPersona"),
        persona_config                  = application["CONFIG"].get("PERSONA"),
        context_file                    = context_filepath,
        tune_dir                        = tune_dir,
        tune_ext                        = application["CONFIG"].get("TREE.EXTENSIONS.TUNING"),
        sys_dir                         = sys_dir,
        sys_ext                         = application["CONFIG"].get("TREE.EXTENSIONS.TUNING")
    )            
    
    ################################################################################
    #                      APPLICATION CONVERSATIONS                               #
    ################################################################################
    application["LOGGER"].debug("Initialize chat histories...")
    hist_rel_path                       = application["CONFIG"].get("TREE.DIRECTORIES.HISTORY")
    mem_rel_path                        = application["CONFIG"].get("TREE.DIRECTORIES.MEMORY")
    hist_dir                            = os.path.join(app_dir, hist_rel_path)
    mem_dir                             = os.path.join(app_dir, mem_rel_path)
    application["CONVERSATIONS"]        = conversation.Conversation(
        hist_dir                        = hist_dir,
        hist_ext                        = application["CONFIG"].get("TREE.EXTENSIONS.CONVERSATION"),
        mem_dir                         = mem_dir,
        mem_ext                         = application["CONFIG"].get("TREE.EXTENSIONS.MEMORY"),
        tz_offset                       = application["CONFIG"].get("CONVERSATION.TIMEZONE_OFFSET")
    )

    ################################################################################
    #                         APPLICATION TERMINAL                                 #
    ################################################################################
    application["LOGGER"].debug("Initialize interactive terminal...")
    application["TERMINAL"]             = terminal.Terminal(
        terminal_config                 = application["CONFIG"].get("TERMINAL")
    )
    ################################################################################
    #                          APPLICATION REPOSITORY                              #
    ################################################################################
    if "repository" in arguments and "owner" in arguments:
        if application["CONFIG"].get("REPO.VCS") is None:
            raise ValueError("VCS backend not set.")
        
        if application["CONFIG"].get("REPO.VCS") == "github" \
            and not application["CONFIG"].get("REPO.AUTH.CREDS"):
            raise ValueError("VCS_TOKEN environment variable not set for github VCS.")
    
        application["REPO"]             = repo.Repo(
            repository                  = application["ARGUMENTS"].repository,
            owner                       = application["ARGUMENTS"].owner,
            vcs                         = application["CONFIG"].get("REPO.VCS"),
            auth                        = application["CONFIG"].get("REPO.AUTH"),
            backends                    = application["CONFIG"].get("REPO.BACKENDS")
        )
    ################################################################################
    #                          APPLICATION DIRECTORY                               #
    ################################################################################
    if "directory" in arguments:
        application["DIRECTORY"]        = directory.Directory(
            directory                   = application["ARGUMENTS"].directory,
            summary_file                = application["CONFIG"].get("TREE.FILES.SUMMARY"),
            summary_config              = application["CONFIG"].get("SUMMARIZE")
        )

    application["LOGGER"].debug("Application initialized!")
    application["LOGGER"].debug("--- Application Configuration")
    application["LOGGER"].debug(
        pprint.pformat(application["CONFIG"].vars())
    )
    application["LOGGER"].debug("--- Application Cache")
    application["LOGGER"].debug(
        pprint.pformat(application["CACHE"].vars())
    )
    application["LOGGER"].debug("--- Application Arguments")
    application["LOGGER"].debug(
        pprint.pformat(arguments)
    )
    
    typed_app = App(application)
    return typed_app

# APPLICATION ENTRYPOINT

def main() -> bool:
    """
    Main function to run the command-line interface.
    """
    application                         = init()
    operations                          = {
        # Administrative functions
        "configure"                     : configure,
        # Application functions
        "summarize"                     : app.summarize,
        "converse"                      : app.converse,
        "review"                        : app.review,
        "request"                       : app.request,
        "tune"                          : app.tune,
        "analyze"                       : app.analyze
    }

    operation_name                      = application["ARGUMENTS"].operation
    arguments                           = vars(application["ARGUMENTS"]) 

    tty                                 = "interactive" in arguments \
                                            and arguments["interactive"]
    
    if operation_name not in operations:
        return False 
    
    if tty and operation_name == "converse": 
        application["ARGUMENTS"].show   = True
        application["TERMINAL"].interact(
            callable                    = app.converse,
            printer                     = output,
            app                         = application
        )
        return
        
    out                                 = operations[operation_name](application)
    typed_out                           = Output(out)
    
    output(
        application                     = application,
        out                             = typed_out,
        suppress_prompt                 = False
    )
    

if __name__ == "__main__":
    main()