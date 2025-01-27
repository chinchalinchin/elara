# elara

A Python package for interacting with Google's Gemini API. This application uses preambles, context, system instructions and tuning to generate personas on top of the base Gemini models.

The following personas are under development.

- Elara: A generalized assistant. Whimsical, absurd and playful. 
- Axiom: A mathematical explorer. Thoughtful, precise and deep.
- Milton: An embittered engineer. Cranky, a bit of a sourpuss, but a top-tier programmer. 

## References

- [json-schema](https://json-schema.org/)
- [Gemini API](https://ai.google.dev/gemini-api/docs)

### Models 

- models/gemini-exp-1206
- models/gemini-exp-1121
- models/gemini-exp-1114
- models/gemini-2.0-flash-exp
- models/gemini-2.0-flash-thinking-exp
- models/gemini-2.0-flash-thinking-exp-01-21
- models/gemini-2.0-flash-thinking-exp-1219

## Quickstart 

### Build

```bash
pip install build
python3 -m build
pip install dist/elara-0.1.0-py3-none-any.whl
```

##  Usage 

### Configuration

Various properties can be configured through environment variables. See `app/conf.py` for a full list of everything that can be configured.

### Authentication

The application ingests API tokens through the `GEMINI_KEY` and `OBJECTS_REPO_AUTH_CREDS` environment variables.

```bash
## VARIABLES
# GEMINI_KEY: Gemini API key
# OBJECTS_REPO_AUTH_CREDS: Version control API token
export GEMINI_KEY="key"
export OBJECTS_REPO_AUTH_CREDS="token"
elara converse --prompt "Hi there, Elara!"
```

**Note**: The `OBJECTS_REPO_AUTH_CREDS` environment variable is only required for operations that require a VCS, such as having `milton` comment on pull requests. See the **Code Review** section below. 

### Contextual Conversation

The `converse` command will contextualize the prompt and forward it to the Gemini API,

```bash
elara converse --prompt "Hello Elara!" 
```

The conversation history is stored locally in the `data/history` directory as a JSON. This JSON is used to render Jinja2 templates to embed the chat history into a layer of context provided by the template. 

The summary of a local directory can also be injected into a chat prompt with the following argument,

```bash
## VARIABLES
# DIR: directory to summarize
elara converse --prompt "Take a look at this!" --directory $DIR
```

The default persona for conversations is `elara`. Gemini can assume a different persona if the persona flag is passed in as follows,

```bash
elara converse --prompt "Hello Axiom!" --persona "axiom"
```

### Directory Summaries

The `summarize` command will generate an RST summary of a directory and its contents with the following command,

```bash
## VARIABLES
# DIR: directory to summarize
elara summarize --directory $DIR
```

**NOTE**: The summary will be written to the directory it is summarizing. 

### Code Review

The persona `milton` will provide pull request comments on a local git repository and then post the comments to a VCS backend where the pull request is hosted. In order to use the pull request commenting functionality, the VCS backend must be set through the `OBJECTS_REPO_VCS` environment variable. Currently only values of `github` are supported. A personal access token must be provided through the `OBJECTS_REPO_AUTH_CREDS` environment variable.

Using the following commands,

```bash
## VARIABLES
# DIR: Directory containing the git repository to review.
# OWNER: The username of the repository owner.
# REPO: Name of the remote repository.
# PR_NUMBER: The number of the pull request to comment on. 
# OBJECTS_REPO_AUTH_CREDS: A personal access token for the Github API.
# OBJECTS_REPO_VCS: The name of the repository that contains the pull request.
export OBJECTS_REPO_VCS="github"
export OBJECTS_REPO_AUTH_CREDS="<inset API token>"
elara review --repository $REPO --owner $OWNER --pull $PR_NUMBER  --directory $DIR
```

In addition, `milton` has special tags that can be appended to code comments. These comment tags signal different types of attention `milton` will direct to certain sections of the code.

- `@DEVELOPMENT`: Attach this tag to comments above code that is still in the development phase. `milton` will provide helpful comments on possible solutions.
- `@OPERATIONS`: Attach this tag to comments above critical code that needs special attention. `milton` will direct his attention to searching this code for potential errors and bugs.
- `@DATA`: Attach this tag to comments above data structures. `milton` will analyze the data structure in the context of the application and suggests alternative constructions and ways of managing the data structure.

### Feature Request 

`milton` will can also implement functions in any programming language, if the functions are specified using a Gherkin-style specification. To initiate the feature request shell,

```bash
elara request
```

You will then be prompted to enter information regarding the feature request through the terminal. 

### Mathematical Analysis

The persona `axiom` will provide formal and mathematical analysis. Pass this persona a directory of RST documents and it will provide a scholarly review of its content. These documents can be formatted with LaTeX. The LaTeX preamble can be configured through the ``FUNCTIONS_ANALYZE_LATEX_PREAMBLE`` environment variable.

Use the following command,

```bash
elara analyze -d /path/to/directory
```

In addition, `axiom` has custom RST directives that provide enhanced functionality. These roles and directives are detailed below,

1. `critique`: This directive will cause the persona to provide a critique of its content.
2. `prove`: This directive will instruct the persona to provide a formal proof of the asserted theorem.
3. `todo`: This directive will instruct the persona to provide ideas and brainstorm.

As an example,

```rst

.. prove::

    :math:`a^2 + b^2 = c^2`
```

This will prompt `axiom` to generate a formal proof of the Pythagorean theorem. 

## Application Structure

### Tuned Models 

Tuned models are initialized the first time the command line interface is invoked. These models have been fine-tuned with JSONs in `data/tuning/*`.

### Data

All context is managed in the `data` directory. The application uses Jinja2 templates in the ``data/templates``

1. `data/templates`: This subdirectory contains RST templates that are rendered using user input.
2. `data/history`: This subdirectory contains JSONs that contain chat threads with different personas.
3. `data/system`: This subdirectory contains JSON that contain system instructions for each persona. 
4. `data/memories`: This subdirectory contains JSONS that contain chat memories with different personas.
4. `data/tuning`: This subdirectory contains JSON files with tuning data. These are used to initialize the persona models, if tuning is enabled through the ``TUNING`` environment variable.
5. `data/language`: This subdirectory contains RST modules for language processing. These modules add grammatical forms to the persona's diction.

### Language Modules

Additional language plugins can be injected into the prompt. The language modules can be found in ``data/modules``. To enable a Language module, set the value of the following environment variables,

```bash
export OBJECTS_LANGUAGE_MODULES_OBJECT=enabled
export OBJECTS_LANGUAGE_MODULES_INFLECTION=enabled
export OBJECTS_LANGUAGE_MODULES_VOICE=enabled
export OBJECTS_LANGUAGE_MODULES_WORDS=enabled

elara chat -p "Try out these sweet language modules, Elara!"
```

**TODO**: explain purpose of language modules