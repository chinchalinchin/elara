.. _palindromics-appendix-i:

Appendix I: Omissions
=====================

.. _palindromics-appendix-i-i:

Appendix I.I: Omitted Axioms
----------------------------

This section of the Appendix contains Axioms the author considered at various points during the formalization, but as they did not ultimately seem necessary to establish the main results of the work, they have been placed here.

.. _palindromics-axiom-ai:

.. topic:: Axiom AI: Duality Axiom I

    For every Sentence in the Corpus, there exists a Word in the Language which is contained in it.

    .. math::

        \forall \zeta \in C: \exists \alpha \in L: \alpha \subset_s \zeta

.. _palindromics-axiom-aii:

.. topic:: Axiom AII: Duality Axiom II

    For every Word in the Language, there exists a Sentence in the Corpus that contains it.

    .. math::

        \forall \alpha \in L: \exists \zeta \in C: \alpha \subset_s \zeta 

.. note::

    The Duality Axioms are reminiscent of the relation of surjectivity in real analysis. However, containment is not a strict equality relation so this resemblance should not be taken too far.

.. _palindromics-axiom-aiii:

.. topic:: Axiom AIII: Density Axiom

    There exists a natural number such that for all numbers less than it there exists a Sentence in the Corpus with that Word Length.

    \exists n \in \mathbb{N}: \forall i \in N_n: \exists \zeta in C: \Lambda(\zeta) = i 

This Axiom is required to induce proofs about Word Length. Without it, there is no formal way to accomplish an induction over Word Length. However, it may be (justifiably) argued there is no reason a natural language should obey this rule. It is possible to conceive of a natural language that does not have sentences with, say, exactly :math:`n = 13` words, perhaps due to an eccentricity in its grammar. In natural languages such as these, the results that depend on the following theorem are only valid in a truncated Corpus where all sentences with :math:`\Lambda(\zeta) > 12` are ignored. 

.. _palindromics-axiom-aiv:

.. topic:: Axiom AIV: Word Comprehension Axiom

    Every Word in a Sentence of the Corpus belongs to the Language.

    .. math::

        \forall \zeta \in C: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \in L

.. _palindromics-appendix-i-ii:

Appendix I.II: Omitted Proofs
-----------------------------

.. note::

    Numbered theorems in this appendix are directly referenced in the main. An ``x`` in the theorem title indicates the theorem does not fit into the natural flow of the paper.

.. _palindromics-omitted-proofs-section-i-ii:

------------
Section I.II
------------

.. topic:: Theorem 1.2.2

    The Empty Character is contained in every String.

    .. math::

        \forall s \in S: \varepsilon \subset_s s

**Proof** Let :math:`s \in S`. By the Basis clause of :ref:`Concatenation <palindromics-definition-1-2-1>`, 

.. math::

    \varepsilon = \varepsilon\varepsilon

Therefore,

.. math::

    s = {\varepsilon}s = {\varepsilon\varepsilon}s

Let :math:`w_1 = \varepsilon` and :math:`w_2 = s`. Then, :math:`s = {w_1}\varepsilon{w_2}`. By the :ref:`definition of Containment <palindromics-definition-1-2-5>`, 

.. math::

    \varepsilon \subset_s s

∎

.. topic:: Theorem 1.2.x

    If any Character :math:`\iota` is not contained in :math:`u` and :math:`iota` is not contained in :math:`v`, then :math:`\iota` is not contained in :math:`uv`.

    .. math::

        \forall \iota \in \Sigma_e: \forall u, v \in S: (\neg(\iota \subset_s u) \land \neg(\iota \subset_s v)) \implies \neg(\iota \subset_s uv)

**Proof** Follows directly from :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>` by the law of contraposition.

∎

.. _palindromics-omitted-proofs-i-iv:

------------
Section I.IV 
------------

.. topic:: Theorem 1.4.15

    .. math::

        \forall s \in S: s[:l(s)] = s 

**Proof** Let :math:`s \in S`. Let :math:`n = l(s)`. Let :math:`i \in N_n`. The proof proceeds by induction on :math:`i`.

.. BASIS 

:underline:`Basis`: :math:`i = 1`

By :ref:`definition of Left Partial Strings <palindromics-definition-1-4-4>`,

.. math::

    s[:1] = s[i]

.. TODO: ........................................................................

.. INDUCTION

:underline:`Induction`:

.. TODO: ........................................................................

.. topic:: Theorem 1.4.16
    
    .. math::

        \forall s \in S: s[1:] = s


**Proof** Let :math:`s \in S`. Let :math:`n = l(s)`. Consider :math:`s[i:]` with :math:`i \in N_n`. Let 

.. math::
    
    j = n - i + 1
    
Then :math:`j \in N_n`, since :math:`i = 1 \implies j = n` and :math:`i = n \implies j = 1`. The proof proceeds by induction on :math:`j`.

.. BASIS

:underline:`Basis`

.. TODO: ........................................................................

.. INDUCTION

:underline:`Induction`

.. TODO: ........................................................................

.. _palindromics-omitted-proofs-section-ii-i:

------------
Section II.I
------------

.. _palindromics-theorem-2-1-11:

.. topic:: Theorem 2.1.x

    If the Pivot Character of a Canonical String is Empty, then the String is not invertible.

    .. math::

        \forall s \in \mathbb{S}: \omega_s = \varepsilon \implies (s \neq s^{-1})

**Proof** Follows immediately from :ref:`Theorem 2.2.4 <palindromics-theorem-2-2-4>` by the law of contraposition.

∎

.. _palindromics-omitted-proofs-section-ii-iv:

-------------
Section II.IV
-------------


.. topic:: Theorem 2.4.x

    All Perfect Palindromes are Invertible and Subvertible.

    .. math::

        K \subseteq (J \cap \cancel{J})

**Proof** Follow directly from :ref:`Theorem 2-4-1 <palindromics-theorem-2-4-1>`,

.. math::

    \zeta \in J

By :ref:`Theorem 2.4.8 <palindromics-theorem-2-4-8>`,

.. math::

    \zeta \in \cancel{J}

Thus,

.. math::

    \zeta \in J \land \zeta \in \cancel{J}

But this is exactly the definition of set intersections. Therefore, 

.. math::

    \zeta \in K \implies (\zeta \in J \cap \cancel{J})

But this is exactly the definition of subsets,

.. math::

    K \subseteq (J \cap \cancel{J})
    