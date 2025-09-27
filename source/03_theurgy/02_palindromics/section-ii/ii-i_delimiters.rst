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
    
        \forall s \in \mathbb{S}: \Delta(s) = \Delta(s^{-1})

**Proof** Let :math:`s, t \in \mathbb{S}` such that :math:`t = s^{-1}`. Let :math:`n = l(s)`. By :ref:`String Inversion <palindromics-definition-1-2-8>`, 

.. math::

    l(t) = l(s)

.. math::

    \forall i \in N_n: t[i] = s[n - i + 1]

Therefore, since inversion does not insert or delete Characters, i.e. the number of Delimiters in :math:`s` must be equal to the number of Delimiters in :math:`t`. Therefore, 

.. math::

    \forall s,t \in \mathbb{S}: \Delta(s) = \Delta(s^{-1})

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

.. _palindromics-theorem-2-1-5:

.. topic:: Theorem 2.1.5

    If a Canonical String is equal to its own Inverse and has an odd Delimiter Count, then its central Character is a Delimiter. 

    .. math::

        \forall s \in \mathbb{S}: ((\exists n \in \mathbb{N}: \Delta(s) = 2n +1 ) \land (s = s^{-1})) \implies s[\frac{l(s)+1}{2}] = \sigma

**Proof** Let :math:`s,t \in \mathbb{S}` such that :math:`\Delta(s) = 2n + 1` for some :math:`n \in \mathbb{N}` and :math:`t = s^{-1}`. Let :math:`m = l(s)`. Let :math:`P` be the set of Delimiter indices in :math:`s`,

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

    \forall s \in \mathbb{S}: ((\exists n \in \mathbb{N}: \Delta(s) = 2n +1 ) \land (s = s^{-1})) \implies s[\frac{l(s)+1}{2}] = \sigma

∎

.. note::

    An interesting corollary to :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>` is established in the next theorem. This shows the parity of a Canonical String can be inferred from its invertibility and the parity of its Delimter Count.

.. _palindromics-theorem-2-1-6:

.. topic:: Theorem 2.1.6 

    If a Canonical String is equal to its own Inverse and has an odd number of Delimiters, then its String Length must be odd.

    .. math::

        \forall s \in \mathbb{S}: ((\exists n \in \mathbb{N}: \Delta(s) = 2n + 1) \land (s = s^{-1})) \implies (\exists i \in N_{l(s)}: l(s) = 2i - 1)

**Proof** Let :math:`s \in \mathbb{S}`. Assume :math:`\Delta(s) = 2n + 1` for some :math:`n \in \mathbb{N}`. Assume :math:`s = s^{-1}`. By :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>`,

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

    As will be shown over the course of the next theorems, the parity of the Delimter Count of a String is a *sufficient*, but not *necessary*, condition for the parity of its String Length.

    In other words, knowing an Invertible String has an odd number of Delimiters is sufficient for concluding its String Length is odd. However, an Invertible String which has an odd String Length does not necessarily have an odd number of Delimiters.

    In fact, this logic generalizes to *any* Alphabetic Character. If *any* Alphabetic Character occurs within a invertible Canonical String an odd number of times, then that is sufficient for concluding the String has an odd String Length.

