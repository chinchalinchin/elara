.. _probatum:

--------
Probatum
--------

.. _induction:

Induction
---------

.. topic:: First Principle of Finite Induction

    Let :math:`S` be a set of positive integers with the following properties.

    1. :math:`1 \in S`
    2. :math:`k \in S \implies (k+1) \in S`

    Then :math:`S` is the set of all positive integers.

Let :math:`T` be the set of all positive integers not in :math:`S`. Assume :math:`T` is non-empty. By the Well-Ordering Principle, :math:`T` has a least element, denoted :math:`a`. Because :math:`1 \in S`, certainly :math:`a > 1` and so, :math:`0 < a - 1 < a`. The choice of :math:`a` as the smallest positive integer in :math:`T` implies that :math:`a-1` is not a member of :math:`T`, or equivalently, :math:`(a-1) \in S`. By hypothesis, :math:`(a - 1 + 1) = a`, which is also in :math:`S`, contradicting the assumption that :math:`a \in T`. Therefore, by contradiction, the set :math:`T` must be empty and as a consequence, :math:`\forall n \in \mathbb{N}: n \in S`.

.. _transfinitude:

Transfinitude
-------------

.. _rebellious-set:

The Curse of the Rebellious Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. topic:: Definition: The Rebellious Set

    Let :math:`A` be any set and let :math:`P(A)` be it's power set. Assume :math:`f: A \to P(A)`. The Rebellious Set, denoted R, is defined as the set which satisfies this formula,

    .. math::

        R = \{ x \in A \, \mid \, x \notin f(x) \}

**Theorem** :math:`f: A \to P(A) \leftrightarrow \lvert R \rvert \geq 1`

Let :math:`P(A)` be the power set of :math:`A` (the set of all subsets of :math:`A`). Suppose there exists a bijection :math:`f: A \to P(A)`. This means every element in :math:`A` is paired with a unique subset of :math:`A`, and vice versa.

If :math:`A = \emptyset`, then its power set :math:`P(A)` contains one element, the empty set itself, :math:`P(A) = {∅}`. In this case, there's no bijection between :math:`A` and :math:`P(A)`, and the theorem holds trivially.

