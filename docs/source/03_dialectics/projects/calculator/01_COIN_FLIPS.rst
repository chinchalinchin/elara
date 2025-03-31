.. _calculator_project_two:

==========
Simulation
==========

.. epigraph::

	Your mind makes it real.

	-- Morpheus, The Matrix


In this project, a program is created on a *TI-83/84/85* calculator that simulates flipping a fixed amount of coins. The user will be able to adjust the probability of a getting heads or tails, in order to simulate fair and unfair conditions. The simulation will be performed a prescribed amount of times. These three values will be the parameters of the simulation,

	1. **n**: Number of coins flips 
	2. **p**: Probability of a single successful coin flip
	3. **m**: Number of simulations

"*Successful*" is here defined to mean "*getting an outcome of heads*". 

The output of the program will be a sampling distribution for the number of heads obtained when flipping a coin *n* times. The sampling distribution will have *m* data points.

.. _calculator_project_two_instructions:

Instructions
============

1. Read through the :ref:`calculator_project_two_background` section.

2. Read through the :ref:`calculator_project_two_project` section. As you read through this section, follow along on your own calculator. 

3. Read through the :ref:`calculator_project_two_analysis`. As you read through, complete the questions in the :ref:`calculator_project_two_analysis` section in a document. When you completed the :ref:`calculator_project_two_analysis` section, upload the document to the Google Classroom assignment. 

4. On the due date, bring your calculator to class and connect to the ViewSonic. Use the **TIConnect** software to export your simulation for grading. 
	
.. _calculator_project_two_background:
	
Background
==========

Augment
-------

AUGMENT is a list operation that takes a list as input and produces a new list as output. Execute the command,

.. math::

	\{ 1, 2, 3 \} \rightarrow L_1
	
In other words, store the list ﻿:math:`\{ 1, 2, 3 `\} in :math:`L_1`. 

That's a nice list and all, but it needs more...list!  So, let's say, you want to add 4 to the end of this list. In order to do this on your calculator without creating an entirely new list, you have to use AUGMENT. 

.. topic:: Augment
	
	- :math:`\text{BUTTON} : \text{LIST}`
	- :math:`\text{MENU} : \text{OPS}`
	- :math:`9 : \text{AUGMENT(}`


Execute the following command,

.. math::

	\text{augment}(L_1, \{ 4 \}) \rightarrow L_1

With AUGMENT, we have told our calculators to take the current list stored in ﻿:math:`L_1`, merge it with the list ﻿:math:`\{ 4 \}` and then store the result back in ﻿:math:`L_1`
﻿
This will be useful in what follows! This function will be integral in the simulation created in this project. 

TI Basic
--------

In a previous project, we introduced `TI Basic <http://tibasicdev.wikidot.com/home>`_ and used it to write a relatively simple program for our *TI-84s* to calculate the :ref:`correlation` of two variables. 

.. topic:: New Program

	To start a new program on your *TI-84*, type the following,
	
	- :math:`\text{BUTTON} : \text{PRGM}`
	- :math:`MENU : \text{NEW}`
	
	Title the program ``COINSIM``.

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

TODO

.. _calculator_project_two_analysis:

Analysis
========

Logical Structure
-----------------

TODO

.. topic:: Question #1

	Explains what happens when the COINSIM program is executed in its current form.
	
TODO

.. topic:: Question #2

	Explains what happens when the COINSIM program is executed in its current form.
	
TODO

.. topic:: Question #3

	Explains what happens when the COINSIM program is executed in its current form.
	
Simulation
----------

TODO

.. topic:: Question #4

	Explains what happens when the COINSIM program is executed in its current form.
	
TODO

.. topic:: Question #5

	Explains what happens when the COINSIM program is executed in its current form.
	
TODO

Sampling Distributions
----------------------

TODO

.. topic:: Question #6

	Write a few sentences describing the simulated sampling distribution. What value is the distribution centered around? What shape does the distribution have?

TODO

.. topic:: Question #7
	
	Fix **m** = 5 and **p**=0.5. Run the simulation with **n** = 10, 30, 50 and 100. How does changing the number of trials (*coin flips*) affect the sampling distribution for the number of heads? What happens to the center of the distribution? What happens to the variability?

TODO

.. topic:: Question #8
	
	Fix **n** = 30 and **p**=0.5. Run the simulation with **m** = 5, 10, 20 and 50. How does changing the number of simulations affect the sampling distribution for the number of heads? What happens to the center of the distribution? What happens to the variability?
	
TODO

.. topic:: Question #9
	
	Fix **n** = 30 and **m**=5. Run the simulation with **p** = 0.1, 0.25, 0.75 and 0.9. How does changing the probability of success affect the sampling distribution for the number of heads? What happens to the center of the distribution? What happens to the variability?
	
TODO

.. topic:: Question #10
	
	Summarize the results. How do the three parameters, **n**, **m** and **p**, affect the sampling distribution for the number of heads in a fixed number of coin flips?
