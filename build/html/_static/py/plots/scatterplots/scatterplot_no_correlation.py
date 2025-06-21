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
#   NOTE: Range x (Random Number Between 0, 1) + Lower Limit
n = 20
data = [
    [ rand.randint(0, 10) for _ in range(n)],
    [ 10*rand.random() - 5 for _ in range(n) ]
]

# Label the graph appropriately
plt.suptitle("Scatterplot of Quiz Scores vs Minutes Late to Class")
plt.title(f"n = {n}")
## Label Scatter Plot Axes
axs.set_xlabel("Time Spent Studying")
axs.set_ylabel("Quiz Score")

# Generate and output
## Plot Histogram
axs.scatter(*data)
## Show results
plt.show()
