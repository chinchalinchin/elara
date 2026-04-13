import string
import typing

constants                                           = {
    "delimiter"                                     : " ",
    "punctuation"                                   : string.punctuation
}


# FORMALIZING FUNCTIONS
## These functions convert the Python data structures into formal entities.

def _reindex(s: str, i: int)                        -> str:
    """
    Args:
        - s: Any string.
        - i: Character index, starting at 1.
    """
    if i < 1:
        raise ValueError("Character Index starts at 1")
    
    if i > len(s):
        raise ValueError(f"Character Index ends at {len(s)}")
    
    return s[int(i-1)]


def _depunctuate(s: str)                             -> str:
    """
    Args:
        - s: Any string.
    """
    return "".join([a for a in s if a not in constants["punctuation"]])


# FORMALIZED FUNCTIONS
## These functions implement various functions of the formal model.

def invert(s: str)                                  -> str:
    return s[::-1]


def reduce(s: str)                                  -> str:
    """
    Args:
        - s: Any string.
    """
    return "".join([a for a in s if a != constants["delimiter"]])


def delimter_count(s: str)                          -> int:
    """
    Args:
        - s: Any string.
    """
    return len([1 for a in s if a == constants["delimiter"]])


def words(
    s                                               : str, 
    language                                        : typing.Callable = lambda _: True
)                                                   -> list:
    """
    Args:
        - s: Any string.
        - language: function that when a word is inputted determines if the word belongs to a given language. 
    """
    words                                           = []
    word                                            = ""

    for a in s:
        if a != constants["delimiter"]:
            word                                    += a
            continue

        if language:
            words.append(word)

        word                                        = ""

    if not is_empty(word):
        words.append(word)
        
    return words


def word_length(
    s                                               : str, 
    language                                        : typing.Callable = lambda _: True
)                                                   -> int: 
    """
    Args:
        - s: Any string.
        - language: function that when a word is inputted determines if the word belongs to a given language. 
    """
    return len(words(s, language))


def pivot_char(s: str)                              -> str:
    """
    Args:
        - s: Any string.
    """
    if len(s) % 2 == 0:
        left_index, right_index                     = len(s)/2, (len(s) + 2)/2
            
    if len(s) % 2 == 1:
        left_index, right_index                     = (len(s) + 1)/2, (len(s) + 1)/2

    if _reindex(s, left_index) == _reindex(s, right_index):
        return _reindex(s, left_index)

    return None


def pivot_word(
    s                                               : str, 
    language                                        : typing.Callable = lambda _: True
)                                                   -> str:
    """
    Args:
        - s: Any string.
        - language: function that when a word is inputted determines if the word belongs to a given language. 
    """
    w                                               = words(s, language)
    if len(w) % 2 == 0:
        left_index, right_index                     = len(w)/2, (len(w) + 2)/2
    
    if len(w) % 2 == 1:
        left_index,right_index                      = (len(w) + 1)/2, (len(w) + 1)/2

    if _reindex(w, left_index) == invert(_reindex(w, right_index)):
        return _reindex(w, left_index)
        
    return None


# TRUTH VALUE FUNCTIONS

## SYNTACTIC TRUTH VALUES

def is_empty(s: str):
    """
    Args:
        - s: Any string.
    """
    return s == "" or s is None


def is_palindrome(s: str)                           -> bool:
    """
    Args:
        - s: Any string.
    """
    return reduce(s) == invert(reduce(s))


## SEMANTIC TRUTH VALUES

def is_subvertible(
    s                                               : str, 
    language                                        : typing.Callable = lambda _: True
)                                                   -> bool:
    """
    Args:
        - s: Any string.
        - language: function that when a word is inputted determines if the word belongs to a given language. 
    """
    return pivot_char(s) is not None and pivot_word(s, language) is not None


def is_invertible(
    s                                               : str,
    language                                        : typing.Callable = lambda _: True
)                                                   -> bool:
    """
    Args:
        - s: Any string.
        - language: function that when a word is inputted determines if the word belongs to a given language. 
    """
    return language(invert(s))


# EXTENSIONAL FUNCTIONS

def invertible_sentences(c: typing.List[str])       -> typing.List[str]:
    return [z for z in c if is_invertible(z)]


def subvertible_sentences(c: typing.List[str])      -> typing.List[str]:
    return [z for z in c if is_subvertible(z)]


def palindromes(c: typing.List[str])                -> typing.List[str]:
    return [z for z in c if is_palindrome(z)]
