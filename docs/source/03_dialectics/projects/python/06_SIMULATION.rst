.. _project_six:

==========
Simulation
==========

.. epigraph:: 
	Your mind makes it real.

	-- Morpheus, The Matrix

*Simulation* is a way of modelling random real-world processes. The idea relies on interpretting the results of random number generation as outcomes in an experiment. We have encountered this idea a few times in class already, but now that we have the concepts of probability in our catalogue of knowledge, we are ready to study simulation in detail.

**Python** has all the tools necessary to simulate experiments that would otherwise be tedious to perform. In this lab, we will explore a few techniques for conducting *simulations* to model the outcomes of random processes.

Instructions
============

1. Create a Python ``.py`` script named ``LASTNAME_FIRSTNAME_project_six.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``LASTNAME`` and ``FIRSTNAME`` with your last and first name, respectively.

2. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.

3. Read the :ref:`project_six_background` section.

4. Perform all exercises and answer all questions in the :ref:`project_six_project` section. Label your script with comments where appropriate.

5. When you are done, zip your script in a zip file named ``LASTNAME_FIRSTNAME_project_six.zip``

6. Upload the zip file to the Google Classroom Project Six Assignment.

.. _project_six_background:

Background
==========

Loops
-----

Loops are essential to the concept of *simulation*. A loop is a programmatic construct for repeating a block of instructions. As with many things in computer science and mathematics, this is easier to see than to say. Consider the following example,

.. code:: python

	for pet in ["cat", "dog", "hippopotamus"]:
		print(pet)
		
Output:

	cat
	
	dog
	
	hippopotamus

.. note::

	The ``pet`` variable is a *local* variable. It only exists within the ``for`` loop block. If you try to reference ``pet`` outside of the ``for`` loop, you will get an **Undefined** error.
	
This snippet of code uses a *for-loop* to iterate over the list containing the elements, ``dog``, ``cat`` and ``hippopotamus``. Each time it iterates over the list, it stores the current element in the ``pet`` variable. The body of the loop then uses the ``pet`` variable and prints it to screen. Each element of the list is output to screen; this is because the loop passes each element of the list to the ``pet`` variable and then executes the code in the body of the loop with that value of ``pet``.  Once there are no more elements in the list, the loop halts.

``for`` loops can be used in conjunction with the ``range()`` function to iterate over sequences of integers starting at 0,

.. code:: python

	for i in range(5):
		print(i)

Output:

	0
	
	1
	
	2
	
	3
	
	4
	
Note the output in the preceding example starts at 0 and ends at 4. The ``range()`` function iterates over all the natural numbers from 0 up to, but not including, the value inputted into the function.  

Loops can be chained together to form *nested* loops,

.. code:: python

	for pet in ["dog", "cat"]:
		for owner in ["rory", "sophia", "sejal", "rachael", "lydia"]:
		
			print(owner, " has a ", pet)

Output:

	rory  has a  dog
	
	sophia  has a  dog
	
	sejal  has a  dog
	
	rachael  has a  dog
	
	lydia  has a  dog
	
	rory  has a  cat
	
	sophia  has a  cat
	
	sejal  has a  cat
	
	rachael  has a  cat
	
	lydia  has a  cat
	
The order of operations in a *nested* loop is important! For each iteration of the *outer* loop (the one iterating over pets), the *inner* loop (the one iterating over owners) is executed in its entirety.

Law of Large Numbers
--------------------

Definition
**********

Consider the experiment of flipping a fair coin ten times. We intuitively understand that, if the coin is truly fair, we should get an approximately even amount of heads and tails. However, the chances of getting exactly five heads and exactly five tails in one sequence of ten coin flips is small. Since each flip of the coin is :ref:`independent <independence>` of the previous coin flip, the fact we get a head on the first flip in no way influences the probability of getting a head on the second flip. The second coin flip has no responsibility to come out as tails if the first flip was heads.

The *Law of Large Numbers* gives a tool for understanding this result. First, we take the experiment of flipping a fair coin ten times and perform this experiment itself a large number of times, let us say 100 times. For each experiment of ten coin flips, we count the number of heads and the number of tails. If we then take the result of each repetition of the experiment and average them all together, the average value will be close to the true population value of five heads. The more times we repeat the experiment, i.e. the more samples we create to pool into the average value, the closer and closer the overall average becomes. In the limit, as the number of repetitions becomes infinite, the average value of the experiment equals its true value. In other words, if we replicate our experiment enough times, the average result will approximate its true population value. In this case, we should observe, after a large number of repetitions, the approximate proportion of heads to be 50% and the approximate proportion of tails to be 50%.

Python
******

Using the :ref:`python_control_structures` introduced in the preceding section and a few :ref:`python_builtin_functions` we have used in previous projects, we can simulate the outcomes of random experiments and see the *Law of Large Numbers* in action. 

The key idea is using random numbers to represent observations drawn from a given population. If we think of a random number between 0 and 1 as an observation, i.e. an outcome in an experiment, then we can use the random numbers to model the distribution of the experiment. 

For example, let the event of getting a random number less than 0.5 correspond to the event of getting heads in a coin flip. Let the event of getting number between 0.5 and 1 correspond to the event of getting a tail. Then, by simulating random numbers between 0 and 1 and interpretting the results as outcomes of flipping a coin, we can derive a probability distribution for the experiment of flipping a coin any number of times.

