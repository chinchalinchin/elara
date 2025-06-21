"""
Normal Probability Calculations
===============================
Grant Moore
-----------
Some Time In The Distant Past
*****************************

This script illustrates some basic normal probability calculations and demonstrates the symmetry of the normal distribution.
"""


import statistics

# Define some functions to make the output look pretty.

def line_break():
    # print a line break. \ is an "escape character" that allows special characters
    # to be embedded in strings, such as line breaks.
    print("\n")

def underscore(sentence):
    print(sentence)
    line_break()

def fancify(sentence):
    line_break()
    print("-"*10, sentence, "-"*10)
    line_break()

# Create a normal distribution
mu = 50
sigma = 10
dist = statistics.NormalDist(mu, sigma)

# Find some important percentiles
first_quartile = dist.inv_cdf(0.25)
median = dist.inv_cdf(0.5)
third_quartile = dist.inv_cdf(0.75)

# Print the quartiles and make it look pretty
fancify(f"NormalDist(mu={mu}, sigma={sigma})")
print("the first quartile of this distribution is : ", first_quartile)
print("the median of this distribution is         : ", median)
print("the third quartile of this distribution is : ", third_quartile)

# Calculate some probabilities
prob_thirty = dist.cdf(30)
prob_fifty = dist.cdf(50)
prob_seventy= dist.cdf(70)

# Print the probabilities and make it look pretty
sep = "-"*5
fancify("Probability Calculations")
print("P(X <= 30 )                              = ", prob_thirty)
print("P(X <= 50 )                              = ", prob_fifty) 
print("P(X <= 70 )                              = ", prob_seventy)

# Calculate some complements
complement_prob_thirty = 1 - prob_thirty
complement_prob_seventy = 1 - prob_seventy

# Print the complements and make it look pretty
fancify("Important")
underscore("Both 30 and 70 are equal distances from the center!")
underscore("The normal distribution is symmetric!")
print("1 - P(X<=30) = P(X>30) = P(X <= 70)      = ", complement_prob_thirty)
print("1 - P(X<=70) = P(X>70) = P(X <= 30)      = ", complement_prob_seventy)