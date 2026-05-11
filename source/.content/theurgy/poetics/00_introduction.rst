.. _poetics-introduction:

Section I: Introduction
=======================

.. epigraph::

    | When Ajax strives, some Rock's vast Weight to throw,
    | The Line too labours, and the Words move slow:

    -- `Essay on Man`_, Alexander Pope

.. _poetics-praeparatio:

Praeparatio
-----------

The sum :math:`\sum` symbol will be borrowed from mathematics and extended over the domain of poetic objects. This would not present a problem if it were not sometimes necessary to use the :math:`\sum` in its mathematical capacity. It will be the convention of the formal system being developed to *overload* the arguments of the :math:`\sum` operation to be defined on numbers as well as poetic variables. For that reason, the meaning of the symbol,

.. math::

    \sum_i^n x_i 

Should be attended with the utmost care. When :math:`x_i` is a poetic sign, then the summation will be understood to be the aggregation of signs into a poem. If :math:`x_i` is a number, then the summation will be understood in its usual arithemtical sense. 

.. _poetics-formalization:

Formalization
-------------

The poetic hierarchy, in descending order, is given by, 

1. Poems
2. Stanzas
3. Lines 
4. Words
5. Syllables

Each layer is composed of elements from the layer beneath it joined together through operations (to be defined shortly). 

In this formalization, English letters will be used to represent lines, Greek letters will be used to represent words and Coptic letters will be used to represent syllables. 

.. _poetics-constants:

---------
Constants
---------

1. Uppercase English letters (:math:`A, B, C, ...` ): Fixed lines.
    a. The uppercase English letter :math:`S` is reserved for sets.
2. Uppercase Greek letters (:math:`\mathrm{A}, \mathrm{B}, \Gamma, ...`): Fixed words.
3. Uppercase Coptic letters (:math:`Ⲁ, Ⲃ, Ⲅ, ...`): Fixed syllables.
4. The lowercase Fraktur letters (:math:`\mathfrak{a}, \mathfrak{b}, \mathfrak{c}, ...`) are reserved for meters.
5. The empty set :math:`\varnothing` is reserved for the pause (caesura). 

.. _poetics-variables:

---------
Variables
---------

1. Lowercase English letters (:math:`a, b, c, ...` ): Indeterminate rhymed lines.
    a. The lowercase English letters :math:`u, v, w` are reserved for indeterminate lines, not necessarily rhymed. 
    b. The lowercase English letters :math:`x, y, z` are reserved for general poetic variables (syllables, words, lines, stanzas and poems)
    c. The lowercase English letter :math:`i, j, k, n, m` are reserved for natural numbers.
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

The variables will sometimes be referred to as *poetic variables*, or *signs*. 

Uppercase-lowercase pairs of English letters are understood to be rhymes. The difference in the symbolism is the *fixed* nature of the denotation. For example, the sign :math:`A.a.a.A` denotes one fixed line, a rhyming couplet and then the fixed line again,

    | The cat on the mat
    | Got large and fat
    | So-and-so such that 
    | The cat on the mat

Note that both :math:`A` and both instances of :math:`a` rhyme in this example. The rhyme structure of a composite sign is encoded through the case of constants and variables. In other words, preemptively using the notation from the next :ref:`section <poetics-relations>`, :math:`A \parallel a`, :math:`B \parallel b`, etc.

The intent behind defining :math:`p` and :math:`q` as "*poetic*" variables is to formalize the schema of a certain fixed poetic forms through operations performed on line, word and syllabic variables and constants. "*Poetic*" variables can be seen as the well-formed formulae that emerge through the calculus that governs the lower levels of the poetic hierarchy.

.. _poetics-relations:

---------
Relations
---------

All poetic relations are to be understood as truth values, meaning each expression results in a judgement of truth or falsity. 

Containment
^^^^^^^^^^^

.. topic:: Containment

    .. math::

        y \subset_p x

.. important::

    The subscript *p* is used to differentiate containment from the set relation of "*subset*".

If :math:`y \subset_p x`, then the sign :math:`y` is said to be "*contained*" in the sign :math:`x`. The relation of "*contains*" extends up the levels of the poetic hierarchy, capturing each successive level under its umbrella as it moves up each rung of the ladder,
 
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

Pendment
^^^^^^^^

The relations of *pendment* can be defined through concatenation,

.. topic:: Pendment

    .. math::

        x \sim y \equiv \exists w: x = wy

If :math:`x \sim y`, :math:`y` is said to *append* :math:`x`, or inversely, :math:`x` is said to *prepend* :math:`y`.

The relation of *pendment* will be important when rhymation is defined more thoroughly in :ref:`poetics-rhymation`. 

Rhymation
^^^^^^^^^

Refer to :ref:`Rhymation <poetics-rhymation>` for a more thorough definition of *rhymation*.

.. topic:: Rhymation

    The sign :math:`x` rhymes with the sign :math:`y`,

    .. math::

        x \parallel y

Chirality
^^^^^^^^^

Refer to :ref:`poetics-chirality` for a more thorough definition of *chirality*.

.. topic:: Chirality
    
    The sign :math:`x` is the chiamus of sign :math:`y`,

    .. math::

        x \bowtie y

.. _poetics-operations:

----------
Operations
----------

This section introduces the operations of *poetics*. These are the "*verbs*" of the system. They are used to express poetic proposition *within the system*.

In other words, all operations defined in this section are to be understood as *object* level constructs, in contradistinction to :ref:`relations <poetics-relations>` like containment or rhymation, which are predicated of objects and yield truth-values as a result. All poetic operations are to be understood as being closed under the domain of signs, meaning each operation will always yield a sign as a result.

