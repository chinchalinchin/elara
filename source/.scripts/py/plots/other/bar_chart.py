"""
Bar Chart
=========
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a bar chart for a (hard-coded) distribution of quiz grades.

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
#       To render the website, I have to use a "headless" backend to generate the images. 
#       If you want to run this script on your computer, comment out the following line 
#       with the "#" you see appended to each line of this comment:

matplotlib.use('agg')

import matplotlib.pyplot as plt

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
(fig, axes) = plt.subplots()

# Generate Data
# NOTE: ``data``` is a dictionary. Dictionaries are another "data type" in Python.
#       see python documentation for more information: 
#           https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#
#       Dictionaries are "key-value" pairs, i.e. a set of ordered pairs (key, value)
#  
#       { 
#           'key_1': value_1,
#           'key_2': value_2 
#       }
# 
#       "keys" are strings. they are like the "index" of a dictionary. 
#
#       Recall the third element of 
# 
#           this_list = [0, 3, 9]
# 
#       Can be accessed through the bracket [] notation by using the index,
#
#           print(this_list[2])
#
#       This would output,
#
#           9
#
#       Dictionaries are a way of setting your own "index". Try loading the 
#       the following dictionary into your Python shell (i.e., copy and paste 
#       the ``data`` variable) and executing,
#
#           print(data['A'])
#
#           print(data['B'])
#
#       You should see the following output,
#
#           12
#       
#           10
data = {
    'A': 12,
    'B': 10,
    'C': 8,
    'D': 6,
    'E': 4,
    'F': 2
}

# display the keys of the dictionary: [ 'A', 'B', 'C', 'D', 'E', 'F' ]
print("keys: ", data.keys())
# display the values of the dictionary: [ 12, 10, 8, 6, 4, 2 ]
print("values: ", data.values())

# find the sum of frequencies
# NOTE: frequencies are the "values", i.e. right-hand side, of the dictionary
#       so we call the `values()` function **on** the ``data`` dictionary.
total_observations = sum(data.values())

# display the number of observations
print("total observations (n) = ", total_observations)

# create the relative frequency distribution
# NOTE: iterate over all (key, value) pairs in the ``data`` dictionary, and divide 
#       each value by the total number of observations
# NOTE: `data.items()` allows us to iterate over the (key, value) pairs in the 
#	dictionary at the same time.
relative_freq = { key: (value / total_observations) for key,value in data.items() }

# Label the graph appropriately
plt.suptitle("Bar Chart of Quiz Grades")
# NOTE: you can "template" strings with variables using f-strings. See python docs for more information:
#       https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
#       essentially, we are "injecting" the value of the variable in the string before it gets 
#       interpretted by Python and printed to screen, in the next line.
plt.title(f"n = {total_observations}")

# Set the axes labels
axes.set_xlabel("Grades")
axes.set_ylabel("Frequency")

# Plot the bar chart
# NOTE: access dictionary "keys" list, i.e. ['A', 'B', 'C', 'D', 'E', 'F'], with relative_freq.keys()
# NOTE: access dictionary "values" list, i.e. [12, 10, 8, 6, 4, 2], with relative_freq.values()
axes.bar(relative_freq.keys(), relative_freq.values(), color="lightblue", ec="red", width=0.5)

plt.show()
