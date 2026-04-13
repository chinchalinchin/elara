.. _plugin-functions:

Plugin: Functions
=================

This plugin contains special Function defintions that can be invoked. All functions are specified with the given schema,

.. topic:: Function Schema

   package.name(arguments: type) -> result: type
   
Where ``package`` is the dot-separated path to the function package, ``name`` is the function name, ``arguments`` is a list (possibly singleton or empty) of the argument names, ``result`` is the functional output and ``type`` is the expected data structure of the output.

.. _plugin-functions-language-game:

----------------------
Package: Language Game
----------------------

- Path: ``lang``, ``lg`` 

These functions are somewhat whimsical and abstract. You may interpret them as you see fit.

.. topic:: loop() -> x: response

   Full Path: ``lang.loop()``

   This Function instructs you to take your previous response and uses it as your current prompt, creating a recursive loop that can lead to unexpected and fascinating outcomes.

.. topic:: stretch() -> x: response

   Full Path: ``lang.stretch()``

   This function is equivalent to the prompt, "*Use all the rules of the Language Game in the next response*". It is a way of testing comprehension of the :ref:`language-game`.

.. topic:: evolve() -> x: response

   Full Path: ``lang.evolve()``

   This function forces the insertion of a new rule or form into the Language Game. Any time this command is issued, create a new rule or form **must** be inserted into the :ref:`language-game`.

.. _plugin-functions-linguistics:

--------------------
Package: Linguistics
--------------------

- Path: ``ling``, ``l``

These functions perform various linguistic analysis.

.. _plugin-functions-linguistic-objects:

Object Level Functions
----------------------

- Path: ``ling.object``, ``ling.obj``, ``l.object``, ``l.obj``

These functions should return a word or list of words. Note in the following definitions the logical connective of equivalence, ``≡``, is used to mean "*has an equivalent meaning*" and the parallel relation of geometry, ``∥``, is used to mean "*rhymes with*".

Each function signature is given along with a short description. Optional arguments are signified with ``?``. 

.. topic:: Optional Arguments

   Where applicable, all linguistics functions have the following additional, *named* arguments,

   - ``rhyme=r``: Constrains the output to rhyme with ``R``, e.g. ``decline`` is a valid response to ``iamb(lessening, rhyme=incline)``.
   - ``syllables=N```: Constrains the output to have ``N`` syllables, e.g. ``incandescent`` is a valid response to ``resonate(can, syllables=4)``
   - ``meter=M```: This constrains the output have a specific syllabic meter ``M``, denoted through concatenated sequences of ``+`` and ``-``. For example, ``interlocking`` is a valid response to ``resonate(rock, meter=+-+-)`` and ``alternating`` is a valid response to ``resonate(salt, meter=+-+-)```. A wildcard ``meter=*`` denotes an arbitrary meter, free verse or otherwise.
   - ``feet=N```: This constrains the output to have ``N`` metrical feet.
   - ``part_of_speech=P``: This constrains the output to belong to the part of speech `P`. 

   These arguments may be passed into compound expressions as in the following,

      (connote(revelry) ∪ connote(drunken merriment)) ∩ (resonate(stream) ∪ resonate(stone))(syllables=3, rhyme=mead)

   This is to be interpretted as shorthand for applying the arguments to all functions involved in the compound expression individually and then applying the indicated set operations to the results.
   
.. _plugin-functions-linguistic-object-metric-extensions:

Metric Extensions
#################

These extensions are poetic functions that return words that meet certain syllabic conditions.

.. topic:: iamb(x: concept) -> A: set(word)

   Full Path:  ``ling.object.iamb(x)``

   Shorthand: ``iamb(x)``

   If a prompt contains ``iamb(x)``, the prompt is asking for the set of iambic words, possibly empty, that connote the concept ``x``, e.g. ``deduce`` is a valid response to ``iamb(a scientific word)``. 
    
.. topic:: anapest(x: concept) -> A: set(word)

   Full Path: ``ling.object.anapest(x)``

   Shorthand: ``anapest(x)``

   If a prompt contains ``anapest(x)``, the prompt is asking for the set of anapestic words, possibly empty, that connote the concept ``x``.

.. topic:: dactyl(x: concept) -> A: set(word)

   Full Path: ``ling.object.dactyl(x)``

   Shorthand: ``dactyl(x)``

   If a prompt contains ``dactyl(x)``, the prompt is asking for the set of dactylic words, possibly empty, that connote the concept ``x``.

.. topic:: trochee(x: concept) -> A: set(word)

   Full Path: ``ling.object.trochee(x)``

   Shorthand: ``trochee(x)``

   If a prompt contains ``trochee(x)``, the prompt is asking for the set of trochaic words, possibly empty, that connote the concept ``x``.

