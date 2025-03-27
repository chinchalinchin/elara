.. _syntagmics:

----------
Syntagmics
----------

Formalization
-------------

**Prior Definitions**

Given below are existing definitions of poetical devices. 

.. topic:: Definition: Feet
    
    - Iamb: One unstressed syllable followed by a stressed syllable.
    - Spondee: A stressed syllable followed by a stressed syllable. Employed to slow down the pace of a line.
    - Dactyl: A stressed syllable followed by two unstressed syllables. Employed to create a sense of falling or release.
    - Trochee: A stressed syllable folowed by an unstressed syllable. Employed to emphasize urgency or directness.
    - Anapest: Two unstressed syllables followed by a stressed syllable. Employed to create a sense of building momentum.

.. topic:: Definition: Lines

    - Tetrameter: A line with four feet.
    - Pentameter: A line with five feet.
    - Trimeter: A line with three feet.
    - Hendecasyllable: A line consisting of eleven syllables. 

.. topic:: Definitions: Stanzas

    - Couplet: A stanza with two lines.
    - Tercet: A stanza with three lines
    - Quatrain: A stanza with four lines
    - Cinquain: A stanza with five lines
    - Sestet: A stanza with six lines.
    - Octet: A stanza with eight lines.
    - Envoi: A short, concluding stanza.

**Constants**

1. Uppercase English letters (A, B, C, ... ): Fixed lines.
2. Uppercase Greek letters (Α, Β, Γ, ): Fixed syllables.
3. Lowercase Greek letters (α, β, γ, ... ): Fixed words.
4. The lowercase English letter n is reserved for natural numbers.
5. The lowercase Fraktur letter 𝔦 is reserved for iambs.
6. The lowercase Fraktur letter 𝔱 is reserved for trochees.
7. The lowercase Fraktur letter 𝔰 is reserved for spondees. 
8. The lowercase Fraktur letter 𝔞 is reserved for anapests.
9. The lowercase Fraktur letter 𝔡 is reserved for dactyls.
10. The mathematical symbol ∅ is reserved for the pause (caesura). 
11. The ampersand & represents blank newlines. 
   
**Variables**

1. Lowercase English letters (a, b, c, ... ): Indeterminate rhymed lines.
2. The lowercase English letters u, v, w are reserved for indeterminate lines, not necessarily rhymed. 
3. The lowercase Greek letters φ, χ, ψ are reserved for indeterminate rhymed words.
4. The lowercase Greek letter λ is reserved for indetermine words, not necessarily rhymed.
5. The lowercase Greek letters π, Π are reserved for indeterminate syllables. 
6. The lowercase Fraktur letter 𝔵 is reserved for indeterminate meters.
7. The lowercase Greek letter ς is reserved for indeterminate stanzas.
8. The English letters x, y and z are reserved for global variables, i.e. syllables, lines and stanzas. 

.. important::

    Upper English letters are meant to denote particular lines, whereas lowercase English letters are meant to denote indeterminate lines that are related through their rhyme scheme. 

.. important::

    The choice of π and Π to represent syllables mirrors the unstressed and stressed syllables of verses. In other words, π is meant to represent indeterminate unstressed syllables, whereas Π is meant to represent indeterminate stressed syllables. However, π is often used in a more general capacity, when the indeterminate syllable could be one that is either stressed or unstressed. It will be clear from context when π is employed in this manner. 

The variables *x*, *y* and *z* will sometimes be referred to as *syntagmic variables*, or *signs*, to stress their range over the entire domain of poetic objects. 

Uppercase-lowercase pairs of English letters are understood to be rhymes. The difference in the symbolism is the *fixed* nature of the denotation. For example, the expression *A.a.a.A* denotes one fixed line, a rhyming couplet and then the fixed line again,

    The cat on the mat
    Got large and fat
    So-and-so such that 
    The cat on the mat

The scope of a rhyme does not extend beyond a stanza, i.e. past the "+" sign. For example, in the expression "*a.b.a + a.b.a*", the rhyme in "*a*" within the first stanza does not extend to the rhyme in "*a*" within the second stanza. 

**Notation**

