.. _palindromics-section-ii-i:

Section II.I: Delimiter Count
=============================

.. _palindromics-delimiter-count:

Definition & Examples
---------------------

.. _palindromics-definition-2-1-1:

.. topic:: Definition 2.1.1: Delimiter Count

    Let :math:`s \in S`. The Delimiter Count of :math:`s`, denoted :math:`\Delta(s)`, is defined inductively using the following schema,

    - Basis: 
        - If :math:`\neg(\sigma \subset_s s)`, then :math:`\Delta(s) = 0`
        - If :math:`s = \varepsilon`, then :math:`\Delta(s) = 0`
    - Induction:
        - If :math:`s = (u)(\sigma)(v)` for any :math:`u,v \in S` where :math:`\neg(\sigma \subset_s u)`, :math:`\Delta(s) = \Delta(v) + 1`

**Example** Let :math:`ᚠ = \text{with up so floating many bells down}`. Consider :math:`\Delta(ᚠ)`.

.. note::

    The astute reader will note there are 6 Delimiters in :math:`ᚠ`.

Let :math:`u_1 = \text{with}` and :math:`v_1 = \text{up so floating many bells down}`. Then, :math:`ᚠ = (u_1)(\sigma)(v_1)`. Note :math:`\neg(\sigma \subset_s u_1)`. By the Induction clause :ref:`of the Delimiter Count <palindromics-definition-2-1-1>`,

.. math::

    \Delta(ᚠ) = \Delta(v_1) + 1

Let :math:`u_2 = \text{up}` and :math:`v_2 = \text{so floating many bells down}`. Then, :math:`v_1 = (u_2)(\sigma)(v_2)`. Note :math:`\neg(\sigma \subset_s u_2)`. By the Induction clause,

.. math::

    \Delta(v_1) = \Delta(v_2) + 1


Let :math:`u_3 = \text{so}` and :math:`v_3 = \text{floating many bells down}`. Then, :math:`v_2 = (u_3)(\sigma)(v_3)`. Note :math:`\neg(\sigma \subset_s u_3)`. By the Induction clause,

.. math::

    \Delta(v_2) = \Delta(v_3) + 1

Let :math:`u_4 = \text{floating}` and :math:`v_4 = \text{many bells down}`. Then, :math:`v_3 = (u_4)(\sigma)(v_4)`. Note :math:`\neg(\sigma \subset_s u_4)`. By the Induction clause,

.. math::

    \Delta(v_3) = \Delta(v_4) + 1

Let :math:`u_5 = \text{many}` and :math:`v_5 = \text{bells down}`. Then, :math:`v_4 = (u_5)(\sigma)(v_5)`. Note :math:`\neg(\sigma \subset_s u_5)`. By the Induction clause,

.. math::

    \Delta(v_4) = \Delta(v_5) + 1


Let :math:`u_6 = \text{bells}` and :math:`v_6 = \text{down}`. Then, :math:`v_5 = (u_6)(\sigma)(v_6)`. Note :math:`\neg(\sigma \subset_s u_6)`. By the Induction clause,

.. math::

    \Delta(v_5) = \Delta(v_6) + 1

Note :math:`\neg(\sigma \subset_s v_6)`. Therefore, by the Basis clause,

.. math::

    \Delta(v_6) = 0

Putting the recursion together,

.. math::

    \Delta(ᚠ) = (((((0 + 1) + 1) + 1) + 1) + 1) + 1 = 6

∎

.. _palindromics-delimiter-count-properties:

Properties
----------

.. note::

    All of these properties follow from the :ref:`definition of Delimiter Counts <palindromics-definition-2-1-1>` and the indicated axioms, and they are quantified over their respective domains.

1. From the definition itself: :math:`\Delta(\sigma) = 1`
2. From the :ref:`Discovery Axiom <palindromics-axiom-iv>`: :math:`\Delta(\alpha) = 0`
3. From the :ref:`definition of Canonization <palindromics-definition-1-2-6>`: :math:`\Delta(\pi(s)) = \Delta(s)`
4. From the :ref:`definition of Containment <palindromics-definition-1-2-5>` :math:`\Delta(s) = 0 \equiv \neg(\sigma \subset_s s)`

