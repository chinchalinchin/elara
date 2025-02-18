.. _zalta:

-----
Zalta
-----

.. _zalta-metaphysics:

Metaphysics of Abstraction
--------------------------

Zalta attempted to partition the objects of a language through those that map to being actual and those that map to being abstract. 

.. topic:: Definition: Predicates 

    - Ox: *x is an ordinary individual*
    - Ax: *x is an abstract individual*
    - xF: *x encodes the property F*
    - Fx: *x exemplifies the property F* 

Ordinary individuals necessarily and always fail to encode properties.

.. math::

    \forall x: Ox \to \Box \neg \exists F: xF


For every condition on properties, it is necessarily and always the case that there is an abstract individual that encodes just the properties satisfying the condition.

.. math::

    \forall \phi: \exists x: Ax \land \Box \forall F: (xF \leftrightarrow \phi(F))


Two individuals are identical if and only if they are both ordinary individuals and they necessarily and always exemplify the same properties, or they are both abstract individuals and they necessarily and always encode the same properties.

.. math::

    \forall x: \forall y: (x =y) \leftrightarrow [ (Ox \land Oy \land \Box \forall F: (Fx \leftrightarrow Fy)) \lor (Ax \land Ay \land \Box \forall F: (xF \leftrightarrow yF))]

If it is possible or sometimes the case that an individual encodes a property, then that individual encodes that property necessarily and always.

.. math::

    \forall x: \forall F: \Diamond xF \to \Box xF


For every exemplification condition on individuals that does not involve quantification over relations, there is a property which is such that, necessarily and always, all and only the individuals satisfying the condition exemplify it.

.. math::

    \forall \phi: \exists F: \Box \forall x: Fx \leftrightarrow \phi(x)

Two properties are identical just in case it is necessarily and always the case that they are encoded by the same individuals.   

.. math::

    \forall F: \forall G: (F = G) \leftrightarrow \Box \forall x: (xF \leftrightarrow xG)
