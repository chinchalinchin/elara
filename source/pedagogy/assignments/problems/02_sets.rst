.. _set_theory_classwork:

----
Sets
----

Introduction
------------

For the problems #1 -9, you are given,

.. math:: 
    
    S = \{ 1, 2, 3, 5, 7, 12, 19, 31, 50, 81 \}

.. math:: 

    A = \{ 1, 2, 3, 19 \}

.. math:: 

    B = \{ 19, 50, 81 \}

.. math:: 

    C = \{ 2, 12, 19, 50, 81 \}

.. math:: 

    D = \{ 31, 50 \}

Where :math:`S` is the universal set and **A**, **B**, **C** and **D** are subsets of :math:`S`.

Defintions
----------
	
1. **Set Operations** 

Write the elements of each of the following sets in :ref:`list-notation`,

    a. :math:`A^c`

    b. :math:`B^c`

    c. :math:`A \cap B`

    d. :math:`A \cup B`

    e. :math:`C \cup A`

    f. :math:`C \cup B`

    g. :math:`C \cap A`

    h. :math:`C \cap B`

Laws
----

2. **Cardinality Laws** 

Answer each of the following problems,

    a. :math:`n(C)`

    b. :math:`n(C^c)`

    c. :math:`n(S)`

    d. :math:`n(S) - n(C^c)`

    e. **Spoiler Alert** Why does *part d* equal *part a*?

3. **De Morgan's Laws**. 

Write the elements of each of the following sets in :ref:`list-notation`. Use the answers from #1 where appriopriate.

    a. :math:`(A^c) \cup (B^c)``

    b. :math:`(A \cup B)^c`

    c. :math:`(A^c) \cap (B^c)`

    d. :math:`(A \cap B)^c`

    e. Based on the answers to *part a - d*, what conclusions can you draw about the relationship that exists between the operations of *complementation*, *intersection* and *union*?

4. **Absorption Laws** 

Write the elements of each of the following sets in :ref:`list-notation`. Use the answers from #1 where appriopriate.

    a. :math:`A \cup (A \cap B)`

    b. :math:`B \cap (A \cup B)`

    c. Based on the answers to *part a - b*, what conclusions can you draw about the relationship that exists between the operations of *intersection* and *union*?

5. **Distributive Laws** 

Write the elements of each of the following sets in :ref:`list-notation`. User the answers from #1 where appriopriate.

    a. :math:`C \cup (A \cap B)`

    b. :math:`C \cap (A \cup B)`

    c. :math:`(C \cup A) \cap (C \cup B)`

    d. :math:`(C \cap A) \cup (C \cap B)`

    e. Based on the answers to *part a - d*, what conclusions can you draw about the relationship that exists between the operations of *intersection* and *union*?

6. **Counting Laws**. 

Find the cardinality of each of the following sets. 

    a. :math:`n(D)`

	b. :math:`n(C)`

    c. :math:`D \cap C`

    d. :math:`(D \cap C)^c`

    e. :math:`n(D \cup C)`
    
    f. Why does :math:`n(D) + n(C) \neq n(D \cup C)`?

Relations
---------

1. **Membership** 

Determine whether each of the following propositions is *true* or *false*.

	a. :math:`2 \in A`
	
	b. :math:`5 \notin B`
	
	c. :math:`3 \in D`
	
	d. :math:`A \in S`
	
	e. :math:`A \notin S`
	
2. **Equivalence and Equality**. 

Determine whether each of the following propositions is *true* or *false*.

    a. :math:`A = B`

    b. :math:`A \equiv B`

    c. :math:`A = B \implies A \equiv B`

    d. :math:`A \equiv B \implies A = B`

3. **Subsets** 

Determine whether each of the following propositions is *true* or *false*.

    a. :math:`B \subseteq C`

    b. :math:`B^c \subseteq C^c`

    c. :math:`C^c \subseteq B^c`

4. **Power Sets**

Write the following sets in list notation.

	a. The set of all subsets of :math:`D`.
	
	b. The set of all subsets of :math:`B`.
	
	c. The set of all subsets of :math:`A`.
	
	d. In general, for a set **P** with *n* elements, how many subsets can be formed from **P**?
	
5. **Ordered Pairs**

Set theory is the foundation of all modern mathematics. For example, `Kazimierz Kuratowski <https://en.wikipedia.org/wiki/Kazimierz_Kuratowski>`_, a Polish mathematician, proposed the following `definition of an ordered pair <https://math.stackexchange.com/questions/1767604/please-explain-kuratowski-definition-of-ordered-pairs>`_,

.. topic:: Kuratowski's Definition of an Ordered Pair

	Let :math:`(a,b)` represent the set, 
	
	.. math::
		
		\{ \{ a \}, \{ a, b \} \}
		
