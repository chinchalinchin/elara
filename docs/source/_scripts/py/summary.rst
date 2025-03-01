.. _summary:

Summary
#######

.. _palindromes-directory-report:

===========
palindromes
===========

.. _directory-structure:

Structure
=========

The following block shows the directory structure of the files given in the :ref:`directory-files` section.

.. code-block:: bash

    __init__.py
    estimators.py
    graphs.py
    main.py
    model.py
    parse.py

.. _directory-files:

Files
=====

.. note::

    Some of the files may have been excluded from the summary to conserve space.

.. _estimators:
 
-------------
estimators.py
-------------

.. code-block:: python

    """ palindrome.estimators: Module for statistical analysis.
    """
    import math
    import statistics
    import numpy as np
    import scipy.stats
    from scipy.special import comb
    
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
    
    def sample_mean_freq(data_dict):
        """
        Calculates the sample mean of a dictionary, weighted by the values.
    
        Args:
            data_dict: A dictionary where keys are data points and values are their frequencies.
    
        Returns:
            The weighted sample mean.
        """
        
        total_sum = sum(key * value for key, value in data_dict.items())
        total_count = sum(value for value in data_dict.values())
    
        if total_count == 0:
            return None  # Handle the case of an empty dictionary
    
        return total_sum / total_count
    
    def length_frequencies(corpus):
        """
        Calculates the frequency of each sentence length in a corpus.
    
        Args:
            corpus: A list of sentences (strings).
    
        Returns:
            A dictionary where keys are sentence lengths and values are their frequencies.
        """
        freq_dict = {}
        for sentence in corpus:
            length = len(sentence)
            freq_dict[length] = freq_dict.get(length, 0) + 1
        return freq_dict
    
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
    
    def uniform_prior(num_points=1000):
        """
        Creates a uniform prior distribution for the delimiter probability p.
    
        Args:
            num_points: The number of points to use for discretization.
    
        Returns:
            A tuple of two arrays:
            - x: The values of p (from 0 to 1).
            - prior: The corresponding prior probabilities for each value of p.
        """
        x = np.linspace(0, 1, num_points)
        prior = np.ones_like(x) / num_points  # Uniform distribution
        return x, prior
    
    def beta_prior(alpha, beta, num_points=1000):
        """
        Creates a Beta distribution prior for the delimiter probability p.
    
        Args:
            alpha: The alpha parameter of the Beta distribution.
            beta: The beta parameter of the Beta distribution.
            num_points: The number of points to use for discretization.
    
        Returns:
            A tuple of two arrays:
            - x: The values of p (from 0 to 1).
            - prior: The corresponding prior probabilities for each value of p.
        """
        x = np.linspace(0, 1, num_points)
        prior = scipy.stats.beta.pdf(x, alpha, beta)
        return x, prior
    
    def binomial_likelihood(n, z, p):
        """
        Calculates the binomial likelihood of observing z delimiters in a sentence of length n.
    
        Args:
            n: The length of the sentence (integer).
            z: The number of delimiters in the sentence (integer).
            p: The prior probability of a character being a delimiter.
    
        Returns:
            The likelihood of observing z delimiters in a sentence of length n.
        """
        return comb(n, z) * (p ** z) * ((1 - p) ** (n - z))

.. _graphs:
 
---------
graphs.py
---------

