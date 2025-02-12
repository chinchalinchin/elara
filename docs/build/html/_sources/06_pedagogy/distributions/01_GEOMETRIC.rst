.. _geometric-distribution:

======================
Geometric Distribution
======================

TODO

.. _geometric-random-variable:

Geometric Random Variable
=========================

Definition
----------

TODO

.. _geometric-conditions:

Geometric Conditions
--------------------

TODO

.. topic:: Conditions for Geometric Random Variable

	1. The trials must be independent.
	
	2. Each trial must be either a success or failure.
	
	3. The probability of each trial must be the same across trials. 
	

TODO

.. _geometric-parameters:

Geometric Parameters
--------------------

A Geometric Random Variable has single parameter.

.. topic:: Geometric Parameters

	1. :math:`p`: the probability of success in a single trial.

.. _geometric-probability:

Geometric Probability
=====================

TODO 

.. _geometric-pdf:

Probability Density Function
----------------------------

TODO

.. math:: 

    P(\mathcal{X} = x) = \sum_{i=1}^{x} (1-p)^{x-1} \cdot p

TODO

.. _geometric-cdf:

Cumulative Distribution Function
--------------------------------

TODO

In order to show the geometric density represents a distribution, we must show the probability of all outcomes sums to 1. In order to do this, we must first talk about the *geometric series*.

.. _geometric-series:

Geometric Series
****************

A geometric series is defined as the sum of powers of ``r``,

.. math:: 

    \sum_{i=1}^{n} r^i = r + r^2 + r^3 + ... + r^n 

The reason it is called *geometric* can be easily seen if we give ``r`` a value. For instance, if :math:`r = \frac{1}{4}`, then the first few terms of the geometric series are given by,

.. math:: 

    \sum_{i=1}^{n} (\frac{1}{4})^i = \frac{1}{4} + \frac{1}{16} + \frac{1}{64} + ... + (\frac{1}{4})^n

Each term on the right hand side can be identified with the areas of successive squares in the following picture,

.. image:: ../../_static/img/mathematics/geometric_series.png
    :align: center
    
.. _geometric-expectation:

Expectation
-----------

TODO