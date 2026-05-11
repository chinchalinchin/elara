.. _ti_binomcdf_problems:

===============================
BINOMCDF: Binomial Distribution
===============================

Introduction
============

Recall the Cumulative Distribution Function (CDF) of a Random Variable is defined as,

.. math:: 

	P(\mathcal{X} \leq x)
	
In other words, the **CDF** of a Random Variable tells you the probability of observing an outcome of that Random Variable less than or equal to the given value x. Graphically, we interpret this as the area of the density curve to the left of the point x (when the Random Variable is continuous; when the Random Variable is discrete, the **CDF** is the sum of the heights).

All well-behaved Random Variables have a **CDF**. A Binomial Random Variable is no different! 

Calculator
==========

.. topic:: Binomial Probability Density Function

	To calculate a Binomial probability on a *TI-83/84* calculator, type in the following commands,
	 
	- :math:`\text{BUTTON}: \text{DISTR}`
	- :math:`\text{MENU}: \text{DISTR}`
	- :math:`\text{B}: \text{BINOMPDF}`
	
	
The **BINOMCDF** function requires three arguments,

1. ``n``: The number of independent trials.
2. ``p``: The probability of success for a single trial.
3. ``x``: The number of successes whose cumulative probability is sought.


Problems
========

1. A student body population is 45% female and 55% male. From this population, the Prom Committee is selected. Prom Committee is made up of 10 students. The school administration claims the committee is randomly drawn from all eligible students.

	a. Supposing the administration's claim is true, what is the probability of observing a committee with more than 5 females? Round to 4 decimal places.
	
	b. Supposing the administration's claim is true, what is the probability of observing a committee with less than 3 females? Round to 4 decimal places.
	
	c. Suppose this year's Prom Committee only has 2 female members. Does this provide convincing evidence the selection for Prom Committee is not random? Why or why not?
	
	d. Supposing the administration's claim is true, what is the probability of observing a committee with more than five males? Round to 4 decimal places.
	
	e. Supposing the administration's claim is true, what is the probability of observing a committee with less than 3 males? Round to 4 decimal places
	
	f. Suppose this year's Prom Committee only has 2 male members. Does this provide convincing evidence the selection for Prom Committee is not random? Why or why not?
	
Solutions
=========

TODO: jquery these into hidden elements

- 1a: 0.2616
- 1b: 0.0996
- 1d: 0.5044
- 1e: 0.0274	
