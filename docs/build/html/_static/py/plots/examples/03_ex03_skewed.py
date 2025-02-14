##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib as mpl

## NOTE: How-To: Run This Script On Your Computer
#
# To render the website, I have to use a "headless" backend to generate the images. 
# If you want to run this script on your computer, comment out the following line 
# with the "#" you see appended to each line of this comment:

mpl.use('agg')

import matplotlib.pyplot as plt

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axs) = plt.subplots()

# Generate data
data = [ 50000, 65000, 45000, 30000, 120000, 200000, 70000, 56000, 55000, 2000000 ]

# Label axes
plt.suptitle("Histogram of Annual Income in City X")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Income")
axs.set_ylabel("Frequency")

axs.hist(data, bins=50)

# Show results
plt.show()
