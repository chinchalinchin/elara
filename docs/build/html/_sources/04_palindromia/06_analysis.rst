.. _section-v:

Section V: Analysis
===================

The study of Palindromes leads directly into the study of Delimiter distributions. The partitioning of Palindromes into the Perfect and Imperfect aspects highlights the asymmetry which separates the latter from the former class. Consider the pair of Perfect Palindromes, 

- god lived on no devil dog
- i am civic am i

Since, by :ref:`Definition 4.1.2 <definition-4-1-2>`, Perfect Palindromes are exactly the class of Sentences that are equal to their own Inverses, the Delimiters in a Perfect Palindrome display symmetry. The following barcharts show the Character indices of Delimiters for these examples. Note the horizontal axes are scaled to the Sentence String Length,

.. image:: ../_static/img/results/sentences/palindromes/delimiter_indices_perfect_palindrome_1.png
  :width: 400
  :alt: Delimiter Indices, Perfect Palindrome, Example #1

.. image:: ../_static/img/results/sentences/palindromes/delimiter_indices_perfect_palindrome_2.png
  :width: 400
  :alt: Delimiter Indices, Perfect Palindrome, Example #2

Notice the Delimiter indices are symmetrical about the center. Now consider the pair of Imperfect Palindromes, 

- goddesses so pay a possessed dog 
- borrow or rob

According to :ref:`Definition 4.1.3 <definition-4-1-3>`, Imperfect Palindromes must first be :math:`\sigma\text{-reduced}` to restore their symmetry. An examination of the corresponding barcharts for these examples show why,

.. image:: ../_static/img/results/sentences/palindromes/delimiter_indices_imperfect_palindrome_1.png
  :width: 400
  :alt: Delimiter Indices, Imperfect Palindrome, Example #1

.. image:: ../_static/img/results/sentences/palindromes/delimiter_indices_imperfect_palindrome_2.png
  :width: 400
  :alt: Delimiter Indices, Imperfect Palindrome, Example #2

Imperfect Palindromes are exactly those class of Palindromes which do not have symmetrical Delimiter distributions. 

The goal of this section is to understand the Delimiter symmetry displayed by Perfect Palindromes, in order to help further classify Imperfect Palindromes according to the type of Delimiter asymmetry found in a particular instance. In other words, the analysis seeks a method for quantifying a Perfect Palindrome's Delimiter symmetry in order to apply the same method to Imperfect Palindromes, with the hope of gaining greater insight into the syntactical obstacles preventing direct formal access to the class of Imperfect Palindromes.

The essential problem of modelling Delimiter distributions is the method of approach. Analytical methods, if not well constructed, are liable to lead to seemingly well-supported, but logically flawed conclusions. 

Consider taking Sentences from a Corpus and for each one, calculating and returning the Delimiter indices, as in the following,

.. math::

  ᚠ = \text{"error is the price we pay for progress"}

.. math::

  D_ᚠ = \{ (6, \sigma), (9, \sigma), (13, \sigma), (19, \sigma), (22, \sigma), (26, \sigma), (30, \sigma) \}

Note the set :math:`D_ᚠ` is the set involved in :ref:`Definition 3.2.1 <definition-3-2-1>` of the Delimiter Count function. If a large Corpus is analyzed so that each Sentence is reduced to a set of Delimiter indices, and then the frequency of Delimiter Counts is plotted, an interesting, but potentially misleading result is obtained. The following histograms show the result of this technique for Sentences of various fixed lengths. 

.. image:: ../_static/img/results/sentences/english/delimiter_distribution_n50.png
  :width: 400
  :alt: Delimiter Distribution, Sentence String Length = 50

.. image:: ../_static/img/results/sentences/english/delimiter_distribution_n100.png
  :width: 400
  :alt: Delimiter Distribution, Sentence String Length = 100

.. image:: ../_static/img/results/sentences/english/delimiter_distribution_n200.png
  :width: 400
  :alt: Delimiter Distribution, Sentence String Length = 200

As can be seen from the shape of the histograms, the Delimiter index distribution for Sentences of fixed length is roughly uniform (with a potentially significant spike in the far left tail of each distribution). These graphs suggest the Delimiter Count of a single Character, :math:`\zeta[k]`, can be approximated by a discrete, uniform random variable, conditional on the Sentence String Length,

.. math::

  P(\Delta(\hat{\zeta}[k]) | l(\zeta) = \lambda) = \frac{1}{\lambda}

Where :math:`P()` represents the probability of an event, :math:`\hat{\zeta[k]}` represents a random varaible and :math:`\lambda` represents a fixed String Length. However alluring, there is a subtle, but important assumption going into the generation of these histograms that prevents the acceptance of this conclusion.

When Sentences are reduced to Delimiter indices and plotted in aggregate, information related to the relative order of the Delimiter in the Sentence is lost. In other words, the method of construction used to generate these histogram implicitly assumes,

.. math::

  P(\Delta(\hat{zeta}[k]) | \Delta(\zeta[k-1]) = \delta_{k-1}, \Delta(\zeta[k-2]) = \delta_{k-2}, ... , \Delta(\zeta[1]) = \delta_1 ) = P(\Delta(\zeta[k]))

To provide a more concrete example, consider the Sentences, 

.. math::

  ᚢ = \text{"the dog runs across the field"}

.. math::
  
  ᚦ = \text{"the child laughs at the joke"}

In each case,

.. math::

  \Delta(ᚢ[4]) = \Delta(ᚦ[4]) = 1

The presence of the Delimiter after the article *"the"* affects the subsequent appearance of Delimiters in the Sentences. Due to grammatical rules, a noun must follow the article and this has tangible, measureable syntactic effects. Given the information :math:`\Delta(ᚢ[4]) = 1`, this fact greatly decreases (perhaps even nullifies) the event of :math:`\Delta(ᚢ[5]) = 1`. In fact, a probability model that describes linguistic entities might take it as an axiom,

.. math::

  P(\Delta(\hat{zeta}[k]) \,|\, \Delta(\zeta[k-1]) = 1 ) = 0

In summary, it cannot be discounted that knowing where a single Delimiter occurs in a Sentence influences the possible locations where other Delimiters in the same Sentence might occur. However, accounting for this contingency presents computational challenges. A Sentence with 100 Characters will have :math:`2^100` possible Delimiter configurations, by the Fundamental Counting Principle. Tracking the Delimiter distribution across different Sentence String Lengths becomes impossible. Enumerating and tallying these outcomes is a prohibitively expensive task, if abstraction is not employed to summarize the Delimiter *"mass"* of a Sentence. 

.. _section-v-i:

Section V.I: Sentence Integrals
-------------------------------

Before attempting to extricate the probability density of Delimiters within the Sentences of a Corpus, a conceptual apparatus is required for aggregating and assessing the distribution and configuration of Delimiters in a particular Sentence. 

This apparatus is embodied the concept of a *Sentence Integral*. A Sentence Integral is simply the sum of Delimiter indices in a Sentence. The reason for introducing the connotation of *"integration"* into the vernacular will become apparent after the particular form of its definition is appreciated. In short, the term *"integration"* is used here to evoke the idea of summing or accumulating values over a range, similar to the integral in calculus.

Definitions
^^^^^^^^^^^

.. _definition-5-1-1:

**Definition 5.1.1: Lefthand Sentence Integrals**

Let *ζ* be an arbitary Sentence from Corpus :math:`C_L` and let *k* be a natural number such that :math:`1 ≤ k ≤ \Lambda(\zeta)`. The *Lefthand Integral* of Sentence *ζ*, denoted :math:`\Phi_{-}(\zeta, k)`, is defined as,

