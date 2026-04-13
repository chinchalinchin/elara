#!/usr/bin/env python3

import argparse
import pronouncing

def get_rhyming_words(target_word, target_syllables):
    """
    Finds rhyming words for a target word and filters them by syllable count.
    """
    # Fetch all rhymes for the given word
    rhymes = pronouncing.rhymes(target_word)
    
    filtered_rhymes = []
    for word in rhymes:
        # Get the pronunciation phonemes for the rhyming word
        phones = pronouncing.phones_for_word(word)
        if phones:
            # Use the first common pronunciation to count syllables
            syllable_count = pronouncing.syllable_count(phones[0])
            if syllable_count == target_syllables:
                filtered_rhymes.append(word)
                
    # Return a deduplicated, sorted list
    return sorted(list(set(filtered_rhymes)))


def main():
    # Set up the CLI parser
    parser = argparse.ArgumentParser(
        description="A CLI tool to find rhyming words filtered by syllable count."
    )
    
    # Positional argument for the target text/word
    parser.add_argument(
        "word", 
        type=str, 
        help="The target word to rhyme with."
    )
    
    # Optional argument for syllables, allowing both --syllable and --syllables
    parser.add_argument(
        "--syllable", "--syllables", 
        type=int, 
        default=1, 
        dest="syllables",
        help="Number of syllables the rhymed words should have (default: 1)."
    )
    
    args = parser.parse_args()
    
    # Execute the search
    rhymes = get_rhyming_words(args.word, args.syllables)
    
    # Format and print the output
    if rhymes:
        print(", ".join(rhymes))
    else:
        print(f"No {args.syllables}-syllable rhymes found for '{args.word}'.")


if __name__ == "__main__":
    main()