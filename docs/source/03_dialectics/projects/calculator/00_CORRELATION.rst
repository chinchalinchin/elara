.. _calculator_project_one:

===========
Correlation
===========

.. epigraph::

	If, in an expression (whose content need not be a judgeable content), a simple or complex symbol occurs in one or more places, and we think of it as replaceable at all or some of its occurrences by another symbol (but everywhere by the same symbol), then we call the part of the expression that on this occasion appears invariant the function, and the replaceable part its argument.
	
	-- Gottlob Frege, Begriffsschrift

.. _calculator_project_one_instructions:

Instructions
============

1. Read the :ref:`calculator_project_one_background` section.

2. Read the :ref:`calculator_project_one_correlation_function` section. Follow along with the instructions in that section. Watch the accompanying video at the end of the section. Type each command as shown into your calculator to create the **CORREL** function. 

3. Read the :ref:`calculator_project_one_sse_function` section. Carefully read the **SSE** function requirements. Create the indicated function so that it fulfills the given requirements.

4. On the project due date, plug your calculator into the ViewSonic in the classroom and export your programs for grading. At the end of the project, you should have two functions **CORREL** and **SSE**. These functions must satisfy the requirements given in each of the sections below.

.. _calculator_project_one_background:

Background
==========

TODO

.. _calculator_project_one_ti_basic:

TI Basic
--------

TODO

.. _calculator_project_one_bivariate_statistics:

Bivariate Statistics
--------------------

TODO

.. _calculator_project_one_correlation:

Correlation
***********

TODO

.. math::

	r_{xy} = \frac{1}{n-1} sum^{n}_{i=1} z^{x}_i \cdot z^{y}_i
	
TODO

.. _calculator_project_one_sse:

SSE
***

TODO

.. math::

	SSE = sum^{n}_{i=1} (y_i - \hat{y_i})^2
	
TODO


.. _calculator_project_one_correlation_function:

Correlation Function
====================

TODO

.. _calculator_project_one_video:

Video
-----

The following video walks you through creating the **CORREL** function on your calculator.

.. image:: https://img.youtube.com/vi/6xtN2i2FbsQ/maxresdefault.jpg
	:alt: Correlation
	:target: https://www.youtube.com/watch?v=6xtN2i2FbsQ

.. _calculator_project_one_sse_function:

SSE Function
============

TODO

.. topic:: SSE Function Requirements

	1. The function should run the :ref:`calculator_linreq` program and store the line of best fit.
	
	2. The function should calculate the residuals of the stored Linear Regression model.
	
	3. The function should calculate the sum squared of the residuals.
	
	4. The function should display the results of the calculation back to the user in a readable format.
	
.. topic:: Extra Credit

	You have an opportunity to get 5% Extra Credit on your overall Project grade if your **SSE** function also accomplishes the following:
	
	1. The function prints SSR to screen in a readable format.
	
	2. The function prints SST to screen in a readable format.
	
	3. The function prints the coefficient of determination, :math:`R^2`, to screen.


