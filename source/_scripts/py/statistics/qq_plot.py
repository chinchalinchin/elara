"""
Normal QQ Plot
==============
Grant Moore
-----------
Some Time In The Distant Past
*****************************

This script shows how to find the QQ plot of a sample to assess normality. 

The sample is ordered (i.e. the *order statistics* are found) and then the theoretical percentiles from the Normal Distribution are found for each order statistic.
"""

import math
import random 
import statistics
import matplotlib.pyplot as plot 


def sample_mean(sample):
	"""
	Calculate the sample mean of a sample of data.
	"""
	xbar = sum(sample) / len(sample)
	return xbar

def sample_std_deviation(sample):
	"""
	Calculate the sample standard deviation of a sample of data.
	"""
	n = len(sample)
	mean = sample_mean(sample)
	sum_squared_deviations = sum( (obs - mean)**2 for obs in sample )
	std_dev = math.sqrt(sum_squared_deviations / (n-1))
	return std_dev
	
def qq_series(sample):
	"""
	Plot the ordered sample against its percentile from the normal distribution to see if the distribution is approximately normal.
	
	The sample is ordered (i.e. the *order statistics* are found) and then the theoretical percentiles from the Normal Distribution are found for each order statistic. 
	
	The result is returned as a list of ordered pairs (x_i, p_i), where x_i is the i-th ordered observation (order statistic) and p_i is the i-th theoretical normal percentile.
	"""
	sample.sort()
	n = len(sample)
	mean = sample_mean(sample)
	std_dev = sample_std_deviation(sample)
	theory_dist = statistics.NormalDist(mean, std_dev)
	theory_percentiles = [ theory_dist.inv_cdf((i+1)/(n+1)) for i in range(n) ]
	qq = [ (x, z) for x,z in zip(sample, theory_percentiles) ]
	return qq
	
# Generate some data.
data = [ random.randint(1, 50) for _ in range(30) ] 
qq = qq_series(data)
ordered_observations = [ pair[0] for pair in qq ]
theory_percentiles = [ pair[1] for pair in qq ]

# Create the plot
fig, axes = plot.subplots()
axes.scatter(ordered_observations, theory_percentiles)

# Label the plot
axes.set_xlabel("Ranked Observations")
axes.set_ylabel("Theoretical Normal Percentiles")

plot.show()
