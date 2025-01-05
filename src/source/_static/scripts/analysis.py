import multiprocessing
import nltk
import string
import matplotlib.pyplot as plt
from nltk.corpus import brown, cess_esp
from nltk.tokenize import sent_tokenize
import statistics
import scipy.stats
import json

# Download necessary NLTK data if you haven't already
nltk.download('brown')
nltk.download('cess_esp')
nltk.download('punkt')

def get_corpus_sentences(language, min_length, max_length):
    """
    Loads and preprocesses sentences from a specified corpus.

    Args:
        language: Either "english" or "spanish".
        min_length: The minimum sentence length (in characters).
        max_length: The maximum sentence length (in characters).

    Returns:
        A list of cleaned sentences (strings) from the specified corpus.
    """

    if language == "english":
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


    elif language == "spanish":
        corpus = cess_esp.sents()
        cleaned_sentences = []
        for sentence in corpus:
            cleaned_sentence = " ".join(word for word in sentence if word not in string.punctuation and word not in "¡¿")
            cleaned_sentence = " ".join(cleaned_sentence.split()).lower()
            if min_length <= len(cleaned_sentence) <= max_length:
                cleaned_sentences.append(cleaned_sentence)
        return cleaned_sentences

    else:
        raise ValueError("Invalid language specified. Choose 'english' or 'spanish'.")

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

def delimiter_count(char):
    """
    Calculates the delimiter count of a single character.

    Args:
        char: The character to check.

    Returns:
        1 if the character is a delimiter (space), 0 otherwise.
    """
    return 1 if char == ' ' else 0

def calculate_left_integral(sentence, k):
    """
    Calculates the Left-Hand Sentence Integral of a sentence up to index k.

    Args:
        sentence: The input sentence (string).
        k: The upper limit of the summation (natural number).

    Returns:
        The Left-Hand Sentence Integral (float).
    """
    l = len(sentence)
    total = 0
    for i in range(1, min(k + 1, l + 1)):
        total += delimiter_count(sentence[i - 1]) * (i / l)
    return total

def calculate_right_integral(sentence, k):
    """
    Calculates the Right-Hand Sentence Integral of a sentence up to index k.

    Args:
        sentence: The input sentence (string).
        k: The upper limit of the summation (natural number).

    Returns:
        The Right-Hand Sentence Integral (float).
    """
    l = len(sentence)
    total = 0
    for i in range(1, min(k + 1, l + 1)):
        total += delimiter_count(sentence[i - 1]) * ((l - i + 1) / l)
    return total

def is_palindrome(sentence):
    """
    Checks if a sentence is a palindrome based on our formal definition.

    Args:
        sentence: The input sentence (string).

    Returns:
        True if the sentence is a palindrome, False otherwise.
    """
    # Remove punctuation (except spaces) and convert to lowercase
    processed_sentence = "".join(
        c for c in sentence if c not in string.punctuation or c == " "
    )
    processed_sentence = " ".join(processed_sentence.split()).lower()

    # Calculate the sigma-reduction (remove spaces)
    sigma_reduced_sentence = "".join(c for c in processed_sentence if c != " ")

    # Check if the sigma-reduced sentence is its own inverse
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
        palindrome_flags = pool.map(is_palindrome, sentences)

    return [s for s, is_p in zip(sentences, palindrome_flags) if is_p]

def calculate_statistics(data):
    """
    Calculates descriptive statistics for a given dataset.

    Args:
        data: A list of numerical data.

    Returns:
        A dictionary containing the statistics.
    """
    if not data:
        return {
            "number of samples": 0,
            "mean": None,
            "median": None,
            "stdev": None,
            "skewness": None,
            "min": None,
            "max": None,
            "mode": None
        }

    try:
        mode = statistics.mode(data)
    except statistics.StatisticsError:
        mode = None  # Handle cases with no unique mode

    stats = {
        "number of samples": len(data),
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "min": min(data),
        "max": max(data),
        "mode": mode,
    }

    if len(data) > 1:
        stats["stdev"] = statistics.stdev(data)
        stats["skewness"] = scipy.stats.skew(data, bias=False)  # Using Pearson's moment coefficient of skewness
    else:
        stats["stdev"] = None
        stats["skewness"] = None

    return stats

def analyze_integrals_by_length(sentences, min_length, max_length):
    """
    Iterates over sentence lengths, analyzes Sentence Integrals, and calculates delimiter densities.

    Args:
        sentences: The list of sentences.
        min_length: The minimum sentence length to analyze.
        max_length: The maximum sentence length to analyze.

    Returns:
        A dictionary containing the statistics for each sentence length and a list of delimiter densities.
    """
    all_stats = {}
    delimiter_densities = []

    for length in range(min_length, max_length + 1):
        left_integrals, right_integrals = analyze_sentence_integrals(sentences, length)

        if not left_integrals:
            continue

        left_stats = calculate_statistics(left_integrals)
        right_stats = calculate_statistics(right_integrals)

        all_stats[f"n={length}"] = {
            "left": left_stats,
            "right": right_stats,
        }

        # Calculate delimiter densities based on mean integral values
        d_left = calculate_delimiter_density(left_stats["mean"], length)
        d_right = calculate_delimiter_density(right_stats["mean"], length)

        delimiter_densities.append((length, d_left, d_right))

    # Calculate statistics for delimiter densities

    delimiter_density_stats = {
        "mean": statistics.mean([d_pair[1] for d_pair in delimiter_densities])
    }
    if len(delimiter_densities) > 1:
        delimiter_density_stats["stdev"] = statistics.stdev([d_pair[1] for d_pair in delimiter_densities])
    else:
        delimiter_density_stats["stdev"] = 0

    return all_stats, delimiter_densities, delimiter_density_stats

