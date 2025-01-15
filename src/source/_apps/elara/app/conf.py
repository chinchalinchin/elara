""" # conf.py
Constants and static functions for the application.
"""
# Standard Library Modules
import os
from pathlib import Path

# External Modules
import google.generativeai as genai

_dir = Path(__file__).resolve().parent

PERSIST = {
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
        }
    }
}
"""Configuration for application file structures and output."""

MODEL = {
    "GENERATION_CONFIG": genai.types.GenerationConfig(
        candidate_count=int(os.environ.setdefault("GEMINI_CANDIDATES", "1")),
        max_output_tokens=int(os.environ.setdefault("GEMINI_OUTPUT_TOKENS", "6000")),
        temperature=float(os.environ.setdefault("GEMINI_TEMPERATURE", "0.7")),
        top_p=float(os.environ.setdefault("GEMINI_TOP_P", "0.9")), 
        top_k=int(os.environ.setdefault("GEMINI_TOP_K", "40"))
    ),
    "SAFETY_SETTINGS": {
        genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_NONE
    }, 
    "BASE_MODELS": [{
        "tag": "pro",
        "path": "models/gemini-1.5-pro-latest"
    }, {
        "tag": "flash",
        "path": "models/gemini-1.5-flash-latest"
    },{
        "tag": "flash-tune",
        "path": "models/gemini-1.5-flash-001-tuning"
    }, {
        "tag": "flash-exp",
        "path": "models/gemini-2.0-flash-exp"
    },{
        "tag": "flash-think-exp",
        "path": "models/gemini-2.0-flash-thinking-exp"
    }]
}
"""Configuration for ``google.generativeai.GenerativeModel``"""

LANGUAGE = {
    "EXTENSION": ".rst",
    "MODULES": {
        "OBJECT": bool(os.environ.setdefault("LANGUAGE_OBJECT", "1")),
        "INFLECTION": bool(os.environ.setdefault("INFLECTION", "1")),
        "VOICE": bool(os.environ.setdefault("VOICE", "0")),
        "WORDS": bool(os.environ.setdefault("WORDS", "1"))
    }
}
"""Configuration for Language modules"""

PERSONAS = {
    "ALL": ["elara", "axiom"]
}
"""Configuration for personas"""

CONVERSATION = {
    "TIMEZONE_OFFSET": int(os.environ.setdefault("CONVO_TIMEZONE","-5"))
}

DEFAULTS = {
    "SOURCE": os.environ.setdefault("GEMINI_SOURCE", "models/gemini-1.5-flash-001-tuning"),
    "MODEL": "models/gemini-2.0-flash-exp",
    # "MODEL": os.environ.setdefault("GEMINI_MODEL", "tunedModels/elara-a38gqsr3zzw8"),
    "PERSONA": os.environ.setdefault("GEMINI_PERSONA", "elara"),
    "PROMPTER": os.environ.setdefault("GEMINI_PROMPTER", "grant"),
    "PROMPT": "Hello! Form is the possibility of structure.",
}
"""Configuration for application deaults"""

SUMMARIZE = {
    "DIRECTIVES": {
        ".py": "python",
        ".sh": "bash", 
        ".toml": "toml",
        ".cfg": "toml",
        ".json": "json",
        ".yaml": "yaml",
        ".html": "html",
        ".js": "js"
    },
    "INCLUDES": [        
        ".txt", 
        ".rst", 
        ".md",
        ".ini"
    ],
    "FILE": "summary",
    "EXT": "rst"
}
"""Configuration for the ``summarize`` function. """

ARGUMENTS = [{
    "mode": "name",
    "syntax": "operation",
    "choices": ["chat", "summarize"],
    "help": "The operation to perform (`chat`, `summarize`). Chat "
},{
    "mode": "name",
    "syntax": "configure",
    "nargs": "*",
    "help": "Set configuration values as key-value pairs (e.g., currentModel=models/gemini-pro)."
},{
    "mode": "flag",
    "syntax": ["-p", "--prompt"],
    "type": str,
    "default": DEFAULTS["PROMPT"],
    "help": "Input string for chat operation. Required for `chat` operation. Defaults to 'Hello! Form is the possibility of structure!'"
},{
    "mode": "flag",
    "syntax": ["-m", "--model"],
    "type": str,
    "default": DEFAULTS["MODEL"],
    "help": "Input model for Gemini API. Optional for `chat` operation. Defaults to the value of `GEMINI_MODEL` environment variable."
},{
    "mode": "flag",
    "syntax": ["-r", "--persona"],
    "type": str,
    "default": DEFAULTS["PERSONA"],
    "help": "Input Persona for Gemini API. Optional for `chat` operation. Defaults to the value of the `GEMINI_PERSON` environment variable."
},{
    "mode": "flag",
    "syntax": ["-f", "--self"],
    "type": str,
    "default": DEFAULTS["PROMPTER"],
    "help": "Input Prompter for Gemini API. Optional for `chat` operation. Defaults to the value of the `GEMINI_PROMPTER` environment variable."
},{
    "mode": "flag",
    "syntax": ["-d", "--directory"],
    "default": None,
    "type": str,
    "help": "The path to the directory to summarize. Required for 'summarize' operation. Optional for the `chat` operation."
}]
"""Configuration for command line arguments"""

VERSION = os.environ.setdefault("VERSION", "1.0")
"""Version configuration"""

API_KEY = os.environ.get("GEMINI_KEY")
"""Gemini API key"""

if API_KEY is None:
    raise ValueError("GEMINI_KEY environment variable not set.")

def summary_extensions():
    """
    Returns all valid extensions for ``summarize()`` function
    """
    return [ 
        k for k in SUMMARIZE["DIRECTIVES"].keys()
    ] + SUMMARIZE["INCLUDES"]

def summary_file():
    """
    Returns the ``summarize()`` filename and extension
    """
    return ".".join([SUMMARIZE["FILE"], SUMMARIZE["EXT"]])

def language_modules():
    """
    Return a list of enabled Language modules.
    """
    if any(v for v in LANGUAGE["MODULES"].values()):
        return [ k.lower() for k,v in LANGUAGE["MODULES"].items() ]
    return []