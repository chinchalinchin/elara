.. _point-estimation:

================
Point Estimation
================

A sample of data is characterized numerically by *point estimates* of *sample statistics*.

Motivation
==========

In the first few sections, we discussed the idea of *drawing a sample* and using it to make inferences about the *population* . Now we begin the study of how to apply these ideas quantitatively and make them more exact.

We want to know the *parameters* of a population, but we do not have the entire population on hand to determine the values of these *parameters*. So, we *sample* the population and then calculate *point estimates*. *Point estimates* are *sample statistics* that represent our best guess of the *true* value of population *parameters*.

For example, in this section, we will introduce the idea of the *sample mean*, :math:`\bar{x}`. The *sample mean* is a *sample statistic*; It is an *estimate*. This in contrast to the *population mean*, :math:`\mu`, the *true* value of :math:`\bar{x}` we would get if we had access to entire population.

In general, as we move through this section, keep in mind the following table,

+----------------------+------------------+
| Population Parameter | Sample Statistic |
+----------------------+------------------+
| :math:`\mu`          | :math:`\bar{x}`  |
+----------------------+------------------+
| :math:`\sigma`       | :math:`s`        |
+----------------------+------------------+

The left hand column of this table represents the *true* value of a quantity that describes the population *distribution*. The right hand column represents the *estimated* value of this quantity as derived from the sample *distribution*.

As we go through this section, keep in mind all the point estimators we introduce are sample statistics, not population parameters. In general, the population paramter is *never* known. We must always *estimate* its value.

.. topic:: Population Parameter

	The true value of a population characteristic.
	
.. topic:: Sample Statistic

	An estimated value of a population characteristic calculated from a sample of the population.
	
	
Definitions
===========

.. _observation:

Observation
-----------

Symbolic Expression
    :math:`x_i`

Definition
    An :ref:`individual`; A single piece of data. 
    
The subscript *i* is called the *index* of the observation. If the sample is ordered, the *index* corresponds to the order in which the observation was made, i.e. :math:`x_1` is the first observation, :math:`x_2` is the second observation, etc. 

.. _sample:

Sample
------

Symbolic Expression 
    :math:`S = \{ x_1, x_2, ..., x_{n-1}, x_n \}`

Definition 
    A collection, or :ref:`set <set_theory>`, of observations. 
    
The number of samples, *n*, is called the *sample size*.

.. _frequency:

Frequency
---------

Symbolic Expression
    :math:`f(x_i)`

Definition
    The number of times a particular observation :math:`x_i` occurs in a sample of data.

.. _relative-frequency:

Relative Frequency
------------------

Symbolic Expression
    :math:`p(x_i)`

Definition
    The *percentage* of times a particular observation :math:`x_i` occurs in a sample of data.

Note by definition, in a sample of *n* observations,

.. math::

    p(x_i) = \frac{f(x_i)}{n}

.. _cumulative-frequency:

Cumulative Frequency 
--------------------

Symbolic Expression 
    :math:`F(x_i)`

Definition
    The number of times an observation *less than of equal to* :math:`x_i` occurs in a sample of data.

Note the relation between *frequency* and *cumulative frequency*,

.. math::

    F(x_i) = \sum^{i}_{j = 1} f(x_j)

.. important:: 

    Take note of the indices on the summation. The sum starts at the first observation and goes all the way up to the :math:`i^{\text{th}}` observation.

Also note by definition,

.. math::

    F( max(S) ) = n

.. _cumulative-relative-frequency:

Cumulative Relative Frequency 
-----------------------------

Symbolic Expression 
    :math:`P(x_i)`

Definition
    The percentage of times an observation *less than of equal to* :math:`x_i` occurs in a sample of data.

Note the relation between *relative frequency* and *cumulative relative frequency*,

.. math::

    P(x_i) = \sum^{i}_{j = 1} p(x_j)

.. important:: 

    Take note of the indices on the summation. The sum starts at the first observation and goes all the way up to the :math:`i^{\text{th}}` observation.

Another important relation to remember is the relative between *cumulative frequency* and *cumulative relative frequency*,

.. math:: 
    
    F(x_i) = \frac{P(x_i)}{n}

Also note by definition,

.. math::

    P( max(S) ) = 1

.. _joint-frequency:

Joint Frequency
---------------

Symbolic Expression 
    :math:`f(x_i \cap y_i)`

Definition
    The number of times a bivariate observation :math:`(x_i, y_i)` occurs in a sample of data.

.. important::

    The joint frequency is only defined when the sample is *bivariate*. 

Conditional Relative Frequency
------------------------------

Symbolic Expression
    :math:`P(x_i | y_i)`

Definition 
    The proportion of times the outcomes :math:`x_i` **and** :math:`y_i` are observed as compared to the number of times the outcome :math:`y_i` is observed alone. 

By definition,

.. math::

    P(x_i | y_i) = \frac{n(x_i \cap y_i)}{n(y_i)}

.. important::

    Conditional frequencies are *always* relative. 

.. _minimum:

Minimum
-------

Symbolic Expression 
    :math:`min(\{ x_i \})`

    :math:`min(S)`
    
    :math:`x_{min}`

Definition
    The smallest value in a sample of observations.

.. _maximum:

Maximum
-------

Symbolic Expression 
    :math:`max(\{ x_i \})`

    :math:`max(S)`

    :math:`x_{max}`

Definition
    The largest value in a sample of observations

.. _outliers:

Outliers
--------

Definition
    An unusual observation.

What we mean by "*unusual*" depends on the data. Generally speaking, we mean something that roughly approximates, "*a data that is far outside what is expected*".

If we are measuring :ref:`numerical data <data_characteristic>`, this might mean an observation that is much, much greater than or much, much less than the majority of the data. 

If we are measuring :ref:`categorical data <data_characteristic>`, this might mean an observation is in infrequent.

.. _floor-function:

Floor Function 
--------------

Symbolic Expression
    .. math::

        \lfloor x \rfloor

Definition
    The *floor function* returns the integer-valued part of a number. In other words, it removes the decimal from a number.


Example
    .. math::

        \lfloor 4.5 \rfloor = 4

.. _ceiling-function:

Ceiling Function
----------------

Symbolic Expression 
    .. math::

        \lceil x \rceil 

Definition 
    The *ceiling* returns the next largest integer. In other words, it always rounds *up*.


Example 
    .. math::

        \lceil 4.5 \rceil = 5

.. _measures-of-centrality:

Measures of Centrality 
======================

