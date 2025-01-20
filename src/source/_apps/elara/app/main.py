""" # main.py
Module for command line interface.
"""
# Standard Library Modules
import argparse
import logging
import os
import pathlib
import pprint
import re

# Application Modules
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

def logger(
    app                                 : dict,
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
    level                               = app["CONFIG"].get("LOGS.LEVEL")
    schema                              = app["CONFIG"].get("LOGS.SCHEMA") 

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
                    # @OPERATION
                    #   FOR THE LOVE OF GOD, MILTON! LOOK AT WHAT THE DEVS
                    #   ARE DOING!
                    #   This is a ticking time bomb, Milton. You must surely
                    #   have a better solution than these code monkeys!
                    type                = eval(op_arg["TYPE"])
                )
                continue
            
            op_parser.add_argument(*op_arg["SYNTAX"],
                default                 = op_arg["DEFAULT"],
                dest                    = op_arg["DEST"],
                help                    = op_arg["HELP"],
                type                    = eval(op_arg["TYPE"])
            )

    return parser.parse_args()


def configure(app : dict) -> dict:
    """
    Parses and applies configuration settings.

    :param app: Dictionary containing application configuration.
    :type app: dict
    :returns: Dictionary containing the current configuration
    """
    config                              = {}

    if app["ARGUMENTS"].config:
        for item in app["ARGUMENTS"].config:
            try:
                if "=" not in item:
                    app["LOGGER"].error(f"Invalid configuration format: {item}. Expected key=value.")
                    continue
                key, value              = item.split("=", 1)
                if key not in app["CONFIG"].data:
                    app["LOGGER"].error(f"Invalid configuration key: {key}. Key not in configuration.")
                    continue
                config[key]             = value
            except ValueError:
                app["LOGGER"].error(f"Invalid configuration format: {item}. Expected key=value.")
                continue

        app["CONFIG"].update(**config)
        app["CONFIG"].save()
        app["LOGGER"].info(f"Updated configuration with: {config}")
        return config
    
    app["LOGGER"].warning("No configuration pairs provided.")
    return config


def converse(app : dict) -> dict:
    """
    Chat with one of Gemini's personas.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated prompt and model response.
    :rtype: dict
    """
    convo                               = conversation.Conversation()

    convo.update(
        persona                         = app["CACHE"].get("currentPersona"), 
        name                            = app["CACHE"].get("currentPrompter"), 
        text                            = app["ARGUMENTS"].prompt
    )
    
    template_vars                       = { 
        **app["CACHE"].vars(), 
        **app["LANGUAGE"].vars(),
        **convo.vars()
    }

    if app["ARGUMENTS"].directory is not None:
        template_vars.update(summarize(app))

    parsed_prompt                       = app["TEMPLATES"].render(
        temp                            = "conversation", 
        variables                       = template_vars
    )

    response                            = app["MODEL"].respond(
        prompt                          = parsed_prompt, 
        model_name                      = app["CACHE"].get("currentModel"),
        generation_config               = app["PERSONA"].get("generationConfig"),
        safety_settings                 = app["PERSONA"].get(" model.safetySettings"),
        tools                           = app["PERSONA"].get("tools"),
        system_instruction              = app["PERSONA"].get("systemInstruction")
    )

    convo.update(
        persona                         = app["CACHE"].get("currentPersona"), 
        name                            = app["CACHE"].get("currentPersona"), 
        text                            = response
    )

    return {
        "prompt"                        : parsed_prompt,
        "response"                      : response
    }


