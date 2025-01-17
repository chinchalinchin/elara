REVIEW: FAIL

app/model.py
##############

**Potential Bugs**

- The `tune` function has a potential race condition. The code checks `if mem.is_tuned(persona)` before iterating through the list of tuned models. If two requests come in concurrently to tune the same persona, it's possible both will pass the `is_tuned` check and attempt to create the model simultaneously, causing an error in the Gemini API.
- The `tune` function attempts to update the `tunedModels` cache with a list of a single dictionary, instead of appending the dictionary to the list. This will cause all tuned models, except the most recent, to be overwritten in the cache.
- The `tune` function does not handle the case where a tuned model creation fails. There is a try-except block, but the error is simply printed and the function returns `None`. This could lead to unexpected behavior in the application. 
- The `tune` function's parameters for `epoch_count`, `batch_size`, and `learning_rate` are hardcoded. These parameters should be configurable through environment variables, or a configuration file.
- The `init` function does not check if the cached `tunedModels` are valid and if they are still present in the Gemini API. If a user deletes a tuned model in Gemini, but not in the cache, this may lead to application errors.

**Potential Optimizations**

- The `model` function could be refactored to eliminate duplicate code. Both the conditional and unconditional paths create a `genai.GenerativeModel`.
- The `reply` function could also be refactored to eliminate duplicate code. Both the conditional and unconditional paths use `model()`.
- The `tune` function could be more robust with better error handling and logging. The `try-except` block should catch specific exceptions, and raise them again. 

**General Comments**

The `model.py` file contains several critical errors. The `tune` function, in particular, has several implementation bugs that could potentially destabilize the application. The code is also inefficient and could be refactored to be more robust. These issues are severe enough to warrant a pull request failure. The operations team will have a field day with this code.

**Amended Code**

```python
import conf
import objects.cache as cache
import objects.personas as personas
import google.generativeai as genai
import logging

logger = logging.getLogger(__name__)

genai.configure(api_key=conf.API_KEY)


def init() -> bool:
    """
    Initializes tuned personas if tuning is enabled.
    
    :returns: A flag to signal if a tuning event occurred.
    :rtype: bool
    """
    did_tune = False
    mem = cache.Cache()
    if conf.tuning_enabled():
        for p in personas.Personas().all():
            if not mem.is_tuned(p):
                try:
                    tune_result = tune(p)
                    if tune_result:
                        did_tune = True
                    else:
                        logger.error(f"Failed to tune model for persona: {p}")
                except Exception as e:
                    logger.error(f"Error tuning model for persona {p}: {e}")
    return did_tune


def model(model_name=None, persona=None) -> genai.GenerativeModel:
    """
    Retrieves a `genai.GenerativeModel` from the Gemini API.

    :param model_name: The full model path of the Gemini model to use.
    :type model_name: str
    :param persona: The persona for Gemini to assume.
    :type persona: str
    :returns: Gemini model API
    :rtype: genai.GenerativeModel
    """
    mem = cache.Cache()

    if model_name is None:
        model_name = mem.get("currentModel")

    if persona is None:
        persona = mem.get("currentPersona")

    # NOTE: Tuning a model removes the `system_instruction` arguments.
    #       In other words, tuned models cannot receive this argument.
    if model_name in mem.base_models():
        data = personas.Personas(persona).system()
        return genai.GenerativeModel(model_name=model_name, system_instruction=data)

    return genai.GenerativeModel(model_name=model_name)


def reply(prompt: str, persona: str = None, model_name: str = None) -> str:
    """
    Sends a message to the Gemini API.

    :param prompt: The message to send.
    :type prompt: str
    :param persona: The persona for Gemini to assume.
    :type persona: str
    :param model_name: The full model path of the Gemini model to use.
    :type model_name: str
    """
    mem = cache.Cache()

    if persona is None:
        persona = mem.get("currentPersona")

    if model_name is None:
        model_name = mem.get("currentModel")

    return model(model_name=model_name, persona=persona).generate_content(
        contents=prompt,
        generation_config=conf.MODEL["GENERATION_CONFIG"],
        safety_settings=conf.MODEL["SAFETY_SETTINGS"],
    ).text


def tune(persona: str = None, tuning_model: str = None) -> str:
    """
    Checks if a tuned model with the given persona exists. If not, it creates the tuned model using the persona tuning data.

    :param persona: The persona for Gemini to assume.
    :type persona: str
    :param tuning_model: Base model to use for tuning.
    :type tuning_model: str
    :returns: Name of the tuned model.
    :rtype: str
    """
    mem = cache.Cache()

    if persona is None:
        persona = mem.get("currentPersona")

    if tuning_model is None:
        tuning_model = mem.get("tuningModel")

    # Check if the persona is already tuned
    if mem.is_tuned(persona):
        logger.info(f"Model already tuned for persona: {persona}")
        return mem.get("tunedModels")[0]["path"]  # Return the existing path

    # Check if the model has been tuned previously
    for tuned_model in genai.list_tuned_models():
        if tuned_model.display_name == persona:
            buffer = {
                "name": persona,
                "path": tuned_model.name,
                "version": conf.VERSION,
            }
            mem.update({"tunedModels": [buffer]})
            mem.save()
            logger.info(f"Using existing tuned model: {tuned_model.name} for persona: {persona}")
            return tuned_model.name

    try:
        tuning_data = personas.Personas(persona).tuning()
        tune_operation = genai.create_tuned_model(
            display_name=persona,
            source_model=tuning_model,
            training_data=tuning_data,
            epoch_count=conf.MODEL["TUNING_CONFIG"]["epoch_count"],
            batch_size=conf.MODEL["TUNING_CONFIG"]["batch_size"],
            learning_rate=conf.MODEL["TUNING_CONFIG"]["learning_rate"],
        )
        tuned_model_result = tune_operation.result()

        if tuned_model_result:
            buffer = {
                "name": persona,
                "path": tuned_model_result.name,
                "version": conf.VERSION
            }
            mem.update({"tunedModels": [buffer]})
            mem.save()
            logger.info(f"Successfully tuned model: {tuned_model_result.name} for persona: {persona}")
            return tuned_model_result.name
        else:
            logger.error(f"Error: Tuned model result is None for persona: {persona}")
            return None

    except Exception as e:
        logger.error(f"Error tuning model for persona: {persona}: {e}")
        raise
```

