"""
Normal Boxplot
==============
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a histogram for a sample of quiz grades. The distribution of grades is normal.

.. note:: 

    This script is written to run in a `Continuous Integration Pipeline <https://about.gitlab.com/topics/ci-cd/>`_. It is used to render images for the `AP Stats Bishop Walsh website <https://bishopwalshmath.org>`_. In other words, it is running in an environment without a desktop. Read comments below for more information on running it on your computer. 
"""


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
import random as rand

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
# NOTE: 2 axes are being created!
    #       1 to graph the histogram
    #       1 to graph the boxplot
(fig, axs) = plt.subplots(1, 2)

# Generate Data
# NOTE: You can add the contents of lists together with "+"
data = ( 
    [ 9*rand.random() + 40 for _ in range(5) ] + # generate some random F's, 40 - 49
    [ 9*rand.random() + 50 for _ in range(9) ] + # generate some random E's, 50 - 59 
    [ 9*rand.random() + 60 for _ in range(12) ] + # generate some random D's, 60 -69
    [ 9*rand.random() + 70 for _ in range(8) ] + # generate some random C's, 70- 79
    [ 9*rand.random() + 80 for _ in range(6) ] + # generate some random B's, 80 - 89
    [ 10*rand.random() + 90 for _ in range(2) ] # generate some random A's, 90 - 100
)


# Label the graph appropriately
plt.suptitle("Histogram and Box Plot of Quiz Scores")
plt.title(f"n = {len(data)}")

## Label Histogram Axes
axs[0].set_xlabel("Score")
axs[0].set_ylabel("Frequency")

## Label Boxplot Axes
axs[1].set_xlabel("Score")
axs[1].set_ylabel("Sample")

## Plot Histogram
axs[0].hist(data, bins=6, align='mid', color="lightblue", ec="red")

## Plot Boxplot
axs[1].boxplot(data, vert=False, whis=(0,100))

# Display image
plt.show()
