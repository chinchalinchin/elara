.. _palindromics-appendix-i:

Appendix I: Addendums
=====================

TODO

.. _palindromics-appendix-i-i:

Appendix I.I: Omitted Axioms
-----------------------------

.. _palindromics-axiom-s-3:

.. topic:: Axiom S.3: Duality Axiom II

    For every Word in the Language, there exists a Sentence in the Corpus that contains it.

    .. math::

        \forall \alpha \in L: \exists \zeta \in C: \alpha \subset_s \zeta 

.. _palindromics-axiom-s-4:

.. topic:: Axiom S.4: Density Axiom

    There exists a natural number such that for all numbers less than it there exists a Sentence in the Corpus with that Word Length.

    \exists n \in \mathbb{N}: \forall i \in N_n: \exists \zeta in C: \Lambda(\zeta) = i 

This Axiom is required to induce proofs about Word Length. Without it, there is no formal way to accomplish an induction over Word Length. However, it may be (justifiably) argued there is no reason a natural language should obey this rule. It is possible to conceive of a natural language that does not have sentences with, say, exactly :math:`n = 13` words, perhaps due to an eccentricity in its grammar. In natural languages such as these, the results that depend on the following theorem are only valid in a truncated Corpus where all sentences with :math:`\Lambda(\zeta) > 12` are ignored. 

.. _palindromics-appendix-i-ii:

Appendix I.II: Omitted Proofs
------------------------------

TODO