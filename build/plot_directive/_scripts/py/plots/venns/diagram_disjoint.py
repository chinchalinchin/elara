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
subset_a = 20  # Size of A
subset_b = 15  # Size of B
subset_ab = 0    # Size of the intersection (A and B) - set to 0 for disjoint

# Create the Venn diagram
v = venn2(subsets=(subset_a, subset_b, subset_ab), set_labels=('Set A', 'Set B'))

# Get the individual patches
area_a = v.get_patch_by_id('10')
area_b = v.get_patch_by_id('01')

# Color the sets
if area_a:
    area_a.set_color('red')
if area_b:
    area_b.set_color('blue')

# There is no intersection in disjoint sets, so we don't need to color '11'

# Remove the text labels
if v.get_label_by_id('10'):
    v.get_label_by_id('10').set_text('')
if v.get_label_by_id('01'):
    v.get_label_by_id('01').set_text('')
if v.get_label_by_id('11'):
    v.get_label_by_id('11').set_text('')

# Show the plot
plt.title("Disjoint Sets")
plt.show()
