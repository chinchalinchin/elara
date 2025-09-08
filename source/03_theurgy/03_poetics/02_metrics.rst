
.. _poetics-metrics:

Section III: Metrics
====================

.. _poetics-feet:

Feet
----

1. **Iamb**: :math:`\mathfrak{i} = ⲡⲠ`
2. **Trochee**: :math:`\mathfrak{t} = Ⲡⲡ`
3. **Spondee** :math:`\mathfrak{s} = ⲠⲠ`
4. **Pyrrhic** :math:`\mathfrak{p} = ⲡⲡ`   
5. **Dactyl** :math:`\mathfrak{d} = Ⲡⲡⲡ`
6. **Anapest**: :math:`\mathfrak{a} = ⲡⲡⲠ`
7. **Amphibrach**: :math:`\mathfrak{m} = ⲡⲠⲡ`
8. **Amphimacer**: :math:`\mathfrak{c} = ⲠⲡⲠ`
9. **Bacchius**: :math:`\mathfrak{b} = ⲡⲠⲠ`
10. **Antibacchius**: :math:`\mathfrak{h} = ⲠⲠⲡ`
11. **Molossus**: :math:`\mathfrak{l} = ⲠⲠⲠ`
12. **Tribrach**: :math:`\mathfrak{t} = ⲡⲡⲡ`

.. topic:: Definition: Meters

    :math:`a \div \mathfrak{x}_i` denotes a line in :math:`\mathfrak{x}` meter with :math:`i` feet. 

For example, 

.. math::

    [a \div \mathfrak{i}_4].[b \div \mathfrak{i}_3].[a \div \mathfrak{i}_4]

Refers to a tercet where the first and third line are written in iambic tetrameter, whereas the second line is written in iambic trimeter. In other words,

.. math::

    [a \div \mathfrak{i}_4] = {ⲡ_1}{Ⲡ_1}{ⲡ_2}{Ⲡ_2}{ⲡ_3}{Ⲡ_3}{ⲡ_4}{Ⲡ_4}

Note in this example the first and third line rhyme. 

The scope of a meter extends to everything contained in the parenthesis it marks. For example,

.. math::

    [a.a \div \mathfrak{i}_4]

Denotes a rhyming couplet where each line is written in iambic tetrameter. 

Often, when refering to a single line, :math:`a \div \mathfrak{x}_i`, the :math:`a \div ` will be dropped and the line will be represented simply as :math:`\mathfrak{x}_i`.

.. _poetics-lengths:

Lengths
-------

A poetic sign has many different notions of "*length*" beyond the purely linguistic lengths of a sentence. A sentence, as it is conceived in the fields of formal linguistic, can be broken into sequences of characters, words or phonemes (among other categorizations). A poetic sign possesses these notions of length as a result of its embodiment in the medium of language, but it also possesses dimensions of length over and above the lengths prescribed by syntax, semantics and pragmatics. These concepts of length are derived from the structure of poetic signs and represent a space orthogonal to conventional formal linguistics where the semantics of poems are encoded. These different, but interrelated notions of length, are listed directly below and then defined,

- Stanza Length of a Poem 
- Line Length of a Poem
- Line Length of a Stanza
- Syllable Length of a Line
- Syllable Length of a Stanza
- Syllable Length of a Poem

.. _poetics-primitive-lengths:

-----------------
Primitive Lengths
-----------------

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

    Let :math:`u` be an arbitrary line with syllables :math:`ⲣ_i`. The syllable length of :math:`u`, denoted :math:`l(u \mid ⲣ)`, is the natural number :math:`n` that satisfies, 

    .. math::

        l(u \mid ⲣ) = n \equiv u = \prod_1^n ⲣ_i

In effect, the stanza length of a poem is defined as the number times the operation of separation has been applied to stanzas to create a poem, the line length of a stanza is defined as the number of times succession has been applied to lines to construct a stanza, the syllable length is the number of times concatenation has been applied to the syllables to construct a line.

.. note::

    The definition of a length in a level of the poetic hierarchy is given in terms of the level directly below it. 

