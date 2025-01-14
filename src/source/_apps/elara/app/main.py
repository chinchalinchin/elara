""" # main.py
Module for command line parsing.
"""
# Standard Library Imports 
import argparse

# Application Module Imports
import conf
import experiment
import model
import parse

def args():
    parser = argparse.ArgumentParser(description="Interact with Gemini.")
    for arg in conf.ARGUMENTS: 
        if arg["mode"] == "name":
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

def chat(prompt, context, model_type=conf.DEFAULTS["MODEL"]):
    """
    Chat with Gemini
    """
    parsed_prompt = parse.contextualize(prompt, context)
    response = model.reply(parsed_prompt, model_type)
    context = parse.persist(prompt, response, context)
    return response

def main():
    """
    Main function to run the command-line interface.
    """
    parse.init()
    parsed_args = args()
    if parsed_args.operation == "chat":
        res = chat(parsed_args.prompt, parsed_args.context, parsed_args.model)
        print(res)
    elif parsed_args.operation == "conduct":
        experiment.conduct(parsed_args.experiment)
    elif parsed_args.operation == "summarize":
        parse.summarize(parsed_args.directory)
    else:
        print("Invalid operation. Choose 'chat', 'conduct', or 'summarize'.")

if __name__ == "__main__":
    main()