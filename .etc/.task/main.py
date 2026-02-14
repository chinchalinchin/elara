"""
Jinja2 Template Renderer

This module automates the generation of context-rich Markdown files. It extends the standard Jinja2 
environment with custom hooks for filesystem access and shell command execution, allowing templates 
to dynamically include the latest project state.

Usage:
    python task.py [template_file] [--output output_file] [--vars vars_file]

Dependencies:
    - jinja2

Security Warning:
    This script enables Arbitrary Code Execution (ACE) via the `command` function. Only render templates from trusted sources.
"""

import os
import subprocess
import jinja2
import argparse
import json
import sys

# -------------------- Configuration

DEFAULT_TEMPLATE                = '.task.md.j2'
DEFAULT_PROPS_FILE              = '.config/.props.json'
DEFAULT_VIEWS_FILE              = '.config/.views.json'
DEFAULT_VARS_FILE               = '.task.json'
DEFAULT_OUTPUT_SUBDIR           = 'prompt'
DEFAULT_OUTPUT_FILE             = 'prompt.md'


# -------------------- Templating Functions

def command(command_str: str) -> str:
    """
    Executes a shell command and returns the standard output.

    This function uses `subprocess.check_output` with `shell=True`. It is designed
    to capture the output of tools like `tree`, `ls`, or `git diff`s.

    Args:
        command_str (str): The shell command to execute.

    Returns:
        str: The stripped stdout of the command, or an error message if execution fails.
             This ensures the template rendering does not crash on a single failed command.
    """
    try:
        # Security Note: shell=True is necessary for pipes/complex commands but carries RCE risk.
        result = subprocess.check_output(
            command_str,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing command '{command_str}':\n{e.output}"
    except Exception as e:
        return f"Execution failed: {str(e)}"


def file(file_path: str) -> str:
    """
    Reads a file from the absolute or relative path provided and returns its content.

    Args:
        file_path (str): The path to the file to read. Supports `~` expansion.

    Returns:
        str: The content of the file, or an error message if the file is missing
             or unreadable.
    """
    # Expand ~ if present
    full_path = os.path.expanduser(file_path)

    if not os.path.exists(full_path):
        return f"Error: File not found at {full_path}"

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        return f"Error reading file: {str(e)}"


def load(vars_path: str) -> dict:
    """
    Loads variables from a JSON file.

    Args:
        vars_path (str): Path to the JSON file.

    Returns:
        dict: The parsed JSON data, or an empty dict if the file 
              does not exist or cannot be parsed.
    """
    if not os.path.exists(vars_path):
        # If the file doesn't exist, we just return empty context
        # (unless it was explicitly requested, handled in main)
        return {}

    try:
        with open(vars_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"Loaded variables from '{vars_path}'.")
            return data
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from '{vars_path}': {e}")
        return {}
    except Exception as e:
        print(f"Error reading vars file '{vars_path}': {e}")
        return {}


def render(template_path: str, output_path: str, vars_path: str) -> None:
    """
    Orchestrates the Jinja2 rendering workflow.

    Initializes a Jinja2 Environment with the directory containing this script as the loader.
    Injects the custom `command` and `file` functions into the global namespace,
    loads optional variables from JSON, renders the specified template, and writes the result to disk.

    Args:
        template_path (str): The filename of the Jinja2 template to render.
        output_path (str): The absolute or relative path to save the rendered output.
        vars_path (str): The path to the variables JSON file.

    Raises:
        jinja2.TemplateNotFound: If the specified template file does not exist.
        Exception: For generic IO or rendering errors.
    """
    # Determine the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    props_path = os.path.join(script_dir, DEFAULT_PROPS_FILE)

    # Set up the Jinja2 environment
    # Use FileSystemLoader to load templates from the script's directory
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(script_dir),
        autoescape=False,  # False is preferred for Markdown generation
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Register custom functions into the Jinja globals
    env.globals['command'] = command
    env.globals['file'] = file

    # Load both context files
    task_data = load(vars_path)
    props_data = load(props_path)
    
    # Merge: props_context keys will be added to task_context. 
    # If keys collide, task_context (the specific task) wins.
    # Swap them (task_context | props_context) if you want props to win.
    context = props_data| task_data

    try:
        # Load the template
        template = env.get_template(template_path)

        # Render the template with the context variables
        rendered_output = template.render(**context)

        # Ensure the directory for the output file exists
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # Write the output to a markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_output)

        print(f"Successfully rendered '{template_path}' to '{output_path}'.")

    except jinja2.TemplateNotFound:
        print(f"Error: Could not find template '{template_path}' in {script_dir}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# -------------------- Entrypoint

if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(
        description="Render Jinja2 templates into Markdown."
    )

    # Add positional argument for the template file
    parser.add_argument(
        "template_file",
        nargs="?",              # '?' means the argument is optional
        default=DEFAULT_TEMPLATE,
        help=f"The Jinja2 template file to render (default: {DEFAULT_TEMPLATE})"
    )

    # Add optional argument for the output location
    parser.add_argument(
        "-o", "--output",
        help=f"The output filename. Defaults to '{os.path.join(DEFAULT_OUTPUT_SUBDIR, DEFAULT_OUTPUT_FILE)}' relative to the script directory."
    )

    # Add optional argument for the vars file
    parser.add_argument(
        "-v", "--vars",
        help=f"Path to a JSON file containing variables (default: {DEFAULT_VARS_FILE} in script directory)."
    )

    args = parser.parse_args()

    # Determine script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Determine output path
    if args.output:
        target_output = args.output
    else:
        target_output = os.path.join(script_dir, DEFAULT_OUTPUT_SUBDIR, DEFAULT_OUTPUT_FILE)

    # Determine vars path
    if args.vars:
        target_vars = args.vars
        # If user explicitly provided a path, verify it exists before proceeding
        if not os.path.exists(target_vars):
            print(f"Error: The specified variables file '{target_vars}' does not exist.")
            sys.exit(1)
    else:
        target_vars = os.path.join(script_dir, DEFAULT_VARS_FILE)

    render(args.template_file, target_output, target_vars)