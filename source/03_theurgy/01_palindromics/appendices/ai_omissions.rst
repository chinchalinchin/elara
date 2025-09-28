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

.. topic:: Theorem 1.2.1
    
    The String Length of the concatenation of String :math:`s` and String :math:`t` is equal to the sum of their String Lengths.

    .. math::
        
        \forall s,t \in S: l(st) = l(s) + l(t)

**Proof** The proof proceeds by induction on :math:`t`.

:underline:`Basis`: Let :math:`t = \varepsilon` and :math:`s \in S`. Consider :math:`st = s\varepsilon`.

By the :ref:`basis clause of concatenation <palindromics-definition-1-2-1>`, :math:`s\varepsilon = s`. By the :ref:`basis clause of String Length <palindromics-definition-1-2-2>`, :math:`l(\varepsilon) = 0`. It follows from the basic laws of arithmetic,

.. math::

    l(s\varepsilon) = l(s)  = l(s) + 0 

.. math::

    = l(s) + l(\varepsilon) = l(s) + l(t)

Therefore, the base case, :math:`l(st) = l(s) + l(t)`, holds.

:underline:`Induction`: Let :math:`s, t \in S` and `u \in \Sigma_{e}`. Assume :math:`l(st) = l(s) + l(t)`. Let :math:`v = tu` and consider,

.. math::

    l(sv) = l(s(tu)) = l((st)u)

If :math:`u = \varepsilon`, then applying the argument of the base case,

.. math::

    l(sv) = l((st)u) = l(st) + l(\varepsilon) 

.. math::

    = l(st) = l(s) + l(t)

Where the last equality follows from the inductive hypothesis. Note :math:`t = t\varepsilon = tu = v` by the :ref:`basis clause of concatenation <palindromics-definition-1-2-1>`. From this, it follows the inductive step is established for :math:`u = \varepsilon`,

.. math::

    l(sv) = l(s) + l(v)

If :math:`u \neq \varepsilon`, then it follows from the :ref:`induction clause of String Length <palindromics-definition-1-2-2>`,

.. math::

    l((st)u) = l(st) + 1 = l(s) + l(t) + 1 \quad \text{ (1) }

Where the last equality follows from the inductive hypothesis. Consider the quantity :math:`l(tu)`. By the :ref:`induction clause of String Length <palindromics-definition-1-2-2>`,

.. math::

    l(tu) = l(t) + 1

Adding :math:`l(s)` to both sides,

.. math::

    l(s) + l(tu) = l(s) + l(t) + 1 \quad \text{ (2) }

Comparing the RHS of (1) and (2), it follows the LHS are equal,

.. math::

    l(stu) = l(s) + l(tu)

Summarizing, if :math:`l(st) = l(s) + l(t)` and :math:`u \in \Sigma_{e}`, then :math:`l(stu) = l(s) + l(tu)`. Therefore, the inductive step is established. 

Since the basis case and inductive step have both been established, it follows from the principle of finite induction,

.. math::

    \forall s,t \in S: l(st) = l(s) + l(t)

∎

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

.. _palindromics-theorem-1-2-x:

.. topic:: Theorem 1.2.x

    If any Character :math:`\iota` is not contained in :math:`u` and :math:`iota` is not contained in :math:`v`, then :math:`\iota` is not contained in :math:`uv`.

    .. math::

        \forall \iota \in \Sigma_e: \forall u, v \in S: (\neg(\iota \subset_s u) \land \neg(\iota \subset_s v)) \implies \neg(\iota \subset_s uv)

**Proof** Follows directly from :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>` by the law of contraposition.

∎


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