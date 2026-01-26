"""
Jinja2 Template Renderer

This module automates the generation of context-rich Markdown files. It extends the standard Jinja2 
environment with custom hooks for filesystem access and shell command execution, allowing templates 
to dynamically include the latest project state.

Usage:
    python task.py [template_file]

Dependencies:
    - jinja2

Security Warning:
    This script enables Arbitrary Code Execution (ACE) via the `command` function. Only render templates from trusted sources.
"""

import os
import subprocess
import jinja2
import argparse

# Configuration
DEFAULT_TEMPLATE = '.task.md.j2'
OUTPUT_FILENAME = 'prompt.md'


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


def render(template_path: str) -> None:
    """
    Orchestrates the Jinja2 rendering workflow.

    Initializes a Jinja2 Environment with the current working directory as the loader.
    Injects the custom `command` and `file` functions into the global namespace,
    renders the specified template, and writes the result to disk.

    Args:
        template_path (str): The filename of the Jinja2 template to render.

    Raises:
        jinja2.TemplateNotFound: If the specified template file does not exist.
        Exception: For generic IO or rendering errors.
    """
    # Set up the Jinja2 environment
    # Use FileSystemLoader to load templates from the current directory
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.getcwd()),
        autoescape=False,  # False is preferred for Markdown generation
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Register custom functions into the Jinja globals
    env.globals['command'] = command
    env.globals['file'] = file

    try:
        # Load the template
        template = env.get_template(template_path)

        # Render the template
        rendered_output = template.render()

        # Write the output to a markdown file
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
            f.write(rendered_output)

        print(f"Successfully rendered '{template_path}' to '{OUTPUT_FILENAME}'.")

    except jinja2.TemplateNotFound:
        print(f"Error: Could not find template '{template_path}' in {os.getcwd()}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


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

    args = parser.parse_args()

    render(args.template_file)