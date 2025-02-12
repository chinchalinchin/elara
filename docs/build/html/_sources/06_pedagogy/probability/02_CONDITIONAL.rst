.. _conditional_probability:

=======================
Conditional Probability
=======================

Probability is merely a guess. It is based on whatever currently available information we have. If new information about the outcomes in the sample space becomes available, the probability assigned to the remaining events must be updated to take into account the new state of the world (or more accurately, :ref:`knowledge <knowledge>` of the new state of the world). *Conditional probability* is the tool for incorporating *new* information into probability calculations.

Motivation
==========

.. topic:: Example


	Suppose three red balls numbered 1 - 3 and four green balls numbered 1 - 4 are placed into a box. A friend selects a ball at random from the box without showing you what she selected. 

	        1. What is the probability the ball she selected has the number 2 written on it?
	        
	        2. If she now tells you the ball she selected is red, how does this affect the probability in part 1? 

Let **A** represent the event of selecting a ball numbered 2. Let **B** represent the event of selecting a red ball. Then :math:`n(A) = 2`, :math:`n(B)=3` and :math:`n(S) = 7` (Why?) Without taking into account the second part of the problem yet, the :ref:`classical_definition` yields the probability the ball she selected has the number 2 written it,

.. math::   

    	P(A) = \frac{2}{7} \approx 0.286

This number represents the probability of **A** *without any further information* provided about the sample space. 

If the friend now informs us the ball she selected was red, then this new information affects the probability. Certain outcomes have been *removed* from the sample space and are no longer possible. Because your friend revealed the color of the ball, we can discount all outcomes that involve the four green balls numbered 1 - 4. This type of :ref:`reduction_of_the_sample_space` is called *conditioning on the event* **B**. The event of **A** given **B** is denoted :math:`A \mid B`

Applying the :ref:`classical_definition` to this *reduced* sample space, we get the *probability of selecting a ball with the number 2, given the ball is red*,

.. math:: 
    
    	P(A \mid B) = \frac{1}{3} \approx 0.333

In other words, knowing the event a red ball was selected has *increased* the probability the ball has the number 2 written onit. Taking a look at the original sample space, this should be intuitive. There are less red balls than green balls, so more probability is "concentrated" in the red number 2 ball when the green balls are removed from the sample space.  

In order to further understand what is going, return to the point in time when your friend has not yet revealed the color she has selected, i.e. before the information the ball is red has become available. Before you know the ball is red, the probability of it being red is given by,

.. math:: 
    
    	P(B) = \frac{3}{7}

The probability of it being *red and having the number 2 written on it* is the probability of the :ref:`intersection` of **A** and **B**. Noting :math:`A \cap B` has only outcome in it (Why?), the outcome of a red ball with the number 2 has a probability, 

.. math:: 
    
    	P(A \cap B) = \frac{1}{7}

If the event **B** has occurred, then the only way the event **A** can now occur is through the event :math:`A /cap B`. The *conditional* probability of **A** given the occurrence of **B** is the ratio of ways **A** and **B** can occur to the ways **B** alone can occur,

.. math:: 

    	P(A \mid B) = \frac{\frac{1}{7}}{\frac{3}{7}} = \frac{1}{3} \approx 0.333

.. _conditional_probability_formula:

Condtional Probability Formula
==============================

Abstracting from the details from the previous example, the *conditional probability* of an event **A** given the occurrence of an event **B** is defined by the following formula,

.. math::
    
    	P(A \mid B) = \frac{P(A \cap B)}{P(B)}

An equivalent formula is given in terms of the :ref:`cardinality` of the sets :math:`A \cap B` and **B**,

.. math:: 
    
    	P(A \mid B) = \frac{n(A \cap B)}{n(B)}


.. topic:: Example

    	TODO 

.. topic:: Solution
    
	TODO
    
.. note::

	It is important to keep in mind that conditional probability is a *definition*. It is not an :ref:`axiom of probability <axioms_of_probability>`. 
	
	In mathematics, *axioms* represent the necessary assumptions for deriving a corpus of knowledge through syntactical rules: the initial *starting points* from which theorems are deduced. 
	
	A *definition* is *semantical* in nature, insofar that it expresses the opinion of the definer that the thing being defined is deserving of special notice, for it delineates a special concept that (hopefully) corresponds in some way to the observer's intuitive notions about reality. 

