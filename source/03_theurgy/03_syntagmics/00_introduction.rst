.. _syntagmics-introduction:

Section I: Introduction
=======================

.. epigraph::

    | When Ajax strives, some Rock's vast Weight to throw,
    | The Line too labours, and the Words move slow:

    -- `Essay on Man`_, Alexander Pope

.. _syntagmics-prior-definitions:

Praeparatio
-----------

-----------
Mathematics 
-----------

The sum :math:`\sum` symbol will be borrowed from mathematics and extended over the domain of poetic objects. This would not present a problem if it were not sometimes necessary to use the :math:`\sum` in its mathematical capacity. It will be the convention of the formal system being developed to *overload* the arguments of the :math:`\sum` operation to be defined on numbers as well as syntagmic variables. For that reason, the meaning of the symbol,

.. math::

    \sum_i^n x_i 

Should be attended with the utmost care. When :math:`x_i` is a poetic sign, then the summation will be understood to be the aggregation of signs into a poem. If :math:`x_i` is a number, then the summation will be understood in its usual arithemtical sense. 

-------
Poetics
-------

Given below are existing definitions of poetical devices. 

.. topic:: Definition: Feet
    
    - Iamb: One unstressed syllable followed by a stressed syllable.
    - Spondee: A stressed syllable followed by a stressed syllable. Employed to slow down the pace of a line.
    - Dactyl: A stressed syllable followed by two unstressed syllables. Employed to create a sense of falling or release.
    - Trochee: A stressed syllable folowed by an unstressed syllable. Employed to emphasize urgency or directness.
    - Anapest: Two unstressed syllables followed by a stressed syllable. Employed to create a sense of building momentum.
    - Pyrrhic (Dibrachs): Two unstressed syllables. 
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

Formalization
-------------

The syntagmic hierarchy, in descending order, is given by, 

1. Poems
2. Stanzas
3. Lines 
4. Words
5. Syllables

Each layer is composed of elements from the layer beneath it joined together through operations (to be defined shortly). 

In this formalization, English letters will be used to represent lines, Greek letters will be used to represent words and Coptic letters will be used to represent syllables. 

.. note::

    All symbolic terms will be typeset differently to distinguish them from the level of analysis and definition, and to indicate their nature as "*sentences*" in the language of syntagmics. 

.. _syntagmics-constants:

---------
Constants
---------

1. Uppercase English letters (:math:`A, B, C, ...` ): Fixed lines.
    a. The uppercase English letter :math:`S` is reserved for sets.
2. Uppercase Greek letters (:math:`\mathrm{A}, \mathrm{B}, \Gamma, ...`): Fixed words.
3. Uppercase Coptic letters (:math:`Ⲁ, Ⲃ, Ⲅ, ...`): Fixed syllables.
4. The lowercase English letter n is reserved for natural numbers.
5. The lowercase Fraktur letter :math:`\mathfrak{i}` is reserved for iambs.
6. The lowercase Fraktur letter :math:`\mathfrak{t}` is reserved for trochees.
7. The lowercase Fraktur letter :math:`\mathfrak{s}` is reserved for spondees. 
8. The lowercase Fraktur letter :math:`\mathfrak{a}` is reserved for anapests.
9.  The lowercase Fraktur letter :math:`\mathfrak{d}` is reserved for dactyls.
10. The lowercase Fraktur letter :math:`\mathfrak{p}` is reserved for pyrrchis (dibrachs)
11. The empty set :math:`\varnothing` is reserved for the pause (caesura). 

The caesura deserves special mention. In poetics, a caesura represents a dramatic or structural pause.

.. _syntagmics-variables:

---------
Variables
---------

1. Lowercase English letters (:math:`a, b, c, ...` ): Indeterminate rhymed lines.
    a. The lowercase English letters :math:`u, v, w` are reserved for indeterminate lines, not necessarily rhymed. 
    b. The lowercase English letters :math:`x, y, z` are reserved for general syntagmic variables (syllables, words, lines, stanzas and poems)
2. The lowercase Greek letters (:math:`\alpha, \beta, \gamma`): Indeterminate rhymed words.
    a. The lowercase Greek letter :math:`\kappa, \lambda, \mu` are reserved for indetermine words, not necessarily rhymed.
