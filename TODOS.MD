```python
def review(
    pr: str,
    src: str,
    owner: str,
    commit: str,
    model_name: str = None,
    show: bool = True,
) -> dict:
    source = repo.Repo(repo=src, owner=owner, commit=commit)
    prompt = parse.scrutinize(src=source)
    gemini_res = model.reply(
        prompt=prompt, persona=conf.PERSONAS["DEFAULTS"]["REVIEW"], model_name=model_name
    )

    if show:
       _format_output(prompt, gemini_res)
    
    # Regex to parse file paths and their corresponding comments from Gemini's output
    file_comment_pattern = re.compile(r"^(.*?)\n(.*?)(?=\n\n|\Z)", re.DOTALL | re.MULTILINE)
    file_comments = {}
    for match in file_comment_pattern.finditer(gemini_res):
        file_path = match.group(1).strip()
        comment = match.group(2).strip()
        if file_path and comment:
            file_comments[file_path] = comment
        else:
            logger.warning(f"Could not parse the following match: {match.group()}")

    try:
        github_res = source.comment(
            msg = gemini_res, 
            pr = pr,
            commit = commit,
            file_comments=file_comments,
            )
        logger.info(f"Github response: {github_res}")
        return {
            "gemini": gemini_res,
            "github": github_res
        }
    except Exception as e:
       logger.error(f"An unexpected error occurred in the `review` function: {e}")
       return {
            "gemini": gemini_res
        }
```

```python
def summarize(directory: str, stringify: bool = False) -> dict:
    if not os.path.isdir(directory):
        raise errors.SummarizeDirectoryNotFoundError(f"{directory} does not exist.")

    summary_file = conf.summary_file()
    output_file = os.path.join(directory, summary_file)

    try:
        tree_output = subprocess.check_output(["tree", "-n", directory], text=True)
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
    }

    for entry in os.scandir(directory):
        if not entry.is_file():
            continue
        file_path = entry.path
        base, ext = os.path.splitext(entry.name)
        if ext not in conf.summary_extensions() or base == conf.SUMMARIZE["FILE"]:
            continue
        try:
            with open(file_path, "r") as infile:
                data = infile.read()
                directive = ext in conf.SUMMARIZE["DIRECTIVES"].keys()
                if directive:
                    template_vars["files"].append(
                        {
                            "type": "code",
                            "data": data,
                            "lang": conf.SUMMARIZE["DIRECTIVES"][ext],
                            "name": os.path.relpath(file_path, directory),
                        }
                    )
                else:
                    template_vars["files"].append(
                        {
                            "type": "raw",
                            "data": data,
                            "name": os.path.relpath(file_path, directory),
                        }
                    )
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")

    payload = templates.Template().render("summary", template_vars)

    if not stringify:
        with open(output_file, "w") as out:
            out.write(payload)
        print(f"Summary generated at: {output_file}")

    return {"summary": payload}


```