.. _logic:

=====
Logic
=====

.. _propositional-logic:

Propositional Logic
===================

.. _proposition:

------------
Propositions
------------

.. epigraph::

  I shall not try to give a general definition of "proposition", as it is impossible to do so.

  -- `Wittgenstein Lectures`_, Ludwig Wittgenstein

Symbolic Expression
  :math:`p, q, r`

Definition
  A sentence that can be judged either *true* or *false*.

.. _truth-tables:

------------
Truth Tables
------------

:ref:`Truth tables <truth-tables>` are the standard way of evaluating the :ref:`truth <truth>` of a symbolic proposition. However, when the number of terms in a compound proposition rises above 4, :ref:`truth tables <truth>` can quickly become cumbersome. See :ref:`carnaps-method` for an alternate way of evaluating the truth of a symbolic propositions.

.. _truth-values:

.. topic:: Truth Values

  TODO

.. _value-assignment:

Value Assignment
----------------

Each row of a :ref:`truth table <truth-tables>` represents a different *value assignment* to the constituent propositions involved in the compound proposition. For example, in the case of *"p or q"*, the compound symbolic proposition is :math:`p \lor q`. A :ref:`truth table <truth-tables>` is constructed by listing every possible combination of truth value for ``p`` and ``q``,

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

----------
Operations
----------

.. _logical-negation:

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
    - :math:`p \implies q`
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
^^^^^^^^^^^^^^^^^^

Logical implication can be expressed in terms of the other logical connectives introduced. Notice the range of the implication connective assigns a value of ``True`` in three cases of the four possible value assignments to its constituent propositions (i.e. three rows of the :ref:`truth table <truth-tables>` are ``True``). Logical disjunctions also assigns a value of ``True`` to three of its four possible value assignments. It is a natural question whether implication can be reduced to disjunction or visa versa.

TODO

It can be shown that all second-order logic can be reduced to :ref:`universal quantification <universal-quantification>` and :ref:`logical equivalence <logical-equivalence>`. See :ref:`logical-primitives` for more information regarding the number of necessarily primitive logical connectives.

.. _logical-inference:

---------
Inference
---------

.. _modus-ponens:

Law of Detachment
-----------------

The *Law of Detachment* is a symbolic expression for the process of deductive logic. The truth of an implication is asserted in conjunction with the truth of its hypothesis, which leads to the truth of the implication's consequence. Symbolically,

.. math::

    ( (p \implies q) \land p ) \implies q

.. note::

    The *Law of Detachment* is often known by its Latin name, *modus ponens*.

Symbolic Arguments
------------------

TODO

.. _tautologies:

Tautologies
^^^^^^^^^^^

TODO

.. _contradictions:

Contradictions
^^^^^^^^^^^^^^

TODO

.. _carnaps-method:

Carnap's Method of Tautology
----------------------------

A common problem in formal :ref:`logic <logic>` is determining whether a given proposition is a :ref:`tautology <tautologies>`, i.e. :ref:`true <truth>` in all possible cases. Since the number of rows in a :ref:`truth table <truth-tables>` grows exponentially with the number of :ref:`propositions <proposition>`, the traditional method of :ref:`truth tables <truth-tables>` is computationally expensive. In `Introduction to Symbolic Logic and Its Applications`_, Carnap presents a different method for evaluating whether or not a given :ref:`proposition <proposition>` is a :ref:`tautology <tautologies>`. Rather than enumerating all possible cases and checking if each one is true, it suffices to show the assignment of false to a :ref:`proposition <proposition>` is impossible. In other words, Carnap's method starts by assuming the :ref:`proposition <proposition>` is false and then works backwards through the logical connectives to see whether or not an :ref:`assignment <value-assignment>` of false is consistent with the :ref:`proposition <proposition>`.

For example, consider the well-known property of implications,

.. math::

    ((p \implies r) \land (q \implies r)) \implies ((p \land q) \implies r)