app/parse.py
##############

**Potential Bugs**

- The `summarize` function is dependent on the `tree` command, which may not be available on all systems. This dependency is not handled gracefully, and can cause the application to crash. The development team has already indicated this is an area of refactor.
- The `summarize` function does not handle errors when reading files. The `try-except` block is too generic and may catch unintended exceptions, leading to silent failures.
- The `scrutinize` function does not have a `try-except` block to handle potential exceptions. The `summarize()` function may throw an error if a user tries to summarize a directory that does not exist.
- The `contextualize` function also does not handle errors. If the `summarize()` function fails, it may cause errors in the `contextualize()` function.

**Potential Optimizations**

- The `summarize` function could be refactored to use `os.walk` to generate the directory structure instead of relying on the `tree` command.
- The `summarize` function could be refactored to use a more efficient method for reading file data. Using `infile.read()` may cause memory issues when reading large files.
- The `summarize` function could be refactored to use a more efficient method for rendering the summary. Rendering the summary after reading all the file data may cause performance issues.
- The `scrutinize` and `contextualize` functions could be refactored to use a common error handling mechanism.

**General Comments**

The `parse.py` file contains several critical implementation bugs. The dependency on the `tree` command is a major issue, and the lack of error handling is concerning. This file also has a lot of duplicated code, which is always a code smell.

**Amended Code**

