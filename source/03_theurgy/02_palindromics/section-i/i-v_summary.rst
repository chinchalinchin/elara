
.. _palindromics-section-i-v:

Section I.V: Summary
====================

The analysis requires one more piece of formal machinery before it can codify the phenomenon of palindromes. However, even without the later results, :ref:`Theorem 1.4.10 <palindromics-theorem-1-4-10>` and :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>` are particularly compelling results that demonstrate the efficacy of the current formal system and its ability to generate novel, if intuitively obvious, theorems. 

The deductive path from :ref:`Theorem 1.4.10 <palindromics-theorem-1-4-10>` to :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>` follows a "*propagation of inversion*" up the semantic hierarchy, from Characters to Words to Sentences. 

First, :ref:`String Inversion <palindromics-definition-1-2-6>` was defined as a operation performed on the Characters within a String,

.. math::

    s[i] = t[l(s) - i + 1]

Where :math:`t` is the inverse of :math:`s`, :math:`t^{-1} = s`. This in turn defined an equivalence class over involutive Words in :ref:`Reflective Words <palindromics-theorem-1-3-1>`, 

    \alpha \in R \equiv \alpha = {\alpha}^{-1}

Moreover, it created a semi-group in :ref:`Invertible Words <palindromics-definition-1-3-2>`,

.. math::

    \alpha \in I \equiv {\alpha}^{-1} \in I

This inversion makes its way to the top layer of the semantic hierarchy with :ref:`Invertible Sentences <palindromics-definition-1-4-3>`,

.. math::

    \zeta \in K \equiv {\zeta}^{-1} \in C

The class :math:`K` then imposes a condition on all Sentences that belong to it, namely that :ref:`its Words must be also invertible <palindromics-theorem-1-4-10>`,

.. math::

    \zeta[[i]] \in I

The inversion then "*propagates*" up a level in the semantic hierarchy and results in a directly analogous :ref:`condition on the Word-level <palindromics-theorem-1-4-11>` to the Character-level symmetry,

.. math::

    {\zeta}^{-1}[[i]] = (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}

.. important::

    The direction of implication in :ref:`Theorem 1.4.10 <palindromics-theorem-1-4-10>` and :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>` is unidirectional. In other words, while invertibility implies the previous two equations, invertibility cannot be concluded on the basis of the previous two equations. This is an artifact of the formal system's inability to formalize the grammar of Sentences.

