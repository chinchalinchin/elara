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