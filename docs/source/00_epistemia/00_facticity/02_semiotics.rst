.. _semiotics:

---------
Semiotics
---------

Measure
-------

.. topic:: Length of Open Interval

    The length :math:`l(I)` of an open interval :math:`I` is defined by,

    1. If :math:`I = (a,b)` for some :math:`a, b \in \mathbb{R}` with :math:`a < b`, then :math:`l(I) = b - a` 
    
    2. If :math:`I = \emptyset`, then :math:`l(I) = 0`.
    
    3. If :math:`I = (-\infty, a)` or :math:`I = (a, \infty)`,for some :math:`a \in \mathbb{R}`, then :math:`l(I) = \infty`. 
    
    4. If :math:`I = (-\infty, \infty)`, then :math:`l(I) = \infty` 

.. topic:: Outer Measure

    The outer measure :math:`\lvert A \rvert` of a set :math:`A \subset \mathbb{R}` is defined by,

    .. math::

        \lvert A \rvert = inf\{ \sum_{k = 1}^{\infty} l(I_k) : I_1, I_2, ... \text{are open intervals such that} A \subset \cup_{k = 1}^{\infty} I_k} 