The following code snippet simulates flipping a fair coin 10 times and stores the simulation in a list. It then takes the simulated distribution and displays a histogram to the user,

.. code:: python

	import random
	import matplotlib.pyplot as mpl

	# simulation parameters
	no_simulations = 100
	no_coins = 10
	coin_prob = 0.5
	# simulation results
	head_dist = []

	# simulation loop
	for i in range(no_simulations):
	    	# resetting simulation variables
		sim_heads = 0
		
		# start simulation
		for j in range(no_coins):
		
			# simulating a single coin flip
			flip = random.random()

			# checking if simulated outcome = heads
			if flip >= coin_prob:
				sim_heads += 1 
				
		# end simulation
				
		print("simulation #", i)
		print("\t number of heads: ", sim_heads)
		
		head_dist.append(sim_heads)
	
	# create histogram of heads distribution
	## manually create bins to prevent weird histogram classes
	bins = [ i + 1 for i in range(no_coins) ]
	(fig, axes) = mpl.subplots()
	axes.hist(head_dist, bins, ec="red",color="lightblue")
	axes.set_xlabel("Number of Heads")
	axes.set_ylabel("Frequency")
	mpl.show()

.. _project_six_project:

Project
=======

1. Consider the experiment of flipping 10 fair coins. Using the techniques described in the :ref:`project_six_background` section, simulate flipping 10 coins. Perform the simulation 200 times. 

	a. Calculate the mean and standard deviation of the simulated sampling distribution. In the :ref:`docstring <python_docstring>`, write a sentence or two interpretting the meaning of these sample statistics in the context of the sampling distributions.

	b. Plot the results using a histogram. Label the axes appropriately. Ensure the histogram class limits are set to 0, 1, 2, ..., 9, 10.

	.. hint:: 

		Use the ``bins`` argument on the ``hist()`` function to change the class limits! Refer to :ref:`project_two` for more information on changing the histogram class limits!

	c. In the :ref:`docstring <python_docstring>`, describe the simulated distribution in a few sentences. What value is the distribution centered around? What type of shape does the distribution have? Of what theorem in statistics is this an example?

	d. In the :ref:`docstring <python_docstring>`, answer the following question: What would happen to the distribution if you increased the number of coins being flipped? What features mentioned in *part c* would change? What features would stay the same?

	.. hint::

		Test it out yourself by changing the number of coins in your code!

	e. In the :ref:`docstring <python_docstring>`, answer the following question: What would happen to the shape of the distribution if you increased the number of simulations being performed? What features mentioned in *part c* would change? What features would stay the same?
	    
	.. hint::

		Test it out yourself by changing the number of simulations in your code!

	f. In the :ref:`docstring <python_docstring>`, answer the following question: What would happen to the shape of the distribution if you flipped an *unfair* coin, i.e. what would happen if you changed the probability of getting a head? What features mentioned in *part c* would change? What features would stay the same?

	.. hint::

		Test it out yourself by changing the probability of getting heads in your code!

	g. In the :ref:`docstring <python_docstring>`, answer the following question: Based on the results of your simulation, what is the probability of observing 9 or more heads in a series of 10 coin flips?

2. Approximately 2% of the world's population has blonde hair. Consider the experiment of selecting 30 people at random from the world's population and recording the number of people in the sample with blonde hair. Using the techniques described in the :ref:`project_six_background` section, simulate the hair color of a sample of 30 people. Perform the simulation 500 times.

	a. Calculate the mean and standard deviation of the simulated sampling distribution. In the :ref:`docstring <python_docstring>`, write a sentence or two interpretting the meaning of these sample statistics in the context of the sampling distributions.

	b. Plot the results using a histogram. Label the axes appropriately. Ensure the histogram class limits are set to 0, 1, 2, 3, ..., 29, 30.

	c. In the :ref:`docstring <python_docstring>`, describe the simulated distribution in a few sentences. What value is the distribution centered around? What type of shape does the distribution have? 

	d. In the :ref:`docstring <python_docstring>`, answer the following question: What happens to the variation in the simulation distribution as you increase the number of people sampled?

	e. In the :ref:`docstring <python_docstring>`, answer the following question: What happens to the variation in the simulation distribution as you increase the number of simulations?


3. Consider the experiment of rolling 10 six-sided die. Using the techniques described in the :ref:`project_six_background` section, simulate 10 rolls of a six-sided die. Perform the simulation 500 times.

.. hint::

	This one is easier to simulate if you use ``randint()`` instead of ``random()``!
	
	a. Calculate the mean and standard deviation of the simulated sampling distribution. In the :ref:`docstring <python_docstring>`, write a sentence or two interpretting the meaning of these sample statistics in the context of the sampling distributions.

	b. Plot the results using a histogram. Label the axes appropriately. Ensure the histogram class limits are set to 1, 2, 3, 4, 5, 6.

	c. In the :ref:`docstring <python_docstring>`, describe the simulated distribution in a few sentences. What value is the distribution centered around? What type of shape does the distribution have? Of what theorem in statistics is this an example?

	d. In the :ref:`docstring <python_docstring>`, answer the following question: what would happen to the shape of the distribution if you simulated rolling a 12-sided die instead of a six-sided die? What features mentioned in *part c* would change? What features would stay the same?
