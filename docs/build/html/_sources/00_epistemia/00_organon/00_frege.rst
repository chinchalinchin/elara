.. _frege:

-----
Frege
-----

.. _frege-grundgesetze:

Grundgesetze der Arithmetik
---------------------------

.. topic:: Law I

    TODO

.. topic:: Law II

    TODO

.. topic:: Law III: Identity of Indiscernibles 

    If two objects have the same properties, they are the same object. 

    .. math::

        \forall a, b: (a = b) \equiv (\forall f: f(a) \equiv f(b))

.. topic:: Law IV

    TODO

.. _frege-law-v:

.. topic:: Law V: Extensionality

    .. math::

        (\hat{\epsilon}f = \hat{\epsilon}g) \equiv (\forall x: f(x) \equiv g(x))

.. _frege-definitions:

Definitions
-----------

.. _frege-converse:

.. topic:: Definition: Converse

    .. math::

        \text{Conv}_{\alpha\epsilon}(R\alpha\epsilon)(x, y) \equiv Ryx

TODO 

.. _frege-function:

.. topic:: Definition: Function

    .. math::
    
        \text{Func}_{\alpha\epsilon}(R\alpha\epsilon) \equiv \forall x,y: (Rxy \implies \forall z: (Rxz \implies y = z))

TODO 

.. _frege-mapping:

.. topic:: Definition: Mapping 
    
    .. math::

        \text{Map}_{\alpha\epsilon\xi\eta}(R\alpha\epsilon)(F\xi, G\eta) \equiv \text{Func}_{\alpha\epsilon}(R\alpha\epsilon) \land \forall x: (Fx \implies \exists y: (Rxy \land Gy))

TODO 

.. _frege-predecession:

.. topic:: Definition: Predecession 

    .. math::

        Pmn \equiv \exists F, x: (Fx \land (n = Nz :Fz) \land (m =  Nz: (Fz \land z \neq x)))


.. _frege-zero:

.. topic:: Definition: Zero 

    .. math::

        0 \equiv Nx: x \neq x

.. topic:: Definition: Hume's Principle

    The Number belonging to the concept F is identical with the Number belonging to the concept G if the concept F is equinumerous with the concept G.

    .. math::

        (Nx: Fx = Nx: Gx) \equiv \exists R: (Map(R)(F,G) \land Map(Conv(R))(G, F))

TODO 