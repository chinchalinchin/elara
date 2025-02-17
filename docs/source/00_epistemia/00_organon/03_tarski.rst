.. _tarski:

------
Tarski
------

.. _tarski-logical-primitives:

Logical Primitives
------------------

Tarski explored the consequences of defining the logical conditions for truth in an early paper from 1923, `On The Primitive Term of the Logistic <>`_.

In this formulation, the notion of "*truth*" is treated as an equivalency with syntactically tautologous expressions. In this way, Tarski tries to define the "*truth*" of language within the language used to express true proposition. In this early attempt, he had not yet fully developed the distinction between semantics and syntax, between meta-languages and object-languages. 

It becomes clear, as his definitions are made and theorems derived, that this meta-logical definition of "*truth*" is insufficient 

.. topic:: Definition: Truth

    ``p is true`` is equivalent to ``p`` being equivalent to ``p``.

    .. math::

        \forall p: tr(p) \equiv (p \equiv p)

.. topic:: Definition: Assertion

    ``p is asserted`` is equivalent to ``p``

    .. math::

        \forall p: as(p) \equiv p

.. topic:: Definition: Falsity

    ``p is false`` is equivalent to ``p`` being equivalent to ``not p``

    .. math::

        \forall p: fl(p) \equiv (p \equiv \neg p)

The use of the *predicates* ``f(p)`` in these definitions implicitly allows second-order constructs into the discourse. ``f(p)``, for any *f*, is equivalent to asserting there exists an *F* such that :math:`p \in F`, where *F* is the *set* of *p*'s that have the property *f*. 

Predication is a sneaky way of inserting "*sets*" and "*classes*" into a language without explicitly introducing the predicates :math:`\in` and :math:`\subset`.
    
Refer to :ref:`frege-law-v` for the ultimate consequences of abstraction.

In the following commentary, the predicates "*truth*", "*falsity*" and "*assertion*" should be understood operationally as predicates which satisfy these extensional definitions. 

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

Truth, however, is not a mere consequence of self-evidence. It is not wholly :ref:`a-priori`; it is constructed out of parts tautologous and empirical, in short it is :ref:`synthetic`. This realization is what led to Tarski to the insights which fueled `Concept of Truth in Formalized Languages <>`_ in 1931.   

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

10. Two propositions imply one proposition is equivalent to the equivalency of all equivalent properties of the other proposition, 

.. math::

    \forall p, q, f: (p \and q) \implies (p \equiv ((\forall r: p \equiv (fr)) \equiv (\forall r: q \equiv f(r))))
    
11. The final theorem is a strengthening of the previous one,

.. math::

    \forall p,q: (p \and q) \equiv (\forall f: p \equiv ((\forall r: p \equiv f(r)) \equiv (\forall r: q \equiv f(r))))

However, to your point about negation, Tarski starts his paper by referencing another paper by Herny Hiz that showed negation could be defined as, 

.. math::

    \forall p: (\neg p) \equiv (p \equiv (\forall q: q))

So, it would seem, Tarski, along with Henry Hiz, have shown logic can be constructed using only quantification and equivalence. If conjunction can be reduced to these two operations, then implication can be defined,

.. math::

    \forall p, q: (p \implies q) \equiv (p \equiv (p \and q))

And it is straightforward to define disjunction in terms of implication, namely,

.. math::

    \forall p, q: (p \or q) \equiv (\neq p \implies q)

Discuss what that means. It would seem to mean that second order quantification allows the entirety of first order logic to be projected onto a single basis operation, namely, equivalence.

.. _tarski-mereology:

Mereology
---------

.. topic:: Definition: Parts

    :math:`\subset` (part-of relation): A binary relation that holds between two individuals when one is a part of the other.

.. topic:: Definition: Disjoint

    :math:`\otimes` (disjoint relation): A binary relation that holds between two individuals when they have no common parts.

.. topic:: Definition: Ergo Sum 
    
    Every element of *α* is a part of a sum,

    .. math::

        \forall y: y \in \alpha \to y \subset \sum \alpha
    
**Reflexivity**

    Every individual is a part of itself.

.. math::

    \forall x: x \subset x

**Transivity**

    If x is a part of y, and y is a part of z, then x is a part of z.

.. math::

    \forall x: \forall y: \forall z: ((x \subset y) \land (y \subset z)) \to (x \subset z)

**Antisymmetry**

    If x is a part of y, and y is a part of x, then x and y are identical.

.. math::

    \forall x: \forall y: ((x \subset y) \land (y \subset x) \to x = y)

**Supplementation**

    If x is not a part of y, then there exists a part z of x that is disjoint from y 

.. math::

    \forall x: \forall y: \neg(x \subset y) \to ((\exists z: z \subset x) \land (z \otimes y))

**Summation**

    For any non-empty class α of individuals, there exists an individual x that is the sum of all elements of α.

.. math::

    \forall \alpha \forall x: x = \sum \alpha

**Atomicity**

    Every non-empty class of individuals has an element that shares no parts with any other element.

.. math::

    \forall \alpha: \alpha \neq \emptyset \to (\exists x: (x \in \alpha) \land (\neg \exists y:(y \in \alpha) \land (y \subset x) ))