""" # main.py
Module for command line parsing.
"""

import argparse
import os 

import experiment
import model
import parse

DEFAULT_PROMPT = "Hello Gemini! Form is the possibility of structure!"

arguments = [{
    "mode": "name",
    "syntax": "operation",
    "choices": ["chat", "conduct", "summarize"],
    "help": "The operation to perform (chat, conduct)"
},{
    "mode": "flag",
    "syntax": ["-p", "--prompt"],
    "type": str,
    "default": DEFAULT_PROMPT,
    "help": "Input string for chat operation."
},{
    "mode": "flag",
    "syntax": ["-c", "--context"],
    "type": str,
    "default": parse.DEFAULT_CONTEXT,
    "help": "Override the default context file."
},{
    "mode": "flag",
    "syntax": ["-e", "--experiment"],
    "type": str,
    "default": experiment.DEFAULT_EXPERIMENT,
    "help": "Input experiment for conduct operation."
},{
    "mode": "flag",
    "syntax": ["-m", "--model"],
    "type": str,
    "default": model.DEFAULT_MODEL,
    "help": "Input model for Gemini API."
},{
    "mode": "flag",
    "syntax": ["-d", "--directory"],
    "default": parse.DEFAULT_SUMMARY,
    "type": str,
    "help": "The path to the directory to summarize. Required for 'summarize' operation."
}]

def args():
    parser = argparse.ArgumentParser(description="Interact with Gemini.")
    for arg in arguments: 
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

def chat(prompt, context, model_type=model.DEFAULT_MODEL):
    """Chat with Gemini"""
    parsed_prompt = parse.prefix(prompt, context)
    response = model.reply(parsed_prompt, model_type)
    context = parse.persist(prompt, response, context)
    return response

def main():
    """
    Main function to run the command-line interface.
    """
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