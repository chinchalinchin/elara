.. _project_eight:

======================
Monte Carlo Simulation
======================


.. epigraph::

	'Tis but fortune. All is fortune.

	-- William Shakespeare, The Twelfeth Night

*Monte Carlo Simulation* is a modelling technique from statistics with many applications in different fields. The essence of *Monte Carlo Simulation* lies in interpretting randomly generated numbers as outcomes in an experiment. In this project, we will take a look at several ways of using the interpretation of random numbers to model physical processes in order to estimate quantities of interest.

Instructions
============

1. Create a Python ``.py`` script named ``LASTNAME_FIRSTNAME_project_eight.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``LASTNAME`` and ``FIRSTNAME`` with your last and first name, respectively.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_eight_background` section.
5. Perform all exercises and answer all questions in the :ref:`project_eight_project` section. Label your script with comments as indicated in the instructions of each problem.
6. When you are done, zip your script **and** the *csv* file in a zip file named ``LASTNAME_FIRSTNAME_project_eight.zip``
7. Upload the zip file to the Google Classroom Project Four Assignment.


.. _project_eight_background:

Background
==========
 
Integration
-----------

In calculus, *integration* is a technique for finding the area under a curve :math:`f(x)`. *Monte Carlo Simulation* gives us an alternative way of approaching the same set of problems. According to the :ref:`classical_definition`,

.. math::

	P(A) = \frac{n(A)}{n(S)}
	
Where :math:`n(A)` is the total number of outcomes that belong to the event :math:`A` and :math:`n(S)` is the total number of outcomes in the entire *sample space*. This definition applies to *discrete* events. When the events in question are continuous, we adjust the interpretation of :math:`n(A)` to mean the relative *area* of the event :math:`A` as compared to the area of the total sample space :math:`n(S)`. 

By simulating all the outcomes in :math:`S` and determining which belong to :math:`A`, we can estimate the *area* of the event :math:`A`. This simple idea underlies everything that follows.

Estimating Pi
*************

To see this technique in action, let's look at a simple example. Consider a cirlce inscribed in a square of with a side of length 1, centered at the origin :math:`(0,0)`.

TODO

Due to the Law of Large Numbers, as the number of simulations increases, the approximation of :math:`\pi` converges to its true value. 

.. image:: ../../../assets/imgs/python/monte_carlo_pi_100.png
    :align: center
   
.. image:: ../../../assets/imgs/python/monte_carlo_pi_1000.png
    :align: center
    
.. image:: ../../../assets/imgs/python/monte_carlo_pi_10000.png
    :align: center
    

Areas Under Curves
******************

The same technique used to estimate :math:`\pi` can be applied to an arbitrary curve :math:`f(x)`. Take the example of the following linear function on the interval :math:`[0,1]`,

.. math::

	f(x) = 0.5 \cdot x
	
(TODO: insert picture)

From the graph, we see the area can be calculated using the formula for the area of a triangle. The base of the triangle is :math:`1` and the height of the triangle is :math:`\frac{1}{2}`, which leads to an exact area of,

.. math::

	A = \frac{1}{2} \cdot b \cdot h = 0.25
	
Let us apply the technique of Monte Carlo integration to see how we can use random number generation to approximate this value. While this simple example can be calculated exactly using geometrical arguments, the area under the curve of more complicated function is not so easily determined; the universality of Monte Carlo integration can nevertheless be applied to an arbitrary curve without alteration.

TODO

.. _project_eight_project:

Project
=======

TODO 

1. Use Monte Carlo Integration to estimate the area under the curve :math:`f(x) = x^2` from :math:`x = 0` to :math:`x = 1`.

a. The actual value of the area is :math:`\frac{1}{3}`. About how many simulations do you have to perform in order to get within two decimal places of accuracy?


2. Use Monte Carlo Integration to estimate the area under the curve :math:`f(x) = e^x` from :math:`x = 0` to :math:`x = 1`.

a. The actual value of the area is :math:`e - 1`. About how many simulations do you have to perform in order to get within two decimal places of accuracy?


3. Use Monte Carlo Integration to estimate the area under the curve :math:`f(z) = \frac{1}{sqrt{2 \pi}} \cdot e^(-z^2)` from :math:`z = -3` to :math:`z = 3` 

.. hint::

	This function is the Standard Normal density function! Think about what the empirical rule says about the percentage of the distribution that is contained in the interval :math:`[-3, 3]`.
	
a. The actual value of this area is :math:`0.9973000656`. About how many simulation do you have to perform in order to get within two decimal places of accuracy? 

