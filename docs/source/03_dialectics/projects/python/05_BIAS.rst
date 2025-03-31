.. _project_five:

====
Bias
====

.. epigraph::
	There's something happening here, but what it is ain't exactly clear.

	-- Buffalo Springfield

In this lab, you will perform some graphical analysis on a famously biased data set and use statistical reasoning to draw conclusions about the method of observation used to generate the data.

Instructions
============

1. Download the *csv* dataset in the :ref:`project_five_dataset` section and place it in the ``Linux Files`` folder on your folder system where you save your ``.py`` scripts.
2. Create a Python ``.py`` script named ``NAME_project_five.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``NAME`` with your name.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_five_background` section.
5. Read the :ref:`project_five_loading_data` section.
6. Load in the data from the ``.csv`` file using the technique outlined in the :ref:`project_five_loading_data` section.
7. Perform all exercises and answer all questions in the :ref:`project_five_project` section. Label your script with comments as indicated in the instructions of each problem.
8. When you are done, zip your script **and** the *csv* file in a zip file named ``NAME_project_five.zip``
9. Upload the zip file to the Google Classroom Project Three Assignment.

.. _project_five_background:

Background
==========

`In the years 1969, 1970, 1971 and 1972, the Selective Service System in the United States held a draft lottery by order of President Lyndon B. Johnson for men born between the dates of January 1, 1944 and December 31, 1950 <https://en.wikipedia.org/wiki/Draft_lottery_(1969)>`_. 

Individuals born between these dates were to be selected at random and drafted into military service to fight in the Vietnam War.

Method of Selection
-------------------

The method used to select individuals for service is highly controversial. Many argued it was not truly random and unfairly selected certain groups of individuals over others. In this project we are going to investigate these claims and see if there is any statistical evidence to suggest they are true.

To do this, we will need to understand how draftees were selected. 

In an attempt to randomize the selection, the Selective Service System held a draft lottery. 365 days of the year were printed on sheets of paper and placed in a shoebox,

    { January 1, January 2, ... , Feburary 1, February 2, ... , December 30, December 31 }

Slips of paper were then selected at random and anyone of eligible age who had a birthday on the date indicated would be drafted. The important point is *individuals who shared the same birthday* would be drafted at the same time. As example, two men who had the birthdays April 5 :sup:`th`, 1946 and April 5 :sup:`th`, 1947 would both be drafted in the event the slip of paper *"April 5"* was selected.

.. _project_five_python:

Python
======

Loops
-----

Loops are a :ref:`control structure <python_control_structures>` that allow us to organize the flow a program. We have actually encountered loops many times already. We are using loops whenever we write,

.. code:: python:

	data = [ (0,1), (1,2), (2,3), (3,4) ]
	x_var = [ obs[0] for obs in data ]
	print(x_var)
	
Output:

	[ 0, 1, 2, 3 ]
	
:ref:`python_list_comprehension` is a specialized type of loop; a *list generator* like the one above uses a ``for`` loop to iterate over a dataset and apply a formula to each observation. This is one of **Python**'s many idiomatic expressions (TODO: link to idiomatic), a eccentricity unique to **Python** (i.e. you will not find novel expresions like this in other languages, except maybe Javascript, but Javascript is a dumpster fire). **Python** has a lot grammatical tricks like this that make it easy to condense a lot of logic into a single, understandable line.

In reality, the *list generator* in the above expression is really shorthand for following ``for`` loop,

.. code:: python:

	data = [ (0,1), (1,2), (2,3), (3,4) ]
	x_var = [ ]
	for obs in data:
		x_var.append(obs[0])
	print(x_var)
	
Output:

	[ 0, 1, 2, 3 ]
	

Enumeration
-----------

In **Python**, we have been dealing with lists of data, such as,

.. code:: python

	some_data = [ "Rory", "Lydia", "Sophia", "Rachael", "Sejal" ]
	
It is often useful (as it will be in this lab) to get the index of each observation *programmatically* (as opposed to finding it manually by counting up the observations). The ``enumerate()`` gives us a way of accessing the index of an element in a list as we loop over it.

.. code:: python

	some_data = [ "Rory", "Lydia", "Sophia", "Rachael", "Sejal" ]
	
	for index, obs in enumerate(some_data):
		print("#", index, " : ", obs)
		
Output:

	#0 : Rory
	#1 : Lydia
	#2 : Sophia
	#3 : Rachael
	#4 : Sejal
	
.. topic:: Easter Egg
	 
	 Add the following line underneath the ``print`` statement in the code snippet above for a fun Easter Egg!
	 
  .. code:: python
  
	if index != 4:
		print("\t Yay!")
	else:
		print("\t Boo!")
	 	
The ``enumerate()`` function allows us to *step* over each element of a list and grab the index while we do it.
 
.. _project_five_project:

Project
=======