To determine whether this constitues a :ref:`tautology <tautologies>`, it must be shown whether or not an :ref:`assignment <value-assignment>` of false can be made to the entire :ref:`proposition <proposition>`. The :ref:`proposition <proposition>` is built out of nested propositions. The :ref:`assignment <value-assignment>` of false to entire :ref:`proposition <proposition>` will in turn require the subformulas of the :ref:`proposition <proposition>` to assume particular values. This will yield conditions for evaluating whether the overall :ref:`assignment <value-assignment>` is consistent with the :ref:`assignment <value-assignment>` of its components. The top-level connective is,

.. math::

    s \implies t

Where :math:`s = (p \implies r) \land (q \implies r)` and :math:`t = ((p \land q) \implies r)`.

In order for this :ref:`implication <logical-implication>` to be false, the hypothesis, :math:`s`, must be :ref:`true <truth>`, while the consequence, :math:`t`, must be false.

The :ref:`assignment <value-assignment>` of false to :math:`t` in turn requires :math:`p \land q` to be true and :math:`r` to be false.

The :ref:`assignment <value-assignment>` of :ref:`true <truth>` to :math:`p \land q` in turn requires :math:`p` be true and :math:`q` be :ref:`true <truth>`.

Thus, it is seen in order for the :ref:`proposition <proposition>` itself to be false, :math:`p` and :math:`q` must be true, while :math:`r` is false.

These values, however, are inconsistent with the hypothesis, :math:`s`, which was required to be :ref:`true <truth>`, for :math:`p \implies r` and :math:`q \implies r` are both false under this :ref:`assignment <value-assignment>`, and thus their :ref:`conjunction <logical-conjunction>` is false. This :ref:`contradicts <contradictions>` our initial assumption that :math:`s` is :ref:`true <truth>`. Therefore, the entire :ref:`proposition <proposition>` cannot be false for any assignment and it must be concluded the entire :ref:`proposition <proposition>` is :ref:`true <truth>` for all possible values of :math:`p`, :math:`q` and :math:`r`.

.. math::

    \forall p, q, r: ((p \implies r) \land (q \implies r)) \implies ((p \land q) \implies r)

.. _categorical-logic:

Categorical Logic
=================

.. _aristotelian-logic:

------------------
Aristotelian Logic
------------------

Aristotelian logic differs from propositional logic. In (first order) propositional logic, the proposition being expressed is reduced to a single truth value and this value is what enables its syntactic calculus through symbolic arguments. Aristotle, however, viewed the proposition as being decomposed into *terms* which then had categorical relations asserted between them. In other words, The Aristotelian model of logic is the study of sentences that express *categorical relations* between *terms*.

.. topic:: Definition

  1. Uppercase Letters (**A**, **B**, **C**): Terms.
  2. Lowercase Letters (**a**, **i**, **o**, **e**): Categorical Relations

A "*term*" in Aristotelian logic is not quite a :ref:`set <sets>` and it is not quite a :ref:`proposition <proposition>`. A "*term*" is a grammatical object that denotes both the *subject* and the *predicate*. In short, a *term* can be understood, roughly, as Aristotle's "*οὐσία*", the substance and essence of a *thing*.

The ontological status of a "*term*" in Aristotelian logic is substantially more complex than the preceding implies. To fully elucidate its natures requires a nuanced discussion on the `Categories`_ of Aristotle. To be brief, Aristotle considers thought of :ref:`language <language>` as being composed of ten categories,

1. Substance (οὐσία): What something fundamentally is.
2. Quantity (ποσόν): How much or how many of the subtance exists.
3. Quality (ποιόν): What kind or sort of thing a substance is.
4. Relation (πρός τι): How a substance stands in reference to another substance.
5. Place (ποῦ): Where the substance is located.
6. Time (πότε): When the substance exists.
7. Position (κεῖσθαι): The physical arrangement of the substance's parts.
8. State (ἔχειν): The condition or state of having something.
9. Action (ποιεῖν): What the substance is actively doing.
10. Passion (πάσχειν): What is being done to the substance.

The ultimate subject of a sentence in Aristotelian logic must reduce to a "*substantial* :ref:`being <being>`" of reality.

.. topic:: Definitions

  1. **AaB**: All **B** are **A**.
  2. **AiB**: Some **B** are **A**.
  3. **AoB**: Some **B** are not **A**
  4. **AeB**: No **B** are **A**

