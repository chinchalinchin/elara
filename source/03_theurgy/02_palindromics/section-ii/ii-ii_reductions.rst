
.. _palindromics-section-ii-ii:

Section II.II: Reductions
=========================

.. _palindromics-definition-2-2-1:

.. topic:: Definition 2.2.1: σ-Reduction

    Let :math:`s \in S`. The σ-Reduction of :math:`s`, denoted :math:`\varsigma(s)`, is defined inductively with the following schema,

    - Basis: 
        - :math:`\varsigma(\sigma) = \varespilon`
        - If :math:`neg(\sigma \subset_s s)`, then :math:`\varsigma(s) = s`
    - Induction:
        - If :math:`s = (u)(\varsigma)(v)` for any :math:`u, v \in S` where :math:`\neg(\sigma \subset_s u)`, :math:`\varsigma(s) = \varsigma(uv)`

    :math:`\varsigma(s)` is said to be *reduced* from, or a *reduction* of, :math:`s`.

**Example** :math:`ᚠ = \text{"the widening circles into nothing gone"}`. Consider :math:`\varsigma(ᚠ)`

Let :math:`u_1 = \text{"the"}` and :math:`v_1 = \text{"widening circles into nothing gone"}`. Let :math:`w_1 = (u_1)(v_1)`. Then, :math:`ᚠ = (u_1)(\varsigma)(v_1)`. By the Induction clause :ref:`of σ-Reduction <palindromics-definition-2-2-1>`,

.. math::

    \varsigma(ᚠ) = \varsigma((u_1)(v_1)) = \varsigma(w_1)

Let :math:`u_2 = \text{"thewidening"}` and :math:`v_2 = \text{"circles into nothing gone"}`. Let :math:`w_2 = (u_2)(v_2)`. Then :math:`w_1 = (u_2)(\varsigma)(v_2)`. By the Induction clause,

.. math::

    \varsigma(w_1) = \varsigma((u_2)(v_2)) = \varsigma(w_2)

Let :math:`u_3 = \text{"thewideningcircles"}` and :math:`v_3 = \text{"into nothing gone"}`. Let :math:`w_3 = (u_3)(v_3)`. Then :math:`w_2 = (u_3)(\varsigma)(v_3)`. By the Induction clause,

.. math::

    \varsigma(w_2) = \varsigmna((u_3)(v_3)) = \varsigma(w_3)

Let :math:`u_4 = \text{"thewideningcirclesinto"}` and :math:`v_4 = \text{"nothing gone"}`. Let :math:`w_4 = (u_4)(v_4)`. Then :math:`w_3 = (u_4)(\varsigma)(v_4)`. By the Induction clause,

.. math::

    \varsigma(w_3) = \varsigmna((u_4)(v_4)) = \varsigma(w_4)

Let :math:`u_5 = \text{"thewideningcirclesintonothing"}` and :math:`v_5 = \text{"gone"}`. Let :math:`w_5 = (u_5)(v_5)`. Then :math:`w_4 = (u_5)(\varsigma)(v_5)`. By the Induction clause,

.. math::

    \varsigma(w_4) = \varsigmna((u_5)(v_5)) = \varsigma(w_5)

But :math:`neg(\sigma \subset_s w_5)`, therefore by the Basis clause,

.. math::

    \varsigma(w_5) = w_5

Working back up through the recursion, the original reduction is found,

.. math::

    \varsigma(ᚠ) = \text{"thewideningcirclesintonothinggone"}

∎

.. _palindromics-elementary-properties:

Elementary Properties
---------------------

1. From the Basis clause of :ref:`σ-Reduction <palindromics-definition-2-2-1>` and the :ref:`definition of String Length <palindromics-definition-1-2-2>`,

.. math::

    l(\varsigma(\sigma)) = l(\varepsilon) = 0

∎

2. From the Basis clause of :ref:`σ-Reduction <palindromics-definition-2-2-1>` and the :ref:`Discovery Axiom <palindromics-axiom-v>`,

