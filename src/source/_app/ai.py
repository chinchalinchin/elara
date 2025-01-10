import argparse
import os
import time

import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
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
    """Parses the arguments."""

    parser = argparse.ArgumentParser(description="Interact with Gemini.")
    parser.add_argument(
        "operation", 
        choices=["chat", "experiment"], 
        help="The operation to perform (chat or experiment)"
    )
    parser.add_argument(
        "-c", 
        "--string", 
        type=str, 
        help="Input string (for chat operation)"
    )
    parser.add_argument(
        "-f",
        "--context_file",
        type=str,
        default="context.txt",
        help="Path to the context file",
    )
    parser.add_argument(
        "--exp-name",
        type=str,
        help="Name of the experiment (for experiment operation)"
    )
    args = parser.parse_args()
    return args

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

def experiment(choice):
    """Conducts an experiment based on the given choice."""

    if choice == "duality":
        duality()

def duality(exp_name="duality", max_cycles = 20, max_delay = 60):
    """
    Conducts the 'duality' experiment with exponential backoff, 
    separate error handling, and correct sleep placement.
    """
    context_A = preamble
    context_B = preamble
    cycle = 0
    initial_prompt = "Form is the possibility of structure."
    delay = 1  # Initial delay in seconds

    # Initial interaction
    response_A = model.generate_content(context_A + format_prompt(initial_prompt)).text
    context_A += format_prompt(initial_prompt) + format_response(response_A)

    while cycle < max_cycles:
        time.sleep(delay)  # Sleep at the beginning of the loop

        # A talks to B
        try:
            response_B = model.generate_content(context_B + format_prompt(response_A)).text
            context_B += format_prompt(response_A) + format_response(response_B)
        except ResourceExhausted:
            print(f"Rate limit hit for model B. Increasing delay to {delay * 2} seconds.")
            delay = min(delay * 2, max_delay)
            continue  # Skip to the next cycle


        # B talks to A
        try:
            response_A = model.generate_content(context_A + format_prompt(response_B)).text
            context_A += format_prompt(response_B) + format_response(response_A)
        except ResourceExhausted:
            print(f"Rate limit hit for model A. Increasing delay to {delay * 2} seconds.")
            delay = min(delay * 2, max_delay)
            continue  # Skip to the next cycle

        cycle += 1
        delay = 1  # Reset delay after a successful cycle

    # Output to files
    with open(f"{exp_name}_A.txt", "w") as f:
        f.write(context_A)
    with open(f"{exp_name}_B.txt", "w") as f:
        f.write(context_B)

    print(f"Duality experiment completed. Results saved to {exp_name}_A.txt and {exp_name}_B.txt")


if __name__ == "__main__":
    parsed_args = args()
    if parsed_args.operation == "chat":
        if parsed_args.string:
            talk_to_gemini(parsed_args.string, parsed_args.context_file)
            exit()
        print("No string provided with the -c argument for chat operation.")
    elif parsed_args.operation == "experiment":
        experiment(parsed_args.exp_name)
        exit()
    else:
        print("Invalid operation. Choose 'chat' or 'experiment'.")