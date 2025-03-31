.. _python_sets:

====
Sets
====

.. _python_set_variables:

Set Variables
=============

A set is an *unordered* collection of variables. By *unordered* it is meant a set that contains *a* and *b* is considered the same as a set that contains *b* and *a*. 

A set is defined in **Python** using the familiar :math:`\{ \}` :ref:`list_notation`,

.. code:: python

    pets = { "dog", "cat", "fish", "hamster", "snake" }

    four_legs = { "dog", "cat", "hamster" }

    swims = { "dog", "fish", "snake" }

    warm_blooded = { "dog", "cat", "hamster" }

    poets = { "byron", "shakespeare", "eliot" }

The examples on this page will refer to the above sets.

.. _python_set_operations: 

Set Operations
==============

.. note:: 
    Before executing these commands, try working them out by hand first and see if your work agrees!

.. _python_set_cardinality:

Cardinality
-----------

The :ref:`cardinality` of a set is found by calculating its :ref:`length <python_builtin_functions>`,

.. code:: python 

    total_pets = len(pets)
    print(total_pets)

.. collapse:: Cardinality Solution
        
    Output:

        5

.. _python_set_union:

Union
-----

The :ref:`union` of two sets is found by,

.. code:: python

    pets_or_poets = pets.union(poets)
    print(pets_or_poets)

.. collapse:: Union Solution 

    Output:

        {'snake', 'byron', 'shakespeare', 'eliot', 'fish', 'cat', 'dog', 'hamster'}

.. important:: 
    
    Take note: *set operations* do **not** preserve the order of the sets. In technical terms, *sets* are not *indexed*. Notice the *order* of the set in the output is *random*. 

.. _python_set_intersection:

Intersection
------------

The :ref:`intersection` of two sets is found by,

.. code:: python 

    four_legs_and_swims = four_legs.intersect(swims)
    print(four_legs_and_swims)

.. collapse:: Intersection Solution

    Output:

        {'dog'}

.. _python_set_difference:

Difference
----------

The :ref:`set_difference` of two sets is found by,

.. code:: python

    swims_but_not_warmblooded = swims - warm_blooded
    print(swims_but_not_warmblooded)

.. collapse:: Difference Solution 

    Output:

        {'snake'}