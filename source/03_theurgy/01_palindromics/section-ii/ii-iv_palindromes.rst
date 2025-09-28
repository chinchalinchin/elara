
.. _palindromics-section-ii-iv:

Section II.IV: Palindromes
===========================

.. _palindromics-palindrome-definition:

Definition & Examples
---------------------

.. _palindromics-definition-2-4-1:

.. topic:: Definition 2.4.1: Palindromes

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

.. _palindromics-perfect-palindromes:

-------------------
Perfect Palindromes 
-------------------

.. _palindromics-definition-2-4-2:

.. topic:: Definition 2.4.2: Perfect Palindromes

    The class of Perfect Palindromes, denoted :math:`J`, is defined the Sentences that satisfy the following formula, 

    .. math::

        \zeta \in K \equiv \zeta = \zeta^{-1}

.. note::

    The name, *Perfect Palindromes*, is premature, as it must be shown this definition satisfies :ref:`Definition 2.3.1 <palindromics-definition-2-4-1>` before concluding membership in :math:`K` implies membership in :math:`P`. This will be established in :ref:`Theorem 2.3.4 <palindromics-theorem-2-3-4>`.

.. _palindromics-theorem-2-4-1:

.. topic:: Theorem 2.4.1

    Perfect Palindromes are Invertible Setences.

    .. math::

        K \subseteq J

**Proof** Let :math:`\zeta \in K`. Then by :ref:`definition of Perfect Palindromes <palindromics-definition-2-4-2>`,

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

    :ref:`Theroem 2.4.2 <palindromics-theorem-2-4-2>` through :ref:`Theorem 2.4.4 <palindromics-theorem-2-4-3>` follow directly from :ref:`Theorem 2.4.1 <palindromics-theorem-2-4-1>` and :ref:`Theorem 1.4.10 <palindromics-theorem-1-4-10>` through :ref:`Theorem 1.4.12 <palindromics-theorem-1-4-11>`.

.. _palindromics-theorem-2-4-2:

.. topic:: Theorem 2.4.2

    .. math::

        \forall \zeta \in K: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \in I

◼︎

.. _palindromics-theorem-2-4-3:

.. topic:: Theorem 2.4.3 

    .. math::

        \forall \zeta \in K: \forall i \in N_{\Lambda(\zeta)}: \zeta^{-1}[[i]] = (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}

◼︎

.. _palindromics-theorem-2-4-4:

.. topic:: Theorem 2.4.4

    .. math::

        \forall \zeta \in K: \Lambda(\zeta) = \Lambda(\zeta^{-1})

◼︎

.. _palindromics-theorem-2-4-5:

.. topic:: Theorem 2.4.5

    Perfect Palindromes are Palindromes.

    .. math::

        K \subseteq P 

**Proof** Let :math:`\zeta \in K`. By :ref:`definition of Perfect Palindromes <palindromics-definition-2-4-2>`, 

.. math::

    \zeta = \zeta^{-1}

:ref:`Reducing <palindromics-definition-2-2-1>` both sides,

.. math::

    \varsigma(\zeta) = \varsigma(\zeta^{-1})

By :ref:`Theorem 2.2.4 <palindromics-theorem-2-2-4>`,

.. math::

    \varsigma(\zeta) = (\varsigma(\zeta))^{-1}

Therefore, by :ref:`definition of Palindromes <palindromics-definition-2-4-1>`,

.. math::

    \zeta \in J \implies \zeta \in P

But this is exactly the definition of subsets, 

.. math::

    K \subseteq P

◼︎

.. _palindromics-theorem-2-4-6:

.. topic:: Theorem 2.4.6

    All Perfect Palindromes have a non-Empty Pivot Character.
    
    .. math::

        \forall \zeta \in K: \omega_{\zeta} \neq \varepsilon

**Proof** Let :math:`\zeta \in K`.

By :ref:`definition of a Perfect Palindrome <palindromics-definition-2-4-2>`, :math:`\zeta = \zeta^{-1}`.  By :ref:`Theorem 2.2.4 <palindromics-theorem-2-2-4>`,

.. math::

    \omega_{\zeta} \neq \varepsilon

◼

.. _palindromics-theorem-2-4-7:

.. topic:: Theorem 2.4.7

    All Perfect Palindromes have a non-Empty Pivot Word

    .. math::

        \forall \zeta \in K: \Omega_{\zeta} \neq \varepsilon

**Proof** Let :math:`\zeta \in K` and :math:`n = \Lambda(\zeta)`. 

By :ref:`definition of String Inversion <palindromics-definition-1-2-8>`,

.. math::

    l(\zeta) = l(\zeta^{-1}) \quad \text{ (1) }

By :ref:`Theorem 2.4.3 <palindromics-theorem-2-4-3>`,

.. math::

    {\zeta}^{-1}[[i]] = (\zeta[[n - i + 1]])^{-1} \quad \text{ (2) }

By :ref:`Theorem 1.4.12 <palindromics-theorem-1-4-12>` and :math:`K \subseteq J` (by :ref:`Theorem 2.4.1 <palindromics-theorem-2-4-1>`),

.. math::

    \Lambda(\zeta) = \Lambda(\zeta^{-1}) \quad \text{ (3) }

.. CASE I 

:underline:`Case I`: :math:`n = 2i` for some :math:`i \in \mathbb{N}`.

By the :ref:`definition of Pivot Words <palindromics-definition-2-2-2>`,

