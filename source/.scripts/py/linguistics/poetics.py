#!/usr/bin/env python3

import csv
import os
import argparse
import nltk
from nltk.corpus import cmudict

# Download the dictionary if not already present
try:
    nltk.data.find('corpora/cmudict')
except LookupError:
    nltk.download('cmudict')

# Map CMU ARPAbet phonemes to broad IPA transcription
ARPABET_TO_IPA = {
    'AA': 'ɑ', 'AE': 'æ', 'AH': 'ə',
    'AO': 'ɔ', 'AW': 'aʊ', 'AY': 'aɪ', 'EH': 'ɛ', 'ER': 'ɚ',
    'EY': 'eɪ', 'IH': 'ɪ', 'IY': 'i', 'OW': 'oʊ', 'OY': 'ɔɪ',
    'UH': 'ʊ', 'UW': 'u',
    'P': 'p', 'B': 'b', 'T': 't', 'D': 'd', 'K': 'k', 'G': 'ɡ',
    'CH': 'tʃ', 'JH': 'dʒ', 'F': 'f', 'V': 'v', 'TH': 'θ', 'DH': 'ð',
    'S': 's', 'Z': 'z', 'SH': 'ʃ', 'ZH': 'ʒ', 'HH': 'h', 'M': 'm',
    'N': 'n', 'NG': 'ŋ', 'L': 'l', 'R': 'r', 'Y': 'j', 'W': 'w'
}

# Define the acceptable stress values for each position in a metrical foot.
# 0 = Unstressed, 1 = Primary Stress, 2 = Secondary Stress
METERS = {
    'iamb'      : [(0,), (1, 2)],
    'trochee'   : [(1, 2), (0,)],
    'dactyl'    : [(1, 2), (0,), (0,)],
    'anapest'   : [(0,), (0,), (1, 2)],
    'spondee'   : [(1, 2), (1, 2)]
}

def phoneme_to_ipa(phoneme):
    """Converts a single ARPAbet phoneme to IPA and extracts its stress level."""
    base = ''.join([c for c in phoneme if not c.isdigit()])
    stress = ''.join([c for c in phoneme if c.isdigit()])
    
    ipa_char = ARPABET_TO_IPA.get(base, base)
    
    # Adjust schwa and r-colored vowels based on stress
    if base == 'AH' and stress in ('1', '2'):
        ipa_char = 'ʌ'
    elif base == 'ER' and stress in ('1', '2'):
        ipa_char = 'ɝ'
        
    return ipa_char, stress

def syllabify(phonemes):
    """
    Groups phonemes into syllables using a medial-split approximation 
    for consonant clusters between vowels.
    """
    vowel_indices = [i for i, p in enumerate(phonemes) if p[-1].isdigit()]
    syllables = []
    start = 0
    
    for i in range(len(vowel_indices) - 1):
        v1_idx = vowel_indices[i]
        v2_idx = vowel_indices[i+1]
        
        num_consonants = v2_idx - v1_idx - 1
        coda_len = num_consonants // 2
        split_point = v1_idx + 1 + coda_len
        
        syllables.append(phonemes[start:split_point])
        start = split_point
        
    if vowel_indices:
        syllables.append(phonemes[start:])
    
    return syllables

def format_syllable_ipa(syllable_phonemes):
    """Translates a chunk of phonemes into an IPA string with stress markers."""
    ipa_str = ""
    stress_marker = ""
    
    for p in syllable_phonemes:
        ipa_char, stress = phoneme_to_ipa(p)
        ipa_str += ipa_char
        
        if stress == '1':
            stress_marker = 'ˈ'
        elif stress == '2':
            stress_marker = 'ˌ'
            
    return stress_marker + ipa_str

def get_stresses(pronunciation):
    """Extracts just the numeric stress pattern."""
    return [int(char) for p in pronunciation for char in p if char.isdigit()]

def matches_meter(stresses, meter_name):
    """Checks if the word's stresses exactly match repetitions of the chosen foot."""
    if not stresses:
        return False
        
    foot_pattern = METERS[meter_name]
    foot_length = len(foot_pattern)
    
    # The word must consist of complete metrical feet
    if len(stresses) % foot_length != 0:
        return False
        
    # Check each syllable against the expected stress mapping for its position in the foot
    for i, stress in enumerate(stresses):
        expected_stresses = foot_pattern[i % foot_length]
        if stress not in expected_stresses:
            return False
            
    return True

def generate_meter_csv(meter_name):
    cmu_dict = cmudict.dict()
    output_rows = []
    max_syllables = 0

    print(f"Scanning dictionary for strict {meter_name} patterns...")
    
    for word, pronunciations in cmu_dict.items():
        if not word.isalpha():
            continue
            
        for pron in pronunciations:
            stresses = get_stresses(pron)
            
            if matches_meter(stresses, meter_name):
                syllables_raw = syllabify(pron)
                ipa_syllables = [format_syllable_ipa(s) for s in syllables_raw]
                
                if len(ipa_syllables) > max_syllables:
                    max_syllables = len(ipa_syllables)
                
                output_rows.append([word.lower()] + ipa_syllables)
                break 

    output_rows.sort(key=lambda x: x[0])

    headers = ['word'] + [f'ipa_syl_{i+1}' for i in range(max_syllables)]
    
    output_filename = f'{meter_name}_words.csv'
    output_path = os.path.join(os.getcwd(), output_filename)
    
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(output_rows)
        
    print(f"Success! {len(output_rows)} {meter_name} words exported to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract words matching specific metrical patterns from the CMU Pronouncing Dictionary.")
    parser.add_argument(
        '--meter', 
        type=str, 
        choices=['iamb', 'trochee', 'dactyl', 'spondee', 'anapest'], 
        default='iamb',
        help="The metrical foot pattern to search for (default: iamb)."
    )
    
    args = parser.parse_args()
    generate_meter_csv(args.meter)