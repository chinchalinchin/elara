# elara

A Python package for interacting with Google's Gemini API. This application uses preambles, context, system instructions and tuning to generate personas on top of the base Gemini models.

The following personas are under development.

- Elara: A generalized assistant. Whimsical, absurd and playful. 
- Axiom: A mathematical mind. Thoughtful, precise and deep.
- Valis: A code analyst. Cranky, a bit of a sourpuss, but a top-tier programmer. 

## Quickstart 

### Build

```bash
pip install build
python -m build
pip install dist/elara-0.1.0-py3-none-any.whl
```

##  Usage 

### Configuration

Various properties can be configured through environment variables. See `app/conf.py` for a full list of everything that can be configured.

### Authentication

The application ingests API tokenS through the `GEMINI_KEY` and `VCS_TOKEN` environment variables.

```bash
## VARIABLES
# GEMINI_KEY: Gemini API key
# VCS_TOKEN: Version control API token
export GEMINI_KEY="key"
export VCS_TOKEN="token"
elara chat -p 
```

### Contextual Chat 

The `chat` command will contextualize the prompt and forward it to the Gemini API.

```bash
elara chat -p "Hello Gemini!" 
```

The `summarize` command will generate an RST summary of a directory and its contents with the followign command

```bash
## VARIABLES
# DIR: directory to summarize
elara summarize -d $DIR
```

A directory summary can also be injected into a chat prompt.

```bash
## VARIABLES
# DIR: directory to summarize
elara chat -p "Take a look at this!" -d $DIR
```
### Code Review

The application persona `valis` will provide pull request comments on the current working directory. In order to use the pull request commenting functionality, the VCS backend must be set through the `VCS` environment variable. Currently only values of `github` are supported. A personal access token must be provided through the `VCS_TOKEN` environment variable.

Using the following commands,

```bash
## VARIABLES
# PR_NUMBER: The number of the pull request to comment on. 
# REPO: The name of the repository that contains the pull request.
# OWNER: The username of the repository owner.
# COMMIT_ID: SHA Hash ID of the commit which opened the pull request.
# GITHUB_TOKEN: A personal access token for the Github API.
export VCS="github"
export VCS_TOKEN="token"
elara review -pr $PR_NUMBER -re $REPO -o $OWNER -c $COMMIT_ID
```

**TODO**: should allow user to change directory instead of running in current working directory!

In addition, `valis` will has special tags that can be appended to code comments. This comment tags signal different types of attention `valis` will direct to certain sections of the code.

- `@DEVELOPMENT`: Attach this tag to comments above code that is still in the development phase. `valis` will provide helpful comments on possible solutions.
- `@OPERATIONS`: Attach this tag to comments above critical code that needs special attention. `valis` will direct his attention to searching this code for potential errors and bugs.

## Application Structure

### Tuned Models 

Tuned models are initialized the first time the command line interface is invoked. These models have been fine-tuned with JSONs in `data/tuning/*`.

### Data

All context is managed in the `data` directory. The application uses Jinja2 templates in the ``data/templates``

1. `data/templates`: This subdirectory contains RST templates that are rendered using user input.
2. `data/history`: This subdirectory contains JSONs that contain chat threads with different personas.
2. `data/system`: This subdirectory contains JSON that contain system instructions for each persona. 
3. `data/tuning`: This contains JSON files with tuning data. These are used to initialize the persona models, if tuning is enabled through the ``TUNING`` environment variable.

### Language Modules

Additional language plugins can be injected into the prompt. The language modules can be found in ``data/modules``. To enable a Language module, set the value of the following environment variables,

```bash
export LANGUAGE_OBJECT=enabled
export LANGUAGE_INFLECTION=enabled
export LANGUAGE_VOICE=enabled
export LANGUAGE_WORDS=enabled

elara chat -p "Try out these sweet language modules, Elara!"
```