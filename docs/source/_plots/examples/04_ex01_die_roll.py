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

(fig, axes) = plt.subplots()

outcomes = [ 1, 2, 3, 4, 5, 6]
freqs = [ 1 / 6 ] * 6

axes.bar(outcomes, freqs, width=1, ec="red", color="lightblue")
axes.set_xlabel("Die Roll")
axes.set_ylabel("Freq (%)")

plt.show()