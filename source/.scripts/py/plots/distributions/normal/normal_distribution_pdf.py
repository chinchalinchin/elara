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


##################################################################################
###                                SCRIPT                                      ###
##################################################################################

import random
import statistics as stat
import matplotlib.pyplot as mpl
	
data = [ 1, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9,10,12 ]
(fig, axes) = mpl.subplots()

# find range of data sample_min
sample_min = min(data)
sample_max = max(data)

# divide range in 1000 sub-intervals
m = 1000
delta = (sample_max - sample_min)/m
	
# calculate sample stats
xbar = stat.mean(data)
s = stat.stdev(data)
n = len(data)
	
# create ideal (population) distribution
dist = stat.NormalDist(xbar, s)
	
# find actual density
## create density axis by iterating over 1000
## calculate the x-value for each sub-interval
## i.e., add multiples of the delta to the sample_min
density_axis = [ sample_min + i * delta for i in range(m) ]
## calculate the density for each x-value
density = [ dist.pdf(x) for x in density_axis ]
	
# plot actual histogram
axes.hist(data, bins=10, density=True, color="lightblue", ec="red", label="Histogram")

# plot density curve on top
axes.plot(density_axis, density, label="Ideal") 

# label graph
axes.legend()
mpl.title("Sample vs. Ideal Distribution")
axes.set_ylabel("Density")
axes.set_xlabel("Observation")

# show
mpl.show()
