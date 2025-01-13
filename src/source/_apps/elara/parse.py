""" # parse.py
Module for formatting prompts and responses. It also handles context.
"""
import os
import subprocess
import textwrap
from pathlib import Path

preamble = """
Our Conversation
================

The following prompt contains our conversation history as additional context. It has been 
formatted as RestructuredText (RST). My prompts are denoted with the ".. me::" directive.
Your prompts are denoted with the ".. you::" directive. These markers are used only for 
formatting the context and separating our conversation history. These markers should not be 
included in your actual responses. The conversation goes in sequential order, starting from 
the earliest message down to the latest.\n\n
"""

THIS_DIR = Path(__file__).resolve().parent
DATA_DIR = os.path.join(THIS_DIR, "data")
DEFAULT_CONTEXT = os.path.join(DATA_DIR,"context.rst")
DEFAULT_SUMMARY = THIS_DIR

def prompt(text):
    return f"\n.. me::\n\n\t{text}\n"

def response(text):
    """Formats the model's response for RST.
    
    This function now handles multiple newlines correctly.
    """
    # Indent each line individually
    indented_lines = textwrap.indent(text, "\t").splitlines()
    # Join with newline and add to directive
    formatted_response = ".. you::\n\n" + "\n".join(indented_lines) + "\n"
    return formatted_response

def persist(raw_prompt, raw_response, context_file=DEFAULT_CONTEXT):
    """Appends the prompt and response to the context file."""
    os.makedirs(DATA_DIR, exist_ok=True)  # Ensure DATA_DIR exists

    # Create context if file doesn't exist
    if not os.path.exists(context_file):
        with open(context_file, "w") as f:
            f.write(preamble)  # Initialize with the preamble

    context = prompt(raw_prompt) + "\n" + response(raw_response)  # Removed extra newline

    with open(context_file, "a") as f:
        f.write(context)

    return context

def prefix(raw_prompt, context_file=DEFAULT_CONTEXT):
    """Appends the preamble and context to prompt."""

    prefixed_prompt = ""

    if os.path.exists(context_file):
        with open(context_file, "r") as f:
            context = f.read()
        prefixed_prompt += preamble + context
    prefixed_prompt += prompt(raw_prompt)

    return prefixed_prompt

def summarize(dir_path=DEFAULT_SUMMARY):
    """Summarizes the contents of a directory in an RST document."""
    if not os.path.isdir(dir_path):
        print(f"Error: '{dir_path}' is not a valid directory.")
        return

    output_file = os.path.join(dir_path, "summary.rst")
    with open(output_file, "w") as f:
        f.write(f"{os.path.basename(dir_path)}\n")  # Directory name as title
        f.write("=" * len(os.path.basename(dir_path)) + "\n\n")  # Underline

        # Generate directory tree using subprocess
        f.write("Directory Structure\n")
        f.write("-" * 19 + "\n\n")
        f.write(".. code-block:: bash\n\n")
        try:
            tree_output = subprocess.check_output(["tree", "-n", dir_path], text=True) # Added text=True for string output
            f.write(textwrap.indent(tree_output, "\t"))
        except FileNotFoundError:
            print("Error: The 'tree' command was not found. Please install it.")
            return
        except subprocess.CalledProcessError as e:
            print(f"Error: The 'tree' command returned a non-zero exit code: {e.returncode}")
            return
        f.write("\n")

        # Iterate through files and add their contents
        for root, _, files in os.walk(dir_path):
            for file in files:
                # Filter file extensions
                base, ext = os.path.splitext(file)
                if ext not in [".py", ".sh", ".txt"]:
                    continue

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, dir_path)

                f.write(f"{relative_path}\n")
                f.write("-" * len(relative_path) + "\n\n")

                # Use appropriate directive based on file extension
                if ext == ".py":
                    f.write(".. code:: python\n\n")
                elif ext == ".sh":
                    f.write(".. code:: bash\n\n")
                elif ext == ".txt":
                    f.write(".. parsed-literal::\n\n")

                with open(file_path, "r") as infile:
                    content = infile.read()
                    # Indent content for RST code block
                    indented_content = textwrap.indent(content, "\t")
                    f.write(indented_content)
                f.write("\n\n")

    print(f"Summary generated at: {output_file}")