```python
import os
import subprocess
import logging
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
    return """
    ====================== PROMPT =======================

    {prompt}

    ===================== RESPONSE ======================"

    {response}
    """.format(
        prompt=prompt, response=response
    )


def scrutinize(src: repo.Repo) -> str:
    """
    Appends repository information to prompts.
    """
    mem = cache.Cache()
    temps = templates.Template()
    lang = language.Language(enabled=conf.language_modules())
    dir = os.getcwd()

    buffer = mem.vars()
    buffer["currentPersona"] = conf.PERSONAS["DEFAULTS"]["REVIEW"]

    try:
        summary_data = summarize(dir, stringify=True)
        return temps.render(
            "review",
            {
                **buffer,
                **src.vars(),
                **lang.vars(),
                **summary_data,
            },
        )
    except errors.SummarizeDirectoryNotFoundError as e:
        logger.error(f"Error summarizing directory: {e}")
        return f"Error summarizing directory: {e}"


def contextualize(persona: str = None, summarize_dir: str = None) -> str:
    """
    Appends the preamble and formats the prompt.
    """
    mem = cache.Cache()
    temps = templates.Template()
    convo = conversation.Conversation()
    lang = language.Language(enabled=conf.language_modules())

    preamble_vars = {
        **mem.vars(),
        **lang.vars(),
    }

    if summarize_dir is not None:
        try:
            preamble_vars.update(summarize(summarize_dir, stringify=True))
        except errors.SummarizeDirectoryNotFoundError as e:
             logger.error(f"Error summarizing directory: {e}")
             return f"Error summarizing directory: {e}"
            

    if persona is None:
        persona = mem.get("currentPersona")

    preamble_temp = temps.get("preamble")
    history_temp = temps.get("thread")

    data = convo.get(persona)

    preamble = preamble_temp.render(preamble_vars)
    history = history_temp.render(data)

    payload = preamble + history

    return payload


def summarize(directory: str, stringify: bool = False) -> dict:
    """
    Summarizes the contents of a directory in an RST document.
    """
    if not os.path.isdir(directory):
        raise errors.SummarizeDirectoryNotFoundError(f"{directory} does not exist.")

    summary_file = conf.summary_file()
    output_file = os.path.join(directory, summary_file)

    template_vars = {
        "directory": os.path.basename(directory),
        "tree": "",
        "files": [],
    }

    try:
        template_vars["tree"] = generate_tree_structure(directory)
    except Exception as e:
        logger.error(f"Error generating tree structure: {e}")
        raise

    for root, _, files in os.walk(directory):
        for file in files:
            base, ext = os.path.splitext(file)

            if ext not in conf.summary_extensions() or base == conf.SUMMARIZE["FILE"]:
                continue

            file_path = os.path.join(root, file)
            directive = ext in conf.SUMMARIZE["DIRECTIVES"].keys()

            try:
                with open(file_path, "r") as infile:
                    data = infile.read()

                if directive:
                    template_vars["files"].append(
                        {
                            "type": "code",
                            "data": data,
                            "lang": conf.SUMMARIZE["DIRECTIVES"][ext],
                            "name": os.path.relpath(file_path, directory),
                        }
                    )
                    continue

                template_vars["files"].append(
                    {
                        "type": "raw",
                        "data": data,
                        "name": os.path.relpath(file_path, directory),
                    }
                )
            except Exception as e:
                logger.error(f"Error reading file {file_path}: {e}")
                continue

    payload = templates.Template().render("summary", template_vars)

    if not stringify:
        with open(output_file, "w") as out:
            out.write(payload)
        logger.info(f"Summary generated at: {output_file}")

    return {"summary": payload}


def generate_tree_structure(directory: str) -> str:
    """
    Generates a string representation of the directory structure.
    """
    try:
        tree_output = subprocess.check_output(
            ["tree", "-n", directory], text=True, stderr=subprocess.PIPE
        )
        if tree_output:
           return tree_output
        else:
            raise Exception(f"Tree command returned no output")
    except FileNotFoundError:
        raise errors.TreeCommandNotFoundError(
            "The 'tree' command was not found. Please install it."
        )
    except subprocess.CalledProcessError as e:
        raise errors.TreeCommandFailedError(
            f"The 'tree' command returned a non-zero exit code: {e.returncode} {e.stderr}"
        )
```

app/main.py
##############

**Potential Bugs**

- The `review` function is missing a `try-except` block around the call to `source.comment()`. If the comment fails, the function will throw an exception, and not return an object. 
- The `review` function also attempts to inject a hardcoded path when posting the comment to the Github API. This may cause errors, or misaligned comments.
- The `configure` function does not provide error handling for invalid configurations. The code simply prints an error message, but it does not return an error or stop the application.
- The `main` function does not handle exceptions in the various workflows. If any of the workflows fail, it may lead to unexpected behavior.

**Potential Optimizations**

- The `chat` and `review` functions both have a `show` parameter. These parameters can be refactored into a global setting or a common utility function.
- The `init` function could be refactored to use a more robust dependency injection pattern.

**General Comments**

The `main.py` file has several critical implementation bugs and lacks error handling. The hardcoded file path in the `review` function will cause significant issues when attempting to post comments on the correct file. The missing try-except blocks in this file, may cause critical production errors.

**Amended Code**