.. code-block:: python

    """ palindromes.graphs: Module for visualizing palindromic structures.
    """
    import matplotlib.pyplot as plt
    
    def conditional_character_histogram(freq_dist, length, condition, index):
        """
        Plots a histogram of the frequency distribution.
    
        Args:
            freq_dist: The frequency distribution dictionary.
            length: The length of the words analyzed.
            condition: The starting condition used.
        """
        sorted_freq = dict(sorted(freq_dist.items()))
        plt.figure(figsize=(10, 5))
        plt.bar(sorted_freq.keys(), sorted_freq.values())
        i = len(condition)
        plt.title(f"α[{index + 1}] Frequency Distribution | l(α) = {length} and  α[:{i}] = '{condition}')")
        plt.xlabel("Character")
        plt.ylabel("Frequency")
        plt.show()
    
    def integral_histograms(left_integrals, right_integrals, sentence_length, num_bins=20):
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
    
    def coefficient_histogram(all_coefficients, sentence_length):
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
        
    def length_histogram(length_freq_dict, mean_length):
        """
        Generates a histogram of sentence lengths for a given corpus.
    
        Args:
            length_freq_dict: A dictionary where keys are sentence lengths and values are their frequencies.
            mean_length: The sample mean of the sentence lengths.
        """
        lengths = list(length_freq_dict.keys())
        frequencies = list(length_freq_dict.values())
    
        plt.figure(figsize=(10, 5))
        plt.bar(lengths, frequencies, width=0.85)
        plt.axvline(mean_length, color='red', linestyle='dashed', linewidth=1, label=f"Mean: {mean_length:.2f}")
        plt.title("Sentence Length Distribution")
        plt.xlabel("Sentence Length (Characters)")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()
    
    def posterior_delimiter_histogram(p_values, posterior_probs, num_bins=20):
        """
        Generates a histogram of the posterior delimiter probabilities.
    
        Args:
            p_values: The values of p for which the prior is defined.
            posterior_probs: The posterior probabilities for each p_value.
            num_bins: The number of bins for the histogram.
        """
        plt.figure(figsize=(10, 5))
        plt.hist(p_values, weights=posterior_probs, bins=num_bins)
        plt.title(f"Posterior Delimiter Probability Distribution")
        plt.xlabel("p")
        plt.ylabel("Probability Density")
        plt.show()
    
    def delimiter_histogram(distribution_data):
        """
        Generates histograms of delimiter index distributions for each language and sentence length.
    
        Args:
            distribution_data: A dictionary containing the delimiter index frequency distributions.
        """
        for language, length_data in distribution_data.items():
            for length, index_freq in length_data.items():
                indices = list(index_freq.keys())
                frequencies = list(index_freq.values())
    
                plt.figure(figsize=(10, 5))
                plt.bar(indices, frequencies)
                plt.title(f"Delimiter Index Distribution ({language}, Length = {length})")
                plt.xlabel("Delimiter Index")
                plt.ylabel("Frequency")
                plt.show()
    
    def delimiter_barchart(delimiter_indices, sentence):  # Modified function
        """
        Generates a bar chart of delimiter indices with a specified left limit.
    
        Args:
            delimiter_indices: A list of delimiter indices.
            limit: The left limit of the x-axis (integer).
        """
        if not delimiter_indices:
            return  # Handle empty list
    
        plt.figure(figsize=(10, 5))
        plt.bar(delimiter_indices, [1] * len(delimiter_indices), width=0.05)  # Adjust width as needed
        plt.xlim(0, len(sentence))  # Set the left limit of the x-axis
        plt.title("Delimiter Index Distribution")
        plt.xlabel("Delimiter Index")
        plt.ylabel("Frequency")
        plt.suptitle(sentence, fontsize=10) 
        plt.show()

.. _main:
 
-------
main.py
-------

