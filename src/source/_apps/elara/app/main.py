""" # main.py
Module for command line interface.
"""
# Standard Library Modules
import argparse
import logging

# Application Modules
import conf
import model
import objects.cache as cache
import objects.conversation as conversation
import objects.language as language
import objects.personas as personas
import objects.repo as repo
import parse

logger = logging.getLogger(__name__)

def args():
    """
    Parse and format command line arguments
    """
    parser = argparse.ArgumentParser(description="Plumb the depths of generative AI.")
    for arg in conf.ARGUMENTS: 
        if arg["mode"] == "name":
            if "nargs" in arg:
                parser.add_argument(
                    arg["syntax"],
                    nargs = arg["nargs"],
                    help = arg["help"]
                )
            else:
                parser.add_argument(
                    arg["syntax"],
                    choices = arg["choices"],
                    help = arg["help"]
                )
        elif arg["mode"] == "flag":
            parser.add_argument(
                *arg["syntax"], 
                type = arg["type"],
                default = arg["default"],
                help = arg["help"]
            )
    args = parser.parse_args()
    return args

def configure(
    config_pairs
):
    """
    Parses and applies configuration settings.
    """
    mem = cache.Cache()
    if config_pairs:
        config_dict = {}
        for item in config_pairs:
            try:
                key, value = item.split("=", 1)
                config_dict[key] = value
            except ValueError:
                logger.error(f"Invalid configuration format: {item}. Expected key=value.")
                continue
        mem.update(**config_dict)
        mem.save()
        logger.info(f"Updated configuration with: {config_dict}")
    else:
        logger.warning("No configuration pairs provided.")
    return config_dict

def chat(
    prompt : str,
    persona : str = None,
    prompter : str = None,
    model_name : str = None, 
    summarize_dir : str = None,
    show : bool = True
) -> str:
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
    mem = cache.Cache()
    convo = conversation.Conversation()

    if model_name is None:
        model_name = mem.get("currentModel")

    if persona is None:
        persona = mem.get("currentPersona")

    if prompter is None:
        prompter = mem.get("currentPrompter")

    convo.update(
        persona = persona, 
        name = prompter, 
        text = prompt
    )
    
    parsed_prompt = parse.contextualize(
        persona = persona, 
        summarize_dir = summarize_dir
    )

    response = model.reply(
        prompt = parsed_prompt, 
        persona = persona, 
        model_name = model_name
    )

    if show:
        print(parse.output(parsed_prompt, response))

    convo.update(
        persona = persona, 
        name = persona, 
        text = response
    )

    return response

def analysis(
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

    try:
        prompt = parse.scrutinize(src=source)
    except Exception as e:
        logger.error(f"Error in scrutinize: {e}")
        return {
           "status": "failed",
           "error": str(e)
        }

    try:
        gemini_res = model.reply(
            prompt=prompt,
            persona=conf.PERSONAS["DEFAULTS"]["REVIEW"],
            model_name=model_name,
        )
    except Exception as e:
        logger.error(f"Error in model.reply: {e}")
        return {
           "status": "failed",
           "error": str(e)
        }

    if show:
        print(parse.output(prompt, gemini_res))

    try:
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
            #   paths in Gemini's output (i.e. your output!). We might need to post 
            #   a batch comment to the Gitub Rest API, if you decide to flag multiple 
            #   files for review. Right now the comments are only being appended to 
            #   the README.md file. 
            path = "README.md"
            #   Everyone on the development has been looking for the correct endpoint
            #   and request body format to use to accomplish this. We might need to
            #   overhaul the ``comment()`` function to accomplish this!
            # @DEVELOPMENT
        )
        print(github_res)
        return {
            "gemini": gemini_res,
            "github": github_res
        }
    except Exception as e:
        print("error occured")

    return {
        "gemini": gemini_res
    }

def init(
    debug : bool = conf.DEBUG
):
    """
    Initialize application:
    
    - Create classes of singletons to load in data.
    - Initiate model tuning, if applicable.
    - Parse command line arguments

    :returns: Command line arguments
    :rtype: dict
    """
    mem = cache.Cache()
    personas.Personas()
    conversation.Conversation()
    language.Language(enabled = conf.language_modules())    
    model.init()
    
    if debug:
        print(vars(mem))

    return args()

def main():
    """
    Main function to run the command-line interface.
    """
    parsed_args = init()
    if parsed_args.operation == "chat":
        chat(
            prompt=parsed_args.prompt, 
            model_name=parsed_args.model,
            prompter=parsed_args.self,
            persona=parsed_args.persona,
            summarize_dir=parsed_args.dir,
            show = True
        )
    elif parsed_args.operation == "summarize":
        parse.summarize(
            directory = parsed_args.dir
        )
    elif parsed_args.operation == "configure":
        configure(
            config_paris = parsed_args.configure
        )
    elif parsed_args.operation == "analyze":
        analysis(
            summarize_dir=parsed_args.dir,
            model_name=parsed_args.model,
            show = True
        )
    elif parsed_args.operation == "review":
        res = review(
            pr=parsed_args.pullrequest,
            commit=parsed_args.commit,
            src=parsed_args.repository,
            owner=parsed_args.owner,
            model_name=parsed_args.model,
            show = True
        )
        if res["github"]["status"] == "failed":
           print(f"Error posting comment to Github: {res['github']['error']}")
    else:
        print("Invalid operation. Choose 'chat', 'summarize', 'review' or 'configure'.")

if __name__ == "__main__":
    main()