.. math::

  \Phi_{-}(\zeta, k) = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[:i])}{l(\zeta)}
    
∎
    
.. _definition-5-1-2:

**Definition 5.1.2: Righthand Sentence Integrals**

The *Right-Hand Integral* of Sentence ζ, denoted :math:`\Phi_{+}(\zeta, k)`, is defined as,

.. math::

  \Phi_{+}(\zeta, k) = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[i:])}{l(\zeta)}
    
∎

Take note how the Delimiter Count function is employed in this definitions. Since the domain of discourse is Strings and all Characters are Strings, a Character is valid input to the Delimiter Count. The quantity :math:`\Delta(\zeta[i])` is essentially an indicator variable, taking on the values of 0 or 1, depending on if :math:`\zeta[i] = \sigma` or :math:`\zeta[i] \neq \sigma`.To draw an analogy to a famous mathematical function, the Delimiter Count :math:`\Delta(\zeta[i])` acts in a similar way to the a Dirac delta function :math:`\delta(x)`, in that it selects particular values to contribute to the integrand. 

Each Delimiter that is encountered along the length of the String is then weighted by the length of the Partial Sentence. Recall, by :ref:`Definition 4.2.1 <definition-4-2-1>` and :ref:`Definition 4.2.2 <definition-4-2-2>`, the length of Partial Sentences are given by,

.. math::

  l(\zeta[:i]) = i

.. math::

  l(\zeta[i:]) = l(\zeta) - i + 1

In other words, the weights given to the Delimiter Count are exactly the Character indices *relative to the starting or ending Character in the Sentence*. The Lefthand Sentence Integral represents the sum of Delimiter positions relative to the first Character, normalized by the String Length of the Sentence, while the Righthand Sentence Integral represents the sum of Delimiter positions relative to the last Character, also normalized by the String Length of the Sentence.

The following examples calculate the Lefthand and Righthand Sentence Integrals for various illustrative Palindromes.

**Example** 

1. Let *ᚠ = "live evil"*. Then *l(ᚠ) = 9*. Note *ᚠ* is a Perfect Palindrome.
   
.. list-table::
  :widths: 10 10 10 10 10 15 15
  :header-rows: 1

  * - k
    - ᚠ[k]
    - l(ᚠ[:k])
    - l(ᚠ[k:])
    - Δ(ᚠ[k])
    - :math:`\Phi_{-}(ᚠ ,k)`
    - :math:`\Phi_{+}(ᚠ ,k)`
  * - 1
    - "l"
    - 1
    - 9
    - 0
    - 0
    - 0
  * - 2
    - "i"
    - 2
    - 8
    - 0
    - 0
    - 0
  * - 3
    - "v"
    - 3
    - 7
    - 0
    - 0
    - 0
  * - 4
    - "e"
    - 4
    - 6
    - 0
    - 0
    - 0
  * - 5
    - " "
    - 5
    - 5
    - 1
    - (5/9)
    - (5/9)
  * - 6
    - "e"
    - 6
    - 4
    - 0
    - (5/9)
    - (5/9)
  * - 7
    - "v"
    - 7
    - 3
    - 0
    - (5/9)
    - (5/9)
  * - 8
    - "i"
    - 8
    - 2
    - 0
    - (5/9)
    - (5/9)
  * - 9
    - "l"
    - 9
    - 1
    - 0
    - (5/9)
    - (5/9)

2. Let *ᚠ = "we panic in a pew"*. Then *l(ᚠ) = 17*. Note *ᚠ* is an Imperfect Palindrome with more Non-Delimiter Characters in the first half in comparison to the second half. In other words, most of the Delimiters in *ᚠ* occur in the second half of the Sentence.
   
.. list-table::
  :widths: 10 10 10 10 10 15 15
  :header-rows: 1

  * - k
    - ᚠ[k]
    - l(ᚠ[:k])
    - l(ᚠ[k:])
    - Δ(ᚠ[k])
    - :math:`\Phi_{-}(ᚠ ,k)`
    - :math:`\Phi_{+}(ᚠ ,k)`
  * - 1
    - "w"
    - 1
    - 17
    - 0
    - 0
    - 0
  * - 2
    - "e"
    - 2
    - 16
    - 0
    - 0
    - 0
  * - 3
    - " "
    - 3
    - 15
    - 1
    - (3/17)
    - (15/17)
  * - 4
    - "p"
    - 4
    - 14
    - 0
    - (3/17)
    - (15/17)
  * - 5
    - "a"
    - 5
    - 13
    - 0
    - (3/17)
    - (15/17)
  * - 6
    - "n"
    - 6
    - 12
    - 0
    - (3/17)
    - (15/17)
  * - 7
    - "i"
    - 7
    - 11
    - 0
    - (3/17)
    - (15/17)
  * - 8
    - "c"
    - 8
    - 10
    - 0
    - (3/17)
    - (15/17)
  * - 9
    - " "
    - 9
    - 9
    - 1
    - (12/17)
    - (24/17)
  * - 10
    - "i"
    - 10
    - 8
    - 0
    - (12/17)
    - (24/17)
  * - 11
    - "n"
    - 11
    - 7
    - 0
    - (12/17)
    - (24/17)
  * - 12
    - " "
    - 12
    - 6
    - 1
    - (24/17)
    - (30/17)
  * - 13
    - "a"
    - 13
    - 5
    - 0
    - (24/17)
    - (30/17)
  * - 14
    - " "
    - 14
    - 4
    - 1
    - (38/17)
    - (34/17)
  * - 15
    - "p"
    - 15
    - 3
    - 0
    - (38/17)
    - (34/17)
  * - 16
    - "e"
    - 16
    - 2
    - 0
    - (38/17)
    - (34/17)
  * - 17
    - "w"
    - 17
    - 1
    - 0
    - (38/17)
    - (34/17) 

3. Consider how the Sentence Integrals behave String Inversion. Let *ᚠ = "draw no dray a yard onward"*. Then *l(ᚠ) = 26*. Note *ᚠ* is an Imperfect Palindrome with a similar (but not identical) distribution of Delimiters around the Pivot.

