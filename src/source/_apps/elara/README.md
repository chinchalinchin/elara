# elara

A Python package for interacting with Google's Gemini API. This application uses preambles, context, system instructions and tuning to generate personas on top of the base Gemini models.

The following personas are under development.

- Elara: A generalized assistant. Whimsical, absurd and playful. 
- Axiom: A mathematical mind. Thoughtful, precise and deep.

## Quickstart 

### Build

```bash
pip install build
python -m build
pip install dist/elara-0.1.0-py3-none-any.whl
```

##  Usage 

### Authentication

**Gemini API**

The application ingests the Gemini API token through the ``GEMINI_KEY`` environment variable.

```bash
export GEMINI_KEY="key goes here"
elara chat -p 
```

**VCS**

The application ingests VCS tokens through the ``VCS_TOKEN`` environment variable.

```bash
export VCS_TOKEN="token goes here"
elara review -pr 7 -c <sha> 
```
### Contextual Chat 

The `chat` command will contextualize the prompt and forward it to the Gemini API.

```bash
elara chat -p "Hello Gemini!" 
```

The `summarize` command will generate an RST summary of a directory and its contents.

```bash
elara summarize -d /path/to/directory
```

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