.. important::

    :ref:`Theorem 2.1.5 <palindromics-theorem-1-2-5>` and :ref:`Theorem 2.1.6 <palindromics-theorem-2-1-6>` apply to *all* Strings in :math:`S`. However, the analogue for even Delimiter counts must be restricted to a special subdomain of :math:`S` where the Delimiter structure is regular, i.e. the *Dialect* of a Language, :math:`D`. 

    Moreover, the direct analogue of :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>` requires the introduction of a key palindromic structural element, the *Pivot Character*, and the formal proof of a few of its key properties.

.. _palindromics-pivots:

Pivots
------

.. _palindromics-pivot-characters:

----------------
Pivot Characters
----------------

.. _palindromics-definition-2-1-2:

.. topic:: Definition 2.1.2: Pivot Characters

    Let :math:`s \in S`.

    The Left Pivot Character of :math:`s`, denoted :math:`\overrightarrow{\omega_s}`, is defined as the Character :math:`s[\overrightarrow{i}]`, where :math:`\overrightarrow{i}` is called the *Left Pivot Character Index*, which satisies the following conditions,

    1. If :math:`l(s)` is odd, then :math:`\overrightarrow{i} = \frac{l(s) + 1}{2}`
    2. If :math:`l(s)` is even, then :math:`\overrightarrow{i} = \frac{l(s)}{2}` 

    The Right Pivot, denoted :math:`\overleftarrow{\omega_s}`, is defined as the Character :math:`s[\overleftarrow{i}]`, where :math:`\overleftarrow{i}` is called the *Right Pivot Character Index*, which satisfies the following conditions,

    1. If :math:`l(s)` is odd, then :math:`\overleftarrow{i} = \frac{l(s) + 1}{2}`
    2. If :math:`l(s)` is even, then :math:`\overleftarrow{i} = \frac{l(s) + 2}{2}` 

    The *Pivot Character*, denoted :math:`\omega_s`, is defined as the Character which satisfies the following conditions,

    1. If :math:`\overleftarrow{\omega_s} = \overrightarrow{\omega_s}`, then :math:`\omega_s = \overleftarrow{\omega_s} = \overrightarrow{\omega_s}`
    2. If :math:`\overleftarrow{\omega_s} \neq \overrightarrow{\omega_s}`, then :math:`\omega_s = \varepsilon`

**Example** Let :math:`ᚠ = \text{strap on no parts}`. Then :math:`l(ᚠ) = 17`.

Thus, since :math:`l(ᚠ) = 17` is odd,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{17 + 1}{2} = 9`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{17 + 1}{2} = 9`
- *Left Pivot Character*: :math:`\overrightarrow{\omega_{ᚠ}} = ᚠ[9] = \sigma`
- *Right Pivot Character*: :math:`\overleftarrow{\omega_{ᚠ}} = ᚠ[9] = \sigma`
- *Pivot Character*: :math:`\omega_{ᚠ} =  ᚠ[9] = \sigma`

∎

**Example** Let :math:`ᚠ = \text{no noon on}`. Then `l(ᚠ)= 10`.

Thus, since :math:`l(ᚠ)= 10` is even,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{10}{2} = 5`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{10 + 2}{2} = 6`
- *Left Pivot Character*: :math:`\overrightarrow{\omega_{ᚠ}} = ᚠ[5] = \text{o}`
- *Right Pivot Character*: :math:`\overleftarrow{\omega_{ᚠ}} = ᚠ[6] = \text{o}`
- *Pivot Character*: :math:`\omega_{ᚠ} = \text{o}`

∎

**Example** Let :math:`ᚠ = \text{draw no dray a yard onward}`. Then `l(ᚠ)= 26`.

Thus, since :math:`l(ᚠ)= 26` is even,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{26}{2} = 13`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{26 + 2}{2} = 14`
- *Left Pivot Character*: :math:`\overrightarrow{\omega_{ᚠ}} = ᚠ[13] = \sigma`
- *Right Pivot Character*: :math:`\overleftarrow{\omega_{ᚠ}} = ᚠ[14] = \text{a}`
- *Pivot Character*: :math:`\omega_{ᚠ} = \varepsilon`

∎

.. note::

    From the previous examples, it should be clear a Pivot Character of a String is a Empty Character if and only if its String Length is even. However, if a Pivot Characteris a non-Empty Character, then it cannot be concluded whether the String Length is odd or even.

    However, it should be clear that if a Pivot Character is non-Empty, it imposes certain structural constraints on the String. These structural constraints will be more fully elaborated in the next series of theorems.

.. _palindromics-theorem-2-1-7:

.. topic:: Theorem 2.1.7

    If a Canonical String has an odd number of Delimiter Characters and is equal to its own Inverse, then its Left and Right Pivot Characters are equal.

    .. math::
    
        \forall s \in \mathbb{S}: ((\exists n \in \mathbb{N}: \Delta(s) = 2n + 1) \land (s = s^{-1})) \implies (\overrightarrow{\omega_s} = \overleftarrow{\omega_s})

**Proof**: Let :math:`s \in \mathbb{S}` such that :math:`\Delta(s) = 2n + 1` for some :math:`n \in \mathbb{N}` and :math:`s = s^{-1}`. Then, by :ref:`Theorem 2.1.6 <palindromics-theorem-2-1-6>`,

.. math::

    \exists i \in N_{l(t)}: l(s) = 2i - 1

Therefore, :math:`l(s)` is odd. By :ref:`definition of Pivot Characters <palindromics-definition-2-1-2>`,

.. math::

    \overrightarrow{\omega_s} = s[\frac{l(s) + 1}{2}]

.. math::

    \overleftarrow{\omega_s} = s[\frac{l(s) + 1}{2}]

Thus,

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

Summarizing and generalizing,

.. math::

    \forall s \in \mathbb{S}: ((\exists n \in \mathbb{N}: \Delta(s) = 2n + 1)) \implies (\overrightarrow{\omega_s} = \overleftarrow{\omega_s})

∎

.. _palindromics-theorem-2-1-8:

.. topic:: Theorem 2.1.8

    If a String in the Dialect has an even String Length and is equal to its own inverse, then its Left and Right Pivot Characters cannot be Delimiters.

    .. math::

        \forall s \in D: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies ((\overrightarrow{\omega_s} \neq \sigma) \land  (\overleftarrow{\omega_s} \neq \sigma))

**Proof** The proof is similar to :ref:`Theoreom 2.1.5 <palindromics-theorem-2-1-5>`. Let :math:`s,t \in D` such that :math:`\Delta(s) = 2n` for some :math:`n \in \mathbb{N}` and :math:`t = s^{-1}` with :math:`s = t`. Let :math:`m = l(s)`. Let :math:`P` be the set of Delimiter indices in :math:`s`,

.. math::

    P = \{ i \mid s[i] = \sigma \}

Then :math:`\lvert P \rvert = \Delta(s) = 2n` by assumption.

By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    t[i] = s[m - i + 1]

There are two cases to consider, :math:`l(s)` is even or :math:`l(s)` is odd.

.. EVEN CASE 

:underline:`Case I`: :math:`l(s) = m` is even.

Assume, for the sake of contradiction, :math:`s[\frac{l(s)}{2}] = s[\frac{m}{2}]= \sigma`. Then, every Delimiter must have a symmetric pair in :math:`P`.

.. math::

    t[i] = s[m - i  + 1]

So, using :math:`i = \frac{m}{2}`

.. math::

    t[\frac{m}{2}] = s[\frac{m}{2} + 1]

Therefore, 

.. math::

    s[\frac{m}{2}] = \sigma

.. math::

    s[\frac{m}{2} + 1] = \sigma

That is, two consecutive Characters in :math:`s` are Delimiters. But this is impossible if :math:`s \in D`. Therefore, it must be the case :math:`s[\frac{l(s)}{2}] \neq \sigma`. Likewise, :math:`s[\frac{l(s)}{2} + 1] \neq \sigma`. Since :math:`l(s)` is even, by :ref:`definition of Pivot Characters <palindromics-definition-2-1-2>`,

.. math::

    s[\frac{l(s) + 2}{2}] = \overleftarrow{\omega_s}

.. math::

    s[\frac{l(s)}{2}] = \overrightarrow{\omega_s}

It follows from this,

.. math::

    (\overleftarrow{\omega_s} \neq \sigma) \land (\overrightarrow{\omega_s} \neq \sigma)

.. ODD CASE 

:underline:`Case II`: :math:`l(s) = m` is odd. 

By :ref:`Theorem 2.1.7 <palindromics-theorem-2-1-7>`,

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s} \quad \text{ (1) }

Where, by :ref:`definition of Pivot Characters <palindromics-definition-2-1-2>`,

.. math::
    
    \omega_s = \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

.. math::

    \omega_s = s[\frac{l(s) + 1}{2}]

Assume, for the sake of contradiction, :math:`\omega_s = \sigma`. Then, by :ref:`Containment <palindromics-definition-1-2-5>`

.. math::

    s = (u)(\sigma)(v)

From the :ref:`definition of Delimiter Count <palindromics-definition-2-1-1>`,

.. math::

    \Delta(s) = \Delta(u) + \Delta(v) + 1 = \Delta(uv) + 1

Where the last equality follows from :ref:`Theorem 2.1.4 <palindromics-theorem-2-1-4>`. Thus, since :math:`\Delta(s)` is even, the number of Delimiters in :math:`uv` is odd,

.. math::

    \Delta(uv) = 2n - 1

Furthermore, by repeated application of :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>`