.. code-block:: python

    """ palindromes.main: Main module.
    """
    import json
    # application modules
    import estimators
    import parse
    import graphs
    import model
    
    def write(data, file_name):
        with open(file_name, "w") as outfile:
            json.dump(data, outfile)
    
    def update_posterior(p_values, prior_probs, sentence, likelihood_func):
        """
        Updates the prior distribution based on the observed sentence.
    
        Args:
            p_values: The values of p for which the prior is defined.
            prior_probs: The prior probabilities for each value of p.
            sentence: The observed sentence (string).
            likelihood_func: A function that calculates the likelihood of observing a sentence given delimiter indices and length.
    
        Returns:
            A new list representing the updated posterior distribution over p values.
        """
        n = len(sentence)
        z = sentence.count(' ') # Count of delimiters in the sentence
    
        # Calculate likelihood for the observed sentence length and each value of p
        likelihoods = [likelihood_func(n, z, p_val) for p_val in p_values]
    
        # Calculate the denominator P(ζ) using the law of total probability
        p_zeta = sum(l * p for l, p in zip(likelihoods, prior_probs))
    
        # Update the prior based on the likelihood and the normalizing constant
        posterior_probs = [(l * p) / p_zeta if p_zeta > 0 else 0 for l, p in zip(likelihoods, prior_probs)]
    
        return posterior_probs
    
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
    
        if not sentences:
            return left_integrals, right_integrals
    
        for sentence in sentences:
            if len(sentence) == sentence_length:
                left_integrals.append(model.lefthand_integral(sentence, sentence_length))
                right_integrals.append(model.righthand_integral(sentence, sentence_length))
    
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
            left_integrals, right_integrals = model.sentence_integrals(sentences, length)
    
            if not left_integrals and not right_integrals:
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
            sentences = parse.corpus(min_length, max_length, language, )
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
            sentences = parse.corpus(min_length, max_length, corpus)
            length_freq = estimators.length_frequencies(sentences)
            mean_length = estimators.sample_mean_freq(length_freq)
            graphs.length_histogram(length_freq, mean_length)
            results[corpus.value] = {
                "length_frequencies": length_freq,
                "mean_length": mean_length,
            }
    
        return results
    
    def analyze_delimiter_posterior(min_length, max_length):
        cleaned_sentences = parse.corpus(min_length, max_length)
    
        p_values, prior_probs = estimators.beta_prior(alpha=2, beta=10)
    
        # Iterate through the sentences and update the posterior
        posterior_probs = prior_probs.copy()
        for sentence in cleaned_sentences:
          if len(sentence) in range(min_length, max_length):
              posterior_probs = update_posterior(dict(zip([len(sentence)], [posterior_probs])), 
                                                 sentence, 
                                                 estimators.binomial_likelihood)
    
        midpoint = int((min_length + max_length)/2)
        graphs.posterior_delimiter_histogram(p_values, posterior_probs, midpoint)
        return posterior_probs
    
    def analyze_delimiter_distribution(min_length, max_length):
        """
        Analyzes the distribution of delimiter indices in sentences of varying lengths across different corpora.
    
        Args:
            min_length: The minimum sentence length to analyze.
            max_length: The maximum sentence length to analyze.
    
        Returns:
            A dictionary containing the delimiter index frequency distributions for each language and sentence length.
        """
        corpora = [parse.CORPORA.ENGLISH, parse.CORPORA.SPANISH, parse.CORPORA.HINDI]
        results = {}
    
        for corpus in corpora:
            results[corpus.value] = {}
            sentences = parse.corpus(min_length, max_length, corpus)
            for sentence in sentences:
                delimiter_indices = model.delimit(sentence)
                length = len(sentence)
                if length not in results[corpus.value]:
                    results[corpus.value][length] = {}
                for index in delimiter_indices:
                    results[corpus.value][length][index] = results[corpus.value][length].get(index, 0) + 1
    
        graphs.delimiter_histogram(results)
        return results
    
    def analyze_sentence_delimiters(sentence):
        """
        Analyzes the delimiter distribution in a sentence.
    
        Args:
            sentence: The input sentence (string).
        """
        delimiter_indices = model.delimit(sentence)
        graphs.delimiter_barchart(delimiter_indices, sentence)
    
    def analyze_conditional_word_probability(length, condition, offset=0):
        """
        Calculates the frequency distribution of characters at a specific position 
        in words of a given length that start with a given condition.
    
        Args:
            length: The desired length of the words.
            condition: The starting string condition (e.g., "da").
    
        Returns:
            A dictionary representing the frequency distribution of characters 
            at the position after the condition.
        """
    
        if len(condition) >= length:
            raise ValueError("Length of condition must be less than the length of the word.")
    
        # Get all words from the Brown corpus, convert to lowercase, remove non-alphanumeric,
        # and filter by length and starting condition
        words = parse.words(length)
        all_words = set(
            word.lower()
            for word in words
            if word.startswith(condition)
        )
    
        # Calculate the position after the condition
        position = len(condition) + offset
    
        # Create a frequency distribution of characters at the specified position
        freq_dist = {}
        for word in all_words:
            char = word[position]
            freq_dist[char] = freq_dist.get(char, 0) + 1
    
        graphs.conditional_character_histogram(freq_dist, length, condition, position)
    
        return freq_dist
    
    if __name__ == "__main__":
        length = 4
        condition = "wor"
        freq_dist = analyze_conditional_word_probability(length, condition, 0)
    
    

