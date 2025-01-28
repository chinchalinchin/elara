"""
constants.py
------------

Application constants and properties.
"""

import enum


class Functions(enum.Enum):
    """
    Application functions enumeration.
    """
    ANAYLZE             = "analyze"
    CONVERSE            = "converse"
    REVIEW              = "review"
    REQUEST             = "request"


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
    SCHEMA_FILENAME     = "SCHEMA_FILENAME"


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
    SCHEMA_FILENAME     = "SCHEMA_FILENAME"


class ModelProps(enum.Enum):
    """
    Model property key enumeration
    """
    # Internal Properties
    NAME                = "name"
    VERSION             = "version"
    PATH                = "path"


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
    AUTH                = "AUTH"
    BACKENDS            = "BACKENDS"
    VCS_TYPE            = "VCS"
    TYPE                = "TYPE"
    GITHUB              = "GITHUB"
    # GitHub Service Properties
    API                 = "API"
    PR                  = "PR"
    COMMENTS            = "COMMENTS"
    PULLS               = "PULLS"
    FILES               = "FILES"
    CREDS               = "CREDS"
    HEADERS             = "HEADERS"