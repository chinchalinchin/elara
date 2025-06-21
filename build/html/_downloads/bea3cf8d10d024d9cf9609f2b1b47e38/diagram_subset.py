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
subset_a = 20  # Size of the outer set
subset_ab = 10  # Size of the inner set (A and B)

# Create the Venn diagram.  The order of subsets is (A only, B only, A and B)
v = venn2(subsets=(subset_a - subset_ab, 0, subset_ab), set_labels=('A', 'B'))

# Get the individual patches
outer_set = v.get_patch_by_id('10')
inner_set = v.get_patch_by_id('11')

# Color the sets
if outer_set:
    outer_set.set_color('lightblue')
if inner_set:
    inner_set.set_color('darkblue')

# Remove the text labels
if v.get_label_by_id('10'):
    v.get_label_by_id('10').set_text('')
if v.get_label_by_id('11'):
    v.get_label_by_id('11').set_text('')
if v.get_label_by_id('01'):
    v.get_label_by_id('01').set_text('')

# Set the background color to white
plt.gcf().set_facecolor('white')

# Show the plot
plt.title("Subsets")
plt.show()