*Measures of centrality*, sometimes known as *measures of central tendency*, describe *where* the "*center*" of a sample of data is located. What we mean by "*center*" is, in some sense, left to the reader's intuition. A good analogy for the statistical conception of *centrality* comes from the field of physics: the idea of `center of mass <https://en.wikipedia.org/wiki/Center_of_mass>`_. The *center of mass* is the *balance point*, the point around which a body of mass is distributed so the torque generated by gravity is held is equilibrium. In this analogy, the *mass* is the *sample of data*. *Centrality* in a *sample* is a measure of its "*center of mass*", so to speak.  

.. _arithmetic-mean:

Arithmetic Mean
---------------

The *arithmetic* mean is a sample statistic you have probably seen before; what you probably didn't know is it is not the *only* way of calculating the mean. You will see in the next few sections alternate ways of calculating a quantity that is meant to represent the *mean* of a sample. Each of these *sample statistics* represents a way of quantifying the notion of "*central tendency*"

Before getting to the good stuff, let's review the *arithmetic* mean. There are two equivalent ways of defining the *sample mean*. 

.. _sample-mean-formula:

Sample Formula
**************

If the sample of data is specified as a set or list of data as in the following, 

.. math:: 

    S = \{ x_1, x_2, ... , x_n \}

Then the sample arithmetic mean can be calculated with the formula,

.. math::

    \bar{x}_A = \frac{\sum_{1}^n x_i}{n}

This is known as the *sample mean formula* for the arithmetic mean.

Example
    Suppose you survey 10 people and ask them how many of the 11 full-length, major motion picture *Star Wars* movies they have seen. Suppose the sample **S** of their responses is given below,

    .. math::
    
        S = \{ 6, 7, 9, 0, 1, 0, 3, 6, 3, 9 \}

    Find the average number of *Star Wars* movies seen by this sample of people.

Applying the *sample mean formula*,
    
.. math::

    \bar{x}_A = \frac{6 + 7 + 9 + 0 + 1 + 0 + 3 + 6 + 3 + 9}{10} = 4.4 \text{ movies}

.. note::
    
    Notice in this example the *sample mean* does **not** correspond to an observable value in the sample. 
    
    The *sample mean* is not even a *possible value* of an individual observation in this sample (unless we allow for people who stopped watching half-way through one of the movies).

Interlude
*********

Suppose in a sample of data **S**, some of the observations have identical values, such as in the following dataset that represents the age in years of an A.P Statistics student,

    S = \{ 16, 16, 17, 18, 16, 17, 17, 17 \}

Before moving on to calculate the sample mean, let us represent this sample **S** in an equivalent way using a table,

+--------------+----------------+
|  :math:`x_i` | :math:`f(x_i)` |
+--------------+----------------+
|      16      |       3        |
+--------------+----------------+
|      17      |       4        |
+--------------+----------------+
|      18      |       1        |
+--------------+----------------+

This way of representing a sample of data, where the first column stands for the value of the observation and the second column that stands for the frequency of that observation, is known as a :ref:`frequency-distributions`. 

(We will study *frequency distributions* in more detail in the :ref:`next section <graphical-representations-of-data>`.)

Let us move on to the task at hand: calculating the sample mean. In this case, the formula for the arithmetic mean gives,

.. math:: 

    \bar{x}_A = \frac{16 + 16 + 17 + 18 + 16 + 17 + 17 + 17}{8}

If we collect all the terms in the numerator that are *like*, we may rewrite this as,

.. math::

    \bar{x}_A = \frac{3 \cdot 16 + 4 \cdot 17 + 1 \cdot 18}{8}

Notice the first factor of each term in the numerator is simply frequency of that observation in the *frequency distribution* table, whereas the second factor is the actual value of the observation. In other words, each term of the numerator is of the form,

.. math::

    x_i \cdot f(x_i)

This recognization leads the following formula that comes in handy when sample distributions are given in terms of :ref:`frequency distributions <frequency-distributions>`

.. _sample-mean-frequency-formula:

Frequency Formula
*****************

If the sample of data is specified as a frequency distribution as in the following,

+-------------+-------------------+
|     x       |      f(x)         |
+=============+===================+
|  x :sub:`0` |   f( x :sub:`0`)  |
+-------------+-------------------+
|  x :sub:`1` |   f( x :sub:`1`)  |
+-------------+-------------------+
|  ...        |  ...              |
+-------------+-------------------+
|  x :sub:`n` |   f( x :sub:`n`)  |
+-------------+-------------------+

Then the sample arithmetic mean can be calculated with the formula, 

.. math::

    \bar{x}_A = \sum_{i}^n x_i \cdot f(x_i)

Example
    
    	Taking the same example from the previous section, we had a sample of responses to the question of how many of *Star Wars* movies a group of people had seen,
    	
    	.. math::
    		
        	S = \{ 6, 7, 9, 0, 1, 0, 3, 6, 3, 9 \}
        	
        Use the frequency sample mean formula to find the sample mean of this data.

We summarize the sample with a :ref:`ungrouped-frequency-distributions`, adding a column to it that represents the *product* of the first two columns,

+--------------+----------------+--------------------------+
|  :math:`x_i` | :math:`f(x_i)` | :math:`x_i \cdot f(x_i)` |
+--------------+----------------+--------------------------+
|     0        |       2        |            0             |
+--------------+----------------+--------------------------+
|     1        |       1        |            1             |
+--------------+----------------+--------------------------+
|     2        |       0        |            0             |
+--------------+----------------+--------------------------+
|     3        |       2        |            6             |
+--------------+----------------+--------------------------+
|     4        |       0        |            0             |
+--------------+----------------+--------------------------+
|     5        |       0        |            0             |
+--------------+----------------+--------------------------+
|     6        |       2        |            12            |
+--------------+----------------+--------------------------+
|     7        |       1        |            7             |
+--------------+----------------+--------------------------+
|     8        |       0        |            0             |
+--------------+----------------+--------------------------+
|     9        |       2        |            18            |
+--------------+----------------+--------------------------+

Where we have included all possible observation values, even those that do not occur in the sample of data. 

Take note, summarized in this way, the third column makes it apparent that observations with higher values, the ``9`` and ``6`` in this sample, while having the sample frequency as lower values like ``3`` and ``0``, contribute greater *weight* to the sample mean calculation. This property of the mean will appear in a different form when we talk about the effects of :ref:`skewness` in a few sections.

To find the sample mean here, we average the values of the third column,

.. math::

	\bar{x} = \frac{1 + 6 + 12 + 7 + 18 }{10} = 4.4 \text{ movies}

This idea, that the product of the observation and its frequency represent the *weight* of an observed value in the calculation of the sample mean leads directly to the next section.

