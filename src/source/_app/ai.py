import argparse
import os

import google.generativeai as genai

# Configure the logger to only show errors

api_key = os.environ.get("GEMINI_KEY")
model_type = os.environ.setdefault("GEMINI_MODEL", "gemini-1.5-pro")

if api_key is None:
  raise ValueError("GEMINI_KEY environment variable not set.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_type)

preamble = """
The following prompt contains our conversation history as additional context. My prompts are denoted by $$ .. $$ markers. Your responses are denoted with && .. && markers.  These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest. \n\n
"""

def format_prompt(prompt):
    return f"\n$$\n{prompt}\n$$"

def format_response(response):
    return f"\n&&\n{response}\n&&"

def args():
    """Parses the -c argument for a string and returns it."""

    parser = argparse.ArgumentParser(description="Process a string argument.")
    parser.add_argument(
        "-c", 
        "--string", 
        type=str, 
        help="Input string"
    )
    parser.add_argument(
        "-f",
        "--context_file",
        type=str,
        default="context.txt",
        help="Path to the context file",
    )
    args = parser.parse_args()
    return args.string, args.context_file

def talk_to_gemini(prompt, context_file="context.txt"):
    """Sends the prompt to Gemini, managing context with an external file."""

    if os.path.exists(context_file):
        with open(context_file, "r") as f:
            context = f.read()
        full_prompt = preamble + context + format_prompt(prompt)
    else:
        full_prompt = format_prompt(prompt)

    response = model.generate_content(full_prompt) 
    print(response.text)

    context = append_to_context(prompt, response.text, context_file)
    return context

def append_to_context(prompt, response, context_file="context.txt"):
    """Appends the prompt and response to the context file."""

    if not os.path.exists(context_file):
        with open(context_file, "w") as f:
            pass  

    with open(context_file, "a") as f:
        f.write(format_prompt(prompt))
        f.write(format_response(response))

    with open(context_file, "r") as f:
        context = f.read()
    return context

if __name__ == "__main__":
    string_arg, context_file = args()  # Get both values
    if string_arg:
        talk_to_gemini(string_arg, context_file)
        exit()
    print("No string provided with the -c argument.")