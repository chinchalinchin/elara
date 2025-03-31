.. _project_one:

==========
Bar Charts 
==========

.. epigraph::

	The picture is a model of reality.

	-- Ludwig Wittgenstein

In this lab, you will get familiar with the statistical plotting features of **Python** using a dataset we have already seen. We will explore the association between two categorical variables and determine if a relationship exists.

.. _project_one_instructions:

Instructions
============

1. Download the ``.csv`` dataset in the :ref:`project_one_dataset` section and place it in the ``Linux Files`` folder on your ChromeBook's file system where you save your ``.py`` scripts.
2. Create a Python ``.py`` script named ``NAME_project_one.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``NAME`` with your name.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_one_installs` section. (We will do this part in class!)
5. Read the :ref:`project_one_background` section.
6. Read the :ref:`project_one_loading_data` section. (We will do this part in class!)
7. Read the :ref:`project_one_bar_charts` section. Download the script files in that section onto your ChromeBook. Read through them carefully and execute them on your computer. 
8. Read the :ref:`project_one_set_operations` section. 
9. Load in the data from the ``.csv`` file using the technique outlined in the :ref:`project_three_loading_data` section. (We will do this part in class!)
10. Perform all exercises and answer all questions in the :ref:`project_one_project` section. Label your script with comments as indicated in the *Project* section.
11. Keep in mind, there is a section dedicated to :ref:`python_plotting` underneath the :ref:`References > Python > Plotting <python_reference>` on the left-hand menu of the site.
12. When you are done, zip your script **and** your *csv* file into a file named ``NAME_project_one.zip``
13. Upload the zip file to the Google Classroom Project One Assignment.

.. _project_one_installs:

Prerequisites
=============

.. note::

    We will do this in class together.

We installed **Python** in :ref:`our first project <project_zero>` and got familiar with some of its basic functionality, in particular :ref:`list variables <python_lists>` and the :ref:`operations that can be performed on them <python_list_operations>`, skills that will be helpful in completing this project. 

We also discovered our ChromeBook's **Python** installation is a bit different than a typical installation; it's missing a few essential pieces that we will now install. In order to go further with **Python** in this class, we need to do the following.

Open up a *Linux* terminal and type the command,

.. code:: shell

	sudo apt-get install python3-pip
	
This command will install the **Python Package Manager** onto your computer. The **Python Package Manager**, or ``pip`` for short, allows us to install **Python** extensions. And that is exactly what we are going to do. Once the previous command completes, verify the installation with,

.. code:: shell

	pip3 --version
	
You should see something along the lines of,

    pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
  
Your version may not match exactly. You should be fine as long as your **Python** version is above *3.7*. 

Now that ``pip`` is installed, let's plug in the final pieces we need into our **Python** installation.
 
`matplotlib <https://matplotlib.org/>`_ will be used to generate graphical representations of data. `tkinter <https://docs.python.org/3/library/tkinter.html>`_ will be used to render the output of `matplotlib <https://matplotlib.org/>`_ into JPEG and PNG images. These packages can be installed through the command line. 

Type the following command into your *Linux* terminal,

.. code:: shell

    pip3 install matplotlib tk

.. image:: ../../../assets/imgs/python/matplotlib_tk_install_done.png
    :align: center 

Output:

    Defaulting to user installation because normal site-packages is not writeable

    Collecting tk
        Downloading tk-0.1.0-py3-none-any.whl (3.9 kB)
    
    ...

    Installing collected packages: tk

    Successfully installed tk-0.1.0

.. image:: ../../../assets/imgs/python/matplotlib_tk_install_done.png
    :align: center 

You should see the packages download and install into your system.

That's it! You are ready to plot some sweet statistical graphs.

.. _project_one_background:

Background
==========

Electric Vehicles in Washington State 
-------------------------------------

Recall the dataset we used in :ref:`#1 From the Classwork <graphical_representations_of_data_classwork>`,

    The United States Government General Services Administration maintains a huge database of public available information. One of the datasets they publish is the `Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing <https://catalog.data.gov/dataset/electric-vehicle-population-data>`_

This dataset was taken from `data.gov <https://data.gov/>`_. This is an excellent resource, if you ever find yourself in need of some data. We will be using this online database quite a bit once we get fully up to speed on **Python**.

We examined the *electric vehicle* dataset a little bit in class on the first week. We are now prepared to do a little more in-depth analysis. 

First, let's take a look at some of the variables being observed in this dataset.

Make
****

The **Make** variable represents the manufacturer of the car. The possible values for this variable are listed below,

