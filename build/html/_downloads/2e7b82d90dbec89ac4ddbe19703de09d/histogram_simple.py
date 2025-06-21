"""
Boxplot
=======
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

import matplotlib.pyplot as plot

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

data = [ 1, 9, 10, 11, 20, 29, 30, 31, 39 ]

# Create figure and axes to graph on
(fig, axes) = plot.subplots()

axes.hist(data, align="mid")

plot.title("Histogram of Random Sample")
axes.set_xlabel("Random Numbers")
axes.set_ylabel("Sample")

plot.show()