def analyze_sentence_integrals(sentences, sentence_length):
    """
    Analyzes the Left and Right-Hand Sentence Integrals of sentences in a corpus.

    Args:
        sentences: The list of sentences.
        sentence_length: The desired sentence length.

    Returns:
        A tuple containing two lists:
        - left_integrals: A list of Left-Hand Sentence Integrals.
        - right_integrals: A list of Right-Hand Sentence Integrals.
    """
    left_integrals = []
    right_integrals = []

    for sentence in sentences:
        if len(sentence) == sentence_length:
            left_integrals.append(calculate_left_integral(sentence, sentence_length))
            right_integrals.append(calculate_right_integral(sentence, sentence_length))

    return left_integrals, right_integrals

def calculate_delimiter_density(mean_integral_value, sentence_length):
    """
    Calculates the delimiter density (d) based on the mean Sentence Integral value and sentence length.

    Args:
        mean_integral_value: The mean value of the Sentence Integral (either Left or Right).
        sentence_length: The length of the sentences.

    Returns:
        The estimated delimiter density (d).
    """
    if sentence_length < 1:
        return None

    # From our approximation before: E[Ω:sub:`-`(ζ,l(ζ))] ≈ d * (l(ζ) + 1)/2
    # We also know that E[Ω:sub:`-`(ζ,l(ζ))] ≈ mean_integral_value

    d = (2 * mean_integral_value) / (sentence_length + 1)
    return d

def generate_integral_histograms(left_integrals, right_integrals, sentence_length, num_bins=20):
    """
    Generates histograms for the Left and Right-Hand Sentence Integrals.

    Args:
        left_integrals: A list of Left-Hand Sentence Integrals.
        right_integrals: A list of Right-Hand Sentence Integrals.
        sentence_length: The length of the sentences analyzed.
        num_bins: The number of bins for the histograms.
    """

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(left_integrals, bins=num_bins, range=(0, 10))
    plt.title(f"Left-Hand Integrals (Length = {sentence_length})")
    plt.xlabel("Integral Value")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.hist(right_integrals, bins=num_bins, range=(0, 10))
    plt.title(f"Right-Hand Integrals (Length = {sentence_length})")
    plt.xlabel("Integral Value")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

def generate_coefficient_histogram(all_coefficients, sentence_length):
    """
    Generates a histogram of the delimiter coefficients.

    Args:
        all_coefficients: A list of lists, where each inner list contains the coefficients for a sentence.
        sentence_length: The length of the sentences analyzed.
    """
    # Flatten the list of lists into a single list
    flat_coefficients = [item for sublist in all_coefficients for item in sublist]

    plt.hist(flat_coefficients, bins=range(-sentence_length + 1, sentence_length, 2)) # Bins for odd/even coefficients
    plt.title(f"Delimiter Coefficient Distribution (Sentence Length = {sentence_length})")
    plt.xlabel("Coefficient (2i - l(ζ) - 1)")
    plt.ylabel("Frequency")
    plt.show()
    
# Example Usage:
min_length = 2
max_length = 200

test_palindrome = "no devil lived on"
result = is_palindrome(test_palindrome)
print(f"'{test_palindrome}' is a palindrome: {result}")

# # Load sentences of the appropriate language
# cleaned_sentences = get_corpus_sentences("english", min_length, max_length)

# # Filter for palindromes
# palindrome_sentences = filter_palindromes(cleaned_sentences)

# print(palindrome_sentences)

# # Now you can use the cleaned_sentences list with your analysis functions:
# all_stats, delimiter_densities, delimiter_density_stats = analyze_integrals_by_length(
#     palindrome_sentences, min_length, max_length
# )

# # Save results to JSON files (Optional)
# with open("palindrome_all_stats.json", "w") as outfile:
#     json.dump(all_stats, outfile)

# with open("palindrome_delimiter_densities.json", "w") as outfile:
#     json.dump(delimiter_densities, outfile)

# with open("palindrome_delimiter_density_stats.json", "w") as outfile:
#     json.dump(delimiter_density_stats, outfile)

# # Print the statistics for each sentence length
# for length, stats in all_stats.items():
#     print(f"Sentence Length: {length}")
#     print("  Left-Hand Integral Stats:", stats["left"])
#     print("  Right-Hand Integral Stats:", stats["right"])
#     print("-" * 20)

# # Print the delimiter densities
# print("\nDelimiter Densities:")
# for length, d_left, d_right in delimiter_densities:
#     print(f"Length: {length}, Left d: {d_left:.4f}, Right d: {d_right:.4f}")

# # Print overall delimiter density statistics
# print("\nDelimiter Density Statistics:")
# print(delimiter_density_stats)