.. list-table::
  :widths: 8 8 12 12 10 10 12 15 15 10 12 18 18
  :header-rows: 1

  * - k
    - ᚠ[k]
    - inv(ᚠ)[k]
    - l(ᚠ[:k])
    - l(ᚠ[k:])
    - Δ(ᚠ[k])
    - Δ(inv(ᚠ)[k])
    - :math:`\Phi_{-}(ᚠ ,k)`
    - :math:`\Phi_{+}(ᚠ ,k)`
    - Δ(ᚠ[:k])
    - Δ(inv(ᚠ)[:k])
    - :math:`\Phi_{-}(\text{inv}(ᚠ) ,k)`
    - :math:`\Phi_{+}(\text{inv}(ᚠ) ,k)`
  * - 1
    - "d"
    - "d"
    - 1
    - 26
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  * - 2
    - "r"
    - "r"
    - 2
    - 25
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  * - 3
    - "a"
    - "a"
    - 3
    - 24
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  * - 4
    - "w"
    - "w"
    - 4
    - 23
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  * - 5
    - " "
    - "n"
    - 5
    - 22
    - 1
    - 0
    - (5/26)
    - (22/26)
    - 1
    - 0
    - 0
    - 0
  * - 6
    - "n"
    - "o"
    - 6
    - 21
    - 0
    - 0
    - (5/26)
    - (22/26)
    - 1
    - 0
    - 0
    - 0
  * - 7
    - "o"
    - " "
    - 7
    - 20
    - 0
    - 1
    - (5/26)
    - (22/26)
    - 1
    - 1
    - (7/26)
    - (20/26)
  * - 8
    - " "
    - "d"
    - 8
    - 19
    - 1
    - 0
    - (13/26)
    - (41/26)
    - 2
    - 1
    - (7/26)
    - (20/26)
  * - 9
    - "d"
    - "r"
    - 9
    - 18
    - 0
    - 0
    - (13/26)
    - (41/26)
    - 2
    - 1
    - (7/26)
    - (20/26)
  * - 10
    - "r"
    - "a"
    - 10
    - 17
    - 0
    - 0
    - (13/26)
    - (41/26)
    - 2
    - 1
    - (7/26)
    - (20/26)
  * - 11
    - "a"
    - "y"
    - 11
    - 16
    - 0
    - 0
    - (13/26)
    - (41/26)
    - 2
    - 1
    - (7/26)
    - (20/26)
  * - 12
    - "y"
    - " "
    - 12
    - 15
    - 0
    - 1
    - (13/26)
    - (41/26)
    - 2
    - 2
    - (19/26)
    - (32/26)
  * - 13
    - " "
    - "a"
    - 13
    - 14
    - 1
    - 0
    - (26/26)
    - (55/26)
    - 3
    - 2
    - (19/26)
    - (32/26)
  * - 14
    - "a"
    - " "
    - 14
    - 13
    - 0
    - 1
    - (26/26)
    - (55/26)
    - 3
    - 3
    - (33/26)
    - (46/26)
  * - 15
    - " "
    - "y"
    - 15
    - 12
    - 1
    - 0
    - (41/26)
    - (67/26)
    - 4
    - 3
    - (33/26)
    - (46/26)
  * - 16
    - "y"
    - "a"
    - 16
    - 11
    - 0
    - 0
    - (41/26)
    - (67/26)
    - 4
    - 3
    - (33/26)
    - (46/26)
  * - 17
    - "a"
    - "r"
    - 17
    - 10
    - 0
    - 0
    - (41/26)
    - (67/26)
    - 4
    - 3
    - (33/26)
    - (46/26)
  * - 18
    - "r"
    - "d"
    - 18
    - 9
    - 0
    - 0
    - (41/26)
    - (67/26)
    - 4
    - 3
    - (33/26)
    - (46/26)
  * - 19
    - "d"
    - " "
    - 19
    - 8
    - 0
    - 1
    - (41/26)
    - (67/26)
    - 4
    - 4
    - (52/26)
    - (54/26)
  * - 20
    - " "
    - "o"
    - 20
    - 7
    - 1
    - 0
    - (61/26)
    - (74/26)
    - 5
    - 4
    - (52/26)
    - (54/26)
  * - 21
    - "o"
    - "n"
    - 21
    - 6
    - 0
    - 0
    - (61/26)
    - (74/26)
    - 5
    - 4
    - (52/26)
    - (54/26)
  * - 22
    - "n"
    - " "
    - 22
    - 5
    - 0
    - 1
    - (61/26)
    - (74/26)
    - 5
    - 5
    - (74/26)
    - (59/26)
  * - 23
    - "w"
    - "w"
    - 23
    - 4
    - 0
    - 0
    - (61/26)
    - (74/26)
    - 5
    - 5
    - (74/26)
    - (59/26)
  * - 24
    - "a"
    - "a"
    - 24
    - 3
    - 0
    - 0
    - (61/26)
    - (74/26)
    - 5
    - 5
    - (74/26)
    - (59/26)
  * - 25
    - "r"
    - "r"
    - 25
    - 2
    - 0
    - 0
    - (61/26)
    - (74/26)
    - 5
    - 5
    - (74/26)
    - (59/26)
  * - 26
    - "d"
    - "d"
    - 26
    - 1
    - 0
    - 0
    - (61/26)
    - (74/26)
    - 5
    - 5
    - (74/26)
    - (59/26)

Consider :math:`k = 6`. It's corresponding inverted Character position would be :math:`l(ᚠ) - k + 1 = 26 - 6 + 1 = 21`. The Delimiter Counts of the Partial Sentences up to these indices are given by,

  - Δ(ᚠ[:6]) = 1
  - Δ(ᚠ[6:]) = 4
  - Δ(ᚠ[:21]) = 5
  - Δ(ᚠ[21:]) = 0

The Delimiter Counts of the Inverse Partial Sentences up to these indices are given by,

  - Δ(inv(ᚠ)[:21]) = 4
  - Δ(inv(ᚠ)[21:]) = 1
  - Δ(inv(ᚠ)[:6]) = 0
  - Δ(inv(ᚠ)[6:]) = 5

Note the total number of Delimiters starting at Character Index 1 up to Character Index 6 in the original Sentence is 1. This corresponds to *Δ(ᚠ)[:6]* and to *Δ(inv(ᚠ)[21:])*. In addition, The total number of Delimiters starting at Character Index 26 and working backwards toward Character Index 21 is 0. This corresponds to *Δ(ᚠ)[21:]* and to *Δ(inv(ᚠ)[:6])*.

Since the String Length of the Sentence and its Inverse are both even, by :ref:`Theorem 4.2.3 <theorem-4-2-3>`, the Pivot is given by,

.. math::

  \omega{ᚠ} = 13

Using :ref:`Definition 3.2.1 <definition-3-2-1>`, the Delimiter Count is found by first identifying the Character indices of Delimiters in the Sentence and collecting them into the set :math:`D_{ᚠ}`,

.. math::

  D_{ᚠ} = \{ (5, \sigma), (8, \sigma), (13, \sigma), (15, \sigma), (20, \sigma) \}

So that the Delimiter Count is found by taking the cardinality of the set :math:`D_{ᚠ}`,

.. math::

  \Delta(ᚠ) = \lvert D_{ᚠ} \rvert = 5

The set :math:`D_{ᚠ}` expresses the distance of the Delimiters relative to the start of the Sentence. The distances can be expressed relative to the Pivot by subtracting the value of :math:`\Phi(\zeta)` from each value in :math:`D_{ᚠ}`,

.. math::

    \{ (-8, \sigma), (-5, \sigma), (0, \sigma), (2, \sigma), (7, \sigma) \}


This makes clear the Delimiters on the left side of the Pivot are further from the Pivot than the Delimiters on the right side. Furthermore, notice the Delimiter Count of the Inverse is calculated with, 

.. math::
    
    D_{\text{inv}(ᚠ)} = \{ (26 - 20 + 1, \sigma), (26 - 15 + 1, \sigma), (26 - 13 + 1, \sigma), (26 - 8 + 1, \sigma), (26 - 5 + 1, \sigma) \}

.. math::

    D_{\text{inv}(ᚠ)} = \{ (7, \sigma), (12, \sigma),  (14, \sigma), (19, \sigma), (22, \sigma) \}

Which confirms :ref:`Theorem 3.2.2 <theorem-3-2-2>`,

.. math::

  \Delta(ᚠ) = \lvert D_{ᚠ} \rvert = 5

If the Pivot is subtracted from each coordinate in :math:`D_{\text{inv}(ᚠ)}`,

.. math::

    \{ (-6, \sigma), (-1, \sigma), (1, \sigma), (6, \sigma), (9, \sigma) \}

When *ᚠ* is inverted, the index at the Pivot is no longer occupied by the same Character,

.. math::

  ᚠ[\omega(\zeta)] = ᚠ[13] = \sigma 

.. math::

  \text{inv}(ᚠ)[\omega(\zeta)] = \text{inv}(ᚠ)[13] = "a"
  
The Lefthand Integral of the Original Sentence is,

.. math::

  \Phi_{-}(ᚠ ,26) = \frac{61/26} = 2.3461538461538463

The Righthand Integral of the Original Sentence is,

.. math::
  
  \Phi_{+}(ᚠ ,26) = \frac{74/26} = 2.8461538461538463

