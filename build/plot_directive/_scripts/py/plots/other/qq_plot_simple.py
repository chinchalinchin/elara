"""
Normal QQ Plot
==============
Grant Moore
-----------
Some Time In The Distant Past
*****************************

This script shows how to find the QQ plot of a sample to assess normality with hard-coded data. In practice, the theoretical percentiles would be generated using the Inverse Normal CDF (Cumulative Distribution Function).

.. note:: 

    This script is written to run in a `Continuous Integration Pipeline <https://about.gitlab.com/topics/ci-cd/>`_. 
    
    It is used to render images for the `AP Stats Bishop Walsh website <https://bishopwalshmath.org>`_. 
    
    In other words, it is running in an environment without a desktop. Read comments below for more information on running it on your computer.

	
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

import matplotlib.pyplot as plot 

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

ordered_observations = [ -1.02, -0.44, 0.15, 1.32 ]
theory_percentiles = [ -0.84, -0.25, 0.25, 0.84]

# Create the plot
(fig, axes) = plot.subplots()

# Plot the points
axes.scatter(ordered_observations, theory_percentiles)

# Label the plot
axes.set_xlabel("Ranked Z-Scores")
axes.set_ylabel("Theoretical Normal Percentiles")

plot.show()
