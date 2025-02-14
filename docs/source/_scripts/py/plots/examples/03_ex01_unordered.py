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
data = [ 6.5, -2.5, 4.3, 0.5, 7.0, -1.0, 5.0, 3.0, -1.5 ]
obs_order = [ i for i, _ in enumerate(data) ]

# Label axes
plt.suptitle("Scatter Plot of Minutes Late vs Observation Order")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Observation Order")
axs.set_ylabel("Minutes Late")

# Plot data
axs.scatter(obs_order, data)

mpl.rcParams['lines.linewidth'] = 0.5
mpl.rcParams['lines.linestyle'] = '--'

for i in obs_order:
    plt.axvline(x=i)

# Show results
plt.show()