.. math::

    l(s) = l(u) + l(\sigma) + l(v) = l(u) + l(v) + 1 = l(uv) + 1

Thus,

.. math::
    
    l(uv) = l(s) - 1 = m - 1 \quad \text{ (2) }
 
From which it follows :math:`l(uv)` is even.

By repeated application of :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-10>`

.. math::

    s^{-1} = ((u)(\sigma)(v))^{-1} = (v^{-1})(\sigma^{-1})(u^{-1})

By assumption, :math:`s = s^{-1}`. Using :math:`\sigma^{-1} = \sigma`, the previous equation becomes,

.. math::

    (u)(\sigma)(v) = (v^{-1})(\sigma)(u^{-1})

Note :math:`\sigma` in :math:`(u)(\sigma)(v)` occupies the same Character Index as the :math:`\sigma` in :math:`(v^{-1})(\sigma)(u^{-1})`, since :math:`\omega_s = s[\frac{l(s) + 1}{2}] = \sigma` and :math:`\omega_{s^{-1}} = s[\frac{l(s) + 1}{2}] = \sigma`. By the Left and Right Cancellation property of :ref:`Equality Axiom <palindromics-axiom-ii>`, it follows,

.. math::

    u = v^{-1}

And 

.. math::

    v = u^{-1}

Therefore,

.. math::

    uv = (v^{-1})(u^{-1}) = (uv)^{-1}

Now, consider what has been shown of :math:`uv`. :math:`\Delta(uv) = 2n - 1` and :math:`uv = (uv)^{-1}`. By :ref:`Theorem 2.1.6 <palindromics-theorem-2-1-6>`, this implies 

.. math::

    \exists j \in N_{l(uv)}: l(uv) = 2j - 1

But this contradicts (2), which states :math:`l(uv)` is even, which in turn followed directly from the assumption :math:`l(s)` is odd. Therefore, the only possibility is :math:`\omega_s \neq \sigma`. Therefore, from (1),

.. math::

    \overleftarrow{\omega_s} \neq \sigma

.. math::

    \overrightarrow{\omega_s} \neq \sigma

∎

.. _palindromics-theorem-2-1-9:

.. topic:: Theorem 2.1.9

    .. math::

        \forall s \in \mathbb{S}: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

**Proof** Let :math:`s \in \mathbb{S}` such that :math:`s = s^{-1}`. Let :math:`t \in D` such :math:`t = s^{-1}` and :math:`\Delta(s) = 2n` for some :math:`n \in \mathbb{N}`. Let :math:`m = l(s)`. Let :math:`P` be the set of Delimiter indices in :math:`s`,

.. math::

    P = \{ i \mid s[i] = \sigma \}

Then :math:`\lvert P \rvert = \Delta(s) = 2n` by assumption.

By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    t[i] = s[m - i + 1]

There are two cases to consider, :math:`l(s)` is even or :math:`l(s)` is odd.

.. EVEN CASE 

:underline:`Case I`: :math:`l(s) = m` is even.

By :ref:`Definition of Pivot Characters <palindromics-definition-2-1-2>`,

.. math::

    \overrightarrow{i} = \frac{l(s)}{2} = \frac{m}{2} \quad \text{ (1) }

.. math::

    \overleftarrow{i} = \frac{l(s)}{2} + 1  = \frac{m}{2} + 1 \quad \text{ (2) }

Therefore, the Pivot Characters must be consecutive Characters. 

Since :math:`\lvert P \rvert`, each index :math:`i` has a symmetric pair given by the inversion :math:`m - i + 1`,

.. math::

    \overrightarrow{i}_{\text{pair}} = m - \overrightarrow{i} + 1 = \frac{m}{2} + 1 \quad \text{ (3) }

.. math:: 

    \overleftarrow{i}_{\text{pair}} = m - \overleftarrow{i} + 1 = \frac{m}{2} \quad \text{ (4) }

Therefore, from (1) and (4) the Left Pivot Character Index pairs with the Right Pivot Character Index, and from (2) and (3) the Right Pivot Character Index pairs with Left Pivot Character Index,

.. math::

    \overrightarrow{i}_{\text{pair}} = \overleftarrow{i}

.. math::

    \overleftarrow{i}_{\text{pair}} = \overrightarrow{i}

By :ref:`definition of String Inversion <palindromics-definition-1-2-8>`,

.. math::

    t[\overrightarrow{i}] = s[\overrightarrow{i}_{\text{pair}}] = s[\overleftarrow{i}]

.. math::

    t[\overleftarrow{i}] = s[\overleftarrow{i}_{\text{pair}}] = s[\overrightarrow{i}]

Plugging in values,

.. math::

    t[\frac{m}{2}] = s[\frac{m}{2} + 1]

.. math::

    t[\frac{m}{2} +1] = s[\frac{m}{2}]

Using the assumption :math:`s = t`, it follows,

.. math::

    s[\frac{m}{2} + 1] = s[\frac{m}{2}]

Therefore,

.. math::

    \overleftarrow{\omega_s} = \overrightarrow{\omega_s}

.. ODD CASE 

:underline:`Case I`: :math:`l(s) = m` is odd.

This follows directly from the :ref:`definition of Pivot Characters <palindromics-definition-2-1-2>`. Therefore, both cases are established. Summarizing and generalizing,

.. math::

    \forall s \in \mathbb{S}: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

∎

.. _palindromics-theorem-2-1-10:

.. topic:: Theorem 2.1.10 

    If a Canonical String is equal to its own Inverse, then its Pivot Character is non-empty.
    
    .. math::

        \forall s \in \mathbb{S}: (s = s^{-1}) \implies (\omega_s \neq \varepsilon)

**Proof** Let :math:`s \in \mathbb{S}` such that :math:`s = s^{-1}`. 

By the laws of arithmetic, either :math:`\Delta(s)` is odd or it is even. 

If :math:`\Delta(s)` is odd, then by :ref:`Theorem 2.1.7 <palindromics-theorem-2-1-7>`, 

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

If :math:`\Delta(s)` is even, then by :ref:`Theorem 2.1.9 <palindromics-theorem-2-1-7>`,

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

In either case, the conclusion follows. Thus, summarizing and generalizing,

.. math::

    \forall s \in \mathbb{S}: (s = s^{-1}) \implies (\omega_s \neq \varepsilon)

∎

.. note::

    :ref:`Theorem 2.1.10 <palindromics-theorem-2-1-10>` establishes that all invertible Strings in the Canon have a non-Empty Pivot Character. As an immediate corollary to this theorem, if a canonical String has an Empty Pivot Character, then it cannot be invertible.

    Furthemore, the contrapositive establishes a sufficient condition for *non-invertibiility*. In other words, if :math:`\omega_s = \varepsilon` it can be concluded :math:`s` is uninvertible. 

.. _palindromics-pivot-words:

-----------
Pivot Words
-----------

.. _palindromics-definition-2-1-3:

.. topic:: Definition 2.1.3: Pivot Word

    Let :math:`\zeta \in C`.

    The Left Pivot Word of :math:`\zeta`, denoted :math:`\overrightarrow{\Omega_{\zeta}}`, is defined as the Word :math:`\zeta[[\overrightarrow{j}]]`, where :math:`\overrightarrow{j}` is called the *Left Pivot Word Index*, which satisies the following conditions,

    1. If :math:`\Lambda(\zeta)` is odd, then :math:`\overrightarrow{j} = \frac{\Lambda(\zeta) + 1}{2}`
    2. If :math:`\Lambda(\zeta)` is even, then :math:`\overrightarrow{j} = \frac{\Lambda(\zeta)}{2}` 

    The Right Pivot Word, denoted :math:`\overleftarrow{\Omega_{\zeta}}`, is defined as the Word :math:`\zeta[[\overleftarrow{j}]]`, where :math:`\overleftarrow{j}` is called the *Right Pivot Word Index*, which satisfies the following conditions,

    1. If :math:`\Lambda(\zeta)` is odd, then :math:`\overleftarrow{j} = \frac{\Lambda(\zeta) + 1}{2}`
    2. If :math:`\Lambda(\zeta)` is even, then :math:`\overleftarrow{i} = \frac{\Lambda(\zeta) + 2}{2}` 

    The *Pivot Word*, denoted :math:`\Omega_{\zeta}`, is defined as the Character which satisfies the following conditions,

    1. If :math:`\overleftarrow{\Omega_{\zeta}} = \overrightarrow{\Omega_{\zeta}}`, then :math:`\Omega_{\zeta} = \overleftarrow{\Omega_{\zeta}} = \overrightarrow{\Omega_{\zeta}}`
    2. If :math:`\overleftarrow{\Omega_{\zeta}} \neq \overrightarrow{\Omega_{\zeta}}`, then :math:`\Omega_{\zeta} = \varepsilon`

.. note::

    In essence, the existence of a Pivot Character or Pivot Word in a Sentence is a property of a String's *self-invertibility*, i.e. :math:`s = s^{-1}`. All self-invertible Strings possess the property "*has a Pivot Character and Word*", but having this propery is not a *sufficient* for establishing self-invertibility.

    The existence of a Pivot Character and Pivot Word in a Sentence define a class of Sentences in the Corpus. However, the relationship between Pivot Characters and Pivot Words is deceptively subtle, as these next examples illustrate. 

**Example** Let `ᚠ_1 = \text{a crowd flowed over london bridge}`. Note :math:`\Lambda(ᚠ_1) = 6` and :math:`l(ᚠ_1) = 33`

The Pivot Word calculations proceed as follows,

- *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{6}{2} = 3`
- *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{8}{2} = 4`
- *Left Pivot Word*: :math:`ᚠ_1[[3]] = \overrightarrow{\Omega_{ᚠ_1}} = \text{flowed}`
- *Right Pivot Word*: :math:`ᚠ_1[[4]] = \overleftarrow{\Omega_{ᚠ_1}} = \text{over}`
- *Pivot Word*: :math:`\Omega_{ᚠ_1} = \varepsilon`

The Pivot Character calculations proceed as follows,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{34}{2} = 17`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{34}{2} = 17`
- *Left Pivot Character*: :math:`ᚠ_1[17]= \text{v}`
- *Right Pivot Character*: :math:`ᚠ_1[17]= \text{v}`
- *Pivot Character*: :math:`\omega_{ᚠ_1} = \text{v}`

Let :math:`ᚠ_2 = \text{i had not thought death had undone so many}`. Note :math:`\Lambda(ᚠ_2) = 9` and :math:`l(ᚠ_2) =  42`

The Pivot Word calculations proceed as follows,

- *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{10}{2} = 5`
- *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{10}{2} = 5`
- *Left Pivot Word*: :math:`ᚠ_2[[3]] = \overrightarrow{\Omega_{ᚠ_2}} = \text{death}`
- *Right Pivot Word*: :math:`ᚠ_2[[4]] = \overleftarrow{\Omega_{ᚠ_2}} = \text{death}`
- *Pivot Word*: :math:`\Omega_{ᚠ_2} = \text{death}`

The Pivot Character calculations proceed as follows,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{42}{2} = 21`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{44}{2} = 22`
- *Left Pivot Character*: :math:`ᚠ_2[21]= \text{a}`
- *Right Pivot Character*: :math:`ᚠ_2[22]= \text{t}`
- *Pivot Character*: :math:`\omega_{ᚠ_2} = \varepsilon`

Let :math:`ᚠ_3 = \text{no radar on}`. Note :math:`\Lambda(ᚠ_3) = 3` and :math:`l(ᚠ_3) = 11`

The Pivot Word calculations proceed as follows,

- *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{4}{2} = 2`
- *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{4}{2} = 2`
- *Left Pivot Word*: :math:`ᚠ_3[[2]] = \overrightarrow{\Omega_{ᚠ_3}} = \text{radar}`
- *Right Pivot Word*: :math:`ᚠ_3[[4]] = \overleftarrow{\Omega_{ᚠ_3}} = \text{radar}`
- *Pivot Word*: :math:`\Omega_{ᚠ_3} = \text{radar}`

The Pivot Character calculations proceed as follows,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{12}{2} = 6`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{12}{2} = 6`
- *Left Pivot Character*: :math:`ᚠ_3[6]= \text{d}`
- *Right Pivot Character*: :math:`ᚠ_3[6]= \text{d}`
- *Pivot Character*: :math:`\omega_{ᚠ_3} = \text{d}`

Let :math:`ᚠ_4 = \text{tell me stories}`. Note :math:`\Lambda(ᚠ_4) = 3` and :math:`l(ᚠ_4) = 15`

The Pivot Word calculations proceed as follows,

- *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{4}{2} = 2`
- *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{4}{2} = 2`
- *Left Pivot Word*: :math:`ᚠ_4[[2]] = \overrightarrow{\Omega_{ᚠ_4}} = \text{me}`
- *Right Pivot Word*: :math:`ᚠ_4[[4]] = \overleftarrow{\Omega_{ᚠ_4}} = \text{me}`
- *Pivot Word*: :math:`\Omega_{ᚠ_4} = \text{radar}`

The Pivot Character calculations proceed as follows,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{16}{2} = 8`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{16}{2} = 8`
- *Left Pivot Character*: :math:`ᚠ_4[6]= \sigma`
- *Right Pivot Character*: :math:`ᚠ_4[6]= \sigma`
- *Pivot Character*: :math:`\omega_{ᚠ_4} = \sigma`

Let :math:`ᚠ_5 = \text{emit naps noon span time}`. Note :math:`\Lambda(ᚠ_5) = 5` and :math:`l(ᚠ_5) = 24`.

The Pivot Word calculations proceed as follows,

- *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{6}{2} = 3`
- *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{6}{2} = 3`
- *Left Pivot Word*: :math:`ᚠ_5[[2]] = \overrightarrow{\Omega_{ᚠ_5}} = \text{noon}`
- *Right Pivot Word*: :math:`ᚠ_5[[4]] = \overleftarrow{\Omega_{ᚠ_5}} = \text{noon}`
- *Pivot Word*: :math:`\Omega_{ᚠ_5} = \text{noon}`

The Pivot Character calculations proceed as follows,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{24}{2} = 12`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{26}{2} = 13`
- *Left Pivot Character*: :math:`ᚠ_5[12]= \text{o}`
- *Right Pivot Character*: :math:`ᚠ_5[6]= \text{o}`
- *Pivot Character*: :math:`\omega_{ᚠ_5} = \text{o}`

∎

.. _palindromics-theorem-2-1-11:

.. topic:: Theorem 2.1.11

    .. math::

        \forall \zeta \in C: (\exists i \in \mathbb{N}: \Delta(\zeta) = 2i) \implies (\Omega_{\zeta} \neq \varepsilon)

**Proof** Let :math:`\zeta \in C`. Assume :math:`\Delta(\zeta) = 2i` for some :math:`i \in \mathbb{N}`. Then, by :ref:`Theroem 2.1.1 <palindromics-theorem-2-1-1>`,

.. math::

    \Lambda(\zeta) = 2i + 1.

Thus, :math:`\Lambda(\zeta)` is odd. By the :ref:`definition of Pivot Words <palindromics-definition-2-1-3>`,

.. math::

    \overrightarrow{j} = \frac{\Lambda(\zeta) + 1}{2}

.. math::

    \overleftarrow{j} = \frac{\Lambda(\zeta) + 1}{2}`