If :math:`A \neq \emptyset`, it must contain at least one element. Let *a* be this element. Consider the subset of :math:`A`` that contains only this element, :math:`\{a\}`. Since *f* is assumed to be a bijection, there must be some element :math:`y \in A` such that :math:`f(y) = \{a\}`.

If :math:`y = a`, then, :math:`a \in f(a)`, which contradicts the definition of :math:`B` (that is, the elements in :math:`B` are not in the set they are mapped to).

If :math:`y \neq a`, then :math:`y \notin f(y)`, which means *y* should be in :math:`B` according to its definition. Since *y* exists, :math:`B` is not empty. ∎

.. _more-parts-than-wholes:

More Parts Than Wholes
^^^^^^^^^^^^^^^^^^^^^^

**Theorem** :math:`\forall A: \lvert P(A) \rvert > \lvert A \rvert`

For the sake of contradiction, suppose there exists a bijection (a one-to-one correspondence)  :math:`f: A \to P(A)`. This means every element in :math:`A` is paired with a unique subset of :math:`A`, and vice versa.

Consider the rebellious set,

.. math::

    R = \{ x \in A \, \mid \, x \notin f(x) \}

This set :math:`R` contains all elements of :math:`A` that are not members of the subset they are mapped to by *f*. By the previous theorem, this set is non-empty. Since *f* is a bijection, there must be an element :math:`r \in A` such that :math:`f(r) = R`.

If :math:`r \in R`, then by the definition of :math:`R`, :math:`r \notin f(r)`. But :math:`f(r) = R`, so :math:`r \notin R`, a contradiction.

If :math:`r \notin R`, then by the definition of :math:`R`, :math:`r \in f(r)`. But :math:`f(r) = R`, so :math:`r \in R`, again a contradiction.

The initial assumption that there exists a bijection between :math:`A` and :math:`P(A)` must be false.

Therefore,

.. math::

    \lvert P(A) \rvert > \lvert A \rvert

.. _logical-primitives:

Logical Primitives
------------------

In one of his earlier papers published in 1923, *On the Primitive Term of Logistic*, Tarksi proved all logical operations in second-order logic could be defined in terms of :ref:`quantification <logical-quantification>` (i.e. categorical assertions) and :ref:`equivalence <logical-equivalence>` (i.e. substitutability).

In doing so, Tarksi introduced a ":ref:`truth <truth>`" predicate into the meta-language of analysis. This notion of ":ref:`truth <truth>`" differs considerably from the natural conception of :ref:`truth <truth>`, for it treats :ref:`truth <truth>` as an equivalency with syntactically tautologous expressions. It becomes clear, as his definitions are made and theorems derived, that this meta-logical definition of ":ref:`truth <truth>`" is insufficient for fully elaborating the synthetic and empirical modes of :ref:`truth <truth>`.

.. topic:: Definition: Truth

    "*p is true*" is equivalent to "*p*"" being equivalent to "*p*".

    .. math::

        \forall p: tr(p) \equiv (p \equiv p)

.. topic:: Definition: Assertion

    "*p is asserted*" is equivalent to "*p*"

    .. math::

        \forall p: as(p) \equiv p

.. topic:: Definition: Falsity

    "*p is false*" is equivalent to "*p*" being equivalent to "*not p*"

    .. math::

        \forall p: fl(p) \equiv (p \equiv \neg p)

The predicates ":ref:`truth <truth>`", "*falsity*" and "*assertion*" should be understood operationally as predicates which satisfy these extensional definitions, and not as representatives of their colloquial interpretations.

The use of the indeterminate predicate :math:`f(p)` in these definitions implicitly allows second-order constructs into the discourse. :math:`f(p)`, for any *f*, is equivalent to asserting there exists an :math:`F` such that :math:`p \in F`, where :math:`F` is the *set* of :math:`p`'s that have the property *f*. Predication is a sneaky way of inserting ":ref:`sets <sets>`"  (or "*classes*") into a language without explicitly introducing the predicates :math:`\in` and :math:`\subset`. Refer to :ref:`Frege's Law V <frege-axioms>` for the ultimate consequences of abstraction.

Tarski begins the paper with a reference to a previously established result that shows logical :ref:`negation <logical-negation>` can be defined using only :ref:`quantification <logical-quantification>` and :ref:`equivalence <logical-equivalence>`,

.. math::

    \forall p: (\neg p) \equiv (p \equiv (\forall q: q))

Tarski uses this theorem as a starting point to show that :ref:`equivalence <logical-equivalence>` and :ref:`quantification <logical-quantification>` constitute the sole primitive terms of propositional calculus.

However, there is an interesting *implicit* assumption being made by asserting this theorem. The validity of this theorem rests on the contradiction of the inner expression :math:`\forall q: q`. In other words, in order for this theorem to obtain, it must be the case that :math:`\forall q: q` is always false. :math:`\neg \forall q: q` is indeed true, but not unconditionally, and the conditions in which it is not true are worth considering. The essence of this distinction is given in the insight the truth being expressed in the proposition :math:`\neg \forall q: q` is of a different order than a truth that is expressed :ref:`tautologically <tautologies>`, e.g. by a pure :ref:`equivalence <logical-equivalence>` such as :math:`\neg(p \lor q) \equiv (\neg p \land \neg q)`.

:ref:`Tautological <tautologies>` :ref:`truth <truth>` are vacuous; they reveal nothing about the state of the world. A proposition such as :math:`p \lor \neg p` is a *formal* :ref:`truth <truth>` that depends only on the syntax of logic. It's :ref:`truth <truth>` is not a function of the :ref:`language <language>` in which it is expressed; While the symbols :math:`\lor` and :math:`\neg` may be assigned different meanings, the resulting :ref:`language <language>` will still retain an expression which expresses the fundamental logical :ref:`truth <truth>` given by the law of excluded middle, however cumbersome and unintuitive its symbolic representation in this hypothetical :ref:`language <language>` may be.

