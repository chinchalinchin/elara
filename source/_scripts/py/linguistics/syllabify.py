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
    Uses lookarounds to prevent overlapping match failures, 
    handles complex consonant clusters, and separates vowel hiatus.
    """
    # Standard IPA vowels commonly produced by eng_to_ipa
    vowels = r'ɑæəɛɪiɔʊuʌaeo'
    
    # 1. Stress marks denote the onset of a syllable. Add a dot before them.
    res = re.sub(r'(.)([ˈˌ])', r'\1.\2', ipa_text)
    
    # 2. VCCCCV -> VC.CCCV (e.g., in.struct -> n.str)
    res = re.sub(f'(?<=[{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])(?=[{vowels}])', r'\1.\2\3\4', res)

    # 3. VCCCV -> VC.CCV (e.g., e.lec.tric -> k.tr)
    res = re.sub(f'(?<=[{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])(?=[{vowels}])', r'\1.\2\3', res)

    # 4. Complex Onsets (V.CCV)
    # Catch indivisible consonant clusters FIRST and place the dot before them.
    complex_onsets = r'(kw|tw|dw|gw|tr|dr|pr|br|kr|gr|fr|θr|ʃr|pl|bl|kl|gl|fl|sl|st|sp|sk|sm|sn)'
    res = re.sub(f'(?<=[{vowels}])({complex_onsets})(?=[{vowels}])', r'.\1', res)

    # 5. Standard VCCV -> VC.CV 
    res = re.sub(f'(?<=[{vowels}])([^.ˈˌ{vowels}])([^.ˈˌ{vowels}])(?=[{vowels}])', r'\1.\2', res)
    
    # 6. Standard VCV -> V.CV 
    res = re.sub(f'(?<=[{vowels}])([^.ˈˌ{vowels}])(?=[{vowels}])', r'.\1', res)
    
    # 7. VV -> V.V (Vowel hiatus, e.g., me.di.um -> i.ə)
    # Insert a dot between ANY two adjacent vowels...
    res = re.sub(f'(?<=[{vowels}])(?=[{vowels}])', '.', res)
    
    # ...and then immediately remove the dot from standard English diphthongs 
    # so we don't accidentally split a single syllable.
    diphthongs = ['a.ɪ', 'a.ʊ', 'e.ɪ', 'o.ʊ', 'ɔ.ɪ']
    for d in diphthongs:
        res = res.replace(d, d.replace('.', ''))
    
    # 8. Clean up any accidental double dots or leading/trailing dots
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