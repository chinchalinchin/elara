"""
Die Roll Sum Simulation
=======================
Grant Moore
-----------
Some Time In The Distant Past
*****************************

This script will simulate rolling *m* dice *n* times. It will sum up the *m* die rolls and create a histogram of the outcomes. 

This script is meant to illustrate the motivating idea behind the Central Limit Theorem: independent, identically distributed random variables are summed together. Some of the random variable values will correspond to small values (i.e. rolling nothing but ones), while some values will correspond to large values (i.e. rolling nothing but sixes). On average, the variations will be "averaged" out of the distribution until the distribution becomes approximately normal.

The more die we roll and the more times we roll them, the closer the resulting distribution becomes to normal. The Central Limit Theorem states that as *m* and *n* go to infinity, **all** distributions become normal, no matter what the underlying population looks like.
"""

import random 
import matplotlib.pyplot as plot 

def sum_dice(dice): 
    roll = sum([random.randint(1, 6) for _ in range(dice) ])
    return roll

# NOTE: Run this script and then modify *n* and *m* to see how the 
#       distribution is affected.

# number of experiments
n = 30
# number of rolls per experiment
m = 5

# roll m die n times
die_rolls = [ sum_dice(m) for _ in range(n) ]

fig, axes = plot.subplots()

axes.set_xlabel(f"Sum of {m} Die Rolls, {n} times")
axes.set_ylabel("Frequency")
axes.hist(die_rolls)

plot.show()
