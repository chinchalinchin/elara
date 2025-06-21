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

from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Define the size of the set
subset_a = 1  # Size of Set A -  Must be > 0.

# Create the Venn diagram.  venn2 requires at least two circles.
# We pass a tuple of subset sizes, with the size of the second set as 0.
v = venn2(subsets=(subset_a, 0, 0), set_labels=('Set A', ''))

# Get the individual patch
area_a = v.get_patch_by_id('10')

# Color the set
if area_a:
    area_a.set_color('darkblue')

# Color the background.  We use plt.gca() to get the current axes.
plt.gcf().set_facecolor('lightblue')
plt.gca().set_axis_off() # Turn off the axis

# Remove the text label inside the circle
if v.get_label_by_id('10'):
    v.get_label_by_id('10').set_text('')
if v.get_label_by_id('01'):
    v.get_label_by_id('01').set_text('') #remove the 0

# Add the complement label.  We'll do this as a text annotation.
plt.annotate(r'$A^c$', xy=(0.8, 0.8), xycoords='axes fraction', fontsize=16, ha='center', va='center')

# Show the plot
plt.title("Complementary Sets")
plt.show()
