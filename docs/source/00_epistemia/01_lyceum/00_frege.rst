.. _frege:

-----
Frege
-----

.. epigraph::

    Dear colleague, 
    
    For a year and a half, I have been acquainted with your *The Foundations of Arithmetic*, but it is only now that I have been able to find the time for the thorough study I intended to make of your work. I find myself in complete agreement with you in all essentials, particularly when you reject any psychological element in logic and when you place a high value upon an ideography for the foundations of mathematics and of formal logic, which, incidentally, I find in your work discussions, distinctions, and definitions that one seeks in vain in the works of other logicians. Especially so far as function is concerned, I have been led on my own to views that are the same even in the details. There is just one point where I have encountered a difficulty. You state that a function, too, can act as the indeterminate element. This I formerly believed, but now this view seems doubtful to me because of the following contradiction. Let *w* be the predicate: to be a predicate that cannot be predicated of itself. Can *w* be predicated of itself? From each answer, its opposite follows. Therefore, we must conclude that *w* is not a predicate. Likewise there is no class (as a totality) of those classes which, each taken as a totality, do not belong to themselves. From this I conclude that under certain circumstances a definable collection does not form a totality.

    -- *Correspondence with Gottlob Frege*, Bertrand Russell
    
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