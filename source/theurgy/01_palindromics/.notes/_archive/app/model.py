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