.. math::

    \overrightarrow{\Omega_{\zeta}} = \zeta[[\frac{n}{2}]]

.. math::

    \overleftarrow{\Omega_{\zeta}} = \zeta[[\frac{n + 2}{2}]]

By (2),

.. math::

    (\zeta[[\frac{n}{2}]])^{-1} = \zeta^{-1}[[\frac{n + 2}{2}]]

Therefore,

.. math::

    \overleftarrow{\Omega_{\zeta}} =  (\zeta^{-1}[[\frac{n}{2}]])^{-1}

But since :math:`\zeta \in K` and :math:`\zeta = \zeta^{-1}` by :ref:`definition of Perfect Palindromes <palindromics-definition-2-4-2>`,

.. math::

    \overleftarrow{\Omega_{\zeta}} = (\zeta[[\frac{n}{2}]])^{-1} = (\overrightarrow(\Omega_{\zeta}))^{-1}

Therefore, by :ref:`definition of Pivot Words <palindromics-definition-2-2-2>`,

.. math::

    \Omega_{\zeta} \neq \varepsilon

.. CASE II 

:underline:`Case II`: :math:`n = 2i + 1` for some :math:`i \in \mathbb{N}`

By the :ref:`definition of Pivot Words <palindromics-definition-2-2-2>`,

.. math::

    \overleftarrow{\Omega_{\zeta}} = \zeta[[\frac{n + 1}{2}]]

.. math::

    \overrightarrow{\Omega_{\zeta}} = \zeta[[\frac{n + 1}{2}]]

By (2),

.. math::

    (\zeta[[\frac{n + 1}{2}]])^{-1} = \zeta^{-1}[[n - \frac{n + 1}{2} + 1]] = \zeta{-1}[[\frac{n+1}{2}]]

But :math:`\zeta = \zeta^{-1}` by assumption. Therefore,

.. math::

    (\overrightarrow{\Omega_{\zeta}})^{-1} =(\zeta[[\frac{n + 1}{2}]])^{-1} = \zeta[[\frac{n+1}{2}]] = \overleftarrow{\Omega_{\zeta}}

Therefore, by :ref:`definition of Pivot Words <palindromics-definition-2-2-2>`,

.. math::

    \Omega_{\zeta} \neq \varepsilon

Summarizing and generalizing, 

.. math::

    \forall \zeta \in K: \Omega_{\zeta} \neq \varepsilon

◼

.. _palindromics-theorem-2-4-8:

.. topic:: Theorem 2.4.8

    All Perfect Palindromes are Subvertible.

    .. math::

        K \subseteq \cancel{J}

**Proof** Let :math:`\zeta \in K`. Then, by :ref:`Theorem 2.4.7 <palindromics-theorem-2-4-7>` and :ref:`Theorem 2.4.8 <palindromics-theorem-2-4-8>`,

.. math::

    \omega_{\zeta} \neq \varepsilon

.. math::

    \Omega_{\zeta} \neq \varepsilon

Therefore, by :ref:`definition of Subvertible Sentences <palindromics-definition-2-2-3>`,

.. math::

    \zeta \in \cancel{J}

Thus, :math:`\zeta \in K \implies \zeta \in J`. But this is exactly the definition of a subset,

.. math::

    K \subseteq \cancel{J}

◼

.. note::

    It follows directly from :ref:`Theorem 2.4.1 <palindromics-theorem-2-4-1>` and :ref:`Theorem 2.4.8 <palindromics-theorem-2-4-8>` that all Perfect Palindromes are Invertible and Subvertible.

    .. math::

        K \subseteq (J \cap \cancel{J})

.. _palindromics-imperfect-palindromes:

---------------------
Imperfect Palindromes
---------------------

.. _palindromics-definition-2-4-3:

.. topic:: Definition 2.4.3: Imperfect Palindromes

    TODO 

.. ..............................................................................
.. ................................. TODO .......................................
.. ..............................................................................

.. _palindromics-parity:

Parity
------

.. _palindromics-definition-2-4-4:

.. topic:: Definition 2.4.4: Parity

    The set of Odd Palindromes, denoted :math:`P_{-}`, is defined as the set of Sentences which satisfy the open formula,
    
    .. math::

        \zeta \in P_{-} \equiv ((\zeta \in P) \land (\exists n \in \mathbb{N}: l(\zeta) = 2i + 1))

    The set of Even Palindromes, denoted :math:`P_{+}`, is defined as the set of Sentences which satisfy the open formula,

    .. math::

        \zeta \in P_{+} \equiv (\zeta \in P) \land (\exists n \in \mathbb{N}: l(\zeta) = 2i)

.. ..............................................................................
.. ................................. TODO .......................................
.. ..............................................................................

.. _palindromics-theorem-2-4-x:

.. topic:: Theorem 2.4.x

    The Pivot Word of all Even Perfect Palindromes is Reflective. 

    .. math::
    
        \forall \zeta \in (K \cap P_{-}): \Omega_{\zeta} \in R

.. ..............................................................................
.. ................................. TODO .......................................
.. ..............................................................................

.. _palindromics-theorem-2-4-x+1:

.. topic:: Theorem 2.4.x+1

    The Pivot Character of all Odd Perfect Palindromes is a Delimiter

    .. math::

        \forall \zeta \in (K \cap P_{+}): \omega_{\zeta} = \sigma

.. ..............................................................................
.. ................................. TODO .......................................
.. ..............................................................................
