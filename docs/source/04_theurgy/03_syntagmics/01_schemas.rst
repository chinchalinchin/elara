
.. _schemes:

Schemes
=======

.. _ballad:

Ballad
------

.. topic:: Schema

    .. math::

        \sum_1^{n} \overline{(a/\mathfrak{i}_4).(b/\mathfrak{i}_3).(a:c/\mathfrak{i}_4).(b/\mathfrak{i}_3)}

**References**

- `A tragical ballad of the unfortunate loves of Lord Thomas and fair Eleanor`_, Frances James Child
- `The Ballad of the Goodly Fere`_, Ezra Pound
- `The Ballad of Sir Patrick Stern`_, W. Scott
- `La Belle Dame sans Merci`_, John Keats
- `Lord Thomas and Annet`_, Old English Ballad
- `Tam Lin`_, Old Scottish Ballad

.. _ballade: 

Ballade
-------

.. topic:: Schema
    
    .. math::

        a.b.a.b.b.c.b.C + a.b.a.b.b.c.b.C + a.b.a.b.b.c.b.C + b.c.b.C

    :ref:`Reducing <syntagmics-shorthand>`,

    .. math::

        \overline{[\sum_1^3 {[a.b]^2}.b.c.b.C] + b.c.b.C}

.. topic:: Schema (Ballade Royal)

    .. math::

        [a.b.a + b.b + c.c]:[a.b.a.b + b.c.c]

    :ref:`Reducing <syntagmics-shorthand>`,
    
    .. math::

        [a.b.a + b^2 + c^2]:[[a.b]^2 +b.{c^2}]

