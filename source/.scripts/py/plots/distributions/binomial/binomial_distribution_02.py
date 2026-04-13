##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib

## NOTE: How-To: Run This Script On Your Computer
#
# To render the website, I have to use a "headless" backend to generate the images. 
# If you want to run this script on your computer, comment out the following line 
# with the "#" you see appended to each line of this comment:

matplotlib.use('agg')

import matplotlib.pyplot as plt
import math

##################################################################################
###                                FUNCTIONS                                   ###
##################################################################################

def combination(n, r):
    return math.factorial(n) / ( math.factorial(r) * math.factorial(n-r) )

def binomial(n, p, x):
    return (p ** x) * ((1 - p) ** (n - x)) * combination(n, x)

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axs) = plt.subplots()

n = 30
p = 0.2

# Label the graph appropriately
plt.suptitle("Binomial Distribution")
plt.title(f"n = {n}, p = {p}")
axs.set_xlabel("Successes")
axs.set_ylabel("Probability")

successes = [x for x in range(n + 1) ]
probabilities = [ binomial(n, p, x) for x in range(n +1) ]

# Generate and output
axs.bar(successes, probabilities, color="lightblue", ec="red")
plt.show()