.. _weighted-mean:

Weighted Mean
*************

If the sample is broken up into groups, then the mean of the overall sample can be computed by weighting the mean of each group by the proportion of the overall sample it represents.

Example
    The following datasets represent the heights (in feet) of male and female students in a statistics class,

    .. math::

        S_{\text{male}} = \{ 5.8 \text{ ft}, 5.7 \text{ ft}, 5.9 \text{ ft}, 6.1 \text{ ft}, 5.6 \text{ ft}\}

    .. math:: 

        S_{\text{female}} = \{ 5.9 \text{ ft}, 5.6 \text{ ft}, 5.4 \text{ ft}, 5.5 \text{ ft}, 5.6 \text{ ft} \} 

    Find the average height of all students in this class.

The sample is broken into 2 groups here, whereas the question is asking for the mean of the entire sample. We *could* merge the two samples into one giant sample,

.. math:: 

        S = \{ 5.8 \text{ ft}, 5.7 \text{ ft}, 5.9 \text{ ft}, 5.9 \text{ ft}, 5.6 \text{ ft}, 5.5 \text{ ft}, 5.9 \text{ ft}, 5.6 \text{ ft}, 5.4 \text{ ft}, 5.5 \text{ ft}, 5.6 \text{ ft}, 5.7 \text{ ft} \} 

And then calculate the sample mean directly, but there is an alternate approach here that is easier. We can first find the mean of each group,

.. math:: 

    \bar{x_{\text{male}}} = \frac{ 5.8 \text{ ft} + 5.7 \text{ ft} + 5.9 \text{ ft} + 6.1 \text{ ft} + 5.6 \text{ ft}}{5} = 5.82 \text{ ft}

.. math:: 

    \bar{x_{\text{female}}} = \frac{ 5.9 \text{ ft} + 5.6 \text{ ft} + 5.4 \text{ ft} + 5.5 \text{ ft}}{5} = 5.6 \text{ ft}

Then we find the *weight* :math:`w_j` of the male and female groups. The weight is simply the ratio of samples in a group to the total number of samples,

.. math:: 
    w_j = \frac{n(\{ x_j \})}{n}

.. note:: 

    We are using :ref:`set theoretic <set_theory>` notation here that we have not yet introduced formally. Nevertheless, the meaning of this equation should be intuitive. It represents the fraction of the sample that belongs to the given group.

The number of males in this sample is 5 and the number of females in this sample is 4. Thus,

.. math:: 

    w_{\text{male}} = \frac{5}{9}


.. math:: 
    
    w_{\text{female}} = \frac{4}{9}

Then, the overall mean of the sample can be calculated by *weighting* each mean of the sample groups,

.. math:: 

    \bar{x} = w_{\text{male}} \cdot \bar{x_{\text{male}}} + w_{\text{female}} \cdot \bar{x_{\text{female}}}

.. math:: 

    \implies = \frac{5}{9} \cdot 5.82 \text{ ft} + \frac{4}{9} \cdot 5.6 \text{ ft} \approx 5.72 \text{ ft}

Note, this agrees with first method we discussed in this section, namely calculating the mean directly from a merged sample,

.. math:: 

    \bar{x} = \frac{5.8 \text{ ft} + 5.7 \text{ ft} + 5.9 \text{ ft} + 6.1 \text{ ft} + 5.6 \text{ ft} + 5.9 \text{ ft} + 5.6 \text{ ft} + 5.4 \text{ ft} + 5.5 \text{ ft}}{9}

.. math:: 

    \implies \approx 5.72 \text{ ft}

.. _weighted-mean-formula:

Formula
*******

.. important::

	We are dropping the *A* subscript from the sample mean formula in this section to provide a confusion of superscripts and subscripts. Keep in mind, even though it is not explicitly written, the sample means in this section refer to the *arithmetic* sample mean.
	
Suppose a sample of data **S** with *n* observations has been broken up into *m* groups, 

.. math::

	S_j = \{ x^{j}_i \}

For :math:`j = 0, 1, 2, ..., m`. Note, by definition, 

.. math::

	\sum_{j=1}^m n(S_j) = n

.. important::

	Pay careful attention to the indices of the summation here. We are summing over the number of *groups*, **not** the number of observations. 
	
If these conditions are met, then we can calculate the sample mean of **S** as the weighted sum of each sub-sample :math:`S_j`,

.. math:: 

    	\bar{x} = \sum_{j}^m \bar{x^{j}_i} \cdot w_j

Where the weight :math:`w_j` is the proportion of observations that belong to group :math:`j`,

.. math:: 

    	w_j = \frac{n(S_j)}{n}
    
Note, by definitions, the weights must sum to 1,

.. math::
	
	
	\sum_{j=1}^{m} w_j = 1
	
Or equivalently, the sum of the number of observations in each sub-sample must equal the total amount of observations in the entire sample,

.. math::

	\sum_{j=1}^{m} n( \{ x^{j}_i \}) 	

Example
    Suppose you have samples of test scores from three different classes of A.P. Statistics students,
    
    .. math::
    	
    	S_1 = \{ 95, 98, 75, 88 \}
    	
    .. math::
    
    	S_2 = \{ 70, 75, 76 \}
    	
    .. math::
    
    	S_3 = \{ 81, 79, 83 \}
    	
    Find the sample of mean of all three classes.

Here we have three groups :math:`j = 1, 2, 3`. 

We first find the weights of each sample group. 

The first sample has :math:`n_1 = 4`, the second sample has :math:`n_2 = 3` and the third sample has :math:`n_3 = 3`, thus we have,

.. math::

	n = n_1 + n_2 + n_3
	
.. math::
	
	n = 4 + 3 + 3 = 10
	
We find the weight of each sub-sample by finding the proportion of the entire sample that belongs it,

.. math::

	S_1 = \frac{4}{10} = 0.40
	
.. math::

	S_2 = \frac{3}{10} = 0.30
	
.. math::

	S_3 = \frac{3}{10} = 0.30

Next we find the sample mean of each sub-sample,

.. math::

	\bar{x^{1}} = \frac{95 + 98 + 75 + 88}{4} = 89.0
	
.. math::

	\bar{x^{2}} = \frac{70 + 75 + 76}{3} \approx 73.67
	
.. math::

	\bar{x^{3}} = \frac{81 + 79 + 83}{3} = 81.0
	
Then, we can find the overall mean by *weighting* each sub-sample mean,

.. math::

	\bar{x} = \frac{4}{10} \cdot 89.0 + \frac{3}{10} \cdot 73.67 + \frac{3}{10} \cdot 81.0 = 82.0

