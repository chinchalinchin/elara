.. _calculator_project_three:

=============
Pi Estimation
=============

.. epigraph::

	This mysterious Pi, which comes in at every door and window, and down every chimney, calling itself the circumference to a unit of diameter.

	-- August De Morgan

TODO

.. _calculator_project_three_instructions:

Instructions
============

1. Read through the :ref:`calculator_project_three_background` section.

2. Read through the :ref:`calculator_project_three_project` section. As you read through this section, follow along on your own calculator. 

3. Read through the :ref:`calculator_project_three_analysis`. As you read through, complete the questions in the :ref:`calculator_project_three_analysis` section in a document. When you completed the :ref:`calculator_project_three_analysis` section, upload the document to the Google Classroom assignment. 

4. On the due date, bring your calculator to class and connect to the ViewSonic. Use the **TIConnect** software to export your simulation for grading. 

.. _calculator_project_three_videos:

Videos
======

Part One
--------

.. image:: https://img.youtube.com/vi/qSR0jIKeMmU/maxresdefault.jpg
	:alt: Estimating Pi With Simulation 1/3
	:target: https://www.youtube.com/watch?v=qSR0jIKeMmU

Part Two
--------

.. image:: https://img.youtube.com/vi/J9ILZhPYds4/maxresdefault.jpg
	:alt: Estimating Pi With Simulation 2/3
	:target: https://www.youtube.com/watch?v=J9ILZhPYds4

Part Three
----------

TODO

.. _calculator_project_three_background:

Background
==========

TI Basic
--------

.. topic:: New Program

	To start a new program on your *TI-84*, type the following,
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`MENU : \text{NEW}`
	
	Title the program ``MONTEPI``.

Control Structures
------------------

A *control structure* is a programmatic construct for controlling the logical flow of a program. This project will require the use of two fundamental control structures: **FOR** loops and **IF-THEN** statements.

.. note::

	**IF-THEN** statements are often called "*conditional statements*"
	
For Loop
********

A **FOR** loop is a programmatic construct for repeating a block of instructions; The *body* of the **FOR** loop is the block of repeating instructions. The arguments provided to a **FOR** loop determine how many times the block of instructions execute. 

.. topic:: For Loop

	While in **PRGM** editor, type
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`\text{MENU} : \text{CTL}`
	- :math:`4 : \text{FOR(}`

	To insert a **FOR** loop into a program.
	
Whenever a control structure is started, it must *always* be accompanied with a corresponding **END** statement. 

.. topic:: End Statement

	While in **PRGM** editor, type
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`\text{MENU} : \text{CTL}`
	- :math:`7 : \text{END}`
	
	To insert an **END** command into a program.

Once a **FOR** has been inserted into a program and closed with an **END**, it must be supplied with appropriate arguments. A **FOR** has *four* arguments,

	FOR(<INDEX>, <START>, <END>, <STEP>)
	
.. important::
	
	The name of each argument is written between angle brackets, ``<>``, but the angle brackets are not part of the syntax. See below for an example. 

1. ``INDEX`` assigns a variable to be used as the *index* of the loop.

2. ``START`` sets the starting value for the index.

3. ``END`` sets the ending value for the index.

4. ``STEP`` sets the increment added to the index at the end of the loop.
 
As an example, the following code block will prompt the user to enter a value for ``N``. Then it use the index ``I`` to iterate  from :math:`I = 1, 2, 3, ..., N` in steps of *1*. For each value of ``I``, it will print that value to screen,

.. code::

	: INPUT "ITERATIONS: ", N
	
	: FOR(I, 1, N, 1)
	
	: DISP I
	
	: END
	
.. note::

	Recall the **DISP** function can be found from the **PRGM** editor,
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`\text{MENU} : \text{I/O}`
	- :math:`3 : \text{DISP}`
	
.. note::

	Recall the **INPUT** function can be found from the **PRGM** editor,
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`\text{MENU} : \text{I/O}`
	- :math:`1 : \text{INPUT}`
	
Conditional Statement
*********************

A conditional statement provides a way of gating certain blocks of code behind a logical condition. Consider the instructions,

	If it rains, take an umbrella. Otherwise, pack a lunch.
	
The *condition* of this proposition is the actual event of rain. If it is raining, then the *condition* has been met and the *operation* of *taking an umbrella* is performed. In the event it does *not* rain, the operation of *taking an umbrella* is replaced with the operation of *packing a lunch*.

An **IF-THEN-ELSE** idiom provides exactly this sort of control structure for programs on **TI** calculators. If a condition is met, a certain operation is performed while if the condition is not met, a different operation is performed.

.. topic:: If Statement

	While in **PRGM** editor, type
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`\text{MENU} : \text{CTL}`
	- :math:`1 : \text{IF}`
	
	To insert an **IF** command into a program.
	
.. topic:: Then Statement

	While in **PRGM** editor, type
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`\text{MENU} : \text{CTL}`
	- :math:`2 : \text{THEN}`
	
	To insert an **THEN** command into a program.
	
.. topic:: Else Statement

	While in **PRGM** editor, type
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`\text{MENU} : \text{CTL}`
	- :math:`3 : \text{ELSE}`
	
	To insert an **ELSE** command into a program.
	
.. topic:: End Statement

	While in **PRGM** editor, type
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`\text{MENU} : \text{CTL}`
	- :math:`7 : \text{END}`
	
	To insert an **END** command into a program.

.. important::

	The **ELSE** command is *optional*. Every conditional statement needs an **IF** and a **THEN**, but the inclusion of **ELSE** is not necessary.
	
The following code block will generate a random number between 0 and 1. If the number is greater than 0.5, it will print ``YAHTZEE`` to screen; otherwise, it will print ``WHOMP WHOMP``. 

.. code::

	: RAND -> A
	: IF A>0.5
	: THEN
	: DISP "YAHTZEE"
	: ELSE
	: DISP "WHOMP WHOMP"
	: END

Graphing
--------

TODO: PT-ON function

.. _calculator_project_three_project:

Project
=======

.. _calculator_project_three_monte_carlo:

Monte Carlo Simulation
----------------------

TODO: walk through it

.. _calculator_project_three_analysis:

Analysis
========
