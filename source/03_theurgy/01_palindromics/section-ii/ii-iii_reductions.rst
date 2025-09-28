
.. _palindromics-section-ii-iii:

Section II.III: Reductions
==========================

.. _palindromics-reduction-definition:

Definition & Examples
---------------------

.. _palindromics-definition-2-3-1:

.. topic:: Definition 2.3.1: σ-Reduction

    Let :math:`s \in S`. The σ-Reduction of :math:`s`, denoted :math:`\varsigma(s)`, is defined inductively with the following schema,

    - Basis: 
        - :math:`\varsigma(\sigma) = \varepsilon`
        - If :math:`\neg(\sigma \subset_s s)`, then :math:`\varsigma(s) = s`
    - Induction:
        - If :math:`s = (u)(\sigma)(v)` for any :math:`u, v \in S` where :math:`\neg(\sigma \subset_s u)`, :math:`\varsigma(s) = \varsigma(uv)`

    :math:`\varsigma(s)` is said to be *reduced* from, or a *reduction* of, :math:`s`.

**Example** :math:`ᚠ = \text{the widening circles into nothing gone}`. Consider :math:`\varsigma(ᚠ)`

Let :math:`u_1 = \text{the}` and :math:`v_1 = \text{widening circles into nothing gone}`. Let :math:`w_1 = (u_1)(v_1)`. Then, :math:`ᚠ = (u_1)(\sigma)(v_1)`. By the Induction clause :ref:`of σ-Reduction <palindromics-definition-2-3-1>`,

.. math::

    \varsigma(ᚠ) = \varsigma((u_1)(v_1)) = \varsigma(w_1)

Let :math:`u_2 = \text{thewidening}` and :math:`v_2 = \text{circles into nothing gone}`. Let :math:`w_2 = (u_2)(v_2)`. Then :math:`w_1 = (u_2)(\sigma)(v_2)`. By the Induction clause,

.. math::

    \varsigma(w_1) = \varsigma((u_2)(v_2)) = \varsigma(w_2)

Let :math:`u_3 = \text{thewideningcircles}` and :math:`v_3 = \text{into nothing gone}`. Let :math:`w_3 = (u_3)(v_3)`. Then :math:`w_2 = (u_3)(\sigma)(v_3)`. By the Induction clause,

.. math::

    \varsigma(w_2) = \varsigma((u_3)(v_3)) = \varsigma(w_3)

Let :math:`u_4 = \text{thewideningcirclesinto}` and :math:`v_4 = \text{nothing gone}`. Let :math:`w_4 = (u_4)(v_4)`. Then :math:`w_3 = (u_4)(\sigma)(v_4)`. By the Induction clause,

.. math::

    \varsigma(w_3) = \varsigma((u_4)(v_4)) = \varsigma(w_4)

Let :math:`u_5 = \text{thewideningcirclesintonothing}` and :math:`v_5 = \text{gone}`. Let :math:`w_5 = (u_5)(v_5)`. Then :math:`w_4 = (u_5)(\sigma)(v_5)`. By the Induction clause,

.. math::

    \varsigma(w_4) = \varsigma((u_5)(v_5)) = \varsigma(w_5)

But :math:`neg(\sigma \subset_s w_5)`, therefore by the Basis clause,

.. math::

    \varsigma(w_5) = w_5

Working back up through the recursion, the original reduction is found,

.. math::

    \varsigma(ᚠ) = \text{"thewideningcirclesintonothinggone"}

∎

.. _palindromics-reduction-properties:

Properties
----------

.. note::

    All of these properties follow from the definition of :ref:`σ-Reduction <palindromics-definition-2-3-1>` and the indicated axiom or theorem, and they are all understood to be quantified over :math:`S`.

1. From the :ref:`definition of String Length <palindromics-definition-1-2-2>`: :math:`l(\varsigma(\sigma)) = l(\varepsilon) = 0`
2. From the :ref:`Discovery Axiom <palindromics-axiom-v>`: :math:`\varsigma(\alpha) = \alpha`
3. From the :ref:`Discovery Axiom <palindromics-axiom-v>` and the :ref:`definition of String Length <palindromics-definition-1-2-2>`: :math:`l(\varsigma(\alpha)) = l(\alpha)`
4. From the :ref:`definition of String Length <palindromics-definition-1-2-2>`: :math:`l(\varsigma(s)) \leq l(s)`
5. From the :ref:`definition of Concatenation <palindromics-definition-1-2-1>` and the :ref:`Closure Axiom <palindromics-axiom-iii>`: :math:`\varsigma(s) \in S`
6. From the :ref:`definition of the Delimiter Count <palindromics-definition-2-1-1>`: :math:`\Delta(\varsigma(s)) = 0`

