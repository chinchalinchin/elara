""" palindromes.parse: Module for parsing external data sources
"""
import enum
import nltk
from nltk.corpus import brown, cess_esp, indian
from nltk.tokenize import sent_tokenize
import string

class CORPORA(enum.Enum):
    ENGLISH = "english"
    SPANISH = "spanish"
    HINDI = "hindi"

def init():
    # Download necessary NLTK data if you haven't already
    nltk.download('brown')
    nltk.download('cess_esp')
    nltk.download('punkt')
    nltk.download('indian')

def _clean_corpus(language, min_length, max_length):
    # Updated to use the CORPORA enum

    if language == CORPORA.ENGLISH:
        corpus = brown
        all_sentences = corpus.sents()
        flattened_sentences = [" ".join(sentence) for sentence in all_sentences]
        tokenized_sentences = []
        for text in flattened_sentences:
            tokenized_sentences.extend(sent_tokenize(text))

        cleaned_sentences = []
        for sentence in tokenized_sentences:
            cleaned_sentence = "".join(
                c for c in sentence if c not in string.punctuation or c == ' '
            )
            cleaned_sentence = " ".join(cleaned_sentence.split()).lower()
            if min_length <= len(cleaned_sentence) <= max_length:
                cleaned_sentences.append(cleaned_sentence)
        return cleaned_sentences

    elif language == CORPORA.SPANISH:
        corpus = cess_esp.sents()
        cleaned_sentences = []
        for sentence in corpus:
            cleaned_sentence = " ".join(word for word in sentence if word not in string.punctuation and word not in "¡¿")
            cleaned_sentence = " ".join(cleaned_sentence.split()).lower()
            if min_length <= len(cleaned_sentence) <= max_length:
                cleaned_sentences.append(cleaned_sentence)
        return cleaned_sentences

    elif language == CORPORA.HINDI:
        corpus = indian
        cleaned_sentences = []
        words = corpus.words('hindi.pos')
        
        # Build sentences based on full stop delimiter ('।')
        sentence = ""
        for word in words:
          if word == '।':
            if min_length <= len(sentence) <= max_length:
              cleaned_sentences.append(sentence.strip())
            sentence = ""
          else:
            if len(sentence) > 0:
              sentence += " "
            sentence += word
        
        # Add the last sentence if it meets the length criteria
        if len(sentence) > 0 and min_length <= len(sentence) <= max_length:
          cleaned_sentences.append(sentence.strip())

        return cleaned_sentences

    else:
        raise ValueError("Invalid language specified. Choose from 'english', 'spanish', or 'hindi'.")

def _english_corpus(min_length, max_length):
    # Updated to use the new corpus function
    return _clean_corpus(CORPORA.ENGLISH, min_length, max_length)

def _spanish_corpus(min_length, max_length):
    # Updated to use the new corpus function
    return _clean_corpus(CORPORA.SPANISH, min_length, max_length)

def _hindi_corpus(min_length, max_length):
    # Updated to use the new corpus function
    return _clean_corpus(CORPORA.HINDI, min_length, max_length)

def corpus(min_length = 100, max_length = 200, language = CORPORA.ENGLISH):
    if language == CORPORA.HINDI:
        return _hindi_corpus(min_length, max_length)
    if language == CORPORA.SPANISH:
        return _spanish_corpus(min_length, max_length)
    return _english_corpus(min_length, max_length)