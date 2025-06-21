
"""
Point Estimators
================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script illustrates how altering the sample distribution affects the value of the sample deviation.
"""

# import everything you need

import math
import random
import matplotlib.pyplot as plot # use `as` to get a shortcut name.

# some useful functions

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
	
# create figure and axes on which to plot
(fig, axes) = plot.subplots()

# hardcode some data
# NOTE: try changing the data set to see how it affects the variation
data = [ 1, 1, 3, 5,5.75, 10, 12]

# find the height of each unique observation's dot plot point
y_values = [] # declare an empty list to hold some values
# for each *unique* observation in the sample
# 	i.e., calling set(list) will return the *unique* values
for element in set(data):	
	# find the frequency of the observation
	freq = sum(1 for obs in data if obs == element)
	# stack y-value for each 0, 1, 2, ..., freq
	# add the heights of each dot to the y_values list. add 1 because range starts at 0.
	y_values += [ height + 1 for height in range(freq)] 
	
# calculate number of samples
n = len(data)

# calculate sample statistics
xbar = sample_mean(data)
deviations = [ (obs - xbar) for obs in data ]
std_dev = sample_std_deviation(data)
abs_dev = sum(abs(dev) for dev in deviations)/(n-1)
avg_dev = sum(deviations)/(n-1)

# Label the graph appropriately
plot.suptitle("Dot Plot of Quiz Grades")
plot.title(f"avg_dev = {round(avg_dev, 2)}, abs_dev = {round(abs_dev,2)}, std_dev = {round(std_dev,2)}")
axes.set_xlabel("Grades")
axes.set_ylabel("Frequency")

# Generate dotplot
axes.scatter(data, y_values)

# Plot the mean as a vertical line
axes.plot([xbar, xbar], [0, 10], linestyle="--", color="green")
axes.text(xbar + 0.25, 5, f"Sample Mean = {round(xbar, 2)}", color="green")

# Plot deviations as horizontal lines
for dev, height in zip(deviations, y_values):
	# make positive deviations blue, negative deviations red.
	color = "blue" if dev >= 0 else "red"
	# add random offset to height so lines don't overlap
	offset = (random.random() - 1) / 4
	axes.plot([xbar, xbar + dev], [height + offset, height + offset], linestyle="--", color=color)
	
plot.show()