.. _reduction_of_the_sample_space:

Reduction of Sample Space
=========================

TODO 

Formula
-------

.. math::
	
	P(A \mid B) = \frac{n(A \mid B)}{n(S \mid B)}

The following example and its accompanying solutions serve to illustrate how conditional probability and the reduction of the sample space can be used to solve problems involving probability. Either method yields the correct answer.

.. topic:: Example
	
	A fair, two-sided coin with heads and tails on either side is placed into a box alongside a double-sided coin that has heads on both sides. You select a coin at random from the box and, without looking at which coin you picked, flip it. If the coin lands on heads, what is the probability you selected the two-sided coin?

.. topic:: Solution #1: Application of Conditional Probability Formula


	Before solving the problem, first define the :ref:`sample space <sample_space>` and identify the events that correspond to its various outcomes.
	
	Let :math:`(x, y)` represent the ordered pair of outcomes, where :math:`x` represents the face of the coin observed and :math:`y` represents the type of coin selected. The following table illustrates what is meant by this assignment,

	+-------------------------+-----------------------------------------|	
	| Symbolic Representation |          Interpretation                 |
	+-------------------------+-----------------------------------------|
	|       :math:`(h, f)`    |    outcome of heads with fair coin      |
	+-------------------------+-----------------------------------------|
	|       :math:`(t,f)`     |    outcome of tails with fair coin      |
	+-------------------------+-----------------------------------------|
	|       :math:`(h_1, d)`  | outcome of heads with double-sided coin |	
	+-------------------------+-----------------------------------------|
	|       :math:`(h_2, d)`  | outcome of heads with double-sided coin |
	+-------------------------+-----------------------------------------|
	
	Note the two heads on the double-sided coin are distinguished with subscripts. With this notation, the sample space of the experiment is given by,
	
	.. math::
	
		S = \{ (h,f), (t,f), (h_1, d), (h_2, d) \}
			
    	.. math::
    	
        	n(S) = 4 

	The event of selecting the fair coin, :math:`F`, contains the outcomes,

	.. math::
		
		F = \{ (h,f), (t,f) \}

	.. math::

	        n(F) = 2

	Likewise, the event of selecting the double-sided coin, :math:`D`, contains the outcomes,

    	.. math::
    		
    		D = \{ (h_1, d), (h_2, d) \}
    	
    	.. math::
        	
        	n(D) = 2

	The event of getting a head, :math:`H`, contains the outcomes,

	.. math:: 

		H = \{ (h, f), (h_1, d), (h_2, d) \}
	
	.. math::
        
        	n(H) = 3
    
	Note in this formulation the event of getting a head :math:`H` is an abstraction, a logical grouping of possible outcomes, whereas the outcomes ":math:`h`", ":math:`h_1`" and ":math:`h_2`" are the actual things being abstracted, the symbols we use to represent the *physical* occurrence of a possibility. 
    	

	The problem can then be expressed in terms of the :ref:`conditional_probability_formula`,

	.. math::
	
		P(D \mid H) = \frac{P(D \cap H)}{P(H)}

	The denominator of this expression can be found by straight-forward application of the :ref:`classical_definition`,

	.. math::
	
		P(H) = \frac{3}{4}

	Whereas the numerator first requires calculating the intersection of **D** and **H**,

	.. math::
        
        	D \cap H = \{ (h_1, d), (h_2,d) \}

	.. math::
        
        	n(D \cap H) = 2

	Whereupon the :ref:`classical_definition` can be applied again,

	.. math::
	
        	P(D \cap H) = \frac{2}{4} = \frac{1}{2}

	The conditional probability of **D** given the occurrence of **H** is then calculated from the previously mentioned :ref:`conditional_probability_formula`,
	
	.. math::
	
	        P(D \mid H) = \frac{\frac{1}{2}}{\frac{3}{4}} = \frac{1}{2} \cdot \frac{4}{3} = \frac{2}{3}

