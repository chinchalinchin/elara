##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib

## NOTE: How-To: Run This Script On Your Computer
#
# To render the website, I have to use a "headless" backend to generate the images. 
# If you want to run this script on your computer, comment out the following line 
# with the "#" you see appended to each line of this comment:

# matplotlib.use('agg')

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axes
fig, ax = plt.subplots(figsize=(8, 8))

# Set the background color
fig.patch.set_facecolor('lightblue')
ax.set_facecolor('lightblue')

# Set the limits of the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Turn off the axes

# Define the positions and labels for the vertices
positions = {
    'A': (0, 1),
    'E': (0, -1),
    'I': (0.8, 0),
    'O': (-0.8, 0),
}
labels = {
    'A': 'All S are P',
    'E': 'No S are P',
    'I': 'Some S are P',
    'O': 'Some S are not P',
}

# Draw the vertices as circles
for pos, label_text in labels.items():
    x, y = positions[pos]
    circle = patches.Circle((x, y), radius=0.1, facecolor='darkblue', edgecolor='black')
    ax.add_patch(circle)
    ax.text(x, y, label_text, ha='center', va='center', color='white', fontsize=10)

# Draw the lines connecting the vertices
ax.plot([positions['A'][0], positions['E'][0]], [positions['A'][1], positions['E'][1]], color='black', linestyle='-', linewidth=2)
ax.plot([positions['I'][0], positions['O'][0]], [positions['I'][1], positions['O'][1]], color='black', linestyle='-', linewidth=2)
ax.plot([positions['A'][0], positions['I'][0]], [positions['A'][1], positions['I'][1]], color='black', linestyle='-', linewidth=2)
ax.plot([positions['A'][0], positions['O'][0]], [positions['A'][1], positions['O'][1]], color='black', linestyle='-', linewidth=2)
ax.plot([positions['E'][0], positions['I'][0]], [positions['E'][1], positions['I'][1]], color='black', linestyle='-', linewidth=2)
ax.plot([positions['E'][0], positions['O'][0]], [positions['E'][1], positions['O'][1]], color='black', linestyle='-', linewidth=2)

# Add labels for the relations
ax.text(0, 0.5, 'Contraries', ha='center', va='center', fontsize=12)
ax.text(0, -0.5, 'Contradictories', ha='center', va='center', fontsize=12)
ax.text(0.4, 0.8, 'Subalternation', ha='center', va='center', fontsize=12)
ax.text(0.4, -0.8, 'Subalternation', ha='center', va='center', fontsize=12)
ax.text(-0.4, 0.8, 'Subcontraries', ha='center', va='center', fontsize=12)
ax.text(-0.4, -0.8, 'Subcontraries', ha='center', va='center', fontsize=12)


# Set the title
plt.title("Aristotle's Square of Opposition", fontsize=16)

# Show the plot
plt.show()
