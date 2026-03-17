Okay, like I said, I am involved in refactoring. Before moving on, I want to go through this section in a little more detail. There is an analogue of Theorem 2.1.5 for even Delimiter Counts that I think is provable, 

    \forall s \in D: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies s[\frac{l(s)}{2}] \neq \sigma

However, I believe in order to be fully justified, it has to be shown that inversion is closed over the Dialect, i.e. \forall s \in D: s^{-1} \in D.  Moreover, I think it is necessary to prove 

    \forall s \in D: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies \exists m: l(s) = 2m

i.e., if a String belongs to a Dialect, is its own inverse and has an even number of Delimiter, it's String Length is also even. 

This is the proof I have for the new theorem:

.. important::

    :ref:`Theorem 2.1.5` applies to *all* Strings in :math:`S`. However, it's analogue for even Delimiter counts must be restricted to a special subdomain of :math:`S` where the Delimiter structure is regular, i.e. the *Dialect* of a Language, :math:`D`. 

.. _palindromcs-theorem-2-1-6:

.. topic:: Theorem 2.1.6

    .. math::

        \forall s \in D: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies s[\frac{l(s)}{2}] \neq \sigma

**Proof** The proof is similar to :ref:`Theoreom 2.1.5 <palindromics-theorem-2-1-5>`. Let :math:`s,t \in D` such that :math:`\Delta(s) = 2n` for some :math:`n \in \mathbb{N}` and :math:`t = s^{-1}`. Let :math:`m = l(s)`. Let :math:`P` be the set of Delimiter indices in :math:`s`,

.. math::

    P = \{ i \mid s[i] = \sigma \}

Then :math:`\lvert P \rvert = \Delta(s) = 2n` by assumption.

By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    t[i] = s[m - i + 1]

Assume, for the sake of contradiction, :math:`s[\frac{l(s)}{2}] = s[\frac{m}{2}]= \sigma`. Then, every Delimiter must have a symmetric pair in :math:`P`.

.. math::

    t[i] = s[m - i  + 1]

So, using :math:`i = \frac{m}{2}`

.. wait. this can only be the case if string length is even. how do you know string length isn't odd, making s[m/2] undefined. i need a lemma to show string length is even if string is in Dialect with even number of Delimiters...

.. math::

    t[\frac{m}{2}] = s[\frac{m}{2} + 1]

Therefore, 

.. math::

    s[\frac{m}{2}] = \sigma
    
.. math::

    s[\frac{m}{2} + 1] = \sigma

That is, two consecutive Characters in :math:`s` are Delimiters. But this is impossible if :math:`s \in D`. Therefore, it must be the case :math:`s[\frac{l(s)}{2}] \neq \sigma`.

---

How would you prove the closure of inversion over the Dialect? And how would you prove even string length if string is Dialect with even number of Delimiters?