Which may also be verified by calcualting the sample mean from the entire sample directly,

.. math:: 

	\bar{x} = \frac{95 + 98 + 75 + 88 + 70 + 75 + 76 + 81 + 79 + 83}{10} = 82.0
 	
.. _geometric-mean:

Geometric Mean
--------------

Let us consider *why* the arithmetic mean yields a measure of centrality. From the prior discussion of the weighted mean, it is apparent the sample mean formula is a measure of the *additive* center of a sample. We take *n* data points, add them up (perform *n* operations) and then divide by *n* (average). Each observation contributes its *weight* by adding to the total in the numerator of the arithmetic mean formula. Observations with more *weight* (higher values) contribute more heavily to the overall value of the arithmetic mean.

There are, however, other ways of characterizing the *center* of a sample of data with other types of *sample statistics*. 

The *geometric mean* is such an alternate way of defining the *mean* of a sample data. 

The *geometric mean* is defined as,

.. math::
    \bar{x}_G = (x_1 \cdot x_2 \cdot ... \cdot x_{n-1} \cdot x_n )^(\frac{1}{n})

The *geometric mean* is a measure of a sample's *multiplicative* center, rather than its *additive* center. 

Example
	Suppose you have a sample of data,
	
	.. math::
	
		S = \{ 10, 12, 14 \}
		
	Find the arithmetic sample mean and geometric sample mean. Compare and contrast their values.
	
First, let's start with what we know, the arithmetic mean,

.. math::

	\bar{x}_A = \frac{10 + 12 + 14}{3} = 12
	
Simple enough. Now let's try the *geometric sample mean*. In order to calculate the geometric mean, we *multiply* all of the observations rather than add them up. Then, to average a product, rather than dividing by the total number of observations, we take the n :sup:`th` root of the product,

.. math::

	\bar{x}_G = (10 \cdot 12 \cdot 14)^{\frac{1}{3}} \approx 11.89

Notice: the geometric mean is *less* than the arithmetic mean.

.. _geometric-vs-arithmetic-mean:

Geometric vs. Arithmetic Mean
*****************************

So, which point estimate of centrality do we use? The arithmetic mean or the geometric mean?

There are several reasons to prefer the arithmetic mean. Perhaps the simplest to understand at this point in your study of statistics is its simplicity: it is easy to calculate and easy to interpret. 

The geometric mean, on the other hand, is not *as* easy to calculate. 

Beyond that, there are more philosophical reasons for preferring the arithmetic mean over the geometric mean. These reasons we are not yet ready to discuss, as they require a deeper understanding of probability, :ref:`random_variables` and :ref:`central_limit_theorem`. Suffice to say, the arithmetic mean has very nice properties that lend themselves to statistical inference easier than the geometric mean do. 

The Moral of the Story
**********************

There are other variants of the *mean* that sometimes appear in the literature. For example, when dealing with certain types of data, the `harmonic mean <https://en.wikipedia.org/wiki/Harmonic_mean>`_ is often the most appropriate measure for *central tendency*. 

We talk about these other variants only to make you aware of them. In this class, we will exclusively be dealing with the *arithmetic mean*.

Nevertheless, before moving on, there is an important point to make: *central tendency* is not an absolute measure of a sample; its value depends on the *way* we calculate it. 

This feature of statistics may be surprising. The amount of choice we have in *how* we go about measuing the population from a sample of data may seem as if it should not lead to a rigorous and well defined branch of mathematics.

It is true the choice we make between using the geometric mean and the arithmetic mean is to some extent arbitrary; there is not a particularly good reason for preferring one over the other, besides convention (and certain other properties that make calculations easier, as we shall see in later chapters). It is not important which one we choose; it is only important *that* we choose one and stick with it.

One of the key idea of statistics is, not that we should *rid* ourselves of assumptions and biases (an impossible task), but that we should be *aware* of our assumptions and biases. Otherwise, without awareness, those assumptions and biases may show up and influence the data.

Categorical Measures
--------------------

The :ref:`arithmetic-mean` and the :ref:`geometric-mean` only apply if the data being measured is :ref:`quantitative data <data-characteristic>`. If, however, the data being measured is categorical is nature, we do not have these tools available to us. Instead, we use the next two measures of central tendency to get a picture of the distribution shape.

.. _mode:

Mode
****

Definition
    The *mode* is the most frequent of observation in a sample of data.

Sample Proportion
*****************

Definition
    .. math::

        \hat{p} = \frac{f(x_i)}{n}

The sample proportion is the ratio of the number of individuals in the sample that share a certain property to the total number of individuals in the sample. In other words, it is the frequency of an observation divided by the the number of observations.

.. _measures-of-location:

Measures of Location
====================

.. important:: 

    Your book does not do a good job of covering this topic. 

In the :ref:`measures_of_centrality`, we drew the analogy between mass and a sample. Specifically, we proposed the following relation,

    Center of mass is to matter as measures of centrality are to a sample of data.

Extending the analogy, the center of mass is not enough to specify the *distribution of mass* in a body. We also need information about the volume (e.g. :math:`cm^3`) enclosed by the body and the density of the matter (e.g. :math:`\frac{gm}{cm^3}`) it contains.

Likewise, *measures of centrality* do not tell us the whole story about a sample. We need additional information in order to get a clearer picture of the distribution of data. *Measures of location* are a type of sample statistics that provide this information.

Order Statistics
----------------

An *order* statistic gives you information about the *ordinality* of a sample. The term "*ordinality*" refers to the *structural* or *sequential* nature of a sample. 

To see what is meant by the term *ordinality*, suppose you have a sample of :ref:`quantiative data <data-characteristic>` :math:`\{ x_i \}`,

.. math:: 

    S = \{ x_1, x_2, ..., x_i, ... , x_n \}

The *m* :sup:`th` order statistic, :math:`x_{(m)}` is the *m* :sup:`th` observation in the ordered sample :math:`S_{(o)}`,

.. math:: 

    S_{(o)} = \{ x_{(1)}, x_{(2)}, ... x_{(m)}, ..., x_{(n)} \}

After the data set is sorted, the new index (subscript) ``(m)`` attached to the observation is called the *order* of the observation. 

Example
    Suppose you measure the lifetime of a sample of batteries in years. You obtain the following result,

    .. math::

        S = \{ 5.1 \text{ years }, 3.2 \text{ years }, 6.7 \text{ years }, 1.4 \text{ years } \}


Then the ordered sample :math:`S_{(o)}` is given

