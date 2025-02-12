.. _linear_regression:

=================
Linear Regression
=================

*Linear Regression* is a technique for leveraging the linear correlation that exists between two variables; It uses the information available in one variable to help predict the value of the other variable. The variable used to predict is called the *predictor* variable and is typically denoted :math:`x_i`. The variable whose value is being predicted is called the *response* variable and is typically denoted :math:`y_i`.

The objective to *Linear Regression* is to fit a *model* :math:`\hat{y}` that describes the dependence the :math:`y_i` variable has on the :math:`x_i`. The *model* :math:`\hat{y}` will be used to make predictions for given values of :math:`x_i`. The predicted value of :math:`y_i` given :math:`x_i` will be denoted :math:`\hat{y_i}`. 

.. note::

	:math:`\hat{y}` is a linear *function*. :math:`\hat{y_i}` is a point on the curve on :math:`\hat{y}`. (If one were committed to the purity of symbols, :math:`\hat{y_i}` would represent the y-value of a point; but implicit in the subscript notation is its mapping to a corresponding :math:`x_i` value.) 

In order to find a good model, the concept of *model error* will be concentrated in the definition of a *residual*,

.. math::

	\varepsilon_i = y_i - \hat{y_i}	
	
This quantity will provide a metric for validating models against observed data.

TODO

.. _regression_model:

Regression Model
================

TODO

The Linear Regression Model is specified by two equations. The first equation parameterizes the *predicted* value of :math:`y_i` given :math:`x_i`, :math:`\hat{y_i}`. The second equation describes the distribution of *error terms* as the difference of *actual* values and *predicted values*.

.. topic:: Regression Model, Part 1: Predictions

	.. math::
	
		\hat{y_i} = \mathcal{B}_1 \cdot x_i + \mathcal{B}_0
    
.. topic:: Regressio Model, Part 2: Error

	.. math::
	
		y_i = \hat{y_i} + \varepsilon_i

The term :math:`\varepsilon_i` is a normally distributed error term centered around 0 with a variance equal to the **mean squared error** of the model,

.. math::

    \varepsilon_i \sim \mathcal{N}(0, \sqrt{\text{MSE}})

TODO

.. topic:: Regression Model Assumptios

	1. TODO
	
	2. Residuals must be normally distributed.
	
	TODO
	
.. _mean_squared_error:

Mean Squared Error
==================

The term :math:`\hat{y}` is **not** the observed value of :math:`y` in the bivariate sample of data that was used to calibrate the model. It is the *predicted* value of :math:`y` given the *observed* value of :math:`x`. This is an *extremely* important point when talking about regression. The *model* equation is a *prediction*, and the prediction is not *exact*. Each *predicted value* of :math:`y`, :math:`\hat{y}`, will deviate from the *observed* value of :math:`y`. The deviation, if the model is a good fit, should be *normally distributed* around 0. 

TODO 

Sum Squared Error
-----------------

TODO 

.. math::

    \text{SSE} = \sum_{i=1}^{n} (\hat{y}_i - y_i)^2

TODO

MSE: Mean Squared Error
-----------------------

TODO 

.. math::

    \text{MSE} = \frac{\sum_{i=1}^n (\hat{y}_i - y_i)^2}{n-2}

TODO 

TODO: degrees of freedom, two parameters in regression model, etc

Model Estimation
================

*Model-fitting* in the context of *Linear Regression* can be understood as the task of finding the values of the model coefficients, :math:`\mathcal{B}_0` and :math:`\mathcal{B}_1`, most appropriate to use in the Regression Equation, :math:`\hat{y}`.

Least Squares Estimation
------------------------

One of the most common and easily understood methods for estimating the value of the model coefficients is known as *Least Squares Estimation*. The reason for the name *Least Squares* will shortly be explained. In short, with this method, the Regression Model is estimated by finding the values of :math:`\mathcal{B}_0` and :math:`\mathcal{B}_1` that *minimize* the MSE of the model. 

The formulae that result from the application of this process are given directly in the following cards for reference. The logic and derivation of these formulae are the the topics of discussion in the next section. 

.. topic:: Slope Coefficient, :math:`\mathcal{B}_1`

	.. math::
	
		\mathcal{B}_1 = r_{xy} \cdot \frac{s_y}{s_x}
		
.. topic:: Intercept Coefficient, :math:`\mathcal{B}_0`

	.. math::
	 	
	 	\mathcal{B}_0 = \bar{y} - \mathcal{B}_1 \ cdot \bar{x}

TODO


TODO

Assessing Model Fit
===================

Regression is a not a one-stop shop; it is important to bear in mind the limitations of Regression. If the model assumptions are not met 
Residual Analysis
-----------------

TODO: distribution of residuals, normality assumption

Error Reduction
---------------
TODO

.. topic:: Total Variation

	.. math::
	
		\text{SST} = \sum^{n}_{i=1} (y_i - \bar{y})^2
		
TODO

.. topic:: Explained Variation

	.. math::
	
		\text{SSR} = \sum^{n}_{i=1} (\hat{y_i} - \bar{y})^2

TODO

.. topic:: Unexplained Variation

	.. math::
	
		\text{SSE} = \sum{n}_{i=1} (y_i - \hat{y_i})^2
		
TODO		

Coefficient of Determination
----------------------------

TODO

.. topic:: Regression Error

	.. math:: 
	
		\text{SST} = \text{SSE} + \text{SSR}
		
TODO