1. Discuss the following questions. Save your answer in the :ref:`docstring <python_docstring>`
   
    a. Is the selection method used for the draft random? Why or why not?
    
    b. If the selection method used for the draft were truly random, what shape would you expect a frequency distribution of the sample to have? 
    
    c. Given the information provided on the selection method, what shape do you expect a frequency distribution of the sample to have?
    
    d. What are some possible sources of bias in the draft lottery? List the cases and identify the *type* of bias in each case.

2. During the first year of the draft, 1969, birthdates were put into the shoebox in descending order of month. In other words, the birth dates in the month of December were first put in the bottom of the shoebox, then birth dates in November were placed on top of the December birth dates, then October birth dates were placed on top of the November birth dates, and so on up to January. The slips of paper were not mixed any further before the draft was selected. Using this new information, answer the following questions. Save your answer in the :ref:`docstring <python_docstring>`

    a. How does this information affect your answer to *#1a*? 

    b. How does this information affect your answer to *#1c*?

    c. How does this information affect your answer to *#1d*?

This selection method was later revised in 1970, 1971 and 1972, once the distribution of data was examined in more detail.

3. Using the birth month of the drafted individual as the classes (the horizontal axis), construct histograms for the years 1969, 1970, 1971 and 1972. 

.. note::

	Read the :ref:`project_five_datasets` section carefully. You will need to clean the data before you are able to construct the histograms properly.

4. Based on the histograms constructed, describe the distribution for each year's draft lottery. Address each of the following points in your answer. Save your answers in the :ref:`docstring <python_docstring>`. 
   
   a. Compare and contrast the distributions of data for each year of the draft. Include descriptions of the location, variation, shape and any possible outliers. 
   
   b. What is the mode of the birth month for each year? 
   
   c. What can we conclude about the relative likelihood of a male with a birthday in January being drafted versus a male with a birthday in December being drafted for the year of 1969? Does this same result appear to hold for 1970, 1971 and 1972?
   
5. Discuss the results. Was the draft lottery fair? If not, why not? If so, why? Justify your answer with sample statistics.

.. _project_five_dataset:

Dataset
=======

.. _project_five_loading_data:

Loading Data
------------

The following code snippet will load in a *CSV* spreadsheet named ``example.csv``, parse it into a list and then print it to screen, assuming that *CSV* file is saved in the same folder as your script. Modify this code snippet to fit the datasets in this lab and then use it to load in the provided datasets in :ref:`project_two_dataset` section.

.. code-block:: python 

    import csv

    # read in data
    with open('example.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        raw_data = [ row for row in csv_reader ]

    # separate headers from data
    headers = raw_data[0]
    columns = raw_data[1:]

    # grab first column from csv file and ensure it's a number (not a string)
    column_1 = [ float(row[0]) for row in columns ]

    print(column_1)

Vietnam Draft Lottery Data
--------------------------

You can download the full dataset :download:`here <../../assets/datasets/vietnam_draft_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Vietnam Draft Lottery Data
   :file: ../../../assets/datasets/previews/vietnam_draft_data_preview.csv

The meaning of the columns is as follows.

*M* represents the birth month of the draftee,
    
    M = 1, 2, 3, ... , 11, 12

*D* represents the birth day of the draftee,

    D = 1, 2, 3, ... , 30, 31 

And *N69*, *N70*, *N71* and *N72* represent the number of individuals selected with a given birth date in the years 1969, 1970, 1971 and 1972, respectively.

Cleaning the Data Set
---------------------

The *experimental unit* in this lab is a date. Each entry in the datasets corresponds to a particular birthdate, i.e. a month and day. For example, the first row of the dataset looks like,

| M | D | N69 | N70 | N71 | N72 |
| 1 | 1 | 305 | 133 | 207 | 150 |
| 1 | 2 | 159 | 195 | 225 | 328 |

The lab is asking to group the data into monthly classes so the sample can be visualized with 12 classes on a histogram. Since we are only interested in *birth months*, we may ignore the **D** column. That leaves us with our class data broken up across multiple rows of the list. We will need to manually group the data to calculate the total number of draftees per month.  

In other words, we will need to step (*iterate*) over the dataset and look at each row. As we do so, we will need to check if the first column **M** is 1, 2, 3, ..., 11 or 12. Then, based on the value of the first column **M**, we will grab the entries from the ``N69``, ``N70``, ``N71`` and ``N72`` columns and add them to the corresponding monthly totals. 

To re-iterate, to *clean the data*, we will need to perform the following steps:
    
    1.  create a list, named ``data_1969``, of twelve *0*'s, ``[0, 0, 0, ... , 0, 0]``, one for each month.
    
    2.  step through ``column_1`` with the ``row_number``.
    
    3.  grab the corresponding entry of the third column, ``column_3[row_number]``
    
    4.  add the value of the third column to the list entry in ``data_1969`` that represents that month. 

The following code snippet implements this algorithm, assuming you have the **M** column stored in ``column_1`` and the ``N69`` column stored in ``column_3``. Use this logic in the lab to clean your data,

.. code:: python 

    data_1969 = [ 0 ] * 12

    for row_number, entry in enumerate(column_1):
        data_1969[int(entry) - 1] += column_3[row_number]