- FIAT
- MINI
- LEXUS
- CHRYSLER
- LINCOLN
- ALFA ROMEO
- RIVIAN
- TOYOTA
- AZURE DYNAMICS
- GENESIS
- VOLKSWAGEN
- JEEP
- PORSCHE
- MERCEDES-BENZ
- CADILLAC
- KIA
- JAGUAR
- POLESTAR
- FISKER
- FORD
- TESLA
- SMART
- HYUNDAI
- BENTLEY
- NISSAN
- MITSUBISHI
- TH!NK
- VOLVO
- LUCID
- CHEVROLET
- WHEEGO ELECTRIC CARS
- HONDA
- LAND ROVER
- SUBARU
- AUDI
- MAZDA
- BMW
  
Clean Alternative Fuel Vehicle (CAFV) Eligibility
*************************************************

`The state of Washington offers many incentives for vehicle owners to invest in an electric vehicle <https://www.dol.wa.gov/vehicles-and-boats/taxes-fuel-tax-and-other-fees/tax-exemptions-alternative-fuel-vehicles-and-plug-hybrids>`_,

    In 2019, Washington State reinstated the sales and use tax exemption for the sales of vehicles powered by a clean alternative fuel and certain plug-in hybrids.

However, not all cars are eligible for this tax exemption. The exemption depends on the battery range of the electric vehicle. If your electric vehicle does not have a large enough range, your vehicle is deemed ineligible for a tax exemption.

The **Clean Alternative Fuel Vehicle (CAFV) Eligibility** variable in this dataset records whether or not an individual car is eligible. The possible values of this variable are:

- Not eligible due to low battery range
- Eligibility unknown as battery range has not been researched
- Clean Alternative Fuel Vehicle Eligible

Electric Vehicle Type
*********************

Electric vehicles come in two varieties: vehicles that are fully electric and hybrid vehicles that revert to a gasoline engine when they run out of electric power. This `article from PC Magazine goes into greater detail about the differences between these two types of electric vehicles <https://www.pcmag.com/how-to/ev-vs-hev-vs-phev-what-are-the-types-of-electric-vehicles>`_

The **Electric Vehicle Type** variable records what *type* of electric vehicle was registered with Washington State. The possible values of this variable are:

- Battery Electric Vehicle (BEV)
- Plug-in Hybrid Electric Vehicle (PHEV)

*BEV* electric vehicles are *fully electric*. *PHEV* use hybrid engines; when *PHEV* engines run out of power, they start using gasoline.

.. _project_one_bar_charts:

Bar Charts
==========

.. important::

    Refer to :ref:`python_plotting` section for a more in-depth look at the various features of :ref:`matplotlib`, the library we are using to create graphs.

.. _project_one_standard_bar_charts:

No Frills
---------

Recall a standard bar chart is a way of visually representing the marginal frequency distribution for a sample of categorical data,

.. math::

	P(A) = \frac{n(A)}{n(S)}
	
	
Up until now we have been living in the stone age, creating these graphs by hand. Welcome to the twenty-first century. Behold, the power of `matplotlib <https://matplotlib.org/>`_,

.. plot:: assets/plots/other/bar_chart.py

Click on the ``Source Code`` button in the top left corner of the graph to download the *.py* script used to generate this graph. Examine the source code contained therein for generating a *Bar Chart* with :ref:`matplotlib <python_plotting>`. Be sure to read the comments before you execute it, as you will need to tweak a setting to get it to run on your computer. 

The key line to pay attention to in this script is the following,

.. code:: python

    axes.bar(relative_freq.keys(), relative_freq.values(), color="lightblue", ec="red", width=0.5)

The `bar() <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html>`_ function is :ref:`matplotlib`'s *bar chart* graphing function. 

The first argument of the ``bar()`` function is the values of the categorical variable you wish to plot. The second argument is the frequencies of each of the values. The *order* of each list that is passed in must be the same. For example, if we have a sample of data,

.. math::

    S = \{ A, A, A, A, A, B, B, B, B, B, B, B \}

We would graph its *frequency* distribution using the following code,

.. code:: python

    import matplotlib.pyplot as plot 

    (fig, axes) = plot.subplots()

    values = [ "A", "B"]
    frequencies = [ 5, 7 ]

    axes.bar(values, frequencies, color="lightblue", ec="red", width=0.5)

    axes.set_xlabel("Categories")
    axes.set_ylabel("Frequency")

    plot.show()

This code will create a bar chart with two values of a categorical variable on the ``x`` axis, ``A`` and ``B``. It will plot their respective frequencies, ``5`` and ``7``, on the y-axis.

The two arguments, ``color`` and ``ec``, affect the *styling* of the bar chart. ``color`` determines the fill color of the bars and ``ec`` determines the outline color.

.. note:: 

    ``ec`` stands for "*edge color*"

The full list of colors available to use in :ref:`matplotlib` is detailed in the following chart,

.. image:: ../../assets/imgs/python/matplotlib_colors.png
    :align: center

Any value in this chart can be used an argument for ``color`` or ``ec``.

This script is annotated with lots of comments for you to read. Give them a peak, and then let's meet over in the next section.