1. #x: A lengthened sign. 
2. ♭x: A shortened sign.  
3. x.y (**Succession**): Successive signs.
4. x-y (**Concatenation**): Concatenated signs.
5. x:y (**Delimitation**): Delimited signs.
6. x ∨ y (**Disjunction**): A sign that is either x or y.
7. x + y (**Separation**): Separated signs.
8. x∝λ : Sign containing a word. 
9. x(λ) : A sign ending in a word.  
10. (λ)x: A sign beginning with a word. 
11. x(π): A sign ending in a syllable.
12. (π)x: A sign starting with a syllable
13. x.y.x | x = z: Substitute z for x in the sign "x.y.x"

Brackets, [], are used to group operations within expressions by precedence.

To see what is meant by the distinction between *separation* and *succession*, let x = "*the fish in the dish*" and y = "*the dog on a jog*". Then x.y means,

| the fish in the dish
| the dog on a jog

Where as x + y means,

| the fish in the dish
| 
| the dog on a jog

From this, it can be see the operation of *successions* inserts a new line after the first line, whereas the operation of *separation* inserts a new line after the first line *and* before the second line, to create a blank line between them. In effect, the operation of *separation* creates stanzas, whereas the operation of *succession* creates lines. 

The connotation of the "+" symbol is leveraged to extend the symbolism to the "*Σ*" symbol, i.e.,

    Σ :sub:`1`:sup:`n` x :sub:`i` 

Is meant to denote a series of signs separated by blank lines. 

A *delimitation* is mainly used in reference to words or syllables, and can be seen as a shorthand for excessive concatenation. *Delimitation* denotes the insertion of *pauses* (delimiters) in between words,

    α:β:γ = α-∅-β-∅-γ

**Propositions**

∀ς: ∃x: ς = x
    All stanzas are made of lines. 

∀p: p  = Σ :sub:`1`:sup:`n` ς :sub:`i` 
    All poems are made of stanzas. 

**Examples**

a.b.a
    A tercet where the first and third lines rhyme. 

A.b.A 
    A tercet where the first and third lines are the same. 

a.b.a + a.b.a 
    Two rhyming tercets.

a.b.[b ∨ a]
    A tercet where the last line rhymes with either the first line or the second line.

**Meter**

𝔦 = π-Π
    The definition of an **iamb**

𝔱 = Π-π
    The definition of a **trochee**

𝔰 = Π-Π
    The definition of a **spondee**

𝔡 = Π-π-π
    The definition of **dactyl**

𝔞 = π-π-Π
    The definition of a **anapest**

.. topic:: Definition: Meters

    a/𝔵 :sub:`n` denotes a line in 𝔵 n-meter. 

For example, 

    (a/𝔦 :sub:`4`).(b/𝔦 :sub:`3`).(a/𝔦 :sub:`4`)

Refers to a tercet where the first and third line are written in iambic tetrameter, whereas the second line is written in iambic trimeter. Note in this example the first and third line rhyme. 

The scope of a meter extends to everything contained in the parenthesis it marks. For example,

    (a.a/𝔦 :sub:`4`)

Denotes a rhyming couplet where each line is written in iambic tetrameter. 

.. _schemes:

Schemes
-------

.. _ballad:

Ballad
^^^^^^

.. topic:: Schema

    Σ :sub:`1`:sup:`n` (a/𝔦 :sub:`4`).(b/𝔦 :sub:`3`).(a ∨ c/𝔦 :sub:`4`).(b/𝔦 :sub:`3`)

**References**

- `A tragical ballad of the unfortunate loves of Lord Thomas and fair Eleanor: together with the downfall of the brown girl <https://archive.org/details/bim_eighteenth-century_a-tragical-ballad-of-t_1795>`_, Frances James Child
- `Ballad of the Goodly Fere <https://allpoetry.com/Ballad-Of-The-Goodly-Fere>`_, Ezra Pound
- `Ballad of Sir Patrick Stern <https://sites.williams.edu/sirpatrickspens/ballad/293/>`_, W. Scott
- `La Belle Dame sans Merci <https://www.poetryfoundation.org/poems/44475/la-belle-dame-sans-merci-a-ballad>`_, John Keats
- `Lord Thomas and Annet <https://sacred-texts.com/neu/eng/child/ch073.htm>`_, Old English Ballad
- `Tam Lin <https://tam-lin.org/versions/39A.html>`_, Old Scottish Ballad

.. _ballade: 

Ballade
^^^^^^^