The sentences **AaB** and **AeB** are called *universal assertions* since they express relations of the whole. The sentences **AiB** and **AoB** are called *particular assertions* since they express relations between the parts.

A sentence *p* is the *contradictory* of another sentence *q* if the :ref:`truth <truth>` of *p* implies the falsity of the *q* and the falsity of *p* implies the :ref:`truth <truth>` of *q*. For example, if all **B** are **A** is true, then it must be the case that some **B** are not **A** is false (i.e., some **B** *are* A). In the opposite direction, if all **B** are **A** is false, then it must be the case the some **B** are not **A** is true

.. topic:: Contradictories

  1. **AaB** is the contradictory of **AoB**
  2. **AiB** is the contradictory of **AeB**

A sentence *p* is the *contrary* of *q* if the :ref:`truth <truth>` of *p* implies the falsity of *q*, but the falsity of *p* does not imply the falsity of *q*. For example, if **AaB** is true, then it must be the case that **AeB** is false. However, if **AaB** is false, then **AeB** is not necessarily true, since it may be the case **AiB**.

.. topic:: Contraries

  1. **AaB** is the contrary of **AeB**
  2. **AeB** is the contray of **AaB**

A sentence *p* is the *subcontrary* of *q* is the falsity of *p* implies the :ref:`truth <truth>` of *q*, but the :ref:`truth <truth>` of *p* does not imply the falsity of *q*. For example, if **AiB** is false, then it must be the case **AoB**. However, from the truth of **AiB**, nothing regarding **AoB** can be deduced.

.. topic:: Subcontraries

  1. **AiB** is *subcontrary* of **AoB**
  2. **AoB** is the *subcontray* of **AiB**

A sentence *p* is the *subalternation* of *q* if the :ref:`truth <truth>` of *q* implies the :ref:`truth <truth>` of *p*. For example, if **AaB**, it must be the case **AiB**.

.. topic:: Subalternations

  1. **AiB** is the subalternation of **AaB**
  2. **AoB** is the subalternation of **AeB**

A sentence *p* is the *superalternation* of *q* if the falsity of *q* implies the falsity of *p*. For example, if **AiB** is false, then **AaB** must also be false.

.. topic:: Superalternations

  1. **AaB** is the superalternation of **AiB**
  2. **AeB** is the superalternation of **AoB**

.. _aristotelian-conversions:

Conversions
-----------

1. **AeB** → **BeA**

TODO

2. **BiA** → **AiB**

TODO

3. **AaB** → **AiB**

TODO

.. _aristotelian-figures:

Figures
-------

.. note::

  The traditional medieval pneumonic devices are included beside each deductive figure. The order of the vowels in the Latin name corresponds to the order of relations in symbolic argument.

First Figure
^^^^^^^^^^^^

1. (*Barbara*) **AaB**, **BaC** ⊢ **AaC**

TODO

2. (*Celarent*) **AeB**, **BaC** ⊢ **AeC**

TODO

3. (*Darii*) **AaB**, **BiC** ⊢ **AiC**

TODO

4. (*Ferio*) **AeB**, **BiC** ⊢ **AoC**

Second Figure
^^^^^^^^^^^^^

1. (*Camestres*) **MaN**, **MeX** ⊢ **NeX**

TODO

2. (*Cesare*) **MeN**, **MaX** ⊢ **NeX**

TODO

3. (*Festino*) **MeN**, **MiX** ⊢ **NoX**

TODO

4. (*Baroco*) **MaN**, **MoX** ⊢ **NoX**

TODO

Third Figure
^^^^^^^^^^^^

1. (*Darapti*) **PaS**, **RaS** ⊢ **PiR**

.. note::

  This one could be strengthened in a system with more expressive power to "all P that are S are also R".

TODO

2. (*Felapton*) **PeS**, **RaS** ⊢ **PoR**

TODO

3. (*Datisi*) **PaS**, **RiS** ⊢ **PiR**

TODO

4. (*Disamis*) **PiS**, **RaS** ⊢ **PiR**

TODO

5. (*Bocardo*) **PoS**, **RaS** ⊢ **PoR**

TODO

6. (*Ferison*) **PeS**, **RiS** ⊢ **PoR**

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