3. The Coptic letters :math:`ⲣ, ⲡ, Ⲡ` are reserved for indeterminate syllables. Subscripts are often used with syllabic variables to denote different syllables. 
4. The lowercase Fraktur letter :math:`\mathfrak{x}` is reserved for indeterminate meters.
5. The lowercase Fraktur letter :math:`\mathfrak{u}` is reserved for indeterminate speeds.
6. The lowercase Greek letter :math:`\varsigma` is reserved for indeterminate stanzas.
7. The lowercase English letters :math:`p` and :math:`q` are reserved for indeterminate poems. 

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

Note that both :math:`A` and both instances of :math:`a` rhyme in this example. The rhyme structure of a composite sign is encoded through the case of constants and variables. In other words, preemptively using the notation from the next :ref:`section <syntagmics-relations>`, :math:`A \parallel a`, :math:`B \parallel b`, etc.

The intent behind defining :math:`p` and :math:`q` as "*poetic*" variables is to formalize the schema of a certain fixed poetic forms through operations performed on line, word and syllabic variables and constants. "*Poetic*" variables can be seen as the well-formed formulae that emerge through the calculus that governs the lower levels of the syntagmic hierarchy.

.. _syntagmics-relations:

---------
Relations
---------

All syntagmic relations are to be understood as truth values, meaning each expression results in a judgement of truth or falsity. 

.. topic:: Containment

    .. math::

        y \subset_p x

.. important::

    The subscript *p* is used to differentiate containment from the set relation of "*subset*".

If :math:`y subset_p x`, then the sign :math:`y` is said to be "*contained*" in the sign :math:`x`. The relation of "*contains*" extends up the levels of the syntagmic hierarchy, capturing each successive level under its umbrella as it moves up each rung of the ladder,
 
- Words contain syllables
- Lines contain words and syllables
- Stanzas contain lines, words and syllables
 
Consider the line from `Spring and Fall`_ by Gerard Manley Hopkins, 

.. math::

    x = \text{Though worlds of wanwood leafmeal lie}

Then for each word :math:`\lambda` in :math:`\{ \text{Though}, \text{worlds}, ..., \text{lie} \}`,

.. math::

    \lambda \subset_p x

Similarly, for each syllable :math:`\rho` in :math:`\{ \text{Though}, ... \text{wan}, \text{wood}, ... \text{lie} \}`,

.. math::

    \rho \subset_p x

The relations of *pendment* can be defined through containment and concatenation,

.. topic:: Pendment

    x \sim y \equiv [y \subset_p x] \land [\exists w: x = wy]

If :math:`x \sim y`, :math:`y` is said to *append* :math:`x`, or inversely, :math:`x` is said to *prepend* :math:`y`.

The relation of *pendment* will be important when rhymation is defined more thoroughly in :ref:`syntagmics-rhymes` sectoin. For now, this section will close by introducing the symbolic relation of rhymation,

.. topic:: Rhymation

    The sign :math:`x` rhymes with the sign :math:`y`,

    .. math::

        x \parallel y

.. _syntagmics-operations:

----------
Operations
----------

This section introduces the operations of *syntagmics*. These are the verbs of the system. They are used to express syntagmic proposition *within the system*.

In other words, all operations defined in this section are to be understood as *object* level constructs, in contradistinction to :ref:`relations <syntagmics-relations>` like containment or rhymation which are predicated of objects and yield truth-values as a result. All syntagmic operations are to be understood as being closed under the domain of signs, meaning each operation will always yield a sign as a result.

1. **Concatenation** :math:`xy`
2. **Succession** :math:`x.y`
3. **Disjunction** :math:`x:y`
4. **Separation** :math:`x + y`

.. topic:: Provisional Notation 

   1. #x: A lengthened sign. 
   2. ♭x: A shortened sign.  

   Virelais require alternating rhymes to shorten and length across stanzas. The signs "#x" and "♭x" are here provisionally offered as a symbolic way of capturing this form. However, further research needs to be done on the exact syntactical rules of these signs.

Separation vs. Succession 
^^^^^^^^^^^^^^^^^^^^^^^^^