The notation, :math:`l(p \mid \varsigma)`, :math:`l(\varsigma \mid u)` and :math:`l(u \mid ⲣ)` is meant to invoke the concept of "*conditioning*" from Bayesian analysis. Each type of length is relative to the particular formal term within a poetic sign that falls to the right the :math:`\mid` marker. 

.. _poetics-derivative-lengths:

------------------
Derivative Lengths
------------------

There are several other concepts of length that are derived directly from these definitions, illustrating how these "*basic*" units of poetic length interconnect to form more abstract notions of length. 

.. topic:: Line Length of a Poem 

    Let :math:`p` be an arbitrary poem with stanzas :math:`\varsigma_i`. Let each :math:`\varsigma_i` have lines :math:`u_j`. The line length of :math:`p`, denoted :math:`l(p \mid u)` is defined as,

    .. math::

        l(p \mid u) = \sum_1^{l(p \mid \varsigma)} l(\varsigma \mid u)

.. important::

    :math:`l(\varsigma \mid u)` is a number! Therefore, the :math:`\sum` that appears in the previous definition is an *arithmetical* sum. Recall the :math:`\sum` symbol is overloaded. It may be benefit the reader to treat the preceding as a definition in the metalanguage of poetics, rather than its object language, where the :math:`\sum` symbol is used as a semantic construct. 

This definition captures the common sense notion that the number of lines in a poem is equal to the sum of the number of lines in each stanza. 

.. topic:: Syllable Length of a Stanza 

    Let :math:`\varsigma` be an arbitrary stanza. Let each :math:`\varsigma` have lines :math:`u_i`. Let each line :math:`u_i` have syllables :math:`ⲣ_j`. The syllable length of :math:`\varsigma`, denoted :math:`l(\varsigma \mid ⲣ)` is defined as,

    .. math::

        l(\varsigma \mid ⲣ) = \sum_1^{l(\varsigma \mid u)} l(u_j \mid ⲣ)

Once again, this captures the idea the number of syllables in a stanza is equal to the sum of the number of syllables in each line of the stanza.

There are two ways to define the syllable length of a poem. It can either be defined using the line length of a poem and syllable length of a line, or it can be defined using the stanza length of a poem and the syllable length of a stanza. Whichever definition is selected, the alternative not selected will become a theorem of the formal system as a consequence of the definitions of length. For the current purposes, the first alternative is selected.

.. topic:: Syllable Length of a Poem

    Let :math:`p` be an arbitrary poem with stanzas :math:`\varsigma_i`. Let each :math:`\varsigma_i` have lines :math:`u_j`.  Let each line :math:`u_j` have syllables :math:`ⲣ_k` The syllable length of :math:`p`, denoted :math:`l(p \mid ⲣ)` is defined as,

    .. math::

        l(p \mid ⲣ) = \sum_1^{l(p \mid u)} l(u \mid ⲣ)

In the previous three definition, the "*condition*" of the summation limit becomes the summand's length, while the "*condition*" of the summand becomes the "*condition*" of the result. This is directly analogous to dimensional analysis in fields of science, where the units of two quantities must cancel out in order for the result to be unitless. This can be viewed a type of a "*poetic dimensional analysis*".

.. _poetics-speed:

Speed
-----

This document opened with a quote by Alexander Pope that illustrates a phonological phenomenon that is often employed poetically for effect: sentences with clusters of stressed syllables in sequence have the psychological effect of appearing "*slow*", as opposed to anapestic or dactylic rhythms which are often associated with "*galloping*" or "*rapid*" paces. In other words, there is a correlation between the perceived "*speed*" of a poem and its use syllabic stresses. 

The notion of *poetic speed* is intended to explicate the psychological phenomenon illustrated by Pope and make it conducive to analysis. In making this definition, an important tool for the statistical analysis of poems will be introduced as a result.

First note that syllables are either stressed or unstressed, but not both. Therefore, the total number of syllables in a sign :math:`x` is equal to the number of unstressed syllables :math:`ⲡ` in :math:`x` plus the number of stressed syllables :math:`Ⲡ` in :math:`x`. Introducing the following notation,

