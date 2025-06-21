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

# matplotlib.use('agg')

import matplotlib.pyplot as plt
import random as rand

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
# Create 2 axes. 
# NOTE: the first argument to subplots() is the number of "figures".
#   We are not using figures in this class, but if we want to create two sets of axes
#   we have to be sure to pass in 1 first. subplots() always interprets the first argument
#   as the number of figures. 
#   The second argument is the number of axes you wish to plot on. We are creating one
#   set for the histogram and one set for the boxplot.
# NOTE: subplots(1, 2) will return a *list* of axes.
(fig, axes) = plt.subplots(1, 2)

# Generate Data
data = [ 1, 9, 10, 11, 20, 29, 30, 31, 39 ]

# Label graph
plt.suptitle('Histogram and Boxplot of Random Sample')
plt.title(f"n = {len(data)}")

# Label axes
# Access the first axes with bracket notation. Because we created two subplots, the axes
#   variable is actually a list. We have to make sure to plot on the correct axis!

## Label Histogram
axes[0].set_xlabel('Grades')
axes[0].set_ylabel('Frequency')

## Label Boxplot
axes[1].set_xlabel("Grades")
axes[1].set_ylabel("Sample")

# Plot data on the axes
# NOTE: classes are "bins" in matplotlib (and most other statistical applications)
axes[0].hist(data, bins=6, align='left', color='lightblue', ec='red')
axes[1].boxplot(data, vert=False, whis=(0,100))

# Show results
plt.show()