.. _project_one_stacked_bar_charts:

Stacked
-------

Recall a *stacked bar chart* is a way of visually representing a *conditional distribution* of one categorical variable with respect to another,

.. math::

	P(A \mid B) = \frac{n(A \cap B)}{n(B)}
	
.. plot:: assets/plots/other/stacked_bar_chart.py

This one is extremely tricky, so read through it carefully. 

.. note::

    We are performing the same calculations in this script that we performed in class on Thursday, September 7 :sup:`th` with the simulated distribution of shapes and colors. You should have your calculations saved in a file named ``stacked_bar_chart.py`` in your ``Linux Files`` folder on your ChromeBook.

`matplotlib <https://matplotlib.org/>`_ does not have a nice way of making stacked bar charts; Unforunately, the twenty-first century isn't all it's cracked up to be. In this timeline, you have to "stack" your bar charts yourself. Make sure to download this one and go through it step by step. The script has been well commented; every step has been detailed. 

.. hint::
	
	Your script comments should look like the ones in the scripts you just downloaded.

The key lines to pay attention to in this script are the follwoing,

.. code:: python

    # Stack Conditional Distribution of Shape Given Red
    axs.bar("RED", percent_of_red_that_are_balls, color="yellow", ec="blue", width=0.5, label="BALL")
    # add the previous percent to the `bottom` to stack
    axs.bar("RED", percent_of_red_that_are_ducks, bottom=percent_of_red_that_are_balls, color="lightgreen", ec="blue", width=0.5,  label="DUCK")

    # Stack Conditional Distribution of Shape Given Blue
    # NOTE: don't label this group, or else you'll get two legends
    axs.bar("BLUE", percent_of_blue_that_are_balls, color="yellow", ec="blue", width=0.5)
    # add the previous percent to the `bottom` to stack
    axs.bar("BLUE", percent_of_blue_that_are_ducks,  bottom=percent_of_blue_that_are_balls, color="lightgreen", ec="blue", width=0.5,)

We have to *manually* stack the bars on top of each category and then add the previous percentage to the ``bottom`` of the next bar. Note for ``RED``, we are passing in additional argument of ``bottom`` in the second line; this tells :ref:`matplotlib` to start the next bar at that height. Similarly for ``BLUE``.

.. _project_one_set_operations:
	
Set Operations
==============

A set in **Python** is defined with a pair of curly brackets ``{ }``. 

.. code:: python

	emperors = { "Augustus", "Commodus", "Nero", "Hadrian" }
	
A :ref:`set variable <python_sets>` in **Python** is a special type of variable.  When you create a set, it won't distinguish between identical elements. In other words, *sets* do not allow duplicates. As an example,

.. code:: python

	set_of_dupes = { "a", "a", "b", "b" }
	
	print(set_of_dupes)
	
Output:

	{'a', 'b'}
	
Notice the repetitions of *a* and *b* are ignored. This property of *sets* is extremely useful for categorical data.

Suppose you have a list of categorical data such as,

.. code:: python

	some_list = [ "A", "A", "B", "C", "D", "D", "D" ]
	
Suppose, further, you didn't know how many values the categorical variable took on. In this particular case, it's easy to see what the values are just by looking at the list (i.e. ``A``, ``B``, ``C`` and ``D``), but in real world datasets, you could have *thousands of individual observations* to sort through to determine exactly how many values a categorical variable can assume. 

Rather than trying to determine what the *distinct* values are by hand, let **Python** do the hard work for you by converting the *list* into a *set*,

.. code:: python
	
	set(some_list)
	
Output:

	{'A', 'B', 'C', 'D'}

.. _project_one_project:

Project
=======

No Frills 
---------

1. Calculate the relative frequency of the following **Makes** of *Electric Vehicles*,

- TESLA
- CHEVROLET
- NISSAN
- TOYOTA
- VOLKSWAGEN

Label your calculations with comments.

2. Using your answers to #1, construct a bar chart for *only* these five values of the **Make** categorical variable. Label the commands used to render the graph with comments.

3. In the :ref:`python_docstring` at the top of your script, answer the following questions.

a. Out of these five values, what is the most frequent **Make** of *Electric Vehicle* in Washington State?

4. Find the *joint frequency distribution* of **Make** and **Electric Vehicle Type** for the same **Makes** as in *#1* and *#2*. In other words, fill out the following table,


+-------------+---------------------------------+-----------------------------------------+
|             | Battery Electric Vehicle (BEV)  |  Plug-in Hybrid Electric Vehicle (PHEV) |
+-------------+---------------------------------+-----------------------------------------+
|  TESLA      |             ?                   |                    ?                    |
+-------------+---------------------------------+-----------------------------------------+
| CHEVROLET   |             ?                   |                    ?                    |
+-------------+---------------------------------+-----------------------------------------+
|   NISSAN    |             ?                   |                    ?                    |
+-------------+---------------------------------+-----------------------------------------+
|   TOYOTA    |             ?                   |                    ?                    |
+-------------+---------------------------------+-----------------------------------------+
|  VOLKSWAGEN |             ?                   |                    ?                    |
+-------------+---------------------------------+-----------------------------------------+

