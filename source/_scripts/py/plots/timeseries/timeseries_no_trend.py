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
from matplotlib.ticker import PercentFormatter
import random as rand

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axs) = plt.subplots()

# Generate Data
n = 100
x_data = [ i for i in range(n) ]
y_data = [ 0.5 * (0.25 ** 2) * (1/252) * rand.normalvariate(0, 1) for x in x_data ]

# Label the graph appropriately
plt.suptitle("Time Series of Stock Return Over " + str(n) + " Days")
## Label Scatter Plot Axes
axs.set_xlabel("Day")
axs.set_ylabel("Stock Return")
axs.yaxis.set_major_formatter(PercentFormatter(1))

# Generate and output
## Plot Histogram
axs.plot(x_data, y_data)

plt.show()
