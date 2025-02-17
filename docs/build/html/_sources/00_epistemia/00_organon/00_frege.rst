.. _frege:

-----
Frege
-----

.. _humes-principle:


Hume's Principle
----------------

TODO

.. _fregean-definition-of-zero:

Zero as the Cardinality of Contradiction
----------------------------------------

.. math::

    A = \{ x \mid x \neq x \} 

.. math::

    n(A) = 0 

.. _fregean-definition-of-one:

One as the Cardinality of Zero
------------------------------

.. math::
    
    B = \{ y \mid y = n(A) \}

.. math::
    
    n(B) = 1

.. _frege-five-laws:

Frege's Five Laws
-----------------

.. topic:: Law I

    TODO

.. topic:: Law II

    TODO

.. topic:: Law III: The Identity of Indiscernibles 

    If two objects have the same properties, they are the same object. 

    .. math::

        \forall a, b: (a = b) \equiv (\forall f: f(a) \equiv f(b))

.. topic:: Law IV

    TODO

.. _frege-law-v:

.. topic:: Law V: Extensionality

    .. math::

        (\hat{\epsilon}f = \hat{\epsilon}g) \equiv (\forall x: f(x) \equiv g(x))