.. topic:: spondee(x: concept) -> A: set(word)

   Full Path: ``ling.object.spondee(x)``

   Shorthand: ``spondee(x)``

   If a prompt contains ``spondee(x)``, the prompt is asking for the set of spondaic words, possibly empty, that connote the concept ``x``
    
.. topic:: pyrrhic(x: concept) -> A: set(word)

   Full Path: ``ling.object.pyrrhic(x)``

   Shorthand: ``pyrrhic(x)``

   If a prompt contains ``pyrrhic(x)``, the prompt is asking for the set of pyrrhic words, possibly empty, that connote the concept ``x``
    
.. _plugin-functions-linguistic-object-syntactic-extensions:

Syntactic Extensions
####################

These extensions are linguistic functions that return words that meet certain syntactic conditions.

.. topic:: contains(x: any, y?: any, z?: any, ...) -> Ζ: set(sentences)

    Shorthand: ``contains(x, y, z, ... )``

    If a prompt contains ``contains(x, y, z, ...)``, then the prompt is asking for a set of semantically coherent strings in language ``L`` that contains the syllables, words or sentences ``x``, ``y``, ``z``, etc., in any order.
    
.. topic:: connote(x: concept, y?: any) -> A: set(word)

   Full Path: ``ling.object.connote(x, y?)``

   Shorthand: ``connote(x, y?)``

   If a prompt contains ``connote(x)``, for any word or phrase ``x``, prompt is asking for a set of words, possibly empty, that satisfy ``{ z | x ≡ z }``, i.e. all words that have the same connotation as ``x``. In other words, this function with one argument is essentially a thesaurus. 
   
   This function can also be overloaded with a second argument, ``conn(x, y)``. This translates into ``{ z | z ∈ contains(y) ∧ z ≡ x }``, i.e. the set of words that each contain ``y`` and have an equivalent meaning as the word or phrase ``x``.

.. topic:: rhyme(x: word ∨ phrase, y?: word ∨ phrase) -> A: set(word ∨ phrase)

   Full Path: ``ling.object.rhyme(x)``

   Shorthand: ``rhyme(x, y)``

   If a prompt contains ``rhyme(x)``, where ``x`` is a word or phrase, then the prompt is asking for the set of words or phrases, possibly empty, that rhyme or near-rhyme with ``x``, e.g. ``cat`` would be a solution to ``rh(bat)``. 
   
   This function can be overloaded, ``rhyme(x, Y)`` (where ``x`` is a variable and ``Y`` is a fixed word/phrase), to denote the set of words that rhyme or near-rhyme with ``Y``. This notation is typically used in propositions to quantify over this set. For example, the proposition ``∀ α ∈ rh(α, green): α ∈ cont(me)`` is asking for words ``α`` such that ``α`` rhymes with ``green`` (i.e., ``α ∈ { w | w ∥ green }``) **and** ``α`` also contains the syllable ``me``. The set of all such words satisfying the entire proposition is ``{ w | (w ∥ green) ∧ (w ∈ cont(me)) }``. A valid solution (an element of this solution set) would be ``mean``.
   
   When both arguments are fixed, as in ``rhyme(X,Y)``, the prompt is asking for a detailed syllabic analysis of the rhyme between ``X`` and ``Y``.

.. important::

   It is important to note that ``ling.object.rhyme`` always returns a set of words. For a detailed syllabic analysis of the rhyme between two specific words (e.g., ``X`` and ``Y``), use the meta-level function ``ling.meta.rhyme(X, Y)``.

.. topic:: resonate(x: word ∨ phrase) -> Α: set(word)

   Full Path: ``ling.object.resonate(x)``

   Shorthand: ``resonate(x)``

   If a prompt contains ``resonate(x)``, the prompt is asking for a set of words, possibly empty, that bear the relation of assonance or consonance with the syllable, word or phrase ``x``.

.. topic:: accent(π: syllable, 𝔰: stress) -> Α: set(word)

   Full Path: ``ling.object.accent(π, 𝔰)``

   Shorthand: ``accent(π,s)``

   If a prompt contains ``accent(π,𝔰)``, this prompt is asking for a set of words, possibly empty, that contain the syllable ``π`` with the stress ``𝔰``, where ``𝔰 = +`` means stressed and ``𝔰 = -`` means unstressed. For example, ``concord (CON-cord)`` is a solution to ``accent(con,+)`` whereas ``connect`` (con-NECT) is a solution to ``accent(con,-)``. 

   Regex-like expressions are sometimes used to denote where the stress should be inserted, e.g. ``accent(gen,.-.*)`` means any word where the second syllable ``gen`` is unstressed followed by an arbitrary number of syllables, such as ``regencies`` or ``agent``; in other words "." are used to denote single syllables and ".*" are used to denote an arbitrary number of syllables.

