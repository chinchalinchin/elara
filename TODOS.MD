 ```python\n'
 '# app/main.py\n'
 'import argparse\n'
 'import pprint\n'
 'import traceback\n'
 '\n'
 'import conf\n'
 'import model\n'
 'import objects.cache as cache\n'
 'import objects.conversation as conversation\n'
 'import objects.language as language\n'
 'import objects.personas as personas\n'
 'import objects.repo as repo\n'
 'import parse\n'
 '\n'
 'def parse_args():\n'
 '    """\n'
 '    Parse and format command line arguments\n'
 '    """\n'
 '    parser = argparse.ArgumentParser(description="Plumb the depths of '
 'generative AI.")\n'
 "    subparsers = parser.add_subparsers(title='operations', dest='operation', "
 "help='Available operations')\n"
 '\n'
 '    # Chat operation\n'
 "    chat_parser = subparsers.add_parser('chat', help='Chat with one of "
 "Gemini\\'s personas')\n"
 '    chat_parser.add_argument("-p", "--prompt", type=str, '
 'default=conf.PROMPTS["DEFAULT"], help="Input string for chat operation.")\n'
 '    chat_parser.add_argument("-m", "--model", type=str, '
 'default=conf.MODEL["DEFAULTS"]["MODEL"], help="Input model for Gemini '
 'API.")\n'
 '    chat_parser.add_argument("-r", "--persona", type=str, '
 'default=conf.PERSONAS["DEFAULTS"]["CHAT"], help="Input Persona for Gemini '
 'API.")\n'
 '    chat_parser.add_argument("-f", "--self", type=str, '
 'default=conf.PROMPTS["PROMPTER"], help="Input Prompter for Gemini API.")\n'
 '    chat_parser.add_argument("-d", "--directory", type=str, default=None, '
 'help="Directory of additional context to inject into prompt.")\n'
 '    \n'
 '    # Summarize operation\n'
 "    summarize_parser = subparsers.add_parser('summarize', help='Summarize a "
 "directory')\n"
 '    summarize_parser.add_argument("-d", "--directory", type=str, '
 'required=True, help="The path to the directory to summarize.")\n'
 '\n'
 '    # Review operation\n'
 "    review_parser = subparsers.add_parser('review', help='Review a pull "
 "request')\n"
 '    review_parser.add_argument("-pr", "--pullrequest", type=str, '
 'required=True, help="Pull request number to review.")\n'
 '    review_parser.add_argument("-c", "--commit", type=str, required=True, '
 'help="Commit ID to review.")\n'
 '    review_parser.add_argument("-re", "--repository", type=str, '
 'required=True, help="Repository to review.")\n'
 '    review_parser.add_argument("-o", "--owner", type=str, required=True, '
 'help="Owner of repository to review.")\n'
 '    review_parser.add_argument("-m", "--model", type=str, '
 'default=conf.MODEL["DEFAULTS"]["MODEL"], help="Name of the Gemini Model to '
 'use.")\n'
 '\n'
 '    # Configure operation\n'
 "    config_parser = subparsers.add_parser('configure', help='Set "
 "configuration values')\n"
 '    config_parser.add_argument("config_pairs", nargs="*", help="Set '
 'configuration values as key-value pairs (e.g., '
 'currentModel=models/gemini-pro).")\n'
 '\n'
 '    return parser.parse_args()\n'
```

