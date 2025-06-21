"""
Dot Plot
========
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a dot plot for a (hard-coded) distribution of quiz grades.

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
(fig, axs) = plt.subplots()

# Generate Data
# NOTE: the y-variable in the ordered pair is being increased by 1 in every iteration
#       of range(). This is so the dots can be stacked.
data = \
[ (3, i+1) for i in range(2) ] +\
[ (4, i+1) for i in range(3) ] +\
[ (5, i+1) for i in range(2) ] +\
[ (6, i+1) for i in range(6) ] +\
[ (7, i+1) for i in range(2) ] +\
[ (9, 1) ]

# Label the graph appropriately
plt.suptitle("Dot Plot of Quiz Grades")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Generate and output
# Get the x-coordinates and get the y-coordinates
x_values = [bit[0] for bit in data]
y_values = [bit[1] for bit in data]

axs.scatter(x_values, y_values)
plt.show()