import os
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
DATA_DIR = os.path.join(THIS_DIR, "data")
PERSONA_DIR = os.path.join(DATA_DIR, "persona")

PROMPTER = os.environ.setdefault("GEMINI_PROMPTER", "grant")


SUMMARY = {
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

WHITELISTED_EXTS = [ 
    k for k in SUMMARY["DIRECTIVES"].keys()
]+ SUMMARY["INCLUDES"]

DEFAULTS = {
    "CONTEXT": os.path.join(DATA_DIR,"context.rst"),
    "SUMMARY": THIS_DIR,
    "MODEL": os.environ.setdefault("GEMINI_MODEL", "gemini-1.5-pro"),
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

