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

.. TODO:
    This is also not quite right. Need some way of expressing "*necessarily*". The scope of rhymes over the entire poem isn't *necessarily* equivalent to the scope of the rhymes within the stanzas. 