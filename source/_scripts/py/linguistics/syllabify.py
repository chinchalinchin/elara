#!/usr/bin/env python3
import argparse
import sys
import re

try:
    import eng_to_ipa as ipa
except ImportError:
    print("Error: The 'eng_to_ipa' module is not installed.")
    print("Please install it running: pip install eng-to-ipa")
    sys.exit(1)

def add_syllable_dots(ipa_text):
    """
    A heuristic function to approximate phonetic syllabification.
    It uses a simplified Maximum Onset Principle and stress markers.
    """
    # Standard IPA vowels commonly produced by eng_to_ipa
    vowels = r'ɑæəɛɪiɔʊuʌaeo'
    
    # 1. Stress marks denote the onset of a syllable. Add a dot before them.
    res = re.sub(r'(.)([ˈˌ])', r'\1.\2', ipa_text)
    
    # 2. VCV -> V.CV (Push a single consonant to the right syllable)
    res = re.sub(f'([{vowels}])([^.ˈˌ{vowels}])([{vowels}])', r'\1.\2\3', res)
    
    # 3. VCCV -> VC.CV (Split between two consonants)
    res = re.sub(f'([{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])([{vowels}])', r'\1\2.\3\4', res)
    
    # 4. Clean up any accidental double dots or leading/trailing dots
    res = re.sub(r'\.+', '.', res).strip('.')
    
    return res

def analyze_phonetics(input_string, pretty=False):
    words = input_string.split()
    
    if pretty:
        print(f"{'WORD':<20} | {'IPA TRANSCRIPTION':<25} | {'SYLLABLES'}")
        print("-" * 60)
        
    ipa_results = []
    
    for word in words:
        clean_word = word.strip(".,!?\"'()[]{}")
        if not clean_word:
            continue
            
        # Fetch raw IPA
        raw_ipa = ipa.convert(clean_word)
        
        # Inject syllable boundaries
        syllabified_ipa = add_syllable_dots(raw_ipa)
        
        # Fetch syllable count
        syllables = ipa.syllable_count(clean_word)
        
        if pretty:
            print(f"{clean_word:<20} | {syllabified_ipa:<25} | {syllables}")
        else:
            ipa_results.append(syllabified_ipa)
            
    # Default behavior: Just output the space-separated IPA transcript
    if not pretty and ipa_results:
        print(" ".join(ipa_results))

def main():
    parser = argparse.ArgumentParser(
        description="A CLI tool to break down a string into its IPA transcription with apparent syllable boundaries."
    )
    parser.add_argument(
        "text", 
        type=str, 
        help="The text string you want to analyze. Enclose in quotes."
    )
    parser.add_argument(
        "--pretty", 
        action="store_true", 
        help="Format the output as a detailed table with syllable counts."
    )
    
    args = parser.parse_args()
    analyze_phonetics(args.text, args.pretty)

if __name__ == "__main__":
    main()