.. note::

    Due to property #4, the formal system now has two equivalent ways of expressing the property "*has no Delimiters*". See the passage directly after :ref:`Theorem 2.1.1 <palindromics-theorem-2-1-1>` for a more detailed discussion.

.. _palindromics-delimiter-count-theorems:

Theorems
--------

.. _palindromics-theorem-2-1-1:

.. topic:: Theorem 2.1.1

    The Word Length of a Sentence in the Corpus is equal to one more than its Delimiter Count.

    .. math::

        \forall \zeta \in C: \Lambda(\zeta) = \Delta(\zeta) + 1

**Proof** Let :math:`\zeta \in C`. Let :math:`n = \Lambda(\zeta)`. By the :ref:`Theorem 1.4.3 <palindromics-theorem-1-4-3>`,

.. math::

    \zeta = \Pi_{i=1}^{n} \zeta[[i]]

By :ref:`the definition of Limitations <palindromics-definition-1-3-5>`,

.. math::

    = (\zeta[[1]])(\sigma)(\zeta[[2]]) ... (\sigma)(\zeta[[n]])

The proof proceeds by induction on Word Length. 

.. Basis

:underline:`Basis`: Assume :math:`n = 1`. Then,

.. math::

    \zeta = \zeta[[1]]

Let :math:`m = l(\zeta[[1]])`. By the :ref:`Discovery Axiom <palindromics-axiom-v>`,

.. math::

    \forall i \in N_m: (\zeta[[1]])[i] \neq \sigma

By :ref:`Containment <palindromics-definition-1-2-5>`,

.. math::

    \neg(\sigma \subset_s \zeta[[1]])

By the Basis clause of :ref:`Delimiter Counts <palindromics-definition-2-1-1>`,

.. math::
    
    \Delta(\zeta) = 0

Therefore, 

.. math::

    \Lambda(\zeta) = \Delta(\zeta) + 1

.. INDUCTION

:underline:`Induction`: Let :math:`\Lambda(\zeta) = n` for some :math:`n \geq 1`. Assume :math:`\Lambda(\zeta) = \Delta(\zeta) + 1` 

Let :math:`\xi \in C` such that :math:`\Lambda(\xi) = n + 1`. Therefore, :math:`\sigma \subset_s \xi`. By :ref:`Containment <palindromics-definition-1-2-5>`,

.. math::

    \exists u,v \in S: \xi = (u)(\sigma)(v)

Choose :math:`u = \xi[[1]]` so that :math:`\neg(\sigma \subset_s u)`. Then, by :ref:`definition of Word Length <palindromics-definition-1-4-1>`, :math:`\Lambda(v) = n`. Then, by the Induction clause of the :ref:`Delimiter Counts <palindromics-definition-2-1-1>`

.. math::

    \Delta(\xi) = \Delta(v) + 1

By inductive hypothesis,

.. math::

    \Lambda(v) = \Delta(v) + 1

From which it follows,

.. math::

    \Delta(v) = n - 1

And thus, 

.. math::

    \Delta(\xi) = n

Substituting :math:`\Lambda(\xi) = n + 1`

.. math::

    \Lambda(\xi) = \Delta(\xi) + 1 

Therefore the induction is established. Summarizing and generalizing,

.. math::

    \forall \zeta \in C: \Lambda(\zeta) = \Delta(\zeta) + 1

∎

The previous example and theorem should make clear :math:`\Delta(s)` plays the role of a logical functor :math:`\Delta(s): S \to \mathbb{N}` that maps Strings with equal amounts of Delimiter Characters to the same natural Number. For this reason, the term :math:`\Delta(s)` can be treated formally as "*the number of Delimiters*" in :math:`s`. 

To make this notion more precise and rigorous, note if :math:`\neg(\sigma \subset_s s)`, then :math:`\Delta(s) = 0`, i.e. Strings that do not contain Delimiters have a Delimiter Count of 0. 

