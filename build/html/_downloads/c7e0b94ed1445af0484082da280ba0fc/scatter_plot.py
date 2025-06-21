"""
Linear Regression
=================
Grant Moore
-----------
Some Time In The Distant Past
*****************************

This script shows how to analyze a bivariate sample of quantitative data. 

The sample of data used is pulled from Twitter. You will need to download the dataset here:

    https://bishopwalshmath.org/references/DOCS.html

The variables of interest in this datasets are: followers and tweet count.

We will call the "tweet count" the indicator variable.

We will call the "followers" the response variable.

We want to see how "followers" *respond* to "tweet count".

This script will:

1. Construct a scatter plot of the indicator variable versus the response variable.
"""

##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib.pyplot as plot
import csv 

def divider():
    print("-------------------------------------------------------------------------------------------------------")

with open("celebrity_twitter_data.csv") as infile:
    raw_data = [ obs for obs in csv.reader(infile) ]

headers = raw_data[0]
data = raw_data[1:]

print("------------------------------------- Twitter Dataset -------------------------------------------------")
print("source: https://www.kaggle.com/datasets/ahmedshahriarsakib/top-1000-twitter-celebrity-tweets-embeddings")
divider()
print("variable in dataset: ", headers)
print("first row of data: ", data[0])
print("second row of data: ", data[1])
divider()

# Follower Count Column: 4, Tweet Count Column: 5
# NOTE: the fifth column is the x-variable, or indicator variable
# NOTE: the fourth column is the y-variable, or response variable
sample = [ (obs[5], obs[4]) for obs in data ]

(fig, axes) = plot.subplots()

# separate x values from y values in sample
x_axis = [ int(obs[0]) for obs in sample ]
y_axis = [ int(obs[1]) for obs in sample ]
axes.scatter(x_axis, y_axis)

plot.title("Tweet Count vs Follower Count")

axes.set_xlabel("Tweets")
axes.set_ylabel("Followers (in tens of millions)")

plot.show()