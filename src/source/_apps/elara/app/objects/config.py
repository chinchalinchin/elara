import json 
import os


class Config:
    _rel_path = None

    inst = None
    
    data = None

    directory = None 

    def __init__(
        self, 
        app_directory : str, 
        rel_path : str = os.path.join("data", "config.json")
    ):
        self.app_directory = app_directory
        self.rel_path = rel_path
        self.file_name = os.path.join(
            self.app_directory, 
            self._rel_path 
        )
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
            with open(self.file_name, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading config file: {e}")
            self.data = {}
    
    def _override(self):
        """
        Override configuration with environment variables, if applicable.
        """

        self.data["TUNING_SOURCE"] = os.environ.get(
            "TUNING_SOURCE", 
            self.data["MODEL"]["DEFAULTS"]["TUNING"]
        )

        self.data["DEFAULT_MODEL"] = os.environ.get(
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
                "LANGUAGE_WORDS", 
                self.data["LANGUAGE"]["MODULES"]["WORDS"]
            )
        )

        self.data["CONVERSATION"]["TIMEZONE_OFFSET"] = int(
            os.environ.get(
                "CONVO_TIMEZONE", 
                self.data["CONVERSATION"]["TIMEZONE_OFFSET"]
            )
        )
        
        self.data["ANALYSIS"]["LATEX_PREAMBLE"] = os.environ.get(
            "LATEX_PREAMBLE",
            self.data["LATEX_PREAMBLE"]
        )

        self.data["REPO"]["VCS"] = os.environ.get(
            "VCS", 
            self.data["REPOS"]["VCS"]
        )

        self.data["REPO"]["AUTH"]["CREDS"] = os.environ.get(
            "VCS_TOKEN",
            self.data["REPO"]["AUTH"]["CREDS"]
        )

        self.data["VERSION"] = os.environ.get(
            "VERSION", 
            self.data["VERSION"]
        )

        self.data["GEMINI_KEY"] = os.environ.get(
            "GEMINI_KEY", 
            self.data["GEMINI_KEY"]
        )

        self.data["DEBUG"] = os.environ.get(
            "DEBUG", 
            self.data["DEBUG"]
        )

    def save(self):
        """
        Saves the cache to the JSON file in ``data`` directory.
        """
        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=4)
        return True
    
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

    def update(self, **kwargs):
        """
        Update the Config using keyword arguments. Key must exist in Config to be updated.
        """
        for key, value in kwargs.items():
            if key not in self.data:
                continue 

            if isinstance(self.data[key], list) and isinstance(value, list):
                self.data[key].extend(value)
            elif isinstance(self.data[key], dict) and isinstance(value, dict):
                self.data[key].update(value)
            else:
                self.data[key] = value
    
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
            k for k in self.data["SUMMARIZE"]["DIRECTIVES"].keys()
        ] + self.data["SUMMARIZE"]["INCLUDES"]

    def summary_file(self):
        """
        Returns the ``summarize()`` filename and extension
        """
        return ".".join([
            self.data["SUMMARIZE"]["FILE"], 
            self.data["SUMMARIZE"]["EXT"]
        ])

    def language_modules(self):
        """
        Return a list of enabled Language modules.
        """
        modules = self.data["LANGUAGE"]["MODULES"]
        if any(v == "enabled" for v in modules.values()):
            return [
                k.lower()
                for k,v
                in modules.items()
                if v == "enabled"
            ]
        return []