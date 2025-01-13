""" # experiment.py
Module for performing experiments on LLMs.
"""
# Application Modules
import model 
import parse

# Standard Library Modules
import time 
import os

# External Modules
from google.api_core.exceptions import ResourceExhausted

DEFAULT_EXPERIMENT = "duality"
"""Default experiment to conduct."""

def conduct(choice, model_type = model.DEFAULT_MODEL):
    """Conducts an experiment based on the given choice."""
    if choice == "duality":
        _duality(model_type=model_type)

def _duality(
        max_cycles = 20, 
        max_delay = 60, 
        initial_prompt = "Form is the possibility of structure.",
        model_type = model.DEFAULT_MODEL):
    """
    Conducts the 'duality' experiment with exponential backoff,
    separate error handling, and correct sleep placement.

    Args:
        max_cycles (int): The maximum number of cycles to run the experiment.
        max_delay (int): The maximum delay (in seconds) for exponential backoff.
        initial_prompt (str): The initial prompt to start the conversation.
        model_type (str): The type of model to use (e.g., "gemini-pro").
    """
    context_A = parse.preamble
    context_B = parse.preamble
    cycle = 0
    delay = 1  # Initial delay in seconds

    # Initial interaction
    response_A = model.reply(context_A + parse.prompt(initial_prompt), model_type)
    context_A += parse.prompt(initial_prompt) + parse.response(response_A)

    while cycle < max_cycles:
        time.sleep(delay)  # Sleep at the beginning of the loop

        # A talks to B
        try:
            response_B = model.reply(context_B + parse.prompt(response_A), model_type)
            context_B += parse.prompt(response_A) + parse.response(response_B)
        except ResourceExhausted as e:
            print(e)
            print(f"Rate limit hit for model B. Increasing delay to {delay * 2} seconds.")
            delay = min(delay * 2, max_delay)
            continue  # Skip to the next cycle


        # B talks to A
        try:
            response_A = model.reply(context_A + parse.prompt(response_B), model_type)
            context_A += parse.prompt(response_B) + parse.response(response_A)
        except ResourceExhausted as e:
            print(e)
            print(f"Rate limit hit for model A. Increasing delay to {delay * 2} seconds.")
            delay = min(delay * 2, max_delay)
            continue  # Skip to the next cycle

        cycle += 1
        delay = 1  # Reset delay after a successful cycle

    # Output to files
    a_file = os.path.join(parse.DATA_DIR, "duality_context_A.txt")
    b_file = os.path.join(parse.DATA_DIR, "duality_context_B.txt")

    with open(a_file, "w") as f:
        f.write(context_A)
    with open(b_file, "w") as f:
        f.write(context_B)

    print('Duality experiment completed. Results saved to \n\n\t{a_file}\n\n and \n\n\t{b_file}]\n\n')