Furthermore, if :math:`s[i] = \sigma` for :math:`i \geq 1`, that is, if :math:`s` contains atleast one Delimiter, then :math:`s = {u}{\sigma}{v}` by :ref:`Containment <palindromics-definition-1-2-5>` for some :math:`u` such that :math:`\neg(\sigma \subset_s u)` and :math:`v` bears the relation "*having one less Delimiter than*" to :math:`u`. By the Induction clause of :ref:`Delimiter Count <palindromics-definition-2-1-1>`, this means,

.. math::

    \Delta(s) = \Delta(v) + 1

Therefore, it can be seen the equivalence of the property of "*having i Delimiters*" and :math:`\Delta(s) = i` is dependent on the equivalence of the property of "*having i-1 Delimiters*" and :math:`\Delta(u) = i - 1`. Therefore, by induction, in every instance,

    :math:`\Delta(s) = n` is equivalent to the structural property of "*having* :math:`n` *Delimiters*"

This ability to switch between the formal expression :math:`\Delta(s) = n` and the colloquial ":math:`s` has :math:`n` Delimiters" is invaluable in simplifying the proofs of many of the properties of the Delimiter Count, as these next theorems show.

.. _palindromics-theorem-2-1-2:

.. topic:: Theorem 2.1.2 

    The Delimiter Count of a canonical String is equal to the Delimter Count of its inverse.

    .. math::
    
        \forall s \in S: \Delta(s) = \Delta(s^{-1})

**Proof** Let :math:`s, t \in S` such that :math:`t = s^{-1}`. Let :math:`n = l(s)`. By :ref:`String Inversion <palindromics-definition-1-2-8>`, 

.. math::

    l(t) = l(s)

.. math::

    \forall i \in N_n: t[i] = s[n - i + 1]

Therefore, since inversion does not insert or delete Characters, i.e. the number of Delimiters in :math:`s` must be equal to the number of Delimiters in :math:`t`. Therefore, 

.. math::

    \forall s,t \in S: \Delta(s) = \Delta(s^{-1})

∎

.. _palindromics-theorem-2-1-3:

.. topic:: Theorem 2.1.3

    The String Length of a Sentence is equal to its Delimiter count plus the sum of the String Lengths of its Words.

    .. math::

        \forall \zeta \in C: l(\zeta) = \Delta(\zeta) + \sum_{i=1}^{\Lambda(\zeta)} l(\zeta[[i]])

**Proof** Let :math:`\zeta \in C`. 

By definition, since :math:`\zeta[i] = \sigma` or :math:`\zeta[i] \neq \sigma`, but both, the number of Characters in :math:`\zeta` is the number of Delimiter Characters plus the number of non-Delimiter Characters. 

The number of Delimiter Characters in :math:`\zeta` is :math:`\Delta(\zeta)`.

The number of non-Delimiter Characters is exactly equal to sum of the number of Characters in each Word, :math:`\zeta[i]`, :math:`\sum_{i=1}^{\Lambda(\zeta)} l(\zeta[[i]])`.

Thus, putting everything together,

.. math::

    l(\zeta) = \Delta(\zeta) + \sum_{i=1}^{\Lambda(\zeta)} l(\zeta[i])

∎

.. _palindromics-theorem-2-1-4:

.. topic:: Theorem 2.1.4
    
    The number of Delimiters in two Concatenated Strings is equal to the sum of the number of Delimiters in each individual String.

    .. math::

        \forall s,t \in S: \Delta(st) = \Delta(s) + \Delta(t)

Let :math:`s,t \in S`. Then, by :ref:`Concatenation <palindromics-definition-1-2-1>`, :math:`st` is a String compose of non-overlapping Strings :math:`s` and :math:`s`. Therefore, by the law of disjoint unions, the number of Delimiters contained in :math:`st` must equal the sum of the of Delimiters contained in :math:`s` and the number of Delimiters contained in :math:`s`.

∎

The next theorem establishes an important property that will be essential in the study of palindromic parity.