.. _model:
 
--------
model.py
--------

.. code-block:: python

    """ palindromes.module: Module containing the results and theorems of the formal system.
    """
    import string 
    
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
    
    def delimit(sentence):
        """
        Returns a list of delimiter indices in a sentence.
    
        Args:
            sentence: The input sentence (string).
    
        Returns:
            A list of integers, where each integer is the index of a delimiter in the sentence.
        """
        delimiter_indices = []
        for i, char in enumerate(sentence):
            if delimiter_count(char):
                delimiter_indices.append(i + 1)  # Add 1 to match our 1-based indexing
        return delimiter_indices
    
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
        return [sentence for sentence in sentences if is_palindrome(sentence)]
    
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
    

.. _parse:
 
--------
parse.py
--------

.. code-block:: python

    """ palindromes.parse: Module for parsing external data sources
    """
    import enum
    import nltk
    from nltk.corpus import brown, cess_esp, indian
    from nltk.tokenize import sent_tokenize
    import string
    
    class CORPORA(enum.Enum):
        ENGLISH = "english"
        SPANISH = "spanish"
        HINDI = "hindi"
    
    def init():
        # Download necessary NLTK data if you haven't already
        nltk.download('brown')
        nltk.download('cess_esp')
        nltk.download('punkt')
        nltk.download('punkt_tab')
        nltk.download('indian')
    
    def _clean_corpus(language, min_length, max_length):
        # Updated to use the CORPORA enum
    
        if language == CORPORA.ENGLISH:
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
    
        elif language == CORPORA.SPANISH:
            corpus = cess_esp.sents()
            cleaned_sentences = []
            for sentence in corpus:
                cleaned_sentence = " ".join(word for word in sentence if word not in string.punctuation and word not in "¡¿")
                cleaned_sentence = " ".join(cleaned_sentence.split()).lower()
                if min_length <= len(cleaned_sentence) <= max_length:
                    cleaned_sentences.append(cleaned_sentence)
            return cleaned_sentences
    
        elif language == CORPORA.HINDI:
            corpus = indian
            cleaned_sentences = []
            words = corpus.words('hindi.pos')
            
            # Build sentences based on full stop delimiter ('।')
            sentence = ""
            for word in words:
              if word == '।':
                if min_length <= len(sentence) <= max_length:
                  cleaned_sentences.append(sentence.strip())
                sentence = ""
              else:
                if len(sentence) > 0:
                  sentence += " "
                sentence += word
            
            # Add the last sentence if it meets the length criteria
            if len(sentence) > 0 and min_length <= len(sentence) <= max_length:
              cleaned_sentences.append(sentence.strip())
    
            return cleaned_sentences
    
        else:
            raise ValueError("Invalid language specified. Choose from 'english', 'spanish', or 'hindi'.")
    
    def corpus(min_length = 100, max_length = 200, language = CORPORA.ENGLISH):
        return _clean_corpus(language, min_length, max_length)
    
    def words(length, language = CORPORA.ENGLISH):
        if language == CORPORA.ENGLISH:
           return [ 
              word 
              for word 
              in brown.words() 
              if len(word) == length and word.isalpha() 
            ]