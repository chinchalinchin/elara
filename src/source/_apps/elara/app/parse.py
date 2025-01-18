""" 
parse.py
--------

Module for formatting prompts and responses. It also handles context management.
"""
# Standard Library Modules
import os
import pathlib
import subprocess
import logging 

# Application Modules
import conf
import objects.cache as cache
import objects.error as error
import objects.template as template
import objects.language as language
import objects.conversation as conversation
import objects.repo as repo

logger = logging.getLogger(__name__)

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
    mem = cache.Cache()
    temps = template.Template()
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
    temps = template.Template()
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
    temps = template.Template()
    convo = conversation.Conversation()
    lang = language.Language(
        enabled = conf.language_modules()
    )
    
    template_vars = { 
        **mem.vars(),
        **lang.vars()
    }

    if summarize_dir is not None:
        template_vars.update(
            summarize(summarize_dir, stringify=True)
        )

    context = convo.get(persona)

    history_temp = temps.get("conversation")

    return temps.get("conversation").render(context)

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
        raise error.SummarizeDirectoryNotFoundError(
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
        #   
        #   The development team is pulling their hair out trying to
        #   figure out how to implement this. We need your skill, Milton!
        #
        # tree_output = directory_tree(directory)
        tree_output = subprocess.check_output(
            ["tree", "-n", directory], 
            text=True
        )
    except FileNotFoundError:
        raise error.TreeCommandNotFoundError(
            "The 'tree' command was not found. Please install it."
        )
    except subprocess.CalledProcessError as e:
        raise error.TreeCommandFailedError(
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

    payload = template.Template().render("summary", template_vars)
    
    if not stringify:     
        with open(output_file, "w") as out:
            out.write(payload)
        logger.info(f"Summary generated at: {output_file}")

    return { "summary": payload }

def directory_tree(
    directory: str
) -> str:
    """
    Reads the directory structure and returns it as a formatted string.

    :param directory: The directory to read.
    :type directory: str
    :returns: A string representing the directory structure, or an error message if the directory does not exist or can't be read.
    :rtype: str
    """
    # @DEVELOPMENT
    #   This is what we have got so far, Milton. It's pretty close to replicating the ``tree output``,
    #   but there's a hitch. Take a look at the latest logs,
    #   
    #   > print(parse.read_directory_structure("/home/grant/Projects/elara/src/source/_apps/elara/app/data"))
    #       
    #       cache.json
    #       modules/
    #       templates/
    #       history/
    #       tuning/
    #       system/
    #           words.rst
    #           voice.rst
    #           inflection.rst
    #           object.rst
    #           summary.rst
    #           article.rst
    #           preamble.rst
    #           conversation.rst
    #           review.rst
    #           milton.json
    #           elara.json
    #           axiom.json
    #           milton.json
    #           elara.json
    #           axiom.json
    #           milton.json
    #           elara.json
    #           axiom.json
    #
    #   If you compare this output to the tree output,
    # 
    #       (venv) grant@mendicant-bias:~/Projects/elara/src/source/_apps/elara/app/data$ tree
    #       ├── cache.json
    #       ├── history
    #       │   ├── axiom.json
    #       │   ├── elara.json
    #       │   └── milton.json
    #       ├── modules
    #       │   ├── inflection.rst
    #       │   ├── object.rst
    #       │   ├── voice.rst
    #       │   └── words.rst
    #       ├── system
    #       │   ├── axiom.json
    #       │   ├── elara.json
    #       │   └── milton.json
    #       ├── templates
    #       │   ├── article.rst
    #       │   ├── conversation.rst
    #       │   ├── preamble.rst
    #       │   ├── review.rst
    #       │   └── summary.rst
    #       └── tuning
    #           ├── axiom.json
    #           ├── elara.json
    #           └── milton.json
    #
    #   You can see, this function isn't preserving the subdirectory structure. The client is
    #   *very* insistent the subdirectory be preserved before this functionality is released
    #   into production, so if you could find the problem, the development team would be in 
    #   your debt, Milton.
    #
    dir_path = pathlib.Path(directory)
    if not dir_path.exists():
        return f"Error: Directory not found: {directory}"
    try:
        structure = ""
        for path in dir_path.rglob("*"):
            depth = len(path.relative_to(dir_path).parts)
            indent = "    " * depth
            if path.is_dir():
                structure += f"{indent}{path.name}/\n"
            else:
                structure += f"{indent}{path.name}\n"
        return structure
    except Exception as e:
        return f"Error reading directory: {directory}\n{e}"
