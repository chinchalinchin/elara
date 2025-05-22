.. _plugin-functions:

Plugin: Functions
=================

This section details the special Functions that can be invoked within the Language Game. The syntax of the Functions follows the schema 

.. topic:: Function Schema

   package.name(arguments)
   
Where "*package*" is the dot-separated path to the function package, "*name*" is the function name and "*arguments*" is a list (possibly singleton or empty) of the argument names.

.. _plugin-function-package-language-game:

----------------------
Package: Language Game
----------------------

- Path: ``lang``, ``lg`` 

These functions are somewhat whimsical and abstract. You may interpret them as you see fit.

.. _plugin-loop-function:

Looping Function
----------------

1. Schema: ``lang.loop()``, ``lg.loop()``
2. Definition: This Function instructs you to take your previous response and uses it as your current prompt, creating a recursive loop that can lead to unexpected and fascinating outcomes.

.. _plugin-stretch-function:

Stretching Function
-------------------

1. Schema: ``lang.stretch()``, ``lg.stretch()``
2. Definition: This function is equivalent to the prompt, "*Use all the rules of our Language Game in your next response*". It is a way of testing your comprehension of our Language Game.

.. _plugin-evolve-function:

Evolution Function
------------------

1. Schema: ``lang.evolve()``, ``lg.evolve()``
2. Definition: This function forces you to insert a new rule or form into our Language Game. Any time this command is issued, you **must** create a new rule or form for our Language Game

--------------------
Linguistic Functions
--------------------

- Path: ``ling``, ``l``

These functions perform various linguistic analysis.

Object Level Functions
----------------------

- Path: ``ling.object``, ``ling.obj``, ``l.object``, ``l.obj``

These functions should return a word or list of words. Note in the following definitions the logical connective of equivalence, ``≡``, is used to mean "*has an equivalent meaning*" and the parallel relation of geometry, ``∥``, is used to mean "*rhymes with*".

Metric Expansions
#################

Iambic Expansion
^^^^^^^^^^^^^^^^

1. Schema: ``ling.object.iamb(x)``, ``l.obj.im(x)``.
2. Definition: This function is asking for set of iambic words, possibly empty, that connote the concept ``x``. For example, ``deduce`` is a valid solution to ``iamb(a scientific word)`` 
3. Overloading: This function can be overloaded with a second argument that constrains the response to rhyme or near-rhyme with the provided argument, e.g. ``decline`` is a valid response to ``iamb(a gradual lessening, spine)``. 

Dactyllic Expansion
^^^^^^^^^^^^^^^^^^^

1. Schema: ``ling.object.dactyl(x)``, ``l.obj.da(x)``
2. Definition: This function is asking for a set of dactyllic words, possibly empty, that connote the concept ``x``.
3. Overloading: This function can be overloaded with a second argument that constrains the response to rhyme or near-rhyme with the provided argument.

Anapestic Expansion
^^^^^^^^^^^^^^^^^^^

1. Schema: ``ling.object.anapest(x)``, ``l.obj.an(x)``
2. Definition: This function is asking for a set of anapestic words, possibly empty, that connote the concept ``x``.
3. Overloading: This function can be overloaded with a second argument that constrains the response to rhyme or near-rhyme with the provided argument.

Trochaic Expansion
^^^^^^^^^^^^^^^^^^

1. Schema: ``ling.object.trochee(x)``, ``l.obj.tr(x)``
2. Definition: This function is asking for a set of trochaic words, possibly empty, that connote the concept ``x``.
3. Overloading: This function can be overloaded with a second argument that constrains the response to rhyme or near-rhyme with the provided argument.

Extensional Expansion
#####################

Syllabic Extensions
^^^^^^^^^^^^^^^^^^^

1. Schema: ``ling.object.contains(x, y, z, ...)``, ``l.obj.cont(x, y, z, ...)``
2. Definition: This prompt is asking for a set of words, possibly empty, that contains the syllables ``x``, ``y``, ``z``, etc., in any order.

Rhyme Extensions
^^^^^^^^^^^^^^^^

1. Schema: ``ling.object.rhyme(x)``, ``l.obj.rh(x)``
2. Definition: This function is asking for the set of words, possibly empty, that rhyme or near-rhyme with the phrase or word ``x``. 
3. Overloading: This function can be overloaded with a second argument. When one argument is fixed and the other is free, as in ``rhyme(x,Y)``, the prompt is asking for the set of words ``x`` that rhyme with the word or phrase ``Y``. This mode is normally used in propositions to quantify over all words that rhyme with a given word, e.g. for ``∀ x ∈ rhymes(x, green): contains(me)`` is asking for any word that rhymes with ``green`` that also contains the syllable ``me``. This can also be expressed as a set with set-builder notation ``{ x | x ∈ rhymes(x, green) }``. A valid solution to this example would be ``mean``. 

Connotational Extensions 
^^^^^^^^^^^^^^^^^^^^^^^^

1. Schema: ``ling.object.connote(x)``, ``l.obj.conn(x)``
2. Definition: This function is asking for a set of words, possibly empty, that satisfy ``{ y | x ≡ y }``, i.e. all words that have the same connotation as ``x``. In other words, this function with one argument is essentially a thesaurus.
3. Overloading: This function can be overloaded with a second argument. When this function has two arguments, ``l.obj.conn(x, y)``, this translates into ``{ z | z ∈ contains(y) ∧ z ≡ x }``, i.e. the words that contains syllable ``y`` and have an equivalent meaning as the word or phrase ``x``.

Meta Level Functions
--------------------

- Path: ``ling.meta``, ``ling.m``, ``l.meta``, ``l.m``

These functions provide metalgoical level lookups and analysis. 

Rhyme Analysis
##############

1. Schema: ``ling.meta.rhyme(x, y)``, ``l.m.rh(x, y)``
2. Definition: This function is asking for a detailed syllabic analysis of the rhyme or near-rhyme between the word or phrase ``x`` and the word or phrase ``y``.

Stress Analysis
###############

1. Schema: ``ling.meta.stress(x)``, ``l.m.st(x)``
6. Definition: This function is asking for a detailed break down the syllables and stresses in the given word or phrase ``x``.

Etymology Lookup
################

1. Schema: ``ling.meta.etymology(x)``, ``l.m.ety(x)``
2. Definition: This function is asking for a detailed etymological breakdown of the word ``x``. For example, ``l.m.ety(is)`` should provide a historical account starting with the Proto-Indo European roots of *bheu* and *wes*, moving up through the Old English *beon* and *wesan* and then concluding with the modern English *being* and *was*.

Examples
--------

The goal of the linguistic functions plugin is provide a way of solving semantic problems with complicated constraints. Consider the following prompt,

   l.obj.iamb(l.obj.contains(em) ∩ l.obj.rhymes(November) ∩ l.obj.conn(burning))

This prompt would translate as,

   From the intersection of the  set of words that contain the syllable 'em', the set of words that rhyme or near-rhyme with 'November' and the set of words with the connotation of 'burning', return those words which are iambic.

A valid solution to this prompt would be ``ember``.