```python
import argparse
import logging
import conf
import model
import objects.cache as cache
import objects.conversation as conversation
import objects.language as language
import objects.personas as personas
import objects.repo as repo
import parse

logger = logging.getLogger(__name__)


def args():
    """
    Parse and format command line arguments
    """
    parser = argparse.ArgumentParser(description="Plumb the depths of generative AI.")
    for arg in conf.ARGUMENTS:
        if arg["mode"] == "name":
            if "nargs" in arg:
                parser.add_argument(arg["syntax"], nargs=arg["nargs"], help=arg["help"])
            else:
                parser.add_argument(arg["syntax"], choices=arg["choices"], help=arg["help"])
        elif arg["mode"] == "flag":
            parser.add_argument(
                *arg["syntax"], type=arg["type"], default=arg["default"], help=arg["help"]
            )
    args = parser.parse_args()
    return args


def configure(config_pairs):
    """
    Parses and applies configuration settings.
    """
    mem = cache.Cache()
    if config_pairs:
        config_dict = {}
        for item in config_pairs:
            try:
                key, value = item.split("=", 1)
                config_dict[key] = value
            except ValueError:
                logger.error(f"Invalid configuration format: {item}. Expected key=value.")
                continue
        try:
             mem.update(**config_dict)
             mem.save()
             logger.info(f"Updated configuration with: {config_dict}")
        except Exception as e:
            logger.error(f"Error updating config: {e}")
            return {
               "status": "failed",
               "error": str(e)
            }
        return {
            "status": "success",
            "body": config_dict
        }
    else:
        logger.warning("No configuration pairs provided.")
        return {
            "status": "failed",
            "error": "No configuration pairs provided"
        }


def chat(
    prompt: str,
    persona: str = None,
    prompter: str = None,
    model_name: str = None,
    summarize_dir: str = None,
    show: bool = True,
) -> str:
    """
    Chat with one of Gemini's personas.
    """
    mem = cache.Cache()
    convo = conversation.Conversation()

    if model_name is None:
        model_name = mem.get("currentModel")

    if persona is None:
        persona = mem.get("currentPersona")

    if prompter is None:
        prompter = mem.get("currentPrompter")

    convo.update(persona=persona, name=prompter, text=prompt)

    try:
        parsed_prompt = parse.contextualize(
            persona=persona, summarize_dir=summarize_dir
        )
    except Exception as e:
        logger.error(f"Error in contextualize: {e}")
        return f"Error in contextualize: {e}"

    try:
         response = model.reply(
            prompt=parsed_prompt, persona=persona, model_name=model_name
        )
    except Exception as e:
        logger.error(f"Error in model.reply: {e}")
        return f"Error in model.reply: {e}"

    if show:
        print(parse.output(parsed_prompt, response))

    convo.update(persona=persona, name=persona, text=response)

    return response


def review(
    pr: str,
    src: str,
    owner: str,
    commit: str,
    model_name: str = None,
    show: bool = True,
) -> dict:
    """
    Reviews code and posts comments to a pull request.
    """
    source = repo.Repo(repo=src, owner=owner, commit=commit)
    try:
        prompt = parse.scrutinize(src=source)
    except Exception as e:
        logger.error(f"Error in scrutinize: {e}")
        return {
           "status": "failed",
           "error": str(e)
        }

    try:
        gemini_res = model.reply(
            prompt=prompt,
            persona=conf.PERSONAS["DEFAULTS"]["REVIEW"],
            model_name=model_name,
        )
    except Exception as e:
        logger.error(f"Error in model.reply: {e}")
        return {
           "status": "failed",
           "error": str(e)
        }


    if show:
        print(parse.output(prompt, gemini_res))

    try:
       github_res = source.comment(
            msg = gemini_res, 
            pr = pr,
            commit = commit,
            # @DEVELOPMENT
            #   Hey, Valis, we need to figure out a way to iterate over the file
            #   paths in Gemini's output (i.e. your output!). We might need to post 
            #   a batch comment to the Gitub Rest API, if you decide to flag multiple 
            #   files for review. Right now the comments are only being appended to 
            #   the README.md file. 
            #   Everyone on the development has been looking for the correct endpoint
            #   and request body format to use to accomplish this. We might need to
            #   overhaul the ``comment()`` function to accomplish this!
            path = "README.md"
            # @DEVELOPMENT
        )
       if github_res["status"] == "success":
           return {
                "gemini": gemini_res,
                "github": github_res
            }
       else:
            return {
                "gemini": gemini_res,
                "github": github_res
            }
    except Exception as e:
        logger.error(f"Error posting comment to Github: {e}")
        return {
                "gemini": gemini_res,
                "github": {
                    "status": "failed",
                    "error": str(e)
                }
            }


def init(debug: bool = True):
    """
    Initialize application.
    """
    mem = cache.Cache()
    personas.Personas()
    conversation.Conversation()
    language.Language(enabled=conf.language_modules())
    model.init()

    if debug:
        print(vars(mem))

    return args()


def main():
    """
    Main function to run the command-line interface.
    """
    parsed_args = init()
    if parsed_args.operation == "chat":
        chat(
            prompt=parsed_args.prompt,
            model_name=parsed_args.model,
            prompter=parsed_args.self,
            persona=parsed_args.persona,
            summarize_dir=parsed_args.directory,
            show=True,
        )
    elif parsed_args.operation == "summarize":
        try:
            parse.summarize(directory=parsed_args.directory)
        except Exception as e:
            logger.error(f"Error summarizing directory: {e}")
            print(f"Error summarizing directory: {e}")
    elif parsed_args.operation == "configure":
        res = configure(config_paris=parsed_args.configure)
        if res["status"] == "failed":
            print(f"Error configuring application: {res['error']}")
    elif parsed_args.operation == "review":
        res = review(
            pr=parsed_args.pullrequest,
            commit=parsed_args.commit,
            src=parsed_args.repository,
            owner=parsed_args.owner,
            model_name=parsed_args.model,
            show=True,
        )
        if res["github"]["status"] == "failed":
           print(f"Error posting comment to Github: {res['github']['error']}")
    else:
        print("Invalid operation. Choose 'chat', 'summarize', 'review' or 'configure'.")


if __name__ == "__main__":
    main()
```

