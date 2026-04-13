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

# Define the sizes of the subsets
subset_ab = 30  # Size of the intersection (A and B)
subset_a_minus_b = 20  # Size of A only
subset_b_minus_a = 15  # Size of B only

# Create the Venn diagram
v = venn2(subsets=(subset_a_minus_b, subset_b_minus_a, subset_ab), set_labels=('Set A', 'Set B'))

# Get the individual patches
area_ab = v.get_patch_by_id('11')
area_a = v.get_patch_by_id('10')
area_b = v.get_patch_by_id('01')

# Set the colors for the areas
if area_ab:
    area_ab.set_color('purple')
if area_a:
    area_a.set_color('red')
if area_b:
    area_b.set_color('blue')

# Remove the text labels
if v.get_label_by_id('11'):
    v.get_label_by_id('11').set_text('')
if v.get_label_by_id('10'):
    v.get_label_by_id('10').set_text('')
if v.get_label_by_id('01'):
    v.get_label_by_id('01').set_text('')

# Show the plot
plt.title("Overlapping Sets")
plt.show()