In contrast, :math:`\neg \forall q: q` is not *necessarily* :ref:`true <truth>` in any :ref:`language <language>`, where ":ref:`language <language>`" is to be understood as the set of all :ref:`propositions <proposition>` *q*. It is conceivable to imagine a :ref:`language <language>` that only allows the expression of true statements, in which case, since all :math:`q` are :ref:`true <truth>`, :math:`\neg \forall q: q`, a *meta*-:ref:`proposition <proposition>` *about* the :ref:`language <language>`, becomes false.

In addition, it is conceivable to imagine a :ref:`language <language>` that expresses notions other than :ref:`truth values <truth-values>`, in which case *q* cannot be treated as an assertion of :ref:`truth <truth>` and the *meta*-:ref:`proposition <proposition>` :math:`\neg \forall q: q` becomes meaningless.

If :math:`\neg \forall q: q` is to be :ref:`true <truth>`, it must be the case that :ref:`language <language>` given by the set of *q* is capable of expressing false statements. In other words, :math:`\neg \forall q: q` is a :ref:`proposition <proposition>` about the semantic content of :math:`\{ q | \forall q: q \}`, in particular, it is asserting a partition of the :ref:`language <language>` into those statements which are true and those statements which are false exists, and furthermore, the partition of false :ref:`propositions <proposition>` is non-empty.

.. math::

    (\neg \forall q: q) \equiv (\exists q: \neg q)

In other words, at least one false :ref:`proposition <proposition>` exists. While this is a pragmatic and practical assumption as far as any non-trivial :ref:`language <language>` is concerned, it is nevertheless not a "*free*" assumption, in the sense that is automatically granted if the laws of :ref:`tautology <tautologies>` are also granted. The proposition :math:`\neg \forall q: q` cannot be unconditionally true, and so its truth depends on the particular :ref:`language <language>` that is under inspection. In other words, :math:`\neg \forall q: q` is implicitly a :ref:`proposition <proposition>` *about* :ref:`propositions <proposition>`, namely that not all of them can be :ref:`true <truth>`.

If this assumption is granted, the other logical operations can be reduced to the operations of quantification and equivalence as follows: It is well-known :ref:`disjunction <logical-disjunction>` can be defined in terms in of :ref:`implication <logical-implication>`.

.. math::

    \forall p, q: (p \lor q) \equiv (\neg p \implies q)

Moreover, it is well-known that logical implication can be defined in terms of equivalence and conjunction,

.. math::

    \forall p, q: (p \implies q) \equiv (p \equiv (p \land q))

Therefore, if :ref:`conjunction <logical-conjunction>` can be defined in terms of equivalence and quantification, it can be asserted all of second-order logic is contained in the operations of :ref:`equivalence <logical-equivalence>` and :ref:`quantification <logical-quantification>`, since all other operations can be syllogistically defined in terms of these two primitives. With this goal in mind, Tarksi builds up in sequence the following theorems.

**Theorem** :math:`\forall p: tr(p)`

All propositions are equivalent to themselves. Every proposition is either true or false, whence the following :ref:`truth table <truth-tables>` obtains,

.. list-table::
  :header-rows: 1

  * - :math:`p`
    - :math:`p \equiv p`
  * - T
    - T
  * - F
    - T

**Theorem** :math:`\forall p: (\forall q: p \equiv tr(q)) \implies p`

All propositions that are always :ref:`true <truth>` implies themselves.

For each proposition *q* in the hypothesis, the following :ref:`truth table <truth-tables>` describes the possible outcomes,

.. list-table::
  :header-rows: 1

  * - :math:`p`
    - :math:`q`
    - :math:`q \equiv q`
    - :math:`p \equiv (q \equiv q)`
  * - T
    - T
    - T
    - T
  * - T
    - F
    - T
    - T
  * - F
    - T
    - T
    - F
  * - F
    - F
    - T
    - F

Since the hypothesis is always false exactly when :math:`p` is false, the theorem follows from the definition of implication.

**Theorem** :math:`\forall p, q: p \implies (p \equiv tr(q))`

All propositions imply they are equivalent to always :ref:`being <being>` :ref:`true <truth>`. The :ref:`truth table <truth-tables>` from the previous theorem can be used to verify this theorem for every possible proposition :math:`p` and :math:`q`.