.. _palindromics-reduction-theorems:

Theorems
--------

.. _palindromics-theorem-2-3-1:

.. topic:: Theorem 2.3.1

    The Reduction of Concatenations is the Concatenation of Reductions.

    .. math::

        \forall s,t \in S: \varsigma(st) = (\varsigma(s))(\varsigma(t))

**Proof** Let :math:`s,t \in S`.

By :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`, there are only three cases to consider.

- Case I: :math:`\neg(\sigma \subset_s st)`
- Case II: :math:`\neg(\sigma \subset_s s) \land (\sigma \subset_s t)`
- Case III: :math:`(\sigma \subset_s s) \land \neg(\sigma \subset_s t)`

Note :math:`(\sigma \subset_s st)` is included in the disjunction of Case II and III.

.. CASE I

:underline:`Case I`: :math:`\neg(\sigma \subset_s st)`

By the contrapositive of :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`,

.. math::

    \neg(\sigma \subset_s st) \implies (\neg(\sigma \subset_s s) \land \neg(\sigma \subset t))

Thus, by assumption, :math:`\neg(\sigma \subset_s s)` and :math:`\neg(\sigma \subset_s t)` are true.

From this and the :ref:`definition of Reductions <palindromics-definition-2-3-1>`, it follows,

.. math::

    \varsigma(s) = s

.. math::

    \varsigma(t) = t

.. math::

    \varsigma(st) = st

Thus,

.. math::

    \varsigma(st) = st = (\varsigma(s))(\varsigma(t))

.. CASE II

:underline:`Case II` :math:`\neg(\sigma \subset_s s) \land (\sigma \subset_s t)`

By assumption and :ref:`Containment <palindromics-definition-1-2-5>`, for some :math:`u,v \in S` with :math:`\neg(\sigma \subset_s u)`,

.. math::

    t = (u)(\sigma)(v)

By the Induction clause of :ref:`Reduction <palindromics-definition-2-3-1>`,

.. math::

    \varsigma(t) = (u)(\varsigma(v))

Now, consider :math:`st`

.. math::

    st = (s)(u)(\sigma)(v)

By the contrapositive of :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`, 

.. math::

    \neg(\sigma \subset_s s) \land \neg(\sigma \subset_s u) \implies \neg(\sigma \subset_s su)

Thus, :math:`\neg(\sigma \subset_s su)`. From this, it can be concluded,

.. math::

    \varsigma(s) = s 

.. math::

    \varsigma(u) = u

.. math::
    
    \varsigma(su) = su

Putting these three equalities together,

.. math::

    \varsigma(su) = (\varsigma(s))(\varsigma(u))

By the Induction clause :ref:`Reduction <palindromics-definition-2-3-1>`,

.. math::

    \varsigma(st) = \varsigma((s)(u)(\sigma)(v)) = (su)\varsigma(v)

.. math::

    = (s)(u\varsigma(v)) = \varsigma(s)\varsigma(t)

:underline:`Case III`

The proof for Case III is identical to Case II, except :math:`s` is decomposed into :math:`s = (u)(\varsigma)(v)` with :math:`\neg(\sigma \subset_s v)`

Thus all three cases are established. Summarizing and generalizing,

.. math::

    \forall s \in S: \varsigma(st) = (\varsigma(s))(\varsigma(t))

∎

.. _palindromics-theorem-2-3-2:

.. topic:: Theorem 2.3.2

    There are no Delimiters in a String if and only if it is equal to its own Reduction.

    .. math::

       \forall s \in S: \Delta(s) = 0 \equiv \varsigma(s) = s

**Proof** Let :math:`s \in S`.

(:math:`\rightarrow`) Assume :math:`\Delta(s) = 0`. By the :ref:`properties of the Delimiter Count <palindromics-delimiter-count-properties>`,

.. math::

    \neg(\sigma \subset_s s)

Therefore, by the Basis clause of :ref:`Reduction <palindromics-definition-2-3-1>`,

.. math::

    \varsigma(s) = s

(:math:`\leftarrow`) Assume :math:`\varsigma(s) = s`. By the :ref:`properties of Reductions <palindromics-reduction-properties>`, 

.. math::
    
    \Delta(\varsigma(s)) = 0
    
But by assumption,

.. math::

    \Delta(s) = 0

Thus equivalence is established. Summarizing and generalizing,

.. math::

    \forall s \in S: \Delta(s) = 0 \equiv \varsigma(s) = s

∎

.. warning::
    
    The next theorem is quantified over the :math:`\mathbb{S}`, **not** :math:`S`.

.. .................................................................................

TODO

.. .................................................................................

.. _palindromics-theorem-2-3-4:

.. topic:: Theorem 2.3.4

    The Inverse of a Reduction is the Reduction of the Inverse. 

    .. math::

        \forall s \in \mathbb{S}: (\varsigma(s))^{-1} = \varsigma(s^{-1})

**Proof** Let :math:`s \in \mathbb{S}`. The proof proceeds by induction on the number of Delimiters in :math:`s`.

.. BASIS 

:underline:`Basis` Let :math:`\neg(\sigma \subset_s s)`; that is, assume there are no Delimiters in :math:`s` (:math:`\Delta(s) = 0`). By :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-11>` and the fact :math:`\sigma^{-1} = \sigma`,

