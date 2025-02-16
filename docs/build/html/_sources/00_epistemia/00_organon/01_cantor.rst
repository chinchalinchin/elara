.. _cantor:

Cantor
======

    Je le vois, mais je ne le crois pas!

    -- *Correspondence with Richard Dedekind*, Georg Cantor, 1877

.. _transfinitude: 

Transfinitude
-------------

.. _rebellious-set:

The Curse of the Rebellious Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _definition_rebellious_set:

.. topic:: Definition: The Rebellious Set 

    Let :math:`A` be any set and let :math:`P(A)` be it's power set. Assume :math:`f: A \to P(A)`. The Rebellious Set, denoted R, is defined as the set which satisfies this formula,

    .. math::

        R = \{ x \in A \, \mid \, x \notin f(x) \}

    ∎

.. _rebellious-set-theorem:

**Theorem** :math:`f: A \to P(A) \leftrightarrow \lvert R \rvert \geq 1`

Let :math:`P(A)` be the power set of :math:`A` (the set of all subsets of :math:`A`). Suppose there exists a bijection :math:`f: A -> P(A)`. This means every element in :math:`A` is paired with a unique subset of :math:`A`, and vice versa.

If :math:`A = \emptyset`, then its power set :math:`P(A)` contains one element, the empty set itself, :math:`P(A) = {∅}`. In this case, there's no bijection between :math:`A` and :math:`P(A)`, and the theorem holds trivially.

If :math:`A \neq \emptyset`, it must contain at least one element. Let *a* be this element. Consider the subset of :math:`A`` that contains only this element, :math:`\{a\}`. Since *f* is assumed to be a bijection, there must be some element :math:`y \in A` such that :math:`f(y) = \{a\}`.

If :math:`y = a`, then, :math:`a \in f(a)`, which contradicts the definition of :math:`B` (that is, the elements in :math:`B` are not in the set they are mapped to).

If :math:`y \neq a`, then :math:`y \notin f(y)`, which means *y* should be in :math:`B` according to its definition. Since *y* exists, :math:`B` is not empty. ∎

.. _more-parts-than-wholes:

More Parts Than Wholes
^^^^^^^^^^^^^^^^^^^^^^

.. _part-whole-theorem:

**Theorem** :math:`\forall A: \lvert P(A) \rvert > \lvert A \rvert`

For the sake of contradiction, suppose there exists a bijection (a one-to-one correspondence)  :math:`f: A \to P(A)`. This means every element in :math:`A` is paired with a unique subset of :math:`A`, and vice versa.

Consider the rebellious set, 

.. math::
    
    R = \{ x \in A \, \mid \, x \notin f(x) \} 

This set :math:`R` contains all elements of :math:`A` that are not members of the subset they are mapped to by *f*. By the previous theorem, this set is non-empty. Since *f* is a bijection, there must be an element :math:`r \in A` such that :math:`f(r) = R`.

If :math:`r \in R`, then by the definition of :math:`R`, :math:`r ∉ f(r)`. But :math:`f(r) = R`, so :math:`r \notin R`, a contradiction.

If :math:`r \notin R`, then by the definition of :math:`R`, :math:`r ∈ f(r)`. But :math:`f(r) = R`, so :math:`r \in R`, again a contradiction.

The initial assumption that there exists a bijection between :math:`A` and :math:`P(A)` must be false. 

Therefore, 

.. math::

    \lvert P(A) \rvert > \lvert A \rvert

∎