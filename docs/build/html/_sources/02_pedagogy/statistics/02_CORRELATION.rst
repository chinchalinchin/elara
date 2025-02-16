.. _correlation:

===========
Correlation
===========


Up to now we have been dealing with *univariate* data. In this section, we begin the study of *bivariate data*.

Definitions
===========

.. _bivariate-data:

Bivariate Data
--------------

:math:`S = \{ (x_1, y_1), (x_2, y_2), ... , (x_n, y_n) \}`
	When two variables are measured on one individual, we call such data *bivariate*.
	
The :math:`x` variable is sometimes called the *independent* or *predictor* variable. The :math:`y` variable is sometimes called the *dependent* or *response* variable. It is important to understand this terminology is only used in the context of the :ref:`linear_regression` model introduced in the next section. Before the *statistical significance* of the relationship is established, this terminology is misleading, as it implies a relationship between the :math:`x` and `y` variable when none may exist. Correlation can be measured between variables that have no relationship whatsoever; in such instance we call the variables *uncorrelated*. 

.. important::

	Because we are dealing with randomness, *uncorrelated* variables will not necessarily have a correlation of 0. In fact, correlations of 0 are never observed in practice. There will always be a non-zero correlation between any given variables; the task of statistics is to determine whether or not this correlation is significant enough to use the outcome of one variable to make predictions about the outcome of the other variable.

Correlation
-----------

Correlation is a measure of the strength of a relationship that exists between two observable variables. Before we can begin our study of *correlation*, let's make some preliminary defintions that will help us keep everything clear and precise.

.. _univariate-correlation-statistics:

Univariate Statistics
*********************

In order to differentiate between the statistics relationing to the *x* and *y* variables, we introduce some notation.

:math:`\bar{x}` and :math:`\bar{y}` are defined as the *univariate* sample means of the :math:`x` and :math:`y` variables. In other words, :math:`\bar{y}` is the sample mean of the :math:`y` variable, as if we were observing the :math:`y` variable in isolation. Similarly for :math:`\bar{x}`.


:math:`s_x` and :math:`s_y` are defined as the *univariate* standard deviations of the :math:`x` and :math:`y` variables. In other words, :math:`s_x` is the standard deviation of the :math:`x` variable, as if we were observing the :math:`x` variable in isolation. Similarly, for :math:`s_y`. 

.. math::

	s_{x}^2 = \frac{1}{n-1} \cdot \sum_{i=1}^{n} (x_i - \bar{x})^2
	
.. math::
	
	s_{y}^2 = \frac{1}{n-1} \cdot \sum_{i=1}^{n} (y_i - \bar{y})^2
	
TODO


:math:`s_x` and :math:`s_y` are defined as the *univariate* standard deviations of the :math:`x` and :math:`y` variables. In other words, :math:`s_x` is the standard deviation of the :math:`x` variable, as if we were observing only :math:`x` alone. Similarly, for :math:`s_y`. 

.. math::

	s_{x}^2 = \frac{1}{n-1} \cdot \sum_{i=1}^{n} (x_i - \bar{x})^2
	
.. math::
	
	s_{y}^2 = \frac{1}{n-1} \cdot \sum{i=1}^{n} (y_i - \bar{y})^2
	
TODO

Definition
**********

TODO

.. topic:: Correlation, Version 1

	.. math::

		r_{xy} = \frac{1}{n-1} \cdot \sum_{i=1}^{n} z^{x}_i \cdot z^{y}_i
	

TODO: justification. make some plots.


.. topic:: Correlation, Version 2
	
	.. math::

		r_{xy} = \frac{1}{n-1} \cdot \sum_{i=1}^{n} (\frac{x_i - \bar{x}}{s_x}) \cdot (\frac{y_i - \bar{y}}{s_y})
	
.. topic:: Correlation "Shortcut" Formula

	TODO


.. _scatter-plots:

Scatter Plots
=============

A scatterplot is a very simple and easy to understand graphical representation of bivariate data. The :math:`x` variable is plotted on the horizontal axis versus the :math:`y` variable on the vertical axis. Graphs of *scatterplots* are classified based on the *direction* of the relationship observed, the *strength* of the relationship observed and the *linearity* of the relationship observed.

.. _correlation-direction:

Direction
---------

.. _no-correlation:

No Correlation
**************

A scatterplot with no correlation between the :math:`x` and :math:`y` variables should appear random,

.. plot:: _scripts/py/plots/scatterplots/scatterplot_no_correlation.py

.. _positive-correlation:

Positive Correlation
********************

A scatterplot with a positive correlation betwen the :math:`x` and :math:`y` variables should have a general upward trend,

.. plot:: _scripts/py/plots/scatterplots/scatterplot_positive_correlation.py

.. _negative_correlation:

Negative Correlation
********************

.. plot:: _scripts/py/plots/scatterplots/scatterplot_negative_correlation.py

.. _correlation_strength:

Strength
--------

.. _strong_correlation:

Strong
******

TODO

.. _weak_correlation:

Weak
****

TODO

.. _correlation_linearity:

Linearity
---------

.. _linear_correlation:

Linear
******

TODO 

.. _nonlinear_correlation:

Non-Linear
**********
 
TODO

.. _time_series:

Time Series
===========

A *time series* is similar to a *scatter plot* in almost all ways, except the *independent* variable in a *time series* is always a unit of time. A *correlation* for a *time series* is called a *trend*.

Positive Trend
--------------

.. plot:: _scripts/py/plots/timeseries/timeseries_positive_trend.py

Negative Trend
--------------

.. plot:: _scripts/py/plots/timeseries/timeseries_negative_trend.py

No Trend
--------

.. plot:: _scripts/py/plots/timeseries/timeseries_no_trend.py
