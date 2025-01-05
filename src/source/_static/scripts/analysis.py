import json
import multiprocessing
import math
import scipy.stats
import statistics
import string
from parse import init, \
        clean_and_filter_english, \
        clean_and_filter_hindi_bengali, \
        clean_and_filter_spanish

def write(data, file_name):
    with open(file_name, "w") as outfile:
        json.dump(data, outfile)

def summarize(data):
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

def difference_of_means_test(mean_1, stdev_1, n1, mean_2, stdev_2, n2):
    """
    Performs a two-sample t-test (difference of means test) assuming unequal variances.

    Args:
        mean_1: Mean of the first sample.
        stdev_1: Standard deviation of the first sample.
        n1: Number of observations in the first sample.
        mean_2: Mean of the second sample.
        stdev_2: Standard deviation of the second sample.
        n2: Number of observations in the second sample.

    Returns:
        A tuple containing the t-statistic and the p-value.
    """
    print("performing tests")
    if stdev_1 is None or stdev_2 is None or n1 < 2 or n2 < 2:
        return None, None

    # Calculate the t-statistic
    t_statistic = (mean_1 - mean_2) / math.sqrt((stdev_1**2 / n1) + (stdev_2**2 / n2))

    # Calculate the degrees of freedom using the Welch-Satterthwaite equation
    df = ((stdev_1**2 / n1) + (stdev_2**2 / n2))**2 / (
        (stdev_1**4) / (n1**2 * (n1 - 1)) + (stdev_2**4) / (n2**2 * (n2 - 1))
    )

    # Calculate the p-value (two-tailed test)
    p_value = 2 * (1 - scipy.stats.t.cdf(abs(t_statistic), df))

    return t_statistic, p_value

def corpus(language, min_length, max_length):
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
        return clean_and_filter_english(min_length, max_length)

    elif language == "spanish":
        return clean_and_filter_spanish(min_length, max_length)

    elif language == "hindi" or language == "bengali":
        return clean_and_filter_hindi_bengali(min_length, max_length, language)

    raise ValueError("Invalid language specified. Choose 'english', 'spanish', 'hindi', or 'bengali'.")

def invert(sentence):
    return sentence[::-1]

def sigma_reduce(sentence):
     # Remove punctuation (except spaces) and convert to lowercase
    processed_sentence = "".join(
        c for c in sentence if c not in string.punctuation or c == " "
    )
    processed_sentence = " ".join(processed_sentence.split()).lower()

    # Calculate the sigma-reduction (remove spaces)
    sigma_reduced_sentence = "".join(c for c in processed_sentence if c != " ")
    return sigma_reduced_sentence

def delimiter_count(char):
    """
    Calculates the delimiter count of a single character.

    Args:
        char: The character to check.

    Returns:
        1 if the character is a delimiter (space), 0 otherwise.
    """
    return 1 if char == ' ' else 0

def integral_coefficients(sentence):
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

def delimiter_density(mean_integral_value, sentence_length):
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

def integral_distribution(corpus, sentence_length):
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
            coefficients = integral_coefficients(sentence)
            all_coefficients.append(coefficients)
    return all_coefficients

def lefthand_integral(sentence, k):
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

def righthand_integral(sentence, k):
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

    sigma_sentence = sigma_reduce(sentence)
    inverse_sigma_sentence = invert(sigma_sentence)
    return sigma_sentence == inverse_sigma_sentence

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

def sentence_integrals(sentences, sentence_length):
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
            left_integrals.append(lefthand_integral(sentence, sentence_length))
            right_integrals.append(righthand_integral(sentence, sentence_length))

    return left_integrals, right_integrals