Thus, 

.. math::

    \overrightarrow{\Omega_{\zeta}} = \overleftarrow{\Omega_{\zeta}}

.. math::

    \Omega_{\zeta} \neq \varepsilon

Therefore, summarizing and generalizing,

.. math::

    \forall \zeta \in C: (\exists i \in \mathbb{N}: \Delta(\zeta) = 2i) \implies (\Omega_{\zeta} \neq \varepsilon)

∎

.. _palindromics-theorem-2-1-12:

.. topic:: Theorem 2.1.12

    .. math::

        \forall \zeta \in C: (\exists i \in \mathbb{N}: \Delta(\zeta) = 2i + 1) \land (\zeta = \zeta^{-1}) \implies (\overrightarrow{\Omega_{\zeta}} = \overleftarrow{\Omega_{\zeta}}^{-1})

**Proof** Let :math:`\zeta \in C`. Assume :math:`\zeta = \zeta^{-1}` with :math:`\Delta(\zeta) = 2i + 1` for some :math:`i \in \mathbb{N}`.

Since :math:`\zeta = \zeta^{-1}`, it follows :math:`\zeta^{-1} \in C`. By :ref:`definition of Invertible Sentences <palindromics-definition-1-4-3>`, it follows :math:`\zeta \in K`. By :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>`,

.. math::

    {\zeta}^{-1}[[j]] = (\zeta[[\Lambda(\zeta) - j + 1]])^{-1}

For all :math:`j \in N_{\Lambda(\zeta)}`. 

Furthermore, since :math:`\Delta(\zeta)` is odd and :math:`\zeta = \zeta^{-1}`, it follows from :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>` and the :ref:`definition of Pivot Characters <palindromics-definition-2-1-2>`,

