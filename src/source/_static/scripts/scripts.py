import nltk
import string
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize
import multiprocessing

nltk.download('brown')
nltk.download('punkt')

def calculate_coefficients(sentence):
    """
    Calculates the coefficients (2i - l(ζ) - 1) for each delimiter in a sentence.

    Args:
        sentence: The input sentence (string).

    Returns:
        A list of coefficients, one for each delimiter in the sentence.
    """
    l = len(sentence)
    coefficients = []
    for i in range(1, l + 1):
        if sentence[i - 1] == ' ':  # Assuming space as the delimiter
            coefficients.append(2 * i - l - 1)
    return coefficients

def process_sentences(corpus, sentence_length):
    """
    Processes a corpus of sentences, filters for sentences of a specific length,
    and calculates the coefficients for each sentence.

    Args:
        corpus: A list of sentences (strings).
        sentence_length: The desired sentence length.

    Returns:
        A list of lists, where each inner list contains the coefficients for a single sentence.
    """
    all_coefficients = []
    for sentence in corpus:
        if len(sentence) == sentence_length:
            coefficients = calculate_coefficients(sentence)
            all_coefficients.append(coefficients)
    return all_coefficients

def clean_and_filter_sentences(corpus):
    """
    Cleans and filters sentences from a corpus based on length and punctuation.

    Args:
        corpus: The NLTK corpus object (e.g., brown).
        min_length: The minimum sentence length (in characters).
        max_length: The maximum sentence length (in characters).

    Returns:
        A list of cleaned sentences (strings).
    """
    # Get all sentences from the corpus
    all_sentences = corpus.sents()

    # Flatten the list of lists into a single list of sentences
    flattened_sentences = [" ".join(sentence) for sentence in all_sentences]

    # Tokenize the flattened sentences into individual sentences
    tokenized_sentences = []
    for text in flattened_sentences:
        tokenized_sentences.extend(sent_tokenize(text))

    return tokenized_sentences

def is_palindrome(sentence):
    """
    Checks if a sentence is a palindrome based on our formal definition.

    Args:
        sentence: The input sentence (string).

    Returns:
        True if the sentence is a palindrome, False otherwise.
    """
    processed_sentence = "".join(c for c in sentence if c not in string.punctuation or c == ' ')
    processed_sentence = " ".join(processed_sentence.split()).lower()
    
    
    sigma_reduced_sentence = "".join(c for c in processed_sentence if c != ' ')

    return sigma_reduced_sentence == sigma_reduced_sentence[::-1]

def filter_palindromes(sentences):
    """
    Filters a list of sentences to find palindromes.

    Args:
        sentences: A list of sentences (strings).

    Returns:
        A list of palindromes (strings).
    """
    
    with multiprocessing.Pool() as pool:
        palindromes = pool.map(is_palindrome, sentences)

    return [s for s, is_p in zip(sentences, palindromes) if is_p]

# Example Usage (using the cleaned_sentences from before):
min_length = 10  # Minimum sentence length
max_length = 500  # Maximum sentence length (adjust as needed)

cleaned_sentences = clean_and_filter_sentences(brown)
palindromes = filter_palindromes(cleaned_sentences)

print(f"Found {len(palindromes)} palindromes in the Brown Corpus.")
for palindrome in palindromes:
    print(palindrome)

# Generate and display the histogram
# generate_histogram(all_coefficients, sentence_length)



# import json
# # Example Usage:
# result = {}
# for chars in [ 10, 30, 100, 200, 300 ]:
#     left_integrals, right_integrals = analyze_sentence_integrals(brown, chars)

#     # Assuming you have lists 'left_integrals' and 'right_integrals' from the previous analysis
#     left_stats = calculate_statistics(left_integrals)
#     right_stats = calculate_statistics(right_integrals)
#     result[f'n=${chars}'] = {
#         "left": left_stats,
#         "right": right_stats
#     }

# with open("stats.json", "w") as outfile: 
#     json.dump(result, outfile)

# Example usage:
# min_length = 100  # Minimum sentence length
# max_length = 100 # Maximum sentence length (adjust as needed)

# cleaned_sentences = clean_and_filter_sentences(brown, min_length, max_length)

# print(f"Found {len(cleaned_sentences)} sentences between {min_length} and {max_length} characters.")

# Now you can use the cleaned_sentences list with your coefficient calculation functions:
# all_coefficients = process_sentences(cleaned_sentences, max_length)  # Adjust sentence_length as needed
# generate_histogram(all_coefficients, max_length)