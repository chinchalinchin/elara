=====
Logic
=====

.. _proposition:

Propositions
============

Symbolic Expression
    :math:`p, q, r`

Definition
    A sentence that can be judged either *true* or *false*.

.. _truth-tables:

Truth Tables
============

Truth tables are the standard way of evaluating the truth of a symbolic proposition. However, when the number of terms in a compound proposition rises above 4, truth tables can quickly become cumbersome. See :ref:`carnaps-method` for an alternate way of evaluating the truth of a symbolic propositions.

.. _truth-values:

.. topic:: Truth Values

    TODO

.. _value-assignment:

----------------
Value Assignment
----------------

Each row of a *Truth Table* represents a different *value assignment* to the constituent propositions involved in the compound proposition. For example, in the case of *"p or q"*, the compound symbolic proposition is :math:`p \lor q`. A truth table is constructed by listing every possible combination of truth value for ``p`` and ``q``,

.. list-table::
  :header-rows: 1

  * - :math:`p`
    - :math:`q`
    - :math:`p \lor q`
  * - T
    - T
    - T
  * - T
    - F
    - T
  * - F
    - T
    - T
  * - F
    - F
    - F

The first two columns represent the *input* propositions and their respective truth-values. The third column represents the *output* proposition and the truth-value that results from that particular value assignment.

Each row details a different *state* of the world. The list is exhaustive because every possible combination is contained in the table. Therefore, by looking at the table, we know in which cases we can correctly say :math:`p \lor q`.

.. _logical-operations:

Operations
==========

.. _logical-negation:

--------
Negation
--------

Symbolic Expression
    :math:`\neq p`

.. list-table::
  :header-rows: 1

  * - :math:`p`
    - :math:`\neq p`
  * - T
    - F
  * - F
    - T

.. _logical-conjunction:

-----------
Conjunction
-----------

Symbolic Expression
    :math:`p \land q`

.. list-table::
  :header-rows: 1

  * - :math:`p`
    - :math:`q`
    - :math:`p \land q`
  * - T
    - T
    - T
  * - T
    - F
    - F
  * - F
    - T
    - F
  * - F
    - F
    - F

.. _logical-disjunction:

-----------
Disjunction
-----------

Symbolic Expression
    :math:`p \lor q`

.. list-table::
  :header-rows: 1

  * - :math:`p`
    - :math:`q`
    - :math:`p \lor q`
  * - T
    - T
    - T
  * - T
    - F
    - T
  * - F
    - T
    - T
  * - F
    - F
    - F

.. _logical-equivalence:

-----------
Equivalence
-----------

Symbolic Expression
    :math:`p \equiv q`

.. list-table::
  :header-rows: 1

  * - :math:`p`
    - :math:`q`
    - :math:`p \equiv q`
  * - T
    - T
    - T
  * - T
    - F
    - F
  * - F
    - T
    - F
  * - F
    - F
    - T

.. _logical-implication:

-----------
Implication
-----------

Symbolic Expression
    :math:`p \implies q`

Definition
    A symbolic representation of a *conditional* (if-then) relationship between two *propositions*.

This type of proposition can be translated into English in the following ways,

1. "if *p*, then *q*"
2. "whenever *p*, then *q*"
3. "*p* implies *q*"
4. "*q* follows from *p*"

The :ref:`truth table <truth-tables>` for logical implication is given below,

.. list-table::
  :header-rows: 1

  * - :math:`p`
    - :math:`q`
    - :math:`p \imples q`
  * - T
    - T
    - T
  * - T
    - F
    - F
  * - F
    - T
    - T
  * - F
    - F
    - T

Logical Redundancy
------------------

Logical implication can be expressed in terms of the other logical connectives introduced. Notice the range of the implication connective assigns a value of ``True`` in three cases of the four possible value assignments to its constituent propositions (i.e. three rows of the :ref:`truth table <truth-tables>` are ``True``). Logical disjunctions also assigns a value of ``True`` to three of its four possible value assignments. It is a natural question whether implication can be reduced to disjunction or visa versa.

TODO

It can be shown that all second-order logic can be reduced to :ref:`universal quantification <universal-quantification>` and :ref:`logical equivalence <logical-equivalence>`. See :ref:`logical-primitives` for more information regarding the number of necessarily primitive logical connectives.

.. _logical-inference:

Inference
=========

.. _modus-ponens:

-----------------
Law of Detachment
-----------------

The *Law of Detachment* is a symbolic expression for the process of deductive logic. The truth of an implication is asserted in conjunction with the truth of its hypothesis, which leads to the truth of the implication's consequence. Symbolically,

.. math::

    ( (p \implies q) \land p ) \implies q

.. note::

    The *Law of Detachment* is often known by its Latin name, *modus ponens*.

------------------
Symbolic Arguments
------------------

TODO

Tautologies
-----------

TODO

Contradictions
--------------

TODO

Categorical Logic
=================

------------------
Aristotelian Logic
------------------

TODO

.. _logical-quantification:

--------------
Quantification
--------------

TODO

.. _universal-quantification:

Universal Quantification
------------------------

Symbolic Expression
    :math:`\forall p: q`

Definition
    A symbolic expression for a universal proposition.

This type of proposition can be translated into English in the following ways,

1. "for all *p*, *q*"
2. "for every *p*, *q*"
3. "for each *p*, *q*"

.. _existential-quantification:

Existential Quantification
--------------------------

Symbolic Expression
    :math:`\exists p: q`

Definition
    A symbolic representation of an existential proposition.

This type of proposition can be translated into English in the following ways,

1. "there exists a *p* such that *q*"
2. "for some *p*, *q*"
3. "there is a *p* that *q*"
