#!/usr/bin/env python3

import argparse
import sys
import re
import os

# Prepend the current directory to sys.path to allow importing from poetics.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import eng_to_ipa as ipa
except ImportError:
    print("Error: The 'eng_to_ipa' module is not installed.")
    print("Please install it running: pip install eng-to-ipa")
    sys.exit(1)

try:
    import nltk
    from nltk.corpus import cmudict
    # Import existing logic from poetics.py to reduce logical complexity
    from poetics import syllabify, format_syllable_ipa
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Ensure 'poetics.py' is in the same directory and nltk is installed.")
    sys.exit(1)

# Ensure the CMU dictionary is downloaded quietly
try:
    nltk.data.find('corpora/cmudict')
except LookupError:
    nltk.download('cmudict', quiet=True)

def add_syllable_dots(ipa_text):
    """
    A heuristic function to approximate phonetic syllabification.
    Used as a fallback for words not found in the CMU dictionary.
    """
    vowels = r'ɑæəɛɪiɔʊuʌaeo'
    
    # 1. Stress marks denote the onset of a syllable. Add a dot before them.
    res = re.sub(r'(.)([ˈˌ])', r'\1.\2', ipa_text)
    
    # 2. VCCCCV -> VC.CCCV (e.g., in.struct -> n.str)
    res = re.sub(f'(?<=[{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])(?=[{vowels}])', r'\1.\2\3\4', res)

    # 3. VCCCV -> VC.CCV (e.g., e.lec.tric -> k.tr)
    res = re.sub(f'(?<=[{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])(?=[{vowels}])', r'\1.\2\3', res)

    # 4. Complex Onsets (V.CCV)
    complex_onsets = r'(kw|tw|dw|gw|tr|dr|pr|br|kr|gr|fr|θr|ʃr|pl|bl|kl|gl|fl|sl|st|sp|sk|sm|sn)'
    res = re.sub(f'(?<=[{vowels}])({complex_onsets})(?=[{vowels}])', r'.\1', res)

    # 5. Standard VCCV -> VC.CV 
    res = re.sub(f'(?<=[{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])(?=[{vowels}])', r'\1.\2', res)
    
    # 6. Standard VCV -> V.CV 
    res = re.sub(f'(?<=[{vowels}])([^.ˈˌ{vowels}])(?=[{vowels}])', r'.\1', res)
    
    # 7. VV -> V.V (Vowel hiatus)
    res = re.sub(f'(?<=[{vowels}])(?=[{vowels}])', '.', res)
    
    # Remove dots from standard English diphthongs
    diphthongs = ['a.ɪ', 'a.ʊ', 'e.ɪ', 'o.ʊ', 'ɔ.ɪ']
    for d in diphthongs:
        res = res.replace(d, d.replace('.', ''))
    
    # 8. Clean up any accidental double dots or leading/trailing dots
    res = re.sub(r'\.+', '.', res).strip('.')
    
    return res

def analyze_phonetics(input_string, pretty=False):
    words = input_string.split()
    cmu = cmudict.dict()
    
    if pretty:
        print(f"{'WORD':<20} | {'IPA TRANSCRIPTION':<35} | {'SYLLABLES'}")
        print("-" * 70)
        
    ipa_results = []
    
    for word in words:
        clean_word = word.strip(".,!?\"'()[]{}").lower()
        if not clean_word:
            continue
            
        # Attempt to use CMU Dict for superior stress accuracy and multiple pronunciations
        if clean_word in cmu:
            pronunciations = cmu[clean_word]
            word_ipas = []
            syllable_counts = []
            
            for pron in pronunciations:
                # Leverage the logic from poetics.py
                syllables_raw = syllabify(pron)
                syllable_counts.append(str(len(syllables_raw)))
                
                ipa_syllables = [format_syllable_ipa(s) for s in syllables_raw]
                word_ipas.append(".".join(ipa_syllables))
            
            # Deduplicate while preserving order
            unique_ipas = []
            for ipa_str in word_ipas:
                if ipa_str not in unique_ipas:
                    unique_ipas.append(ipa_str)
                    
            combined_ipa = ", ".join(unique_ipas)
            syllables = ", ".join(sorted(list(set(syllable_counts))))
            
        else:
            # Fallback to eng_to_ipa heuristic if not in CMU Dict
            raw_ipa = ipa.convert(clean_word)
            combined_ipa = add_syllable_dots(raw_ipa)
            syllables = str(ipa.syllable_count(clean_word))
        
        if pretty:
            print(f"{clean_word:<20} | {combined_ipa:<35} | {syllables}")
        else:
            ipa_results.append(combined_ipa)
            
    if not pretty and ipa_results:
        # If parsing multiple words, separate word blocks by a pipe to avoid comma confusion 
        print(" | ".join(ipa_results) if len(words) > 1 else ipa_results[0])

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