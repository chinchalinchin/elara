.. _ti_geometcdf_problems:

=================================
GEOMETCDF: Geometric Distribution
=================================

Introduction
============

The Geometric Distribution, like every other parametric distribution, has a Cumulative Distribution Function (CDF). Recall the CDF of a random variable X is given by,

.. math::

	F(x) = P(\mathcal{X} \leq x)
	
In other words, the CDF of a random variable tells you the probability of observing an outcome of that random variable less than or equal to the given value ``x``. Graphically, we interpret this as the area of the density curve to the left of the point x.

(TODO: INSERT PICTURE)

Calculator
==========

.. topic:: Geometric Cumulative Distribution Function

	The following sequence will bring up the **geometCDF** function on the *TI-83/84* family of calculators,

	- :math:`\text{BUTTON}: \text{2ND}`
	- :math:`\text{BUTTON}: \text{DISTR}`
	- :math:`\text{MENU}: \text{DISTR}`
	- :math:`\text{F}: \text{GEOMETCDF}`
	
1. ``p``: a probability of success for a single trial.
2. ``x``: the number of trials whose probability of being less than the indicated value is sought. 

(TODO: insert picture of GEOMETCDF menu)

Problems
========

1. Three red balls and seven green balls are placed into a magical probability box. You select them one by one, with replacement.

	a. What is the probability that you draw less than five balls before you get the first red ball? Round to four decimal places.

	b. What is the probability that you draw at least five balls before you get the first red ball? Round to four decimal places.
	
	c. What is the probability you draw at least five balls before you get the first green ball? Round to four decimal places.

	d. Explain why the answer to *part c* is less than *part b* if there are more green balls in the magical probability box than red balls.
	
2. A recent news report (TODO: link to YouGov poll) claimed 10% of people believe the Earth is flat.

	a. If you ask 20 people before finding someone who believes the Earth is flat, what are the chances of an outcome at least this extreme occuring by random chance? Round to three decimal spots.
	
	b. If you ask 30 people before finding someone who believes the Earth si flat, what are the chances of an outcome at least this extreme occuring by random chance? Round to three decimal spots.
	
	c. Interpret the answers to *part a* and *part b* in terms of statistical significance. What happens to the likelihood of the news report claim as you observe more and more people who do not believe the Earth is flat before finding one who does? Explain how the answers to *part a* and *part b* provide evidence to support or contradict the news report claim.
	
Solutions
=========

TODO: jquery these into hidden elements

- 1a: 0.7599
- 1b: 0.2401
- 1c: 0.0081
- 2a: 0.135
- 2b: 0.047


