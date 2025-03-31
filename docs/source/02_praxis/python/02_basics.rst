.. _python_basics:

======
Basics 
======

**Python** is made up of *functions* and *variables*. Everything in **Python** is either one or the other. 

.. tip:: 

    As you read through this page, open an :ref:`IDLE shell<python_idle>` and try out the commands yourself.

.. _python_comments:

Comments
========

*Comments* are code that doesn't get interpretted by the **Python** shell. They allow you to annotate your actual program with explanations geared towards an audience that is trying to understand what your program is doing. For example,

.. code:: python 

    # this is a comment, it won't have any effect on this script
    print("this a command, it will be interpretted by Python")

Output:

    this is a command, it will be interpretted by Python 

Any line that starts with a hashtag ``#`` is skipped over by **Python** when it is executing your script. 

Comments should provide clear and precise explanations for the code it is annotating.

.. topic:: Bad Comments

    The following is an example of a bad comment. The code below it is complicated and hard to understand and the comment provides no insight.

.. code:: python

    # this is a bad comment
    numbers = [1 if x %% 5 == 0 else 0 for x in range(100)]

.. topic:: Good Comments

    The following is an example of a good comment. It explains what the code it is attached to is doing and allows the reader to gain insight in your program.

.. code:: python
    
    # this will step through the numbers 1 through 100. Then it will either,
    # add 1 to a list if the number is divisible by 5
    # add 0 to a list if the number is not divisible by 5
    numbers = [1 if x % 5 == 0 else 0 for x in range(100)]

When you create scripts for the projects in this class, be sure to add comments where appropriate, especially if your code is complicated. 

.. _python_docstring:

Docstrings
==========

.. important:: 

    Anytime a lab asks you to answer a question that requires a written response, write your answer in a docstring! *All* of your work should be done in the *py* file.

Comments annotate code. Docstrings annotate scripts. A `docstring <https://peps.python.org/pep-0257/>`_ is a special type of comment that provides a quick summary of everything that is happening in a script. As an example, save the following snippet as a file named *example_docstring.py*,

.. code:: python

    """This is a docstring comment. It explains what the whole script is doing.
    """
    
    # This is a normal comment. It explains what the line below it is doing.
    print("hello world")

Output:

    hello world 

After you save the file, open up a *Linux* terminal and type, 

.. code:: shell

    python3 -m pdoc example_docstring

You will see the docstring content get printed to screen. This allows programmers, such as yourself, to quickly determine what a script is doing without executing the code. 

.. warning:: 

	This command won't work on your computer yet. We need to install some things. 

When you write a docstring for your projects, use the following format,

.. code:: python

    """
    Project <Name>
    ==============
    <Your Name>
    -----------
    Date
    ****

    This is where your preamble will go. Explain what your script does here.

    1. Label each problem in your docstring.
    2. If your problems aren't labelled, you will lose points.
    """
    
    # this is a difficult math problem
    x = 2 + 2
    print(x)

Variables
=========

A variable is a stored piece of data. A variable has a *type* that is determined by the form of the data, called the *data type*. 

Every variable must be *assigned* a value in order to be used. A value assignment occurs when you type an expression of the form,

    x = y

The left hand side, *x*, is the *name* of the variable. The right hand side, *y*, is the *value* of the variable. The order in which the *name* and *value* appear is important: the *name* of the variable always occurs on the left hand side and the *value* of the variable always occurs on the right hand side. The equals sign in between them is the *assignment operator*; it assigns the value of *y* to *x*. 

.. warning:: 
    The assignment operator ``=`` is not *exactly* the same as the equals signs from **Algebra**, but it is similar. With an assignment, we are not *equating* two expressions. Instead, we are *assigning* the value of the right hand side to the left hand side.

.. _python_strings:

Strings
-------

Definition
    Data that represents text are called *strings*. A string is enclosed by double quotes "" or single quotes '',

.. code:: python

    var = "hello world"
    another_var = 'this is a sentence'
    print("these are strings: '", var, "'' & '", another_var, "'")

Output:

    these are strings: 'hello world' & 'this is a sentence'

.. _python_integers:

Integers
--------

Definition
    Data that represents whole numbered quantities are called *integers*.

.. code:: python

    a_number = 5
    another_number = 15
    print("these are integers: ", a_number, ", ", another_number)

Output:

    these are integers: 5, 15

.. _python_floats:

Floats
------

Definition
    Data that represents numerical quantities with decimals are called *floats*. 

.. code:: python

    n = 100.00000001
    m = 25.76
    print("these are floats: ", n, ", ", m)

Output: 

    these are floats: 100.00000001, 25.76

.. _python_tuples:

Tuples
------

Definition
    Tuples are *ordered pairs* of variables. 

.. code:: python

    pair = (1, 2)
    another_pair = ("dog", "cat")
    print("these are tuples: ", pair, ", ", another_pair)

Output:

    these are tuples: (1,2), ('dog', 'cat')

