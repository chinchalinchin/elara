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
import random as rand

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axs) = plt.subplots()

# Generate Data
# NOTE: You can add the contents of lists together with "+" the same way you add 
#       numbers. This is type of addition is known as "concatenation" of lists.
data = ( 
    [ 9*rand.random() + 40 for x in range(2) ] + # generate some random F's, 40 - 49
    [ 9*rand.random() + 50 for x in range(5) ] + # generate some random E's, 50 - 59 
    [ 9*rand.random() + 60 for x in range(10) ] + # generate some random D's, 60 -69
    [ 9*rand.random() + 70 for x in range(10) ] + # generate some random C's, 70- 79
    [ 9*rand.random() + 80 for x in range(5) ] + # generate some random B's, 80 - 89
    [ 10*rand.random() + 90 for x in range(2) ] # generate some random A's, 90 - 100
)

# Label graph
plt.suptitle('Histogram of Quiz Grades')
plt.title(f"n = {len(data)}")

# Label axes
axs.set_xlabel('Grades')
axs.set_ylabel('Frequency')

# Plot data on the axes
# NOTE: classes are "bins" in matplotlib (and most other statistical applications)
axs.hist(data, bins=6, align='left', color='lightblue', ec='red')

# Show results
plt.show()