.. math::

    \neg(\sigma \subset_s s) \equiv \neg(\sigma \subset_s s^{-1})

Consider :math:`(\varsigma(s))^{-1}`. By the Basis clause of :ref:`the Reduction definition <palindromics-definition-2-3-1>` and the Basis assumption,

.. math::

    \varsigma(s) = s

Therefore,

.. math::

    (\varsigma(s))^{-1} = s^{-1}

Consider :math:`\varsigma(s^{-1})`. By :math:`\neg (\sigma \subset_s s^{-1})` and the Basis clause of :ref:`the Reduction definition <palindromics-definition-2-3-1>`, 

.. math::

    \varsigma(s^{-1}) = s^{-1}

.. INDUCTION 

:underline:`Induction` Assume for any :math:`s` with :math:`\Delta(s) = k` for some :math:`k \geq 1` that :math:`(\varsigma(s))^{-1} = \varsigma(s^{-1})`. 

Let :math:`u \in S` such that :math:`\Delta(u) = k + 1`. Let :math:`u = (v)(\sigma)(w)`, where :math:`\Delta(v) = 0` and :math:`\Delta(w) = k`. By Induction clause of :ref:`Reduction <palindromics-definition-2-3-1>`,

.. math::

    \varsigma(u) = \varsigma(vw) = \varsigma(v)\varsigma(w)

Where the last equality follows from :ref:`Theorem 2.2.1 <palindromics-theorem-2-3-1>`. Consider :math:`(\varsigma(u))^{-1}`.By application of :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-10>`,

.. math::

    (\varsigma(u))^{-1} = (\varsigma(w))^{-1}(\varsigma(v))^{-1} \quad \text{ (1) }

Consider :math:`u^{-1}`. By application of :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-10>`,

.. math::

    u^{-1} = (w^{-1})(\sigma^{-1})(v^{-1})

By Induction clause of :ref:`Reduction <palindromics-definition-2-3-1>`,

.. math::

    \varsigma(u^{-1}) = \varsigma((w^{-1})(v^{-1}))

From :ref:`Theorem 2.2.1 <palindromics-theorem-2-3-1>`

.. math::

    \varsigma(u^{-1}) = \varsigma(w^{-1})\varsigma(v^{-1}) \quad \text{ (2) }

Since :math:`\Delta(w) = k` satisfies the inductive hypothesis,

.. math::

    \varsigma(w^{-1}) = \varsigma(w)^{-1} \quad \text{ (3) }

Consider :math:`\varsigma(v)`. :math:`\Delta(v) = 0` by construction, thus by :ref:`Theorem 2.2.2 <palindromics-theorem-2-3-2>`,

.. math::

    \varsigma(v) = v \quad \text{ (4) }

Likewise, since :math:`v` and :math:`v^{-1}` contain the same Characters,

.. math::

    \varsigma(v^{-1}) = v^{-1}

From (4) and :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

   (\varsigma(v))^{-1} = v ^{-1}

From which it follows,