a. Which manufacturers produce more *Battery Electric Vehicles (BEV)* than *Plug-in Hybrid Eletric Vehicles (PHEV)*? In other words, what does the *conditional distribution* for the **Electric Vehicle Type** given the **Make** tell you about the manufacturers of *electric vehicles*? Which manufacturers are more likely to produce fully electric cars versus hybrid cars and visa versa?

b. Which manufacturers produce more *Battery Electric Vehicles (BEV)* than their competitors? Which manufacturers produce more *Plug-in Hybrid Electric Vehicles (PHEV)* than their competitors? In other words, what does the *conditional distribution* for the **Make** given the **Electric Vehicle Type** tell you about the market for electric cars in Washington state?

	
Stacked
-------

1. Before starting this part of project, answer the following in a :ref:`python_docstring`: Based on the information provided in the :ref:`project_one_background` section, how would you expect the *conditional distribution* of **Clean Alternative Fuel Vehicle (CAFV) Eligibility** given the **Electric Vehicle Type** to look? Do you expect fully electric vehicles to have greater eligibility for tax credits than hybrid vehicles? Why or why not?
   
2. Answer the following questions. Label any commands you use to solve the problem with comments. Write your answers in the :ref:`python_docstring` at the top of the script.

a. What percentage of *electric vehicles* in Washington State are "*Not eligible due to low battery range*" for the **Clean Alternative Fuel (CAFV) Eligibility** tax exemption?
 
b. What percentage of *electric vehicles* in Washington State are *Battery Electric Vehicles (BEV)*? 

c. What percentage of *electric vehicles* in Washington State are *Plug-in Hybrid Electric Vehicle (PHEV)*? 

d. What percentage of *electric vehicles* in Washington State are both *Battery Electric Vehicles (BEV)* and "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility** tax exemption?

e. What percentage of *electric vehicles* in Washington State are both *Plug-in Hybrid Electric Vehicle (PHEV)* and "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility** tax exemption?

f. What percentage of *Battery Electric Vehicles (BEV)* are "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility** tax exemption?

d. What percentage of *Plug-in Hybrid Electric Vehicle (PHEV)* are "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility** tax exemption?

e. What percentage of "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility** vehicles are *Battery Electric Vehicles (BEV)*?

e. What percentage of "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility** vehicles are *Plug-in Hybrid Electric Vehicle (PHEV)*?

3. Using this information obtained in *#3* and any additional information required, create a stacked bar chart for the *conditional distribution* of the **Electric Vehicle Type** given the **Clean Alternative Fuel Vehicle (CAFV) Eligibility**.

4. What does your stacked bar chart from #3 tell you about the *association* between the **Clean Alternative Fuel Vehicle (CAFV) Eligibility** and the **Electric Vehicle Type**? Write your answer in your script's :ref:`python_docstring` and label the problem.

5. Write a few sentences explaining the results from #2 - #4. Did the result turn out the way you expected? Why or why not?

6. Based on your answer to #4 in this section and #4 from the previous section, which manufacturers in Washington state benefit the most from the tax exemption? What does this tell you about the manufacturer with the *most* electric vehicles registered in Washington state?

.. _project_one_dataset:

Datasets
========

.. _project_one_loading_data:

Loading Data
------------

The following code snippet will load in a *CSV* spreadsheet named ``example.csv``, parse it into a list and then print it to screen, assuming that *CSV* file is saved in the same folder as your script. Modify this code snippet to fit the datasets in this lab and then use it to load in the provided datasets in :ref:`project_one_dataset` section.

.. code-block:: python 

    import csv

    # read in data
    with open('example.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        raw_data = [ row for row in csv_reader ]

    # separate headers from data
    headers = raw_data[0]
    columns = raw_data[1:]

    # grab first column from csv file
    column_1 = [ row[0] for row in columns ]

    print(column_1)

.. note::

    We will do this part in class together. 

Electric Vehicle Dataset 
------------------------

You can download the full dataset :download:`here <../../assets/datasets/electric_vehicle_population_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Electric Vehicles in Washington State
   :file: ../../../assets/datasets/previews/electric_vehicle_population_data_preview.csv

The meaning of the columns was discussed in more detail in :ref:`project_one_background`. Refer to that section for further information on this dataset.

References
==========

- `matplotlib bar charts <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html>`_
- `matplotlib colors <https://matplotlib.org/stable/gallery/color/named_colors.html>`_
- `python dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
- `python string templating <https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals>`_
