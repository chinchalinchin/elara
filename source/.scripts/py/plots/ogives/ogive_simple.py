"""
Normal Histogram
================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a histogram for a randomly generated sample of quiz grades (where the grade is a percentage).

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

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axes) = plt.subplots()

# Generate Data
data = [ 1, 9, 10, 11, 20, 29, 30, 31, 39 ]

# Label graph
plt.suptitle('Histogram and Boxplot of Random Sample')
plt.title(f"n = {len(data)}")

# Label axes
## Label CDF
axes.set_xlabel("Grades")
axes.set_ylabel("Cumulative Frequency")

# Plot data on the axes
axes.hist(data, bins=6, cumulative=True, density=True)

# Show results
plt.show()