.. math::

    \omega_{\zeta} = \sigma

.. Going to need partial sentences here, I think.

.. .................................................................................

TODO

.. .................................................................................

.. _palindromics-theorem-2-1-13:

.. topic:: Theorem 2.1.13

    .. math::

        \forall \zeta \in C: (\exists i \in \mathbb{N}: \Delta(\zeta) = 2i) \land (\zeta = \zeta^{-1}) \implies (\Omega_{\zeta^{-1}} = {\Omega_{\zeta}}^{-1})

**Proof** Let :math:`\zeta \in C`. Assume :math:`\Delta(\zeta) = 2i` for some :math:`i \in \mathbb{N}`. Then, by :ref:`Theroem 2.1.11 <palindromics-theorem-2-1-1>`,

.. math::

    \Omega_{\zeta} \neq \varepsilon

Where the Pivot Word occurs at the Word Index, :math:`k = \frac{\Lambda(\zeta) + 1}{2}`, i.e. 

.. math:: 

    \Omega_{\zeta} = \zeta[[\frac{\Lambda(\zeta) + 1}{2}]]

Since :math:`\zeta = \zeta^{-1}`, it follows :math:`\zeta^{-1} \in C`. By :ref:`definition of Invertible Sentences <palindromics-definition-1-4-3>`, it follows :math:`\zeta \in K`. By :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>`,

.. math::

    {\zeta}^{-1}[[j]] = (\zeta[[\Lambda(\zeta) - j + 1]])^{-1}

For all :math:`j \in N_{\Lambda(\zeta)}`, including the Pivot Word Index. Substituting in the Pivot Word Index, the expression for the index on the RHS simplifies to,

.. math::

    \Lambda(\zeta) - \frac{\Lambda(\zeta) + 1}{2} + 1  = \frac{\Lambda(\zeta) + 1}{2}

Thus, 

.. math::

    {\zeta}^{-1}[[\frac{\Lambda(\zeta)+1}{2}]] = (\zeta[[\frac{\Lambda(\zeta) + 1}{2}]])^{-1}

Since :math:`\Lambda(\zeta^{-1}) = \Lambda(\zeta)`, i.e. their Pivot Word Indices are equal, this means the Inverse of the Pivot Word is the Pivot Word of the Inverse Sentence,

.. math::

    \Omega_{\zeta^{-1}} = {\Omega_{\zeta}}^{-1}

.. .................................................................................

TODO

.. .................................................................................

.. _palindromics-definition-2-1-4:

.. topic:: Definition 2.1.4: Subvertible Sentences

    The set of Subvertible Sentences, denoted :math:`\cancel{J}`, is defined as the set of Sentences which satisfy the open formula,

    .. math::

        \zeta \in \cancel{J} \equiv ((\Omega_\zeta \neq \varepsilon) \land (\omega_\zeta \neq \varepsilon))