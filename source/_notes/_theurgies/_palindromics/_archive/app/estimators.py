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