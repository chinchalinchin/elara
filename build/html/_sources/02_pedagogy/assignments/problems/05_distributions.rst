.. _probability-distribution-problems:

-------------
Distributions
-------------

.. _geometric-problems:

Geometric Distribution 
----------------------

1. **Conditions**

.. topic:: Conditions for Geometric Random Variable

	1. The trials must be independent.
	
	2. Each trial must be either a success or failure.
	
	3. The probability of each trial must be the same across trials.

Determine whether each of the following experiments satisfy the conditions for a Geometric Random Variable.

	a. A basketball player takes shots from the foul line and the number of shots is counted until he misses a basket. 
	
	b. The number of cards drawn from a standard deck of 52 cards *without* replacement is counted until a Queen is drawn. 
	
	c. The number of cards drawn from a standard deck of 52 cards *with* replacement is counted until a Queen is drawn.
	
	d. You count the number of random people you have to survey before someone says *Yes* to the question, "Have you seen the science faction magnum opus from film autuer Ridley Scott, *Blade Runner*?"
	
	e. Suppose two chess players keep playing until one of them wins three games in a row. You count the number of games they have to play until the match is over.
	
2. **Density**

.. topic:: Geometric Probability Density
	
	.. math::

		P(\mathcal{X}=x) = (1-p)^{x-1} \cdot p

Use the Geometric Probability Density Function to answer the following questions.

	a. If :math:`p=0.1`, what is :math:`P(\mathcal{X}=1)`?
	
	b. If :math:`p=0.1`, what is :math:`P(\mathcal{X}=10)`?
	
	c. If :math:`p=0.9`, what is :math:`P(\mathcal{X}=1)`?
	
	d. If :math:`p=0.9`, what is :math:`P(\mathcal{X}=10)`?
	
	e. Write a few sentences in plain English that explains how changing the parameter *p* of the Geometric Distribution affects the probability of its outcomes.

3. **Histogram**

Let the probability of success for a Geometric Random Variable be :math:`p = 0.3`. Create a probability distribution (i.e. a table) for :math:`\mathcal{X}=0,1,2,...,10`. Use this table to create and label histogram. Describe the distribution of a Geometric Random Variable wth :math:`p = 0.3`. 

4. **Probability**

Use the properties of probability and the Geometric Distribution to solve the following problems.

	a. From an ordinary deck of 52 cards, you draw cards at random and with replacement, until the first ace is drawn. what is the probability that atleast five draws are needed?

	
	b. A certain basketball player makes a foul shot 45% of the time. Suppose this player stands on the foul line and continues shooting until he makes two baskets. What is the probability that (i) the first basket occurs on the sixth shot? (ii) the first and second baskets occur on the fourth and eighth shots, respectively?
	
	c. The probability is 0.8 that Marty hits target *M* when he fires at it. The probability is 0.45 that Alvie hits target *A* when he fires at it. Marty and Alvie fire one shot each at their targets. If both of them hit their targets, they stop; otherwise, they will continue. What is the probability that they stop after 3 tries? 

5. **Expectations**

Solve the following problems.

	a. Refer to *#4a*. What is the expected value for the number of cards drawn before an ace is drawn?
	
	b. Refer to *#4b*. How many shots on average will it take the basketball player before the shot goes in? 
	
	c. Refer to *#4c*. What is the expected number of times Marty and Alvie fire before stopping?

6. **2016, Free Response, #4**

A company manufactures model rockets that require igniters to launch. Once an igniter is used to launch a rocket, the igniter cannot be reused. Sometimes an igniter fails to operate correctly, and the rocket does not launch. The company estimates that the overall failure rate, defined as the percent of all igniters that fail to operate correctly, is 15 percent.

A company engineer develops a new igniter, called the super igniter, with the intent of lowering the failure rate.

To test the performance of the super igniters, the engineer uses the following process.

    Step 1: One super igniter is selected at random and used in a rocket.
    
    Step 2: If the rocket launches, another super igniter is selected at random and used in a rocket.

Step 2 is repeated until the process stops. The process stops when a super igniter fails to operate correctly or 32 super igniters have successfully launched rockets, whichever comes first. Assume that super igniter failures are independent.

	a. If the failure rate of the super igniters is 15 percent, what is the probability that the first 30 super igniters selected using the testing process successfully launch rockets?

	b. Given that the first 30 super igniters successfully launch rockets, what is the probability that the first failure occurs on the thirty-first or the thirty-second super igniter tested if the failure rate of the super igniters is 15 percent?

	c. Given that the first 30 super igniters successfully launch rockets, is it reasonable to believe that the failure rate of the super igniters is less than 15 percent? Explain.