Use Kuratowski's definition of an ordered pair to decide which of the following propositions is true:

	a. :math:`a \in (a,b)`
	
	b. :math:`\{ a \} \in (a,b)`
	
	c. :math:`(a,a)=\{ a \}`
	
	d. :math:`b \in (a,b)`
	
	e. :math:`\{ b \} \in (a,b)`
	
	f. :math:`\{ a, b \} \in (a,b)`
	
Theorems
--------

1. **Symbolic Propositions**

Let **E**, **F** and **G** be three events. Determine which of the following statements are correct and which are incorrect. Justify your answers.

	a. :math:`(F^c \cap G) \cup (E^c \cap G) = G \cap ((F \cup E)^c)`
	
	b. :math:`((E \cup F)^c) \cap G = (E^c) \cap (F^c) \cap (G)`

	c. :math:`((E \cap F) \cup (E \cap G) \cup (F \cap G)) \subset (E \cup F \cup G)`
	 
2. **Deductive Proofs** 

Suppose you are given two sets **E** and **F**. Using the properties of sets discussed in class and the ones covered in this classwork, derive an identity for each of the following expressions,

    a. :math:`(E \cap F^c) \cup (E \cap F)`

    b. :math:`(E \cup F^c) \cap (E \cup F)`

.. hint:: 

    Use the distributive laws from #5 and then use the one of the :ref:`complement-theorems`

.. _venn-diagram-problems:

Venn Diagrams
-------------

1. **Surveys Galore**

a. One hundred people were surveyed at random about the car they own. Twenty-two people said they own a car with two seats. Thirty-three people said they own a car with four-wheel drive. Eleven people said they own a car with two seats and four-wheel drive.

	i. How many people in the survey own a car with two seats or a car with four-wheel drive?

	ii. How many people in the survey did not own a car?

b. In a consumer survey of 500 people, 200 indicated that they would be buying a major appliance within the next month, 150 indicated that they would buy a car, and 25 said that they would purchase both a major appliance and a car. How many will purcahse neither?


c. One hundred people were surveyed at random about the devices they use every day. Ninety-two people said they use a cellphone or a laptop every day. Thirty-seven people said they use a cell phone and a laptop every day. Sixty-three people they use only a laptop every day. How many people use only a cellphone?

d. In a survey of 100 investors in the stock market,

- 50 owned shares in IBM
- 40 owned shares in AT&T
- 45 owned shares in GE
- 20 owned shares in both IBM and GE
- 15 owned shares in both AT&T and GE
- 20 owned shares in both IBM and AT&T
- 5 owned shares in all three

	i. How many of the investors surveyed did not have shares in any of the three companies?
	
	ii. How many owned just IBM shares?
	
	iii. How many owned just GE shares?
	
	iv. How many owned neither IBM nor GE? 
	
	v. How many owned either IBM or AT&T but no GE?

3. Shawn did a study of the colors used in the African national flags. He found that 38 flags have red, 20 have blue, 13 have both red and blue and 8 have neither red nor blue. Construct a Venn Diagram for Shawn and then answer the following questions.

	a. How many flags have red but not blue?

	b. How many flags have blue but not red?

	c. How many flags have red or blue?

	d. How many flags were included in the study? 


4. 90 students went to a school carnival. 3 had a hamburger, soft drink and ice-cream. 24 had hamburgers. 5 had a hamburger and a soft drink. 33 had soft drinks. 10 had a soft drink and ice-cream. 38 had ice-cream. 8 had a hamburger and ice-cream. How many had nothing?


5. A group of 62 students were surveyed, and it was found that each of the students surveyed liked at least one of the following three fruits: apricots, bananas, and cantaloupes. The results are as a follows,

- 34 liked apricots.
- 30 liked bananas.
- 33 liked cantaloupes (*weirdos*).
- 11 liked apricots and bananas.
- 15 liked bananas and cantaloupes.
- 17 liked apricots and cantaloupes.
- 19 liked exactly two of the following fruits: apricots, bananas, and cantaloupes
    
	a. How many students liked apricotes, but not bananas or cantaloupes?

	b. How many students liked cantaloupes, but not bananas or apricots?

	c. How many students liked all of the following three fruits: apricots, bananas, and cantaloupes?

	d. How many students liked apricots and cantaloupes, but not bananas?


6. Among 33 students in a class, 17 of them earned A's on the midterm exam, 14 earned A's on the final exam and 11 did not earn A's on either examination. How many students earned an A on both exams? 

7. From a small town, 120 persons were selected at random and asked the following question: Which of three Star Wars trilogies do you like, the prequel, the original or the sequel? The following results were obtained: 20 people like the prequel and sequel trilogy, 10 people like the prequel and original trilogy but not the sequel trilogy, 15 people liked all three, 30 people liked only the sequel trilogy, 35 people liked the original trilogy but not the sequel trilogy, 25 people liked the original and the sequel trilogy and 10 people hated all three. 
 
a. How many people liked only the prequel trilogy?

b. How many people liked only the original trilogy?

c. How many people liked the original and the prequel trilogy?