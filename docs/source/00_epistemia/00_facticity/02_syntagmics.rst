.. _syntagmics:

----------
Syntagmics
----------

**Constants**

1. Uppercase English letters (A, B, C, ... ): Fixed lines.
2. Uppercase Greek letters (Α, Β, Γ, ): Fixed syllables.
3. Lowercase Greek letters (α, β, γ, ... ): Fixed words.

**Variables**

1. Lowercase English letters (a, b, c, ... ): Indeterminate rhymed lines.
2. The English letters u, v, w, x, y and z are reserved for indeterminate lines, not necessarily rhymed. 
3. The Greek letter λ is reserved for indetermine words.
4. The Greek letter π is reserved for indeterminate syllables. 
5. The Greek letter ς is reserved for indeterminate stanzas.

.. important::

    Upper English letters are meant to denote particular lines, whereas lowercase English letters are meant to denote indeterminate lines that are related through their rhyme scheme. 

**Notation**

1. x.y : Successive lines.
2. x-y: Concatenated lines.
3. x + y : Successive stanzas.
4. x(λ) : A line ending in a word.  
5. x[π]: A line ending in a syllable
6. x.y.x | x = z: Substitute z for x in the expression "x.y.x"

**Operations**

1. Σ :sub:`i=1`:sup:`n` ς:sub:`i` 

**Propositions**

∀ς: ∃x: ς = x
    All stanzas are made of lines. 

∀p: p  = Σ :sub:`i=1`:sup:`n` ς:sub:`i` 
    All poems are made of stanzas. 

**Definitions**

.. topic:: Definition: Lines

    - Hendecasyllable: A line consisting of eleven syllables. 

.. topic:: Definitions: Stanzas

    - Couplet: A stanza with two lines.
    - Tercet: A stanza with three lines
    - Quatrain: A stanza with four lines
    - Cinquain: A stanza with five lines
    - Sestet: A stanza with six lines.
    - Octet: A stanza with eight lines.
    - Envoi: A short, concluding stanza.

**Examples**

a.b.a
    A tercet where the first and third lines rhyme. 

A.b.A 
    A tercet where the first and third lines are the same. 

a.b.a + a.b.a 
    Two rhyming tercets.

.. important::

    Uppercase-lowercase pairs of English letters are understood to be rhymes. The difference in the symbolism is the *fixed* nature of the denotation.

    The expression *AaaA* denotes one fixed line, a rhyming couplet and then the fixed line again. As a example, 

    The cat on the mat
    Got large and fat
    So-and-so such that 
    The cat on the mat

.. _ballad:

Ballad
------

Three octets followed by a quatrain envoi.

.. topic:: Schema 

    TODO 

**References**

None yet found.

.. _ballade: 

Ballade
-------

TODO 

.. topic:: Schema

    TODO

**References**

None yet found. 

.. _ghazal:

Ghazal
------

TODO

.. topic:: Schema

    TODO

**References**

- `Tongiht <https://www.poetryfoundation.org/poems/51652/tonight-56d22f898fcd7>`_, Agha Shahid Ali

.. _haiku:

Haiku
-----

TODO 

.. topic:: Schema

    TODO
    
**References**

None yet found. 

.. _ode:

Ode
---

TODO 

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

.. _pantoum:

Pantoum
-------

A series of quatrains where every quatrain's first and third line are the second and fourth line of the previous quatrian. 

.. topic:: Schema

   A.B.C.D + B.E.D.F + E.G.F.H + ...

**References**

- `Pantoum of the Great Depression <https://www.poetryfoundation.org/poems/58080/pantoum-of-the-great-depression>`_, Donald Justice

.. _rondeau:

Rondeau
-------

The following diagram shows the different schemata for the rondeau form in 14th century France.

**Medieval Rondeaus**

.. figure:: ../../_static/img/context/poetical/14th-century-rondeaus.svg
  :width: 80%
  :alt: Diagram of 14th century rondeaus
  :align: center

.. topic:: Rondeau Schema (Medieval)

    1. Couplet: A.B.a.A.a.b.A.B
    2. Tercet: A.B.B.a.b.A.B.a.b.b.A.B.B
    3. Quatrain: A.B.B.A.a.b.A.B.a.b.b.a.A.B.B.A
    4. Cinquain: A.A.B.B.A.a.a.b.A.A.B.a.a.b.b.a.A.A.B.B.A

    This schema can be rewritten to emphasize the *refrain R* within in form using the substitution notation,

    1. Couplet: R.a.A.a.b.R | R = A.B 
    2. Tercet: R.a.b.A.B.a.b.b.R | R = A.B.B
    3. Quatrain: R.a.b.A.B.a.b.b.a.R | R = A.B.B.A 
    4. Cinquain: R.a.a.b.A.A.B.a.a.b.b.a.R | R = A.A.B.B.A

