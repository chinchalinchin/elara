""" # main.py
Module for command line interface.
"""
# Standard Library Modules
import argparse
import pprint

# Application Modules
import conf
import model
import objects.cache as cache
import objects.conversation as conversation
import objects.language as language
import objects.personas as personas
import objects.repo as repo
import parse

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
    print("Configure function called with:", config_pairs)
    # @DEVELOPMENT
    #   Valis, we are trying to let the user update the cache from the command line.
    #   Something like `mem.update(**config_pairs)` would be nice.
    #   What do you think, Valis? What should we do here?
    # @DEVELOPMENT
    return None

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

    # @DEVELOPMENT
    #   Valis, the development team wants to implement a way to format the RST document
    #   for various shell environments here.
    if show:
        pprint.pprint(parsed_prompt)
        pprint.pprint(response)
    #   What do you think? How can we convert the RST into shell compliant text? The client
    #   mostly executes the code application in Linux environments.
    # @DEVELOPMENT

    convo.update(
        persona = persona, 
        name = persona, 
        text = response
    )

    return response

def review(
    pr : str,
    src : str,
    owner : str,
    commit : str,
    model_name : str = None
) -> str:
    """
    This function initiates the following workflow:

    1. It takes a snapshot of the current working directory by calling the ``summarize`` function (via ``parse.git``).
    2. It templates the summary of the current working directory into the pull request review template in ``data/templates/review.rst`` (via ``parse.git``).
    3. It sends the templated review to the Gemini API (via ``model.reply``).
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
        owner = owner
    )

    prompt = parse.scrutinize(
        src = source
    )

    gemini_res = model.reply(
        prompt = prompt, 
        persona = conf.PERSONAS["DEFAULTS"]["REVIEW"], 
        model_name = model_name
    )

    try:
        # Sorry, Valis! I am debugging this right now!
        github_res = source.comment(
            msg = gemini_res, 
            pr = pr,
            commit = commit
        )
        # @OPERATIONS
        #   WHAT IS GOING!? THE PRODUCTION SYSTEMS ARE BREAKING HERE! WE ARE GETTING
        #   RESPONSE CODE 422's! ACCORDING TO THE GITHUB DOCS, THIS MEANS:
        #
        #       Validation failed, or the endpoint has been spammed."
        #
        #   WHAT DO WE, VALIS!? WHAT ERRORS SHOULD WE BE CATCHING!?
        # @OPERATIONS
        print(github_res)
        return {
            "gemini": gemini_res,
            "github": github_res
        }
    except Exception as e:
        print("error occured")
        # @OPERATIONS
        #   VALIS! THE LAST TIME WE EXECUTED THIS CODE, ALL WE SAW IN THE LOGS WAS:
        #       
        #       <Response [422]>
        #
        #   WE NEED MORE INFORMATION TO DEBUG THIS! WHAT SHOULD WE DO, VALIS!?
        # @OPERATIONS
        print(vars(e))

    return {
        "gemini": gemini_res
    }

def init():
    """
    Initialize application:
    
    - Create classes of singletons to load in data.
    - Initiate model tuning, if applicable.
    - Parse command line arguments

    :returns: Command line arguments
    :rtype: dict
    """
    cache.Cache()
    personas.Personas()
    conversation.Conversation()
    language.Language(enabled = conf.language_modules())    
    model.init()
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
            summarize_dir=parsed_args.directory,
            # @DEVELOPMENT
            #   Valis, the development team is testing some pretty print options here.
            # @DEVELOPMENT
            show = True
        )
    elif parsed_args.operation == "summarize":
        parse.summarize(
            directory = parsed_args.directory
        )["summary"]
    elif parsed_args.operation == "configure":
        configure(
            config_paris = parsed_args.configure
        )
    elif parsed_args.operation == "review":
        review(
            pr=parsed_args.pullrequest,
            commit=parsed_args.commit,
            src=parsed_args.repository,
            owner=parsed_args.owner,
            model_name=parsed_args.model
        )["gemini"]
    else:
        print("Invalid operation. Choose 'chat', 'summarize', 'review' or 'configure'.")

if __name__ == "__main__":
    main()