7. **2011, Free Response, #3**

.. warning::

	The problem requires more than the Geometric Distribution to solve.
	
An airline claims that there is a 0.10 probability that a coach-class ticket holder who flies frequently will be upgraded to first class on any flight. This outcome is independent from flight to flight. Sam is a frequent flier who always purchases coach-class tickets.

	a. What is the probability that Sam’s first upgrade will occur after the third flight?

	b. What is the probability that Sam will be upgraded exactly 2 times in his next 20 flights?

	c. Sam will take 104 flights next year. Would you be surprised if Sam receives more than 20 upgrades to first class during the year? Justify your answer.


.. _binomial-problems:

Binomial Distribution
---------------------

1. **Conditions for Binomial Random Variable**

The :ref:`conditions for a Binomial Random Variable <binomial-conditions>` are given below,

.. topic:: Binomial Conditions

	1. The number of trials :math:`n` must be fixed.
	
	2. Each trial must be independent of the others.
	
	3. Each trial must have a binary outcome, usually denoted success or failure.  
	
	4. The probability of success is the same in each trial.
	
Determine whether each of the following experiments satisfies the conditions for a Binomial Random Variable. If it does not satisfy the conditions for a Binomial Random Variable, state which condition is violated and why.

	a. A student is taking a multiple choice quiz. The quiz has 10 questions, with four possible answers each. Each question has only one correct answer. The student randomly guesses on each question. Let
	
		.. math::
		
			\mathcal{X} = \text{number of correct guesses}
	
	Is :math:`\mathcal{X}` a Binomial Random Variable"
	
	b. A manager oversees 11 female employees and 9 male employees. They need to pick 3 of these employees to go on a business trip, so the manager places all 20 names in a hat and chooses at random. Let 
	
		.. math::

			\mathcal{X} = \text{number of female employees chosen}
		
	
	Is :math:`\mathcal{X}` a Binomial Random Variable?
	
	c. You deal yourself a hand of 5 cards from a standard deck of 52 cards. Let
	
		.. math::
			
			\mathcal{X} = \text{number of Aces dealt}
		
		
	Is :math:`\mathcal{X}` a Binomial Random Variable?
	
	d. You deal yourself a single card from a standard deck of 52 cards, place it back into the deck and reshuffle. You repeat this process 10 times. Let
	
		.. math::
		
			\mathcal{X} = \text{number of Aces dealt}
		
	
	Is :math:`\mathcal{X}` a Binomial Random Variable?

	e. `15% of the world's population has seen atleast one Star Wars film <https://www.explainxkcd.com/wiki/index.php/1769:_Never_Seen_Star_Wars>`_. You ask 20 students whether or not they have seen a Star Wars film. Let 
	
		.. math::
		
			\mathcal{X} = \text{number of people who have seen atleast one Star Wars film}
		
	Is :math:`\mathcal{X}` a Binomial Random Variable?
	
2. **Probability Density**

.. topic:: Binomial Probability Density Function

	.. math::

		P(\mathcal{X}=x) = C^{n}_{r} \cdot p^x \cdot (1-p)^{n-x}
		
Use the Binomal Probability Density Function to answer the following questions.

	a. Before performing any calculations, answer the following questions. 
	
		i. If you flip a fair coin ten times, how many heads do you expect to get on average? 
		
		ii. If you perform :math:`n` trials where each trial has a probability of success :math:`p`, how many successes do you expect to get on average? 
	
	b. If :math:`n=10` and :math:`p=0.5`, find :math:`P(\mathcal{X}=3)`.
	
	c. If :math:`n=10` and :math:`p=0.5`, find :math:`P(\mathcal{X}=4)`.
	
	d. If :math:`n=10` and :math:`p=0.5`, find :math:`P(\mathcal{X}=5)`. 
	
	e. If :math:`n=10` and :math:`p=0.5`, find :math:`P(\mathcal{X}=6)`.
	
	f. If :math:`n=10` and :math:`p=0.5`, find :math:`P(\mathcal{X}=7)`.
	
	g. Write a few sentence in plain English interpretting the results of *part b - f*. What happens to Binomial probabilities on either side of the *expected value* of the distribution as you move away from that point? What features of the distribution are apparent from the calculations performed in *parts b - f*? 

