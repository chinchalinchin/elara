""" # parse.py
Module for formatting prompts and responses. It also handles context.
"""
# Standard Library Modules
import os
import subprocess
import textwrap

# Application Modules
import conf
import objects.cache as cache
import objects.errors as errors
import objects.templates as templates
import objects.language as language
import objects.conversation as conversation

def contextualize(
    persona=None,
    summarize_dir=None
):
    """Appends the preamble and context to prompt."""
    mem = cache.Cache().get()
    temps = templates.Template().get()
    lang = language.Language(enabled = conf.modules())
    convo = conversation.Conversation()

    module_vars = lang.get_modules()

    if len(module_vars) > 0:
        module_vars["language"] = True

    preamble_vars = { 
        **mem["template"],
        **module_vars
    }

    if summarize_dir is not None:
        preamble_vars["summary"] = summarize(summarize_dir, stringify=True)

    if persona is None:
        persona = mem["template"]["currentPersona"]

    preamble_temp = temps.get("preamble")
    history_temp = temps.get("thread")

    data = convo.get(persona)

    preamble = preamble_temp.render(preamble_vars)
    history = history_temp.render(data)

    payload = preamble + history

    return payload

def summarize(
    directory,
    stringify = False
):
    """Summarizes the contents of a directory in an RST document."""

    if not os.path.isdir(directory):
        raise errors.SummarizeDirectoryNotFoundError(
            f"{directory} does not exist."
        )

    summary_file = conf.summary_file()
    output_file = os.path.join(directory, summary_file)

    payload= f"{os.path.basename(directory)}\n" + \
        "=" * len(os.path.basename(directory)) + "\n\n" + \
        "Directory Structure\n" + \
        "-" * 19 + "\n\n" + \
        ".. code-block:: bash\n\n"
    
    try:
        tree_output = subprocess.check_output(
            ["tree", "-n", directory], 
            text=True
        )
        payload += textwrap.indent(tree_output, "\t")
    except FileNotFoundError:
        raise errors.TreeCommandNotFoundError(
            "The 'tree' command was not found. Please install it."
        )
    except subprocess.CalledProcessError as e:
        raise errors.TreeCommandFailedError(
            f"The 'tree' command returned a non-zero exit code: {e.returncode}"
        )
    
    payload += "\n\n"

    for root, _, files in os.walk(directory):
        for file in files:

            base, ext = os.path.splitext(file)
            if ext not in conf.extensions() or base == conf.SUMMARIZE["FILE"]:
                continue

            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)

            payload += f"{relative_path}\n" + \
                "-" * len(relative_path) + \
                "\n\n"

            directive = ext in conf.SUMMARIZE["DIRECTIVES"].keys()

            if directive:
                payload += f"{conf.SUMMARIZE["DIRECTIVES"][ext]}\n\n"

            with open(file_path, "r") as infile:
                content = infile.read()

                # Indent content for RST directives
                if directive:
                    content = textwrap.indent(content, "\t")

                payload += content

            payload += "\n\n"

    print(f"Summary generated at: {output_file}")
    
    if not stringify:     
        with open(output_file, "w") as out:
            out.write(payload)

    return payload
