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
import random
import math

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axs) = plt.subplots()

# Generate data
data = [ random.normalvariate(5.9, 1) for i in range(25) ]

# Label axes
plt.suptitle("Histogram")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Height (feet)")
axs.set_ylabel("Frequency")

# Plot data
axs.hist(data, bins=6, align='left', color="lightblue", ec="red")

# Find the median and mean
data.sort()
n = len(data)
percentile_index = 0.5*(n+1)
floor = math.floor(percentile_index) 
ceiling = math.ceil(percentile_index)
lower_order = data[floor]
upper_order = data[ceiling]
median = lower_order + (upper_order - lower_order) * (percentile_index - floor)
mean = sum(data)/n

plt.axvline(x=median, color='green', label="median")
plt.axvline(x=mean, color="blue", label="mean")
# Show results
axs.legend()
plt.show()