Note the variables in the *tuple* do not have to be numbers.

You can access the *values* in a tuple the same way you access elements of a list, using the index of the value you want and the ``[]`` notation,

.. code:: python 

    pair = ("android", "iphone")

    print("this is the x variable in the ordered pair: ", pair[0])
    print("this is the y variable in the ordered pair: ", pair[1])

Output:

    this is the x variable in the ordered pair: 'android'

    this is the y variable in the ordered pair: 'iphone'
    
.. _python_lists:

Lists 
-----

Definition
    Lists are ordered collections of variables. 
    
.. code:: python 

    example_list = [ "Led Zeppelin", "Pink Floyd", "The Beatles" ]

The *index* of an element in a list is the order that it appears, starting at 0. In other words, the first element in a list is *indexed* at 0, the second element at 1, the third element at 2, ... , the n :sup:`th` element at *n-1*. You can access the value of an element by using ``[]`` brackets and the element's index,

.. code:: python

    print("this is a whole list: ", example_list)
    print("this is the first element of a list: ", example_list[0])
    print("this is the second element of a list: ", example_list[1])
    print("this is the last element of a list: ", example_list[2])
    print("this is also the last element of a list: ", example_list[-1])

Output:

    this is a whole list: ['Led Zeppelin', 'Pink Floyd', 'The Beatles']

    this is the first element of a list: Led Zeppelin

    this is the second element of a list: Pink Floyd

    this is the last element of a list: The Beatles 

    this is also the last element of a list: The Beatles

The variables in a list need not be the same type,

.. code:: python

    unlike_list = [ "red", 5.67, "blue", "green" ]
    print("lists can have different types of elements: ", unlike_list[0], ", ", unlike_list[1])

Output:

    lists can have different types of elements: red, 5.67

You can determine the *length* of a list, i.e. how many elements are in it, using the ``len()`` function,

.. code:: python

    my_list = [ 1, 2, 3, 4, 5, 6, 7 ]
    print("length of list: ", len(my_list))

Output: 

    length of list: 7

Arithmetical Operations
=======================

Most of the arithmetical operations in **Python** are exactly what you would expect them to be. The only operation whose symbol may be surprising is :ref:`python_exponentiation`.

.. _python_addition:

Addition
--------

.. code:: python
    
    7 + 3 

Output:

    10 

.. _python_subtraction:

Subtraction
-----------

.. code:: python
    
    10.45 - 3.2

Output:

    7.249999999999999

.. important:: 

    **Python** uses *floating point arithmetic*. If the output above is surprising, read through the `documentation about floating point arithmetic <https://docs.python.org/3/tutorial/floatingpoint.html>`_ to understand what is going on.

    For this class, it is not necessary to understand *why* this doesn't *exactly* equal ``7.25``; it is only necessary to be aware of this limitation.

.. _python_multiplication:

Multiplication
--------------

.. code:: python
    
    5 * 76

Output:

    380

.. _python_division:

Division 
--------

.. code:: python

    68 / 5

Output

    13.6

.. _python_exponentiation:

Exponentiation
--------------

.. code::

    5 ** 2

Output:

    25

.. _python_logical_operations:

Logical Operations
==================

Equivalence
-----------

The *equivalence* operator is used to test the *truth-value* of expressions. The syntax for using it is,


    <expression A> == <expression B>

.. note:: 

    The angular brackets ``<>`` are **not** part of the code. They tell you where to place your code. In other words, the ``<>`` represent the *grammatical rules* for equivalence.

A simple example is given below,

.. code:: python

    variable = "a sentence"
    true_test = (variable == "a sentence")
    false_test = (variable == 4.5)
    print(true_test)
    print(false_test)

Output:

    True
    
    False 

This example is contrived to illustrate the operator and how it works, but in practice, the *equivalence* operator will be used in conjunction with :ref:`python_list_filtering` to parse data sets. It will also pop up again once we introduce :ref:`python_control_structures`.

.. _python_list_operations:

List Operations
===============

The operations in the previous section dealt with :ref:`python_floats` and :ref:`python_integers`. In other words, the operations in the last section applied to numbers. **Python** has many operations that can be applied specifically to :ref:`python_lists`.

.. _python_list_slicing:

Slicing
-------

Slicing a list is **Python**'s way of breaking a list into a smaller sub-list (an especially useful technique in the domain of statistics!). The general syntax of slicing is given below,

    list[<start index : optional> : <end index : optional>]

.. important:: 

    The angular brackets ``<>`` are not part of the code. They represent the *grammatical* rules for *list slicing*. 

Where ``<end index>`` is always *exclusive*, i.e. is **not** included in the slice. For example, 

.. code:: python

    data = [ "a", "b", "c", "d"]
    sliced_data = data[1:3]
    print(sliced_data)

Output:

    ['b', 'c']

The commands above will print to screen the elements starting at the second index up to, but **not including**, the fourth index. 

