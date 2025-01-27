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
    ANAYLZE                                 = "analyze"
    CONVERSE                                = "converse"
    REVIEW                                  = "review"
    REQUEST                                 = "request"

class ConvoProps(enum.Enum):
    """
    Conversation property key enumeration.
    """
    # Internal Properties
    HISTORY                                     = "history"
    MEMORY                                      = "memory"
    MESSAGE                                     = "msg"
    TIMESTAMP                                   = "timestamp"
    NAME                                        = "name"
    # Configuration Properties
    SCHEMA_FILENAME                             = "SCHEMA_FILENAME"

class RepoProps(enum.Enum):
    """
    Conversation property key enumeration.
    """
    # Internal Properties
    OWNER                                       = "owner"
    REPO                                        = "repo"
    VCS                                         = "vcs"
    # Configuration Properties 
    AUTH                                        = "AUTH"
    BACKENDS                                    = "BACKENDS"
    VCS_TYPE                                    = "VCS"
    TYPE                                        = "TYPE"
    GITHUB                                      = "GITHUB"
    # GITHUB Service Properties
    API                                         = "API"
    PR                                          = "PR"
    COMMENTS                                    = "COMMENTS"
    PULLS                                       = "PULLS"
    FILES                                       = "FILES"
    CREDS                                       = "CREDS"
    HEADERS                                     = "HEADERS"