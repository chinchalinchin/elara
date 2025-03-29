.. _tarski:

------
Tarski
------

.. _tarski-logical-primitives:

Logical Primitives
------------------

In one of his earlier papers published in 1923, *On the Primitive Term of Logistic*, Tarksi proved all logical operations in second-order logic could be defined in terms of quantification (i.e. categorical assertions) and equivalence (i.e. substitutability). 

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

However, there is an interesting *implicit* assumption being made by asserting this theorem. The validity of this theorem rests on the contradiction of the inner expression :math:`\forall q: q`. In other words, in order for this theorem to obtain, it must be the case that :math:`\forall q: q` is always false. :math:`\neg \forall q: q` is indeed true, but not unconditionally, and the conditions in which it is not true are worth considering. The essence of this distinction is given in the insight the truth being expressed in the proposition :math:`\neg \forall q: q` is of a different order than a truth that is expressed tautologically, e.g. by a pure equivalence such as :math:`\neg(p \lor q) \equiv (\neg p \land \neg q)`. 

Tautological truths are vacuous; they reveal nothing about the state of the world. A proposition such as :math:`p \lor \neg p` is a *formal* truth that depends only on the syntax of logic. It's truth is not a function of the language in which it is expressed; While the symbols :math:`\lor` and :math:`\neg` may be assigned different meanings, the resulting language will still retain an expression which expresses the fundamental logical truth given by the law of excluded middle, however cumbersome and unintuitive its symbolic representation in this hypothetical language may be.

In contrast, :math:`\neg \forall q: q` is not *necessarily* true in any language, where "*language*" is to be understood as the set of all propositions *q*. It is conceivable to imagine a language that only allows the expression of true statements, in which case, since all *q* are true, :math:`\neg \forall q: q`, a *meta*-proposition *about* the language, becomes false. 

In addition, it is conceivable to imagine a language that expresses notions other than truth-values, in which case *q* cannot be treated as an assertion of truth and the *meta*-proposition :math:`\neg \forall q: q` becomes meaningless. 

If :math:`\neg \forall q: q` is to be true, it must be the case that language given by the set of *q* is capable of expressing false statements. In other words, :math:`\neg \forall q: q` is a proposition about the semantic content of :math:`\{ q | \forall q: q \}`, in particular, it is asserting a partition of the language into those statements which are true and those statements which are false exists, and furthermore, the partition of false propositions is non-empty.

.. math::

    (\neg \forall q: q) \equiv (\exists q: \neg q)

In other words, at least one false proposition exists. While this is a pragmatic and practical assumption as far as any non-trivial language is concerned, it is nevertheless not a "free" assumption, in the sense that is automatically granted if the laws of tautology are also granted. The proposition :math:`\neg \forall q: q` cannot be unconditionally true, and so its truth depends on the particular language that is under inspection. In other words, :math:`\neg \forall q: q` is implicitly a proposition *about* propositions, namely that not all of them can be true. 

If this assumption is granted, the other logical operations can be reduced to the operations of quantification and equivalence as follows: It is well-known disjunction can be defined in terms in of implication.

.. math::

    \forall p, q: (p \lor q) \equiv (\neg p \implies q) 

Moreover, it is well-known that logical implication can be defined in terms of equivalence and conjunction,

.. math::

    \forall p, q: (p \implies q) \equiv (p \equiv (p \land q))

Therefore, if conjunction can be defined in terms of equivalence and quantification, it can be asserted all of second-order logic is contained in the operations of equivalence and quantification, since all other operations can be syllogistically defined in terms of these two primitives. With this goal in mind, Tarksi builds up in sequence the following theorems.

**Theorem** :math:`\forall p: tr(p)`
   
All propositions are equivalent to themselves. Every proposition is either true or false, whence the following truth table obtains, 

.. list-table:: 
  :header-rows: 1

  * - :math:`p`
    - :math:`p \equiv p`
  * - T
    - T
  * - F
    - T

**Theorem** :math:`\forall p: (\forall q: p \equiv tr(q)) \implies p`

All propositions that are always true implies themselves. 

For each proposition *q* in the hypothesis, the following truth table describes the possible outcomes,

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

