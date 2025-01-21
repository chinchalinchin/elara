""" # main.py
Module for command line interface.
"""
# Standard Library Modules
import argparse
import logging
import os
import pathlib
import pprint

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
import object.structures as structures
import objects.template as template
import objects.terminal as terminal

# APPLICATION UTILITIES

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


def output(
    app                                 : dict,
    out                                 : dict,
    suppress_prompt                     : bool = True
):
    """
    
    :param arguments:
    :type arguments: argparse.Namespace
    :param response:
    :type response: dict
    """
    arg_map                             = vars(app["ARGUMENTS"])
    to_file                             = "output" in arg_map.keys() and arg_map["output"]
    to_screen                           = "show" in arg_map.keys() and arg_map["show"]
    prompt                              = "prompt" in out.keys() and arg_map["prompt"]
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
                app["CONFIG"].get("OUTPUT.PROMPT").format(
                    content             = out["prompt"]
                )
            )

        if response:
            print(
                app["CONFIG"].get("OUTPUT.RESPONSE").format(
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


## APPLICATION FUNCTIONS

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
    
    if app["ARGUMENTS"].render:
        return {
            "prompt"                    : parsed_prompt
        }
    
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
            if "=" not in item:
                app["LOGGER"].error(f"Invalid configuration format: {item}. Expected key=value.")
                continue
            
            key, value                  = item.split("=", 1)

            if key not in app["CONFIG"].data:
                app["LOGGER"].error(f"Invalid configuration key: {key}. Key not in configuration.")
                continue

            validated_value             = util.validate(value)

            if validated_value is None:
                app["LOGGER"].error(f"Invalidate configuration type: {key}={value}")
                continue 

            config[key]                 = validated_value

    if config:
        app["CONFIG"].update(**config)
        app["CONFIG"].save()
        app["LOGGER"].info(f"Updated configuration with: {config}")
        return config
    
    app["LOGGER"].warning("No configuration pairs provided.")
    return config


def converse(app: dict) -> dict:
    """
    Chat with one of Gemini's personas.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated prompt and model response.
    :rtype: dict
    """
    prompt                              = app["ARGUMENTS"].prompt
    
    if app["CACHE"].get("currentPersona") is None:
        converse_persona                = app["PERSONAS"].function("converse")
        app["CACHE"].update(**{
            "currentPersona"            : converse_persona
        })
        app["CACHE"].save()
        app["PERSONAS"].update(converse_persona)

    app["CONVERSATIONS"].update(
        persona                         = app["CACHE"].get("currentPersona"), 
        name                            = app["CACHE"].get("currentPrompter"), 
        text                            = prompt
    )
    
    template_vars                       = { 
        **app["CACHE"].vars(), 
        **app["LANGUAGE"].vars(),
        **app["PERSONAS"].vars(app["CACHE"].get("currentPersona")),
        **app["CONVERSATIONS"].vars(app["CACHE"].get("currentPersona"))
    }

    if app["ARGUMENTS"].directory is not None:
        app["LOGGER"].info("Injecting file summary into prompt...")
        template_vars.update(summarize(app))

    parsed_prompt                       = app["TEMPLATES"].render(
        temp                            = "conversation", 
        variables                       = template_vars
    )

    if app["ARGUMENTS"].render:
        return {
            "prompt"                    : parsed_prompt
        }
    
    response                            = app["MODEL"].respond(
        prompt                          = parsed_prompt, 
        model_name                      = app["CACHE"].get("currentModel"),
        generation_config               = app["PERSONAS"].get("generationConfig"),
        safety_settings                 = app["PERSONAS"].get("safetySettings"),
        tools                           = app["PERSONAS"].get("tools"),
        system_instruction              = app["PERSONAS"].get("systemInstruction")
    )

    app["CONVERSATIONS"].update(
        persona                         = app["CACHE"].get("currentPersona"), 
        name                            = app["CACHE"].get("currentPersona"), 
        text                            = response
    )

    return {
        "prompt"                        : parsed_prompt,
        "response"                      : response
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

    request_vars                         = { 
        **app["TERMINAL"].gherkin(), 
        **buffer 
    }
    
    parsed_prompt                       = app["TEMPLATES"].render("request", request_vars)
    
    if app["ARGUMENTS"].render:
        return {
            "prompt"                    : parsed_prompt
        }
    
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
        temp                            = app["CONFIG"].get("REVIEW.TEMPLATE"), 
        variables                       = review_variables
    )

    if app["ARGUMENTS"].render:
        return {
            "prompt"                    : review_prompt
        }
    
    review_config                       = app["PERSONAS"].get("generationConfig", persona)
    # @DEVELOPMENT
    #   HEY MILTON! We're testing structured output for your pull request reviews.
    #   What do you think!? Pretty neat, huh!?
    review_config.update({
        "response_schema"               : structures.Review,
        "response_mime_type"            : "application/json"
    })

    model_res                           = app["MODEL"].respond(
        prompt                          = review_prompt,
        generation_config               = review_config,
        model_name                      = app["CACHE"].get("currentModel"),
        safety_settings                 = app["PERSONAS"].get("safetySettings", persona),
        tools                           = app["PERSONAS"].get("tools", persona),
        system_instruction              = app["PERSONAS"].get("systemInstruction", persona)
    )

    source_res                          = source.comment(
        msg                             = model_res,
        pr                              = app["ARGUMENTS"].pull,
    )
    return {
        "prompt"                        : review_prompt,
        "response"                      : model_res,
        "vcs"                           : source_res
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

    summary                             = app["TEMPLATES"].render(
        temp                            = app["CONFIG"].get("SUMMARIZE.TEMPLATE"), 
        variable                        = summary_vars
    )
    
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
        tuned_models = []
        for p in app["PERSONAS"].all():
            if not app["CACHE"].is_tuned(p):
                res                     = app["MODEL"].tune(
                    display_name        = p,
                    tuning_model        = app["CONFIG"].get("TUNING.SOURCE"),
                    tuning_data         = app["PERSONA"].tuning(p)
                )
                tuned_models.append({
                    "name"              : p,
                    "version"           : app["CONFIG"].get("VERSION"),
                    "path"              : res.name
                })
        if tuned_models:
            app["CACHE"].update(**{
                "tunedModels"           : tuned_models
            })
            app["CACHE"].save()
            return True
    return False
    

# APPLICATION INITIALIZATION

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
    context_file                        = app["CONFIG"].get("TREE.FILES.CONTEXT")
    tune_dir                            = os.path.join(app_dir, tune_rel_path)
    sys_dir                             = os.path.join(app_dir, sys_rel_path)
    context_filepath                    = os.path.join(app_dir, data_dir, context_file)
    app["PERSONAS"]                     = persona.Persona(
        current                         = app["CACHE"].get("currentPersona"),
        config                          = app["CONFIG"].get("PERSONA"),
        context_file                    = context_filepath,
        tune_dir                        = tune_dir,
        tune_ext                        = app["CONFIG"].get("TREE.EXTENSIONS.TUNING"),
        sys_dir                         = sys_dir,
        sys_ext                         = app["CONFIG"].get("TREE.EXTENSIONS.TUNING")
    )            
    
    #############################
    # APPLICATION CONVERSATIONS #
    #############################
    app["LOGGER"].debug("Initialize chat histories...")
    hist_rel_path                       = app["CONFIG"].get("TREE.DIRECTORIES.HISTORY")
    hist_dir                            = os.path.join(app_dir, hist_rel_path)
    app["CONVERSATIONS"]                = conversation.Conversation(
        directory                       = hist_dir,
        extension                       = app["CONFIG"].get("TREE.EXTENSIONS.CONVERSATION"),
        tz_offset                       = app["CONFIG"].get("CONVERSATION.TIMEZONE_OFFSET")
    )

    ########################
    # APPLICATION TERMINAL #
    ########################
    app["LOGGER"].debug("Initialize interactive terminal...")
    app["TERMINAL"]                     = terminal.Terminal(
        terminal_config                 = app["CONFIG"].get("TERMINAL")
    )

    app["LOGGER"].debug("Application initialized!")
    app["LOGGER"].debug("--- Application Configuration")
    app["LOGGER"].debug(pprint.pformat(app["CONFIG"].vars()))
    app["LOGGER"].debug("--- Application Cache")
    app["LOGGER"].debug(pprint.pformat(app["CACHE"].vars()))
    app["LOGGER"].debug("--- Application Arguments")
    app["LOGGER"].debug(pprint.pformat(arguments))
    
    return app

# APPLICATION ENTRYPOINT

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
    arguments                           = vars(app["ARGUMENTS"]) 

    tty                                 = "interactive" in arguments \
                                            and arguments["interactive"]
    
    if operation_name not in operations:
        return False 
    
    if tty and operation_name == "converse": 
        app["ARGUMENTS"].show           = True
        app["TERMINAL"].interact(
            callable                    = converse,
            printer                     = output,
            app                         = app
        )
        return
        
    output(
        app                             = app,
        out                             = operations[operation_name](app),
        suppress_prompt                 = False
    )
    

if __name__ == "__main__":
    main()