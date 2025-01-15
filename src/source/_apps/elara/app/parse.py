""" # parse.py
Module for formatting prompts and responses. It also handles context management.
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
    persona : str = None,
    summarize_dir : str = None
) -> str:
    """
    Appends the preamble and formats the prompt. A directory on the local filesystem can be specified to add  additional context to the prompt. This directory will be summarized using the ``data/templates/summary.rst`` template and injected into the prompt.

    :param persona: Persona with which the prompter is conversing.
    :type persona: str
    :param summarize_dir: Directory containing additional context that is to be summarized.
    :type summarize_dir: str
    :returns: A contextualized prompt.
    :rtype: str
    """
    mem = cache.Cache()
    temps = templates.Template().get()
    convo = conversation.Conversation()
    lang = language.Language(
        enabled = conf.language_modules()
    )

    preamble_vars = { 
        **mem,
        **lang.get_modules()
    }

    if summarize_dir is not None:
        preamble_vars["summary"] = summarize(
            summarize_dir, 
            stringify=True
        )

    if persona is None:
        persona = mem.get("currentPersona")

    preamble_temp = temps.get("preamble")
    history_temp = temps.get("thread")

    data = convo.get(persona)

    preamble = preamble_temp.render(preamble_vars)
    history = history_temp.render(data)

    payload = preamble + history

    return payload

def summarize(
    directory : str,
    stringify : bool = False
) -> str:
    """
    Summarizes the contents of a directory in an RST document. The summary will be written to the directory it is summarizing.
    
    :param directory: Directory to be summarized.
    :type directory: str
    :param stringify: Return the result as a string instead of writing to file.
    :type stringify: bool
    :returns: A summary string in RST format.
    :rtype: str
    """

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
            if ext not in conf.summary_extensions() \
                or base == conf.SUMMARIZE["FILE"]:
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