.. topic:: Solution #2: Reduction of Sample Space Formula

	There is another way of looking at this problem. The fact that it is known the outcome of the coin flip was heads effectively *reduces* the sample space **S** from,

	.. math::
	
		S = \{ (h,f), (t,f), (h_1, d), (h_2, d) \}
		
	To a truncated set :math:S \mid H, the sample space *given the occurence of event* **H**, 

	.. math::
	
		S \mid H = \{ (h,f), (h_1, d), (h_2, d) \}

    	.. math::
    	
        	n(S \mid H) = 3

    	In other words, the outcome of tails is removed as a possibility by the additional information a head has been obtained. Then, the event :math:`D` of selecting the two-sided coin conditioned on the event of getting a head remains,

    	.. math::
        	
        	D \mid H= \{ (h_1, d), (h_2, d)  \}
    
    	.. math::
        	
        	n(D \mid H) = 2

    
    	Therefore, by the *reduction of sample space* formula,

    	.. math::
        
        	P(D \mid H) = \frac{n(D \mid H)}{n(S \mid H)}

    	.. math::
        
        	P(D \mid H) = \frac{2}{3}

.. _monty_hall_problem:

Monty Hall Problem
------------------

TODO

.. _probability_tables_revisted:

Probability Tables Revisited
----------------------------

TODO

.. _bayes_laws:

Bayes' Laws
===========

The most important theorems regarding conditional probability are known collectively as *Bayes' Laws*.

.. _bayes_multiplication_law:

Multiplication Law
------------------

The *conditional probability* formula can be rearranged with the aid of some simple algebra,

.. topic:: Bayes' Multiplication Law

	.. math::
	
		P(A \cap B) = P(B \mid A) \cdot P(A)

This version of the *conditional probability* formula along with the technique of :ref:`reduction_of_the_sample_space` give us an alternate approach for understanding certain probability problems. Often, we need to know the probability of a complicated :ref:`compound event <compound_events>`, which usually involves cumbersome combinatorial analysis. *Conditional probability* can be used to sidestep these calculations.
		