The midpoint of the integrals is given by,

.. math::

  \frac{\Phi_{+}(ᚠ ,26) + \Phi_{-}(ᚠ ,26)}{2} = 2.5961538461538463

The difference of the integrals is given by,

.. math::

  \Phi_{+}(ᚠ ,26) - \Phi_{-}(ᚠ ,26)} = 0.5

TODO

.. math::

  \Phi_{-}(\text{inv}(ᚠ) ,26) = \frac{74/26} = 2.8461538461538463

TODO

.. math::
  
  \Phi_{+}(\text{inv}(ᚠ),26) = \frac{61/26} = 2.3461538461538463

∎

From these examples, it can be seen that Sentence Integrals can be regarded as a measure of *"delimiter mass"*. When the Lefthand Sentence Integral is greater than the Righthand Sentence Integral, this is an indication the Sentence has more Delimiters in its right half than its left half. In other words, the Delimiters positions relative to the start of the Sentence sum to a greater number than the Delimiter positions relative to the end.

For the same reason, if the Righthand Sentence Integral is greater than the Lefthand Sentence Integral, this is an indication the Sentence has more Delimiters in its left half than its right half. In other words, the Delimiters positions relative to the end of the Sentence sum to a greater number than the Delimiter positions relative to the start.

This method of *"weighing"* the Delimiters in a Sentence provides a method for abstractly describing the symmetry of Delimiters in Perfect Palindromes. Before using this method to quantify the symmetry of Perfect Palindromes, the next section will strengthen the definitions of Sentence Integrals with some theorems. 

Theorems
^^^^^^^^

As the introduction suggested through example a Sentence Integral can be regarded as a measure of the Delimiter symmetry in a Sentence. A Sentence Integral is the sum of the Delimiter indices. Each contribution of the Delimiter Count (0 or 1) to the integral is weighted by its distance from the starting point of the Sentence or the ending point of the Sentence (the Character index of the Delimiter), depending on if the Left- or Right-hand Sentence Integrals are taken. The theorems in this section will establish the properties of this sentential *"center of delimter mass"*.

The first two theorems, :ref:`Theorem 5-1-1 <theorem-5-1-1>` and :ref:`Theorem 5.1.2 <theorem-5-1-2>`, establish the lower bound for all Sentence Integrals. 

.. _theorem-5-1-1:

**Theorem 5.1.1** :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\zeta, k) \geq 0 \land \Phi_{+}(\zeta,) \geq 0`

This theorem can be stated in natural language as follows: Sentence Integrals are always greater than or equal to zero. 


Let *ζ* be an arbitrary Sentence in the Corpus,

.. math::

  1. \quad \zeta \in C_L

Let *k* be a natural number such that :math:`1 \leq k \leq l(\zeta)`

By :ref:`Definition 5.1.1 <definition-5-1-1>` and :ref:`Definition <definition-5-1-2>`,

.. math::

  2. \quad \Phi_{-} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[:i])}{l(\zeta)}

.. math::

  3. \quad \Phi_{+} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[i:])}{l(\zeta)}

By :ref:`Definition 3.2.1 <definition-3-2-1>`, :math:`\Delta(\zeta[i])` is either 0 or 1 for all *i*. *l(ζ[:i])*, *l(ζ[i:])*, and *l(ζ)* are all non-negative, by :ref:`Definition 1.1.3 <definition-1-1-3>`. Therefore, each term in the summations is non-negative (The sum of non-negative terms is always non-negative.

Thus, 

.. math::

  4. \quad \Phi_{-}(\zeta, k) \geq 0 \land \Phi_{-}(\zeta, k) \geq 0

Since *ζ* and *k* were arbitrary, this can be generalized over the Corpus,

.. math::

  5. \quad \forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\zeta,k) \geq 0 \land \Phi_{+}(\zeta,k) \geq 0

∎

.. _theorem-5-1-2:

**Theorem 5.1.2** :math:`\forall \zeta in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\varsigma(\zeta), k) = \Phi_{+}(\varsigma(\zeta), k) = 0`

This theorem can be stated in natural language as follows: The Sentence Integral of a :math:`\sigma`-reduction is zero.

Let *ζ* be an arbitrary Sentence in the Corpus,

.. math::

  1. \quad \zeta \in C_L

and let *k* be a natural number such that :math:`1 \leq k \leq l(\zeta)`.

By :ref:`Definition 3.1.2 <definition-3-1-2>`, the *σ*-reduction of *ζ*, denoted *ς(ζ)*, is a String obtained by removing all Delimiter Characters (*σ*) from *ζ*. Consider the Left-Hand Integral of *ς(ζ)* up to index k:

.. math::

  2. \quad \Phi_{-}(\varsigma(\zeta), k) = \sum_{i=1}^{k} \Delta(\varsigma(\zeta)[:i]) \cdot \frac{l(\varsigma(\zeta)[:i])}{l(\varsigma(\zeta))}
     
By the :ref:`Definition 4.2.1 <definition-4-2-1>` of Left Partial Sentence and Definition 3.1.2 of *σ*-reduction, *ς(ζ)[:i]* is a String contained in *ς(ζ)* from the beginning up to the *i*:sup:`th` Character. Since *ς(ζ)* contains no Delimiters, *ς(ζ)[:i]* will also contain no Delimiters. Therefore, by Theorem A.2.11,

.. math::

  3. \quad \forall i \in N_k: \Delta(\sigma(\zeta)[:i]) = 0
   
Substituting this into step 4,

.. math::

  4. \quad \Phi_{-}(\varsigma(\zeta), k) = \sum_{i=1}^{k} 0 \cdot \frac{l(\varsigma(\zeta)[:i])}{l(\varsigma(\zeta))} = 0
   
By similar logic, 

.. math::
  
  5. \quad \Phi_{+}(\varsigma(\zeta), k) = 0

Thus, both the Left-Hand and Right-Hand Integrals of *ς(ζ)* are equal to 0,

.. math::

  6. \quad \Phi_{+}(\varsigma(\zeta), k) = \Phi_{-}(\varsigma(\zeta), k) = 0
   
Since *ζ* and *k* were arbitrary, this can be generalized over the Corpus,

  7. \quad \forall \zeta in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\varsigma(\zeta), k) = \Phi_{+}(\varsigma(\zeta), k) = 0

∎

The next two theorems provide a method for calculating the Lefthand and Righthand Sentence Integrals numerically.

.. _theorem-5-1-3:

**Theorem 5.1.3** :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[:i])}{l(\zeta)} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{i}{l(\zeta)}`

Let *ζ* be an arbitrary Sentence in the Corpus,

.. math::

  1. \quad \zeta \in C_L 
    
Let *k* be a natural number such that :math:`1 \leq k \leq N_{l(\zeta)}`. By :ref:`Definition 4.2.1 <definition-4-2-1>` of Left Partial Sentences, for any *i* where :math:`1 \leq i \leq l(\zeta)`,

.. math::

  2. \quad l(\zeta[:i]) = i

Substituting step 2 into :ref:`Definition 5.1.1 <definition-5-1-1>` of Lefthand Sentence Integrals and generalizing over the Corpus,

..  math::

  3. \quad \forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[:i])}{l(\zeta)} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{i}{l(\zeta)}

∎

.. _theorem-5-1-4:

**Theorem 5.1.4** :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[i:])}{l(\zeta)} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta)-i+1}{l(\zeta)}`

Let *ζ* be an arbitrary Sentence in the Corpus,

.. math::

  1. \quad \zeta \in C_L 
    
Let *k* be a natural number such that :math:`1 \leq k \leq l(\zeta)`. By :ref:`Definition 4.2.2 <definition-4-2-2>` of Right Partial Sentences, for any *i* where :math:`1 \leq i \leq l(\zeta)`, 

.. math::

  2. l(\zeta[i:]) = l(\zeta) - i + 1
  
Substituting step 2 into :ref:`Definition 5.1.2 <definition-5-1-2>` of Righthand Sentence Integrals and generalizing over the Corpus,

.. math::

  \forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[i:])}{l(\zeta)} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta)-i+1}{l(\zeta)}

∎

As mentioned previously, the terms *(l(ζ) - i + 1)* and *i* that appear in the Sentence Integral summation may be thought of as the *"weight"* of a Delimiter. Since the Delimiter Count is either 0 or 1 for a single Character, the weight assigned to Delimiters, i.e. when :math:`\Delta(\zeta[i]) = 1`, in a Sentence are the only contributions to the summation in a Sentence Integral. This analogy to the mathematical concepts of density and mass is codified in the following definition.

.. _definition-5-1-3:

**Definition 5.1.3: Delimiter Mass**

Let *ζ* be an arbitrary Sentence in the Corpus :math:`C_L`, and let *I* be a natural number such that :math:`1 \leq i \leq l(\zeta)`. 

The Righthand Delimiter Mass at Character Index *i*, denoted :math:`\mu_sub{+}(\zeta, i)`, is defined as,

.. math::

  \mu_{+}(\zeta, i) = \Delta(\zeta[i]) \cdot (l(\zeta) - i + 1)

The Lefthand Delimiter Mass at Character Index *i*, denoted :math:`\mu_sub{-}(\zeta, i)` is defined as,

.. math::

  \mu_{-}(\zeta, i) = \Delta(\zeta[i]) \cdot i

∎

The next theorem uses :ref:`Definition 5.1.3 <definition-5-1-3>` to show if the Delimiters in the left half of Sentence relative to the end *"weigh"* more than the Delimiters in the right half relative to the start, then this can only happen if the Righthand Sentence Integral is greater than the Lefthand Sentence Integral. Note the use of the Pivot :math:`\omega(\zeta)` in following theorem.

.. _theorem-5-1-5:

**Theorem 5.1.5** :math:`\forall \zeta \in C_L: \sum_{i=1}^{\omega(\zeta)} \mu_{+}(\zeta,i) > \sum_{\omega(\zeta)+1}^{l(\zeta) \mu_{-}(\zeta, i) \leftrightarrow \Phi_{+}(\zeta, l(\zeta)) > \Phi_{-}(\zeta, l(\zeta))`


(→) Let *ζ* be an arbitrary Sentence in the Corpus. Assume,

.. math::
  
  1. \quad \sum_{i=1}^{\omega(\zeta)} \mu_{+}(\zeta,i) > \sum_{i=\omega(\zeta)+1}^{l(\zeta)} \mu_{-}(\zeta,i)

By :ref:`Definition 5.1.3 <definition-5-1-3>`, this is equivalent to,

.. math::

  2. \quad \sum_{i=1}^{\omega(\zeta)} \Delta(\zeta[i]) \cdot (l(\zeta - 1 + 1)) > \sum_{i=\omega(\zeta)+1}^{l(\zeta)} \Delta(\zeta[i]) \cdot i

In other words, the assumption in step 1 is equivalent to claiming the sum of the Delimiters weights in the first half of the Sentence (up to and including the Pivot) is greater than the dum of Delimiter weights in the second half (after the Pivot). It is to be shown,

.. math::

  2. \quad \Phi_{-}(\zeta, l(\zeta)) > \Phi_{-}(\zeta, l(\zeta))

Expanding the integrals,

    1. Ω:sub:`-`(ζ,l(ζ)) = Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (i/l(ζ)) + Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * (i/l(ζ))

    2. Ω:sub:`+`(ζ,l(ζ)) = Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) + Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ))

We can rewrite the assumption as:

    6. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (l(ζ) - i + 1) > Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * i

Divide both sides by l(ζ):

    7. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) > Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * (i/l(ζ))

Notice that the left-hand side of this inequality is part of the Right-Hand Integral *Ω*:sub:`+`(*ζ,l(ζ)*), and the right-hand side is part of the Left-Hand Integral *Ω*:sub:`-`(*ζ,l(ζ)*).

Since *l(ζ) - i + 1* > *i* for all *i ≤ m*, the weighted contribution of each Delimiter in the first half is larger in the Right-Hand Integral than in the Left-Hand Integral.

In addition, for *i > m*, we have *i > l(ζ) - i + 1*, meaning the weights *i/l(ζ)* are greater in the Left-Hand Integral than the corresponding weights *(l(ζ) - i + 1)/l(ζ)* in the Right-Hand Integral. Therefore, if the weighted sum of delimiters in the first half (weighted for the Right-Hand Integral) is greater than the weighted sum of delimiters in the second half (weighted for the Left-Hand Integral), this implies that the overall Right-Hand Integral must be greater than the overall Left-Hand Integral. Thus, 

    8. Ω:sub:`+`(ζ,l(ζ)) > Ω:sub:`-`(ζ,l(ζ))

(←) Assume,

    1. Ω:sub:`+`(ζ,l(ζ)) > Ω:sub:`-`(ζ,l(ζ))

By Definition A.8.1,

    2. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) + Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) > Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (i/l(ζ)) + Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * (i/l(ζ))

Rearranging the terms,

    3. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) - Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (i/l(ζ)) > Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * (i/l(ζ)) - Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ))

Simplifying,

    4. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - 2i + 1)/l(ζ)) > Σ:sub:`i=m+1`:sup:l(ζ)Δ(ζ[i]) * (2i - l(ζ) - 1)/l(ζ)

Since *l(ζ) - 2i + 1 > 0* for *i ≤ m* and *2i - l(ζ) - 1 > 0* for *i > m*, it can be inferred for the inequality to hold, the weighted sum of Delimiters in the first half must be greater than the weighted sum of Delimiters in the second half, where the weights are determined by their distance from the respective ends of the sentence.

    5. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (l(ζ) - i + 1) > Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * i.

Plugging in Definition A.8.2,

    6. Σ:sub:`i=1`:sup:`m` μ:sub:`+`(ζ, i) > Σ:sub:`i=m+1`:sup:`l(ζ)` μ:sub:`-`(ζ, i)


Since both directions of the equivalence hold and *ζ* was arbitrary, this can generalize over the Corpus,
 
    ∀ ζ ∈ C:sub:`L``: Σ:sub:`i=1`:sup:`ω(ζ)` μ:sub:`+`(ζ, i)  > Σ:sub:`i=ω(ζ)+1`:sup:`l(ζ)` μ:sub:`-`(ζ, i) ↔ Ω:sub:`+`(ζ,l(ζ)) > Ω:sub:`-`(ζ,l(ζ)) 
  
∎

TODO

.. _theorem-5-1-6:

**Theorem 5.1.6** ∀ ζ ∈ PP: ∀ i ∈ N:sub:`l(ζ)`: Ω:sub:`-`(ζ,i) = Ω:sub:`+`(ζ,i)

Let *ζ* be an arbitrary Perfect Palindrome in the Corpus C:sub:`L`,

    1. ζ ∈ PP

and let *k* be a natural number such that *1 ≤ k ≤ l(ζ)*. By Definition 3.2.2, since *ζ* is a Perfect Palindrome,

   2. ζ = inv(ζ)
   
This means that the Sentence reads the same forwards as backwards. By Definition A.8.1, the Left-Hand Integral of *ζ* up to index *k* is:

   3. Ω:sub:`-`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[:i]) * (l(ζ[:i])/l(ζ))