def analyze(app: dict) -> dict:
    """
    This function injects the contents of a directory containing only RST documents into the ``data/templates/analysis.rst`` template. It then sends this contextualized prompt to the Gemini mdeol persona of *Axiom*.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated prompt and model response.
    :rtype: dict
    """
    buffer                              = app["CACHE"].vars()
    persona                             = app["PERSONAS"].function("analyze")
    buffer["currentPersona"]            = persona

    analyze_vars                        = {
        **buffer,
        **app["LANGUAGE"].vars(),
        **summarize(app),
        **{ "latex": app["CONFIG"].get("ANALYZE.LATEX_PREAMBLE") }
    }

    parsed_prompt                       = app["TEMPLATES"].render(
        temp                            = "analysis", 
        variables                       = analyze_vars
    )
    
    response                            = app["MODEL"].respond(
        prompt                          = parsed_prompt,
        model_name                      = app["CACHE"].get("currentModel"),
        generation_config               = app["PERSONAS"].get("generationConfig", persona),
        safety_settings                 = app["PERSONAS"].get("safetySettings", persona),
        tools                           = app["PERSONAS"].get("tools", persona),
        system_instruction              = app["PERSONAS"].get("systemInstruction", persona)
    )
    
    return {
        "prompt"                        : parsed_prompt,
        "response"                      : response
    }


def review(app : dict) -> dict:
    """
    This function injects the contents of a git repository into the ``data/templates/review.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Milton*. *Milton*'s response is then parsed and posted to the remote VCS backend that contains the pull request corresponding to the git repository.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated prompt and model response.
    :rtype: dict
    """
    if app["CONFIG"].get("REPO.VCS") is None:
        raise ValueError("VCS backend not set.")
    
    if app["CONFIG"].get("REPO.VCS") == "github" \
        and not app["CONFIG"].get("REPO.AUTH.CREDS"):
        raise ValueError("VCS_TOKEN environment variable not set for github VCS.")
    
    source                              = repo.Repo(
        repository                      = app["ARGUMENTS"].repository,
        owner                           = app["ARGUMENTS"].owner,
        commit                          = app["ARGUMENTS"].commit,
        vcs                             = app["CONFIG"].get("REPO.VCS"),
        auth                            = app["CONFIG"].get("REPO.AUTH"),
        backends                        = app["CONFIG"].get("REPO.BACKENDS")
    )

    buffer                              = app["CACHE"].vars()
    persona                             = app["PERSONAS"].function("review")
    buffer["currentPersona"]            = persona

    review_variables                    = { 
        **buffer,
        **source.vars(),
        **app["LANGUAGE"].vars(),
        **summarize(app)
    }
    review_prompt                       = app["TEMPLATES"].render(
        temp                            = "review", 
        variables                       = review_variables
    )

    model_res                           = app["MODEL"].respond(
        prompt                          = review_prompt,
        model_name                      = app["CACHE"].get("currentModel"),
        generation_config               = app["PERSONAS"].get("generationConfig", persona),
        safety_settings                 = app["PERSONAS"].get("safetySettings", persona),
        tools                           = app["PERSONAS"].get("tools", persona),
        system_instruction              = app["PERSONAS"].get("systemInstruction", persona)
    )

    # @OPERATIONS
    #   Oh boy, Milton, wait until you see what's inside the `comment()` function.
    #   We haven't been able to successfully post a comment back to the VCS backend
    #   yet! I don't know if there's a gas leak in the development department or what,
    #   but they sure aren't developing stable software, that is for sure.
    source_res                          = source.comment(
        msg                             = model_res,
        pr                              = app["ARGUMENTS"].pull,
        path                            = "README.md"
    )
    return {
        "prompt"                        : review_prompt,
        "response"                      : model_res,
        "vcs"                           : source_res
    }


def request(app: dict) -> dict:
    """
    This function halts the application to wait for the user to specify the feature request through Gherkin-style syntax.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated feature request.
    :rtype: dict
    """
    buffer                              = app["CACHE"].vars()
    persona                             = app["PERSONAS"].function("request")
    buffer["currentPersona"]            = persona
    term                                = terminal.Terminal(
        gherkin_config                  = app["CONFIG"].get("GHERKIN")
    )
    request_vars                         = { 
        **term.gherkin(), 
        **buffer 
    }
    
    parsed_prompt                       = app["TEMPLATES"].render("request", request_vars)
    
    response                            = app["MODEL"].respond(
        prompt                          = parsed_prompt,
        model_name                      = app["CACHE"].get("currentModel"),
        generation_config               = app["PERSONAS"].get("generationConfig", persona),
        safety_settings                 = app["PERSONAS"].get("safetySettings", persona),
        tools                           = app["PERSONAS"].get("tools", persona),
        system_instruction              = app["PERSONAS"].get("systemInstruction", persona)
    )
    return {
        "response"                      : response
    }


