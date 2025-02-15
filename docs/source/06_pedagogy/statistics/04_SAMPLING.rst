.. _sampling-distributions:

======================
Sampling Distributions
======================

TODO

.. _central-limit-theorem:

Central Limit Theorem
=====================

The **Central Limit Theorem** is one of the most important theorems in statistics (if not mathematics). The **Central Limit Theorem** is what allows us to use the :ref:`Normal Distribution <normal_distribution>` to make inferences about the :ref:`population <population>`

TODO

.. _clt-motivation:

Motivation
----------

Consider a pop-quiz made up of two questions administered to a population of a 100 students. Suppose you conducted a census of how many questions each student got right on the pop-quiz. In other words, suppose you knew the probability distribution for the *population* was given by,  

+-----+-------+
|  x  |  p(x) |
+=====+=======+
|  0  |  0.20 |
+-----+-------+
|  1  |  0.30 |
+-----+-------+
|  2  |  0.50 |
+-----+-------+


It is important to keep in mind the meaning of this table. The right hand column represents the probability of selecting an individual with the left hand column number of answers correct. In other words, the probability a single randomly selected individual from the population got 0 answers correct is *0.20*, or *20%*. Similarly, the probability a single randomly selected individual from the population got 1 answer correct is *0.40*, or *40%*. Finally, the probability a single randomly selected individual from the population got both answers correct is again *0.50*, or *50%*. A graph of the :ref:`random-variable-pdf` helps visualizes the situation,

.. plot:: _scripts/py/plots/sampling/population_histogram.py
    :align: center

Since we are assuming we know the population distribution, we can see how sampling the population affects the value and distribution of the sample mean. This will provide insight into the more likely scenario of *not* knowing anything about the population and only having information about the sample. In other words, in what follows, the population distribution will be assumed to see what this implies about the sample mean. Then, the conclusions regarding the sample mean will be applied to scenarios where the population distribution is *unknown*.

Suppose a random sample of 2 students are drawn from this population *with replacement*. Recall "*with replacement*" means the same student may be observed more than once, since every student is put back into the population for subsequenct selections. 

In drawing a sample of 2 students, an account must be taken of all possible ways this sample that might be drawn. Each student will have either gotten 2 answers correct, 1 answer correct or 0 answers correct. By the :ref:`generalized-counting-principle`, the total number of possible 2 person samples that can be drawn from this population is,

.. math:: 
    3 \cdot 3 = 9

All possible samples **S**:sub:`i` are enumerated below in :ref:`list-notation`

    :math:`S_1  = \{ 0, 0 \}`
    
    :math:`S_2 = \{ 0, 1 \}`

    :math:`S_3 = \{ 0, 2 \}`

    :math:`S_4 = \{ 1, 0 \}`

    :math:`S_5 = \{ 1, 1 \}`

    :math:`S_6 = \{ 1, 2 \}`

    :math:`S_7 = \{ 2, 0 \}`

    :math:`S_8 = \{ 2, 1 \}`

    :math:`S_9 = \{ 2, 2 \}`
    
    
TODO

.. _distribution-of-sample-proportion:

Sample Proportion
=================

TODO

.. topic:: Sampling Distribution for Sample Proportion

	If :math:`\mathcal{X}_i \sim \text{Bern}(p)` for :math:`i = 1, 2, ..., n` and the following **conditions for inference** are met,
	
	1. :math:`n \cdot p \geq 10`
	2. :math:`n \cdot (1 - p) \geq 10`
	
	The random variable, :math:`\hat{p} = \frac{\mathcal{X}_1 + \mathcal{X}_2 + ... + \mathcal{X}_n}{n}` has the following distribution,
	
	.. math::
	
		\hat{p} \sim \mathcal{N}(p, \sqrt{\frac{p \cdot (1 - p)}{n}})
TODO

Difference of Proportions
-------------------------

TODO

