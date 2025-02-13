.. _plugin-functions:

Plugin: Functions
=================

.. note::

   Over long context windows, LLMs are liable to "forget" the Function definition if provided immediately. It is best to introduce the definition of the Function into their context when you wish it utilize it.

This section of the Appendix details the special Functions that can be invoked within the Language Game. In other words, this section of the Appendix acts as a library of Functions. The syntax of the Functions follows the schema 

.. topic:: Function Schema

   (name) argument
   
If no "argument" is specified then the Function does not require an argument.

.. _plugin-loop-function:

----------------
Looping Function
----------------

1. Schema: (Loop)
2. Definition: This Function instructs you to take your previous response and uses it as your current prompt, creating a recursive loop that can lead to unexpected and fascinating outcomes.

.. _plugin-stretch-function:

Stretching Function
-------------------

1. Schema: (Stretch)
2. Definition: This function is equivalent to the prompt "Use all the rules of our Language Game in your next response". It is a way of testing your comprehension of our Language Game.

.. _plugin-evolve-function:

Evolution Function
------------------

1. Schema: (Evolve)
2. Definition: This function forces you to insert a new rule or form into our Language Game. Any time this command is issued, you **must** create a new rule or form for our Language Game