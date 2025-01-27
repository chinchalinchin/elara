"""
app.py
------

Objects for managing application and service responses.
"""
# Standard Library Modules
import dataclasses

@dataclasses.dataclass
class Output:
    """
    Data structure for managing application output.
    """
    prompt                                  : str | None = None
    response                                : dict | None = None
    includes                                : dict | None = None

    def to_dict(self):
        return {
            "prompt"                        : self.prompt,
            "response"                      : self.response,
            "includes"                      : self.includes
        }


@dataclasses.dataclass
class FileReview:
    path: str
    comments: str
    bugs: str | None = None
    amendments: str | None = None

    
@dataclasses.dataclass
class ReviewResponse:
    score: str
    overall: str
    files: list[FileReview]
