"""
constants.py
------------

Application constants and properties.
"""

import enum


# APPLICATION PROPERTIES

class Functions(enum.Enum):
    """
    Application function key enumeration.
    """
    ANAYLZE             = "analyze"
    BRAINSTORM          = "brainstorm"
    CONVERSE            = "converse"
    REVIEW              = "review"
    REQUEST             = "request"
    TUNE                = "tune"

class FactoryProps(enum.Enum):
    """
    Application property key enumeration
    """
    AUTH_GEMINI         = "objects.model.gemini.key"
    AUTH_VCS            = "objects.repository.auth.creds"
    DIR_DATA            = "tree.directories.data"
    DIR_CONTEXT         = "tree.directories.context"
    DIR_PERSONA         = "tree.directories.personas"
    DIR_THREADS         = "tree.directories.threads"
    DIR_LOGS            = "tree.directories.logs"
    DIR_TEMPLATES       = "tree.directories.templates"
    FILE_LOG            = "tree.files.logs"
    FILE_CACHE          = "tree.files.cache"
    EXT_CONTEXT         = "tree.extensions.context"
    EXT_TEMPLATES       = "tree.extensions.templates"
    EXT_THREADS         = "tree.extensions.threads"
    EXT_PERSONA         = "tree.extensions.personas"
    OBJECT_CONVO        = "objects.conversation"
    OBJECT_DIR          = "objects.directory"
    OBJECT_PERSONA      = "objects.persona"
    OBJECT_MODEL        = "objects.model"
    OBJECT_TERMINAL     = "objects.terminal"
    OBJECTS_REPOSITORY  = "objects.repository"
    VCS                 = "objects.repository.vcs"
    LOG_LEVEL           = "logs.level"
    LOG_SCHEMA          = "logs.schema"
    
# SERVICE PROPERTIES

class VersionControl(enum.Enum):
    GITHUB              = "github"

# OBJECT PROPERTIES

class CommandLineProps(enum.Enum):
    """
    Command line argument property key enumeration.
    """
    # Argument Configuration Properties
    PARSER_HELP         = "help.parser"
    SUBPARSER_HELP      = "help.subparser"
    SUBPARSER_DEST      = "operation"
    OPERATIONS          = "operations"
    ARGUMENTS           = "arguments"
    FIELDS              = "fields"
    NAME                = "name"
    # Argument Schema Configuration Properties
    HELP                = "help"
    SYNTAX              = "syntax"
    DEST                = "dest"
    ACTION              = "action"
    NARGS               = "nargs"
    DEFAULT             = "default"
    TYPE                = "type"


class ConvoProps(enum.Enum):
    """
    Conversation property key enumeration.
    """
    # Internal Properties
    HISTORY             = "history"
    MEMORY              = "memory"
    MESSAGE             = "msg"
    TIMESTAMP           = "timestamp"
    NAME                = "name"
    # Configuration Properties
    SCHEMA_FILENAME     = "schema_filename"
    TIMEZONE_OFFSET     = "timezone_offset"

class ConfigProps(enum.Enum):
    """
    Configuration property key enumeration.
    """
    OVERRIDES           = "overrides"
    

class ContextProps(enum.Enum):
    """
    Context property key enumeration
    """
    # Internal Properties 
    POEMS               = "poems"
    PROOFS              = "proofs"
    QUOTES              = "quotes"


class PersonaProps(enum.Enum):
    """
    Persona property key enumeration 
    """
    # Internal Properties
    TUNING              = "tuning"
    SYSTEM_INSTRUCTION  = "system"
    CONTEXT             = "context"
    FUNCTIONS           = "functions"
    TOOLS               = "tools"
    GENERATION_CONFIG   = "generation_config"
    SAFETY_SETTINGS     = "safety_settings"
    # Configuration Properties
    SCHEMA_FILENAME     = "schema_filename"


class ModelProps(enum.Enum):
    """
    Model property key enumeration
    """
    # Internal Properties
    NAME                = "name"
    VERSION             = "version"
    PATH                = "path"
    INPUT_LIMIT         = "input_token_limit"
    OUTPUT_LIMIT        = "output_token_limit"
    # Configuration Properties
    ## Gemini Properties
    GEMINI              = "gemini"
    API_KEY             = "key"
    DEFAULT             = "default"
    TUNING              = "tuning"
    SOURCE              = "source"

class CacheProps(enum.Enum):
    """
    Cache property key enumeration
    """
    # Internal Properties
    CURRENT_MODEL       = "current_model"
    CURRENT_PERSONA     = "current_persona"
    CURRENT_PROMPTER    = "current_prompter"
    TUNED_MODELS        = "tuned_models"
    TUNING_MODEL        = "tuning_model"

class RepoProps(enum.Enum):
    """
    Repository property key enumeration.
    """
    # Internal Properties
    OWNER               = "owner"
    REPO                = "repo"
    VCS                 = "vcs"
    # Configuration Properties 
    AUTH                = "auth"
    BACKENDS            = "backends"
    VCS_TYPE            = "vcs"
    TYPE                = "type"
    GITHUB              = "github"
    # GitHub Service Properties
    API                 = "api"
    PR                  = "pr"
    COMMENTS            = "comments"
    PULLS               = "pulls"
    FILES               = "files"
    CREDS               = "creds"
    HEADERS             = "headers"

# VARIOUS PROPERTIES

class ReviewScore(enum.Enum):
    """
    Pull request review score enumeration
    """
    PASS                = "pass"
    FAIL                = "fail"


class LanguageModules(enum.Enum):
    """
    Language module enumeration
    """
    WORDS               = "words"
    INFLECTION          = "inflection"
    VOICE               = "voice"
    OBJECT              = "object"