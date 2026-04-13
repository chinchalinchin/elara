"""
The Effects of Outliers
=======================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a dot plot for a (hard-coded) distribution of quiz grades.
It will then calculate the sample mean and sample median and plot them with red and
green lines, respectively.

We will alter the distribution of grades in class to see how it affects the sample mean
and sample median.
"""

##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib.pyplot as plt
import math

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
fig, axs = plt.subplots()

# Generate Data for Dot Plot
# NOTE: the y-variable in the ordered pair is being increased by 1 in every iteration
#       of range(). This is so the dots can be stacked in a vertical line.
data = \
[ (3, i+1) for i in range(1) ] +\
[ (4, i+1) for i in range(3) ] +\
[ (5, i+1) for i in range(2) ] +\
[ (6, i+1) for i in range(6) ] +\
[ (7, i+1) for i in range(2) ] +\
[ (9, i+1) for i in range(5) ] +\
[ (24, i+1) for i in range(1) ] 

# calculate number of samples
n = len(data)

# Label the graph appropriately
plt.suptitle("Dot Plot of Quiz Grades")
plt.title(f"n = {n}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Get the x-coordinates and get the y-coordinates
x_values = [bit[0] for bit in data]
y_values = [bit[1] for bit in data]

# NOTE: Only the x-coordinate is required for sample statistic calculations. 
#       The y-value is only used to stack the dots.
# NOTE: The x-values are already sorted, so we don't need to sort them.

# Find order statistic for the median.
order = 0.5 * ( n + 1 )
order_floor = math.floor(order)
order_ceiling = math.ceil(order)
lower_percentile = x_values[order_floor]
upper_percentile = x_values[order_ceiling]
percentile_delta = (upper_percentile - lower_percentile)

# Calculate sample median
sample_median = lower_percentile + percentile_delta * (order - order_floor)

# Calculate sample mean
sample_mean = sum(x_values) / n

# Generate dotplot
axs.scatter(x_values, y_values)

# Plot the mean as a vertical line
axs.plot([sample_mean, sample_mean], [0, 10], linestyle="--", color="red")

# Plot sample median as a vertical line
axs.plot([sample_median, sample_median], [0, 10], linestyle="--", color="green")

# Label
axs.text(sample_mean + 1, 5, f"Sample Mean = {sample_mean}", color="red")
axs.text(sample_mean + 1, 4.5, f"Sample Median = {sample_median}", color="green")

plt.show()
