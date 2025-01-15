""" # main.py
Module for command line interface.
"""
# Standard Library Modules
import argparse

# Application Modules
import conf
import model
import objects.cache as cache
import objects.conversation as conversation
import objects.personas as personas
import parse

def args():
    """
    Parse and format command line arguments
    """
    parser = argparse.ArgumentParser(description="Interact with Gemini.")
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

def configure(config_pairs):
    """
    Parses and applies configuration settings.
    """
    print("Configure function called with:", config_pairs)  # Placeholder
    return None

def chat(
    prompt,
    persona=None,
    prompter=None,
    model_type=None, 
    summarize_dir=None
):
    """
    Chat with Gemini
    """
    mem = cache.Cache().get()
    convo = conversation.Conversation()

    if model_type is None:
        model_type = mem["currentModel"]

    if persona is None:
        persona = mem["template"]["currentPersona"]

    if prompter is None:
        prompter = mem["template"]["currentPrompter"]

    convo.update(persona, prompter, prompt)
    parsed_prompt = parse.contextualize(prompt, summarize_dir)
    response = model.reply(parsed_prompt, model_type)
    convo.update(persona, persona, response)

    return response

def init():
    """
    Initialize application
    """
    mem = cache.Cache().get()
    per = personas.Persona(current=mem["template"]["currentPersona"]).get()
    model.init()
    return args()

def main():
    """
    Main function to run the command-line interface.
    """
    parsed_args = init()
    if parsed_args.operation == "chat":
        res = chat(parsed_args.prompt, parsed_args.model)
        print(res)
    elif parsed_args.operation == "summarize":
        parse.summarize(parsed_args.directory)
    elif parsed_args.operation == "configure":
        configure(parsed_args.configure)
    else:
        print("Invalid operation. Choose 'chat', 'conduct', 'summarize', or 'configure'.")

if __name__ == "__main__":
    main()