.. _palindromics-section-iii-ii:

Section III.II: Postulates
==========================

.. .................................................................................

TODO

.. .................................................................................

Pivot Postulates
----------------

.. _palindromics-theorem-3-2-1:

.. topic:: Theorem 3.2.1 

    A Perfect Palindrome has a Delimiter Pivot Character if and only if a Perfect Palindrome has Odd Parity.

    .. math::

        \forall \zeta \in K: (\omega_{\zeta} = \sigma) \equiv \zeta \in P_{-}

**Proof** Let :math:`\zeta \in K`. Note

.. math::

    K \subseteq C \subseteq D

Then by :ref:`definition of Perfect Palindromes <palindromics-definition-2-4-2>`, :math:`\zeta = \zeta^{-1}`.

(:math:`\rightarrow`) Assume :math:`\omega_{\zeta} = \sigma`. Assume, for the sake of contradiction, :math:`\zeta \notin P_{-}`. Then, since,

.. math::

    P_{+} \cup P_{-} = P

And,

.. math::

    P_{+} \cap P_{-} = \varnothing 

It follows that it must be the case, :math:`\zeta \in P_{+}`. Therefore, :math:`\exists i \in mathbb{N}: l(\zeta) = 2i`. Then, by :ref:`definition of Pivot Characters <palindromics-definition-2-2-1>`, 

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s} = \sigma

Where the last equality follows by assumption. Then,

.. math::

    \zeta[\frac{l(s) + 2}{2}] = \zeta[\frac{l(2)}{2}] = \sigma

In other words, two consecutive Characters are Delimiter. But this is impossible if :math:`\zeta \in D`. Therefore, it must be case,

.. math::

    \zeta \in P_{-}

(:math:`\leftarrow`) Assume :math:`\zeta \in P_{-}`. By :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>`, it follows immediately,

.. math::

    \omega_{\zeta} = \sigma

Thus the equivalence is established. Summarizing and generalizing, 

.. math::

    \forall \zeta \in K: (\omega_{\zeta} = \sigma) \equiv \zeta \in P_{-}
    
∎

.. _palindromics-theorem-3-2-2:

.. topic:: Theorem 3.2.2

    The Pivot Character of a Perfect Palindrome is not a Delimtier if and only if its Pivot Word is Reflective.

    .. math::

        \forall \zeta \in K: (\omega_{\zeta} \neq \sigma) \equiv (\Omega_{\zeta} \in R)

**Proof** Let :math:`\zeta \in K`. 

.. .................................................................................

TODO

.. .................................................................................

.. _palindromics-theorem-3-2-3:

.. topic:: Theorem 3.2.3

    The Pivot Character of a Perfect Palindrome is not a Delimiter if and only if its Pivot Character is the Pivot Character of its Pivot Word.

    .. math::

        \forall \zeta \in K: (\omega_{\zeta} \neq \sigma) \equiv (\omega_{\Omega_{\zeta}} = \omega_{\zeta} )

.. .................................................................................

TODO

.. .................................................................................

Inverse Postulates
------------------

.. topic:: Theorem 3.2.x

    Either the first Word of a Palindrome is contained in the first word of its Inverse, or the first Word of its Inverse is contained in its First Word.

    .. math::

        \forall \zeta \in P: (\zeta[[1]] \subset_s \zeta^{-1}[[1]]) \lor (\zeta^{-1}[[1]] \subset_s \zeta[[1]])

.. .................................................................................

TODO

.. .................................................................................

.. topic:: Theorem 3.2.x+1 

    Either the last Word of a Palindrome is contained in the last word of its Inverse, or the last word of its Inverse is contained in the last word of the Palindrome. 

    .. math::

        \forall \zeta \in P:  (\zeta[[\Lambda(\zeta)]] \subset_s \zeta^{-1}[[\Lambda(\zeta)]]) \lor (\zeta^{-1}[[\Lambda(\zeta)]] \subset_s \zeta[[\Lambda(\zeta)]])

.. .................................................................................

TODO

.. .................................................................................