.. important:: 

    Remember the first index of a list is 0!

In other words, if you execute the given commands, you will see the list ``['b', 'c']`` print to screen. 

Try to figure out what the next example will print to screen before pasting it into an :ref:`IDLE notebook <python_idle>`,

.. code:: python 

    data = [ "A", "B", "C" , "D"]
    sliced_data = data[0:2]
    print(sliced_data)

.. collapse:: Solution 
    
    Output:

        ['A', 'B']

If you leave out the ``<start index>``, it is understood to be ``0``, 

.. code:: python

    data = [ "dog", "cat", "fish" ]
    sliced_data = data[:2]
    print(sliced_data)

Output:

    [ 'dog', 'cat']

Likewise, if you leave out ``<end index>``, it is understood to be the (last index + 1),

.. code:: python

    data = [ "dog", "cat", "fish", "hamster", "bearded goat"]
    sliced_data = data[1:]
    print(sliced_data)

Output:

    ['cat', 'fish', 'hamster', 'bearded goat']

We can use slicing in conjunction with the ``len()`` function to remove data from the start and end of a data set, 

.. code:: python

    data = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    n = len(data)
    trimmed_data = data[2:n - 2]
    print(trimmed_data)

Output:

    [3, 4, 5, 6, 7, 8]

Special Slicing Techniques
**************************

There is another type of slicing that allows you extract elements from a list according to a rule. First we give the syntax and then go through a few examples,

    list[ <start_index : optional> :: <step : required>]

.. important:: 

    The angular brackets ``<>`` are not part of the code. They represent the *grammatical* rules for *list slicing*. 

This command tells **Python** to look at the ``<start index>`` and then *iterate* through the list in steps of ``<step>``, grabbing each element it lands on along way,        

.. code:: python

    data = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    even_data = data[0::2]
    print(even_data)

Output:

    [0, 2, 4, 6, 8, 10]

If instead we started at a different index,

.. code:: python 

    data = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    odd_data = data[1::2]
    print(odd_data)

Output

    [1, 3, 5, 7, 9]

.. _python_list_comprehension:

Comprehension
-------------

*List comprehension* is a way of applying an algebraic expression to every element in a list. In other words, *list comprehension* allows us to generate a list of data according to a formula. For this reason, *list comprehension* is sometimes called *list generation*. The general syntax is given below, 

    list = [ <expr : required> for <element : required> in <list: requied> ]

.. important:: 

    The angular brackets ``<>`` are not part of the code. They represent the *grammatical* rules for *list comprehension*. 

For example, the following code snippets uses the list ``[1, 2, 3, 4, 5]`` to generate a new list that squares each element of the first list and then prints it to screen,

.. code:: python

    data = [1, 2, 3, 4, 5]
    squared_data = [ x ** 2 for x in data ]
    print(squared_data)

Output:

    [ 1, 4, 9, 16, 25 ]

*List comprehension* is usually used in conjunction with the :ref:`range() built-in function <python_builtin_functions>`. Hop over to that section, take a look at ``range()`` to see more examples.

.. _python_list_filtering:

Filtering
*********

Suppose you had the a dataset that represented a group of men and women's average height, where each observation in the sample is an ordered pair :math:`(x, y)`
with *x* corresponding the gender of the individual and *y* corresponding to their height measured in feet,

.. math:: 

    S = \{ (m, 5.9), (m, 5.75), (f, 5.6), (f, 5.8), (m, 6.3), (f, 5.7), (m, 6.0), (f, 5.3) \}

In **Python**, you could store this sample in a list with the following code snippet, 


.. code:: python

    data = [ ('m', 5.9), ('m', 5.75), ('f', 5.6), ('f', 5.8), ('m', 6.3), ('f', 5.7), ('m', 6.0), ('f', 5.3) ]

Often we will need to *group* the data by category. For example, in this data set, we might like to look at the average height of *males only* versus the average of *females only*. You can achieve this result with a tecnique known as *filtering*. *Filtering* consists of applying a condition to each member of the list to determine whether it should be included or not. 

The syntax for filtering is given by,

    list = [ <expr : required> for <element : required> in <list : required> if <condition : required> ]

Applying this idea to the dataset above, we can create a list that contains only male heights and a list that contains only female height as follows,

.. code:: python

    male_heights = [ obs[1] for obs in data if obs[0] == 'm' ]
    female_heights = [ obs[1] for obs in data if obs[0] == 'f' ]

    print(male_heights)
    print(female_heights)

Output:

    [5.9, 5.75, 6.3, 6.0]

    [5.6, 5.8, 5.7, 5.3]

*Filtering* is very useful when you are *cleaning data* for analysis. Data is not usually in a format ready for analysis. You will often need to perform some preparatory steps to get the data ready. As this example illustrates, *filtering* is often (but not always!) the exact tool we need to do this. 

References
==========
- `docstrings <https://peps.python.org/pep-0257/>`_