- :math:`l(x \mid Ⲡ)`: The number of stressed syllables in sign :math:`x`
- :math:`l(x \mid ⲡ)`: The number of unstressed syllables in sign :math:`x`

It follows logically from the definitions of syllabic length,

.. math::

    l(x \mid ⲣ) = l(x \mid Ⲡ) + l(x \mid ⲡ)

With this in mind, the notion of "*poetic speed*" is formally defined as the "*density*" of stressed syllables in a sign.

.. topic:: Speed

    Let :math:`x` be a poetic sign such that :math:`l(x \mid ⲣ) > 0`. The speed of :math:`x`, denoted :math:`\mathfrak{u}(x)`, is defined as,

    .. math::

        \mathfrak{u}(x) = \frac{l(x \mid ⲣ)}{l(x \mid Ⲡ)}

.. TODO: This definition assumes all lines must possess at least one stressed syllable. Before refining this definition, however, it would probably be beneficial to elaborate on how the stress of a caesura is to be interpretted in the system.

.. _poetics-metrical-structures:

Metrical Structures
-------------------

A *metrical structure* is essentially a permissable sequence of words in a metered line of poetry.

.. important::

    :math:`\mid` is employed as a delimiter in this section. It should be treated as null concatenative character, i.e. a character that when concatenated into a string adds no content.

The number of "*forms*" for a given metered line :math:`\mathfrak{x}_i` is dependent on the number of feet :math:`i` in that line. The following formula for the form cardinality of a metered line can be derived through combinatorial arguments by noting for :math:`n` syllables :math:`ⲣ_i`, 

.. math::

    {ⲣ_1}{p_2} ... {ⲣ_n} 

there are a total of :math:`n-1` possible positions for delimiters to be inserted between the syllables to partition the resultant line into different permutations of words,

.. topic:: Form Cardinality of a Metered Line
    
    .. math::

        F(\mathfrak{x}_i) = 2 ^ {l(\mathfrak{x}_1 \mid ⲣ) \cdot i - 1}

    Where :math:`F(\mathfrak{x}_i)` is the number of permissible metrical structures (forms).

.. topic:: Structure Definitions

    1. Pure Structure: A line :math:`\mathfrak{x}_i` with no syllabic delimiting.
    2. Perfect Structure: A line :math:`\mathfrak{x}_i` where each word :math:`\lambda` is :math:`\lambda/\mathfrak{x}_1`.
    3. Compound Perfect Structure: A line :math:`\mathfrak{x}_i` where each word :math:`\lambda` is :math:`\lambda/\mathfrak{x}_k` for some :math:`1 < k < i`. 
    4. Semi Perfect Structure: A line :math:`\mathfrak{x}_i` where each word :math:`\lambda` is :math:`\lambda/\mathfrak{x}_k` for some :math:`1 < k < i` or :math:`\lambda = ⲣ`.
    5. Monotone Structure: A line :math:`\mathfrak{x}_i` where each word :math:`\lambda = p`

A *perfect* structure is a metric line where each word in the line is written in the same meter as the line itself. For example, the following line is *perfect* iambic tetrameter,

    | within tonight return again

The syllables in each word of this line map directly to the metrical foot. Moreover, the delimiters in this line correspond exactly to the divisions of metrical feet,

.. math::

    {ⲡ_1}{Ⲡ_1} \mid {ⲡ_2}{Ⲡ_2} \mid {ⲡ_3}{Ⲡ_3} \mid {ⲡ_4}{Ⲡ_5}
    
In other words, not dissimilar to the concept of *idempotency*, each consecutive word of a *perfect* line is itself an instance of a smaller *perfect* line. 

An *imperfect* structure occurs when the metrical feet and syllables in a word do not map one-to-one with one another. For example, the following line is *imperfect* iambic tetrameter,

    | the trigger finger lingers long

The syllables in the middle three words, "*trigger finger lingers*", are spread out across different metrical feet. In other words, in an imperfect struture, the delimiters do **not** correspond to the end of the foot.

.. math::

    ⲡ_1 \mid {Ⲡ_1}{ⲡ_2} \mid {Ⲡ_2}{ⲡ_3} \mid {Ⲡ_3}{ⲡ_4} \mid  Ⲡ_3


