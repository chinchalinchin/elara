------------
Inverse Time
------------

Local Time Inversion
--------------------

Let :math:`dt_2 = - dt_1`. 

Let :math:`t_1 \in [\tau_1^i, \tau_1^f]` and :math:`t_1 \in [\tau_2^i, \tau_2^f]`.

Let :math:`a \, \mid \, b` stand for "*trajectory a relative to frame of reference b*".

Note that :math:`dt_2 = - dt_1` implies :math:`t_1 + t_2 = K` for some constants :math:`K`.

Let an event be measured in two coordinate systems, :math:`(x_1, t_1)` and :math:`(x_2, t_2)`. In the :math:`(x_1, t_1)` coordinate system, let the trajectory of the event be given by :math:`x = f(t_1)` for :math:`t_1 \in [\tau_1^i, \tau_1^f]`. From calculus,

.. math::

    x \mid x_1 = \int_{\tau_1^i}^{\tau_1^f} f'(t_1) \cdot dt_1

In the :math:`(x_2, t_2)` coordinate system, because :math:`dt_2 = - dt_1`. 

.. math::

    x \mid x_2 = - \int_{\tau_1^i}^{\tau_1^f} f'(t_1) \cdot dt_2

.. math::

    x \mid x_2 = \int_{\tau_1^f}^{\tau_1^i} f'(t_1) \cdot dt_2

:math:`dt_2 = - dt_1` implies :math:`\tau_2^f - \tau_2^i = -(\tau_1^f - \tau_1^i) = \tau_1^i - tau_1^f`, so,

.. math::

    \tau_2^f = \tau_1^i

.. math::

    \tau_2^i = \tau_1^f

And,

.. math::

    x \mid x_2 = \int_{\tau_2^i}^{\tau_2^f} f'(t_1) \cdot dt_2

For :math:`t_1`, again the relation, :math:`dt_2 = - dt_1` implies :math:`\tau_2^f - \tau_2^i = -(\tau_1^f - \tau_1^i)`