To see what is meant by the distinction between *separation* and *succession*, let :math:`x = \text{the fish in the dish}` and :math:`y = \text{the dog on a jog}`. Then :math:`x.y` means,

    | the fish in the dish
    | the dog on a jog

Where as :math:`x + y` means,

    | the fish in the dish
    | 
    | the dog on a jog

From this, it can be see the operation of *successions* inserts a new line at the end of first line, whereas the operation of *separation* inserts a new line after the first line *and* before the second line, to create a blank line between them. In effect, the operation of *separation* creates stanzas, whereas the operation of *succession* creates lines within stanzas. 

Substitution
^^^^^^^^^^^^

.. topic:: Substitution

    :math:`f(y) |\, y = z` 
    
This is to indicate one should substitute :math:`z` for :math:`y` in the sign :math:`x`, where :math:`f(x)` is a poetic propositional funciton of :math:`y` [#substitution]_.

Algebraic Properties
^^^^^^^^^^^^^^^^^^^^

Brackets, :math:`[]`, are used to group operations within signs by precedence. However, before adopting their use, several properties of the operations of succession and separationg need to be clarified. 

The major difference of syntagmics over other formal language theories is the introduction of separation and succession, which encapsulate aesthetic functions employed by poetical constructions, i.e. the artistic insertion of new lines to create a certain rhythym, prosody or physical appearance. These operations allow a broad scope of poetic phenomena to be formalized. In other words, while the semantic content of the sign is unaltered by these operations, the *poetic*, or *syntagmic*, content of the sign is dramatically affected. 

Syntagmics is based on *noncommutativity*. None of its operations commute, e.g. :math:`x.y \neq y.x` and :math:`x + y \neq y + x`. However, this does not mean a syntagmic algebra cannot be constructed. The following relationship between separation and succession is a direct result of their definition as operations that insert new lines,

.. math::

    x.\varnothing.y = x + y

In essence, placing a caesura between a succession is equivalent to separating those two signs into stanzas. For this reason, either separation or succession may be regarded individually as primitive and the other may be defined in the terms of the one. 

This identity allows the analogue of the *distributive* property of syntagmics to be expressed in terms of the *associative* property of succession,

.. math::
        
    x.[y + z] = x.[y.\varnothing.z]

In other words, in a syntagmic system one can either have *associativity* of succession, i.e. :math:`x.[y.z] = [x.y].z`, or the *distributivity* of succession over separation, i.e. :math:`x.[y + z] = x.y + x.z`, but *not both*. The current system prioritizes the associativity of succession, i.e.

.. math::

    x.[y.z] = [x.y].z

To make this concrete, let :math:`x = \text{cat}`, :math:`y = \text{rat}` and :math:`z = \text{hat}`. Consider the expression :math:`x.[y + z]`. To preserve the associativity of succession, the operation of separation inside of the brackets must be applied first, resulting in the composite sign,

| cat
| rat 
| 
| hat

.. TODO: The caesura may be accumulating too much responsibility here. I am not sure it should be used to represent blank lines.

.. _syntagmics-shorthand:

Shorthand
^^^^^^^^^

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

Examples
^^^^^^^^

**Poetic Expressions**

:math:`a.b.a`
    A tercet where the first and third lines rhyme. 

:math:`A.b.A` 
    A tercet where the first and third lines are the same. 

:math:`a.b.a + a.b.a` 
    Two rhyming tercets.

:math:`a.b.[b:a]`
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

.. _syntagmics-rhymes:

------
Rhymes
------

.. _syntagmics-scope: 

Scope
^^^^^

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

Stress
^^^^^^

In order to express the different categories of rhymes that may be used to aggregates lines into a scheme, notation is introduced to *accent* a sign to indicate its ending stress. 

If a sign has no accent mark, then any type of stress satisfies the sign.

.. note::

    Stress accents can affix both lines :math:`u` and words :math:`\lambda`. They do *not* operate on syllables. 

The accented sign will be referred to as a *rhyme particle*. For instance, :math:`\hat{x}` (to be defined immediately) is a *rhyme particle*. In and of itself, it does not denote a rhyme. It is only in the context of a poetical proposition that it can be said to bear the meaning of a "*rhyme*". By writing :math:`\hat{x}`, all that has been stated is the syllabic form of the sign. In effect, the hat encodes the syllabic form and the vartiable encodes the rhyme scheme. 

1. Masculine Stress

A masculine rhyme occurs when the final syllable in two words is stressed and phonetically identical. For example, the following pairs of words are masculine rhymes, 

- cat, hat
- bright, light
- despair, compare

A hat is used to denote a masculine ending stress,

.. math::

    \hat{x} \equiv \exists Ⲡ: x \sim Ⲡ

2. Feminine Stress
   
A feminine rhyme occurs when the final syllable in two words is unstressed and phonetically identical. For example, the following pairs of words are feminine rhymes,
   
- mother, another
- flowing, going

A check is used to denote a feminine ending stress,

.. math::

    \check{x} \equiv \exists Ⲡ,ⲡ: x \sim Ⲡⲡ

3. Dactylic Stress

A dactylic rhyme occurs when two words ends in identical dactyls. For example, the following pairs of words are dactylic rhymes, 

- happily, snappily
- tenderness, slenderness

A dot is used to denote a dactylic ending stress, 

.. math::

    \dot{x} \equiv \exists Ⲡ, {ⲡ_1}, {ⲡ_2}: x \sim Ⲡ{ⲡ_1}{ⲡ_2}

4. Off Stress

An off rhyme involves imperfect sound correspondence (assonance, consonance, etc.). For example, the following pairs are off rhymes, 

- bottle, fiddle (syllabic rhyme)
- hammer, carpenter (weak rhyme)

A tilde is used to denote an off stress, 

.. math::

    \tilde{x} \equiv [ ... ]

Where "..." represents as yet undetermined operation.

.. note:: 

    Because off-rhymes do not (yet) have a syllabic representation, they are only used *within* poetical proposition to denote a rhyme. Writing :math:`\tilde{x}` has no meaning outside of the poetical proposition, unlike the other forms of rhymes which represent definite syllabic configurations of ending stress. 

**Shorthand**

To avoid unnecessary complexity, the following notations are defined. In the case of masculine rhyme particles,

.. math::

    \hat{x.y} = \hat{x}.\hat{y} 

.. math::

    \hat{x + y} = \hat{x} + \hat{y}

.. math::

    \hat{x:y} = \hat{x}:\hat{y}

Similarly for the other types of rhyme particles. 

Logical Structure
^^^^^^^^^^^^^^^^^

Now that notation has been introduced to formalize rhyme structure in a poem, the relation of *rhymation* can be clarified. Rhymation is meant to explicate the relation of "*perfect rhymes*" within the formal system being developing.

It should first be noted, by :ref:`definition <syntagmics-variables>`, that all signs rhyme with themselves,

.. math::

    x \parallel x

Furthermore, if an arbitary sign :math:`x` rhymes with the sign :math:`y`, then :math:`y` rhymes with :math:`x`, and visa versa,

.. math::

    x \parallel y \equiv y \parallel x

If two arbitrary signs :math:`x` and :math:`y` end in the same masculine particle, :math:`z`, then they rhyme,

.. math::

    [[x \sim \hat{z}] \land [y \sim \hat{z}]] \implies x \parallel y

If two arbitrary signs :math:`x` and :math:`y` end in the same feminine particle, :math:`z`, then they rhyme,

.. math::

    [[x \sim \check{z}] \land [y \sim \check{z}]] \implies x \parallel y

If two arbitary signs end in the same dactylic particle, then they rhyme, 

.. math::

    [[x \sim \dot{z}] \land [y \sim \dot{z}]] \implies x \parallel y

However, off-rhymes do *not* imply the relation of *rhymation*.

If the secondary relations are defined, 

- :math:`\vdash`, Masculine Rhyme: :math:`x \vdash y \equiv [[x \sim \hat{z}] \land [y \sim \hat{z}]]`
- :math:`\Vdash`, Feminine Rhyme: :math:`x \Vdash y \equiv [[x \sim \check{z}] \land [y \sim \check{z}]]`
- :math:`\Vvdash`, Dactylic Rhyme: :math:`x \Vvdash y \equiv  [[x \sim \dot{z}] \land [y \sim \dot{z}]]`

Then, the relation of *rhymation* can be defined precisely as, 

.. math::

    x \parallel y \equiv [x [ \vdash \lor \Vdash  \lor \Vvdash ] y]

Where the righthand logical sum, :math:`[ \vdash \lor \Vdash  \lor \Vvdash ]`, is shorthand for one of the three relations obtaining between :math:`x` and :math:`y`.

.. _syntagmics-meter:

-----
Meter
-----

:math:`\mathfrak{i} = ⲡⲠ`
    The definition of an **iamb**

:math:`\mathfrak{t} = Ⲡⲡ`
    The definition of a **trochee**

:math:`\mathfrak{s} = ⲠⲠ`
    The definition of a **spondee**

:math:`\mathfrak{p} = ⲡⲡ`
    The definition of a **pyrrhic**
    
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

Lengths
^^^^^^^

A poetic sign has many different notions of "*length*" beyond the purely linguistic lengths of a sentence. A sentence, as it is conceived in the fields of formal linguistic, can be broken into sequences of characters, words or phonemes (among other categorizations). A poetic sign possesses these notions of length as a result of its embodiment in the medium of language, but it also possesses dimensions of length over and above the lengths prescribed by syntax, semantics and pragmatics. These concepts of length are derived from the structure of poetic signs and represent a space orthogonal to conventional formal linguistics where the semantics of poems are encoded. These different, but interrelated notions of length, are listed directly below and then defined,

- Stanza Length of a Poem 
- Line Length of a Poem
- Line Length of a Stanza
- Syllable Length of a Line
- Syllable Length of a Stanza
- Syllable Length of a Poem

**Primitive Lengths**

"*Primitive*" lengths are the immediately measureable quantities of a poem. 

.. topic:: Stanza Length of a Poem

    Let :math:`p` be an arbitrary poem with stanzas :math:`\varsigma_i`. The stanza length of poem :math:`p`, denoted :math:`l(p \mid \varsigma)`, is the natural number :math:`n` that satisfies, 

    .. math::

        l(p \mid \varsigma) = n \equiv p = \sum_1^n \varsigma_i

.. topic:: Line Length of a Stanza

    Let :math:`\varsigma` be an arbitrary stanza with lines :math:`u`. The line length of :math:`\varsigma`, denoted :math:`l(\varsigma \mid u)`, is the natural number :math:`n` that satisfies, 

    .. math::

        l(\varsigma \mid u) = n  \equiv \varsigma = u^n

.. topic:: Syllable Length of a Line

    Let :math:`u` be an arbitrary line with syllables :math:`\rho_i`. The syllable length of :math:`u`, denoted :math:`l(u \mid \rho)`, is the natural number :math:`n` that satisfies, 

    .. math::

        l(u \mid \rho) = n \equiv u = \prod_1^n \rho_i

In effect, the stanza length of a poem is defined as the number times the operation of separation has been applied to stanzas to create a poem, the line length of a stanza is defined as the number of times succession has been applied to lines to construct a stanza, the syllable length is the number of times concatenation has been applied to the syllables to construct a line.

.. note::

    The definition of a length in a level of the syntagmic hierarchy is given in terms of the level directly below it. 

The notation, :math:`l(p \mid \varsigma)`, :math:`l(\varsigma \mid u)` and :math:`l(u \mid \rho)` is meant to invoke the concept of "*conditioning*" from Bayesian analysis. Each type of length is relative to the particular formal term within a syntagmic sign that falls to the right the :math:`\mid` marker. 

**Derivative Lengths**

There are several other concepts of length that are derived directly from these definitions, illustrating how these "*basic*" units of syntagmic length interconnect to form more abstract notions of length. 

.. topic:: Line Length of a Poem 

    Let :math:`p` be an arbitrary poem with stanzas :math:`\varsigma_i`. Let each :math:`\varsigma_i` have lines :math:`u_j`. The line length of :math:`p`, denoted :math:`l(p \mid u)` is defined as,

    .. math::

        l(p \mid u) = \sum_1^{l(p \mid \varsigma)} l(\varsigma \mid u)

.. important::

    :math:`l(\varsigma \mid u)` is a number! Therefore, the :math:`\sum` that appears in the previous definition is an *arithmetical* sum. Recall the :math:`\sum` symbol is overloaded. It may be benefit the reader to treat the preceding as a definition in the metalanguage of syntagmics, rather than its object language, where the :math:`\sum` symbol is used as a semantic construct. 

This definition captures the common sense notion that the number of lines in a poem is equal to the sum of the number of lines in each stanza. 

.. topic:: Syllable Length of a Stanza 

    Let :math:`\varsigma` be an arbitrary stanza. Let each :math:`\varsigma` have lines :math:`u_i`. Let each line :math:`u_i` have syllables :math:`\rho_j`. The syllable length of :math:`\varsigma`, denoted :math:`l(\varsigma \mid \rho)` is defined as,

    .. math::

        l(\varsigma \mid \rho) = \sum_1^{l(\varsigma \mid u)} l(u_j \mid \rho)

Once again, this captures the idea the number of syllables in a stanza is equal to the sum of the number of syllables in each line of the stanza.

There are two ways to define the syllable length of a poem. It can either be defined using the line length of a poem and syllable length of a line, or it can be defined using the stanza length of a poem and the syllable length of a stanza. Whichever definition is selected, the alternative not selected will become a theorem of the formal system as a consequence of the definitions of length. For the current purposes, the first alternative is selected.

.. topic:: Syllable Length of a Poem

    Let :math:`p` be an arbitrary poem with stanzas :math:`\varsigma_i`. Let each :math:`\varsigma_i` have lines :math:`u_j`.  Let each line :math:`u_j` have syllables :math:`\rho_k` The syllable length of :math:`p`, denoted :math:`l(p \mid \rho)` is defined as,

    .. math::

        l(p \mid \rho) = \sum_1^{l(p \mid u)} l(u \mid \rho)

In the previous three definition, the "*condition*" of the summation limit becomes the summand's length, while the "*condition*" of the summand becomes the "*condition*" of the result. This is directly analogous to dimensional analysis in fields of science, where the units of two quantities must cancel out in order for the result to be unitless. This can be viewed a type of a "*poetic dimensional analysis*".

Speed
^^^^^

This document opened with a quote by Alexander Pope that illustrates a phonological phenomenon that is often employed poetically for effect: sentences with clusters of stressed syllables in sequence have the psychological effect of appearing "*slow*", as opposed to anapestic or dactylic rhythms which are often associated with "*galloping*" or "*rapid*" paces. In other words, there is a correlation between the perceived "*speed*" of a poem and its use syllabic stresses. 

The notion of *syntagmic speed* is intended to explicate the psychological phenomenon illustrated by Pope and make it conducive to analysis. In making this definition, an important tool for the statistical analysis of poems will be introduced as a result.

First note that syllables are either stressed or unstressed, but not both. Therefore, the total number of syllables in a sign :math:`x` is equal to the number of unstressed syllables :math:`ⲡ` in :math:`x` plus the number of stressed syllables :math:`Ⲡ` in :math:`x`. Introducing the following notation,

- :math:`l(x \mid Ⲡ)`: The number of stressed syllables in sign :math:`x`
- :math:`l(x \mid ⲡ)`: The number of unstressed syllables in sign :math:`x`

It follows logically from the definitions of syllabic length,

.. math::

    l(x \mid \rho) = l(x \mid Ⲡ) + l(x \mid ⲡ)

With this in mind, the notion of "*poetic speed*" is formally defined as the "*density*" of stressed syllables in a sign.

.. topic:: Speed

    Let :math:`x` be a syntagmic sign such that :math:`l(x \mid \rho) > 0`. The speed of :math:`x`, denoted :math:`\mathfrak{u}(x)`, is defined as,

    .. math::

        \mathfrak{u}(x) = \frac{l(x \mid \rho)}{l(x \mid Ⲡ)}

.. TODO: This definition assumes all lines must possess at least one stressed syllable. Before refining this definition, however, it would probably be beneficial to elaborate on how the stress of a caesura is to be interpretted in the system.

.. [#substitution] A precise definition of a *poetic propositional function* has not yet been given, but it is to be understood in the sense of a truth function, e.g. :math:`\forall p, q, f: ((p \equiv q) \land f(p)) \implies f(q)`