Here is where the collapse of all :ref:`true <truth>` expressions into an equivalence class occurs. :ref:`Truth <truth>` is what aggregates the descriptive operators of language into a whole. It is what unites the propositions "2 + 2 = 4" and "Snow is white" into an equivalence. :ref:`Truth <truth>`, in effect, abstracts away the descriptive predicatives of a language, at least insofar as this formulation is concerned.

**Theorem** :math:`\forall p: (\forall q: p \equiv tr(q)) \equiv p`

All propositions are equivalent to being equivalent to always being :ref:`true <truth>`. Once again, this can be demonstrated with the previous :ref:`truth table <truth-tables>`.

Any :ref:`true <truth>` proposition is equivalent to any other :ref:`true <truth>` proposition because they are all equivalent to tautologies. Only in this desolate landscape of pure vacuity can :ref:`truth <truth>` be defined. A tautology expresses through form what is self-evident.

:ref:`Truth <truth>`, however, is not a mere consequence of self-evidence. It is not wholly :ref:`a priori <a-priori-a-posteriori>`; it is constructed out of parts tautologous and parts empirical, in short it is :ref:`synthetic <synthesis>`. This realization is what led to Tarski to the insights which fueled `The Concept of Truth in Formalized Languages`_ in 1931.

**Theorem** :math:`\forall p,q: (\forall f: p \equiv (\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))) \implies q`

The formulae :math:`\forall r: p \equiv f(r)` and :math:`\forall r: q \equiv f(r)` serve as the main content of this theorem. Therefore, to understand the theorem, these formulae must be understood. Tarski refers to the terms :math:`f(r)` as a :ref:`truth <truth>` functions. He references the work of Russell and Whitehead in elaborating the conditions that must be met to refer to a function as a :ref:`truth <truth>` function, namely,

.. math::

    \forall p, q, f: ((p \equiv q) \land f(p)) \implies f(q)

In essence, this definition asserts that if two conditions are satisfied, then *f* may be regarded as truth-function.

First, it must be the case :math:`p` and :math:`q` are indistinguishable through their :ref:`truth-value <truth-values>`. The propositions ":math:`(5 - 2) \cdot (5 + 2) - 21 = 0`", "*Earth has one moon*", "*George Washington was the first president*", "*The Vietnam War followed the Korean War*" must all be regarded as tokens of the same type of ":ref:`truth <truth>`", i.e. a syntactic :ref:`truth <truth>` that may be shunted through the laws of tautology. This is a loose constraint on what propositions are to be regarded as "equivalent". The only thing that need unite propositions into a equivalency is they be regarded as true under a particular assignment.

Second, there must be a *f* that is well-defined for *p*, e.q. :math:`x^2 \in C` ("a square is a continuous function"), "'Earth has one moon' has one subject.", "'George Washington was the first president' belongs to American History". *f* is a descriptive predicative that abstracts out of its subject a property and asserts a categorical relation with respect to it, e.g. "*All propositions of the form* ':math:`p \land q`' *are true when* :math:`p \implies q` *and* :math:`p` *are both true*" or "*Some propositions of the form* :math:`p \lor q` *are true when p is true*".

*f* is a type of *meta-tautology*, a vacuous :ref:`truth <truth>` of the second order, in contrast to a first order tautology such as :math:`p \lor \neg p`. It is not a tautology *in* the :ref:`language <language>`, but a tautology *about* a :ref:`language <language>`. To say the subject ":math:`1+4+9+16` *is a sum of squares*" is to restate through predication what is already demonstrated through the subject. The description is reflexive. This type of analysis is reminiscent of Aristotelian reciprocals,

.. epigraph::

    We may perhaps most easily comprehend that to which a thing is related, when a name does not exist, if, from that which has a name, we derive a new name, and apply it to that with which the first is reciprocally connected, as in the aforesaid instances, when we derived the word 'winged' from 'wing' and from 'rudder' the word 'ruddered.'  For example, suppose the correlative of 'head' were to be defined as 'animal' - this would be inept and inaccurate. For animal is the correlative of 'man' or 'ox' or other things of that kind, whereas 'head' is held to be correlative to 'that which has a head'. If, therefore, we are to discover the proper correlative of 'head', we might state it as 'headed'. If, however, there were no such word as 'headed', we should have to invent one for the purpose, just as in the instances given above where we coined the words 'winged' and 'ruddered.' For 1  'wing' is relative to 'winged' and 'rudder' to 'ruddered.'

    -- `Categories`_, Aristotle

