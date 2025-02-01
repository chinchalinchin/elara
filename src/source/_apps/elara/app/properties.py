"""
properties.py
------------

Application constants and properties.
"""

import enum


# APPLICATION PROPERTIES

class Functions(enum.Enum):
    """
    Application function key enumeration.
    """
    ## Administrative Functions
    CLEAR               = "clear"
    DEBUG               = "debug"
    ## Rendering Functions 
    SUMMARIZE           = "summarize"
    ## Model Functions
    MODELS              = "models"
    TUNE                = "tune"
    ## Generative Functions
    BRAINSTORM          = "brainstorm"
    CONVERSE            = "converse"
    FORMALIZE           = "formalize"
    REVIEW              = "review"
    REQUEST             = "request"


class AppProps(enum.Enum):
    """
    Application property key enumeration
    """
    # Structured Output Schemas and Mime Types
    BRAINSTORM_SCHEMA   = "functions.brainstorm.schema"
    BRAINSTORM_MIME_TYPE= "functions.brainstorm.mime"
    CONVERSE_SCHEMA     = "functions.converse.schema"
    CONVERSE_MIME_TYPE  = "functions.converse.mime"
    FORMALIZE_SCHEMA    = "functions.formalize.schema"
    FORMALIZE_MIME      = "functions.formalize.mime"
    REVIEW_SCHEMA       = "functions.review.schema"
    REVIEW_MIME_TYPE    = "functions.review.mime"
    REQUEST_SCHEMA      = "functions.request.schema"
    REQUEST_MIME        = "functions.request.mime"
    # Function Properties
    FUNCTIONS           = "functions"
    BLOCKS              = "blocks"
    LATEX               = "latex"
    LATEX_PREAMBLE      = "latex.preamble"
    REPORTS             = "reports"


class FactoryProps(enum.Enum):
    """
    Application property key enumeration
    """
    AUTH_GEMINI         = "objects.model.gemini.key"
    AUTH_VCS            = "objects.repository.auth.creds"
    DIR_DATA            = "tree.directories.data"
    DIR_INJECTIONS      = "tree.directories.injections"
    DIR_PERSONA         = "tree.directories.personas"
    DIR_THREADS         = "tree.directories.threads"
    DIR_TEMPLATES       = "tree.directories.templates"
    FILE_CACHE          = "tree.files.cache"
    EXT_INJECTIONS      = "tree.extensions.injections"
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
    
# SERVICE PROPERTIES

class VersionControl(enum.Enum):
    GITHUB              = "github"

# OBJECT PROPERTIES

class CacheProps(enum.Enum):
    """
    Cache property key enumeration
    """
    # Internal Properties
    CURRENT_MODEL       = "current_model"
    CURRENT_PERSONA     = "current_persona"
    CURRENT_PROMPTER    = "current_prompter"
    MODELS              = "models"
    TUNING_MODEL        = "tuning_model"

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


class ConfigProps(enum.Enum):
    """
    Configuration property key enumeration.
    """
    OVERRIDES           = "overrides"
    

class ConvoProps(enum.Enum):
    """
    Conversation property key enumeration.
    """
    # Internal Properties
    HISTORY             = "history"
    MEMORY              = "memory"
    MESSAGE             = "message"
    TIMESTAMP           = "timestamp"
    NAME                = "name"
    # Configuration Properties
    SCHEMA_FILENAME     = "schema_filename"
    TIMEZONE_OFFSET     = "timezone_offset"


class DirectoryProps(enum.Enum):
    """
    Directory property key enumeration
    """
    # Internal Properties
    ## Summary Properties
    SUMMARY             = "summary"
    SUMMARY_DIRECTORY   = "directory"
    SUMMARY_TREE        = "tree"
    SUMMARY_FILES       = "files"
    SUMMARY_TYPE        = "type"
    SUMMARY_DATA        = "data"
    SUMMARY_LANGUAGE    = "lang"
    SUMMARY_NAME        = "name"
    # Configuration Properties
    ## Summary Configuration Properties
    SUMMARY_DIRECTIVES  = "directives"
    SUMMARY_INCLUDES    = "includes"
    SUMMARY_EXCLUDES    = "excludes"
    SUMMARY_EXCLUDE_EXT = "ext"
    SUMMARY_EXCLUDE_DIR = "dir"
    SUMMARY_EXCLUDE_FILE= "file"
    

class InjectionProps(enum.Enum):
    """
    Injection property key enumeration
    """
    # Internal Properties 
    POEMS               = "poems"
    PROOFS              = "proofs"
    QUOTES              = "quotes"


class LogProps(enum.Enum):
    """
    Log property key enumeration
    """
    # Configuration Properties
    DIRECTORY           = "tree.directories.logs"
    FILE                = "tree.files.logs"
    LEVEL               = "logs.level"
    SCHEMA              = "logs.schema"


class PersonaProps(enum.Enum):
    """
    Persona property key enumeration 
    """
    # Internal Properties
    TUNING              = "tuning"
    SYSTEM_INSTRUCTION  = "system"
    CONTEXT             = "context"
    INJECTIONS          = "injections"
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
    # Configuration Properties
    ## Gemini Properties
    GEMINI              = "gemini"
    API_KEY             = "key"
    DEFAULT             = "default"
    TUNING              = "tuning"
    SOURCE              = "source"
    INPUT_LIMIT         = "input_token_limit"
    OUTPUT_LIMIT        = "output_token_limit"
    GENERATE            = "generateContent"
    METHODS             = "supported_generation_methods"


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
    HEADERS             = "headers"
    CREDS               = "creds"
    BACKENDS            = "backends"
    TYPE                = "type"
    API                 = "api"
    # GitHub Service Properties
    GITHUB              = "github"
    PR                  = "pr"
    COMMENTS            = "comments"
    PULLS               = "pulls"
    FILES               = "files"


class TerminalProps(enum.Enum):
    """
    Terminal property key enumeration.
    """
    # Internal Properties
    REQUEST             = "request"
    # Configuration Properties
    ## Shell Properties
    COMMANDS            = "commands"
    FUNCTIONS           = "functions"
    DISPLAY             = "display"
    INIT                = "init"
    TITLE               = "title"
    START               = "start"
    EXIT                = "exit"
    HELP                = "help"
    PROMPT              = "prompt"
    ## Gherkin Properties
    GHERKIN             = "gherkin"
    GHERKIN_BLOCKS      = "blocks"
    GHERKIN_HELP        = "help"


# VARIOUS PROPERTIES


class LanguageModules(enum.Enum):
    """
    Language module enumeration
    """
    WORDS               = "words"
    INFLECTION          = "inflection"
    VOICE               = "voice"
    OBJECT              = "object"


class ReviewScore(enum.Enum):
    """
    Pull request review score enumeration
    """
    PASS                = "pass"
    FAIL                = "fail"


class TemplateVars(enum.Enum):
    """
    Template variable enumeration
    """
    # Contextualizations
    CONTEXT             = "context"
    ## Injections
    INJECTIONS          = "injections"
    INJECT_POEMS        = "poems"
    INJECT_PROOFS       = "proofs"
    INJECT_QUOTES       = "quotes"
    # Reporting
    REPORT              = "reports"
    REPORT_SUMMARY      = "summary"
    REPORT_REPO         = "repository"
    REPORT_MODELS       = "models"
    REPORT_BASE         = "base_models"
    REPORT_TUNING       = "tuning_models"
    REPORT_TUNED        = "tuned_models"