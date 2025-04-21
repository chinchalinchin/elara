.. _syntagmics-calculus:

Section IV: Calculus
====================

.. _syntagmics-axioms:

Axioms
------

1. All words are made of syllables, all lines are made of words, all stanzas are made of lines. 

.. math::
    
    \forall \varsigma, u, \lambda: \exists ⲣ: [ⲣ \subset \lambda] \land [\lambda \subset u] \land [u \subset \varsigma]

2. All poems are made of stanzas. 

.. math::

    \forall p: \exists n: p  = \sum_1^{n} \varsigma_i  

3. The scope of a poem is not equal to the scope of its stanzas. 

.. math::

    \forall p: \forall n: \sum_1^{n} \overline{\varsigma_i} \neq \overline{ \sum_1^{n} \varsigma_i }

.. TODO: Axiom 3
    This is also not quite right. Need some way of expressing "*necessarily*". The scope of rhymes over the entire poem isn't *necessarily* equivalent to the scope of the rhymes within the stanzas. 

Theorems
--------

.. TODO: Theorems
    - The speed of iambic and trochaic meter is 1/2. The speed of dactylic and anapestic meter is 1/3. The speed of spondaic meter is 1. The speed of pyrrhic meter is 0. 
    - The speed of a poem is a real number in the interval [0, 1]
    - NOTE: probably need to take the inverse of the current definition to allow the quantity to correlate with the psychological perception of slowness! 
    - Define the idea of permissible structures. Then based on constraints like number of lines, number of syllables, only certain poetic forms are permissable. For example, if :math:`l(p \mid u) = 2`, then the only structures possible are :math:`x.y` and :math:`x+y`. If :math:`l(p | u) = 3`, then :math:`x.y.z`, :math:`x.y + z`, :math:`x+y.z`, :math:`x+y+z`, etc. There is some sort of combinatorial relationship between the line length of a poem and the possible structures that can manifested.