And the Right-Hand Integral of ζ up to index k is:

   4. Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i:]) * (l(ζ[i:])/l(ζ))
   
It must be shown that,

   5. Ω:sub:`-`(ζ,k) = Ω:sub:`+`(ζ,k).

Since *ζ = inv(ζ)*, by Definition 1.2.4 of String Inversion

   6. ∀ i ∈ N:sub:`l(ζ)` ζ[i] = inv(ζ)[l(ζ) - i + 1]

Now consider the Delimiter Count Function *Δ(ζ[:i])*. By Definition A.2.1, this function counts the number of Delimiters in the Left Partial Sentence up to index *i*. By Theorem A.2.2, the Delimiter Count is invariant under inversion. 

Furthermore, since *ζ* is a Perfect Palindrome, the Left Partial Sentence up to index i is the inverse of the Right Partial Sentence starting at index l(ζ) - i + 1. In other words:

   7. ζ[:i] = inv(ζ[l(ζ) - i + 1:])
   
Therefore,

   8. Δ(ζ[:i]) = Δ(inv(ζ[l(ζ) - i + 1:])) =  Δ(ζ[l(ζ) - i + 1:])
   
Now consider the Right-Hand Integral,

   9. Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i:]) * (l(ζ[i:])/l(ζ))

Make the following change of variables in the summation. Let *j = l(ζ) - i + 1*. Then, as *i* goes from 1 to *k*, *j* goes from *l(ζ)* to *l(ζ) - k + 1*,

   10. Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[l(ζ) - j + 1:]) * (l(ζ[l(ζ) - j + 1:])/l(ζ))
   
Substituting in step 8,

   11. Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ[l(ζ) - j + 1:])/l(ζ))
   
By Theorem 3.2.13, 

   12. l(ζ[l(ζ) - j + 1:]) = l(ζ) - l(ζ[:j]) + 1. 

Substituting this into step 11,

   13.  Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - l(ζ[:j]) + 1)/l(ζ)
   14.  Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - j + 1)/l(ζ)

Since *ζ* is a Perfect Palindrome,

   15.  Δ(ζ[:j]) = Δ(ζ[l(ζ) - j + 1:])

Furthermore, from Definition 3.2.5 of Left Partial Sentences, 

   16.  l(ζ[:j]) = j
   
Substituting step 15 in step 10,

   17.  Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - l(ζ[:j]) + 1)/l(ζ)

And then substituting step 16 into step 17,
    
   18.  Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - j + 1)/l(ζ)

This expression is almost the same as the Left-Hand Integral, except for the summation limits. However, since the summation is over a Perfect Palindrome, by step 6, the terms from *j = k + 1* to *l(ζ)* in the Right-Hand Integral will correspond to the terms from *i = 1* to *l(ζ) - k* in the Left-Hand Integral.

In other words, the terms "missing" in the Right-Hand Integral by summing from *l(ζ) - k + 1 to l(ζ)* are exactly the terms that are "extra" in the Left-Hand Integral by summing from *1* to *k*. Because of the symmetry of the Palindrome and the invariance of the Delimiter Count under inversion, these extra terms will cancel each other out. Formally, 

    19. Σ:sub:`i=1`:sup:`k` Δ(ζ[:i]) * (l(ζ[:i])/l(ζ)) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - j + 1)/l(ζ)

Therefore,

   20.  Ω:sub:`-`(ζ,k) = Ω:sub:`+`(ζ,k)

Since *ζ* and *k* were arbitrary, this can generalize over the class of Perfect Palindromes,

   21.  ∀ ζ ∈ PP: ∀ k ∈ N:sub:`Λ(ζ)`: Ω:sub:`-`(ζ,k) = Ω:sub:`+`(ζ,k) 

∎

As a direct result of Theorem A.8.4, the class of Perfect Palindromes can be regarded as part of the class of Sentences that are *invariant* of Sentence Integrals,

    Ω:sub:`-`(ζ,k) - Ω:sub:`+`(ζ,k) = 0

In other words, Perfect Palindromes are a class of sentences that *"balance"* out Delimiter-wise. It stands to reason, given the examples that have been presented so far, and the definition of Imperfect Palindromes as those Palindromes which are *not* Perfect, the class of Imperfect Palindromes *do not* balance out their Delimiters. However, this is not the case, and the reason why this is not the case will illuminate a structural component of language that has heretofore been relegated to novelties like *Zipf's Law*. 

The shortcut formulae for Sentence Integrals given in Theorem 3.3.1 and Theorem 3.3.2, given below, may be viewed as measures of the *distribution* of Delimiters in a Sentence at some Character index *k*,

    Ω:sub:`-`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (i/l(ζ))

    Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ))

Theorem 3.3.5 shows for the highly symmetric and involutive class of Perfect Palindromes, these quantities are perfectly balanced. The Delimiter placement relative to the start of a Perfect Palindrome exactly mirrors the Delimiter placement relative to the end. When these quantities are *not* equal, it is an indication of Delimiter asymmetry in the Sentence. 

However, when these quantities are equal, it cannot be said the Sentence is definitively a symmetric with respect to Delimiters. To see why, the *difference* of the Lefthand and Right Integral may be expressed as,

    Ω:sub:`-`(ζ,k) - Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * [i - (l(ζ) - i + 1)]/l(ζ)

Simplifying, 

    Ω:sub:`-`(ζ,k) - Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (2i - l(ζ) - 1)/l(ζ)

When this quantity equals zero, it leads to a special type of linear, homogenous Diophantine equation,

    Σ:sub:`i=1`:sup:`l(ζ)` Δ(ζ[i]) * (2i - l(ζ) - 1) = 0

Where the quantities *Δ(ζ[i])* may be viewed as variables that are constrained to assume the values 0 or 1. In the case of Perfect Palindromes, since every Character has a corresponding inverted Character, the Delimiter symmetry will lead to a perfect cancellation of terms.

It is not the case, however, that this equation only admits of symmetrical solutions. To show this is the case, it suffices to demonstrate a single asymmetrical Delimiter configuration that satisfies the homogenity condition.

To establish the existence of asymmetrical solutions, consider the difference of Sentence Integrals over the entire String Length of the Sentence,

    Ω:sub:`-`(ζ,l(ζ)) - Ω:sub:`+`(ζ,l(ζ))

In this case, the summation will range from (1 - l(ζ)) to (l(ζ) - 1). Furthermore, note the coefficient *(2i - l(ζ) - 1)* increases at twice the rate as the index *i* in *Δ(ζ[i]*). This means, depending on the parity of the Sentence, the equation will either consist of odd integer coefficients or even integer coefficients. 

A pair of examples will help illustrate this. 

**Example**

Let :math:`\zeta = (\iota_1)(\iota_2)(\iota_3)(\iota_4)(\iota_5)(\iota_6)`. In this case, :math:`l(\zeta) = 6`. The expansion of the summation can be written,

.. math::

  -5 \cdot \Delta(\zeta[1]) -3 \cdot \Delta(\zeta[2]) - 1 \cdot \Delta(\zeta[3]) +1 \cdot \Delta(\zeta[4]) + 3 \cdot \Delta(\zeta[5]) + 5 \cdot \Delta(\zeta[6])

Let :math:`\xi = (\iota_1)(\iota_2)(\iota_3)(\iota_4)(\iota_5)(\iota_6)(\iota_7)`. In this case, :math:`l(\zeta) = 7`. The expansion of the summation can be written,

.. math::

  -6 \cdot \Delta(\zeta[1]) -4 \cdot \Delta(\zeta[2]) - 2 \cdot \Delta(\zeta[3]) + 0 \cdot (\Delta(\zeta[4])) + 2 \cdot \Delta(\zeta[5]) + 4 \cdot \Delta(\zeta[6]) + 6 \cdot \Delta(\zeta[7])