def analyze_delimiter_densities(sentences, min_length, max_length):
    """
    Iterates over sentence lengths, analyzes Sentence Integrals, and calculates delimiter densities.

    Args:
        sentences: The list of sentences.
        min_length: The minimum sentence length to analyze.
        max_length: The maximum sentence length to analyze.

    Returns:
        A dictionary containing the statistics for each sentence length and a list of delimiter densities.
    """
    delimiter_densities = []

    for length in range(min_length, max_length + 1):
        left_integrals, right_integrals = sentence_integrals(sentences, length)

        if not left_integrals or not right_integrals:
            continue

        left_stats = summarize(left_integrals)
        right_stats = summarize(right_integrals)

        # Calculate delimiter densities based on mean integral values
        d_left = delimiter_density(left_stats["mean"], length)
        d_right = delimiter_density(right_stats["mean"], length)

        delimiter_densities.append({
            "sentence_length": length,
            "n": left_stats["number of samples"],  # Assuming n is the same for both left and right
            "left": left_stats["mean"],
            "right": right_stats["mean"],
            "stdev(left)": left_stats["stdev"],
            "stdev(right)": right_stats["stdev"],
            "d_left": d_left,
            "d_right": d_right,
            "stdev(d_left)": None,  # Placeholder for now
            "stdev(d_right)": None,  # Placeholder for now
        })

    return delimiter_densities

def analyze_languages(min_length, max_length):
    """
    Analyzes delimiter densities for English, Spanish, and Hindi corpora.

    Args:
        min_length: The minimum sentence length to analyze.
        max_length: The maximum sentence length to analyze.

    Returns:
        A list of dictionaries, where each dictionary contains the results of the difference of means tests for a specific sentence length.
    """
    languages = ["english", "spanish", "hindi"]
    all_corpora_delimiter_data = {}

    for language in languages:
        sentences = corpus(language, min_length, max_length)
        all_corpora_delimiter_data[language] = analyze_delimiter_densities(sentences, 
                                                                           min_length, 
                                                                           max_length)

        print(sentences[:3])

    comparison_results = []
    for length in range(min_length, max_length + 1):
        
        # Check if data exists for all languages at this length
        if not all(any(d["sentence_length"] == length for d in all_corpora_delimiter_data[lang]) for lang in languages):
            continue

        english_data = all_corpora_delimiter_data["english"]
        spanish_data = all_corpora_delimiter_data["spanish"]
        hindi_data = all_corpora_delimiter_data["hindi"]

        # Find the data for the current length in each language
        english_stats = next((d for d in english_data if d["sentence_length"] == length), None)
        spanish_stats = next((d for d in spanish_data if d["sentence_length"] == length), None)
        hindi_stats = next((d for d in hindi_data if d["sentence_length"] == length), None)

        if not english_stats or not spanish_stats or not hindi_stats:
            continue
        
        result = {
            "sentence_length": length,
            "n": english_stats["n"], # Assuming n is the same across languages for a given length
            "comparisons": {}
        }

        # Perform comparisons and store results
        comparisons = [("spanish", "english"), ("spanish", "hindi"), ("hindi", "english")]
        for lang1, lang2 in comparisons:
            data1 = english_stats if lang1 == "english" else spanish_stats if lang1 == "spanish" else hindi_stats
            data2 = english_stats if lang2 == "english" else spanish_stats if lang2 == "spanish" else hindi_stats

            t_left, p_left = difference_of_means_test(data1["left"], 
                                                        data1["stdev(left)"], 
                                                        data1["n"], 
                                                        data2["left"], 
                                                        data2["stdev(left)"], 
                                                        data2["n"])
            t_right, p_right = difference_of_means_test(data1["right"], 
                                                        data1["stdev(right)"], 
                                                        data1["n"], 
                                                        data2["right"], 
                                                        data2["stdev(right)"], 
                                                        data2["n"])

            result["comparisons"][f"{lang1}-{lang2}"] = {
                "t_left": t_left,
                "p_left": p_left,
                "t_right": t_right,
                "p_right": p_right,
            }

        comparison_results.append(result)

    return comparison_results

if __name__ == "__main__":

    init()

    min_length = 50
    max_length = 150

    delimiter_densities= analyze_languages(min_length, max_length)
    
    write(delimiter_densities, 'language_delimiter_comparison.json')
