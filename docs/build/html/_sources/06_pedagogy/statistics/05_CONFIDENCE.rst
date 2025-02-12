.. _confidence_intervals:

====================
Confidence Intervals
====================

Definitions
===========

Critical Value
--------------

TODO

.. topic:: Critical Z Value

	A value :math:`z_{\alpha}` from the Standard Normal distribution is defined as,
	
	.. math::
	
		P(\mathcal{Z} \leq z_{\alpha}) = 1 - \alpha
		
.. topic:: Critical T Value

	A value :math:`t_{\alpha}` from Student's T Distribution is defined as,
	
	.. math::
	
		P(\frac{\bar{\mathcal{X}}-\mu}{\mathcal{S}} \leq t_{\alpha}) = 1 - \alpha

Standard Error
--------------

TODO 
		

.. topic:: Standard Error

	The standard error of an estimator :math:`\hat{\theta}` is defined as,
	
	.. math::
	
		s_{\theta} = E( (\theta - E(\hat{\theta}))^2 )
		
Margin of Error
---------------

.. topic:: Margin of Error

	If *c* is a critical value from a point estimator :math:`\theta`'s sampling distribution and :math:`s_{\theta}` is the standard error of that estimator, then the margin of error for that point estimator is given by,
	
	.. math::
	
		\text{MOE} = c \rvert \cdot s_{\theta}		
		
Intervals
---------

.. topic:: Confidence Intervals

	If :math:`\theta` is a population parameter, :math:`\hat{\theta}` is a point estimator of :math:`\theta` and :math:`\text{MOE}_{\theta}` is the margin of error for that estimator, the confidence interval for :math:`\theta` is given by,
	
	.. math::
	
		\hat{\theta} - \text{MOE}_{\theta} \leq \theta \leq \hat{\theta} + \text{MOE}_{\theta}

TODO

Population Proportion
=====================

Standard Error
--------------

.. topic:: Sample Proportion Standard Error

	.. math::
	
		s_{\hat{p}} = \sqrt{ \frac{ \hat{p} \cdot (1-\hat{p}) }{n} }
		
Difference of Two Proportions
*****************************

.. topic:: Difference of Sample Proportions Standard Error

	.. math::
	
		s_{\hat{p}_1 - \hat{p}_2} = \sqrt{ \frac{ \hat{p}_1 \cdot (1-\hat{p}_1) }{n_1} + \frac{ \hat{p}_2 \cdot (1-\hat{p}_2) }{n_2} }
		
TODO

Margin of Error
---------------

TODO

Intervals
---------

TODO


Population Mean
===============
		
Standard Error
--------------

.. topic:: Sample Mean Standard Error

	.. math::
	
		\text{s}_{\bar{x}} = \frac{s}{\sqrt{n}}
	
Difference of Two Means
***********************

.. topic:: Difference of Means Standard Error

	.. math::
	
		\text{s}_{\bar{x_2}_2 - \bar{x_1}} = \sqrt{ \frac{ s_{ \bar{x_1} } }{n_1} + \frac{ s_{ \bar{x_2}} }{n_2} }

Margin of Error
--------------

.. topic:: Population Mean Margin of Error, Known Standard Deviation

	.. math::
	
		\text{MOE} = \lvert z_{1-\frac{\alpha}{2}} \rvert \cdot s_{\bar{x}}

.. topic:: Population Mean Margin of Error, Unknown Standard Deviation

	.. math::
	
		\text{MOE} = \lvert t_{1-\frac{\alpha}{2}} \rvert \cdot s_{\bar{x}}
TODO

Intervals
---------

.. topic:: Confidence Interval For Population Mean

	.. math::
	
		\bar{x} - \text{MOE} \leq \mu \leq \bar{x} + \text{MOE}

TODO 

Difference of Two Means
***********************

TODO 

.. topic:: Confidence Interval for Difference of Population Means

	.. math::
	
		(\bar{x_2} - \bar{x_1}) - \text{MOE} \leq \mu_2 - \mu_1 \leq (\bar{x_2} - \bar{x_1}) + \text{MOE}

TODO
