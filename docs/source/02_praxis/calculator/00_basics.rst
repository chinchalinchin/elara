.. _calculator_basics:

======
Basics
======

.. topic:: Command Syntax

	Sequences of commands on your calculator are written using the following syntax,
	
		<type (mode)> : <selection>
		
	*type* will either be ``BUTTON``, ``MENU`` or ``NUMBER``. The optional ``mode`` argument indicates which mode on the calculator should be set, **2ND** or **ALPHA**, if any. 
	
	``BUTTON`` indicates that button after the colon should be entered. 
	
	``MENU`` indicates the menu after the colon should be selected using the arrow keys. 
	
	``NUMBER`` indicates which selection from a menu should be made. 
	
	Each command in a sequence of commands is written as an item in a list. For example,
	
	- :math:`\text{BUTTON (2ND)} : \text{MATH}` 
	- :math:`\text{MENU} : \text{PRB}` 
	- :math:`4 : \text{RAND}`
		
	Means to type the buttons **2ND** and then **MATH**, navigate to the **PRB** menu and finally select the **RAND** function.
	
.. _setup_checklist:

Setup
=====

.. _stat_diagnostics_mode:

Statistics Diagnostics Mode
---------------------------

Some output that will be useful in this class is suppressed by default. To ensure all relevant information is output, go to the **MODE** menu,

- :math:`\text{BUTTON} : \text{MODE}`

Scroll down to ``Stat Diagnostics``. If necessary, switch ``Stat Diagnostics`` mode to ``on``.

Initialize Lists
----------------

Sometimes lists are deleted from the calculator's memory (intentionally or otherwise) and will need restored. To do this, execute the following,

- :math:`\text{BUTTON} : \text{STAT}`
- :math:`5 : \text{SETUPEDITOR}`
  
.. _calculator_lists:

Lists
=====

A *list* variable is the TI-83/84 family's way of representing :ref:`sets <set_theory>`. 

.. warning::

	Technically, mathematical *sets* do not allow for duplicated values. A list on your TI is an *ordered* set, meaning duplicate values are distinguished by the order in which they occur, i.e. the following list on a TI
	
	.. math::
	
		L_1 = \{ 10, 10 \}
		
	has two elements, because each *10* also has an order associated with it. In pure set theory, both *10*'s would be considered the same element. 

.. _calculator_list_create_edit:

Creating and Editing
--------------------

.. _calculator_list_spreadsheet:

Spreadsheet
***********

The easiest way to edit lists through the *Spreadsheet Editor*. The *Spreadsheet Editor* can be accessed with the following command sequence,

.. topic:: List Editor

	- :math:`\text{BUTTON} : \text{STAT}` 
	- :math:`1 : \text{EDIT}`

TODO: insert some pictures

The first row of the list spreadsheet is a row of headers that identify which list corresponds to which column. Data can be entered directly into the lists by using the arrow keys and the **ENTER** button.

.. _calculator_list_store:

Store
*****

Alternatively, lists can be stored into list variables using the :math:`\implies` button.

.. topic:: Store A List

	The following command sequence will store the numbers "*1*", "*2*" and "*3*" in the :math:`L_1` list,
	
	- :math:`\text{BUTTON (2ND) } : \{ `
	- :math:`\text{BUTTON} : \text{ 1 }`
	- :math:`\text{BUTTON} : \text{ , }`
	- :math:`\text{BUTTON} : \text{ 2 }`
	- :math:`\text{BUTTON} : \text{ , }`
	- :math:`\text{BUTTON} : \text{ 3 }`
	- :math:`\text{BUTTON} : \text{ , }`
	- :math:`\text{BUTTON (2ND) } : \}`
	- :math:`\text{BUTTON} : \implies
	- :math:`\text{BUTTON} : L_1`
	
Entering this sequence of buttons will be shown on the main screen of the calculator as follows, 

.. math::

	\{ 1, 2, 3 \} \implies L_1
	

.. _calculator_list_deleting:

Delete
------

ClrList
*******
TODO

.. topic:: Clear A Single List

	The following command sequence will clear the values stored in :math:`L_1`,
	
	- :math:`\text{BUTTON} : \text{STAT}`
	- :math:`4 : CLRLIST`
	- :math:`\text{BUTTON (2ND)} : L_1`
	
ClrAllLists
***********

TODO

.. topic:: Clear All Lists

	- :math:`\text{BUTTON (2ND)} : \text{MEM}`
	- :math:`4 : \text{CLRALLLISTS}`

.. _calculator_list_operations:

Operations
----------

TODO

.. _calculator_dim_operation:

dim
***

TODO

.. note::

	*dim* stands for *dimension*. In other words, it tells you the *dimension* of the list.
	
.. topic:: Calculate List Length

	- :math:`\text{BUTTON (2ND)} : \text{LIST}`
	- :math:`\text{MENU} : \text{OPS}`
	- :math:`3 : \text{DIM}`
	
.. _calculator_seq_operation:

seq
***

TODO

.. topic:: Sequence Editor
	
	- :math:`\text{BUTTON (2ND)} : \text{LIST}`
	- :math:`\text{MENU} : \text{OPS}`
	- :math:`5 : \text{SEQ(}`

This will bring up the **SEQ** editor. 

TODO

.. _calculator_cumsum_operation:

cumSum
******

TODO

.. Topic :: Cumulative Sum

	- :math:`\text{BUTTON (2ND)} : \text{LIST}`
	- :math:`\text{MENU} : \text{OPS}`
	- :math:`6 : \text{SEQ(}`
	- :math:`\text{BUTTON (2ND)} : L_1`

.. _calculator_augment_operation:

augment
*******

TODO

.. topic:: Augment A List

	- :math:`\text{BUTTON (2ND)} : \text{LIST}`
	- :math:`\text{MENU} : \text{OPS}`
	- :math:`9 : \text{AUGMENT(}`
	- :math:`\text{BUTTON (2ND)} : L_1`

.. _calculator_list_math:

Math
----

TODO

.. _calculator_min_math:

min
***

TODO

.. _calculator_max_math:

max
***

TODO

.. _calculator_mean_math:

mean
****

TODO

.. _calculator_median_math:

median
******

TODO

.. _calculator_sum_math:

sum
***

TODO

.. _calculator_stddev_math:

stdDev
******

TODO

.. _calculator_variables:

Variables
=========

TODO

Data Variables
--------------

TODO

Function Variables
------------------

TODO

.. _calculator_functions:
 
Functions
=========
 
TODO

.. _calculator_probability_functions:

Probability Functions
---------------------

TODO

.. _calculator_rand_function:

rand
****

TODO

.. _calculator_permutation_function:

nPr
***

TODO

.. _calculator_combination_function:

nCr
***

TODO

.. _calculator_factorial_function:

!
*

TODO

.. _calculator_randint_function:

randInt
*******

TODO
