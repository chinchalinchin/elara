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

The use of the indeterminate predicate *f(p)* in these definitions implicitly allows second-order constructs into the discourse. *f(p)*, for any *f*, is equivalent to asserting there exists an *F* such that :math:`p \in F`, where *F* is the *set* of *p*'s that have the property *f*. 

Predication is a sneaky way of inserting "*sets*" and "*classes*" into a language without explicitly introducing the predicates :math:`\in` and :math:`\subset`. Refer to :ref:`frege-law-v` for the ultimate consequences of abstraction.

In the following commentary, the predicates "*truth*", "*falsity*" and "*assertion*" should be understood operationally as predicates which satisfy these extensional definitions, and not as representatives of their colloquial interpretations.

Tarski begins with a reference to a previously established result that shows logical negation can be defined using only quantification and equivalence, 

.. math::

    \forall p: (\neg p) \equiv (p \equiv (\forall q: q))

Moreover, it is well-known that logical implication can be defined in terms of equivalence and conjunction,

.. math::

    \forall p, q: (p \implies q) \equiv (p \equiv (p \and q))

It is also well-known disjunction can be defined in terms in of implication.

.. math::

    \forall p, q: (p \or q) \equiv (\neq p \implies q)

Therefore, if conjunction can be defined in terms of equivalence and quantification, it can be asserted all of second-order logic is contained in the operations of equivalence and quantification, since all other operations can be syllogistically defined in terms of them. With this goal in mind, Tarksi builds up in sequence the following theorems.

**Theorems**

1. All propositions are equivalent to themselves. 
   
.. math::

    \forall p: tr(p)
   
2. All propositions that are always true implies themselves.
   
.. math::

    \forall p: (\forall q: p \equiv tr(q)) \implies p

3. All propositions imply they are equivalent to always being true.

.. math::

    \forall p, q: p \implies (p \equiv tr(q))

Here is where the collapse of all true expressions into an equivalence class occurs. Truth is what aggregates the descriptive operators of language into a whole. It is what unites the propositions "2 + 2 = 4" and "Snow is white" into an equivalence. Truth, in effect, abstracts away the descriptive predicatives of a language, at least insofar as this formulation is concerned.

4. All propositions are equivalent to being equivalent to always being true. 

.. math::

    \forall p: (\forall q: p \equiv tr(q)) \equiv p

Any true proposition is equivalent to any other true proposition because they are all equivalent to tautologies. Only in this desolate landscape of pure vacuity can *truth* be defined. A tautology expresses through form what is self-evident. 

Truth, however, is not a mere consequence of self-evidence. It is not wholly :ref:`a-priori`; it is constructed out of parts tautologous and parts empirical, in short it is :ref:`synthetic`. This realization is what led to Tarski to the insights which fueled `Concept of Truth in Formalized Languages <>`_ in 1931.   

5. One proposition being equivalent to the equivalency of all equivalent properties of another proposition implies the other proposition.

.. math::

    \forall p,q: (\forall f: p \equiv (\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))) \implies q

6. The formal statement of this theorem is as follows,

.. math::

    \forall p: \neg (\forall q: p \equiv as(q))

To derive an English translation that avoids unnecessary convolutions, it must be tautologically re-expressed in a different form. Keeping in mind the laws of quantification, 

.. math::

    \neg \forall x: f(x) \equiv \exists x: \neg f(x)

This can be restated as,

.. math::

    \forall p: \exists q: p \not\equiv as(q)

Which provides an serviceable translation into English: There is no proposition which is equivalent to the assertion of all propositions. 

7. Every assertion of all propositions is equivalent to any other assertion of all propositions. 

.. math::

    \forall p,q: (\forall r: p \equiv as(r)) \equiv (\forall r: q \equiv as(r))

8. One proposition being equivalent to the equivalency of all equivalent properties of another proposition implies the proposition.

.. math::

    \forall p, q: (\forall f: p \equiv ((\forall r: p \equiv f(r) ) \equiv (\forall r: q \equiv f(r)))) \implies p 

9. One proposition being equivalent to the equivalency of all equivalent properties of another proposition implies both propositions.

.. math::

    \forall p,q: (\forall f: p \equiv ((\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))) ) \implies (p \and q)

10. Two propositions together imply one proposition is equivalent to the equivalency of all equivalent properties of the other proposition, 

.. math::

    \forall p, q, f: (p \and q) \implies (p \equiv ((\forall r: p \equiv (fr)) \equiv (\forall r: q \equiv f(r))))
    
11. Two propositions together is equivalent to one proposition being equivalent to the equivalency of all equivalent properties of the other proposition, 

.. math::

    \forall p,q: (p \and q) \equiv (\forall f: p \equiv ((\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))))