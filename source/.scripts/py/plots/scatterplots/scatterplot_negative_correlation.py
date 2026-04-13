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
import random as rand

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axs) = plt.subplots()

# Generate Data
n = 20
x_data = [ rand.randint(0, 10) for _ in range(n) ]
y_data = [ 10 - 0.5*x +2*(rand.random() - 0.5) for x in x_data ]

# Label the graph appropriately
plt.suptitle("Scatterplot of Quiz Scores vs Hours Spent Playing Video Games")
plt.title(f"n = {n}")
## Label Scatter Plot Axes
axs.set_xlabel("Hours Spent Playing Video Games")
axs.set_ylabel("Quiz Score")

# Generate and output
## Plot Histogram
axs.scatter(*[x_data, y_data])

plt.show()
