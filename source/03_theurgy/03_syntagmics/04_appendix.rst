.. _syntagmics-appendix:

Appendix
========

.. _syntagmics-projection:

Projection
----------

The formalization of sestinas requires a method of composing signs through other signs. The operation of *projection* is an attempt to define a composition operation that will serve this purpose. The author recognizes several flaws with the current approach and for that reason has relegated it to the appendix of this work.

---------
Defintion
---------

.. math::

    x \circ y

It is important to clarify that projection is a *sign*. It is an object *within* the syntagmic system (or more specifically, an operation which yields an object). It serves a semantic function within the system. This differents from the metalogical nature of *containment*, which is an expression *about* the system, i.e. a truth value.

.. important::

    The operation of *projection* is a sign. The relation of *containment* is a truth value.

To state "*y projects x*", or symbolically,

.. math::

    x = x \circ y

Can be seen as a form of "*poetic factorization*", akin to an arithmetic relation :math:`9 = 3 \cdot 3`, where one sign is identified as a constituent (or *factor*) of another. The :math:`y` in :math:`x \circ y` will sometimes be referred to as a *factor* of :math:`x`. 

The operation of projection is not commutative,

.. math::

    x \circ y \neq y \circ x 

The sign on the lefthand side :math:`x` of a projection :math:`x \circ y` is the "*larger*" sign that contains the "*smaller*" sign :math:`y` on the righthand side. In other words, logically, if :math:`x` contains :math:`y`,

.. math::
    
    [y \subset_p x] \implies [x \circ y = x]

However, if :math:`x` does not contain :math:`y`, then :math:`x \circ y` is defined to be a caesura, :math:`\varnothing`, i.e. the absence of a syntagmic variable. 

.. math::

    [\neg y \subset_p x] \implies [x \circ y = \varnothing]

For this reason, :math:`x \circ y` can be thought of an indicator variable that returns the first operand if it contains the second operand, and nothing if the first operand does not contain the second operand. 

.. math::

    [[y \subset_p x] \implies [x = x \circ y]] \lor [x \circ y = \varnothing]

In fact, the prior expression can be seen as the *logical definition* of a *factor*. To be more precise, a factor :math:`y` of a fixed :math:`x` is defined as any syntagmic sign that satsifies the open formula given above. 

Projection is logically related to appendment and prependment. Note :math:`y = \text{cat}` prepends :math:`x = \text{cat on a mat}`, where as :math:`z = \text{mat}` appends :math:`x`. Both :math:`z` and :math:`y` project :math:`x`, as well,

.. math::

    x = x \circ y

.. math::

    x = x \circ z

In other words, if a sign prepends or appends another sign, it also projects that sign. Taking the previous two equations and substituting the first into the second, 

.. math::

    x = [x \circ y] \circ z

The brackets are dropped for notationally convenience and it is understood a projection is to be applied starting with the leftmost sign (:math:`y`) and moving right to the next projection operand (:math:`z`).

.. math::

    x = x \circ y \circ z

Importantly, projection does not imply prependment or appendment. For example :math:`t = \text{on}` projects :math:`x`, but it does not prepend or append it. In other words, appendment, prependment and projection are logically related as follows,

.. math::

    x(y) \implies [x \circ y]

And,

.. math::

    (y)x \implies [x \circ y]

Or more succinctly,

.. math::

    [x(y) \lor (y)x] \implies (x \circ y)


.. important::
    
    The converse of this does not hold. 

The "zero" property of projection is given by noting that caesuras cannot contain anything but themselves,

.. math::

    [\varnothing \cdot y] = \varnothing

Which aligns with the definition. In addition, the operation of projection is *idempotent*,

.. math::

    [x \circ y] \circ y = x \circ y

The inner term, :math:`x \circ y` is guaranteed to be a sign that is either empty or contains :math:`y`. If it is empty (caesura), then, as noted, projecting it any number times will always result in a caesura. If it contains :math:`y`, then it will return the very sign that contains :math:`y`, ensuring :math:`[x \cdot y]` is well defined.
