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

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

import matplotlib.pyplot as plt
import matplotlib_venn as vplt

# Define the size of the set
set_size = 20

# Create the Venn diagram with one set
v = vplt.venn2(subsets=(set_size, 0, 0), set_labels=('Set A', ''),)

# Color the set
v.get_patch_by_id('10').set_color('darkblue')

# Remove set labels
v.get_label_by_id('10').set_text('')
v.get_label_by_id('01').set_text('')

# Set background to white
plt.gcf().set_facecolor('white')

# Remove the axis
plt.gca().set_axis_off()

# Add points
plt.plot(0.1, 0.1, 'ro')  # a inside
plt.plot(0.2, 0, 'ro')    # b inside
plt.plot(0.15, -0.1, 'ro') # c inside
plt.plot(0.6, 0.6, 'ro')  # d outside
plt.plot(-0.6, -0.6, 'ro') # e outside

# Add labels for the points
plt.text(0.1, 0.1, 'a', color='black', ha='center', va='center')
plt.text(0.2, 0, 'b', color='black', ha='center', va='center')
plt.text(0.15, -0.1, 'c', color='black', ha='center', va='center')
plt.text(0.6, 0.6, 'd', color='black', ha='center', va='center')
plt.text(-0.6, -0.6, 'e', color='black', ha='center', va='center')

# Center the plot and adjust the layout
plt.title("Venn Diagram with Elements")
plt.show()