.. math::

    \varsigma(\alpha) = \alpha

∎

3. From the Basis clause of :ref:`σ-Reduction <palindromics-definition-2-2-1>`, the :ref:`Discovery Axiom <palindromics-axiom-v>` and the :ref:`definition of String Length <palindromics-definition-1-2-2>`

.. math::

    l(\varsigma(\alpha)) = l(\alpha)

∎

4. From the Induction clause of :ref:`σ-Reduction <palindromics-definition-2-2-1>` and the :ref:`definition of String Length <palindromics-definition-1-2-2>`,

.. math::

    l(\varsigma(s)) \leq l(s)

∎

5. From the :ref:`definition of Concatenation <palindromics-definition-1-2-1>` and :ref:`the definition of σ-Reduction <palindromics-definition-2-2-1>`, all σ-Reductions are Strings,

.. math::

    \forall s \in S:  \varsigma(s) \in S

∎

.. _palindromics-reduction-theorems:

Theorems
--------

.. _palindromics-theorem-2-2-1:

.. topic:: Theorem 2.2.1

    The inverse of a reduced String is the reduction of the inverse String. 

    .. math::

        \forall s \in S: (\varsigma(s))^{-1} = \varsigma(s^{-1})

**Proof** Let :math:`s \in S`. The proof proceeds by induction on the number of Delimiters in :math:`s`.

.. BASIS 

:underline:`Basis` Let :math:`\neg(\sigma \subset_s s)`; that is, assume there are no Delimiter in :math:`s`. By :ref:`Theorem 1.2.5 <palindromics-theorem-1-2-5>` and the fact :math:`\sigma^{-1} = \sigma`,

.. math::

    \neg(\sigma \subset_s s) \equiv \neg(\sigma subset_s s^{-1})

Consider :math:`(\varsigma(s))^{-1}`. By the Basis clause of :ref:`the Reduction definition <palindromics-definition-2-2-1>`,

.. math::

    \varsigma(s) = s

Therefore,

.. math::

    (\varsigma(s))^{-1} = s^{-1}

Consider :math:`\varsigma(s^{-1})`. By :math:`\neg (\sigma \subset_s s^{-1})` and the Basis clause of :ref:`the Reduction definition <palindromics-definition-2-2-1>`, 

.. math::

    \varsigma(s^{-1}) = s^{-1}

.. INDUCTION 

:underline:`Induction` Let :math:`\sigma \subset_s s`, i.e. :math:`s` has :math:`k` Delimiters for some :math:`k \geq 1`. Assume :math:`(\varsigma(s))^{-1} = \varsigma(s^{-1})`. 

Let :math:`u \in S` such that :math:`u` has :math:`k+1` Delimiters. Let :math:`u = (v)(\varsigma)(w)`, where :math:`\neg(\sigma \subset_s v)`




Then, by the :ref:`definition of Containment <palindromics-definition-1-2-5>`, for some :math:`u,v`, possibly Empty,

.. math::

    s = (u)(\sigma)(v)

By :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`,

.. math::

    s^{-1} = (v^{-1})(\sigma^{-1})(u^{-1})

By the :ref:`definition of String Inversion <palindromics-definition-1-2-5>` and the fact :math:`l(\sigma) = 1`, it follows :math:`\sigma^{-1} = \sigma`. Therefore,

.. math::

    s^{-1} = (v^{-1})(\sigma)(u^{-1})

Consider :math:`\varsigma(s^{-1})`. Apply the Induction clause of :ref:`the Reduction definition <palindromics-definition-2-2-1>`, 

.. math::

    \varsigma(s^{-1}) = \varsigma((v^{-1})(u^{-1}))

Consider :math:`\varsigma(s)`. By the Induction clause of :ref:`the Reduction definition <palindromics-definition-2-2-1>`, 

.. math::

    \varsigma(s) = \varsigma(uv)

By :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`,

.. math::

    (\varsigma(s))^{-1} = (\varsigma(uv))^{-1}


.. ...............................
.. .............. TODO ...........
.. ...............................