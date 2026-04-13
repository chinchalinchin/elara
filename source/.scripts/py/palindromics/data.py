""" palindromes.parse: Module for parsing external data sources
"""
import enum
import string
from typing import List, Callable

try:
    import nltk
    from nltk.corpus import brown, cess_esp, indian
    from nltk.tokenize import sent_tokenize
except ImportError:
    print("NLTK is not installed. Please install it using: pip install nltk")
    exit()



class CORPORA(enum.Enum):
    ENGLISH = "english"
    SPANISH = "spanish"
    HINDI = "hindi"


def init():
    nltk.download('brown')
    nltk.download('cess_esp')
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('indian')


def _english() -> List[str]:
    """Retrieves and performs initial cleaning on sentences from the Brown (English) corpus."""
    # The Brown corpus is a collection of texts. Flatten them into single strings
    # before tokenizing into sentences to handle sentence breaks across text boundaries.
    raw_text = " ".join(" ".join(sent) for sent in brown.sents())
    sentences = sent_tokenize(raw_text)
    
    # Remove standard punctuation.
    translator = str.maketrans('', '', string.punctuation)
    return [s.translate(translator) for s in sentences]


def _spanish() -> List[str]:
    """Retrieves and performs initial cleaning on sentences from the CESS-ESP (Spanish) corpus."""
    # Spanish-specific punctuation to remove.
    spanish_punctuation = string.punctuation + "¡¿"
    translator = str.maketrans('', '', spanish_punctuation)
    
    sentences = [" ".join(sent) for sent in cess_esp.sents()]
    return [s.translate(translator) for s in sentences]


def _hindi() -> List[str]:
    """Retrieves and reconstructs sentences from the Indian (Hindi) corpus."""
    sentences = []
    current_sentence = []
    # The Hindi corpus uses '।'-_ a 'purna viram' - as a sentence delimiter.
    for word in indian.words('hindi.pos'):
        if word == '।':
            if current_sentence:
                sentences.append(" ".join(current_sentence))
                current_sentence = []
        else:
            current_sentence.append(word)
    
    # Add the last sentence if the corpus doesn't end with a delimiter.
    if current_sentence:
        sentences.append(" ".join(current_sentence))
        
    return sentences


def _normalize(
    sentences: List[str], min_length: int, max_length: int
) -> List[str]:
    """
    Applies final normalization and length filtering to a list of sentences.
    
    - Converts to lowercase.
    - Removes extra whitespace.
    - Filters by character length.
    """
    cleaned_sentences = []
    for sentence in sentences:
        # Consolidate whitespace and convert to lowercase.
        normalized = " ".join(sentence.split()).lower()
        if min_length <= len(normalized) <= max_length:
            cleaned_sentences.append(normalized)
    return cleaned_sentences


# Function dispatch dictionaries

_CORPUS: dict[CORPORA, Callable[[], List[str]]] = {
    CORPORA.ENGLISH: _english,
    CORPORA.SPANISH: _spanish,
    CORPORA.HINDI: _hindi,
}

_LANGUAGE: dict[CORPORA, Callable[[], List[str]]] = {
    CORPORA.ENGLISH: lambda: brown.words(),
    CORPORA.SPANISH: lambda: cess_esp.words(),
    CORPORA.HINDI:   lambda: indian.words('hindi.pos'),
}


def corpus(
    language: CORPORA = CORPORA.ENGLISH, min_length: int = 100, max_length: int = 200
) -> List[str]:
    """
    Extracts and cleans sentences from a specified NLTK corpus.

    Args:
        language: The language corpus to use (from the CORPORA enum).
        min_length: The minimum character length for a sentence to be included.
        max_length: The maximum character length for a sentence to be included.

    Returns:
        A list of cleaned and filtered sentences.
        
    Raises:
        ValueError: If an unsupported language is specified.
    """
    if language not in _CORPUS:
        supported = ", ".join(f"'{lang.value}'" for lang in CORPORA)
        raise ValueError(f"Invalid language. Choose from: {supported}.")

    # 1. Get raw sentences using the language-specific getter.
    raw_sentences = _CORPUS[language]()
    
    # 2. Apply common normalization and filtering logic.
    return _normalize(raw_sentences, min_length, max_length)


def language(length: int, language: CORPORA = CORPORA.ENGLISH) -> List[str]:
    """
    Extracts alphabetical words of a specific length from a corpus.

    Args:
        length: The desired length of the words.
        language: The language corpus to use.

    Returns:
        A list of words matching the criteria.
        
    Raises:
        ValueError: If an unsupported language is specified.
    """
    if language not in _LANGUAGE:
        supported = ", ".join(f"'{lang.value}'" for lang in CORPORA)
        raise ValueError(f"Invalid language. Choose from: {supported}.")

    # 1. Get the raw word list using the dispatcher.
    word_list = _LANGUAGE[language]()
    
    # 2. Filter the list based on length and alphabetic characters.
    return [
        word.lower() 
        for word in word_list 
        if len(word) == length and word.isalpha()
    ]

init()