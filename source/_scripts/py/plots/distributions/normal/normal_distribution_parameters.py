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
(fig, axs) = plt.subplots(1, 3, sharey=True)

# NOTE: 
#   n is the number of points in the graph
#   mu is the mean of the normal distribution
#   sigma is the standard deviation of the normal distribution
n = 1000

mu = 10

standard_deviations = [ 2, 5, 10 ]


graph_start = 0
graph_end = 20
graph_step = (graph_end - graph_start) / n
x_data = [ graph_start + i * graph_step for i in range(n) ]

for index, sigma in enumerate(standard_deviations):
    # Generate normal data    
    y_data = [ normal_density(x, mu, sigma) for x in x_data ]
    axs[index].plot(x_data, y_data)
    axs[index].set_xlabel("x")
    axs[index].set_ylabel("p(x)")

# Label the graph appropriately
plt.suptitle("Normal Distribution, mu = 10")
plt.title(f"sigma = 2, 5, 10")

plt.show()