A *monotone* structure occurs when all syllables in a metrical line are separated by delimiters, as in the famous line from Macbeth,

    | to be or not to be
    
.. math::

    ⲡ_1 \mid {Ⲡ_1} \mid {ⲡ_2} \mid {Ⲡ_2} \mid {ⲡ_3} \mid {Ⲡ_3}

These observations show the classification and elaboration of metrical forms can be expressed using combinatorics.

.. topic:: Form Combinatorics

    The number of possible delimiter positions, :math:`n`, in a line of :math:`\mathfrak{x}_i` meter, where :math:`i \in \mathbb{N}`, is one less than the number of syllables in the line,

    .. math::

        n = l(\mathfrak{x}_i \mid ⲣ) - 1 = l(\mathfrak{x}_1 \mid ⲣ) \cdot i - 1

    The number of possible syllabic forms, :math:`F^r(\mathfrak{x}_i)`, in a line of :math:`\mathfrak{x}_i` meter depends on :math:`r`, the number of delimiters. The number of syllabic forms is given by the combinatorial formula,

    .. math::

        {F^r}(\mathfrak{x}_i) = \binom{n}{r} = \frac{(l(\mathfrak{x}_1 \mid ⲣ) \cdot i - 1)!}{(l(\mathfrak{x}_1 \mid ⲣ) \cdot i - r - 1)! \cdot r!}

.. _poetics-iambic-structures:

-----------------
Iambic Structures
-----------------

- :math:`l(\mathfrak{i}_1| ⲣ) = 2`
- :math:`l(\mathfrak{i}_1| Ⲡ) = 1`
- :math:`l(\mathfrak{i}_1| ⲡ) = 1`

Due to the combinatorial explosion, listing out the possible syllabic forms of a metrical line quickly becomes tedious, but the possible combinations are given below for :math:`\mathfrak{i}_2` and :math:`\mathfrak{i}_3` to give the general idea on how they are constructed, and how to identify the different variants (pure, perfect, semi-perfect, compound perfect, monotone).

**Diambic Structures** 

- Possible Delimiters: :math:`2 \cdot l(\mathfrak{i}_1| ⲣ) - 1 = 4 - 1 = 3` 

1. Form 1: Delimiters = 0 
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3}{Ⲡ_4}` (**Pure**)
2. Form 2: Delimiters = 1
    - :math:`ⲡ_1 \mid {Ⲡ_2}{ⲡ_3}{Ⲡ_4}`
    - :math:`{ⲡ_1}{Ⲡ_2} \mid {ⲡ_3}{Ⲡ_4}` (**Perfect**)
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3} \mid Ⲡ_4`
3. Form 3: Delimiters = 2
    - :math:`ⲡ_1 \mid Ⲡ_2 \mid {ⲡ_3}{Ⲡ_4}` (**Semi Perfect**)
    - :math:`ⲡ_1 \mid {Ⲡ_2}{ⲡ_3} \mid Ⲡ_4`
    - :math:`{ⲡ_1}{Ⲡ_2} \mid ⲡ_3 \mid Ⲡ_4` (**Semi Perfect**)
4. Form 4: Delimiters = 3
    - :math:`ⲡ_1 \mid Ⲡ_2 \mid ⲡ_3 \mid Ⲡ_4` (**Monotone**)

**Triambic Structures**

- Possible Delimiters: :math:`3 \cdot l(\mathfrak{x}_1| ⲣ) - 1 = 6 - 1 = 5`

