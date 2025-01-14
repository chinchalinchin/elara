import os
from pathlib import Path

import google.generativeai as genai

THIS_DIR = Path(__file__).resolve().parent
DATA_DIR = os.path.join(THIS_DIR, "data")
PERSONA_DIR = os.path.join(DATA_DIR, "persona")
TUNING_DIR = os.path.join(DATA_DIR, "tuning")

PROMPTER = os.environ.setdefault("GEMINI_PROMPTER", "grant")

GENERATION_CONFIG = genai.types.GenerateContentConfig(
    candidate_count=int(os.environ.setdefault("GEMINI_CANDIDATES", "1")),
    max_output_tokens=int(os.environ.setdefault("GEMINI_OUTPUT_TOKENS", "6000")),
    temperature=float(os.environ.setdefault("GEMINI_TEMPERATURE", "0.7")),
    top_p=float(os.environ.setdefault("GEMINI_TOP_P", "0.9")), 
    top_k=int(os.environ.setdefault("GEMINI_TOP_K", "40")),
    system_instruction=[
        'You are a helpful language translator.',
        'Your mission is to translate text in English to French.'
    ],
    safety_settings = [
        genai.types.SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT",
            threshold="BLOCK_NONE",
        ),
        genai.types.SafetySetting(
            category="HARM_CATEGORY_HATE_SPEECH",
            threshold="BLOCK_NONE",
        ),
        genai.types.SafetySetting(
            category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
            threshold="BLOCK_NONE",
        ),
        genai.types.SafetySetting(
            category="HARM_CATEGORY_HARASSMENT",
            threshold="BLOCK_NONE",
        ),
    ]
)

SUMMARIZE = {
    "DIRECTIVES": {
        ".py": ".. code:: python",
        ".sh": ".. code:: bash", 
        ".toml": ".. code:: toml",
        ".cfg": ".. code:: toml",
        ".json": ".. code:: json",
        ".yaml": ".. code:: yaml",
        ".html": ".. code: html",
        ".js": ".. code: js"
    },
    "INCLUDES": [        
        ".txt", 
        ".rst", 
        ".md",
        ".ini"
    ]
}

EXTENSIONS = [ 
    k for k in SUMMARIZE["DIRECTIVES"].keys()
] + SUMMARIZE["INCLUDES"]

DEFAULTS = {
    "CONTEXT": os.environ.setdefault("GEMINI_CONTENXT", 
                                     os.path.join(DATA_DIR,"context.rst")),
    "SUMMARY": THIS_DIR,
    "SOURCE": os.environ.setdefault("GEMINI_SOURCE", "models/gemini-1.5-flash"),
    "MODEL": os.environ.setdefault("GEMINI_MODEL", "tunedModels/elara"),
    "PERSONA": os.environ.setdefault("GEMINI_PERSONA", "elara"),
    "PROMPT": "Hello Elara! Form is the possibility of structure.",
    "EXPERIMENT": "duality"
}

ARGUMENTS = [{
    "mode": "name",
    "syntax": "operation",
    "choices": ["chat", "conduct", "summarize"],
    "help": "The operation to perform (chat, conduct)"
},{
    "mode": "flag",
    "syntax": ["-p", "--prompt"],
    "type": str,
    "default": DEFAULTS["PROMPT"],
    "help": "Input string for chat operation."
},{
    "mode": "flag",
    "syntax": ["-c", "--context"],
    "type": str,
    "default": DEFAULTS["CONTEXT"],
    "help": "Override the default context file."
},{
    "mode": "flag",
    "syntax": ["-e", "--experiment"],
    "type": str,
    "default": DEFAULTS["EXPERIMENT"],
    "help": "Input experiment for conduct operation."
},{
    "mode": "flag",
    "syntax": ["-m", "--model"],
    "type": str,
    "default": DEFAULTS["MODEL"],
    "help": "Input model for Gemini API."
},{
    "mode": "flag",
    "syntax": ["-d", "--directory"],
    "default": DEFAULTS["SUMMARY"],
    "type": str,
    "help": "The path to the directory to summarize. Required for 'summarize' operation."
}]

API_KEY = os.environ.get("GEMINI_KEY")

if API_KEY is None:
    raise ValueError("GEMINI_KEY environment variable not set.")