.. math:: 

    \varsigma(v^{-1}) = (\varsigma(v))^{-1} \quad \text{ (5) }

Now, (3) and (5) taken together with (1) and (2) imply,

.. math::

    (\varsigma(u))^{-1} = \varsigma(u^{-1})

Thus, the induction is established. Summarizing and generalizing,

.. math::

    \forall s \in S: \varsigma(s^{-1}) = (\varsigma(s))^{-1}

∎

.. _palindromics-theorem-2-3-5:

.. topic:: Theorem 2.3.5

    σ-Reductions are idempotent.

    .. math::

        \forall s \in S: \varsigma(\varsigma(s)) = \varsigma(s)

**Proof** Let :math:`s, t \in S` such that :math:`t = \varsigma(s)`. By THE :ref:`properties of Reductions <palindromics-reduction-properties>`, :math:`\Delta(t) = 0`. Therefore, by :ref:`Theorem 2.2.2 <palindromics-theorem-2-3-2>`, :math:`\varsigma(t) = t`. Thus, substituting in :math:`t`, :math:`\varsigma(\varsigma(s)) = \varsigma(s)`. Summarizing and generalizing, 

.. math::

    \forall s \in S: \varsigma(\varsigma(s)) = \varsigma(s)

∎

.. _palindromics-theorem-2-3-6:

.. topic:: Theorem 2.3.6

    One String is contained in another if and only if their σ-Reductions are contained in one another.

    .. math::

        \forall s,t \in S: s \subset_s t \implies \varsigma(s) \subset_s \varsigma(t)

**Proof** Let :math:`s, t \in S` such that :math:`s \subset_s t`. By :ref:`Containment <palindromics-definition-1-2-5>`, for some :math:`u,v \in S`,

.. math::

    t = (u)(s)(v)

Consider :math:`\varsigma(t)`. By repeated application of :ref:`Theorem 2.2.1 <palindromics-theorem-2-2-1>`,

.. math::

    \varsigma(t) = \varsigma((u)(s)(v)) = (\varsigma(u))(\varsigma(s))(\varsigma(v))

Since :math:`\varsigma(u)` and :math:`\varsigma(v)` by the closure :ref:`property of Reductions <palindromics-reduction-properties>`, it follows,

.. math::

    \varsigma(s) \subset_s \varsigma(t)

∎

.. important::

    :ref:`Theorem 2.2.5 <palindromics-theorem-2-3-6>` is a unidirectional implication, *not* an equivalence. Consider,

    .. math::

        ᚠ = rob or borrow 

    .. math::

        a = orb

    Clearly, :math:`\neg(a \subset_s ᚠ)`, due to the Delimiters in :math:`ᚠ`. However,

    .. math::

        \varsigma(ᚠ) = roborborrow

    .. math::

        \varsigma(a) = orb

    So, :math:`\varsigma(a) \subset_s \varsigma(ᚠ)`.

.. _palindromics-theorem-2-3-7:

.. topic:: Theorem 2.3.7

    Every Word in a Sentence is contained in its σ-Reduction.

    .. math::

        \forall \zeta \in C: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \subset_s \varsigma(\zeta)

**Proof** Let :math:`\zeta \in C`. Clearly :math:`\zeta[[i]] \subset_s \zeta` for any :math:`i \in N_{\Lambda(\zeta)}`. From this and :ref:`Theorem 2.2.5 <palindromics-theorem-2-3-6>`, it can be concluded,

.. math::

    \varsigma(\zeta[[i]]) \subset_s \varsigma(\zeta)


By the :ref:`properties of Reductions <palindromics-reduction-properties>`,

.. math::

    \varsigma(\zeta[[i]]) = \zeta[[i]]

Therefore, 

.. math::

    \zeta[[i]] \subset_s \varsigma(\zeta)

Summarizing and generalizing,

.. math::

    \forall \zeta \in C: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \subset_s \varsigma(\zeta)

◼︎

.. ..............................................................................
.. ................................. TODO .......................................
.. ..............................................................................

.. Need to clarify concatenation as a \mathfrak{F}: S \mapsto \mathbb{S} before attempting this.

.. THEOREM

.. All Reductions are Canonical

.. \forall s \in S: \varsigma(s) \in \mathbb{S}

.. THEOREM

.. The Canon is closed under Reduction.

.. \forall s \in \mathbb{S}: \varsigma(s) \in \mathbb{S}