1. Form 1: Delimiters = 0
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3}{Ⲡ_4}{ⲡ_5}{Ⲡ_6}` (**Pure**)
2. Form 2: Delimiters = 1
    - :math:`ⲡ_1 | {Ⲡ_2}{ⲡ_3}{Ⲡ_4}{ⲡ_5}{Ⲡ_6}`
    - :math:`{ⲡ_1}{Ⲡ_2} | {ⲡ_3}{Ⲡ_4}{ⲡ_5}{Ⲡ_6}` (**Compound Perfect**)
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3} | {Ⲡ_4}{ⲡ_5}{Ⲡ_6}`
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3}{Ⲡ_4} | {ⲡ_5}{Ⲡ_6}` (**Compound Perfect**)
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3}{Ⲡ_4}{ⲡ_5} | Ⲡ_6`
3. Form 3: Delimiters = 2
    - :math:`ⲡ_1 | Ⲡ_2 | {ⲡ_3}{Ⲡ_4}{ⲡ_5}{Ⲡ_6}`
    - :math:`ⲡ_1 | {Ⲡ_2}{ⲡ_3} | {Ⲡ_4}{ⲡ_5}{Ⲡ_6}`
    - :math:`ⲡ_1 | {Ⲡ_2}{ⲡ_3}{Ⲡ_4} | {ⲡ_5}{Ⲡ_6}`
    - :math:`ⲡ_1 | {Ⲡ_2}{ⲡ_3}{Ⲡ_4}{ⲡ_5} | Ⲡ_6`
    - :math:`{ⲡ_1}{Ⲡ_2} | ⲡ_3 | {Ⲡ_4}{ⲡ_5}{Ⲡ_6}`
    - :math:`{ⲡ_1}{Ⲡ_2} | {ⲡ_3}{Ⲡ_4} | {ⲡ_5}{Ⲡ_6}` (**Perfect**)
    - :math:`{ⲡ_1}{Ⲡ_2} | {ⲡ_3}{Ⲡ_4}{ⲡ_5} | Ⲡ_6`
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3} | Ⲡ_4 | {ⲡ_5}{Ⲡ_6}`
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3} | {Ⲡ_4}{ⲡ_5} | Ⲡ_6`
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3}{Ⲡ_4} | ⲡ_5 | Ⲡ_6`
4. Form 4: Delimiters = 3
    - :math:`ⲡ_1 | Ⲡ_2 | ⲡ_3 | {Ⲡ_4}{ⲡ_5}{Ⲡ_6}`
    - :math:`ⲡ_1 | Ⲡ_2 | {ⲡ_3}{Ⲡ_4} | {ⲡ_5}{Ⲡ_6}` (**Semi Perfect**)
    - :math:`ⲡ_1 | Ⲡ_2 | {ⲡ_3}{Ⲡ_4}{ⲡ_5} | Ⲡ_6`
    - :math:`ⲡ_1 | {Ⲡ_2}{ⲡ_3} | Ⲡ_4 | {ⲡ_5}{Ⲡ_6}`
    - :math:`ⲡ_1 | {Ⲡ_2}{ⲡ_3} | {Ⲡ_4}{ⲡ_5} | Ⲡ_6`
    - :math:`ⲡ_1 | {Ⲡ_2}{ⲡ_3}{Ⲡ_4} | ⲡ_5 | Ⲡ_6`
    - :math:`{ⲡ_1}{Ⲡ_2} | ⲡ_3 | Ⲡ_4 | {ⲡ_5}{Ⲡ_6}` (**Semi Perfect**)
    - :math:`{ⲡ_1}{Ⲡ_2} | ⲡ_3 | {Ⲡ_4}{ⲡ_5} | Ⲡ_6`
    - :math:`{ⲡ_1}{Ⲡ_2} | {ⲡ_3}{Ⲡ_4} | ⲡ_5 | Ⲡ_6` (**Semi Perfect**)
    - :math:`{ⲡ_1}{Ⲡ_2}{ⲡ_3} | Ⲡ_4 | ⲡ_5 | Ⲡ_6`
5. Form 5: Delimiters = 4
    - :math:`ⲡ_1 | Ⲡ_2 | ⲡ_3 | Ⲡ_4 | {ⲡ_5}{Ⲡ_6}` (**Semi Perfect**)
    - :math:`ⲡ_1 | Ⲡ_2 | ⲡ_3 | {Ⲡ_4}{ⲡ_5} | Ⲡ_6`
    - :math:`ⲡ_1 | Ⲡ_2 | {ⲡ_3}{Ⲡ_4} | ⲡ_5 | Ⲡ_6` (**Semi Perfect**)
    - :math:`ⲡ_1 | {Ⲡ_2}{ⲡ_3} | Ⲡ_4 | ⲡ_5 | Ⲡ_6`
    - :math:`{ⲡ_1}{Ⲡ_2} | ⲡ_3 | Ⲡ_4 | ⲡ_5 | Ⲡ_6` (**Semi Perfect**)
6. Form 6: Delimiters = 5
    - :math:`ⲡ_1 \mid Ⲡ_2 \mid ⲡ_3 \mid Ⲡ_4 \mid ⲡ_5 \mid Ⲡ_6` (**Monotone**)

From these examples, it should be clear each meter has exactly one *pure* form, one *perfect* and one *monotone*. The number of *semi perfect* and *compound perfect* is dependent on the number of delimiters

.. _poetics-chirality:

Chirality
---------

.. topic:: Chirality

    Let :math:`z_1, z_2, z_3, z_4, z_5, z_6` be artitary poetic signs, possibly caesuras (:math:`\varnothing`).

    A sign :math:`x` is said to be a chiasmus of the sign :math:`y`, denoted :math:`x \bowtie y`, when the following open formula holds,

    .. math::

        x \bowtie y \equiv

    .. math::

        \exists \chi_1, \chi_2: [x = {z_1}{\chi_1}{z_2}{\chi_2}{z_3}]  \land [w = {z_4}{\chi_2}{z_5}{\chi_1}{z_6}]

    Where :math:`\chi_1, \chi_2` are the *chiral pivots*.

.. _poetics-chirality-examples:

--------
Examples
--------

.. epigraph::

    | When their bones are picked clean and the clean bones gone

    -- `And Death Shall Have No Dominion`_, Dylan Thomas

- **Syllabification**:
- **Chiral Pivots**: :math:`\chi_1 = ...`, :math:`\chi_2 = ...`
- **Chirality**: 

.. epigraph::

    | Break in the sun till the sun breaks down

    -- `And Death Shall Have No Dominion`_, Dylan Thomas

- **Syllabification**:
- **Chiral Pivots**: :math:`\chi_1 = ...`, :math:`\chi_2 = ...`
- **Chirality**: 
 
.. epigraph::

    | Pleasure's a sin, and sometimes sin's a pleasure.

    -- Don Jaun, Lord Byron

- **Syllabification**:
- **Chiral Pivots**: :math:`\chi_1 = ...`, :math:`\chi_2 = ...`
- **Chirality**: 

.. epigraph::

    | How beautiful, if sorrow had not made
    | Sorrow more beautiful than Beauty's self.

    -- `Hyperion`_, John Keats

- **Syllabification**:
- **Chiral Pivots**: :math:`\chi_1 = ...`, :math:`\chi_2 = ...`
- **Chirality**: 

.. epigraph::

    | Fair is foul, and foul is fair. 

    -- Macbeth, William Shakespeare

- **Syllabification**:
- **Chiral Pivots**: :math:`\chi_1 = ...`, :math:`\chi_2 = ...`
- **Chirality**: 

.. epigraph::

    | Can make a Heav'n of Hell, a Hell of Heav'n.

    -- Paradise Lost, John Milton

- **Syllabification**: :math:`{ⲡ_1} {Ⲡ_1}`
- **Chiral Pivots**: :math:`\chi_1 = ...`, :math:`\chi_2 = ...`
- **Chirality**: 

.. epigraph::

    | Beauty is truth, truth beauty

    -- `Ode on a Grecian Urn`_, John Keats

- **Syllabification**: :math:`{Ⲡ_1}{ⲡ_2} \mid {ⲡ_3} \mid {Ⲡ_4} \mid {Ⲡ_4} \mid {Ⲡ_1}{ⲡ_2}`
- **Chiral Pivots**: :math:`\chi_1 = {Ⲡ_1}{ⲡ_2}`, :math:`\chi_2 = Ⲡ_4`
- **Chirality**: :math:`{Ⲡ_1}{ⲡ_2} \mid {ⲡ_3} \mid {Ⲡ_4} \bowtie {Ⲡ_4} \mid {Ⲡ_1}{ⲡ_2}`
