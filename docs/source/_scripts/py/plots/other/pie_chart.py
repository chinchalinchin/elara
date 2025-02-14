"""
Pie Chart
=========
Grant Moore
-----------
Some Point In The Distant Past
******************************

MMMM. Pie.

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
import random
##################################################################################
###                           SCRIPT                                           ###
##################################################################################

def frequency(sample, x):
	freq = sum(1 for obs in sample if obs == x)
	return freq
	 
sodas = ["Coke", "Pepsi", "Sprite", "RC"]

sample = [ random.choice(sodas) for _ in range(30) ]

frequencies = [ frequency(sample, obs) for obs in sodas ]

(fig, axes) = plot.subplots()

plot.suptitle("Favorite Soda")
plot.title(f"n = {len(sample)}")

axes.pie(frequencies, labels=sodas)

plot.show()