.. topic:: Sampling Distribution for Difference of Sample Proportions

	If :math:`\mathcal{X}_i \sim \text{Bern}(p_x)` for :math:`i = 1, 2, ..., n_x` and the following **conditions for inference** are met,
	
	1. :math:`n_x \cdot p_x \geq 10`
	2. :math:`n_x \cdot (1 - p_x) \geq 10`
	
	**And** if :math:`\mathcal{Y}_i \sim \text{Bern}(p_y)` for :math:`i = 1, 2, ..., n_y` and the following **conditions for inference** are met,
	
	3. :math:`n_y \cdot p_y \geq 10`
	4. :math:`n_y \cdot (1 - p_y) \geq 10`
	
	Then the random variable :math:`\hat{p}_x - \hat{p}_y` has the following distribution,
	
	.. math::
	
		\hat{p}_{x} - \hat{p}_y \sim \mathcal{N}(p_x - p_y, \sqrt{\frac{p_x \cdot (1 - p_x)}{n_x} + \frac{p_y \cdot (1 - p_y)}{n_y}} ) 
TODO

.. _distribution-of-sample-mean:

Sample Mean
===========

TODO

.. _distribution-of-sample-mean-known-sigma:

Known Standard Deviation
------------------------

TODO 

.. topic:: Sampling Distribution for the Sample Mean, Known Standard Deviation, Version 1

	If 
		1. :math:`\mathcal{X}_i \sim \mathcal{N}(\mu, \sigma)` for :math:`i = 1, 2, ..., n` 
	
	**And** the following **conditions for inference** is met,
	
		2. :math:`n \geq 30`
		
	Then the random variable :math:`\bar{\mathcal{X}} = \frac{\mathcal{X}_1 + \mathcal{X}_2 + ... + \mathcal{X}_n}{n}` has the following distribution, 
	
	.. math::
	
		\bar{\mathcal{X}} \sim \mathcal{N}(\mu, \frac{\sigma}{\sqrt{n}})
	
TODO

.. topic:: Sampling Distribution for the Sample Mean

	If 
		1. :math:`\mathcal{X}_i \sim \mathcal{N}(\mu, \sigma)` for :math:`i = 1, 2, ..., n` 
	
	**And** the following **conditions for inference** is met,
	
		2. :math:`n \geq 30`
		
	Then the standardized value :math:`\mathcal{Z}` of the random variable :math:`\bar{\mathcal{X}} = \frac{\mathcal{X}_1 + \mathcal{X}_2 + ... + \mathcal{X}_n}{n}` has the following distribution, 
	
	.. math::
	
		\frac{\bar{X} - \mu}{ \frac{\sigma}{\sqrt{n}} \sim \mathcal{N}(0, 1)  	
TODO

.. _distribution-of-sample-mean-unknown-sigma:

Unknown Standard Deviation
--------------------------

TODO

.. topic:: Distribution of Sample Mean, Standard Deviation Unknown

	Let each :math:`\mathcal{X_i}` for :math:`i = 1, 2, ..., n` be selected from the same population. If :math:`n \geq 30`, then 
	
	.. math::
	
		\frac{ \bar{X} - \mu }{ \frac{s}{ \sqrt{n} } } \sim t(n-1) 
		
TODO


Difference of Sample Means
--------------------------

.. _distribution-of-sample-mean-difference-known-sigma:

Known Standard Deviation
************************

TODO

.. topic:: Sampling Distribution for Difference of Sample Means, Standard Deviation Known

	If 
	
		1. :math:`\mathcal{X}_i \sim \mathcal{N}(\mu_x, \sigma_y)` for :math:`i = 1, 2, ..., n_x`
		
		2. :math:`\mathcal{Y}_i \sim \mathcal{N}(\mu_y, \sigma_x)` for :math:`i = 1, 2, ..., n_y` 
		
	And the following **conditions for inference** is met,
	
		3. :math:`min(n_1, n_2) \geq 30`
		
	Then the random variable :math:`\bar{\mathcal{X}} - \bar{\mathcal{Y}}` has the following distribution, 
	
	.. math::
	
		\bar{\mathcal{X}} - \bar{\mathcal{Y}} \sim \mathcal{N}(\mu_x - \mu_y, \sqrt{ \frac{{\sigma_x}^2}{n_x} + \frac{{\sigma_y}^2}{n_y}})
TODO