.. note:: 

    Due to :ref:`Theorem 2.1.1 <palindromics-theorem-2-1-1>`, Theorems 2.1.5 - 2.1.9 & 2.1.11 - 2.1.14 have equivalent statements using Word Length :math:`\Lambda(\zeta)` instead of :math:`\Delta(\zeta)`.

.. _palindromics-theorem-2-1-5:

.. topic:: Theorem 2.1.5

    If a String is equal to its own Inverse and has an odd Delimiter Count, then its central Character is a Delimiter. 

    .. math::

        \forall s \in S: ((\exists n \in \mathbb{N}: \Delta(s) = 2n +1 ) \land (s = s^{-1})) \implies s[\frac{l(s)+1}{2}] = \sigma

**Proof** Let :math:`s,t \in S` such that :math:`\Delta(s) = 2n + 1` for some :math:`n \in \mathbb{N}` and :math:`t = s^{-1}`. Let :math:`m = l(s)`. Let :math:`P` be the set of Delimiter indices in :math:`s`,

.. math::

    P = \{ i \mid s[i] = \sigma \}

Then :math:`\lvert P \rvert = \Delta(s) = 2n + 1` by assumption.

By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    t[i] = s[m - i + 1]

In other words, every Delimiter in :math:`s` at :math:`i` must have a symmetric pair at :math:`m - i + 1` and visa versa. Since :math:`\lvert P \rvert` is odd, there must be one element of :math:`P` that is its own symmetric pair. This element must satisfy the condition,

.. math::

    j = m - j + 1

Solving for :math:`j`,

.. math::

    j = \frac{m + 1}{2} = \frac{l(s) + 1}{2} 

Therefore, the Character at :math:`j` in :math:`s` must be a Delimiter. Summarizing and generalizing,

.. math::

    \forall s \in S: ((\exists n \in \mathbb{N}: \Delta(s) = 2n +1 ) \land (s = s^{-1})) \implies s[\frac{l(s)+1}{2}] = \sigma

∎

.. note::

    An interesting corollary to :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>` is established in the next theorem. This shows the parity of a Canonical String can be inferred from its invertibility and the parity of its Delimter Count.

.. _palindromics-theorem-2-1-6:

.. topic:: Theorem 2.1.6 

    If a String is equal to its own Inverse and has an odd number of Delimiters, then its String Length must be odd.

    .. math::

        \forall s \in S: ((\exists n \in \mathbb{N}: \Delta(s) = 2n + 1) \land (s = s^{-1})) \implies (\exists i \in N_{l(s)}: l(s) = 2i - 1)

**Proof** Let :math:`s \in S`. Assume :math:`\Delta(s) = 2n + 1` for some :math:`n \in \mathbb{N}`. Assume :math:`s = s^{-1}`. By :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>`,

.. math::

    s[\frac{l(s)+1}{2}] = \sigma

Therefore, 

.. math::

    \exists i \in N_{l(s)}: i = \frac{l(s) + 1}{2}

Which is equivalent to,

.. math::

    \exists i \in N_{l(s)}: l(s) = 2i - 1

∎

.. note::

    As will be shown over the course of the next section, the parity of the Delimter Count of a String is a *sufficient*, but not *necessary*, condition for the parity of its String Length.

    In other words, knowing an Invertible String has an odd number of Delimiters is sufficient for concluding its String Length is odd. However, an Invertible String which has an odd String Length does not necessarily have an odd number of Delimiters.

    In fact, this logic generalizes to *any* Alphabetic Character. If *any* Alphabetic Character occurs within a invertible Canonical String an odd number of times, then that is sufficient for concluding the String has an odd String Length.

.. important::

    :ref:`Theorem 2.1.5 <palindromics-theorem-1-2-5>` and :ref:`Theorem 2.1.6 <palindromics-theorem-2-1-6>` apply to *all* Strings in :math:`S`. However, the analogue for even Delimiter counts must be restricted to a special subdomain of :math:`S` where the Delimiter structure is regular, i.e. the *Dialect* of a Language, :math:`D`. 

    Moreover, the direct analogue of :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>` requires the introduction of a key palindromic structural element, the *Pivot Character*, and the formal proof of a few of its key properties.