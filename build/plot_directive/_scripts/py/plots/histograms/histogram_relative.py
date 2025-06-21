"""
Relative Frequency Histogram
============================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a histogram for a sample of random data.

.. note:: 

    This script is written to run in a `Continuous Integration Pipeline <https://about.gitlab.com/topics/ci-cd/>`_. It is used to render images for the `AP Stats Bishop Walsh website <https://bishopwalshmath.org>`_. In other words, it is running in an environment without a desktop. Read comments below for more information on running it on your computer. 
"""

##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib

## NOTE: How-To: Run This Script On Your Computer
#
#       To render the website, I have to use a "headless" backend to generate the images. 
#       If you want to run this script on your computer, comment out the following line 
#       with the "#" you see appended to each line of this comment:

matplotlib.use('agg')


import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import random as rand

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axs) = plt.subplots()

# Generate data
# NOTE: Range*(Random Number Between 0 and 1) will give us a dataset of samples 
#       between 0 and Range. In other words, the following command generates a list of 
#       length 100 where each element is a number between 0 and 50
data = [ 50*rand.random() for _ in range(100 ) ]

# NOTE: for the hist() function to plot percentages on the y-axis, each 
#       observation must be assigned a weight that represents what "proportion"
#       of the sample it is.
weights = [ 1/len(data) for _ in data ]

# Label Graph
plt.suptitle("Relative Frequency Histogram of Random Numbers between 0 and 50")
plt.title(f"n = {len(data)}")

# Label Axes
axs.set_xlabel("Classes")
axs.set_ylabel("Frequency")
# Tell the y-axis you want to scale it to percentages
axs.yaxis.set_major_formatter(PercentFormatter(1))

# Generate and output
axs.hist(data, bins=6, weights=weights, align='mid', color="lightblue", ec="red")
plt.show()
