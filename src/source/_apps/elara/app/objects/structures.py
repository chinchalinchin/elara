import enum 

import typing

class ReviewScore(enum.Enum):
    PASS = "pass"
    FAIL = "fail"

class FileReview(typing.TypedDict):
    file_path: str
    potential_bugs:  str | None
    potential_optimizations:  str | None
    general_comments: str | None
    amended_code: str | None 

class Review(typing.TypedDict):
    score: ReviewScore
    files: typing.List[FileReview]