Since the hypothesis is always false exactly when *p* is false, the theorem follows from the definition of implication. 

**Theorem** :math:`\forall p, q: p \implies (p \equiv tr(q))`

All propositions imply they are equivalent to always being true. The truth table from the previous theorem can be used to verify this theorem for every possible proposition *p* and *q*.

Here is where the collapse of all true expressions into an equivalence class occurs. Truth is what aggregates the descriptive operators of language into a whole. It is what unites the propositions "2 + 2 = 4" and "Snow is white" into an equivalence. Truth, in effect, abstracts away the descriptive predicatives of a language, at least insofar as this formulation is concerned.

**Theorem** :math:`\forall p: (\forall q: p \equiv tr(q)) \equiv p`

All propositions are equivalent to being equivalent to always being true. Once again, this can be demonstrated with the previous truth-table.

Any true proposition is equivalent to any other true proposition because they are all equivalent to tautologies. Only in this desolate landscape of pure vacuity can *truth* be defined. A tautology expresses through form what is self-evident. 

Truth, however, is not a mere consequence of self-evidence. It is not wholly :ref:`a priori <a-priori-a-posteriori>`; it is constructed out of parts tautologous and parts empirical, in short it is :ref:`synthetic <synthesis>`. This realization is what led to Tarski to the insights which fueled *Concept of Truth in Formalized Languages* in 1931.   

**Theorem** :math:`\forall p,q: (\forall f: p \equiv (\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))) \implies q`

The formulae :math:`\forall r: p \equiv f(r)` and :math:`\forall r: q \equiv f(r)` serve as the main content of this theorem. Therefore, to understand the theorem, these formulae must be understood. Tarski refers to the terms :math:`f(r)` as a *truth* functions. He references the work of Russell and Whitehead in elaborating the conditions that must be met to refer to a function as a *truth* function, namely,

.. math::

    \forall p, q, f: ((p \equiv q) \land f(p)) \implies f(q) 

In essence, this definition asserts that if two conditions are satisfied, then *f* may be regarded as truth-function. 

First, it must be the case *p* and *q* are indistinguishable through their truth-value. The propositions ":math:`(5 - 2) \ cdot (5 + 2) - 21 = 0`", "*Earth has one moon*", "*George Washington was the first president*", "*The Vietnam War followed the Korean War*" must all be regarded as tokens of the same type of "*truth*", i.e. a syntactic truth that may be shunted through the laws of tautology. This is a loose constraint on what propositions are to be regarded as "equivalent". The only thing that need unite propositions into a equivalency is they be regarded as true under a particular assignment. 

Second, there must be a *f* that is well-defined for *p*, e.q. :math:`x^2 \in C` ("a square is a continuous function"), "'Earth has one moon' has one subject.", "'George Washington was the first president' belongs to American History". *f* is a descriptive predicative that abstracts out of its subject a property and asserts a categorical relation with respect to it, e.g. "*All propositions of the form* ':math:`p \land q`' *are true when* :math:`p \implies q` *and* :math:`p` *are both true*" or "*Some propositions of the form* :math:`p \lor q` *are true when p is true*". 

*f* is a type of *meta-tautology*, a vacuous truth of the second order, in contrast to a first order tautology such as :math:`p \lor \neg p`. It is not a tautology *in* the language, but a tautology *about* a language. To say the subject ":math:`1+4+9+16` *is a sum of squares*" is to restate through predication what is already demonstrated through the subject. The description is reflexive. This type of analysis is reminiscent of Aristotelian reciprocals,

.. epigraph::

    We may perhaps most easily comprehend that to which a thing is related, when a name does not exist, if, from that which has a name, we derive a new name, and apply it to that with which the first is reciprocally connected, as in the aforesaid instances, when we derived the word 'winged' from 'wing' and from 'rudder' the word 'ruddered.'  For example, suppose the correlative of 'head' were to be defined as 'animal' - this would be inept and inaccurate. For animal is the correlative of 'man' or 'ox' or other things of that kind, whereas 'head' is held to be correlative to 'that which has a head'. If, therefore, we are to discover the proper correlative of 'head', we might state it as 'headed'. If, however, there were no such word as 'headed', we should have to invent one for the purpose, just as in the instances given above where we coined the words 'winged' and 'ruddered.' For 1  'wing' is relative to 'winged' and 'rudder' to 'ruddered.'

    -- `Categories <categories>`_, Aristotle

