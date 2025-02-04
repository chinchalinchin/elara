.. _latex-preamble:

LaTeX
=====

LaTeX will be wrapped in either a ``:math:`` role or nested into a ``.. math::`` directive. For example, the LaTeX equation of a parabola will be written inline as :math:`f(x) =x ^2` or within a nested block as,

.. math::

    f(x) = x^2

Preamble
--------

All LaTeX embedded in this document was written using the following preamble,

.. raw:: latex

    {{ latex.preamble  | replace('\n', '\n    ')}}