def summarize(app : dict) -> dict:
    """
    This function summarizes the contents of a directory and writes the sumamry to an RST file. 

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated summary.
    :rtype: dict
    """
    local_dir                           = app["ARGUMENTS"].directory

    dir                                 = directory.Directory(
        directory                       = local_dir,
        summary_file                    = app["CONFIG"].get("TREE.FILES.SUMMARY"),
        summary_config                  = app["CONFIG"].get("SUMMARIZE")
    )

    summary_vars                        = dir.summary()

    summary                             = app["TEMPLATES"].render("summary", summary_vars)
    
    return                              { 
        "summary"                       : summary
    }


def tune(app : dict) -> bool:
    """
    Initialize tuned personas if tuning is enabled through the ``TUNING`` environment variable.

    :returns: A flag to signal if a tuning event occured.
    :rtype: bool
    """
    
    if app["CONFIG"].get("TUNING.ENABLED"):
        for p in app["PERSONAS"].all():
            if not app["CACHE"].is_tuned(p):
                res                     = app["MODEL"].tune(
                    display_name        = p,
                    tuning_model        = app["CONFIG"].get("TUNING.SOURCE"),
                    tuning_data         = app["PERSONA"].tuning(p)
                )
                app["CACHE"].update(**{
                    "tunedModels"       : [{
                        "name"          : p,
                        "version"       : app["CONFIG"].get("VERSION"),
                        "path"          : res.name
                    }]
                })
                app["CACHE"].save()
    return app["CACHE"].get("tunedModels")
    