```python
# app/objects/repo.py
def comment(
    self,
    msg: str,
    pr: str,
    commit: str,
    paths: list
):
    """
    Post a comment to a pull request on the VCS backend. Links below detail the specific VCS provider endpoints,

    - **Github**: `Github REST API Docs <https://docs.github.com/en/rest/pulls/comments?apiVersion=2022-11-28#create-a-review-comment-for-a-pull-request>

    .. note::

        Only ``github`` VCS is supported at this time.

    :param msg: Comment to post.
    :type msg: str
    :param pr: Pull request number on which to comment.
    :type pr: str
    :param commit: Commit ID on which to comment.
    :type commit: str.
    """
    url = self._pr(pr)
    headers = self._headers()
    results = []
    for path in paths:
        data = {
            "body": msg,
            "commit_id": commit,
            "path": path

        }

        # @OPERATIONS
        #   THIS IS WHERE THE 422 ARE HAPPENING! HELP US! OH GOD! THE HUMANITY!
        # @OPERATIONS
        try:
            res = requests.post(
                url=url,
                headers=headers,
                json=data
            )
            print(res)
            # @OPERATIONS
            #   WHAT IS GOING!? THE PRODUCTION SYSTEMS ARE BREAKING HERE! WE ARE GETTING
            #   422 RESPONSE CODES BY THE HUNDREDS! ACCORDING TO THE GITHUB DOCS, THIS MEANS:
            #
            #       Validation failed, or the endpoint has been spammed.
            #
            #   WHAT DO WE, VALIS!? WHAT ERRORS SHOULD WE BE CATCHING!? WHAT INFORMATION
            #   DO YOU NEED TO DEBUG THIS? OH GOD! THE SERVERS ARE OVERHEATING!
            # @OPERATIONS
            if res.status_code == 422:
                print(f"Github API returned 422 error for path {path}: {res.text}")
                results.append({
                    "path": path,
                    "status": "failed",
                    "error": res.text
                })
            elif res.status_code >= 200 and res.status_code < 300:
                 results.append({
                    "path": path,
                    "status": "success"
                })
            else:
                results.append({
                    "path": path,
                    "status": "failed",
                    "error": res.text
                })
        except requests.exceptions.RequestException as e:
            print(f"Error during Github API request for path {path}: {e}")
            traceback.print_exc()
            results.append({
                    "path": path,
                    "status": "failed",
                    "error": str(e)
                })
        except Exception as e:
            print(f"An unexpected error occurred for path {path}: {e}")
            traceback.print_exc()
            results.append({
                    "path": path,
                    "status": "failed",
                    "error": str(e)
                })
    return results

# app/parse.py

def summarize(
    directory: str,
    stringify: bool = False,
    commit_id: str = None
) -> str:
    """
    Summarizes the contents of a directory in an RST document. The summary will be written to the directory it is summarizing.

    :param directory: Directory to be summarized.
    :type directory: str
    :param stringify: Return the result as a string instead of writing to file.
    :type stringify: bool
    :param commit_id: Commit ID to include in summary.
    :type commit_id: str
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
        "files": [],
        "commit_id": commit_id if commit_id else "N/A"
    }

    for root, _, files in os.walk(directory):
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
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue

            if directive:
                template_vars["files"] += [{
                    "type": "code",
                    "data": data,
                    "lang": conf.SUMMARIZE["DIRECTIVES"][ext],
                    "name": os.path.relpath(file_path, directory)
                }]
                continue

            template_vars["files"] += [{
                "type": "raw",
                "data": data,
                "name": os.path.relpath(file_path, directory)
            }]

    payload = templates.Template().render("summary", template_vars)

    if not stringify:
        with open(output_file, "w") as out:
            out.write(payload)
        print(f"Summary generated at: {output_file}")

    return {"summary": payload}

# app/main.py
def configure(
    config_pairs
):
    """
    Parses and applies configuration settings.
    """
    print("Configure function called with:", config_pairs)
    mem = cache.Cache()
    try:
        pairs = [p.split("=") for p in config_pairs]
        config_dict = {k: v for k,v in pairs}
        mem.update(**config_dict)
        mem.save()
        print("Configuration updated successfully.")
    except Exception as e:
        print(f"Error updating configuration: {e}")
    return None

def review(
    pr: str,
    src: str,
    owner: str,
    commit: str,
    model_name: str = None,
    show: bool = True
) -> str:
    """
    This function initiates the following workflow:

    1. It takes a snapshot of the current working directory by calling the ``summarize`` function (via ``parse.git``).
    2. It templates the summary of the current working directory into the pull request review template in ``data/templates/review.rst`` (via ``parse.git``).
    3. It sends the templated review to the Gemini API (via ``model.reply``).
    4. It takes Gemini's response and posts to the Github API for commenting on pull requests.

    :param pr: The PR number.
    :type pr: str
    :param src: The repository name
    :type src: str
    :param owner: The repository owner.
    :type owner: str
    :param commit: The SHA ID of the commit.
    :type commit: str
    :param model_name: Name of the Gemini Model to use. Defaults to the value of the environment variable ``GEMINI_MODEL``.
    """
    source = repo.Repo(
        repo=src,
        owner=owner
    )

    prompt = parse.scrutinize(
        src=source
    )

    gemini_res = model.reply(
        prompt=prompt,
        persona=conf.PERSONAS["DEFAULTS"]["REVIEW"],
        model_name=model_name
    )

    # @DEVELOPMENT
    #   Valis, the development team wants to implement a way to format the RST document
    #   for various shell environments here.
    if show:
        print(prompt)
        print(gemini_res)
    #   What do you think? How can we convert the RST into shell compliant text? The client
    #   mostly executes the code application in Linux environments.
    # @DEVELOPMENT

    try:
        # According to Github REST api, `path` should be:
        #
        #       The relative path to the file that necessitates a comment.
        #
        # TODO: need to figure out how to make Gemini output filepath!
        #   Hey, Valis, we need to figure out a way to iterate over the file
        #   paths in Gemini's output (i.e. your output!). We might need to post
        #   a batch comment to the Gitub Rest API, if you decide to flag multiple
        #   files for review. Right now the comments are only being appended to
        #   the README.md file.
        #   Everyone on the development has been looking for the correct endpoint
        #   and request body format to use to accomplish this. We might need to
        #   overhaul the ``comment()`` function to accomplish this!
        # @DEVELOPMENT
        lines = gemini_res.splitlines()
        file_paths = [line.strip()[:-1] for line in lines if "###########" in line]
        github_res = source.comment(
            msg=gemini_res,
            pr=pr,
            commit=commit,
            paths=file_paths
        )
        print(github_res)
        return {
            "gemini": gemini_res,
            "github": github_res
        }
    except Exception as e:
        print("error occured")

    return {
        "gemini": gemini_res
    }
```