To see in detail what is meant by this definition, it instructive to analyze it through application, to understand how its meaning is built up through its components. Since the definition is being quantified over the domain of propositions, i.e. those objects which can be regarded as either true or false, it suffices to restrict attention to the possible assignments to these propositions, to see what conditions they impose through the definition on the form of the :ref:`truth <truth>` function :math:`f(p)`.

If :math:`p` is true and :math:`q` is true, then the equivalency relation in the definition holds. If it :math:`f(p)` is false, then any assignment to :math:`f(q)` will satisfy the definition. In short, if *p* and *q* are equivalent, then the definition is equivalent to,

.. math::

    f(p) \implies f(q)

If :math:`p` is false and :math:`q` is true, or visa versa, the equivalency relation in the definition fails to obtain. If the hypothesis of the implication is false, then the consequence may be either true or false. Thus, in these cases, any assignment to :math:`f(p)` and :math:`f(q)` will satisfy the definition.

If :math:`p` is false and :math:`q` is false, or if :math:`p` is true and :math:`q` is true, then the equivalency is true. Then, either :math:`f(p)` is true, or it is false. If it is true, then the implication is only true is :math:`f(q)` is also true. If it :math:`f(p)` is false, then any assignment to :math:`f(q)` will satisfy the definition. In short, if *p* and *q* are equivalent, then the definition is equivalent to,

.. math::

    f(p) \implies f(q)

Thus, if :math:`p` and :math:`q` are equivalent, **and** if :math:`f(p)` expresses a true property of *p*, then :math:`f(q)` also expresses a true property of *q*.

The insight to be gleaned here is this definition does not *fully* determine the form of :math:`f(q)`. It only imposes conditions on :math:`f(q)` when syntactical conditions align.

**Theorem** :math:`\forall p: \neg (\forall q: p \equiv as(q))`

To derive an English translation that avoids unnecessary convolutions, it must be tautologically re-expressed in a different form. Keeping in mind the laws of quantification,

.. math::

    \neg \forall x: f(x) \equiv \exists x: \neg f(x)

This can be restated as,

.. math::

    \forall p: \exists q: p \not\equiv as(q)

Which provides an serviceable translation into English: There is no proposition which is equivalent to the assertion of all propositions.

**Theorem** :math:`\forall p,q: (\forall r: p \equiv as(r)) \equiv (\forall r: q \equiv as(r))`

Every assertion of all propositions is equivalent to any other assertion of all propositions.

**Theorem** :math:`\forall p, q: (\forall f: p \equiv ((\forall r: p \equiv f(r) ) \equiv (\forall r: q \equiv f(r)))) \implies p`

One proposition being equivalent to the equivalency of all equivalent properties of another proposition implies the proposition.

**Theorem** :math:`\forall p,q: (\forall f: p \equiv ((\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))) ) \implies (p \land q)`

One proposition being equivalent to the equivalency of all equivalent properties of another proposition implies both propositions.

**Theorem** :math:`\forall p, q, f: (p \land q) \implies (p \equiv ((\forall r: p \equiv (fr)) \equiv (\forall r: q \equiv f(r))))`

Two propositions together imply one proposition is equivalent to the equivalency of all equivalent properties of the other proposition,

**Theorem** :math:`\forall p,q: (p \land q) \equiv (\forall f: p \equiv ((\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))))`

Two propositions together is equivalent to one proposition being equivalent to the equivalency of all equivalent properties of the other proposition.

Deductive Science
-----------------

In his 1930 paper *On Fundamental Concepts of the Methodology of Deductive Sciences*, Tarski began to refine his notion of :ref:`truth <truth>` by incorporating semantics into his constructions. Or, to more accurate, he refined his notion of :ref:`truth <truth>` by making the semantic assignment of :ref:`truth <truth>` a primitive notion. In this paper, Tarski starts by assuming the sentences under analysis have already been interpretted within the semantics of a science.

