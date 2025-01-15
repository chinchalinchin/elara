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

### Flow

- Application Initializes: `parse.init()` traverses `data`, `modules` and `templates`.
- 
### Tuned Models 

Tuned models are initialized the first time the command line interface is invoked. These models have been fine-tuned with JSONs in `data/tuning/*`.

### Data

All context is managed in the `data` directory. The application uses the contents of the `preamble` and `threads` subdirectories to format the prompts that are sent to the Gemini API.  

1. `data/preamble`: This subdirectory contains RST documents that are prefixed to every prompt. They provide additional context to the Gemin model. They are templated with Jinja2 and conditionally rendered based on user input.
2. `data/threads`: This subdirectory contains RST documents the conversation history with Gemini. All prompts and response are persisted in these documents.
2. `data/system`: This subdirectory contains TXT containg system instructions that are provided to the Gemini model.
3. `data/tuning`: This contains JSON files with tuning data. These are used to initialize the persona models.