The following example illustrates the simplification affected by the introduction of *conditional probability* into combinatorial problems. This example can be solved in one of two ways. The first solution uses the techniques from the :ref:`Combinatorics section <combinatorics>`. The second solution uses the techniques of the *Multiplication Rule* and *Reduction of the Sample Space* just discussed. The reader will observe, while both methods yield the same answer, the second method is substantially easier, both from a calculation perpsective and from a conceptual perspective (i.e., it's easier to understand).


.. topic:: Example

	Two cards are drawn without replacement from a standard deck of 52 playing cards. What is the probability both cards are red? 

.. note:: Solution #1: Combinatorics
    
    	The total number of two-card hands dealt from a deck of 52 cards is equal to the number of combinations of 52 distinct objects taken 2 at a time. To find the total number of such combinations, the :ref:`combination_formula` is used,

    	.. math::
        	
        	C_2^{52} = \frac{52!}{2! \cdot 50!} = \frac{52 \cdot 51}{2} = 1326

    	Therefore, there are a total of *1326* hands that can be dealt. 

    	The same logic can be used to find the number of ways to pick two red cards. Note there are :math:`\frac{52}/{2}=26` red cards in a standard deck of playing cards. Therefore, the number of combinations of 26 distinct objects taken 2 at a time is,

    	.. math::
        	
        	C_2^{26} = \frac{26!}{2! \cdot 24!} = \frac{26 \cdot 25}{2} = 325
    
    	Therefore, the desired probability can be found using the :ref:`classical_definition`,

    	.. math::
        	
        	P("two red cards") = \frac{325}{1326} \approx 0.2451

.. note:: Solution #2: Conditional Probability

    	Let **R** :sub:`1` represent the event the first card drawn is red. Let **R** :sub:`2` represent the event the second card drawn is red. Then the event :math:`R_1 \cap R_2` represents the event the first card is red *and* the second card is red. The *Multiplication Rule* states the probability of an intersection can be expressed as,

    	.. math::
        
        	P(R_1 \cap R_2) = P(R_2 \mid R_1 ) \cdot P(R_1)

    	The term :math:`P(R_1)` is the probability of selecting a red card on the first draw. This can be calculated easily with the :ref:`classical_definition`,
    
    	.. math::
        
        	P(R_1) = \frac{26}{52}

    	The term :math:`P(R_2 \mid R_1)` can likewise be quickly decomposed by noticing the event **R** :sub:`1` *reduces the sample space* to *51* cards, *25* of which are red. Using the :ref:`classical_definition` once again, the conditional probability of **R** :sub:`2` given the occurrence of **R** :sub:`1` is,

    	.. math::
        
        	P(R_2 \mid R_1) = \frac{25}{51}

    	Therefore, 

    	.. math::
        
        	P(R_1 \cap R_2) = \frac{26}{52} \cdot \frac{25}{51} = \frac{26 \cdot 25}{52 \cdot 51}

    	.. math::
        
        	P(R_1 \cap R_2) = \frac{650}{2652} \approx 0.2451

.. _law_of_total_probability:

Law of Total Probability
------------------------

Before stating the *Law of Total Probability*, a corrollary is required.

Complementary Intersections
***************************

.. topic:: Complementary Intersections

	For any events :math:`A` and :math:`B`,
	
	..  math::
	
		P(A) = P(A \cap B) + P (A \cap B^c)
	
In order to prove this corrollary, consider the following identity,

.. math::

	A = (A \cap B) \cup (A \cap B^c)
	
Now, by definition, :math:`A \cap B` and :math:`A \cap B^c` are :ref:`mutually exclusive <mutual_exclusion>`. Therefore, it follows from the :ref:`counting_theorems` of set theory, 

.. math:: 

	n(A) = n(A \cap B) + n(A \cap B^c)

An application of the :ref:`classical_definition` leads directly to the result of the corrollary,
 
.. math::

	P(A) = P(A \cap B) + P(A \cap B^c)

Total Probability
*****************

Taking the *Complementary Intersection* corrollary from the previous section and applying the concepts of conditional probability to it, each term on the right hand side can be decomposed Bayes' Multiplication Law,

.. math::

	P(A \cap B) = P(A \mid B) \cdot P(B)
	
.. math::

	P(A \cap B^c) = P(A \mid B^c) \cdot P(B^c)
	
Plugging these definitions into the *Complementary Intersection* corrollary transforms the proposition into the Law of Total Probability,

.. topic:: Law of Total Probability

	.. math::
	
		P(A) = P(A \mid B) \cdot P(B) + P(A \mid B^c) \cdot P(B^c)
	

The following example illustrates an application of the *Law of Total Probability*,

.. topic:: Example

	TODO
	
.. note:: Solution

	TODO
	
Bayes' Formula
--------------

TODO

Tree Diagrams
*************

TODO

DO FALSE POSITIVE EXAMPLE, THOSE ARE ALWAYS FUN

.. _independence:

Independence
============

Definition
----------

Conditional probability allows the precise definition of *independence* and *independent events*. Intuitively, *independent events* are understood as events whose outcomes do not affect one another. If you flip a coin and then roll a dice, the outcome of the coin flip in no way determines the outcome of the die roll. In other words, the *probability of one event does not alter the probability of the other event*. Mathematically, this can be stated as follows,

.. math::

	\text{ A and B are independent events } \equiv P(B | A) = P(B)
	
The knowledge that **A** has happened does not change the probability of **B**. The designation of **A** and **B** are arbitrary, so this also implies,

.. math::

	\text{ A and B are independent events } \equiv P(A | B) = P(A)
	
.. _independence_multiplication_law:

Multiplication Law
------------------

The definition of *independence* leads to an important consequence. Bayes' Multiplication Law states,

.. math::

	P(B \cap A) = P(B \mid A) \cdot P(A)
	
But if **A** and **B** are independent, then by definition :math:`P(B \mid A) = P(B)`,

.. math::

	P(B \cap A) = P(B) \cdot P(A)
	
This result is summarized in the following theorem,

.. topic:: Independence Multiplication Law

	If **A** and **B** are independent events, then
	
	.. math::
		
		P(A \cap B) = P(A) \cdot P(B)
