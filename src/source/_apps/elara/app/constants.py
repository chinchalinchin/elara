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
    MEMORIES                                    = "memories"
    MEMORY                                      = "memory"
    SEQUENCE                                    = "sequence"
    FEEDBACK                                    = "feedback"
    MESSAGE                                     = "msg"
    TIMESTAMP                                   = "timestamp"
    NAME                                        = "name"
    # Configuration Properties
    SCHEMA_FILENAME                             = "SCHEMA_FILENAME"

