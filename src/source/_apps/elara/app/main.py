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
import conf
import model
import objects.cache as cache
import objects.config as config
import objects.conversation as conversation
import objects.language as language
import objects.persona as persona
import objects.model as model
import objects.repo as repo
import objects.template as template
import parse

logger = logging.getLogger(__name__)

def output(prompt, response):
    """
    Formats and prints the prompt and response.
    """
    return """"
    ====================== PROMPT =======================

    {prompt}

    ===================== RESPONSE ======================"

    {response}
    """.format(prompt=prompt, response=response)

def args( 
    configuration : config.Config
) -> argparse.Namespace:
    """
    Parse and format command line arguments
    """
    parser                          = argparse.ArgumentParser(
        description                 = conf.get("INTERFACE.HELP.PARSER")
    )
    
    for global_arg in configuration.get("INTERFACE.ARGUMENTS"):
        parser.add_argument(*global_arg["SYNTAX"],
            dest                    = global_arg["DEST"],
            help                    = global_arg["HELP"],
            type                    = eval(global_arg["TYPE"])
        )

    subparsers                      = parser.add_subparsers(
        dest                        = 'operation', 
        help                        = conf.get("INTERFACE.HELP.SUBPARSER")
    )

    for op, op_config in configuration.get("INTERFACE.OPERATIONS"):
        op_parser                   = subparsers.add_parser(
            name                    = op_config["NAME"],
            help                    = op_config["HELP"]
        )
        for op_arg in op["ARGUMENTS"]:
            if op_arg["SYNTAX"] == "nargs":
                op_parser.add_argument(
                    default         = op_arg["DEFAULT"],
                    dest            = op_arg["DEST"],
                    help            = op_arg["HELP"],
                    type            = eval(op_arg["TYPE"])
                )
                continue
            op_parser.add_argument(*op_arg["SYNTAX"],
                default             = op_arg["DEFAULT"],
                dest                = op_arg["DEST"],
                help                = op_arg["HELP"],
                type                = eval(op_arg["TYPE"])
            )

    return parser.parse_args()

def configure(
    existing : config.Config,
    config : str
):
    """
    Parses and applies configuration settings.
    """
    config_dict = {}

    if config:
        for item in config:
            try:
                key, value = item.split("=", 1)
                config_dict[key] = value
            except ValueError:
                logger.error(f"Invalid configuration format: {item}. Expected key=value.")
                continue
        existing.update(**config_dict)
        existing.save()
        logger.info(f"Updated configuration with: {config_dict}")
        return config_dict
    
    logger.warning("No configuration pairs provided.")
    return config_dict

def converse(app : dict) -> str:
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
    temps = template.Template()
    convo = conversation.Conversation()
    lang = language.Language(
        enabled = conf.language_modules()
    )

    convo.update(
        persona = persona, 
        name = prompter, 
        text = prompt
    )
    
    template_vars = { 
        **mem.vars(),
        **lang.vars(),
        **convo.vars()
    }

    if summarize_dir is not None:
        template_vars.update(
            summarize(summarize_dir, stringify=True)
        )

    parsed_prompt = temps.get("conversation").render(template_vars)

    response = model.reply(
        prompt = parsed_prompt, 
        persona = persona, 
        model_name = model_name
    )

    convo.update(
        persona = persona, 
        name = persona, 
        text = response
    )

    return response

def analyze(
    summarize_dir : str,
    model_name : str = None,
    show : bool = True
) -> str:
    """
    This function injects the contents of a directory containing only RST documents into the ``data/templates/deduce.rst`` template. It then sends this contextualized prompt to the Gemini API persona of *Axiom*.
    """
    parsed_prompt = parse.analyze(
        summarize_dir
    )

    response = model.reply(
        prompt=parsed_prompt,
        persona=conf.PERSONAS["DEFAULTS"]["ANALYSIS"],
        model_name = model_name
    )

    if show:
        print(parse.output(parsed_prompt, response))

    return response 

