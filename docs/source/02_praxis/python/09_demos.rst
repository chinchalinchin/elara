.. _python_demos:

==============
Demonstrations
==============

Below you will find some **Python** scripts that demonstrate various statistical facts and theorems. We will go over them in class when the time comes. 

Conditional Distributions
-------------------------

This script will generate a random bivariate sample of categorical data and then construct a conditional distribution for one variable. A stacked bar chart is then created to visualize the association, or lack thereof, between the two conditional distributions. 

:download:`Stacked Bar Chart (Conditional Distribution) <../../assets/demos/conditional_distributions.py>`

Estimators
----------

This script contains many useful functions for young statisticians seeking to tame the wild beast of uncertainy.

:download:`Point Estimators <../../assets/demos/stats.py>`

Measuring Variation
-------------------

This script displays a dot plot of a sample of data and illustrates how the different measures of variation are affected by the slight alterations in the sample of data.

:download:`Measuring Variation <../../assets/demos/variation.py>`

The Effect of Outliers
----------------------

This script generates a distribution of grades and visualizes the distribution with a dot plot. It will then calculate the sample mean and sample median, and plot as vertical lines, red and green respectively. 

We will alter the distribution in class to see how it affects the sample mean and median.

:download:`The Effects of Outliers <../../assets/demos/outliers.py>`

Scatter Plot of Twitter Data 
----------------------------

This script shows how to parse a CSV file and then create a scatter plot with it. To execute this script, you will need to download the Twitter dataset from :ref:`datasets` section and place it in the same folder where you download this script.

This dataset is an example of :ref:`negative <negative_correlation>`, :ref:`non-linear <non_linear_correlation>` correlation. In other words, even though there is clearly a correlation in this dataset, we cannot use linear regression to fit a model.

:download:`Twitter Data Scatter Plot <../../assets/demos/scatter_plot.py>`

Die Roll Simulation
-------------------

This script will simulate rolling ``m`` die ``n`` times. The outcome of the ``m`` die rolls is then summed and a frequency distribution is created for the ``n`` experiments. The frequency distribution is visualized with a histogram. 

The intent is show how the random variation of :ref:`independent <independence>`, identically distributed :ref:`random variables <random_variables>` leads naturally to the normal distribution. This result is known as :ref:`central_limit_theorem`

:download:`Die Roll Simulations <../../assets/demos/die_rolls.py>`

Normal Distribution
-------------------

This script shows how to work with the normal distribution in **Python**. It demonstrates how to calculate percentiles and probabilities. It also demonstrates how the symmetry of the :ref:`normal_distribution` manifests numerically via the :ref:`law_of_complements`.

:download:`Normal Distribution <../../assets/demos/normal_probabilities.py>`

QQ Plot
-------

This script shows how to construct a QQ plot to assess the normality of a sample of data. 

:download:`QQ Plot <../../assets/demos/qq_plot.py>`

Least Squares Regression
------------------------

This script illustrates how the regression parameters for the slope and intercept of the line of best fit are estimated used least squares.

:download:`Least Squares <../../assets/demos/least_squares.py>`

Biased Estimators
-----------------

This script illustrates the difference between *biased* and *unbiased* estimators. It will simulate a sample from a Normal population and then calculate various statistics. The results of the simulation are shown in a histogram with the true value of the population parameter plotted as a vertical line.

:download:`Biased Estimators <../../assets/demos/sampling_simulations.py>`

Central Limit Theorem
---------------------

This script illustrates the Central Limit Theorem. The user may specify a population distribution and then select a simple random sample from the specified population. The distribution of the sampling distribution for the mean when a sample of this size is selected is then calculated. The results are plotted on side-by-side histograms. The user may adjust the number of samples drawn and then recalculate the sampling distribution to see how increasing the number of samples induces normality in the sampling distribution, no matter how the underlying population is distributed.

:download:`Biased Estimators <../../assets/demos/central_limit_theorem.py>`

Confidence Intervals
--------------------

This script illustrates the frequentist interpretation of a Confidence Interval. Under the frequentist interpretation, the Confidence Interval can be thought of as an interval that will contain the true value of the population parameter with a certain probability. In other words, at a 95% confidence level, 5% of the time a Confidence Interval will **not** contain the true value of the population parameter.

This script will simulate a fixed number of sample from a Normal population and then calculate the indicated confidence interval for each sample. The results are plotted as stacked error bars. The true mean is plotted a black vertical line. Intervals that contain the true value of the population mean will be shown in green whereas intervals that do not contain the true value of the population mean will be shown in red.

:download:`Confidence Intervals <../../assets/demos/confidence_intervals.py>`

Power
-----

This script illustrates the idea of *Power* for hypothesis testing. The test being illustrated is a one-sided mean test. The null distribution is plotted along with its shaded rejection region; this area represents the probability of a Type I error under the null hypothesis. This is shown against the alternate distribution for various values of the population parameter. The area corresponding to the probability of a Type II error in the null distribution is plotted as a shaded region under the alternate distribution above the critical value. The relationship between Type I and Type II errors can be shown by adjusting the significance to see its effects on the *Power* of the hypothesis test.

In addition, the number of samples can be adjusted to see how increasing or decreasing the given sample size affects the *Power* of the hypothesis test.

:download:`Confidence Intervals <../../assets/demos/power.py>`
