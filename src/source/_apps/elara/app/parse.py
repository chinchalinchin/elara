""" 
parse.py
--------

Module for formatting prompts and responses. It also handles context management.
"""
# Standard Library Modules
import os
import subprocess
import logging 

# Application Modules
import conf
import objects.cache as cache
import objects.errors as errors
import objects.templates as templates
import objects.language as language
import objects.conversation as conversation
import objects.repo as repo

logger = logging.getLogger(__name__)

def output(prompt, response):
    """
    Formats and prints the prompt and response.
    """
    return """"
    ====================== PROMPT =======================

    {prompt}

    ===================== RESPONSE ======================"

    {response}
    """.format(prompt=prompt, response=response)

def scrutinize(
    src : repo.Repo
) -> str:
    """
    Appends repository information to prompts. The current working directory is scanned and summarized with a call to the ``summarize`` function. The results are used to render the ``review.rst`` template in the ``data/templates`` directory.

    :param src: The class object that contains the repository metadata.
    :type src: repo.Repo
    :returns: Rendered template of pull request review
    :rtype: str
    """
    # @DEVELOPMENT
    #   Milton, the team has been thinking about allowing the user to specify 
    #   the directory containing the version control source directory. Currently 
    #   the application uses the current working directory. We should probably add
    #   a parameter to this function. We might be able to overload the existing 
    #   ``--directory`` command line argument for the ``scrutinizze`` function.
    #   What do you think?
    # @DEVELOPMENT
    mem = cache.Cache()
    temps = templates.Template()
    lang = language.Language(
        enabled = conf.language_modules()
    )
    dir = os.getcwd()  

    buffer = mem.vars()
    buffer["currentPersona"] = conf.PERSONAS["DEFAULTS"]["REVIEW"]

    return temps.render("review", { 
        **buffer,
        **src.vars(),
        **lang.vars(),
        **summarize(dir, stringify=True)
    })

def analyze(
    summarize_dir : str = None
   
) -> str: 
    """
    Injects the contents of a directory in the ``data/templates/article.rst`` template.

    :param summarize_dir: Directory of documents to analyze.
    :type summarize_dir: str
    """
    mem = cache.Cache()
    temps = templates.Template()
    lang = language.Language(
        enabled = conf.language_modules()
    )
    buffer = mem.vars()
    buffer["currentPersona"] = conf.PERSONAS["DEFAULTS"]["ANALYSIS"]

    return temps.render("article", {
        **buffer,
        **lang.vars(),
        **summarize(summarize_dir, stringify=True),
        **{ "latex": conf.LATEX_PREAMBLE }
    })

def contextualize(
    persona : str = None,
    summarize_dir : str = None
) -> str:
    """
    Appends the preamble and formats the prompt. A directory on the local filesystem can be specified to add additional context to the prompt. This directory will be summarized using the ``data/templates/summary.rst`` template and injected into the prompt.

    :param persona: Persona with which the prompter is conversing.
    :type persona: str
    :param summarize_dir: Directory containing additional context that is to be summarized.
    :type summarize_dir: str
    :returns: A contextualized prompt.
    :rtype: str
    """
    mem = cache.Cache()
    temps = templates.Template()
    convo = conversation.Conversation()
    lang = language.Language(
        enabled = conf.language_modules()
    )
    
    preamble_vars = { 
        **mem.vars(),
        **lang.vars()
    }

    if summarize_dir is not None:
        preamble_vars.update(
            summarize(summarize_dir, stringify=True)
        )

    if persona is None:
        persona = mem.get("currentPersona")

    preamble_temp = temps.get("preamble")
    history_temp = temps.get("conversation")

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

    try:
        # @DEVELOPMENT
        #   Hey, Milton, the client wants us to refactor this.
        #   They don't like making the application dependent on the `tree`
        #   application. They want to generate a data structure that
        #   represents the structure of ``directory`` as a dict, then
        #   they want to update the application to use this output 
        #   to render the ``data/templates/review.rst`` template.
        #   In other words, instead of injecting the raw ``tree``
        #   output into the template, they want to format the directory
        #   structure and then modify the template to generate the 
        #   git summary more gracefully. 
        #
        #   The development team is pulling their hair out trying to
        #   figure out how to implement this. We need your skill, Milton!
        # @DEVELOPMENT
        tree_output = subprocess.check_output(
            ["tree", "-n", directory], 
            text=True
        )
    except FileNotFoundError:
        raise errors.TreeCommandNotFoundError(
            "The 'tree' command was not found. Please install it."
        )
    except subprocess.CalledProcessError as e:
        raise errors.TreeCommandFailedError(
            f"The 'tree' command returned a non-zero exit code: {e.returncode}"
        )
    
    template_vars = {
        "directory": os.path.basename(directory),
        "tree": tree_output,
        "files": []
    }

    # Use `os.walk` to recursivle scan sub-directories.
    for root, _, files in os.walk(directory):
        # traverse files in alphabetical order
        files.sort()
        for file in files:

            base, ext = os.path.splitext(file)

            if ext not in conf.summary_extensions() \
                or base == conf.SUMMARIZE["FILE"]:
                continue

            file_path = os.path.join(root, file)

            directive = ext in conf.SUMMARIZE["DIRECTIVES"].keys()

            try:
                with open(file_path, "r") as infile:
                    data = infile.read()

                if directive:
                    template_vars["files"] += [{
                        "type": "code",
                        "data": data,
                        "lang": conf.SUMMARIZE["DIRECTIVES"][ext],
                        "name" : os.path.relpath(file_path, directory)
                    }]
                    continue

                template_vars["files"] += [{
                    "type": "raw",
                    "data": data,
                    "name": os.path.relpath(file_path, directory)
                }]
            except Exception as e:
                logger.error(F"Error reading file {file_path}: {e}")
                continue

    payload = templates.Template().render("summary", template_vars)
    
    if not stringify:     
        with open(output_file, "w") as out:
            out.write(payload)
        logger.info(f"Summary generated at: {output_file}")

    return { "summary": payload }
