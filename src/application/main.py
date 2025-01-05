import json
import multiprocessing

import estimators
import parse
import graphs
import model

def write(data, file_name):
    with open(file_name, "w") as outfile:
        json.dump(data, outfile)

def filter_palindromes(sentences):
    """
    Filters a list of sentences to find palindromes.

    Args:
        sentences: A list of sentences (strings).

    Returns:
        A list of palindromes (strings).
    """

    with multiprocessing.Pool() as pool:
        palindrome_flags = pool.map(model.is_palindrome, sentences)

    return [s for s, is_p in zip(sentences, palindrome_flags) if is_p]

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
        left_integrals, right_integrals = model.sentence_integrals(sentences, length)

        if not left_integrals or not right_integrals:
            continue

        left_stats = estimators.summarize(left_integrals)
        right_stats = estimators.summarize(right_integrals)

        # Calculate delimiter densities based on mean integral values
        d_left = model.delimiter_density(left_stats["mean"], length)
        d_right = model.delimiter_density(right_stats["mean"], length)

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
        sentences = parse.corpus(language, min_length, max_length)
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

            t_left, p_left = estimators.difference_of_means_test(data1["left"], 
                                                        data1["stdev(left)"], 
                                                        data1["n"], 
                                                        data2["left"], 
                                                        data2["stdev(left)"], 
                                                        data2["n"])
            t_right, p_right = estimators.difference_of_means_test(data1["right"], 
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

def analyze_sentence_lengths(min_length, max_length):
    """
    Analyzes sentence lengths for English, Spanish, and Hindi corpora.

    Args:
        min_length: The minimum sentence length to analyze.
        max_length: The maximum sentence length to analyze.

    Returns:
        A dictionary containing the length frequencies and mean lengths for each corpus.
    """
    corpora = [parse.CORPORA.ENGLISH, parse.CORPORA.SPANISH, parse.CORPORA.HINDI]
    results = {}

    for corpus in corpora:
        sentences = parse.get_corpus_sentences(corpus, min_length, max_length)
        length_freq = parse.length_frequencies(sentences)
        mean_length = parse.sample_mean_freq(length_freq)
        graphs.generate_length_histogram(length_freq, mean_length)
        results[corpus.value] = {
            "length_frequencies": length_freq,
            "mean_length": mean_length,
        }

    return results

if __name__ == "__main__":

    parse.init()

    min_length = 50
    max_length = 150

    length_analysis_results = analyze_sentence_lengths(min_length, max_length)
    print(length_analysis_results)
