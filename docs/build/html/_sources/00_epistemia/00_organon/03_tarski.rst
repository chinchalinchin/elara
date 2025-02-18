.. _tarski:

------
Tarski
------

.. _tarski-logical-primitives:

Logical Primitives
------------------

In one of his earlier papers, `On the Primitive Term of Logistic <>`_, Tarksi proved all logical operations in second-order logic could be defined in terms of quantification (i.e. categorical assertions) and equivalence (i.e. substitutability). 

In doing so, Tarksi introduced a "*truth*" predicate into the meta-language of analysis. This notion of "*truth*" differs considerably from the natural conception of truth, for it treats truth as an equivalency with syntactically tautologous expressions. It becomes clear, as his definitions are made and theorems derived, that this meta-logical definition of "*truth*" is insufficient for fully elaborating the synthetic and empirical modes of truth. 

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

In the following commentary, the predicates "*truth*", "*falsity*" and "*assertion*" should be understood operationally as predicates which satisfy these extensional definitions, and not as representatives of their colloquial interpretations.

The use of the indeterminate predicate *f(p)* in these definitions implicitly allows second-order constructs into the discourse. *f(p)*, for any *f*, is equivalent to asserting there exists an *F* such that :math:`p \in F`, where *F* is the *set* of *p*'s that have the property *f*. Predication is a sneaky way of inserting "*sets*" and "*classes*" into a language without explicitly introducing the predicates :math:`\in` and :math:`\subset`. Refer to :ref:`Frege's Law V <frege-grundgesetze>` for the ultimate consequences of abstraction.

Tarski begins the paper with a reference to a previously established result that shows logical negation can be defined using only quantification and equivalence, 

.. math::

    \forall p: (\neg p) \equiv (p \equiv (\forall q: q))

Tarski uses this theorem as a starting point to show that equivalence and quantification constitute the sole primitive terms of propositional calculus. 

However, there is an interesting *implicit* assumption being made by asserting this theorem. The validity of this theorem rests on the contradiction of the inner expression :math:`\forall q: q`. In other words, in order for this theorem to obtain, it must be the case that :math:`\forall q: q` is always false. :math:`\neg \forall q: q` is indeed true, but not unconditionally, and the conditions in which it is not true are worth considering. The essence of this distinction is given in the insight the truth being expressed in the proposition :math:`\neg \forall q: q` is of a different order than a truth that is expressed tautologically, e.g. by a pure equivalence such as :math:`(p \land (p \implies q)) \implies q`. 

Tautological truths are vacuous; they reveal nothing about the state of the world. A proposition such as :math:`p \lor \neg p` is a *formal* truth that depends only on the syntax of logic. It's truth is not a function of the language in which it is expressed; While the symbols :math:`\lor` and :math:`\neg` may be assigned different meanings, the resulting language will still retain an expression which expresses the fundamental logical truth given by the law of excluded middle, however cumbersome and unintuitive its symbolic representation in this hypothetical language may be.

In contrast, :math:`\neg \forall q: q` is not *necessarily* true in any language, where "*language*" is to be understood as the set of all propositions *q*. It is conceivable to imagine a language that only allows the expression of true statements, in which case, since all *q* are true, :math:`\neg \forall q: q`, a *meta*-proposition *about* the language, becomes false. 

In addition, it is conceivable to imagine a language that expresses notions other than truth-values, in which case *q* cannot be treated as an assertion of truth and the *meta*-proposition :math:`\neg \forall q: q` becomes meaningless. 

If :math:`\neg \forall q: q` is to be true, it must be the case that language given by the set of *q* is capable of expressing false statements. In other words, :math:`\neg \forall q: q` is a proposition about the semantic content of :math:`\{ q | \forall q: q \}`, in particular, it is asserting a partition of the language into those statements which are true and those statements which are false exists, and furthermore, the partition of false propositions is non-empty.

.. math::

    (\neg \forall q: q) \equiv (\exists q: \neg q)

In other words, at least one false proposition exists. While this is a pragmatic and practical assumption as far as any non-trivial language is concerned, it is nevertheless not a "free" assumption, in the sense that is automatically granted if the laws of tautology are also granted. The proposition :math:`\neg \forall q: q` cannot be unconditionally true, and so its truth depends on the particular language that is under inspection. In other words, :math:`\neg \forall q: q` is implicitly a proposition *about* propositions, namely that not all of them are true. 

If this assumption is granted, the other logical operations can be reduced to the operations of quantification and equivalence as follows: It is well-known disjunction can be defined in terms in of implication.

.. math::

    \forall p, q: (p \lor q) \equiv (\neg p \implies q) 


Moreover, it is well-known that logical implication can be defined in terms of equivalence and conjunction,

.. math::

    \forall p, q: (p \implies q) \equiv (p \equiv (p \land q))


Therefore, if conjunction can be defined in terms of equivalence and quantification, it can be asserted all of second-order logic is contained in the operations of equivalence and quantification, since all other operations can be syllogistically defined in terms of these two primitives. With this goal in mind, Tarksi builds up in sequence the following theorems.

**Theorem** :math:`\forall p: tr(p)`
   
All propositions are equivalent to themselves. 
   
**Theorem** :math:` \forall p: (\forall q: p \equiv tr(q)) \implies p`

All propositions that are always true implies themselves.

**Theorem** :math:`\forall p, q: p \implies (p \equiv tr(q))`

All propositions imply they are equivalent to always being true.

Here is where the collapse of all true expressions into an equivalence class occurs. Truth is what aggregates the descriptive operators of language into a whole. It is what unites the propositions "2 + 2 = 4" and "Snow is white" into an equivalence. Truth, in effect, abstracts away the descriptive predicatives of a language, at least insofar as this formulation is concerned.

**Theorem** :math:`\forall p: (\forall q: p \equiv tr(q)) \equiv p`

All propositions are equivalent to being equivalent to always being true. 

Any true proposition is equivalent to any other true proposition because they are all equivalent to tautologies. Only in this desolate landscape of pure vacuity can *truth* be defined. A tautology expresses through form what is self-evident. 

Truth, however, is not a mere consequence of self-evidence. It is not wholly :ref:`a-priori`; it is constructed out of parts tautologous and parts empirical, in short it is :ref:`synthetic`. This realization is what led to Tarski to the insights which fueled `Concept of Truth in Formalized Languages <>`_ in 1931.   

**Theorem** :math:`\forall p,q: (\forall f: p \equiv (\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))) \implies q`

One proposition being equivalent to the equivalency of all equivalent properties of another proposition implies the other proposition.

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