.. topic:: Schema (Chant Royal)

    .. math::

        \sum_1^{5} \overline{a.b.a.b.c.c.d.d.e.d.E + [d.d.e.d.E:c.c.d.d.e.d.E]}

    :ref:`Reducing <syntagmics-shorthand>`,

    .. math::

        \sum_1^5 \overline{{[a.b]^2}.{c^2}.{d^2}.e.d.E + [{d^2}.e.d.E:{c^2}{d^2}.e.d.E]

**References**

None yet found. 

.. _kyrielle:

Kyrielle
--------

.. topic:: Schema 

    .. math::

        \overline{\sum_1^{n} [a.a.b.B:a.A.b.b]}

    :ref:`Reducing <syntagmics-shorthand>`,

    .. math::

        \overline{\sum_1^n [{a^2}.b.B:a.A.{b^2}]}

**References**

- `A Lark in the Mesh`_, John Payne
- `A Lenten Hymn`_, Thomas Campion

.. _ode:

Ode
---

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

- `Ode on a Grecian Urn`_, John Keats
- `Ode to a Nightingale`_, John Keats
- `Ode to the West Wind`_, Percy Blysse Shelely

.. _ottava:

Ottava
------

.. topic:: Schema (ottava siciliana)

    .. math::

        a.b.a.b.a.b.a.b

    :ref:`Reducing <syntagmics-shorthand>`,

    .. math::

        [a.b]^4

.. topic:: Schema (strambotto)

    .. math::

        a.b.a.b.c.c.d.d

    :ref:`Reducing <syntagmics-shorthand>`,
    
    .. math::
        
        {[a.b]^2}.{c^2}.{d^2}

Each line in a *ottava siciliana* or *strambotto* is a hendecasyllable.

.. topic:: Schema (ottava rima)

    .. math::

        (a.b.a.b.a.b.c.c/\mathfrak{i}_5)

    :ref:`Reducing <syntagmics-shorthand>`,

    .. math::

        ({[a.b]^3}.{c^2}/\mathfrak{i}_5)
        
**References**

None yet found.

.. _pantoum:

Pantoum
-------

.. topic:: Schema

    A.B.C.D + B.E.D.F + E.G.F.H + ... + x.y.C.A

**References**

- `Pantoum of the Great Depression`_, Donald Justice

.. _rondeau:

Rondeau
-------

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
    2. Rondeau Prime: (R)a.b.b.a.a.b.R + a.b.b.a.R
    3. Rondeau: (R)a.a.b.b.a + a.a.b + a.a.b.b.a.R

**Roundel**

.. topic:: Roundel Schema 

    .. math::
    
        a.b.a.R + b.a.b + a.b.a.R 

**References**

- `In Flanders Field`_, John McCrae
- `We Wear the Mask`_, Paul Laurence Dunbar

.. _sestina:

Sestina
-------

Six sestets followed by a tercet envoi.

.. topic:: Schema

    .. math::

        u(\mathrm{A}).v(\mathrm{B}).w(\Gamma).x(\Delta).y(\Epsilon).z(\Zeta) + 
        u(\Zeta).v(\mathrm{A}).w(\Epsilon).x(\mathrm{B}).y(\Delta).z(\Gamma) + 
        u(\Gamma).v(\Zeta).w(\Delta).x(\mathrm{A}).y(\mathrm{B}).z(\Epsilon) +
        u(\Epsilon).v(\Gamma).w(\mathrm{B}).x(\Zeta).y(\mathrm{A}).z(\Delta) +
        u(\Delta).v(\Epsilon).w(\mathrm{A}).x(\Gamma).y(\Zeta).z(\mathrm{B}) +
        u(\mathrm{B}).v(\Delta).w(\Zeta).x(\Epsilon).y(\Gamma).z(\mathrm{A}) + 
        [t_1:t_2] | 
        t1 = ((u \circ \mathrm{A}) \circ \mathrm{B}).((v \circ \Gamma) \circ \Delta).((w \circ \Epsilon) \circ \Zeta),
        t2 = ((u \circ \mathrm{A}) \circ \Delta).((v \circ \mathrm{B}) \circ \Epsilon).((w \circ \Gamma) \circ \Zeta),

.. TODO: I don't think the current definition of projection will ensure `t_1` and `t_2` aren't empty, i.e. I think 
        caesures will satisfy this schema!

**References**

- `Sestina (Bishop)`_, Elizabeth Bishop
- `Sestina of the Tramp-Royal`_, Rudyard Kipling
- `Sestina, Travel Notes`_, 

.. _sonnet:

Sonnet
------

.. topic:: Schema (Petrachan)

    .. math::
    
        a.b.b.a.a.b.b.a + c.d.e.c.d.e:c.d.c.d.c.d

    :ref:`Reducing <syntagmics-shorthand>`,

    .. math::

        a.b.b.{a^2}.{b^2}.a + c.d.e.c.d.e:{[c.d]^3}

.. topic:: Schema (Shakespearan)

    .. math::

        ([\sum_i^{3} \overline{a.b.a.b}] + a.a/\mathfrak{i}_5)

    :ref:`Reducing <syntagmics-shorthand>`,

    .. math::

        ([\sum_i^{3} \overline{{a.b}^2}] + a^2/\mathfrak{i}_5)


.. topic:: Schema (Spenserian)

    .. math::

        (a.b.a.b + b.c.b.c + c.d.c.d + e.e/\mathfrak{i}_5)

.. TODO: need some way of representing the interlocking rhyme scheme. 
..      Some way of recursive defining the index of the sum!
..      This would be useful for pantoums and terzas as well!

**References**

- `Batter My Heart, Three Person'd God`_, John Donne
- `Death Be Not Proud`_, John Donne
- `On the Grasshopper and Cricket`_, John Keats
- `When I Have Seen By Times Fell Hand Defac'd`_, William Shakespeare

.. _terza:

Terza
-----

.. topic:: Schema

    .. math::

        \overline{a.b.a + b.c.b + c.d.c + d.e.d +  ... }

**References**

None yet found.

.. _triolet:

Triolet
-------

.. topic:: Schema

    .. math::

        \overline{(A.B.a.A.a.b.A.B/\mathfrak{i}_4)}

**References**

- `Birds at Winter Nightfall`_, Thomas Hardy
- `How Great My Grief`_, Thomas Hardy

.. _virelai:

Virelai
-------

.. topic:: Schema (Ancien)
    
    .. math::
        
        \overline{a.a.♭b.a.a.♭b.a.a.♭b + b.b.♭c.b.b.♭c.b.b.♭c + ... }

.. topic:: Schema (Nouveau)

    .. math::

        \overline{A_1.b.b.a.A_2 + B_1.c.c.b.B_2 +  ... }
    
**References**

- `July`_, Henry Austin Dobson
- `Spring Sadness`_, John Payne

.. _villanelle:

Villanelle
----------

.. topic:: Schema 

    .. math::

        A_1.b.A_2 + a.b.A_1 + a.b.A_2 + a.b.A_1 + a.b.A_2 + a.b.A_1.A_2

**References**

- `Do Not Go Gentle into That Good Night`_, Dylan Thomas
- `Mad Girl's Love Song`_, Sylvia Plath
- `One Art`_, Elizabeth Bishop
- `Song`_, John Fuller
- `The Waking`_, Theodore Roethke
  
