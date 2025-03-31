.. _project_zero:

======
Python
======

.. epigraph:: 

	What I cannot create, I do not understand.   

	-- Richard Feynman

In this lab, you will install **Python** and learn some of its basic functions. The goal is to get familiar with using **Python**.

Instructions
============

1. Create a Python ``.py`` script named ``LASTNAME_FIRSTNAME_project_zero.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``LASTNAME`` and ``FIRSTNAME`` with your last and first name, respectively.
2. Create a :ref:`Python docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
3. Perform all exercises and answer all questions in the :ref:`project_zero_project` section. Label your script with comments as indicated in the instructions of each problem.
4. When you are done, zip your folder and all its contents in a file named ``LASTNAME_FIRSTNAME_project_zero.zip``
5. Upload the zip file to the Google Classroom Project Zero assignment.

.. _project_zero_background:

Background
==========

Like windmills and Heineken, **Python** is a product of the Netherlands. It was invented in the 1980s by Guido van Rossum, an engineer at **Microsoft**. Technically, **Python** is a language `specification <https://docs.python.org/3/reference/index.html>`_, a set of grammatical rules and syntax. Any program that *implements* this specification is considered "**Python**". The actual implementation details vary depending on which **Python** `engine you are running <https://www.jython.org/jython-old-sites/archive/21/docs/differences.html>`_. Popular implementations of **Python** have been written in **Java** and **C**. However, these are details we will never need to know. We are *using* **Python** as an already built tool, not *studying* **Python** in order to understand how it was built. 

**Python** is a very popular tool. Google `python AND data science <https://www.google.com/search?q=python+in+data+science>`_ and you will get a half billion results. 

.. tip:: 
    
    The upper-case "AND" in the search suggestion is a `Google search operator <https://ahrefs.com/blog/google-advanced-search-operators/>`_. Learn how to Google effectively and it will save a ton of time!

In the last decade, **Python** has become the go-to tool for conducting data analysis. There is a reason for this: **Python** is easy to learn and easy to use. You don't need any prior programming experience (although a few math classes help!), so you can focus on the problems you are actually solving rather than learning syntax. 

`Python has excellent documentation <https://docs.python.org/3/tutorial/index.html>`_. If you are ever in doubt (or just want to know more), try using the search bar on the documentation to find an answer:

.. image:: ../../../assets/imgs/context/python_doc_search.png

In addition, you can refer to the :ref:`python_reference` section on this web site, where you will find some resources dedicated to the topics in this class.

.. _project_zero_project:

Project
=======

1. Head over to the :ref:`python_setup` page and prepare your ChromeBook for Python.

2. Read through the :ref:`python_basics` and the :ref:`python_functions` pages. Try the examples on your ChromeBook as you read through these pages. Use them as a reference to complete the exercises that follow.

3. Add the required ``import`` statements from :ref:`project_zero_imports` to the top of your *py* script. 

4. Take the *Natural Numbers* dataset from the :ref:`project_zero_dataset` section and add it to your *py* script. Perform the following operations. Be sure to add :ref:`python_comments` where appriopriate.

    a. Using :ref:`python_list_slicing` and the ``natural_numbers`` list, create a list of all the *even* numbers between 1 and 100. Save the code in your script and label it with a comment ``# 4a``. 

    b. Using :ref:`python_list_slicing` and the ``natural numbers`` list, create a list of all the *odd* numbers between 1 and 100. Save the code in your script and label it with a comment ``# 4b``.

    c. Using :ref:`python_list_comprehension` and the ``natural numbers`` list, a create a list of the first 100 *squares*. Recall a sequence of *n* square numbers is given by :math:`1, 4, 9, 16, ..., n^2`. Save the code in your script and lavel it with a comment ``# 4c``.

    d. Using :ref:`python_list_comprehension` and the ``natural numbers`` list, a create a list that represents the first 100 values of the function :math:`f(n) = \frac{1}{n}`, where ``n`` must be a natural number.

5. Take the *Random Numbers* dataset from the :ref:`project_zero_dataset` section and add it to your *py* script. Perform the following operations. Be sure to add :ref:`python_comments` where appropriate,

a. Using :ref:`python_list_slicing`, break this list into two even lists of 5000 random numbers each. Save the code in your script and label it with a comment ``# 5a``.

b. Using :ref:`python_builtin_functions`, calculate the sum of each of the lists you found in *part a*. Save the code in your script and label it with a comment ``# 5b``. Before executing your code, answer the following questions and include each answer in the :ref:`docstring <python_docstring>`.

    i. How do you expect the sums to be compare? Will they be equal or unequal? Will be they be close together or far apart? Why? Justify your answer.

    ii. Calculate the difference between both sums, i.e. if ``n`` is the variable that contains the sum of your first list and ``m`` is the variable that contains the sum of your second list, find the value of ``n - m``. Should this value be positive, negative or zero?  

    iii. Re-execute your code. Did you do it? Go ahead and do it again, just to be safe. Alright, are you done? Do it one more time, but this time do it with *feeling*. Do you get the same results each time? How do the results compare? Explain.

    iv. If you performed this experiment a 100 times, what do you expect the difference of the sum of these lists to be on average?

6. Now it's your turn to generate some data. Using the :ref:`python_choice_function` and the techniques studied so far, generate a list of data that represents the experiment of asking 100 randomly selected people whether they prefer Mayor McCheese, The Hamburglar, Grimace or Ronald McDonald as McDonald's mascot. Save the code in your script and lavel it with a comment ``# 6a``.
   
.. _project_zero_imports:

Imports
=======

To complete this lab, you will need to import the ``random`` package. Add the following line to the *top* of your *py* script **underneath** your :ref:`docstring <python_docstring>`,

.. code:: python

    import random

.. _project_zero_dataset:

Datasets
========

Natural Numbers
---------------

Copy and paste the following :ref:`list variable <python_lists>` into your *py* script to generate the natural numbers *1* to *100*,

.. code:: python

    natural_numbers = [ x for x in range(100) ]

Random Numbers
--------------

Copy and paste the following :ref:`list variable <python_lists>` into your *py* script to generate 10000 random numbers.

.. code:: python

    random_numbers = [ random.random() for _ in range(10000) ]

References
==========

- `Python Documentation <https://docs.python.org/3/>`_
- `Python Tutorial <https://docs.python.org/3/tutorial/index.html>`_
