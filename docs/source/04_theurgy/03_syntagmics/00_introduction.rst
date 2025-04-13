
.. _syntagmics-introduction:

Introduction
============

.. epigraph::

    | When Ajax strives, some Rock's vast Weight to throw,
    | The Line too labours, and the Words move slow:

    -- `Essay on Man`_, Alexander Pope

.. _syntagmics-prior-definitions:

-----------------
Prior Definitions
-----------------

Given below are existing definitions of poetical devices. 

.. topic:: Definition: Feet
    
    - Iamb: One unstressed syllable followed by a stressed syllable.
    - Spondee: A stressed syllable followed by a stressed syllable. Employed to slow down the pace of a line.
    - Dactyl: A stressed syllable followed by two unstressed syllables. Employed to create a sense of falling or release.
    - Trochee: A stressed syllable folowed by an unstressed syllable. Employed to emphasize urgency or directness.
    - Anapest: Two unstressed syllables followed by a stressed syllable. Employed to create a sense of building momentum.
    - Pyrrchic: Two unstressed syllables. 
    - Amphibrach: An unstressed syllable followed by a stressed syllable and then another unstressed syllable.
    - Bacchius: An unstressed syllable followed by two stressed syllables. 
    - Antibacchius: Two stressed syllables followed by an unstressed syllable.

.. topic:: Definition: Lines

    - Dimeter: A line with two feet.
    - Trimeter: A line with three feet.
    - Tetrameter: A line with four feet.
    - Pentameter: A line with five feet.
    - Hexmeter: A line with six feet.
    - Heptameter: A line with seven feet.
    - Octameter: A line with eight feet. 
    - Hendecasyllable: A line consisting of eleven syllables. 

.. topic:: Definitions: Stanzas

    - Couplet: A stanza with two lines.
    - Tercet: A stanza with three lines
    - Quatrain: A stanza with four lines
    - Cinquain: A stanza with five lines
    - Sestet: A stanza with six lines.
    - Septet: A stanza with seven lines.
    - Octet: A stanza with eight lines.
    - Nonet: A stanza with nine lines.
    - Decastich: A stanza with ten lines.
    - Envoi: A short, concluding stanza.

.. _syntagmics-formalization:

-------------
Formalization
-------------

.. _syntagmics-constants:

Constants
---------

1. Uppercase English letters (A, B, C, ... ): Fixed lines.
2. Uppercase Greek letters (:math:`\mathrm{A}, \mathrm{B}, \Gamma, ...`): Fixed words.
3. Uppercase Coptic letters (:math:`Ⲁ, Ⲃ, Ⲅ, ...`): Fixed syllables.
4. The lowercase English letter n is reserved for natural numbers.
5. The lowercase Fraktur letter :math:`\mathfrak{i}` is reserved for iambs.
6. The lowercase Fraktur letter :math:`\mathfrak{t}` is reserved for trochees.
7. The lowercase Fraktur letter :math:`\mathfrak{s}` is reserved for spondees. 
8. The lowercase Fraktur letter :math:`\mathfrak{a}` is reserved for anapests.
9.  The lowercase Fraktur letter :math:`\mathfrak{d}` is reserved for dactyls.
10. The empty set :math:`\varnothing` is reserved for the pause (caesura). 
11. The ampersand & represents blank newlines. 

.. _syntagmics-variables:

Variables
---------

1. Lowercase English letters (a, b, c, ... ): Indeterminate rhymed lines.
    a. The lowercase English letters u, v, w are reserved for indeterminate lines, not necessarily rhymed. 
    b. The lowercase English letters x and y are reserved for general syntagmic variables (syllables, words, lines, stanzas and poems)
2. The lowercase Greek letters (:math:`\alpha, \beta, \gamma`): Indeterminate rhymed words.
    a. The lowercase Greek letter :math:`\kappa, \lambda, \mu` are reserved for indetermine words, not necessarily rhymed.
