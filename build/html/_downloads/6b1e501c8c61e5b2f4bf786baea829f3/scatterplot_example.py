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

import matplotlib.pyplot as mpl
import statistics as stat

bivariate_data = [
    (2, 1), (8, 3), (1, 1), (2, 0), (9, 4), (3, 2), (5, 3),
    (1, 0), (7, 3), (6, 3), (3, 2), (0, 0), (0, 1), (8, 4),
    (0, 0), (3, 1), (4, 3), (7, 3), (1, 1), (10, 6), (6, 4),
    (3, 2), (7, 3), (6, 2), (9, 5), (5, 3), (1, 1), (4, 2),
    (1, 0), (7, 3)
]
(fig, axes) = mpl.subplots()

# separate x and y data
x_data = [ obs[0] for obs in bivariate_data ]
y_data = [ obs[1] for obs in bivariate_data ]

axes.scatter(x_data, y_data)

# label axes
mpl.title("Scatterplot Example")
axes.set_ylabel("y observation")
axes.set_xlabel("x observation")

mpl.show()