.. topic:: Definitions

    1. :math:`S`: The set of all meaningful sentences in a science.
    2. :math:`A`: An arbitrary subset of **S**.
    3. :math:`C_n(A)`
    4. :math:`E_{f(x)}[ ... ]`: The set of all values of the function *f* corresponding to those values of the argument *x* which satisfy the condition formulated in the brackets "[..]".
    5. :math:`\mathbb{P}(A) = E_X[X \subseteq A]`: The powerset of A, i.e. the set of all subsets of A.
    6. :math:`\mathbb{F} = E_X[ \lvert X \rvert \leq \aleph_0]`: The set of all finite "inductive"sets.

With these minimalistic definitions, Tarski offers up four axioms to construct a science of science,

.. topic:: Axiom 1

    .. math::

        \lvert S \rvert \leq \aleph_0

.. topic:: Axiom 2

    If :math:`A \subseteq S` then :math:`A \subseteq C_n(A) \subseteq S`

.. topic:: Axiom 3

    If :math:`A \subseteq S` then :math:`C_n(C_n(A)) = C_n(A)`

.. topic:: Axiom 4

    If :math:`A \subseteq S` then :math:`C_n (A) = \sum_{X \in \mathbb{P}(A) \cdot \mathbb{F}} C_n(X)`

Upon reflection, Axiom 1 and Axiom 4 may appear to be at odds. It is instructive to highlight the tension that seems to exist between these two axioms and show the way in which this apparent tension is resolved. Axiom 1 of Tarski's deductive system asserts the set of meaningful sentences in a science is at most countably infinite. In fact, after introducing the axiom, in a brief aside, Tarski mentions in an aside that strict equality in Axiom 1 can be assumed without comprising his results.

Axiom 4, on the other hand, states the consequences of an arbitrary subset of meaningful sentences, :math:`A`, is the sum of consequences of sets taken over finite subsets of :math:`A`. Given that Axiom 1 states that :math:`S` is potentially infinte and the hypothesis of Axiom 4 allows the case :math:`A = S`, Axiom 4 appears to state the infinite set :math:`S` is the result of a finite union. In fact, Axiom 1 and Axiom 4 taken together *do assert* an infinite set is the result of a finite union. However, it is a finite union of *consequences*, which are not necessarily finite.

To understand the subtlety of Axiom 1 and Axiom 4, it suffices to consider

.. math::

    C_n({})

Which is to ask: what are the consequences of *nothing*? The consequences of *nothing* are exactly those propositions which are vacuously true, namely tautologies. Every tautological form generates an infinite number of tautologies through the recursive nature of the substitution principle. Take for example the law of the excluded middle, substituted into itself ad infinitum,

.. math::

    p \lor \neg p, (p \lor \neg p) \lor \neg(p \lor \neg p), ...

Thus, it is seen that even though Axiom 4 asserts an infinite set can be reduced to a finite number of unions, the terms of the union are not finite. In light of the recursive nature of tautologies, Tarski's offhand assertion regarding the infinite cardinality of :math:`S` becomes more plausible.

**Theorem** If :math:`A \subseteq B \subseteq S`, then :math:`C_n(A) \subseteq C_n(B)`

If one :ref:`corpus <corpus>` is contained in another :ref:`corpus <corpus>`, then the consequences of the first :ref:`corpus <corpus>` are contained in the consequences of the second :ref:`corpus <corpus>`. In effect, this means the consequences of a part of a deductive science cannot exceed the consequences of the whole of a deductive science.

By assumption,

.. math::

    A \subseteq B \implies P(A) \subset P(B)

And in turn,

.. math::

    P(A) \subseteq P(B) \implies P(A) \cdot \mathbb{F} \subset P(B) \cdot \mathbb{F}

In other words, the indices of the sum for :math:`C_n(A)` are included in the indices of the sum for :math:`C_n(B)`, meaning all of the elements in :math:`C_n(a)` are also elements of :math:`C_n(B)` but elements in :math:`C_n(B)` are not necessarily elements of :math:`C_n(A)`, whereby it follows from the definition of unions and subsets,

.. math::

    C_n(A) \subseteq C_n(B)