1. **Concatenation** :math:`xy`
2. **Succession** :math:`x.y`
3. **Separation** :math:`x + y`

*Concatenation* is the familiar string operation known in computer science, the theory of automata and regular expressions, as well as formal langauge theory. *Succession* and *separation* are new operations peculiar to the field of *poetics* (though not unknown in computer science) that deal with the formation of *new lines*.

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

Caesuras
^^^^^^^^

The caesura deserves special mention, due to a formal role in the system that is analogous to an arithmetical constant like :math:`0` or :math:`1`. The caesura will be used to specify the identities and properties of the poetic algebra being constructed.

In poetics, a caesura represents a dramatic or structural pause. In poetics, it possesses the same meaning but also possesses other dimensions that need to be considered. The essential function of caesura to represent a pause within a line is represented through concatenation,

.. math::

    x{\varnothing}y

The *null* content of the pause is concatenated between the two signs. Since caesuras represent *null* content, they can also be used to represent blank lines. For example, 

.. math::

    X.y.\varnothing.X.z

can be interpretted as two couplets where the first line is repeated. This dual role of caesuras will be employed in the next section to elaborate the algebraic properties of poetics. 

Algebraic Properties
^^^^^^^^^^^^^^^^^^^^

Brackets, :math:`[]`, are used to group operations by precedence. However, before adopting their use, several properties of the operations of succession and separationg need to be clarified. 

The major difference of poetics over other formal language theories is the introduction of separation and succession, which encapsulate aesthetic functions employed by poetical constructions, i.e. the artistic insertion of new lines to create a certain rhythym, prosody or physical appearance. These operations allow a broad scope of poetic phenomena to be formalized. In other words, while the semantic content of the sign is unaltered by these operations, the *poetic*, or *poetic*, content of the sign is dramatically affected. 

poetics is based on *noncommutativity*. None of its operations commute, e.g. :math:`x.y \neq y.x` and :math:`x + y \neq y + x`. However, this does not mean a poetic algebra cannot be constructed. The following relationship between separation and succession is a direct result of their definition as operations that insert new lines,

.. math::

    x.\varnothing.y = x + y

In essence, placing a caesura between a succession is equivalent to separating those two signs into stanzas. For this reason, either separation or succession may be regarded individually as primitive and the other may be defined in the terms of the one. 

This identity allows the analogue of the *distributive* property of poetics to be expressed in terms of the *associative* property of succession,

.. math::
        
    x.[y + z] = x.[y.\varnothing.z]

In other words, the *distributivity* of succession over separation reduces to the *associativity* of succession, which is taken as a fundamental property of succession,

.. topic:: Associative Property of Succession

    .. math::

        x.[y.z] = [x.y].z

To make this concrete, let :math:`x = \text{what a cat}`, :math:`y = \text{ugly rat}` and :math:`z = \text{fine felt hat}`. Consider the expression :math:`x.[y + z]`. To preserve the associativity of succession, the operation of separation inside of the brackets must be applied first, resulting in the composite sign,

    | what a cat
    | ugly rat 
    | 
    | fine felt hat

From the associativity of succession and the fact :math:`x.\varnothing.y = x + y`, the associativity of separation directly follows,

.. math::

    [x + y] + z 
    
.. math::

    = [x.\varnothing.y].\varnothing.z 
    
.. math::

    = x.\varnothing.[y.\varnothing.z] 
    
.. math::

    = x + [y + z]

.. _poetics-shorthand:

Shorthand
^^^^^^^^^

Shorthand notation is introduced in this section to extend the primitive operations defined in the previous seciton.

1. **Summation**: The connotation of the :math:`+` symbol is leveraged to extend the symbolism to the :math:`\sum` symbol. Consider,

.. math::

    \sum_1^{n} {a_i}.{b_i}.{a_i} = a_1.b_1.a_1 + a_2.b_2.a_2 + ... a_n.b_n.a_n 

This example shows how to represent a poem of arbitrary length composed of tercet stanzas where the first and third lines rhyme. 

2. **Serialization**: A *serialization* (serialized concatenation) is used in reference to syllables. It simply means the concatenation of a patterned sequence of syllables. Consider,

.. math::

    \prod_{i=1}^{n} {ⲡ_i}{Ⲡ_i} = {ⲡ_1}{Ⲡ_1}{ⲡ_2}{Ⲡ_2} ... {ⲡ_n}{Ⲡ_n}

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
--------

-----------
Expressions
-----------

:math:`a.b.a`
    A tercet where the first and third lines rhyme. 

:math:`A.b.A` 
    A tercet where the first and third lines are the same. 

:math:`a.b.a + a.b.a` 
    Two rhyming tercets.

:math:`a.b.[b:a]`
    A tercet where the last line rhymes with either the first line or the second line.

------------
Applications
------------

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

Using :ref:`exponentiation <poetics-shorthand>`,

.. math::

    p = a^2 + b^2

Keeping in mind the definition of :ref:`poetics-scope` and applying a :ref:`summation <poetics-shorthand>`, this can be further reduced,

.. math::

    p = \sum_1^2 \overline{a^2}

In general, an arbitrary number of rhyming couplets can be represented,

.. math::

    p = \sum_1^n \overline{a^2}

.. [#substitution] A precise definition of a *poetic propositional function* has not yet been given, but it is to be understood in the sense of a truth function, e.g. :math:`\forall p, q, f: ((p \equiv q) \land f(p)) \implies f(q)`