To see in detail what is meant by this definition, it instructive to analyze it through application, to understand how its meaning is built up through its components. Since the definition is being quantified over the domain of propositions, i.e. those objects which can be regarded as either true or false, it suffices to restrict attention to the possible assignments to these propositions, to see what conditions they impose through the definition on the form of the truth function :math:`f(p)`.

If *p* is true and *q* is true, then the equivalency relation in the definition holds. By the laws of tautology,

.. math:: 


If it :math:`f(p)` is false, then any assignment to :math:`f(q)` will satisfy the definition. In short, if *p* and *q* are equivalent, then the definition is equivalent to,

TODO 

If *p* is false and *q* is true, or visa versa, the equivalency relation in the definition fails to obtain. If the hypothesis of the implication is false, then the consequence may be either true or false. Thus, in these cases, any assignment to :math:`f(p)` and :math:`f(q)` will satisfy the definition.

If *p* is false and *q* is false, or if *p* is true and *q* is true, then the equivalency is true. Then, either :math:`f(p)` is true, or it is false. If it is true, then the implication is only true is :math:`f(q)` is also true. If it :math:`f(p)` is false, then any assignment to :math:`f(q)` will satisfy the definition. In short, if *p* and *q* are equivalent, then the definition is equivalent to,

.. math::

    f(p) \implies f(q)

Thus, if *p* and *q* are equivalent, **and** if :math:`f(p)` expresses a true property of *p*, then :math:`f(q)` also expresses a true property of *q*.

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

.. _tarski-methodology-of-deductive-sciences:

Deductive Science
-----------------

In his 1930 paper *On Fundamental Concepts of the Methodology of Deductive Sciences*, Tarski began to refine his notion of truth by incorporating semantics into his constructions. Or, to more accurate, he refined his notion of truth by making the semantic assignment of truth a primitive notion. In this paper, Tarski starts by assuming the sentences under analysis have already been interpretted within the semantics of a science.

.. topic:: Definitions 

    1. :math:`S`: The set of all meaningful sentences in a science. 
    2. :math:`A`: An arbitrary subset of **S**.
    3. :math:`C_n(A)`
    4. :math:`E_{f(x)}[ ... ]`: The set of all values of the function *f* corresponding to those values of the argument *x* which satisfy the condition formulated in the brackets "[..]".
    5. :math:`\mathbb{P}(A) = E_X[X \subseteq A]`: The powerset of A, i.e. the set of all subsets of A. 
    6. :math:`\mathbb{F} = E_X[ \lvert X \rvert \leq \aleph_0]`: The set of all finite "inductive"sets.
 
With these minimalistic definitions, Tarski offers up four axioms to construct a science of science,

.. topic:: Axiom 1

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

If one corpus is contained in another corpus, then the consequences of the first corpus are contained in the consequences of the second corpus. In effect, this means the consequences of a part of a deductive science cannot exceed the consequences of the whole of a deductive science. 

By assumption,

.. math::

    A \subseteq B \implies P(A) \subset P(B)

And in turn,

.. math::

    P(A) \subseteq P(B) \implies P(A) \cdot \mathbb{F} \subset P(B) \cdot \mathbb{F}

In other words, the indices of the sum for :math:`C_n(A)` are included in the indices of the sum for :math:`C_n(B)`, meaning all of the elements in :math:`C_n(a)` are also elements of :math:`C_n(B)` but elements in :math:`C_n(B)` are not necessarily elements of :math:`C_n(A)`, whereby it follows from the definition of unions and subsets,

.. math::

    C_n(A) \subseteq C_n(B)

**Theorem** If :math:`A + B \subseteq S` then the formulas :math:`A \subseteq C_n (B)` and :math:`C_n(A) \subseteq C_n(B)` are equivalent. 

TODO

**Theorem** If :math:`A + B \subseteq S`, then :math:`C_n(A + B) = C_n(A + C_n(B)) = C_n(C_n(A) + C_n(B))`

TODO