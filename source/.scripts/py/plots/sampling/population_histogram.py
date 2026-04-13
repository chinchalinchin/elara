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

# And uncomment this line: 

# matplotlib.use('tkagg')

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

(fig, axs) = plt.subplots()

data = [ 0, 0, 1, 1, 1, 2, 2, 2, 2, 2 ]
weights = [ 1/len(data) for _ in data ]


plt.suptitle("Histogram of Quiz Scores")
plt.title("n = 100 students")

axs.hist(data, bins=3, weights=weights, range=(0,3))

axs.yaxis.set_major_formatter(PercentFormatter(1))

axs.set_xlabel("Scores")
axs.set_ylabel("Percentage")

plt.show()