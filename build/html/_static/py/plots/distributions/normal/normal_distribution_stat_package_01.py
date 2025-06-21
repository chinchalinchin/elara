##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib

## NOTE: How-To: Run This Script On Your Computer
#
# To render the website, I have to use a "headless" backend to generate the images. 
# If you want to run this script on your computer, comment out the following line 
# with the "#" you see appended to each line of this comment:

matplotlib.use("agg")

import matplotlib.pyplot as mpl
import statistics as stat

(fig, axes) = mpl.subplots()

dist = stat.NormalDist(10, 2)
dist2 = stat.NormalDist(10, 0.5)
dist3 = stat.NormalDist(10, 4)

n = 100
start = 4
end = 16
delta = (end - start) / n

x_axis = [ start + i*delta for i in range(n+1) ]
y_axis = [ dist.pdf(x) for x in x_axis ]
y_axis_2 = [ dist2.pdf(x) for x in x_axis ]
y_axis_3 = [ dist3.pdf(x) for x in x_axis ]

mpl.suptitle("Normal Distributions with Mean = 10")

axes.set_xlabel("x")
axes.set_ylabel("density")

axes.plot(x_axis, y_axis, color="blue", label="std dev = 2")
axes.plot(x_axis, y_axis_2, color="red", label="std dev = 0.5")
axes.plot(x_axis, y_axis_3, color="green", label="std dev = 4")

axes.legend()
mpl.show()