.. math:: 

    S_{(o)} = \{ 1.4 \text{ years }, 3.3 \text{ years }, 5.1 \text{ years }, 6.7 \text{ years } \}

The 1 :sup:`st` *order statistic* :math:`x_{(1)}` is *1.4 years*, the 2 :sup:`nd` *order statistic* :math:`x_{(2)}` is *3.3 years*, the 3 :sup:`rd` *order statistic* :math:`x_{(3)}` is *5.1 years* and the 4 :sup:`th` *order statistic* :math:`x_{(4)}` is *6.7 years*. Another way of saying this would be the *order* of *1.4 years* is 1, the *order* of *3.3 years* is 2, the *order* of *5.1 years* is 3 and the *order* of *6 years* is 4. 

*Order statistics* are important because they allows us to define more complex statistics in a precise manner. 

.. _range:

Range
*****
*****

The range is a measure of the *total variation* of a sample of data.

Definition
    The *range* of a sample of data :math:`\{ x_1, x_2, ..., x_n \}` is the difference between its last order statistic, :math:`x_{(n)},` and its first order statistic, :math:`x_{(1)}` 

    .. math::

        \text{Range}(\{ x_i \}) = x_{(n)} - x_{(1)}

.. _percentile:

Percentile
**********
**********

.. _order-statistics: 

Motivation
**********

The :math:`(p \cdot 100 \%)^{\text{th}}` *percentile* roughly means the observation in a sample with :math:`(p \cdot 100 \%)` percent of the distribution below its value. 

.. note:: 

    *p* is a fraction, i.e. :math:`0<= p <=1`.

You have probably encountered the concept of *percentiles* at some point in other classes and have developed an idea of what they represent. Teachers often express quiz and test scores in terms of percentiles to give students a sense of how they are doing relative to the rest of the class. 

The meaning of a percentile should be intuitive and straight-forward; it is a measure of *how much* of a distribution lies below a given observation. The preliminary definition of a *percentile* conforms to this intuition,

Preliminary Definition 
    If a sample of data has been ordered from lowest value to highest value, then the :math:`(p \cdot 100 \%)^{\text{th}}`:sup:`th` percentile of the sample is the observation such that :math:`(p \cdot 100 \%)` percent of the sample is less than or equal that value.

From this definition, it should be clear *percentiles* only have meaning with respect to :ref:`quantitative data <data_characteristic>`. To *order* a sample of data :math:`\{ x_i \}`, the relation :math:`x_{i-1} < x_i` must have meaning. 

*Order statistics* give us a way to precisely define a percentile. *Order statistics* divide the interval on which the sample is measured into :math:`n+1` intervals, pictured below,

.. image:: ../../_static/img/mathematics/statistics/order_statistics.jpg
    :align: center

Note all of the intervals are *below* the order statistic except the last one, which is *above* its order statistic. Hence :math:`n+1`.

The number of such intervals below a given order statistic is *equal to* to the *order* of that observation. In other words, the fraction of intervals below the *m* :sup:`th` order statistic is given by,

.. math:: 

    p = \frac{m}{n+1}

*p* represents the percent of the intervals below the *m* :sup:`th` order statistic. The *order m* of the observation which corresponds to the :math:`(p \cdot 100 \%)^{\text{th}}` percentile can be found by solving for *m*,

Formula
    .. math::

        m = p \cdot (n+1)

We denote the order statistic :math:`x_{(m)}` which satisfies this formula as the :math:`\pi_p` percentile,

.. math:: 

    \pi_p = x_{(m)}

Example
    Suppose you were conducting a study to determine how many minutes late or early the average city bus arrived versus its scheduled time. You obtained the following data set, measured in minutes, 

    .. math::

        S = \{ 6.5 \text{ min }, -2.5 \text{ min }, 4.3 \text{ min }, 0.5 \text{ min }, 7.0 \text{ min }, -1.0 \text{ min }, 5.0 \text{ min }, 3.0 \text{ min }, -1.5 \text{ mi n} \}

    Find the following percentiles: 20 :sup:`th` and 50 :sup:`th`

Note in this sample we have :math:`n = 9` total samples.

Before we move onto solving the problem, consider a scatter plot of these observations against their observation order,

.. plot:: _plots/examples/03_ex01_unordered.py

To find the percentiles, we need to find the *order statistics*, i.e. we need to *order* the sample from lowest to highest,

.. math:: 

    S_{(o)}= \{ -2.5 \text{min}, -1.5 \text{min}, -1.0 \text{min}, 0.5 \text{min}, 3.0 \text{min}, 4.3 \text{min}, 5.0 \text{min}, 6.5 \text{min}, 7.0 \text{min} \}

Once ordered, we can plot the observations against their *rank order*,

.. plot:: _plots/examples/03_ex02_ordered.py
    
The previous two graphs should make clear the meaning of *order statistics*. To find the 20 :sup:`th` percentile, :math:`pi_{.20}`, we find the *order* in which it occurs in the sample,

.. math:: 

    m = 0.20 \cdot (9 + 1) = 2

This tells us the 20 :sup:`th` percentile is the second order statistic, or in this case ``-1.5`` minutes, i.e.,

.. math:: 

    \pi_{.20} = x_{(2)} = -1.5 \text{min}

Similarly, to find the 50 :sup:`th` percentile, we find the *order* in which it occurs in the sample,

.. math:: 
    
    m = 0.5 \cdot (9 + 1) = 5 

Which corresponds to the fifth order statistic, or in this case, ``3.0`` minutes,

.. math:: 

    \pi_p = x_{(5)} = 3.0 \text{min}

.. _percentile-interpolation:

Interpolation
*************

The previous example was contrived so the *order* of the sample percentile worked out to be a whole number, i.e. in both cases the formula :math:`m = (n+1) \cdot p` gave us an integer value. What happens things are not so simple?

Example
    Consider the same experiment of measuring bus waiting times, with the same sample data,

    .. math::

        S_{(o)}= \{ -2.5 \text{min}, -1.5 \text{min}, -1.0 \text{min}, 0.5 \text{min}, 3.0 \text{min}, 4.3 \text{min}, 5.0 \text{min}, 6.5 \text{min}, 7.0 \text{min} \}

    Find the following percentiles: 25 :sup:`th` percentile. 

When we try to apply the formula to determine the order statistic which corresponds to this percentile, we get,

.. math:: 

    m = 0.25 \cdot (9 + 1) = 2.5

There is no observation which corresponds to a fractional order. To estimate the percentile in this case, we use *linear interpolation*, using the *order* of the observation as the *x* variable and the value of the observation as the *y* variable. 


