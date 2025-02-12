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
import statistics as stat

##################################################################################
###                                FUNCTIONS                                   ###
##################################################################################

def standardize(x, mu = 0, sigma = 1):
    return (x - mu) / sigma

def normal_density(x, mu = 0, sigma = 1):
    z = standardize(x, mu, sigma)
    exponent = - 0.5 * (z ** 2)
    constant = 1 / (sigma * math.sqrt(2 * math.pi))
    density = constant * math.exp(exponent)
    return density

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axs) = plt.subplots()

# NOTE: 
#   n is the number of points in the graph
#   mu is the mean of the normal distribution
#   sigma is the standard deviation of the normal distribution
n = 100
mu = 0
sigma = 1

# NOTE: By the empirical rule, 99% of the data is within 3 standard deviations of the mean
#   so go out four standard deviations on either side of the mean to get the interval,
#
#   [ mu - 4 * sigma, mu + 4 * sigma ]
#
#   The length of this interval is,
#
#   d = (mu + 4 * sigma) - (mu - 4 * sigma) = 8 * sigma
graph_interval = 8 * sigma
graph_step = graph_interval / n
graph_start = mu - 4 * sigma

dist = stat.NormalDist(0, 1)
percentile = dist.inv_cdf(0.35)

# Label the graph appropriately
plt.suptitle("Normal Distribution")
plt.title(f"mu = {mu}, sigma = {sigma}")
axs.set_xlabel("x")
axs.set_ylabel("p(x)")


# Generate normal data
x_data = [ graph_start + i * graph_step for i in range(n) ]
x_fill = [ x for x in x_data if x <= percentile ] + [ percentile ]
y_data = [ normal_density(x, mu, sigma) for x in x_data ]
y_fill = [ normal_density(x, mu, sigma) for x in x_fill ]

# Generate and output
plt.plot(x_data, y_data)
plt.fill_between(x_fill, 0, y_fill)
plt.plot([percentile, percentile], [0, 0.5], color="red", label="35th percentile")
plt.legend()
plt.show()
