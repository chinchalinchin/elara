.. _binomial-distribution:

=====================
Binomial Distribution
=====================

.. _binomial-random-variable:

Binomial Random Variable
========================

Definition
----------

Recall a :ref:`bernoulli-random-variable` is defined over a sample space of binary outcomes, a success ``s`` that occurs with probability :math:`p` of success and a failure ``f`` that occurs with probability :math:`1-p`,

.. math::
    Y = \begin{array}{ c l }
        1                 & \quad \textrm{with probability} p \\
        0                 & \quad \textrm{with probability } 1 - p
    \end{array}

Consider a random variable defined as the sum of :math:`n` **Bernoulli** random variables, :math:`Y_i`

.. math:: 
    X = Y_1 + Y_2 + ... + Y_{n-1} + Y_n

Where each :math:`Y_i` takes the value 1 with probability :math:`p` or it takes the value 0 with probabilitiy :math:`1 - p`

TODO 

From :ref:`conditional-probability`, the probability of an intersection of :ref:`independent events <independence>` is the product of individual probabilitiy,

.. math:: 

    P(A \cap B) = P(A) \cdot P(B)

TODO

.. _binomial-conditions:

Conditions
----------

In order for an experiment to be *Binomial*, the experiment must the conditions just discussed. The summary below provides a list of each condition.

.. topic:: Binomial Conditions

	1. The number of trials :math:`n` must be fixed.
	2. Each trial must be independent of the others.
	3. Each trial must have a binary outcome, usually denoted success or failure.  
	4. The probability of success is the same in each trial.
	

.. _binomial_parameters

Parameters
----------

The Binomial Distribution has two parameters.

.. topic:: Binomial Parameters
	
	1. :math:`n`: The number of trials.

	2. :math:`p`: The probability of success in a single trial.

TODO

.. plot:: _plots/distributions/binomial/binomial_distribution_01.py

.. plot:: _plots/distributions/binomial/binomial_distribution_02.py

.. plot:: _plots/distributions/binomial/binomial_distribution_03.py

.. plot:: _plots/distributions/binomial/binomial_distribution_04.py


Probabilitiy Distribution
=========================

TODO

.. _binomial-pdf:

Probability Density Function
----------------------------

TODO 

.. math:: 

    p(x; n, p) = C^{n}_x \cdot p^{x} \cdot (1 - p)^{n-x}

.. _binomial-cdf:

Cumulative Distribution Function
--------------------------------

TODO

By definition,


.. math:: 

    F(x; n, p) = \sum^{x}_{i=0} C^{n}_i \cdot p^{i} \cdot (1 - p)^{n-i}

.. _binomial-expectation:

Expectation
-----------

TODO

derive through rules of independent random variable sums

.. topic:: Expectation of Binomial Random Variable

	If :math:`\mathcal{X}` is the number of successes in *n* independent trials, each with probability *p*, then the expectation of :math:`\mathcal{X}`, :math:`E(\mathcal{X})`, is given by,
	
	.. math::
	
		E(\mathcal{X}) = n \ cdot p
		
TODO

.. _binomial-standard-deviation:

Standard Deviation
------------------

TODO

.. topic:: Variance of Binomial Random Variable

	If :math:`\mathcal{X}` is the number of successes in *n* independent trials, each with probability *p*, then the variance of :math:`\mathcal{X}`, :math:`Var(\mathcal{X})`, is given by,
	
	.. math::
	
		Var(\mathcal{X}) = n \ cdot p \cdot (1 - p)
	
TODO
	
.. topic:: Standard Deviation of Binomial Random Variable

	If :math:`\mathcal{X}` is the number of successes in *n* independent trials, each with probability *p*, then the standard deviation of :math:`\mathcal{X}`, :math:`\sigma_{Bin(n,p)}`, is given by,
	
	.. math::
	
		\sigma_{Bin(n,p)} = n \ cdot p
TODO

derive through rules of independent random variable sums