To do this, we take the order statistics on each side of :math:`m = 2.5`, in this case :math:`x_{(2)}` and :math:`x_{(3)}`, and find the slope of the line that connects them,

.. math:: 

    \text{slope} = \frac{x_{(3)} - x_{(2)}}{3-2} = x_{(3)} - x_{(2)}

Then we find the point on this line that corresponds to :math:`(2.5, x_{(2.5)})` (using the point-slope formula with the point :math:`(3, x_{(3)}` as the sample point!), which will serve as the estimate of the 25 :sup:`th` percentile,

.. math::

    \text{slope} = \frac{x_{(3)} - x_{(2.5)}}{3 - 2.5} = x_{(3)} - x_{(2)}

Sovling this for :math:`x_{(2.5)}`, we obtain,

.. math::

    x_{(2.5)} = x_{(3)} - (x_{(3)} - x_{(2)}) \cdot (3 - 2.5) \text{      Equation 1}

Or equivalently (plugging :math:`x_{(2)}` into the point-slope formula instead of :math:`x_{(3)}`),

.. math:: 

    x_{(2.5)} = x_{(2)} + (x_{(3)} - x_{(2)}) \cdot (2.5 - 2) \text{      Equation 2}

Notice in *Equation 1*, we are subtracting a quantity from the third order statistic, :math:`x_{(3)}`, whereas in *Equation 2* we are adding a quantity to the second order statistic, :math:`x_{(4)}`. In other words, to find the percentile of a sample data where the percentile does not correspond to an actual observation we may either subtract a corective quantity from the next largest observation, or add a corrective quantity to the next smallest observation.

Plugging the values of the *order statistics* :math:`x_{(2)}` and :math:`x_{(3)}` in either equation will result in the answer. 

Applying *Equation 1* to the example, we calculate the *25* :sup:`th` percentile,

.. math:: 

    x_{(2.5)} = -1.0 - (-1.0 - (-1.5)) \cdot (3 - 2.5) = -1.0 - 0.25 = -1.25

Applying *Equation 1* to the example, we calculate the *25* :sup:`th` percentile,

.. math:: 

    x_{(2.5)} = -1.5 + (-1.0 - (-1.5)) \cdot (2.5 - 2) = -1.5 + 0.25 = -1.25

In both cases, we arrive at the same answer of a 25 :sup:`th` percentile of ``-1.25`` minutes.     

Before moving onto the next section where we give the general formula for calculating the *sample percentile*, let us note both *Equation 1* and *Equation 2* can be rewritten in terms of the :ref:`floor-function` and the :ref:`ceiling-function`,

.. math::

    x_{(2.5)} = x_{(\lceil 2.5 \rceil)} - (x_{(\lceil 2.5 \rceil)} - x_{(\lfloor 2.5 \rfloor)}) \cdot (\lceil 2.5 \rceil - 2.5) \text{      Equation 1, Redux}

Or equivalently (plugging :math:`x_{(2)}` into the point-slope formula instead of :math:`x_{(3)}`),

.. math:: 

    x_{(2.5)} = x_{(\lfloor 2.5 \rfloor)} + (x_{(\lceil 2.5 \rceil)} - x_{(\lfloor 2.5 \rfloor)}) \cdot (2.5 - \lfloor 2.5 \rfloor) \text{      Equation 2, Redux}

.. _percentile-formula:

General Formula
***************

We can abstract away the specifies from the previous example to arrive at the general formula for a *sample percentile*. The :math:`(p \cdot 100 \%)^{\text{th}}` percentile :math:`\pi_p` is defined as the order statistic :math:`x_{(m)}`,

.. math:: 

    \pi_p = x_{(m)} = x_{(\lfloor m \rfloor)} + (x_{(\lceil m \rceil )} - x_{(\lfloor m \rfloor)})* (m - \lfloor m \rfloor)

.. note:: 

    In this definition, we have chosen *Equation 1, Redux* from the previous section to express the percentile. We could also define the percentile :math:`\pi_p` using *Equation 2, Redux* from the previous section as,

    .. math::

        \pi_p = x_{(m)} = x_{(\lceil m \rceil)} - (x_{(\lceil m \rceil )} - x_{(\lfloor m \rfloor)})* (\lceil m \lceil - m)

    In other words, we can either correct from *above* the order staistic :math:`x_{(m)}`, or from *below* the order statistic :math:`x_{(m)}`, as detailed in the previous. Either way will give the same answer.

.. math:: 

    m = p \cdot (n+1)

.. note:: 

    This formula, while conceptually more difficult than the procedure offered by the book, is more versatile. This formula will work no matter if the sample contains an even number of data points or an odd number of data points; It will work if the order *m* is a whole number or if the order *m* is a fraction. It can be applied to *every quantitative* sample of data.


.. _special-percentiles:

Special Percentiles
*******************

The table below lists the names that have been given to special percentiles.

+---------------+-------------------------------------+
| Percentile    | Name                                |
+===============+=====================================+
| 10 :sup:`th`  | First Decile                        |
+---------------+-------------------------------------+
| 20 :sup:`th`  | Second Decile                       |
+---------------+-------------------------------------+
| 25 :sup:`th`  | First Quartile                      |
+---------------+-------------------------------------+
| 30 :sup:`th`  | Third Decile                        |
+---------------+-------------------------------------+
| 40 :sup:`th`  | Fourth Decile                       |
+---------------+-------------------------------------+
| 50 :sup:`th`  | Median/Second Quartile/Fifth Decile |
+---------------+-------------------------------------+
| 60 :sup:`th`  | Sixth Decile                        |
+---------------+-------------------------------------+
| 70 :sup:`th`  | Seventh Decile                      |
+---------------+-------------------------------------+
| 75 :sup:`th`  | Third Quartile                      |
+---------------+-------------------------------------+
| 80 :sup:`th`  | Eighth Decile                       |
+---------------+-------------------------------------+
| 90 :sup:`th`  | Ninth Decile                        |
+---------------+-------------------------------------+
| 100 :sup:`th` | Fourth Quartile/ Tenth Decile       |
+---------------+-------------------------------------+

.. _median:

Median
-------

The *median* of a dataset is the observation such that half of the sample is less than or equal to it and half of the sample is greater than or equal to it. In other words, the *median* is the point in a dataset where half of the sample is above it and half of the sample is below it. As the table in the previous section indicated, another way of saying this is the *median* is the *50* :sup:`th` percentile. 

In this section, we state a quick shortcut formula for the median that you are probably familiar with, although you may not have seen it stated as precisely.

Shortcut
********

