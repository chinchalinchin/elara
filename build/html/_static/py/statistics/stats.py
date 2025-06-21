"""
Point Estimators
================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script contains some useful functions for calculating sample statistics and conducting simulations.
"""

import math
import random
import statistics

def roll_dice(n):
	"""
	Simulates rolling a die *n* times.
	"""
	experiment = [ random.randint(1, 6) for _ in range(n) ]
	return experiment

def marginal_frequency(sample, x):
	freq = sum(1 for obs in sample if obs[0] == x)
	return freq
	
def joint_frequency(sample, x, y):
	"""
	Find the joint frequecy of a sample of bivariate data { (x_i, y_i) } for a particular value of x and y.
	"""
	freq = sum(1 for obs in sample if obs[0] == x and obs[1] == y)
	return freq

def conditional_frequency_x_given_y(sample, x, y):
	marg_freq_y = marginal_frequency(sample, y)
	joint_freq_xy = joint_frequency(sample, x, y)
	conditional_freq_x_given_y = joint_freq_xy / marg_freq_y
	return conditional_freq_x_given_y
	
def sample_mean(sample):
	"""
	Calculate the sample mean of a sample of data.
	"""
	xbar = sum(sample) / len(sample)
	return xbar

def sample_percentile(sample, percentile):
	"""
	Calculate the sample percentile of a sample of data.
	"""
	sample.sort()
	n = len(sample)
	order = percentile * (n + 1)
	order_floor = math.floor(order)
	order_ceiling = math.ceil(order)
	lower_bound = sample[order_floor]
	upper_bound = sample[order_ceiling]
	percentile_delta = (upper_bound - lower_bound)
	result = lower_bound + percentile_delta * (order - order_floor)
	return result
    
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
