""" # main.py
Module for command line interface.
"""
# Standard Library Modules
import argparse

# Application Modules
import conf
import git
import model
import objects.cache as cache
import objects.conversation as conversation
import objects.language as language
import objects.personas as personas
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
                    nargs=arg["nargs"],
                    help=arg["help"]
                )
            else:
                parser.add_argument(
                    arg["syntax"],
                    choices=arg["choices"],
                    help=arg["help"]
                )
        elif arg["mode"] == "flag":
            parser.add_argument(
                *arg["syntax"], 
                type=arg["type"],
                default=arg["default"],
                help=arg["help"]
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
    # TODO: allow user to update cache.
    # TODO: something like `mem.update(**config_pairs)` would be nice.
    return None

def chat(
    prompt : str,
    persona : str = None,
    prompter : str = None,
    model_name : str = None, 
    summarize_dir : str = None
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

    convo.update(persona, prompter, prompt)
    parsed_prompt = parse.contextualize(persona, summarize_dir)
    response = model.reply(parsed_prompt, persona, model_name)
    convo.update(persona, persona, response)

    return response

def review(
    pr_number : str,
    branch : str ,
    model_type : str = conf.DEFAULTS["MODEL"],
    persona : str = conf.DEFAULTS["PERSONA"],
) -> str:
    """
    Placeholder for the code review logic.
    """
    source = repo.Repo()


    review_comment = model.reply(prompt, persona=persona, model_name=model_type)
    # 1. Get current working directory
    # 2. Call parse.summarize to get RST string of git repo
    # 3. Call model.reply to send RST string to Gemini
    # 4. Take respond and add to pull request

    # NOTE: In step 4, we will probably need to use the Github API to post the comment to Github.
    #       Look up libraries we can use. I am hoping there is something simple we can install
    #       to accomplish this. If not, we will have to construct the POST request ourselves.
    return "placeholder"

def init():
    """
    Initialize application:
    
    - Create classes of singletons to load in data.
    - Initiate model tuning, if applicable.
    - Parse command line arguments

    :returns: Command line arguments
    :rtype: dict
    """
    # Initialize application objects
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
        print(
            chat(
                prompt=parsed_args.prompt, 
                model_type=parsed_args.model,
                prompter=parsed_args.self,
                persona=parsed_args.persona,
                summarize_dir=parsed_args.directory
            )
        )
    elif parsed_args.operation == "summarize":
        parse.summarize(
            directory = parsed_args.directory
        )
    elif parsed_args.operation == "configure":
        configure(
            config_paris = parsed_args.configure
        )
    elif parsed_args.operation == "review":
        git.review(
            branch=parsed_args.branch,
            pr_number=parsed_args.pr,
            model_type=parsed_args.model,
            persona=parsed_args.persona
        )
    else:
        print("Invalid operation. Choose 'chat', 'summarize', 'review' or 'configure'.")

if __name__ == "__main__":
    main()