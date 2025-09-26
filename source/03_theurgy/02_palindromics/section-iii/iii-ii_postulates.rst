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

        \forall \zeta \in J: (\omega_{\zeta} = \sigma) \equiv \zeta \in P_{-}

**Proof** Let :math:`\zeta \in J`. Note

.. math::

    J \subseteq C \subseteq D

Then by :ref:`definition of Perfect Palindromes <palindromics-definition-2-3-2>`, :math:`\zeta = \zeta^{-1}`.

(:math:`\rightarrow`) Assume :math:`\omega_{\zeta} = \sigma`. Assume, for the sake of contradiction, :math:`\zeta \notin P_{-}`. Then, since,

.. math::

    P_{+} \cup P_{-} = P

And,

.. math::

    P_{+} \cap P_{-} = \varnothing 

It follows that it must be the case, :math:`\zeta \in P_{+}`. Therefore, :math:`\exists i \in mathbb{N}: l(\zeta) = 2i`. Then, by :ref:`definition of Pivot Characters <palindromics-definition-2-1-2>`, 

.. math::

    \overrrightarrow{\omega_s} = \omegaleftarrow{\omega_s} = \sigma

Where the last equality follows by assumption. Then,

.. math::

    \zeta[\frac{l(s) + 2}{2}] = \zeta[\frac{l(2)}{2}] = \sigma

In other words, two consecutive Characters are Delimiter. But this is impossible if :math:`\zeta \in D`. Therefore, it must be case,

.. math::

    \zeta[\frac{l(2)}{2}] \neq \sigma

And 

.. math::

    \zeta[\frac{l(s) + 2}{2}] \neq \sigma

(:math:`\leftarrow`) Assume :math:`\zeta \in P_{-}`. By :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>`, it follows immediately,

.. math::

    \omega_{\zeta} = \sigma

Thus the equivalence is established. Summarizing and generalizing, 

.. math::

    \forall \zeta \in J: (\omega_{\zeta} = \sigma) \equiv \zeta \in P_{-}
    
∎
.. .................................................................................

TODO

.. .................................................................................

.. _palindromics-theorem-3-2-2:

.. topic:: Theorem 3.2.2

    \forall \zeta \in J: (\omega_{\zeta} \neq \sigma) \equiv (\Omega_{\zeta} \in R)

**Proof** Let :math:`\zeta \in J`. 

.. .................................................................................

TODO

.. .................................................................................

Inverse Postulates
------------------

.. topic:: Theorem 3.2.x

    Either the first Word of a Palindrome is contained in the first word of its Inverse, or the first Word of its Inverse is contained in its First Word.

    .. math::

        \forall \zeta in P: (\zeta[[1]] \subset_s \zeta^{-1}[[1]]) \lor (\zeta^{-1}[[1]] \subset_s \zeta[[1]])

.. topic:: Theorem 3.2.x+1 

    Either the last Word of a Palindrome is contained in the last word of its Inverse, or the last word of its Inverse is contained in the last word of the Palidnrome. 

    .. math::

        \forall \zeta in P:  (\zeta[[\Lambda(\zeta)]] \subset_s \zeta^{-1}[[\Lambda(\zeta)]]) \lor (\zeta^{-1}[[\Lambda(\zeta)]] \subset_s \zeta[[\Lambda(\zeta)]])