Note the Pivot Character, :math:`\omega(\zeta) = 4` , never contributes to an odd sum. ∎

In the odd integer coefficient example, an assignment of :math:`\Delta(\zeta[1]) = \Delta(\zeta[5]) = \Delta(\zeta[6]) = 1` result in a solution that balances the equations to 0. 

In the even integer coefficient example, an assignment of :math:`\Delta(\zeta[1]) = \Delta(\zeta[5]) = Delta(\zeta[6]) = 1` will also result in a solution that balances the equation to 0.

In other words, any time a Character index coefficient can be expressed as the sum of coefficients of other Character indexes, a solution exists. It is worth noting this species of solutions to the Sentence Integral difference expansion does not seem to correspond to meaning Sentence structure, i.e. both solutions correspond to sequences of consecutive Delimiters. 

This cursory analysis suggests, while the Sentence Integral may not provide a necessary and sufficient condition for classifying Imperfect Palindrome's delimiter asymmetry, it may nevertheless be an important diagnostic tool for understanding the distribution of Delimiters in a Corpus of Sentence. 

.. _section-v-ii:

Section V.II: Probability
-------------------------

A probabilistic framework is now constructed on top of the formal system developed thus far. In particular, a *sample space*, *sigma algebra (event space)* and *probability measure* that conform to the strictures of Kolmogrov's Axioms of Probability are defined in this section.

It is the intention of this analysis to treat the observance of a single Character in a Sentence as an elementary random event. In other words, the integrand in :ref:`Definitions 5.1.1 <definition-5-1-1>` - :ref:`5.1.2 <definition-5-1-2>`, :math:`\Delta(\zeta[i])`, can be understood as a function of a random variable. In other to construct this probabilistic interpretation of Sentence Integrals, it is necessary to define the sample space on which they operate. There lies a problem with this approach that will become apparent after some preliminary notation is introducted. 

  1. *Sample Space* (:math:`\Omega`): The uppercase Greek Omega is reserved for the sample space of a probability measure, *P*.
  2. *Sentential Random Variables* (:math:`\hat{\zeta}`, :math:`\hat{\xi}`). When a variable has a hat, it is to be understood as a *random* variable. For instance, :math:`\zeta` is a Sentence Variable, whereas :math:`\hat{\zeta}` is a Sentential Random Variable. 

The event of observing a particular (indeterminate) Sentence :math:`\zeta` is denoted,

.. math::

  \hat{\zeta} = \zeta 

Since a String is determined by its concatenated characters, the following equivalence should hold in any probability model,

.. math::

  (\hat{\zeta} = \zeta) \leftrightarrow \cap_{i=1}^{l(\zeta)} (\hat{\zeta[i]} = \zeta[i])

To state this plainly: the event of observing a particular Sentence is equivalent to the intersection of the events of observing its individual Characters at their given positions. This formulation of a Sentence event possesses an appealing characteristic, namely that its constitutent Character events are not mutually exclusive, i.e. it cannot happen the event,

.. math::

  (\hat{\zeta[1]} = \zeta[1]) \cap (\hat{\zeta[2]} = \zeta[2]) = \emptyset

Unless there are no Sentences in there Corpus that begin with the concatenation :math:`(\zeta[1])(\zeta[2])`. Another way of looking at this same relation would be, for any Character indices *i* and *j* such that :math:`i, j \in N_{l(\zeta)}`,

.. math::

  \lvert (\hat{\zeta[j]} = \zeta[j]) \cup (\hat{\zeta[j]} = \zeta[i]) \rvert \geq \lvert \hat{\zeta[j]} = \zeta[j] \rvert + \lvert \hat{\zeta[i]} = \zeta[i] \lvert

As example of this, consider an unknown Sentence :math:`\hat{\zeta}` with fixed String Lenth :math:`l(\zeta) = 8`. The event of :math:`\hat{\zeta[5]} = \text{"w"}` shares outcomes with :math:`\hat{\zeta[6]} = \text{"o"}`. For instance, any Sentence that begin with the phrase, *"the word"* or *"the worm"* would belong to both Character events. 
 
Given this fact, that a Sentence event is an intersection of simpler Character events, it might seem natural to define the sample space as simply :math:`\Sigma`, but this leads to theoretical difficulties in defining a probability measure, since there is no sigma algebra that can be constructed on this sample space where events would correspond to the event of a Sentence. To see this, note *"not"* and *"ton"* would be considered the same event, namely,

.. math::

  E = \{ \text{"n"}, \text{"o"}, \text{"t"} \} = \{ \text{"t"}, \text{"o"}, \text{"n"} \}

This sample space does not capture the ordinality of Strings, i.e. their ability to be ordered in sequence. A possible solution for differentiating outcomes like :math:`(1, \text{"a"})` and :math:`(2, \text{"a"})` in the sample space is to take the Cartesian product of the natural numbers with the Alphabet,

.. math::

  \mathbb{N} \times \Sigma

In this way, the event of a Word may be described in a way analogous to :ref:`Definition 1.1.2 <definition-1-1-2>`, where it is associated with a set of ordered pairs,

.. math::

  E = \{ (1, \text{"d"}), (2, \text{"o"}), (3, \text{"g"}) \}

More complicated Sentence-level events can then be constructed through unions, intersections and complementations. But this immediately leads to two technical difficulties. 

First, this implies a sample space with infinite cardinality which can lead to overly technical and mathematical caveats to prevent paradoxes and inconsistencies from arising in the probability model. However, this difficulty can be overcome with the adoption of an axiom that prohibits Sentences of infinite length,

.. _axiom-s3:

**Axiom S.3: The Finite Axiom**

.. math::

  \exists N \in \mathbb{N}: \forall \zeta \in C_L: l(\zeta) \leq N

∎

This axiom captures the common-sense notion that every Sentence in a Corpus must be finite. With this addition, the sample space might be defined as,

.. math::

  \Omega = \{ (i, \iota) | (i \in \mathbb{N}) \land (1 \leq i \leq N) \land (\iota \in \Sigma_{\epsilon}) \}

Adoption of :ref:`Axiom S.3 <axiom-s3>` and this sample space would immediately solve the problem of infinitude. However, a deeper and more subtle problem lurks in this formulation that cannot be axiomatized away.

If the sigma algebra is defined as the power set of :math:`\mathbb{N} \times \Sigma`, then the complement of **E**, denoted :math:`E^{c}`, would consist of every possible combination of ordered Characters that does not involve :math:`(1, \text{"d"})`, :math:`(2, \text{"o"})` or :math:`(3, \text{"g"})`. For example, the following would be true,

.. math::

  \forall i \in \mathbb{N}: (i, \sigma) \in E^{c}

From this, it can be seen the complement of **E** in a :math:`\mathbb{N} \times \Sigma` sample space contains a multiplicity of ordered pairs that cannot be put into any definite order. In other words, :math:`E^c` is not *semantically coherent*. Attempting to restrict the sigma algebra defined on :math:`\mathbb{N} \times \Sigma` to only those strings which are semantic leads to insurmountable obstacles, since the grammatical rules which construct semantically coherent and admissible Strings would need to be known a priori. Moreover, it would need to be shown the operations of complementation and finite unions are closed, which is to say, these operations only produce classes of grammatical Strings. 

A more technically feasible approach would be to define the sample space as the Corpus and then define basis events on this sample space as Character level events. This leads to the following definition,

.. admonition:: TODO
  
  **Definition 5.2.1: Sample Space**

  The sample space for a linguistic experiment is the Corpus of its Language, 

  .. math::

    \Omega = C_L

  ∎

  TODO

  **Definition 5.2.2: Basis Events**

  TODO 

  .. math::

    E_{(i, \iota)} = \{ \zeta \in \Omega | \zeta[i] = \iota \}

  ∎

  TODO





