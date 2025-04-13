.. _syntagmic-theorems:

Theorems
--------

.. topic:: Theorem: Cardinality of Rhyme Sets in Finite Terza Rima

    Let :math:`V = \{v_1, v_2, v_3, ...\}` be an indexed set of distinct indeterminate rhyme variables (representing potential rhyme sounds, e.g., :math:`a, b, c, ...`).

    Define the structure of the :math:`i` -th Terza Rima tercet stanza (:math:`i \ge 1`) using variables from :math:`V` as:

    .. math::

        \varsigma_i = v_i . v_{i+1} . v_i

    Consider a finite Terza Rima poetic structure :math:`p_m` composed of :math:`m` such consecutive tercets (:math:`m \in \mathbb{N}, m \ge 1`), where the scope of rhyme linkage required by the schema variables is limited to each individual stanza as represented in the standard Terza Rima schema summation:

    .. math::

        p_m = \sum_{i=1}^{m} \overline{\varsigma_i} = \sum_{i=1}^{m} \overline{v_i . v_{i+1} . v_i}

    Let :math:`R(p_m)` denote the set of all distinct indeterminate rhyme variables :math:`v_k` that appear in the formal expansion of the structure :math:`p_m`.

    **Theorem:** The cardinality of the set of distinct rhyme variables required by the schema :math:`p_m` is exactly one greater than the number of tercets.

    .. math::

        |R(p_m)| = m + 1


This theorem arises directly from the interlocking nature of the Terza Rima form.

- The first stanza, :math:`\varsigma_1 = \overline{v_1 . v_2 . v_1}`, introduces rhyme variables :math:`v_1` and :math:`v_2`.
- The second stanza, :math:`\varsigma_2 = \overline{v_2 . v_3 . v_2}`, reuses :math:`v_2` and introduces the new rhyme variable :math:`v_3`.
- Each subsequent stanza :math:`\varsigma_i = \overline{v_i . v_{i+1} . v_i}` reuses the variable :math:`v_i` (which was introduced as the middle rhyme of the preceding stanza :math:`\varsigma_{i-1}`) and introduces a new variable :math:`v_{i+1}` for its middle line.
- This continues until the final stanza in the sequence, :math:`\varsigma_m = \overline{v_m . v_{m+1} . v_m}`, which introduces the final distinct rhyme variable :math:`v_{m+1}`.

Therefore, the set of all distinct rhyme variables utilized in the schema for :math:`m` tercets is :math:`R(p_m) = \{v_1, v_2, v_3, ..., v_m, v_{m+1}\}`. The number of elements in this set is :math:`m + 1`.

This theorem highlights a fundamental structural property of the Terza Rima schema: the necessary proliferation of rhyme sounds (or at least schema variables) as the poem extends. While a poet might choose to reuse actual sounds (making :math:`v_k` rhyme with :math:`v_j` for :math:`k \neq j`), the abstract schema itself requires :math:`m+1` distinct variable placeholders for :math:`m` tercets.