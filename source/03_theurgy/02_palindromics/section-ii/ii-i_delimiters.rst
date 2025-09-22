.. _palindromics-section-ii-i:

Section II.I: Delimiter Count
=============================

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

Let :math:`m = l(\zeta[[1]])`. By the :ref:`Discovery Axiom <palindromics-axiom-v>`,

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

.. INDUCTION

:underline:`Induction`: Let :math:`\Lambda(\zeta) = n` for some :math:`n \geq 1`. Assume :math:`\Lambda(\zeta) = \Delta(\zeta) + 1` 

Let :math:`\xi \in C` such that :math:`Lambda(\xi) = n + 1`. Therefore, :math:`\sigma \subset_s \xi`. By :ref:`definition of Containment <palindromics-definition-1-2-5>`,

.. math::

    \exists u,v \xi = (u)(\varsigma)(v)

Choose :math:`u = \xi[[1]]` so that :math:`\neg(\varsigma \subset_s u)`. 


.. ................
.. ........... TODO 
.. ................