Applying the :ref:`percentile-formula` to the special case of the median, i.e. :math:`p = 0.5`, we have *order* of the median as,

.. math:: 

    m = 0.5 \cdot (n+1) = \frac{n+1}{2}

We must consider two cases: if *n* is odd or if *n* is even. Depending on the case, the *order m* of the median will be an integer value or an fractional value. 

Odd Sample
**********

If *n* is odd, then *n+1* is even (*divisibly be 2*). If *n+1* is even, then *m* is an integer. If *m* is an integer, then :math:`\lfloor m \rfloor = m = \lceil m \rceil`,

The percentile :math:`\pi_{0.50}` is given by,

.. math:: 

    \pi_{0.50} = x_{(\lfloor m \rfloor)} + (x_{(\lceil m \rceil )} - x_{(\lfloor m \rfloor)}) \cdot (m - \lfloor m \rfloor)

Applying :math:`\lfloor m \rfloor = m = \lceil m \rceil`,

.. math:: 
    
    \pi_{0.50} = x_{(m)} + (x_{(m)} - x_{(m)}) \cdot (m - m)

.. math:: 

    \implies \pi_{0.50} = x_{(m)} + 0 = x_{(m)}

Since :math:`m = \frac{n+1}{2}`,

.. math:: 

    \implies \pi_0.50 = x_{(\frac{n+1}{2})}

Recalling the meaning of the term :math:`x_{(\frac{n+1}{2})}`, we see if the number of samples is odd, then *median* is simply the :math:`\frac{n+1}{2}` :sup:`th` ordered observation.

.. topic:: Odd Sample: Median Shortcut

    .. math::
    
        \pi_{0.50} = x_{(\frac{n+1}{2})}

Even Sample
***********

If *n* is even, then *n+1* is odd (*not divisible by 2*). If *n+1* is odd, then *m* is not an integer. Because *m* is being divided by 2 and it is not an integer, 

.. math:: 
    
    m - \lfloor m \rfloor = 0.5 = \frac{1}{2}

In other words, any fraction with a denominator of 2 is either a whole number or a decimal that ends in *0.5*.

Applying this information to the sample percentile formula,

.. math::

    \pi_{0.50} = x_{(\lfloor m \rfloor)} + (x_{(\lceil m \rceil )} - x_{(\lfloor m \rfloor)}) \cdot \frac{1}{2}

Distributing the :math:`\frac{1}{2}`,

.. math:: 

    \pi_{0.50} = x_{(\lfloor m \rfloor)} + \frac{x_{(\lceil m \rceil )}}{2} - \frac{x_{(\lfloor m \rfloor)}}{2}

.. math:: 

    \implies \pi_{0.50} = \frac{x_{(\lceil m \rceil )}}{2} + \frac{x_{(\lfloor m \rfloor)}}{2}

.. math:: 
    
    \implies \pi_{0.50} = \frac{x_{(\lceil m \rceil )} + x_{(\lfloor m \rfloor)}}{2}

Plugging in :math:`m = \frac{n+1}{2}`

.. math:: 
    
    \pi_{0.50} = \frac{x_{(\lceil \frac{n+1}{2} \rceil )} + x_{(\lfloor \frac{n+1}{2} \rfloor)}}{2}

In other words, when the sample is even, the median is the *midpoint* of the middle two observations,

.. topic:: Odd Sample: Median Shortcut

    .. math::
    
        \pi_{0.50} = \frac{x_{(\lceil \frac{n+1}{2} \rceil )} + x_{(\lfloor \frac{n+1}{2} \rfloor)}}{2}

.. _skewness:

Identifying Skewness
********************

The median is important for helping identify *skewness* in data. To see why, consider the following example.

Example
    The annual income, measured to the nearest thousand, of a random sample of people is given below, 

    .. math::

        S = \{ \$ 50000, \$ 65000, \$ 45000, \$ 30000, \$ 120000, \$ 200000, \$ 70000, \$ 56000, \$ 55000, \$ 2000000 \}

    Find the sample mean and the sample median. 

It is always a good idea to start problems by looking at some sort :ref:`graphical representation <graphical_representations_of_data>` of the data being treated. If we use a histogram here, we immediately notice an unusual feature of this sample,

.. plot:: _plots/examples/03_ex03_skewed.py

One of the observations, the person with an annual income of *$2,000,000*, sits well outside the range of the rest of the observations. This feature of the sample, its *skew*, will manifest in the sample statistics as we move through this example. 

The sample mean is calculated using the :ref:`formula <sample_mean_formula>`,

.. math:: 

    \bar{x} = \frac{ \sum{x_i} }{n} = \$  291000

To find the sample median, we first find the *order* of the 50 :sup:`th` percentile,

.. math:: 

    m = 0.5 \cdot 11 = 5.5

Then we order the sample, 

.. math:: 

    S_{(o)} = \{ \$ 30000, \$ 45000, \$ 50000, \$ 55000, \$ 56000, \$ 65000, \$ 70000, \$ 120000, \$ 200000, \$ 2000000 \}

Finally, we apply the :ref:`general percentile formula <percentile-formula>`, with :math:`x_{(5)} = \$ 56000` and :math:`x_{(6)} = \$ 65000`,

.. math:: 

    \pi_{0.50} = x_{(5.5)} = x_{(\lfloor 5.5 \rfloor)} + (x_{(\lceil 5.5 \rceil)} - x_{(\lfloor 5.5 \rfloor)}) \cdot (5.5 - \lfloor 5.5 \rfloor)
    
.. math::

    = x_{(5)} + (x_{(6)} - x_{(5)}) \cdot (5.5 - 5 )


.. math::
    
    = \$ 56000 + (\$ 65000 - \$ 50000) \cdot (5.5 - 5) = \$ 60500

Take note, there is a large divergence between the value of the sample mean and the value of median here. The sample mean in this example :math:`\bar{x}` has a value that is larger than every observation in the sample except one, the person with an annual income of *$2,000,000*, whereas the median is closer where the majority of observations lie. 

The observation of *$2,000,000* is an :ref:`outlier <outliers>`, an unusual observation. This example illustrates when the sample mean is not a *resilient* measure of *centrality*; the presence of a single outlying observation in the sample *skews* the sample mean *towards* the outlying observation. The median, however, preserves its ability to measure *centrality* when the sample contains outliers. 

This idea will allow us to develop a general rule of thumb for identifying the presence of *skew* in samples.   

Rule of Thumb
*************

Consider a symmetrical sample distribution,

.. math:: 
    
    S = \{ 1, 5, 5, 5, 9 \}

As is easily verified in this example, the mean and median agree. A histogram of this situation would look like,