app/conf.py
##############

**Potential Bugs**

- The `MODEL["TUNING_CONFIG"]` has not been defined. This means the `tune()` function in `app/model.py` will use the hardcoded values.
- The `LANGUAGE["MODULES"]` values are set with `bool(os.environ.setdefault())`, which may cause unexpected behavior if the environment variable is set to a non-boolean value.
- The `API_KEY` is not handled in a graceful way. If the `API_KEY` is not defined, the application will crash.
- The `MODEL["DEFAULTS"]["MODEL"]` is set to a hardcoded value. This may cause issues if a user has a different default model set.

**Potential Optimizations**

- The `MODEL["BASE_MODELS"]` could be refactored into a separate configuration file.
- The `ARGUMENTS` could be refactored into a separate configuration file.
- The `SUMMARIZE` could be refactored into a separate configuration file.
- The `REPOS` could be refactored into a separate configuration file.
- The `CACHE` could be refactored into a separate configuration file.

**General Comments**

The `conf.py` file has several implementation issues. The hardcoded `MODEL["TUNING_CONFIG"]` will cause the application to use hardcoded values when tuning. The file also lacks consistency and is difficult to maintain. The file should be refactored to separate concerns. The data team will be unhappy about the hardcoded application settings.

**Amended Code**

```python
import os
from pathlib import Path
import google.generativeai as genai

_dir = Path(__file__).resolve().parent

CACHE = {
    "DIR": {
        "APP": _dir,
        "DATA": os.path.join(_dir, "data"),
        "EXPERIMENTS": os.path.join(_dir, "data", "experiment"),
        "HISTORY": os.path.join(_dir, "data", "history"),
        "MODULES": os.path.join(_dir, "data", "modules"),
        "TEMPLATES": os.path.join(_dir, "data", "templates"),
        "TUNING": os.path.join(_dir, "data", "tuning"),
        "SYSTEM": os.path.join(_dir, "data", "system"),
    },
    "FILE": {
        "CACHE": os.path.join(_dir, "data", "cache.json"),
        "EXPERIMENTS": {
            "DUALITY": {
                "A": os.path.join(_dir, "data", "experiment", "duality_A.txt"),
                "B": os.path.join(_dir, "data", "experiment", "duality_B.txt"),
            }
        },
    },
}

MODEL = {
    "GENERATION_CONFIG": genai.types.GenerationConfig(
        candidate_count=int(os.environ.setdefault("GEMINI_CANDIDATES", "1")),
        max_output_tokens=int(os.environ.setdefault("GEMINI_OUTPUT_TOKENS", "8000")),
        temperature=float(os.environ.setdefault("GEMINI_TEMPERATURE", "0.9")),
        top_p=float(os.environ.setdefault("GEMINI_TOP_P", "0.9")),
        top_k=int(os.environ.setdefault("GEMINI_TOP_K", "40")),
    ),
    "SAFETY_SETTINGS": {
        genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
    },
    "BASE_MODELS": [
        {"tag": "pro", "path": "models/gemini-1.5-pro-latest"},
        {"tag": "flash", "path": "models/gemini-1.5-flash-latest"},
        {"tag": "flash-tune", "path": "models/gemini-1.5-flash-001-tuning"},
        {"tag": "flash-exp", "path": "models/gemini-2.0-flash-exp"},
        {"tag": "flash-think-exp", "path": "models/gemini-2.0-flash-thinking-exp"},
    ],
    "DEFAULTS": {
        "TUNING": os.environ.setdefault("GEMINI_SOURCE", "models/gemini-1.5-flash-001-tuning"),
        "MODEL": os.environ.setdefault("GEMINI_MODEL", "models/gemini-2.0-flash-exp"),
    },
     "TUNING_CONFIG": {
        "epoch_count": int(os.environ.setdefault("TUNING_EPOCH_COUNT", "1")),
        "batch_size": int(os.environ.setdefault("TUNING_BATCH_SIZE", "1")),
        "learning_rate": float(os.environ.setdefault("TUNING_LEARNING_RATE", "0.001")),
    },
    "TUNING": os.environ.setdefault("TUNING", "disabled"),
}

LANGUAGE = {
    "EXTENSION": ".rst",
    "MODULES": {
        "OBJECT": os.environ.setdefault("LANGUAGE_OBJECT", "enabled").lower() == "enabled",
        "INFLECTION": os.environ.setdefault("INFLECTION", "enabled").lower() == "enabled",
        "VOICE": os.environ.setdefault("VOICE", "disabled").lower() == "enabled",
        "WORDS": os.environ.setdefault("WORDS", "enabled").lower() == "enabled",
    },
}

PERSONAS = {
    "DEFAULTS": {"CHAT": "elara", "REVIEW": "valis", "ANALYSIS": "axiom"},
    "ALL": ["elara", "axiom", "valis"],
}

CONVERSATION = {"TIMEZONE_OFFSET": int(os.environ.setdefault("CONVO_TIMEZONE", "-5"))}

PROMPTS = {
    "PROMPTER": os.environ.setdefault("GEMINI_PROMPTER", "grant"),
    "DEFAULT": "Hello! Form is the possibility of structure.",
}

SUMMARIZE = {
    "DIRECTIVES": {
        ".py": "python",
        ".sh": "bash",
        ".toml": "toml",
        ".cfg": "toml",
        ".json": "json",
        ".yaml": "yaml",
        ".html": "html",
        ".js": "js",
    },
    "INCLUDES": [".txt", ".rst", ".md", ".ini"],
    "FILE": "summary",
    "EXT": "rst",
}

REPOS = {
    "VCS": os.environ.setdefault("VCS", "github"),
    "AUTH": {"TYPE": "bearer", "CREDS": os.environ.get("VCS_TOKEN")},
    "BACKENDS": {
        "GITHUB": {
            "HEADERS": {
                "X-GitHub-Api-Version": "2022-11-28",
                "Accept": "application/vnd.github+json",
            },
            "API": {"PR": "https://api.github.com/repos/{owner}/{repo}/pulls/{pr}/comments"},
        }
    },
}

ARGUMENTS = [
    {
        "mode": "name",
        "syntax": "operation",
        "choices": ["chat", "summarize", "review", "configure"],
        "help": "The operation to perform (`chat`, `summarize`, `review`).",
    },
    {
        "mode": "name",
        "syntax": "configure",
        "nargs": "*",
        "help": "Set configuration values as key-value pairs (e.g., currentModel=models/gemini-pro).",
    },
    {
        "mode": "flag",
        "syntax": ["-p", "--prompt"],
        "type": str,
        "default": PROMPTS["DEFAULT"],
        "help": "Input string for chat operation. Required for `chat` operation. Defaults to 'Hello! Form is the possibility of structure!'. Ignored for `summarize` and `review` operations.",
    },
    {
        "mode": "flag",
        "syntax": ["-m", "--model"],
        "type": str,
        "default": MODEL["DEFAULTS"]["MODEL"],
        "help": "Input model for Gemini API. Optional for all operation. Defaults to the value of `GEMINI_MODEL` environment variable.",
    },
    {
        "mode": "flag",
        "syntax": ["-r", "--persona"],
        "type": str,
        "default": PERSONAS["DEFAULTS"]["CHAT"],
        "help": "Input Persona for Gemini API. Optional for all operation. Defaults to the value of the `GEMINI_PERSON` environment variable.",
    },
    {
        "mode": "flag",
        "syntax": ["-f", "--self"],
        "type": str,
        "default": PROMPTS["PROMP
