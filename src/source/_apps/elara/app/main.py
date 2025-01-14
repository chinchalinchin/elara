""" # main.py
Module for command line interface.
"""
# Standard Library Modules
import argparse

# Application Modules
import conf
import experiment
import model
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
    model_type=None, 
    summarize_dir=None
):
    """
    Chat with Gemini
    """
    cache = parse.load_cache()

    if model_type is None:
        model_type = cache["currentModel"]

    parsed_prompt = parse.contextualize(prompt, summarize_dir)
    response = model.reply(parsed_prompt, model_type)
    _ = parse.persist(response)

    return response

def init():
    """
    Initialize application
    """
    parse.init()
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
    elif parsed_args.operation == "conduct":
        experiment.conduct(parsed_args.experiment)
    elif parsed_args.operation == "summarize":
        parse.summarize(parsed_args.directory)
    elif parsed_args.operation == "configure":
        configure(parsed_args.configure)
    else:
        print("Invalid operation. Choose 'chat', 'conduct', 'summarize', or 'configure'.")

if __name__ == "__main__":
    main()