3. The Coptic letters :math:`ⲣ, ⲡ, Ⲡ` are reserved for indeterminate syllables. Subscripts are often used with syllabic variables to denote different syllables. 
4. The lowercase Fraktur letter :math:`\mathfrak{x}` is reserved for indeterminate meters.
5. The lowercase Greek letter :math:`\varsigma` is reserved for indeterminate stanzas.
6. The lowercase English letters p and q are reserved for indeterminate poems. 

.. important::

    Upper English letters are meant to denote particular lines, whereas lowercase English letters are meant to denote indeterminate lines that are related through their rhyme scheme. 

.. note::

    The choice of :math:`ⲡ` and :math:`Ⲡ` to represent syllables mirrors the unstressed and stressed syllables of verses. In other words, :math:`ⲡ` is meant to represent indeterminate unstressed syllables, whereas :math:`Ⲡ` is meant to represent indeterminate stressed syllables. :math:`ⲣ` is used in a more general capacity, to represent stressed or unstressed syllables.

The variables will sometimes be referred to as *syntagmic variables*, or *signs*. 

Uppercase-lowercase pairs of English letters are understood to be rhymes. The difference in the symbolism is the *fixed* nature of the denotation. For example, the sign :math:`A.a.a.A` denotes one fixed line, a rhyming couplet and then the fixed line again,

    | The cat on the mat
    | Got large and fat
    | So-and-so such that 
    | The cat on the mat

The intent behind defining p and q as "*poetic*" variables is to formalize the schema of a certain fixed poetic forms through operations performed on line, word and syllabic variables. "*Poetic*" variables can be seen as the well-formed formulae that emerge through the calculus that governs the lower levels of the syntagmic hierarchy.

.. _syntagmics-relations:

Relations
---------

All syntagmic relations are to be understood as truth values, meaning each expression results in a judgement of truth or falsity. 

1. :math:`x \subset y` (**Containment**): The sign x is contained in the sign y. 

The relation of containment extends up the levels of the syntagmic hierarchy, capturing each successive level under its umbrella as it moves up each rung of the ladder,
 
- Words contain syllables
- Lines contain words and syllables
- Stanzas contain lines, words and syllables
 
.. _syntagmics-operations:

Operations
----------

This section introduces the primitive operations of *syntagimcs*. 

All syntagmic operations are to be understood as being closed under the domain of signs, meaning each operation will always yield a sign as a result.

1. :math:`x.y` (**Succession**): Successive signs.
2. :math:`xy` (**Concatenation**): Concatenated signs.
3. :math:`x:y` (**Delimitation**): Delimited signs.
4. :math:`x \cup y` (**Disjunction**): A sign that is either x or y.
5. :math:`x + y` (**Separation**): Separated signs.
6. :math:`x \cdot y` (**Projection**) : Sign containing sign. 
7. :math:`x(y)` (**Appendment**): A sign ending in a word.  
8. :math:`(y)x` (**Prependment**): A sign beginning with a word. 
9.  :math:`x.y.x | x = z` (**Substitution**): Substitute z for x in the sign :math:`x.y.x`

Brackets, [], are used to group operations within signs by precedence.

To see what is meant by the distinction between *separation* and *succession*, let :math:`x = \text{the fish in the dish}` and :math:`y = \text{the dog on a jog}`. Then :math:`x.y` means,

    | the fish in the dish
    | the dog on a jog

Where as :math:`x + y` means,

    | the fish in the dish
    | 
    | the dog on a jog

From this, it can be see the operation of *successions* inserts a new line at the end of first line, whereas the operation of *separation* inserts a new line after the first line *and* before the second line, to create a blank line between them. In effect, the operation of *separation* creates stanzas, whereas the operation of *succession* creates lines. 

.. important::

    The operation of *projection* is a sign. The relation of *containment* is a truth value.

Note :math:`y = \text{cat}` prepends :math:`x = \text{cat on a mat}`, where as :math:`z = \text{mat}` appends :math:`x`. These operations are related logically to the more general operation of projection. If a sign prepends or appends another sign, it also projects that sign. 