.. plot:: _plots/examples/03_ex04_symmetric.py

The median and mean are shown with green and blue lines respectively, but because they overlap exactly in this admittedly contrived example, you only see a single line in the graph.

In general, when dealing with symmetrical distributions, the following result holds, 

.. math:: 

    \bar{x} \approx \pi_{0.50}

A histogram for a symmetrical distribution is given below, with the median and mean again labelled with a green and blue line respectively,

.. plot:: _plots/examples/03_ex05_normal.py

In this case, the mean and median do not *exactly* agree. The extent to which the mean and median do **not** agree is a measure of a distribution's departure from *normality*. The less *normal* (*symmetrical*) the distribution becomes, the further apart the mean and median will split. Consider an extreme example like the following,

.. plot:: _plots/examples/03_ex07_right_skew.py

Most of the distribution is *clustered* to the left of the mean. The presence of the *right hand tail* on this distribution pulls the sample mean *towards* it. 

Consider the opposite case, where most of the data is clustered to the right of the mean,

.. plot:: _plots/examples/03_ex06_left_skew.py

As in the previous case, the presence of a *tails* acts like a sink towards which the mean is drawn. 

These results are summarized with the following rule of thumb,

.. topic:: Rule of Thumb for Skew

    1. If median is much greater than mean, then the data are skewed to the left. In this case, we say the distribution has a "*left hand tail*".
    2. If the median is much less than the mean, then the data are skewed to right. In this case, we say the distribution has a "*right hand tail*".
   
.. _z_score:

Z Score
-------

*Percentiles* are one way of describing location, but they are not the only way. We can also use *Z-Scores* to talk about the location of data points in a sample. 

*Z-scores* arise by inquiring into how we compare two different samples of data. 

For example, the SAT and the ACT are two different tests that are meant to measure the aptitude of graduating high school seniors before they are granted entry to college. Both tests are measuring the same variable, the analytical ability of a student, but both tests use different scales to measure the observable. 

Motivation
**********

TODO 

Formula
*******

Definition
    .. math::
        z = \frac{x_i - \bar{x}}{s}

The *z-score* in this formula would be a *sample statistic*. In other words, it is computed from a limited set of data, rather than an entire population. We may also talk about the *z-score* for an individual in the *population*. Recall, when a sample is drawn, we talk about the point estimates :math:`\bar{x}` and :math:`s`. When the entire population is under consider, these quantities are no longer *statistics*, but the *parameters* :math:`\mu` and :math:`\sigma`.

In the case of an individual selected from an entire population, the *z-score* formula would become,

.. math:: 

    z = \frac{x_i - \mu}{\sigma}

TODO 

.. _measures_of_variation:

Measures of Variation 
=====================

*Measures of variation* characterize the *spread* and *dispersion* of a sample of data.

Motivation
----------

Consider these two samples of data :math:`S_1` and :math:`S_2`,

.. math::

    S_1 = \{ 4, 5, 6 \}

.. math::

    S_2 = \{ 0, 5, 10 \}

If we apply the :ref:`Sample Mean Formula <sample-mean-formula>` to :math:`S_1`, we get,

.. math::

    \bar{x_1} = \frac{4 + 5 + 6}{3} = 5

If we apply the :ref:`Sample Mean Formula <sample-mean-formula>` to :math:`S_2`, we get,

.. math::

    \bar{x_2} = \frac{0 + 5 + 10}{3} = 5

In both cases, we wind up with the same sample mean. If we are summarizing these two samples of data to an audience and the only information we gave them was the sample mean, they might erroneously conclude the samples were the same.

However, refering to the actual observations that make up either sample, it is clear the samples are **not** the same.

Clearly, we need some other type of :ref:`sample-statistic` to differentiate these two samples of data. 

In other words, the *sample mean* is *not enough* to completely describe a sample of data. In the language of mathematics, we say the sample mean is "*necessary, but not sufficient*" to determine a sample of data.

But what exactly is different about these two samples? If we plot the samples separately on a number line and compare, we can see what is going on more clearly,

(INSERT PICTURE)

From the picture, it is obvious that :math:`S_2` is more *spread out* around the mean than :math:`S_1`. To put it another way, :math:`S_1` is more tightly *clustered* around the mean than :math:`S_2`. This *spread* or *clustering* is referred to as *variation*.

The goal of the next few sections is to come up with a way of quantifying and measuring this *variation*.

.. _interquartile-range:

Interquartile Range
-------------------

First up, we have the *interquartile range*. The interquartile range is defined as the difference between the third quartile and the first quartiile,

.. math::

	\text{IQR} = \pi_{0.75} - \pi_{0.50}
	
This statistic, by definition, tells us the range between which 50% of the distribution is contained. Moreover, the 50% of the distribution contained in the *IQR* is centered around the median, since the median falls exactly in the middle of the first and third quartile.

Rule of Thumb for Outliers
**************************

A general rule of thumb for identifying *outlying* observations with the *IQR* is given below,

.. topic:: *IQR* Rule for Outliers

    Any observation :math:`x_i` that satisfies the following two conditions may be an outlier.

	.. math::

        x_i \geq Q_3 + 1.5 \cdot IQR

        x_i \leq Q_1 - 1.5 \codt IQR

.. important::

	The cutoff point for *outliers* determined the *IQR* rule is arbitrary. Beyond the idea that most of the distribution is contained within the *IQR* and the insight any observation well outside this range probably qualifies as an outlyer, there is no hard justification for this rule of thumb. It is merely a `heuristic <https://en.wikipedia.org/wiki/Heuristic>`_ developed by professionals to aid in developing intuition about data.

.. _absolute-variation:

Absolute Variation
------------------

TODO 

.. _sample-variance:

Variance
--------

Motivation
**********

Let us consider a rather contrived example that is nevertheless instructive. Suppose **S** a sample of data represents 

TODO


.. _standard-deviation:

Standard Deviation
------------------

TODO

Formula
*******

.. math::

	s = \sqrt{  \frac{\sum^{n}_{i=1} (x_i - \bar{x})^2}{n-1} }

Degrees of Freedom	
******************

TODO

.. _coefficient-of-variation:

Coefficient of Variation
------------------------

TODO 

.. math::
 
    v = \frac{s}{\bar{x}} \cdot 100

TODO 


.. _chebyshevs-theorem:

Chebyshev's Theorem
===================

TODO

.. _data-transformations:

Data Transformations
====================

TODO

Adding or Subtracting A Constant
--------------------------------

TODO

Multiplying Or Dividing By A Constant
-------------------------------------

TODO
