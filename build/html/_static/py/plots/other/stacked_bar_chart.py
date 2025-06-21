"""
Stacked Bar Chart
=================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a stacked bar chart for a randomly generated set of bivariate data. 

The individual in the data is the object selected from a box of ducks and balls (*Imagine that.*) 

The individual may either be **RED** or **BLUE**, or the individual may either be a **DUCK** or **BALL**. 

.. note:: 

    This script is written to run in a `Continuous Integration Pipeline <https://about.gitlab.com/topics/ci-cd/>`_. 
    
    It is used to render images for the `AP Stats Bishop Walsh website <https://bishopwalshmath.org>`_. 
    
    In other words, it is running in an environment without a desktop. Read comments below for more information on running it on your computer.

"""

##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib

## NOTE: How-To: Run This Script On Your Computer
#
#   To render the website, I have to use a "headless" backend to generate the images. 
#   If you want to run this script on your computer, comment out the following line 
#   with the "#" you see appended to each line of this comment:

matplotlib.use('agg')

import matplotlib.pyplot as plt
import random

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axes) = plt.subplots()

####################################################################################
## STEP 1: Create Sample
####################################################################################

# Define categories
shapes = [ "BALL", "DUCK" ]
colors = [ "RED", "BLUE" ]

# Use categories with random.choice() to generate random bivariate sample 
# (shape, color) of 100 observations
data = [ (random.choice(shapes), random.choice(colors)) for _ in range(100) ]
n = len(data) # although we already know it's a 100 (why?)...still good to get in the habit of calculating ``n``.

# Print everything to see what is going on.
separator = "-"*10 
# multiplying a string extends it by that number of characters.
# in other words, the line above will create the string "----------"
print(separator, "SAMPLE OF DATA", separator) # curious, very curious
print(data)

####################################################################################
## STEP 2: Find joint frequencies
####################################################################################

# this is a trick to count the elements in a list of data when you only want to count
# elements that satisfy a certain condition. For instance, to find `blue_balls`, we 
# only want to sum the outcomes that include a shape of 'ball' and a color of 'blue'
# NOTE: we access the x-value of the (shape, color) ordered pair the same way we
#	access an element of a list, with the index.
blue_balls = sum(1 for obs in data if obs[0] == "BALL" and obs[1] == "BLUE")
red_balls = sum(1 for obs in data if obs[0] == "BALL" and obs[1] == "RED")
blue_ducks = sum(1 for obs in data if obs[0] == "DUCK" and obs[1] == "BLUE")
red_ducks = sum(1 for obs in data if obs[0] == "DUCK" and obs[1] == "RED")


print(separator, "Joint Distribution", separator) 

# divide frequencies by n to get relative joint frequencies
print("P(BLUE and BALL) : ", blue_balls/n)
print("P(RED and BALL): ", red_balls/n)
print("P(BLUE and DUCK) : ", blue_ducks/n)
print("P(RED and DUCK) : ", red_ducks/n)

####################################################################################
## STEP 3: Find the marginal frequencies of the groups
####################################################################################

blue_things = blue_ducks + blue_balls
red_things = red_ducks + red_balls

print(separator, "Marginal Distribution of Color", separator)

# divide frequencies by n to get relative marginal frequency
print("P(BLUE) : ", blue_things/n)
print("P(RED) : ", red_things/n) 

####################################################################################
## STEP 4: Find conditional distribution of each group
####################################################################################

# conditional distribution of shape given the individual is blue
percent_of_blue_that_are_balls = blue_balls/blue_things
percent_of_blue_that_are_ducks = blue_ducks/blue_things

print(separator, "Conditional Distribution of Shape Given Blue", separator)
print("P(BALL | BLUE) : ", percent_of_blue_that_are_balls)
print("P(DUCK | BLUE) : ", percent_of_blue_that_are_ducks)

# conditional distribution of shape given the individual is red
percent_of_red_that_are_balls = red_balls/red_things
percent_of_red_that_are_ducks = red_ducks/red_things

print(separator, "Conditional Distribution of Shape Given Red", separator)
print("P(BALL | RED) : ", percent_of_red_that_are_balls)
print("P(DUCK | RED) : ", percent_of_red_that_are_ducks)


# NOTE: unfortunately, there is no nice way of making stacked bar charts with matplotlib
#       you have to "manually" stack the bars on top of the category to which they correspond.
#       each time you stack, you add the height of the previous bar to tell matplotlib
#       to start the bar at the top of the previous bar.

# Stack Conditional Distribution of Shape Given Red
axes.bar("RED", percent_of_red_that_are_balls, color="yellow", ec="blue", width=0.5, label="BALL")
# add the previous percent to the `bottom` to stack
axes.bar("RED", percent_of_red_that_are_ducks, bottom=percent_of_red_that_are_balls, color="lightgreen", ec="blue", width=0.5,  label="DUCK")

# Stack Conditional Distribution of Shape Given Blue
# NOTE: don't label this group, or else you'll get two legends
axes.bar("BLUE", percent_of_blue_that_are_balls, color="yellow", ec="blue", width=0.5)
# add the previous percent to the `bottom` to stack
axes.bar("BLUE", percent_of_blue_that_are_ducks,  bottom=percent_of_blue_that_are_balls, color="lightgreen", ec="blue", width=0.5,)

axes.set_ylabel("Relative Frequency")
plt.legend(loc="upper right")
plt.show()