However, projection does not imply prependment or amendment. For example :math:`t = \text{on}` projects :math:`x`, but it does not prepend or amend it. 

Mathematically,

.. math::

    x(y) \implies [x \cdot y]

And,

    (y)x \implies [x \cdot y]

Or more succinctly,

    [x(y) \lor (y)x] \implies (x \cdot y)

Importantly, the converse of this does not hold.

**Provisional Notation**

1. #x: A lengthened sign. 
2. ♭x: A shortened sign.  

Virelais require alternating rhymes to shorten and length across stanzas. The signs "#x" and "♭x" are here provisionally offered as a symbolic way of capturing this form. However, further research needs to be done on the exact syntactical rules of these signs. 

.. _syntagmics-shorthand:

Shorthand
---------

Shorthand notation is introduced in this section to extend the primitive operations defined in the previous seciton.

1. **Summation**: The connotation of the :math:`+` symbol is leveraged to extend the symbolism to the :math:`\sum` symbol. Consider,

.. math::

    \sum_1^{n} {a_i}{b_i}{a_i} = a_1.b_1.a_1 + a_2.b_2.a_2 + ... a_n.b_n.a_n 

This example shows how to represent a poem of arbitrary length composed of tercet stanzas where the first and third lines rhyme. 

2. **Serialization**: A *serialization* (serialized concatenation) is used in reference to syllables. It simply means the concatenation of a patterned sequence of syllables. Consider,

.. math::

    \prod_{i=1}^{n} {ⲡ_i}{Ⲡ_i} = {ⲡ_i}{Ⲡ_i}{ⲡ_i}{Ⲡ_i} ... {ⲡ_n}{Ⲡ_n}

This example shows how to represent a line of iambic meter, i.e. sequences of unstressed and then stressed syllables. 

3. **Exponentiation**: An exponent is used as shorthand for excessive succession of rhymes. For example, consider the lines, 

| the ball in the bag
| the rip in the rag
| the gig in the gag 
| 
| some dittery dots
| some jittery jots
| these simmering sots. 

This can be represented using the operation of *succession* and the operation of *separation* with the expression, 

.. math::

    p = a.a.a + b.b.b

*Exponentation* is used to denote iterated *succession*. The exponent of a line denotes the numbers of times the rhyme appears. The current example can be expressed,

.. math::

    p = a^3 + b^3

.. _syntagmics-delimitation:

4. **Delimitation**: A *delimitation* is mainly used in reference to words or syllables, and can be seen as a shorthand for excessive concatenation. *Delimitation* denotes the insertion of *pauses* (delimiters) in between signs,

.. math::

    Ⲁ:Ⲃ:Ⲅ = Ⲁ∅Ⲃ∅Ⲅ

.. _syntagmics-scope:

Scope
-----

The *scope* of a rhyme is denoted with a bar. Any line variable of the same character that feels under the scope of a bar rhymes, whereas the same variable used outside of the scope of the bar is not required to rhyme with the variable under the bar. An example will help clear this up. Consider the differences that separate the two poetical propositions, :math:`p` and :math:`q`,

.. math::

   p = \overline{a.b.a} + \overline{a.b.a}

.. math::

   q = \overline{a.b.a + a.b.a}

In the case of *p*, the line variable *a* in the first stanza is not required to rhyme with the line variable *a* in the second stanza. In the case of *q*, the line variable *a* in both the first and second stanza must rhyme. For example, the following values of *p* and *q* satisfy these definitions. For *p*,

    | the dog is brown 
    | the cat is green.
    | the fish does drown. 
    |
    | the dog is blue. 
    | the cat is red. 
    | the fish eats you. 

Whereas for *q*,

    | the dog is brown 
    | the cat is green 
    | the fish does drown
    |
    | the dog does frown.
    | the cat is mean. 
    | the fish gets down. 

If the bar is omitted from a sign, it is implied to extend over the entire proposition.

Examples
--------

**Primitive Operations**

:math:`a.b.a`
    A tercet where the first and third lines rhyme. 