.. topic:: Schema

    a.b.a.b.b.c.b.C + a.b.a.b.b.c.b.C + a.b.a.b.b.c.b.C + b.c.b.C

.. topic:: Schema (Ballade Royal)

    (a.b.a + b.b + c.c) ∨ (a.b.a.b + b.c.c)

.. topic:: Schema (Chant Royal)

    Σ :sub:`1`:sup:`5` a.b.a.b.c.c.d.d.e.d.E + d.d.e.d.E ∨ c.c.d.d.e.d.E

**References**

None yet found. 

.. _ode:

Ode
^^^

No fixed schema.

.. list-table:: 
    
  * - Greek
    - ᾠδή
  * - Latin
    - oda
  * - French
    - ode
  * - English
    - ode

**References**

- `Ode on a Grecian Urn <https://www.poetryfoundation.org/poems/44477/ode-on-a-grecian-urn>`_, John Keats
- `Ode to a Nightingale <https://www.poetryfoundation.org/poems/44479/ode-to-a-nightingale>`_, John Keats
- `Ode to the West Wind <https://www.poetryfoundation.org/poems/45134/ode-to-the-west-wind>`_, Percy Blysse Shelely

.. _ottava:

Ottava
^^^^^^

.. topic:: Schema (ottava siciliana)

    a.b.a.b.a.b.a.b

.. topic:: Schema (strambotto)

    a.b.a.b.c.c.d.d

Each line in a *ottava siciliana* or *strambotto* is a hendecasyllable.

.. topic:: Schema (ottava rima)

    (a.b.a.b.a.b.c.c/𝔦 :sub:`5`)

**References**

None yet found.

.. _pantoum:

Pantoum
^^^^^^^

.. topic:: Schema

   A.B.C.D + B.E.D.F + E.G.F.H + ... + x.y.C.A

**References**

- `Pantoum of the Great Depression <https://www.poetryfoundation.org/poems/58080/pantoum-of-the-great-depression>`_, Donald Justice

.. _rondeau:

Rondeau
^^^^^^^

**Medieval Rondeaus**

The following diagram shows the different schemata for the rondeau form in 14th-century France,

.. figure:: ../../_static/img/context/poetical/14th-century-rondeaus.svg
  :width: 80%
  :alt: Diagram of 14th century rondeaus
  :align: center

.. topic:: Rondeau Schema (Medieval)

    1. Couplet: A.B.a.A.a.b.A.B
    2. Tercet: A.B.B.a.b.A.B.a.b.b.A.B.B
    3. Quatrain: A.B.B.A.a.b.A.B.a.b.b.a.A.B.B.A
    4. Cinquain: A.A.B.B.A.a.a.b.A.A.B.a.a.b.b.a.A.A.B.B.A

    This schema can be rewritten to emphasize the *refrain R* within in the form using substitution notation,

    5. Couplet: R.a.A.a.b.R | R = A.B 
    6. Tercet: R.a.b.A.B.a.b.b.R | R = A.B.B
    7. Quatrain: R.a.b.A.B.a.b.b.a.R | R = A.B.B.A 
    8. Cinquain: R.a.a.b.A.A.B.a.a.b.b.a.R | R = A.A.B.B.A

Note that a *Rondeau Couplet* is simply a :ref:`triolet`. 

**Renaissance Rondeaus**

The following diagrams shows the different schemata for the rondeau form duing the Renaissance, 

.. figure:: ../../_static/img/context/poetical/renaissance-rondeaus.svg
  :width: 80%
  :alt: Diagram of Renaissance rondeaus
  :align: center

.. topic:: Rondeau Schema (Renaissance)

    1. Rondel: A.B.a.b + a.b.A.B + a.b.b.a.A
    2. Rondeau Prime: R-a.b.b.a.a.b.R + a.b.b.a.R
    3. Rondeau: R-a.a.b.b.a + a.a.b + a.a.b.b.a.R

**Roundel**

.. topic:: Roundel Schema 

    a.b.a.R + b.a.b + a.b.a.R 

**References**

- `In Flanders Fields <https://www.poetryfoundation.org/poems/47380/in-flanders-fields>`_, John McCrae
- `We Wear the Mask <https://www.poetryfoundation.org/poems/44203/we-wear-the-mask>`_, Paul Laurence Dunbar

.. _sestina:

Sestina
^^^^^^^

Six sestets followed by a tercet envoi.

.. topic:: Schema

   u(α).v(β).w(γ).x(δ).y(ε).z(ζ) + 
   u(ζ).v(α).w(ε).x(β).y(δ).z(γ) + 
   u(γ).v(ζ).w(δ).x(α).y(β).z(ε) +
   u(ε).v(γ).w(β).x(ζ).y(α).z(δ) +
   u(δ).v(ε).w(α).x(γ).y(ζ).z(β) +
   u(β).v(δ).w(ζ).x(ε).y(γ).z(α) + 
   [u∝α.v∝β.w∝γ] ∨ [u∝γ.v∝δ.w∝ε] ∨ [u∝ζ.v∝β.w∝δ]

**References**

- `Sestina of the Tramp-Royal <https://www.poetryfoundation.org/poems/46775/sestina-of-the-tramp-royal>`_, Rudyard Kipling
- `Sestina: Travel Notes <https://www.poetryfoundation.org/poetrymagazine/browse?volume=62&issue=6&page=28>`_

.. _sonnet:

Sonnet
^^^^^^

.. topic:: Schema (Petrachan)

    a.b.b.a.a.b.b.a + c.d.e.c.d.e ∨ c.d.c.d.c.d
   
.. topic:: Schema (Shakespearan)

   (a.b.a.b + c.d.c.d + e.f.e.f + g.g/𝔦 :sub:`5`)

**References**

- `Batter My Heart, Three Person'd God <https://www.poetryfoundation.org/poems/44106/holy-sonnets-batter-my-heart-three-persond-god>`_, John Donne
- `Death Be Not Proud <https://www.poetryfoundation.org/poems/44107/holy-sonnets-death-be-not-proud>`_, John Donne
- `On the Grasshoper and Cricket <http://keats-poems.com/on-the-grasshopper-and-cricket/>`_, John Keats
- `When I Have Seen By Times Fell Hand Defac'd <https://www.poetryfoundation.org/poems/45096/sonnet-64-when-i-have-seen-by-times-fell-hand-defacd>`_, William Shakespeare

.. _terza:

Terza
^^^^^

.. topic:: Schema

    a.b.a + b.c.b + c.d.c + d.e.d +  ... 

**References**

None yet found.

.. _triolet:

Triolet
^^^^^^^

.. topic:: Schema

    (A.B.a.A.a.b.A.B/𝔦 :sub:`4`)

**References**

- `Birds at Winter Nightfall <https://allpoetry.com/poem/14327645-Birds-At-Winter-Nightfall--Triolet--by-Thomas-Hardy>`_, Thomas Hardy
- `How Great My Grief <https://allpoetry.com/How-Great-My-Grief>`_, Thomas Hardy

.. _virelai:

Virelai
^^^^^^^

.. topic:: Schema (Ancien)
    
    a.a.♭b.a.a.♭b.a.a.♭b + b.b.♭c.b.b.♭c.b.b.♭c + ... 

.. topic:: Schema (Nouveau)

    A.B.
    
    TODO

**References**

- `July <https://www.poetrynook.com/poem/july-41>`_, Henry Austin Dobson
- `Spring Sadness <https://www.gutenberg.org/files/45736/45736-h/45736-h.htm>`_, John Payne

.. _villanelle:

Villanelle
^^^^^^^^^^

TODO: research Terzanelles. 

.. topic:: Schema 


    A :sub:`1`.b.A :sub:`2` + a.b.A :sub:`1` + a.b.A:sub:`2` + a.b.A :sub:`1` + a.b.A :sub:`2` + a.b.A :sub:`1` .A :sub:`2`

**References**

- `Do Not Go Gentle into That Good Night <https://www.poetryfoundation.org/poems/46569/do-not-go-gentle-into-that-good-night>`_, Dylan Thomas
- `Mad Girl's Love Song <https://allpoetry.com/mad-girl's-love-song>`_, Sylvia Plath
- `One Art <https://www.poetryfoundation.org/poems/47536/one-art>`_, Elizabeth Bishop
- `Song <https://www.poetryfoundation.org/poems/47601/song-56d2282a6cdf5>`_
- `The Waking <https://www.poetryfoundation.org/poems/43333/the-waking-56d2220f25315>`_, Theodore Roethke
  
