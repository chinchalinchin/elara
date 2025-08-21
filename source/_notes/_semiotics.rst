.. _semiotics:

---------
Semiotics
---------

.. _measure-theory:

Measure Theory
--------------

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

.. _mereology:

Mereology
---------

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