:math:`A.b.A` 
    A tercet where the first and third lines are the same. 

:math:`a.b.a + a.b.a` 
    Two rhyming tercets.

:math:`a.b.[b \cup a]`
    A tercet where the last line rhymes with either the first line or the second line.

**Examples**

To make clear how shorthand can be leveraged to concisely represent a poetic scheme, some examples are given below.


1. Consider the following poem,

| pippity pop
| slippity slop
|
| yippity yap
| kippity cap 

This expression can be represented using primitive operations as,

.. math::
    
    p = a.a + b.b

Using :ref:`exponentiation <syntagmics-shorthand>`,

.. math::

    p = a^2 + b^2

Keeping in mind the definition of :ref:`syntagmics-scope` and applying a :ref:`summation <syntagmics-shorthand>`, this can be further reduced,

.. math::

    p = \sum_1^2 \overline{a^2}

In general, an arbitrary number of rhyming couplets can be represented,

.. math::

    p = \sum_1^n \overline{a^2}

.. _syntagmics-meter:

Meter
-----

:math:`\mathfrak{i} = ⲡⲠ`
    The definition of an **iamb**

:math:`\mathfrak{t} = Ⲡⲡ`
    The definition of a **trochee**

:math:`\mathfrak{s} = ⲠⲠ`
    The definition of a **spondee**

:math:`\mathfrak{d} = Ⲡⲡⲡ`
    The definition of **dactyl**

:math:`\mathfrak{a} = ⲡⲡⲠ`
    The definition of a **anapest**

.. topic:: Definition: Meters

    :math:`a/\mathfrak{x}_n` denotes a line in :math:`\mathfrak{x}` n-meter. 

For example, 

.. math::

    (a/\mathfrak{i}_4).(b/\mathfrak{i}_3).(a/\mathfrak{i}_4)

Refers to a tercet where the first and third line are written in iambic tetrameter, whereas the second line is written in iambic trimeter. In other words,

.. math::

    (a/\mathfrak{i}_4) = {\pi_1}{\Pi_1}{\pi_2}{\Pi_2}{\pi_3}{\Pi_3}{\pi_4}{\Pi_4}

Note in this example the first and third line rhyme. 
The scope of a meter extends to everything contained in the parenthesis it marks. For example,

.. math::

    (a.a/\mathfrak{i}_4)

Denotes a rhyming couplet where each line is written in iambic tetrameter. 

Rhyme
-----

In order to express the different categories of rhymes that may be used to aggregates lines into a scheme, notation is introduced to *accent* sign. 

If a sign has no accent mark, then any type of rhyme satisfies the sign.

.. note::

    Rhyme accents can operate one both lines *u* and words :math:`\alpha`.

1. Masculine Rhymes

A masculine rhyme occurs when the final syllable in two words is stressed and identical phonetically. For example, the following pairs of words are masculine rhymes, 

- cat, hat
- bright, light
- despair, compare

A hat is used to denote a masculine rhyme,

.. math::

    \hat{a} = a(Ⲡ)

2. Feminine Rhymes
   
A feminine rhyme occurs when the final syllable in two words is unstressed and identically phonetically. For example, the following pairs of words are feminine rhymes,
   
- mother, another
- flowing, going

A check is used to denote a feminine rhyme,

.. math::

    \check{a} = a(Ⲡⲡ)

1. Dactylic Rhyme

A dactylic rhyme occurs when two words ends in identical dactyls. For example, the following pairs of words are dactylic rhymes, 

- happily, snappily
- tenderness, slenderness

A dot is used to denote a dactylic rhyme, 

.. math::

    \dot{a} = a(Ⲡⲡⲡ)

4. Off Rhyme

An off rhyme involves imperfect sound correspondence (assonance, consonance, etc.). For example, the following pairs are off rhymes, 

- bottle, fiddle (syllabic rhyme)
- hammer, carpenter (weak rhyme)

A tilde is used to denote an off rhyme, 

.. math::

    \tilde{a} = [ ... ]

Where "..." represents as yet undetermined operation.