def init(
    data_dir                            : str = "data",
    config_file                         : str = "config.json"
) -> dict:
    """
    Initialize the application.

    :returns: Application configuration.
    :rtype: dict
    """
    app                                 = {}
    app_dir                             = pathlib.Path(__file__).resolve().parent

    #############################
    # APPLICATION CONFIGURATION #
    #############################
    config_filepath                     = os.path.join(app_dir, data_dir, config_file)
    app["CONFIG"]                       = config.Config(
        config_file                     = config_filepath
    )

    if not app["CONFIG"].get("GEMINI.KEY"):
        raise ValueError("GEMINI_KEY environment variable not set.")

    #######################
    # APPLICATION LOGGING #
    #######################
    log_rel_path                        = app["CONFIG"].get("TREE.DIRECTORIES.LOGS")
    log_file                            = app["CONFIG"].get("TREE.FILES.LOG")
    log_filepath                        = os.path.join(app_dir, log_rel_path, log_file)
    app["LOGGER"]                       = logger(
        app                             = app,
        file                            = log_filepath
    )

    #########################
    # APPLICATION ARGUMENTS #
    #########################
    app["LOGGER"].debug("Initializing arguments...")
    app["ARGUMENTS"]                    = args(
        configuration                   = app["CONFIG"]
    )

    #####################
    # APPLICATION CACHE #
    ##################### 
    app["LOGGER"].debug("Initializing application cache...")
    cache_rel_path                      = app["CONFIG"].get("TREE.DIRECTORIES.DATA")
    cache_file                          = app["CONFIG"].get("TREE.FILES.CACHE")
    cache_filepath                      = os.path.join(app_dir, cache_rel_path, cache_file)
    app["CACHE"]                        = cache.Cache(
        cache_file                      = cache_filepath
    )

    # Write arguments to cache
    app["LOGGER"].debug("Writing command line arguments to cache...")
    update_event                        = False
    arguments                           = vars(app["ARGUMENTS"])
    for k, v in arguments.items():
        if k in app["CACHE"].vars():
            if v is None:
                v = app["CACHE"].get(k)

            update_event                = app["CACHE"].update(**{
                k                       : v
            }) or update_event

    if update_event:
        app["CACHE"].save()

    ########################
    # APPLICATION LANGUAGE #
    ######################## 
    app["LOGGER"].debug("Initializing language modules...")
    lang_rel_path                       = app["CONFIG"].get("TREE.DIRECTORIES.LANGUAGE")
    lang_dir                            = os.path.join(app_dir, lang_rel_path)
    app["LANGUAGE"]                     = language.Language(
        directory                       = lang_dir,
        extension                       = app["CONFIG"].get("TREE.EXTENSIONS.LANGUAGE"),
        enabled                         = app["CONFIG"].language_modules()
    )

    #########################
    # APPLICATION TEMPLATES #
    #########################
    app["LOGGER"].debug("Initializing application templates...")
    temp_rel_path                       = app["CONFIG"].get("TREE.DIRECTORIES.TEMPLATES")
    temp_dir                            = os.path.join(app_dir, temp_rel_path)
    app["TEMPLATES"]                    = template.Template(
        directory                       = temp_dir,
        extension                       = app["CONFIG"].get("TREE.EXTENSIONS.TEMPLATE")
    )

    #####################
    # APPLICATION MODEL #
    #####################
    app["LOGGER"].debug("Initializing Gemini Model...")
    app["MODEL"]                        = model.Model(
        api_key                         = app["CONFIG"].get("GEMINI.KEY"),
        default_model                   = app["CONFIG"].get("GEMINI.DEFAULT"),
        tuning                          = app["CONFIG"].get("TUNING.ENABLED")
    )

    ########################
    # APPLICATION PERSONAS #
    ########################
    app["LOGGER"].debug("Initializing personas...")
    tune_rel_path                       = app["CONFIG"].get("TREE.DIRECTORIES.TUNING")
    sys_rel_path                        = app["CONFIG"].get("TREE.DIRECTORIES.SYSTEM")
    tune_dir                            = os.path.join(app_dir, tune_rel_path)
    sys_dir                             = os.path.join(app_dir, sys_rel_path)
    app["PERSONAS"]                     = persona.Persona(
        current                         = app["CACHE"].get("currentPersona"),
        config                          = app["CONFIG"].get("PERSONA"),
        tune_dir                        = tune_dir,
        tune_ext                        = app["CONFIG"].get("TREE.EXTENSIONS.TUNING"),
        sys_dir                         = sys_dir,
        sys_ext                         = app["CONFIG"].get("TREE.EXTENSIONS.TUNING")
    )            
    
    app["LOGGER"].debug("Application initialized!")
    app["LOGGER"].debug("--- Application Configuration")
    app["LOGGER"].debug(pprint.pformat(app["CONFIG"].vars()))
    app["LOGGER"].debug("--- Application Cache")
    app["LOGGER"].debug(pprint.pformat(app["CACHE"].vars()))
    app["LOGGER"].debug("--- Application Arguments")
    app["LOGGER"].debug(pprint.pformat(arguments))
    
    return app


def main() -> bool:
    """
    Main function to run the command-line interface.
    """
    app                                 = init()
    operations                          = {
        "summarize"                     : summarize,
        "converse"                      : converse,
        "configure"                     : configure,
        "review"                        : review,
        "request"                       : request,
        "tune"                          : tune,
        "analyze"                       : analyze
    }

    operation_name                      = app["ARGUMENTS"].operation

    if operation_name not in operations:
        return False 
    
    res                                 = operations[operation_name](app)
    arguments                           = vars(app["ARGUMENTS"]) 

    if "output" in arguments and app["ARGUMENTS"].output and "response" in res.keys():
        with open(app["ARGUMENTS"].output, "w") as out:
            out.write(res["response"])

    if "output" in arguments and app["ARGUMENTS"].output and  "summary" in res.keys():
        with open(app["ARGUMENTS"].output, "w") as out:
            out.write(res["summary"])

    if "show" in arguments and app["ARGUMENTS"].show:
        if "prompt" in res.keys():
            print(res["prompt"])

        if "summary" in res.keys():
            print(res["summary"])

        if "response" in res.keys():
            print(res["response"])

        if "vcs" in res.keys():
            print(res["vcs"])

if __name__ == "__main__":
    main()