3. **Applications**

	a. Suppose that only 25% of all drivers come to a complete stop at an intersection having flashing red lights in all directions when no other cars are visible. You stand at the intersection and randomly sample 20 cars as they pass through the intersection.

		i. What is the probability at most 5 will come to a complete stop?
		
		ii. What is the probability exactly 6 will come to a complete stop?
	
		iii. What is the probability at least 7 will come to a complete stop?
		
		iv. What is the relationship between *part i - iii*? What property of probability does this illustrate?
		
		v. How many drivers in your sample do you expect to come to a complete stop?
		
	b. A multiple choice quiz consists of 10 questions. Each question has five possible answers. After procrastinating for a week and not studying, you wake up the day of the quiz and realize you have no idea which of the answers are correct, so you guess at random on each question. 

		i. What is your probability of scoring a 7 on this quiz?
		
		ii. What is your probability of passing the quiz, i.e. scoring *at least* a 7?
		
		iii. What is the expected number of answers that will be marked correct?	
	
4. **Normal Approximation**

The :ref:`normal-distribution` can be used to approximate the Binomal Distribution under certain conditions. These conditions are given below for quick reference,

.. topic:: Conditions for Binomial Approximation
   
    :math:`n \cdot p \geq 10`

    :math:`n \cdot (1 - p) \geq 10`
    
Use these conditions to determine whether the following Binomial Random Variables can be approximated with the Normal Distribution. In each case, calculate the exact Binomial probability. If the Normal approximation is applicable, calculate the approximate probability and compare it to the exact value. 

	a. According to Mars, 24% of M&M plain candies are blue. In a given sample of 100 M&Ms, 27 are found to be blue. Assuming that the claimed rate of 24% is correct, find the probability of randomly selecting 100 M&Ms and getting 27 or more that are blue. Based on the result, is 27 (out of 100) an unusually high number of blue M&Ms?
	
	b. Six percent of people are universal blood donors (i.e., they can give blood to anyone without it being rejected). A hospital needs 10 universal donors to donate blood, so they conduct a blood drive. If 200 volunteers donate blood, what is the probability tht the number of universal donors is at least 10? Is the pool of 200 volunteers likely to be sufficient?
	
	c. A Boeing 767-300 aircraft has 213 seats. When someone buys a ticket for a flight there is a 0.0995 probability that the person will not show up for the flight. A ticket agent accepts 236 reservations for a flight that uses a Boeing 767-300. Find the probability that not enough seats will be available. Is this probability low enough so that overbooking is not a real concern? If not, how many tickets should be sold so that the probability is less than 10% that at least one person will not have a seat?
	
5. **2004, Free Response, #3**

At an archaeological site that was an ancient swamp, the bones from 20 brontosaur skeletons have been unearthed. The bones do not show any sign of disease or malformation. It is thought that these animals wandered into a deep area of the swamp and became trapped in the swamp bottom. The 20 left femur bones (thigh bones) were located and 4 of these left femurs are to be randomly selected without replacement for DNA testing to determine gender.

	a. Let X be the number out of the 4 selected left femurs that are from males. Based on how these bones were sampled, explain why the probability distribution of X is not binomial.

	b. Suppose that the group of 20 brontosaurs whose remains were found in the swamp had been made up of 10 males and 10 females. What is the probability that all 4 in the sample to be tested are male?

	c. The DNA testing revealed that all 4 femurs tested were from males. Based on this result and your answer from *part b*, do you think that males and females were equally represented in the group of 20 brontosaurs stuck in the swamp? Explain.

	d. Is it reasonable to generalize your conclusion in *part c* pertaining to the group of 20 brontosaurs to the population of all brontosaurs? Explain why or why not.

6. **2006, Free Response Form B, #6**

Sunshine Farms wants to know whether there is a difference in consumer preference for two new juice products—Citrus Fresh and Tropical Taste. In an initial blind taste test, 8 randomly selected consumers were given unmarked samples of the two juices. The product that each consumer tasted first was randomly decided by the flip of a coin. After tasting the two juices, each consumer was asked to choose which juice he or she preferred, and the results were recorded.

	a. Let *p* represent the population proportion of consumers who prefer Citrus Fresh. In terms of *p*, state the hypotheses that Sunshine Farms is interested in testing.

	b. One might consider using a one-proportion z-test to test the hypotheses in part *#a*. Explain why this would not be a reasonable procedure for this sample.

	c. Let X represent the number of consumers in the sample who prefer Citrus Fresh. Assuming there is no difference in consumer preference, find the probability for each possible value of X. Record the x-values and the corresponding probabilities in the table below.