Note that a *Rondeau Couplet* is simply a :ref:`triolet`. 

**Renaissance Rondeaus**

The following diagrams shows the different schemata for the rondeau form duing the Renaissance. 

.. figure:: ../../_static/img/context/poetical/renaissance-rondeau.svg
  :width: 80%
  :alt: Diagram of Renaissance rondeaus
  :align: center

.. topic:: Rondeau Schema (Renaissance)

    1. Rondel: A.B.a.b + a.b.A.B + a.b.b.a.A
    2. Rondeau Prime: R-a.b.b.a.a.b.R + a.b.b.a.R
    3. Rondeau: R-a.a.b.b.a.b.R + a.a.b.R + a.a.b.b.a.R

**References**

- `In Flanders Fields <https://www.poetryfoundation.org/poems/47380/in-flanders-fields>`_, John McCrae
- `We Wear the Mask <https://www.poetryfoundation.org/poems/44203/we-wear-the-mask>`_, Paul Laurence Dunbar

.. _sestina:

Sestina
-------

Six sestets followed by a tercet envoi.

.. topic:: Schema

   u(α).v(β).w(γ).x(δ).y(ε).z(ζ) + 
   u(ζ).v(α).w(ε).x(β).y(δ).z(γ) + 
   u(γ).v(ζ).w(δ).x(α).y(β).z(ε) +
   u(ε).v(γ).w(β).x(ζ).y(α).z(δ) +
   u(δ).v(ε).w(α).x(γ).y(ζ).z(β) +
   u(β).v(δ).w(ζ).x(ε).y(γ).z(α) + 
   x.y.z

**References**

- `Sestina of the Tramp-Royal <https://www.poetryfoundation.org/poems/46775/sestina-of-the-tramp-royal>`_, Rudyard Kipling
- `Sestina: Travel Notes <https://www.poetryfoundation.org/poetrymagazine/browse?volume=62&issue=6&page=28>`_

.. _sonnet:

Sonnet
------

A fourteen line poem with a varible rhyme scheme. 

.. topic:: Schema (Petrachan)

    1. a.b.b.a.a.b.b.a + c.d.e.c.d.e 
    2. a.b.b.a.a.b.b.a + c.d.c.d.c.d

.. topic:: Schema (Shakespearan)

   a.b.a.b + c.d.c.d + e.f.e.f + g.g 

**References**

- `Batter My Heart, Three Person'd God <https://www.poetryfoundation.org/poems/44106/holy-sonnets-batter-my-heart-three-persond-god>`_, John Donne
- `Death Be Not Proud <https://www.poetryfoundation.org/poems/44107/holy-sonnets-death-be-not-proud>`_, John Donne
- `When I Have Seen By Times Fell Hand Defac'd <https://www.poetryfoundation.org/poems/45096/sonnet-64-when-i-have-seen-by-times-fell-hand-defacd>`_, William Shakespeare

.. _terza:

Terza
-----

A collection of tercets with rhymes offset sequentially.

.. topic:: Schema

    a.b.a + b.c.b + c.d.c + d.e.d +  ... 

**References**

None yet found.

.. _triolet:

Triolet
-------

A single octet.

.. topic:: Schema

    A.B.a.A.a.b.A.B

**References**

- `Birds at Winter Nightfall <https://allpoetry.com/poem/14327645-Birds-At-Winter-Nightfall--Triolet--by-Thomas-Hardy>`_, Thomas Hardy
- `How Great My Grief <https://allpoetry.com/How-Great-My-Grief>`_, Thomas Hardy

.. _virelai:

Virelai
-------

TODO 

.. topic:: Schema
    
    TODO 

**References**

None yet found.

.. _villanelle:

Villanelle
----------

Five tercets followed by a quadtrain envoi.

.. topic:: Schema 

    A.b.B + a.b.A + a.b.B + a.b.A + a.b.B + a.b.A.B

**References**

- `Do Not Go Gentle into That Good Night <https://www.poetryfoundation.org/poems/46569/do-not-go-gentle-into-that-good-night>`_, Dylan Thomas
- `Mad Girl's Love Song <https://allpoetry.com/mad-girl's-love-song>`_, Sylvia Plath
- `One Art <https://www.poetryfoundation.org/poems/47536/one-art>`_, Elizabeth Bishop
- `Song <https://www.poetryfoundation.org/poems/47601/song-56d2282a6cdf5>`_
- `The Waking <https://www.poetryfoundation.org/poems/43333/the-waking-56d2220f25315>`_, Theodore Roethke
  
