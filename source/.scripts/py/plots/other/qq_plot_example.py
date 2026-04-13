"""
Normal QQ Plot
==============
Grant Moore
-----------
Some Time In The Distant Past
*****************************

This script shows how to find the QQ plot of a sample to assess normality with hard-coded data.
In practice, the theoretical percentiles would be generated using the Inverse Normal CDF (Cumulative Distribution Function).

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

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

import statistics as stat
import matplotlib.pyplot as plot
	
data = [ 5, 10, 7, 1, 6, 9 ]
dist = stat.NormalDist(0, 1)
(fig, axes) = plot.subplots()
	
# calculate sample stats
xbar = stat.mean(data)
s = stat.mean(data)
n = len(data)

# sort data
data.sort()

# standardize
z_actual = [ (obs - xbar)/s for obs in data ]


# generate theoretical percentiles
z_theoretical = [ dist.inv_cdf((i+1)/(n+1)) for i in range(n)  ]

# plot
axes.scatter( z_actual, z_theoretical )
	
# label
axes.set_xlabel("Ranked Z-Scores")
axes.set_ylabel("Theoretical Z-Scores")
	
# show
plot.title("QQ Plot of Theoretical Z Score versus Actual Z-Score")
plot.show()
