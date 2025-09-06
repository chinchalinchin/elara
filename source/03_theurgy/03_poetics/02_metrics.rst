
.. _poetics-meter:

Section III: Meter
==================

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
    The definition of an **anapest**

:math:`\mathfrak{m} = ⲡⲠⲡ`
    The definition of an **amphibrach**

:math:`\mathfrak{c} = ⲠⲡⲠ`
    The definition of an **amphimacer**

.. topic:: Definition: Meters

    :math:`a/\mathfrak{x}_n` denotes a line in :math:`\mathfrak{x}` n-meter. 

For example, 

.. math::

    (a/\mathfrak{i}_4).(b/\mathfrak{i}_3).(a/\mathfrak{i}_4)

Refers to a tercet where the first and third line are written in iambic tetrameter, whereas the second line is written in iambic trimeter. In other words,

.. math::

    (a/\mathfrak{i}_4) = {ⲡ_1}{Ⲡ_1}{ⲡ_2}{Ⲡ_2}{ⲡ_3}{Ⲡ_3}{ⲡ_4}{Ⲡ_4}

Note in this example the first and third line rhyme. 

The scope of a meter extends to everything contained in the parenthesis it marks. For example,

.. math::

    (a.a/\mathfrak{i}_4)

Denotes a rhyming couplet where each line is written in iambic tetrameter. 

Lengths
-------

A poetic sign has many different notions of "*length*" beyond the purely linguistic lengths of a sentence. A sentence, as it is conceived in the fields of formal linguistic, can be broken into sequences of characters, words or phonemes (among other categorizations). A poetic sign possesses these notions of length as a result of its embodiment in the medium of language, but it also possesses dimensions of length over and above the lengths prescribed by syntax, semantics and pragmatics. These concepts of length are derived from the structure of poetic signs and represent a space orthogonal to conventional formal linguistics where the semantics of poems are encoded. These different, but interrelated notions of length, are listed directly below and then defined,

- Stanza Length of a Poem 
- Line Length of a Poem
- Line Length of a Stanza
- Syllable Length of a Line
- Syllable Length of a Stanza
- Syllable Length of a Poem

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

    Let :math:`u` be an arbitrary line with syllables :math:`\rho_i`. The syllable length of :math:`u`, denoted :math:`l(u \mid \rho)`, is the natural number :math:`n` that satisfies, 

    .. math::

        l(u \mid \rho) = n \equiv u = \prod_1^n \rho_i

In effect, the stanza length of a poem is defined as the number times the operation of separation has been applied to stanzas to create a poem, the line length of a stanza is defined as the number of times succession has been applied to lines to construct a stanza, the syllable length is the number of times concatenation has been applied to the syllables to construct a line.

.. note::

    The definition of a length in a level of the poetic hierarchy is given in terms of the level directly below it. 

The notation, :math:`l(p \mid \varsigma)`, :math:`l(\varsigma \mid u)` and :math:`l(u \mid \rho)` is meant to invoke the concept of "*conditioning*" from Bayesian analysis. Each type of length is relative to the particular formal term within a poetic sign that falls to the right the :math:`\mid` marker. 

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
-----

This document opened with a quote by Alexander Pope that illustrates a phonological phenomenon that is often employed poetically for effect: sentences with clusters of stressed syllables in sequence have the psychological effect of appearing "*slow*", as opposed to anapestic or dactylic rhythms which are often associated with "*galloping*" or "*rapid*" paces. In other words, there is a correlation between the perceived "*speed*" of a poem and its use syllabic stresses. 

The notion of *poetic speed* is intended to explicate the psychological phenomenon illustrated by Pope and make it conducive to analysis. In making this definition, an important tool for the statistical analysis of poems will be introduced as a result.

First note that syllables are either stressed or unstressed, but not both. Therefore, the total number of syllables in a sign :math:`x` is equal to the number of unstressed syllables :math:`ⲡ` in :math:`x` plus the number of stressed syllables :math:`Ⲡ` in :math:`x`. Introducing the following notation,

- :math:`l(x \mid Ⲡ)`: The number of stressed syllables in sign :math:`x`
- :math:`l(x \mid ⲡ)`: The number of unstressed syllables in sign :math:`x`

It follows logically from the definitions of syllabic length,

.. math::

    l(x \mid \rho) = l(x \mid Ⲡ) + l(x \mid ⲡ)

With this in mind, the notion of "*poetic speed*" is formally defined as the "*density*" of stressed syllables in a sign.

.. topic:: Speed

    Let :math:`x` be a poetic sign such that :math:`l(x \mid \rho) > 0`. The speed of :math:`x`, denoted :math:`\mathfrak{u}(x)`, is defined as,

    .. math::

        \mathfrak{u}(x) = \frac{l(x \mid \rho)}{l(x \mid Ⲡ)}

.. TODO: This definition assumes all lines must possess at least one stressed syllable. Before refining this definition, however, it would probably be beneficial to elaborate on how the stress of a caesura is to be interpretted in the system.