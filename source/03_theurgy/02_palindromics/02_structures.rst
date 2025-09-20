.. _palindromics-section-ii:

Section II: Structures
======================

Inversion, while a key component of the apparatus necessary for understanding the dynamics of Palindromes, is not the only linguistic operation involved in the formation of Palindromes. The pure involutive property of Palindromes (e.g., :math:`\zeta = {\zeta}^{-1})` only manifests in a rare class of Sentences known as Perfect Palindromes, to be defined shortly.

However, the vast majority of Palindromes in any language are not pure involutions. Instead, the operation of inversion usually degrades the semantic content of a Sentence by re-ordering the Delimiters, as seen in the following,

.. math::

    \zeta = \text{"now sir a war is won"}

.. math::

    {\zeta}^{-1} = \text{"now si raw a ris won"}

In order to properly understand the nature of a Palindrome, the system requires a method of quantifying the distribution of Delimiters in a Sentence and making claims about the structure of that distribution. Furthermore, it must have a method of removing the "*impurities*" in Delimiter distributions that are introduced through inversion.

.. _palindromics-section-ii-i:

Section II.I: Delimiter Count
-----------------------------

.. _palindromics-definition-2-1-1:

.. topic:: Definition 2.1.1: Delimiter Count

    Let :math:`s \in S`. The Delimiter Count of :math:`s`, denoted :math:`\Delta(s)`, is defined inductively using the following schema,

    - Basis: 
        - If :math:`\neg(\sigma \subset_s s)`, then :math:`\Delta(s) = 0`
        - If :math:`s = \varepsilon`, then :math:`\Delta(s) = 0`
        - If :math:`s = \sigma`, then :math:`\Delta(s) = 1`
    - Induction:
        - If :math:`s = (u)(\varsigma)(v)` for any :math:`u,v \in S` where :math:`\neg(\sigma \subets_s u)`, :math:`\Delta(s) = Delta(v) + 1`

**Example** Let :math:`ᚠ = \text{"with up so floating many bells down"}`. Consider :math:`\Delta(ᚠ)`.

.. note::

    The astute reader will note there are 6 Delimiters in :math:`ᚠ`.

Let :math:`u_1 = \text{"with"}` and :math:`v_1 = \{"up so floating many bells down"}`. Then, :math:`ᚠ = (u_1)(\varsigma)(v_1)`. Note :math:`\neg(\sigma \subset_s u_1)`. By the Induction clause :ref:`of the Delimiter Count <palindromics-definition-2-1-1>`,

.. math::

    \Delta(ᚠ) = \Delta(v_1) + 1

Let :math:`u_2 = \text{"up"}` and :math:`v_2 = \{"so floating many bells down"}`. Then, :math:`v_1 = (u_2)(\varsigma)(v_2)`. Note :math:`\neg(\sigma \subset_s u_2)`. By the Induction clause,

.. math::

    \Delta(v_1) = \Delta(v_2) + 1


Let :math:`u_3 = \text{"so"}` and :math:`v_3 = \{"floating many bells down"}`. Then, :math:`v_2 = (u_3)(\varsigma)(v_3)`. Note :math:`\neg(\sigma \subset_s u_3)`. By the Induction clause,

.. math::

    \Delta(v_2) = \Delta(v_3) + 1

Let :math:`u_4 = \text{"floating"}` and :math:`v_4 = \{"many bells down"}`. Then, :math:`v_3 = (u_4)(\varsigma)(v_4)`. Note :math:`\neg(\sigma \subset_s u_4)`. By the Induction clause,

.. math::

    \Delta(v_3) = \Delta(v_4) + 1

Let :math:`u_5 = \text{"many"}` and :math:`v_5 = \{"bells down"}`. Then, :math:`v_4 = (u_5)(\varsigma)(v_5)`. Note :math:`\neg(\sigma \subset_s u_5)`. By the Induction clause,

.. math::

    \Delta(v_4) = \Delta(v_5) + 1


Let :math:`u_6 = \text{"bells"}` and :math:`v_6 = \{"down"}`. Then, :math:`v_5 = (u_6)(\varsigma)(v_6)`. Note :math:`\neg(\sigma \subset_s u_6)`. By the Induction clause,

.. math::

    \Delta(v_5) = \Delta(v_6) + 1

Note :math:`\neg(\sigma \subset_s v_6)`. Therefore, by the Basis clause,

.. math::

    \Delta(v_6) = 0

Putting the recursion together,

.. math::

    \Delta(ᚠ) = (((((0 + 1) + 1) + 1) + 1) + 1) + 1 = 6

∎


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

    = (\zeta[[1]])(\varsigma)(\zeta[[2]]) ... (\varsigma)(\zeta[[n]])

The proof proceeds by induction on Word Length. 

.. Basis

:underline:`Basis`: Assume :math:`n = 1`. Then,

.. math::

    \zeta = \zeta[[1]]

Let :math:`m = l(\zeta[[1]])`. By the :ref:`Discovery Axiom <palindromics-axiom-w-1>`,

.. math::

    \forall i \in N_m: (\zeta[[1]])[i] \neq \sigma

By the :ref:`definition of Containment <palindromics-definition-1-2-5>`,

.. math::

    \neg(\sigma \subset_s \zeta[[1]])

By the Basis clause of the :ref:`definition of Delimiter Counts <palindromics-definition-2-1-1>`,

.. math::
    
    \Delta(\zeta) = 0

Therefore, 

.. math::

    \Lambda(\zeta) = \Delta(\zeta) + 1

:underline:`Induction`: Let :math:`\Lambda(\zeta) = n` for some :math:`n \geq 1`. Assume :math:`\Lambda(\zeta) = \Delta(\zeta) + 1` 

Let :math:`\xi \in C` such that :math:`Lambda(\xi) = n + 1`. Therefore, :math:`\sigma \subset_s \xi`. By :ref:`definition of Containment <palindromics-definition-1-2-5>`,

.. math::

    \exists u,v \xi = (u)(\varsigma)(v)

Choose :math:`u = \xi[[1]]` so that :math:`\neg(\varsigma \subset_s u)`. 


.. ................
.. ........... TODO 
.. ................

.. _palindromics-section-ii-ii:

Section II.II: Reductions
-------------------------

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

---------------------
Elementary Properties
---------------------

1. From the Basis clause of :ref:`σ-Reduction <palindromics-definition-2-2-1>` and the :ref:`definition of String Length <palindromics-definition-1-2-2>`,

.. math::

    l(\varsigma(\sigma)) = l(\varepsilon) = 0

∎

2. From the Basis clause of :ref:`σ-Reduction <palindromics-definition-2-2-1>` and the :ref:`Discovery Axiom <palindromics-axiom-w-2>`,

.. math::

    \varsigma(\alpha) = \alpha

∎

3. From the Basis clause of :ref:`σ-Reduction <palindromics-definition-2-2-1>`, the :ref:`Discovery Axiom <palindromics-axiom-w-2>` and the :ref:`definition of String Length <palindromics-definition-1-2-2>`

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

--------
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

.. _palindromics-section-ii-iii:

Section II.III: Palindromes 
---------------------------

TODO

.. _palindromics-section-ii-iv:

Section II.IV: Summary
----------------------

TODO

