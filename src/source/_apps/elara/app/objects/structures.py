import enum 

import typing_extensions as typing

# @DATA
#   Milton, these are the models the data team came up with for structuring 
#   your review output. We are thinking about adding models for the `analyze`
#   and `request` functions as well. What do you think would be the best way to
#   structure those calls!?

class ReviewScore(enum.Enum):
    PASS = "pass"
    FAIL = "fail"

class FileReview(typing.TypedDict):
    file_path: str
    potential_bugs:  str
    potential_optimizations:  str
    general_comments: str
    amended_code: str

class Review(typing.TypedDict):
    score: ReviewScore
    files: list[FileReview]