""" # main.py
Module for command line interface.
"""
# Standard Library Modules
import argparse
import logging
import os
import pathlib

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

logger = logging.getLogger(__name__)

def args( 
    configuration                       : config.Config
)                                       -> argparse.Namespace:
    """
    Parse and format command line arguments
    """
    parser                              = argparse.ArgumentParser(
        description                     = configuration.get("INTERFACE.HELP.PARSER")
    )
    
    for global_arg in configuration.get("INTERFACE.ARGUMENTS"):
        if "ACTION" in global_arg.keys():
            parser.add_argument(*global_arg["SYNTAX"],
                dest                    = global_arg["DEST"],
                help                    = global_arg["HELP"],
                action                  = global_arg["ACTION"]
            )
            continue
        parser.add_argument(*global_arg["SYNTAX"],
            dest                        = global_arg["DEST"],
            help                        = global_arg["HELP"],
            type                        = eval(global_arg["TYPE"])
        )

    subparsers                          = parser.add_subparsers(
        dest                            = 'operation', 
        help                            = configuration.get("INTERFACE.HELP.SUBPARSER")
    )

    for op, op_config in configuration.get("INTERFACE.OPERATIONS"):
        op_parser                       = subparsers.add_parser(
            name                        = op_config["NAME"],
            help                        = op_config["HELP"]
        )
        for op_arg in op["ARGUMENTS"]:
            if op_arg["SYNTAX"] == "nargs":
                op_parser.add_argument(
                    default             = op_arg["DEFAULT"],
                    dest                = op_arg["DEST"],
                    help                = op_arg["HELP"],
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


def configure(
    app                                 : dict
)                                       -> dict:
    """
    Parses and applies configuration settings.
    """
    config                              = {}

    if app["ARGUMENTS"].config:
        for item in app["ARGUMENTS"].config:
            try:
                key, value              = item.split("=", 1)
                config[key]             = value
            except ValueError:
                logger.error(f"Invalid configuration format: {item}. Expected key=value.")
                continue

        app["CONFIG"].update(**config)
        app["CONFIG"].save()
        logger.info(f"Updated configuration with: {config}")
        return config
    
    logger.warning("No configuration pairs provided.")
    return {
        "response"                      : config
    }


def converse(
    app                                 : dict
)                                       -> str:
    """
    Chat with one of Gemini's personas.

    :param prompt: Prompt to send.
    :type prompt: str
    :param persona: Persona with which to converse. If no `persona` is provided, it will be retrieved from the cache.
    :type persona: str
    :param model_name: Gemini model to use. If no `model_name` is provided, it will be retrieved from teh cache.
    :type model_type: str
    :param summarize_dir: Directory of additional context to inject into prompt. If this argument is provided, an RST formatted summary of a directory will be generated using `parse.summarize()` and injected into the prompt.
    :type summarize_dir: str
    :param show: A flag signaling whether the prompt and response should be printed to screen.
    :returns: The persona's response to the prompt.
    :rtype: str
    """
    convo = conversation.Conversation()

    convo.update(
        persona                         = app["CACHE"].get("currentPersona"), 
        name                            = app["CACHE"].get("currentPrompter"), 
        text                            = app["ARGUMENTS"].get("prompt")
    )
    
    template_vars                       = { 
        **app["CACHE"].vars(), 
        **app["LANGUAGE"].vars(),
        **convo.vars()
    }

    if app["ARGUMENTS"].get("directory") is not None:
        template_vars.update(
            summarize(
                directory               = app["ARGUMENTS"].get("directory"),
                stringify               = True
            )
        )

    parsed_prompt                       = app["TEMPLATES"].render(
        temp                            = "conversation", 
        variables                       = template_vars
    )

    persona                             = app["CACHE"].get("currentPersona"), 

    response                            = app["MODEL"].respond(
        prompt                          = parsed_prompt, 
        model_name                      = app["CACHE"].get("currentModel")
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


def analyze(
    app                                 : dict
)                                       -> str:
    """
    This function injects the contents of a directory containing only RST documents into the ``data/templates/deduce.rst`` template. It then sends this contextualized prompt to the Gemini API persona of *Axiom*.
    """
    buffer                              = app["CACHE"].vars()
    buffer["currentPersona"]            = app["PERSONAS"].function("analyze")

    analyze_vars                        = {
        **buffer,
        **summarize(app),
        **app["LANGUAGE"].vars(),
        **{ "latex": app["CONFIG"].get("ANALYZE.LATEX_PREAMBLE") }
    }

    parsed_prompt                       = app["TEMPLATES"].render(
        temp                            = "analysis", 
        variables                        = analyze_vars
    )

    response                            = model.reply(
        prompt                          = parsed_prompt,
        persona                         = app["PERSONAS"].get("analyze"),
        model_name                      = app["CACHE"].get("currentModel")
    )
    
    return {
        "prompt"                        : parsed_prompt,
        "response"                      : response
    }


def review(
    app                                 : dict
)                                       -> str:
    """

    """
    source                              = repo.Repo(
        repo                            = app["ARGUMENTS"].get("repository"),
        owner                           = app["ARGUMENTS"].get("owner"),
        commit                          = app["ARGUMENTS"].get("commit")
    )

    buffer                              = app["CACHE"].vars()
    buffer["currentPersona"]            = app["PERSONAS"].function("review")

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
        persona                         = buffer["currentPersona"],
        model_name                      = buffer["currentModel"],
    )

    source_res                          = source.comment(
        msg                             = model_res, 
        pr                              = app["ARGUMENTS"].pull,
        # @DEVELOPMENT
        #   Hey, Milton, we need to figure out a way to iterate over the file
        #   paths in Gemini's output (i.e. your output!). 
        #   
        #   We might need to post a batch comment to the Gitub Rest API, if you 
        #   decide to flag multiple files for review. Right now the comments are only 
        #   being appended to the README.md file.
        #
        #   Everyone on the development team has been looking for the correct endpoint
        #   and request body format to use to accomplish this. We might need to
        #   overhaul the ``comment()`` function to accomplish this!
        #
        #   However, the crux of the issue is parsing Gemini's response. 
        #   We need a clever way to pull the file name from the response, Milton!
        path                            = "README.md"
    )
    return {
        "prompt"                        : review_prompt,
        "response"                      : model_res,
        "vcs"                           : source_res
    }


def summarize(app : dict) -> str:
    """
    
    """
    local_dir                           = app["ARGUMENTS"].get("directory")

    dir                                 = directory.Directory(
        directory                       = local_dir,
        summary_file                    = app["CONFIG"].get("TREE.FILES.SUMMARY"),
        summary_includes                = app["CONFIG"].get("SUMMARIZE.INCLDUES"),
        summary_directives              = app["CONFIG"].get("SUMMARIZE.DIRECTIVES")
    )

    summary_vars                        = dir.summary()

    summary                             = app["TEMPLATES"].render("summary", summary_vars)
    
    return                              { 
        "response"                      : summary
    }


def tune(app : dict) -> bool:
    """
    Initialize tuned personas if tuning is enabled through the ``TUNING`` environment variable.

    :returns: A flag to signal if a tuning event occured.
    :rtype: bool
    """
    
    if app["CONFIG"].get("TUNING.ENABLED"):
        for p in app["PERSONAS"].all():
                res                     = app["MODEL"].tune(
                    display_name        = p,
                    tuning_model        = app["CONFIG"].get("TUNING.SOURCE"),
                    tuning_data         = app["PERSONA"].tuning(p)
                )
                app["CACHE"].update({
                    "tunedModels"       : [{
                        "name"          : p,
                        "version"       : app["CONFIG"].get("VERSION"),
                        "path"          : res.name
                    }]
                })
                app["CACHE"].save()
    return app["CACHE"].get("tunedModels")
    

def init():
    """
    Initialize application.

    :returns: Application configuration.
    :rtype: dict
    """

    app                                 = {}
    app_dir                             = pathlib.Path(__file__).resolve().parent
    app["CONFIG"]                       = config.Config(app_dir)

    app["ARGUMENTS"]                    = args(
        configuration                   = app["CONFIG"]
    )

    cache_rel_path                      = app["CONFIG"].get("TREE.DIRECTORIES.DATA")
    cache_file_name                     = app["CONFIG"].get("TREE.FILES.CACHE")
    cache_dir                           = os.path.join(app_dir, cache_rel_path, cache_file_name)
    app["CACHE"]                        = cache.Cache(cache_dir)

    update_event                        = False
    if app["ARGUMENTS"].persona:
        update_event                    = app["CACHE"].update({ 
            "currentPersona"            : app["ARGUMENTS"].persona 
        }) or update_event

    if app["ARGUMENTS"].prompter:
        update_event                    = app["CACHE"].update({ 
            "currentPrompter"           : app["ARGUMENTS"].prompter 
        }) or update_event

    if app["ARGUMENTS"].model_name:
        update_event                    = app["CACHE"].update({ 
            "currentModel"              : app["ARGUMENTS"].model_name 
        }) or update_event
        
    if update_event:
        app["CACHE"].save()

    lang_rel_path                       = app["CONFIG"].get("TREE.DIRECTORIES.LANGUAGE")
    lang_dir                            = os.path.join(app_dir, lang_rel_path)
    app["LANGUAGE"]                     = language.Language(
        directory                       = lang_dir,
        extension                       = app["CONFIG"].get("TREE.EXTENSIONS.LANGUAGE"),
        enabled                         = app["CONFIG"].language_modules()
    )

    temp_rel_path                       = app["CONFIG"].get("TREE.DIRECTORIES.TEMPLATES")
    temp_dir                            = os.path.join(app_dir, temp_rel_path)
    app["TEMPLATES"]                    = template.Template(
        directory                       = temp_dir,
        extension                       = app["CONFIG"].get("TREE.EXTENSIONS.TEMPLATE")
    )

    app["MODEL"]                        = model.Model(
        api_key                         = app["CONFIG"].get("GEMINI_KEY"),
        tuning                          = app["CONFIG"].get("TUNING")
    )

    app["PERSONAS"]                      = persona.Persona(
        current                         = app["CACHE"].get("currentPersona"),
        config                          = app["CONFIG"].get("PERSONA"),
        tune_dir                        = app["CONFIG"].get("TREE.DIRECTORIES.TUNING"),
        tune_ext                        = app["CONFIG"].get("TREE.EXTENSIONS.TUNING"),
        sys_dir                         = app["CONFIG"].get("TREE.DIRECTORIES.SYSTEM"),
        sys_ext                         = app["CONFIG"].get("TREE.EXTENSIONS.TUNING")
    )            
    
    if app["CONFIG"].get("DEBUG"):
        print(app)

    return app

def main():
    """
    Main function to run the command-line interface.
    """
    app                                 = init()
    res                                 = exec(app["OPERATION"], app)

    if app["ARGUMENTS"].output:
        with open(app["ARGUMENTS"].output, "w") as out:
            out.write(res["response"])

    if app["ARGUMENTS"].show and "prompt" in res.keys():
        print(res["prompt"])

    if app["ARGUMENTS"].show and "response" in res.keys():
        print(res["response"])

if __name__ == "__main__":
    main()