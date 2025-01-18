import json 
import os


class Config:
    # Config has to be naively aware of directory with hardcode values
    #   since it is the first data that is initialized in applciation.
    _rel_path = os.path.join("data", "config.json")

    inst = None
    
    data = None

    directory = None 

    def __init__(
        self, 
        app_directory : str
    ):
        self.app_directory = app_directory
        self._load()
        self._override()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(
                Config, 
                cls
            ).__new__(cls)
        return cls._instance

    def _load(self):
        """
        Load in configuration data from file.
        """
        try:
            file_name = os.path.join(
                self.app_directory, 
                self._rel_path 
            )
            with open(file_name, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading config file: {e}")
            self.data = {}

    def _override(self):
        """
        Override configuration with environment variables, if applicable.
        """
        self.data["MODEL"]["GENERATION_CONFIG"]["candidate_count"] = int(
            os.environ.get(
                "GEMINI_CANDIDATES", 
                self.data["MODEL"]["GENERATION_CONFIG"]["candidate_count"]
            )
        )
        self.data["MODEL"]["GENERATION_CONFIG"]["max_output_tokens"] = int(
            os.environ.get(
                "GEMINI_OUTPUT_TOKENS", 
                self.data["MODEL"]["GENERATION_CONFIG"]["max_output_tokens"]
            )
        )
        self.data["MODEL"]["GENERATION_CONFIG"]["temperature"] = float(
            os.environ.get(
                "GEMINI_TEMPERATURE", 
                self.data["MODEL"]["GENERATION_CONFIG"]["temperature"]
            )
        )
        self.data["MODEL"]["GENERATION_CONFIG"]["top_p"] = float(
            os.environ.get(
                "GEMINI_TOP_P", 
                self.data["MODEL"]["GENERATION_CONFIG"]["top_p"]
            )
        )
        self.data["MODEL"]["GENERATION_CONFIG"]["top_k"] = int(
            os.environ.get(
                "GEMINI_TOP_K", 
                self.data["MODEL"]["GENERATION_CONFIG"]["top_k"]
            )
        )

        self.data["MODEL"]["DEFAULTS"]["TUNING"] = os.environ.get(
            "GEMINI_SOURCE", 
            self.data["MODEL"]["DEFAULTS"]["TUNING"]
        )

        self.data["MODEL"]["DEFAULTS"]["MODEL"] = os.environ.get(
            "GEMINI_MODEL", 
            self.data["MODEL"]["DEFAULTS"]["MODEL"]
        )

        self.data["LANGUAGE"]["MODULES"]["OBJECT"] = bool(
            os.environ.get(
                "LANGUAGE_OBJECT",
                self.data["LANGUAGE"]["MODULES"]["OBJECT"]
            )
        )

        self.data["LANGUAGE"]["MODULES"]["INFLECTION"] = bool(
            os.environ.get(
                "LANGUAGE_INFLECTION", 
                self.data["LANGUAGE"]["MODULES"]["INFLECTION"]
            )
        )

        self.data["LANGUAGE"]["MODULES"]["VOICE"] = bool(
            os.environ.get(
                "LANGUAGE_VOICE", 
                self.data["LANGUAGE"]["MODULES"]["VOICE"]
            )
        )
        
        self.data["LANGUAGE"]["MODULES"]["WORDS"] = bool(
            os.environ.get(
                "WORDS", 
                self.data["LANGUAGE"]["MODULES"]["WORDS"]
            )
        )

        self.data["CONVERSATION"]["TIMEZONE_OFFSET"] = int(
            os.environ.get(
                "CONVO_TIMEZONE", 
                self.data["CONVERSATION"]["TIMEZONE_OFFSET"]
            )
        )

        self.data["PROMPTS"]["PROMPTER"] = os.environ.get(
            "GEMINI_PROMPTER", 
            self.data["PROMPTS"]["PROMPTER"]
        )

        self.data["REPOS"]["VCS"] = os.environ.get(
            "VCS", 
            self.data["REPOS"]["VCS"]
        )

        self.data["VERSION"] = os.environ.get(
            "VERSION", 
            self.data["VERSION"]
        )

        self.data["API_KEY"] = os.environ.get(
            "GEMINI_KEY", 
            self.data["API_KEY"]
        )

        self.data["DEBUG"] = os.environ.get(
            "DEBUG", 
            self.data["DEBUG"]
        )

        self.data["LATEX_PREAMBLE"] = os.environ.get(
            "LATEX_PREAMBLE",
            self.data["LATEX_PREAMBLE"]
        )

    def get(self, key, default=None):
        keys = key.split(".")
        value = self.data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
            if value is None:
                return default
        return value

    def set(self, key, value):
        keys = key.split(".")
        target = self.data
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value

    def tuning_enabled(self):
        """
        Returns a bool flag signaling models should be tuned.
        """
        return self.get("MODEL.TUNING") == "enabled"

    def summary_extensions(self):
        """
        Returns all valid extensions for ``summarize()`` function
        """
        return [
            k for k in self.get("SUMMARIZE.DIRECTIVES").keys()
        ] + self.get("SUMMARIZE.INCLUDES")

    def summary_file(self):
        """
        Returns the ``summarize()`` filename and extension
        """
        return ".".join([self.get("SUMMARIZE.FILE"), self.get("SUMMARIZE.EXT")])

    def language_modules(self):
        """
        Return a list of enabled Language modules.
        """
        modules = self.get("LANGUAGE.MODULES")
        if any(v == "enabled" for v in modules.values()):
            return [
                k.lower()
                for k,v
                in modules.items()
                if v == "enabled"
            ]
        return []