.. image:: ../../../_static/img/problems/2006-apstats-frp-formb-06.png
	:align: center
	
7. **2003, Free Response, #3** 

Men's shirt sizes are determined by their neck sizes. Suppose that men's neck sizes are approximately normally distributed with mean 15.7 inches and standard deviation 0.7 inch. A retailer sells men's shirts in sizes S, M, L, XL, where the shirt sizes are defined in the table below.

.. image:: ../../../_static/img/problems/2003-apstats-frp-03.png
    :align: center

Use this information to answer the following questions.

	a. Because the retailer only stocks the sizes listed above, what proportion of customers will find that the retailer does not carry any shirts in their sizes? Show your work.

	b. Using a sketch of a normal curve, illustrate the proportion of men whose shirt size is M. Calculate this proportion.

	c. Of 12 randomly selected customers, what is the probability that exactly 4 will request size M ? Show your work.

8. **2007, Free Response Form B, #2**

The graph below displays the relative frequency distribution for X, the total number of dogs and cats owned per household, for the households in a large suburban area. For instance, 14 percent of the households own 2 of these pets.

.. image:: ../../../_static/img/problems/2007-apstats-frp-formb-02.png
	:align: center

Use this information to solve the following problems.

	a. According to a local law, each household in this area is prohibited from owning more than 3 of these pets. If a household in this area is selected at random, what is the probability that the selected household will be in violation of this law? Show your work.

	b. If 10 households in this area are selected at random, what is the probability that exactly 2 of them will be in violation of this law? Show your work.


9. **2022, Free Response, #3** 

A machine at a manufacturing company is programmed to fill shampoo bottles such that the amount of shampoo in each bottle is normally distributed with mean 0.60 liter and standard deviation 0.04 liter. Let the random variable **A** represent the amount of shampoo, in liters, that is inserted into a bottle by the filling machine.

	a. A bottle is considered to be underfilled if it has less than 0.50 liter of shampoo. Determine the probability that a randomly selected bottle of shampoo will be underfilled. Show your work.

	b. After the bottles are filled, they are placed in boxes of 10 bottles per box. After the bottles are placed in the boxes, several boxes are placed in a crate for shipping to a beauty supply warehouse. The manufacturing company's contract with the beauty supply warehouse states that one box will be randomly selected from a crate. If 2 or more bottles in the selected box are underfilled, the entire crate will be rejected and sent back to the manufacturing company. The beauty supply warehouse manager is interested in the probability that a crate shipped to the warehouse will be rejected. Assume that the amounts of shampoo in the bottles are independent of each other.

		i. Define the random variable of interest for the warehouse manager and state how the random variable is distributed.

		ii. Determine the probability that a crate will be rejected by the warehouse manager. Show your work.

	c. To reduce the number of crates rejected by the beauty supply warehouse manager, the manufacturing company is considering adjusting the programming of the filling machine so that the amount of shampoo in each bottle is normally distributed with mean 0.56 liter and standard deviation 0.03 liter. Would you recommend that the manufacturing company use the original programming of the filling machine or the adjusted programming of the filling machine? Provide a statistical justification for your choice.

10. **2021, Free Response, #3**

To increase morale among employees, a company began a program in which one employee is randomly selected each week to receive a gift card. Each of the company's 200 employees is equally likely to be selected each week, and the same employee could be selected more than once. Each week’s selection is independent from every other week.

	a. Consider the probability that a particular employee receives at least one gift card in a 52 -week year.

		i. Define the random variable of interest and state how the random variable is distributed.
		
		ii. Determine the probability that a particular employee receives at least one gift card in a 52 -week year. Show your work.

	b. Calculate and interpret the expected value for the number of gift cards a particular employee will receive in a 52 -week year. Show your work.

	c. Suppose that Agatha, an employee at the company, never receives a gift card for an entire 52 -week year. Based on her experience, does Agatha have a strong argument that the selection process was not truly random? Explain your answer.
	
11. **2010, Free Response Form B, #3**

A test consisting of 25 multiple-choice questions with 5 answer choices for each question is administered. For each question, there is only 1 correct answer.

	a. Let :math:`\mathcal{X}` be the number of correct answers if a student guesses randomly from the 5 choices for each of the 25 questions. What is the probability distribution of :math:`\mathcal{X}`?

