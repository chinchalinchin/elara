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

.. TODO: Possible Theorems
    1. If meter is n-iambic, then syllable length has to be congruent modulo 2n. Similar theorems for other meters.
    2. Define the idea of permissible structures. Then based on constraints like number of lines, number of syllables, only certain poetic forms are permissable. For example, if l(p | u) = 2, then the only structures possible are x.y and x+y. If l(p | u) = 3, then x.y.z, x.y + z, x+y.z, x+y+z, etc. There is some sort of combinatorial relationship between the line length of a poem and the possible structures that can manifested.