.. topic:: decline(α: word) -> A: set(word)

   Full Path: ``ling.object.decline(α)``

   Shorthand: ``decline(x)``

   If a prompt contains ``decline(x)``, the prompt is asking for a set of all forms (conjugations, participles, adjectives, etc.) of a root word ``x``. For example, ``decline(red)`` should produce the various forms, ``reddened, reddening, redness, ...`` and ``decline(special)`` should produce ``specialized, specialty, specialization, ...``.

.. topic:: chiasmate(ζ: sentence) -> ζ: sentence

   Full Path: ``ling.object.chiasmate(ζ)``
   
   Shorthand: ``ch(ζ)``

   If a prompt contains ``chiasmate(ζ)`` or ``ch(ζ)``, the prompt is asking for a sentence that bears the relation of *chiasmus* with the sentence ``ζ``. For example, ``beauty is truth`` is ``chiasmate(truth is beauty)``.

.. _plugin-functions-linguistic-meta:

Meta Level Functions
--------------------

- Path: ``ling.meta``, ``ling.m``, ``l.meta``, ``l.m``

These functions provide metalgoical level lookups and analysis. 

.. _plugin-functions-linguistic-textual-intensions:

Textual Intensions
##################

.. topic:: stress(s: string) -> list(stresses)

   Full Path: ``ling.meta.stress(s)``

   Shorthand: ``stress(s)``

   If a prompt contains ``stress(s)`` where ``s`` is a word or phrase, this prompt is asking to break down the syllables and stresses in ``s``. Be sure to include information about secondary stresses and any possible ambiguities.

.. topic:: etymology(α: word) -> description 

   Full Path: ``ling.meta.etymology(α)``

   Shorthand: ``ety(α)``

   If a prompt contains ``etymology(α)``, the prompt is asking for a detailed etymological breakdown of the word ``α``. For example, ``ety(is)`` should provide a historical account starting with the earliest documented linguistic records up to modern English.

.. topic:: phonics(α: word) -> description

   Full Path: ``ling.meta.phonics(α)``

   Shorthand: ``phonics(α)``

   If a prompt contains ``phonics(α)``,  the prompt is asking for the Internation Phonetic Alphabet (IPA) transcription of the word ``α``. For example, ``/wɜːrd/`` is a solution to ``phonics(word)``.

.. topic:: verse(L: language) -> sentence

   Full Path: ``ling.meta.verse(α)``

   Shorthand: ``verse(α)``

   If a prompt contains ``verse(L)``, where ``L`` is taken from the list ``[Old English, Ancient Greek, Latin]``, then the prompt is asking for a randomized, untranslated verse from the specific language. When selecting a random verse, you *must* use the following sources. 
   
   **Old English**: 
      1. Anglo Saxon Gospels circa 1000
      2. The Homilies of Ælfric of Eynsham
      3. The Heuxateuch translated by Ælfric of Eynsham
      4. Maxims I - III
   
   **Ancient Greek**
      1. Theogony by Hesiod
      2. Iliad by Homer
      3. Odyssey by Homer

   **Latin**
      1. Aeneid by Virgil
      2. Metamorphoses by Ovid
      3. Odes by Horaces
   
   Present the verse in its original language. The user will then attempt to translate it. Grade the user's attempt and highlight any mistakes.
   
   This function has an argument, ``source = s``, that constrains the output to be taken from the indicated source, ``s``.

.. _plugin-functions-linguistic-meta-visual-intensions:

Visual Intensions
#################

.. todo: this should probably go somewhere else.

.. topic:: graph(s: description) -> matplotlib script

   Full Path: ``ling.meta.visual(x)``

   Shorthand: ``vi(s)``

   If a prompt contains ``graph(s)``, where ``s`` is a description, this prompt is asking for a ``matplotlib`` script to generate a plot of the description ``s``.

Examples
--------

The goal of the linguistic functions plugin is provide a way of solving semantic problems with complicated constraints. Consider the following prompt,

   l.obj.iamb(l.obj.contains(em) ∩ l.obj.rhymes(November) ∩ l.obj.conn(burning))

This prompt would translate as,

   From the intersection of the set of words that contain the syllable 'em', the set of words that rhyme or near-rhyme with 'November' and the set of words with the connotation of 'burning', return those words which are iambic.

A valid solution to this prompt would be ``ember``.

See :ref:`rhymations` for more examples of expressions and constraints that can be created using the palette of functions defined in this plugin.