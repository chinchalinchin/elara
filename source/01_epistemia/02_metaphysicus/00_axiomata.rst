.. _axiomata:

--------
Axiomata
--------

.. _frege-axioms:

Frege
-----

.. topic:: Law III: Identity of Indiscernibles

    If two objects have the same properties, they are the same object.

    .. math::

        \forall a, b: (a = b) \equiv (\forall f: f(a) \equiv f(b))

.. topic:: Law V: Extensionality

    .. math::

        (\hat{\epsilon}f = \hat{\epsilon}g) \equiv (\forall x: f(x) \equiv g(x))

.. _peano-axioms:

Peano
-----

.. topic:: Axioms of Arithmetic

    1. :math:`1 \in \mathbb{N}`
    2. :math:`a \in \mathbb{N} \supset a = a`
    3. :math:`a,b \in \mathbb{N} \supset (a = b) = (b = a)`
    4. :math:`a, b, c \in \mathbb{N} \supset (a = b) \land (b = c) \land (a = c)`
    5. :math:`(a = b) \land b \in \mathbb{N} \supset a \in \mathbb{N}`
    6. :math:`a \in \mathbb{N} \supset (a + 1) \in \mathbb{N}`
    7. :math:`a,b \in \mathbb{N} \supset (a = b) \land (a + 1) \land (b + 1)`
    8. :math:`a \in \mathbb{N} \supset a + 1 \neq 1`
    9. :math:`(((k \in K) \land (1 \in k) \land (x \in \mathbb{N}) \land (x \in k)) \supset_x (x+1) \in k) \supset (N \supset k)`

.. _kolmogorov-axioms:

Kolmogorov
----------

.. topic:: Axiom of Continuity

    If :math:`A_i` is a sequence of decreasing events,

    .. math::

        A_1 \supset A_2 \supset ... \supset A_n

    And if the intersection of those events is empty,

    .. math::

        \cap_{i=1}^n A_i = \varnothing

    Then the limit as of the probability of this sequence is zero,

    .. math::

        \lim_{n \to \infty} P(A_n) = 0

.. _tarksi-axioms:

Tarski
------

.. _tarski-axioms-deductive-science:

-----------------
Deductive Science
-----------------

.. topic:: Definitions

    1. :math:`S`: The set of all meaningful sentences in a science.
    2. :math:`A`: An arbitrary subset of :math:`S`.
    3. :math:`C_n(A)`
    4. :math:`E_{f(x)}[ ... ]`: The set of all values of the function *f* corresponding to those values of the argument *x* which satisfy the condition formulated in the brackets "[..]".
    5. :math:`\mathbb{P}(A) = E_X[X \subseteq A]`: The powerset of A, i.e. the set of all subsets of A.
    6. :math:`\mathbb{F} = E_X[ \lvert X \rvert \leq \aleph_0]`: The set of all finite "inductive"sets.

.. topic:: Axioms of Deductive Science

    1. The number of sentences is finite or infinite.

    .. math::

        \lvert S \rvert \leq \aleph_0

    2. If :math:`A \subseteq S` then :math:`A \subseteq C_n(A) \subseteq S`

    3. If :math:`A \subseteq S` then :math:`C_n(C_n(A)) = C_n(A)`

    4. If :math:`A \subseteq S` then :math:`C_n (A) = \sum_{X \in \mathbb{P}(A) \cdot \mathbb{F}} C_n(X)`

.. _tarski-axioms-mereology:

---------
Mereology
---------

.. topic:: Definition: Length of Open Interval

    The length :math:`l(I)` of an open interval :math:`I` is defined by,

    1. If :math:`I = (a,b)` for some :math:`a, b \in \mathbb{R}` with :math:`a < b`, then :math:`l(I) = b - a` 
    
    2. If :math:`I = \emptyset`, then :math:`l(I) = 0`.
    
    3. If :math:`I = (-\infty, a)` or :math:`I = (a, \infty)`,for some :math:`a \in \mathbb{R}`, then :math:`l(I) = \infty`. 
    
    4. If :math:`I = (-\infty, \infty)`, then :math:`l(I) = \infty` 

.. topic:: Definition: Outer Measure

    The outer measure :math:`\lvert A \rvert` of a set :math:`A \subset \mathbb{R}` is defined by,

    .. math::

        \lvert A \rvert = \text{inf}\{ \sum_{k = 1}^{\infty} l(I_k) : I_1, I_2, ... \text{are open intervals such that} A \subset \cup_{k = 1}^{\infty} I_k \}

.. topic:: Definition: Parts

    :math:`\subset` (part-of relation): A binary relation that holds between two individuals when one is a part of the other.

.. topic:: Definition: Disjoint

    :math:`\otimes` (disjoint relation): A binary relation that holds between two individuals when they have no common parts.

.. topic:: Definition Sum 
    
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

.. _zalta-axioms:

Zalta
-----

.. topic:: Definitions

    - Ox: *x is an ordinary individual*
    - Ax: *x is an abstract individual*
    - xF: *x encodes the property F*
    - Fx: *x exemplifies the property F*

.. topic:: Abstract Objects

    1. Ordinary individuals necessarily and always fail to encode properties.

    .. math::

        \forall x: Ox \to \Box \neg \exists F: xF


    2. For every condition on properties, it is necessarily and always the case that there is an abstract individual that encodes just the properties satisfying the condition.

    .. math::

        \forall \phi: \exists x: Ax \land \Box \forall F: (xF \leftrightarrow \phi(F))


    3. Two individuals are identical if and only if they are both ordinary individuals and they necessarily and always exemplify the same properties, or they are both abstract individuals and they necessarily and always encode the same properties.

    .. math::

        \forall x: \forall y: (x =y) \leftrightarrow [ (Ox \land Oy \land \Box \forall F: (Fx \leftrightarrow Fy)) \lor (Ax \land Ay \land \Box \forall F: (xF \leftrightarrow yF))]

    4. If it is possible or sometimes the case that an individual encodes a property, then that individual encodes that property necessarily and always.

    .. math::

        \forall x: \forall F: \Diamond xF \to \Box xF

    5. For every exemplification condition on individuals that does not involve quantification over relations, there is a property which is such that, necessarily and always, all and only the individuals satisfying the condition exemplify it.

    .. math::

        \forall \phi: \exists F: \Box \forall x: Fx \leftrightarrow \phi(x)

    6. Two properties are identical just in case it is necessarily and always the case that they are encoded by the same individuals.

    .. math::

        \forall F: \forall G: (F = G) \leftrightarrow \Box \forall x: (xF \leftrightarrow xG)
