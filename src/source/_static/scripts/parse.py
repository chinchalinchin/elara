import nltk
from nltk.corpus import brown, cess_esp, indian
from nltk.tokenize import sent_tokenize
import string

def init():
    # Download necessary NLTK data if you haven't already
    nltk.download('brown')
    nltk.download('cess_esp')
    nltk.download('punkt')
    nltk.download('indian')

def clean_and_filter_hindi_bengali(min_length, max_length, language):
    """
    Cleans and filters sentences from the Indian language corpus based on length.

    Args:
        min_length: The minimum sentence length (in characters).
        max_length: The maximum sentence length (in characters).
        language: The language to extract sentences for, either "hindi" or "bengali"

    Returns:
        A list of cleaned sentences (strings).
    """
    corpus = indian
    cleaned_sentences = []
    words = corpus.words(language + '.pos')
    
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

def clean_and_filter_spanish(min_length, max_length):
    """
    Cleans and filters sentences from the Spanish language corpus based on length.

    Args:
        min_length: The minimum sentence length (in characters).
        max_length: The maximum sentence length (in characters).

    Returns:
        A list of cleaned sentences (strings).
    """
    corpus = cess_esp.sents()
    cleaned_sentences = []
    for sentence in corpus:
        cleaned_sentence = " ".join(word for word in sentence if word not in string.punctuation and word not in "¡¿")
        cleaned_sentence = " ".join(cleaned_sentence.split()).lower()
        if min_length <= len(cleaned_sentence) <= max_length:
            cleaned_sentences.append(cleaned_sentence)
    return cleaned_sentences

def clean_and_filter_english(min_length, max_length):
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