This test, like many multiple-choice tests, is scored using a penalty for guessing. The test score is determined
by awarding 1 point for each question answered correctly, deducting 0.25 point for each question answered
incorrectly, and ignoring any question that is omitted. That is, the test score is calculated using the following
formula.

	Score = (1 x number of correct answers) – (0.25 x number of incorrect answers) + (0 x number of omits)

For example, the score for a student who answers 17 questions correctly, answers 3 questions incorrectly, and omits 5 questions is

	Score = (1 x 17) - (0.25 x 3) + (0 x 5) = 16.25.
	
Use this information to answer the following questions.

	b. Suppose a student knows the correct answers for 18 questions, answers those 18 questions correctly, and chooses randomly from the 5 choices for each of the other 7 questions. Show that the expected value of the student’s score is 18 when using the scoring formula above.

	c. A score of at least 20 is needed to pass the test. Suppose a student knows the correct answers for 18 questions, answers those 18 questions correctly, and chooses randomly from the 5 choices for each of the other 7 questions. What is the probability that the student will pass the test?

.. _normal-problems:

Normal Distribution
-------------------

1. Sketch a Standard Normal distribution in the x-y plane. Shade in the areas indicated in the problems below. Label the axes. Label each area with the percentage of the distribution that corresponds to the shaded region. Use a :ref:`z-table` to find the exact percentage.

	a. :math:`P(\mathcal{Z} \leq -1.62)`

	b. :math:`P(\mathcal{Z} \geq 1.62)`

	c. :math:`P(\mathcal{Z} \leq -1.96)`

	d. :math:`P(\mathcal{Z} \geq 1.96)`

	e. What is the relationship between parts *a* and *b*, and parts *c* and *d*? What characteristic of the Standard Normal distribution is being shown here? 

	f. :math:`P(\mathcal{Z} \leq -0.55)`

        g. :math:`P(\mathcal{Z} \geq 1.77)`

	h. :math:`P(\mathcal{Z} \leq 2.26)`

	i. :math:`P(\mathcal{Z} \geq -2.15)`


2. Sketch a Standard Normal distribution in the x-y plane. Shade in the areas indicated in the problems below. Label the axes. Label each area with the percentage of the distribution that corresponds to the shaded region. Use a :ref:`z-table` to find the exact percentage.

	a. :math:`P(-1.5 \leq \mathcal{Z} \leq 1.5)`

	b. :math:`P(-1.5 \leq \mathcal{Z} \leq 0)`

	c. :math:`P(0 \leq \mathcal{Z} \leq 1.5)`

	d. What is the relationship between parts *a*, *b* and *c*? Explain the result graphically. 

	e. :math:`P(0.33 \leq \mathcal{Z} \leq 1.05)`

	f. :math:`P(-1.17 \leq \mathcal{Z} \leq 2.21)`
	
3. Sketch a Standard Normal distribution in the x-y plane. Find the values of Z which correspond to the areas given below. Shade in the areas and label the axes with the value found. Use a :ref:`z-table` to solve the problem.

	a. 0.90
	
	b. 0.75

	c. 0.5 

	d. 0.25
	
	e. 0.10
	
4. **The Empirical Rule**

Since the Z-Table is the cumulative distribution function for the Standard Normal distribution, The :ref:`empirical-rule` can be derived through a Z-table. Recall the :ref:`empirical-rule` states,

.. topic:: Empirical Rule

	Approximately 68% of a distribution is within one standard deviation of the mean.
	
	Approximately 95% of a distribution is within two standard deviations of the mean.
	
	Approximately 99% of a distribution is within three standard deviations of the mean.
	
This can be stated more precisely in terms of the **Z** distributions as follows,

.. topic:: Empirical Rule (Mathematical Version, z Distributions)

	.. math::
		
		P(-1 \leq \mathcal{Z} \leq 1) = 0.68
	
	.. math::
		
		P(-2 \leq \mathcal{Z} \leq 2) = 0.95
		
	.. math::
		
		P(-3 \leq \mathcal{Z} \leq 3) = 0.99

The *Empirical Rule* is an approximation, meant for quick calculations. It is not exact, as you will soon discover.

	a. Use a :ref:`z-table` to find the exact value of :math:`P(-1 \leq \mathcal{Z} \leq 1)`
	
	b. Use a :ref:`z-table` to find the exact value of :math:`P(-2 \leq \mathcal{Z} \leq 2)`
	
	c. Use a :ref:`z-table` to find the exact value of :math:`P(-3 \leq \mathcal{Z} \leq 3)`

