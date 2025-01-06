""" palindromes.graphs: Module for visualizing palindromic structures.
"""
import matplotlib.pyplot as plt

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