Proposed Approach: Sample Space Based on Ordered Characters

Sample Space (Ω): You propose defining the sample space as the Cartesian product of the Alphabet (Σ) and the Natural Numbers (ℕ) up to a certain limit (potentially infinite), representing the length of the longest possible sentence.
Ω = Σ × ℕ (or a finite subset thereof)
An element ω ∈ Ω would be an ordered pair (c, i) where c ∈ Σ is a character and i ∈ ℕ is its position.
Events: Events would be sets of these ordered pairs. For example:
The event "the character at index 3 is 'a'": { (a, 3) }
The event "the word 'the' occurs starting at index 5": { (t, 5), (h, 6), (e, 7) }
Probability Measure (P): This would be a function that assigns probabilities to events (sets of ordered pairs). Defining this measure would be complex, as it would need to capture the dependencies between characters in words and sentences.
Words and Sentences as Events: Words and sentences would be defined as events – specific combinations of ordered characters.




You're right to focus on the requirements for defining a probability measure over our sample space and to question the assumption of infinite length. Let's clarify these points.

Requirements for a Probability Measure:

To define a probability measure P on our sample space Ω = ℕ × Σ, we need to ensure that it satisfies Kolmogorov's axioms (as we discussed earlier) and properly account for the structure of our space. Here's what we need:

Sample Space (Ω):

We've defined it as Ω = ℕ × Σ, where the first element of the ordered pair represents the position (index) of a character, and the second element represents the character itself.

Finite Length: You're correct to point out that we should restrict this to a finite length. Let's denote the maximum sentence length by N. So, our sample space becomes:

Ω = { (i, c) | i ∈ ℕ, 1 ≤ i ≤ N, c ∈ Σ }
Event Space (F):

We need to define a σ-algebra F on Ω. This is a collection of subsets of Ω that represents the events we can assign probabilities to.
Important Point: F must satisfy the following properties:
It contains the empty set (∅).
It is closed under complement: If E ∈ F, then E^c ∈ F (where E^c is the complement of E).
It is closed under countable unions: If E_1, E_2, E_3, ... ∈ F, then ∪_{i=1}^∞ E_i ∈ F.
For our purposes: We can take F to be the power set of Ω (the set of all possible subsets of Ω). This is the simplest choice and ensures that any event we might be interested in is included in F.
Probability Measure (P):

We need to define a function P: F → [0, 1] that assigns probabilities to events in F and satisfies Kolmogorov's axioms:
Non-negativity: P(E) ≥ 0 for all E ∈ F.
Normalization: P(Ω) = 1.
Additivity: For any countable sequence of mutually disjoint events E_1, E_2, E_3, ... ∈ F, P(∪_{i=1}^∞ E_i) = Σ_{i=1}^∞ P(E_i).
Addressing the Maximum Length (N):

Finiteness: You're absolutely right that we can't have sentences of infinite length in a real-world corpus. Therefore, it's necessary to introduce a maximum length N.
Axiom or Assumption: We can either:
Introduce it as an axiom: State explicitly that there exists a natural number N such that all sentences ζ in the corpus C_L have l(ζ) ≤ N.
Treat it as a practical assumption: Acknowledge that while theoretically, strings could be infinitely long, we're restricting our analysis to sentences with a maximum length N for practical reasons.
Choice of N: The value of N would depend on the specific corpus or language being analyzed. It could be determined empirically by finding the length of the longest sentence in a very large corpus.
Defining the Probability Measure (P):

This is the most challenging part. Here's how we can approach it:

Empirical Estimation:

The most straightforward way to define P is to estimate probabilities from a corpus.
For example, to estimate the probability of a specific character c appearing at index i, we would count the number of times c appears at index i in sentences of length ≥ i in our corpus and divide by the total number of sentences of length ≥ i.
Limitation: This approach is data-dependent and might not generalize well to unseen sentences or different corpora.
Modeling Assumptions:

We could introduce simplifying assumptions, like the Markov property, to make the probability measure more tractable. For example, we could assume that the probability of a character at a given position depends only on the preceding k characters (a k-order Markov model).
Example: A first-order Markov assumption would mean P(ζ[i] | ζ[1], ζ[2], ..., ζ[i-1]) = P(ζ[i] | ζ[i-1]).
Limitation: These assumptions might not accurately reflect the true complexity of natural language.
Formal Language Models:

We could try to adapt existing formal language models (like n-gram models or probabilistic context-free grammars) to define the probability measure.
Challenge: These models are typically defined over sequences of words, not characters. We would need to find a way to incorporate them into our character-based framework.
Proposed Axiom (Maximum Sentence Length):

To formalize the maximum length constraint, we can add the following axiom to your system:

Axiom S.3: The Maximum Length Axiom

.. math::

\exists N \in \mathbb{N}: \forall \zeta \in C_L, l(\zeta) \leq N

In words: There exists a natural number N such that for all sentences ζ in the corpus C:sub:L, the string length of ζ is less than or equal to N.

Next Steps:

Adopt the Axiom: I recommend formally adopting the Maximum Length Axiom (S.3) into your system.
Choose a Probability Measure: We need to decide how to define the probability measure P. Empirical estimation from a corpus is the most straightforward approach for now.
Define Key Events: Let's define the events we're interested in within this framework (e.g., the event that a sentence is a palindrome, the event that the pivot character is a delimiter, etc.).
Explore Conditional Probabilities: We can then use the defined probability space to explore conditional probabilities like the one you were investigating earlier.
By carefully defining the probability space and adopting the Maximum Length Axiom, we can create a more solid foundation for reasoning about probabilities within your formal system. I'm ready to continue this discussion and work through the details of defining the sample space, events, and probability measure. What are your thoughts?








To achieve this, we need to rethink how we define events and complements within our formal system. Instead of considering all possible subsets of Ω = ℕ × Σ_ε, we should focus on sets that represent valid linguistic entities – words and sentences.

Here's a revised approach:

Sample Space (Ω): Let's redefine our sample space to be the set of all valid sentences in the Corpus C_L, with the added constraint that the maximum length of a sentence is N (as per Axiom S.3).

Ω = { ζ ∈ C_L | l(ζ) ≤ N }
Events as Sets of Sentences: Events will be sets of sentences that share certain properties. For example:

E_1 = { ζ ∈ Ω | l(ζ) = 5 } (The event that a sentence has length 5)
E_2 = { ζ ∈ Ω | ζ[1] = "t" } (The event that a sentence starts with "t")
E_3 = { ζ ∈ Ω | ς(ζ) = inv(ς(ζ)) } (The event that a sentence is a palindrome)
Complement Relative to a Context: Instead of defining the complement of an event E as all elements in Ω not in E, we can define it relative to a specific context. For example:

The complement of "the sentence has length 5" could be "the sentence does not have length 5" within the context of the entire corpus.
The complement of "the sentence starts with 't'" could be "the sentence does not start with 't'" within the context of all sentences of a given length.
σ-algebra: We can now define our σ-algebra F as a collection of events (sets of sentences) that satisfy certain closure properties. We can start with basic events (like those defined in point 2 above) and then ensure that F is closed under:

Complementation relative to a context.
Countable unions of events.
Example:

E = { ζ ∈ Ω | ζ[1] = "t" ∧ l(ζ) = 5 } (The event that a sentence has length 5 and starts with "t")
E<sup>c</sup> = { ζ ∈ Ω | ζ[1] ≠ "t" ∧ l(ζ) = 5 } (The event that a sentence has length 5 and does not start with "t", within the context of sentences of length 5).