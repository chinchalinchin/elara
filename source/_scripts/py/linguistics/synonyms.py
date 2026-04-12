#!/usr/bin/env python3

import argparse
import sys
import nltk
from nltk.corpus import wordnet

# Ensure the required NLTK datasets are downloaded silently
def setup_nltk():
    try:
        nltk.data.find('corpora/wordnet.zip')
    except LookupError:
        nltk.download('wordnet', quiet=True)
    try:
        nltk.data.find('corpora/omw-1.4.zip')
    except LookupError:
        nltk.download('omw-1.4', quiet=True)

def get_synonyms(word):
    synonyms = set()
    # WordNet groups words into sets of cognitive synonyms called synsets
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            # Clean up multi-word synonyms by replacing underscores with spaces
            clean_word = lemma.name().replace('_', ' ')
            synonyms.add(clean_word)
    
    # Remove the exact original search term from the results
    if word.lower() in [s.lower() for s in synonyms]:
        synonyms.remove(word.lower())
        
    return sorted(list(synonyms))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find synonyms for a given word using NLTK.")
    parser.add_argument("word", type=str, help="The word you want to find synonyms for.")
    
    args = parser.parse_args()
    
    setup_nltk()
    results = get_synonyms(args.word)
    
    if results:
        print(f"Synonyms for '{args.word}':")
        for synonym in results:
            print(f"  - {synonym}")
    else:
        print(f"No synonyms found in WordNet for '{args.word}'.")
        sys.exit(1)