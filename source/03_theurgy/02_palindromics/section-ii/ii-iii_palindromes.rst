
.. _palindromics-section-ii-iii:

Section II.III: Palindromes
===========================

.. _palindromics-palindrome-definition:

Definition & Examples
---------------------

.. _palindromics-definition-2-3-1:

.. topic:: Definition 2.3.1: Palindromes

    The class of Palindromes, denoted :math:`P`, is defined as the Sentences that satisfy the following formula,

    .. math::

        \zeta \in P \equiv \varsigma(\zeta) = (\varsigma(\zeta))^{-1}

**Example** 

Let :math:`ᚠ_1 = \text{never odd or even}`. Then, 

.. math::

    \varsigma(ᚠ_1) = \text{neveroddoreven}

.. math::

    (\varsigma(ᚠ_1))^{-1} = \text{neveroddoreven}

Therefore, :math:`ᚠ_1 \in P`.

Let :math:`ᚠ_2 = \text{not a ton}`. Then,

.. math::

    \varsigma(ᚠ_2) = \text{notaton}

.. math::

    (\varsigma(ᚠ_2))^{-1} = \text{notaton}

Therefore, :math:`ᚠ_2 \in P`

Let :math:`ᚠ_2 = \text{fair is foul and foul is fair}`. Then,

.. math::

    \varsigma(ᚠ_3) = \text{fairisfoulandfoulisfair}

.. math::

    (\varsigma(ᚠ_3))^{-1} = \text{riafsiluofdnaluofsiriaf}

Therefore, :math:`ᚠ_3 \notin P`

◼︎

.. _palindromics-aspect:

Aspect
------

.. _palindromics-definition-2-3-2:

.. topic:: Definition 2.3.2: Perfect Palindromes

    The class of Perfect Palindromes, denoted :math:`J`, is defined the Sentences that satisfy the following formula, 

    .. math::

        \zeta \in K \equiv \zeta = \zeta^{-1}

.. note::

    The name, *Perfect Palindromes*, is premature, as it must be shown this definition satisfies :ref:`Definition 2.3.1 <palindromics-definition-2-3-1>` before concluding membership in :math:`K` implies membership in :math:`P`. This will be established in :ref:`Theorem 2.3.4 <palindromics-theorem-2-3-4>`.

.. _palindromics-theorem-2-3-1:

.. topic:: Theorem 2.3.1

    Perfect Palindromes are Invertible Setences.

    .. math::

        K \subseteq J

**Proof** Let :math:`\zeta \in K`. Then by :ref:`definition of Perfect Palindromes <palindromics-definition-2-3-2>`,

.. math::

    \zeta = \zeta^{-1}

Therefore, since :math:`\zeta \in C`, :math:`\zeta^{-1} \in C`. By :ref:`definition of Invertible Sentences <palindromics-definition-1-3-2>`, :math:`\zeta \in J`. Therefore,

.. math::

    \zeta \in K \implies \zeta \in J

But this is exactly the definition of a subset. Therefore,

.. math::

    K \subseteq J

◼︎

.. note::

    :ref:`Theroem 2.3.2 <palindromics-theorem-2-3-2>` and :ref:`Theorem 2.3.3 <palindromics-theorem-2-3-3>` follow directly from :ref:`Theorem 2.3.1 <palindromics-theorem-2-3-1>` and :ref:`Theorem 1.4.10 <palindromics-theorem-1-4-10>` and :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>`.

.. _palindromics-theorem-2-3-2:

.. topic:: Theorem 2.3.2

    .. math::

        \forall \zeta \in K: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \in I

◼︎

.. _palindromics-theorem-2-3-3:

.. topic:: Theorem 2.3.3 

    .. math::

        \forall \zeta \in K: \forall i \in N_{\Lambda(\zeta)}: \zeta^{-1}[[i]] = (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}

◼︎

.. _palindromics-theorem-2-3-4:

.. topic:: Theorem 2.3.4

    Perfect Palindromes are Palindromes.

    .. math::

        J \subseteq P 

**Proof** Let :math:`\zeta \in J`. By :ref:`definition of Perfect Palindromes <palindromics-definition-2-3-2>`, 

.. math::

    \zeta = \zeta^{-1}

:ref:`Reducing <palindromics-definition-2-2-1>` both sides,

.. math::

    \varsigma(\zeta) = \varsigma(\zeta^{-1})

By :ref:`Theorem 2.2.4 <palindromics-theorem-2-2-4>`,

.. math::

    \varsigma(\zeta) = (\varsigma(\zeta))^{-1}

Therefore, by :ref:`definition of Palindromes <palindromics-definition-2-3-1>`,

.. math::

    \zeta \in J \implies \zeta \in P

But this is exactly the definition of subsets, 

.. math::

    J \subseteq P

◼︎

.. _palindromics-theorem-2-3-5:

.. topic:: Theorem 2.3.5

    The Pivot Character of all Perfect Palindromes is non-Empty.
    
    .. math::

        \forall \zeta in J: \omega_{\zeta} \neq \varepsilon

**Proof** Let :math:`\zeta \in J`.

By :ref:`definition of a Perfect Palindrome <palindromics-definition-2-3-2>`, :math:`\zeta = \zeta^{-1}`.  By :ref:`Theorem 2.1.10 <palindromics-theorem-2-1-10>`,

.. math::

    \omega_{\zeta} \neq \varepsilon

◼︎

.. _palindromics-definition-2-3-3:

.. topic:: Definition 2.3.3: Imperfect Palindromes

    TODO 

.. .................................................................................

TODO

.. .................................................................................

.. _palindromics-parity:

Parity
------

.. _palindromics-definition-2-3-4:

.. topic:: Definition 2.3.4: Parity

    The set of Odd Palindromes, denoted :math:`P_{-}`, is defined as the set of Sentences which satisfy the open formula,
    
    .. math::

        \zeta \in P_{-} \equiv ((\zeta \in P) \land (\exists n \in \mathbb{N}: l(\zeta) = 2i + 1))

    The set of Even Palindromes, denoted :math:`P_{+}`, is defined as the set of Sentences which satisfy the open formula,

    .. math::

        \zeta \in P_{+} \equiv (\zeta \in P) \land (\exists n \in \mathbb{N}: l(\zeta) = 2i)