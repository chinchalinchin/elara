.. _carnap:

------
Carnap
------

.. _carnaps-method:

Carnap's Method of Tautology
----------------------------

A common problem in formal logic is determining whether a given proposition is a tautology, i.e. true in all possible cases. Since the number of rows in a truth table grows exponentially with the number of propositions, the traditional method of truth tables is computationally expensive. In `Introduction to Symbolic Logic <https://archive.org/details/rudolf-carnap-introduction-to-symbolic-logic-and-its-applications>`_, Carnap presents a different method for evaluating whether or not a given proposition is a tautology. Rather than enumerating all possible cases and checking if each one is true, it suffices to show the assignment of false to a proposition is impossible. In other words, Carnap's method starts by assuming the proposition is false and then works backwards through the logical connectives to see whether or not an assignment of false is consistent with the proposition.

For example, consider the well-known property of implications,

.. math::

    ((p \implies r) \land (q \implies r)) \implies ((p \land q) \implies r) 

To determine whether this constitues a tautology, it must be shown whether or not an assignment of false can be made to the entire proposition. The proposition is built out of nested propositions. The assignment of false to entire proposition will in turn require the subformulas of the proposition to assume particular values. This will yield conditions for evaluating whether the overall assignment is consistent with the assignment of its components. The top-level connective is,

.. math::

    s \implies t 

Where :math:`s = (p \implies r) \land (q \implies r)` and :math:`t = ((p \land q) \implies r)`. 

In order for this implication to be false, the hypothesis, :math:`s`, must be true, while the consequence, :math:`t`, must be false. 

The assignment of false to :math:`t` in turn requires :math:`p \land q` to be true and :math:`r` to be false.

The assignment of true to :math:`p \land q` in turn requires :math:`p` be true and :math:`q` be true. 

Thus, it is seen in order for the proposition itself to be false, :math:`p` and :math:`q` must be true, while :math:`r` is false. 

These values, however, are inconsistent with the hypothesis, :math:`s`, which was required to be true, for :math:`p \implies r` and :math:`q \implies r` are both false under this assignment, and thus their conjunction is false. This contradicts our initial assumption that :math:`s` is true. Therefore, the entire proposition cannot be false for any assignment and it must be concluded the entire proposition is true for all possible values of :math:`p`, :math:`q` and :math:`r`.

.. math::

    \forall p, q, r: ((p \implies r) \land (q \implies r)) \implies ((p \land q) \implies r)