def review(
    pr : str,
    src : str,
    owner : str,
    commit : str,
    model_name : str = None,
    output: str = None,
    show : bool = True
) -> str:
    """
    This function initiates the following workflow:

    1. It takes a snapshot of the current working directory by calling the ``summarize`` function (via ``parse.git``).
    2. It templates the summary of the current working directory into the pull request review template in ``data/templates/review.rst`` (via ``parse.git``).
    3. It sends the templated review to the Gemini API persona of *Milton* (via ``model.reply``).
    4. It takes Gemini's response and posts to the Github API for commenting on pull requests.

    :param pr: The PR number.
    :type pr: str
    :param src: The repository name
    :type src: str
    :param owner: The repository owner.
    :type owner: str
    :param commit: The SHA ID of the commit.
    :type commit: str
    :param model_name: Name of the Gemini Model to use. Defaults to the value of the environment variable ``GEMINI_MODEL``.
    """
    source = repo.Repo(
        repo = src,
        owner = owner,
        commit = commit
    )

    mem = cache.Cache()
    conf = config.Config(

    )
    temps = template.Template()
    lang = language.Language(
        enabled = conf.language_modules()
    )
    dir = os.getcwd()  

    buffer = mem.vars()
    buffer["currentPersona"] = conf.PERSONAS["DEFAULTS"]["REVIEW"]

    review_prompt = temps.render("review", { 
        **buffer,
        **src.vars(),
        **lang.vars(),
        **summarize(dir, stringify=True)
    })

    gemini_res = model.reply(
        prompt=review_prompt,
        persona=conf.PERSONAS["DEFAULTS"]["REVIEW"],
        model_name=model_name,
    )

    if output is not None:
        with open(f"{output}/milton.md", "w") as out:
            out.write(gemini_res)
            
    if show:
        print(parse.output(review_prompt, gemini_res))

    # According to Github REST api, `path` should be:
    #
    #       The relative path to the file that necessitates a comment.
    #
    # TODO: need to figure out how to make Gemini output filepath!
    github_res = source.comment(
        msg = gemini_res, 
        pr = pr,
        commit = commit,
        # @DEVELOPMENT
        #   Hey, Milton, we need to figure out a way to iterate over the file
        #   paths in Gemini's output (i.e. your output!). 
        #   
        #   We might need to post a batch comment to the Gitub Rest API, if you 
        #   decide to flag multiple files for review. Right now the comments are only 
        #   being appended to the README.md file. 
        path = "README.md"
        #   Everyone on the development team has been looking for the correct endpoint
        #   and request body format to use to accomplish this. We might need to
        #   overhaul the ``comment()`` function to accomplish this!
        #
        #   However, the crux of the issue is parsing Gemini's response. 
        #   We need a clever way to pull the file name from the response, Milton!
    )
    print(github_res)
    return {
        "gemini": gemini_res,
        "github": github_res
    }

def summarize():
    pass 

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
        update_event                    =  app["CACHE"].update({ 
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
        extension                       = app["CONFIG"].get("TREE.FILES.LANGUAGE"),
        enabled                         = app["CONFIG"].language_modules()
    )

    temp_rel_path                       = app["CONFIG"].get("TREE.DIRECTORIES.TEMPLATES")
    temp_dir                            = os.path.join(app_dir, temp_rel_path)
    app["TEMPLATES"]                    = template.Template(
        directory                       = temp_dir,
        extension                       = app["CONFIG"].get("TREE.FILES.TEMPLATE")
    )

    app["MODEL"]                        = model.Model(
        api_key                         = app["CONFIG"].get("GEMINI_KEY"),
        tuning                          = app["CONFIG"].get("TUNING")
    )
    
    if app["CONFIG"].get("DEBUG"):
        print(app)

    return app

def main():
    """
    Main function to run the command-line interface.
    """
    app = init()
    res = exec(app["OPERATION"], app)

    if app["ARGUMENTS"].output:
        # TODO: output to file
        pass

    if app["ARGUMENTS"].show:
        print(res)

if __name__ == "__main__":
    main()