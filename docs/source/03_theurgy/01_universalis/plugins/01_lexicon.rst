.. _plugin-lexicon:

Plugin: Lexicon
===============

The Lexicon plugin contains additional symbols, relations and operators and their definitions. This plugin provides an expanded vocabulary.

.. _plugin-lexicon-notation:

--------
Notation
--------

Constants
---------

1. ``σ`` is used to represent delimiters, i.e. spaces. 
2. ``ε`` is used to represent null characters.

Variables
---------

These are general guidelines.

1. ``x``, ``y`` and ``z`` are general variables.
2. ``π `` is used to represent indeterminate syllables, i.e. syllabe variables. 
3. ``ι`` is used to represent indeterminate characters, i.e. character variables. 
4. ``α`` is used to represent indeterminate words, i.e. word variables.. 
5. ``ζ`` is used to represent indeterminant sentences, i.e. sentence variables. 
6. ``p``, ``q`` and ``r`` are reserved for propositional variables.
7. ``n`` and ``m`` are reserved for numerical variables. 
8. ``s`` and ``t`` are reserved for string variables. 

Lowercase letters ``a, b, c, ...`` generally denote elements and uppercase letters ``A, B, C, ...`` generally denote sets. It should be clear from context when this convention is not applied.

Indexing
--------

1. **Character Indexing** For a string ``x``, ``x[i]`` refers to the character at the i:sup:`th` index, where the first character in a string is indexed at 0, e.g ``'hello'[2] = 'l'``.
2. **Word Indexing** For a sentence ``ζ``, ``ζ{i}`` refers to the word at the i:sup:`th` index, where the first word in a sentence is indexed at 0, e.g. ``'hello person how are you'{2} = 'how'``.

.. _plugin-lexicon-sets:

----
Sets
----

1. **Language** The symbol ``L`` refers to the set of all words in a language. If a language other than English is intended, it will be included in a subscript, e.g. L:sub:`spanish`.

2. **Corpus** The symbol ``C:sub:L`` refers to the set of all sentences in a language ``L``. 

3. **Metric Words** The symbol ``M:sub:S`` refers to the set of all words that satisfy the syllabic pattern ``S``, where ``S`` is a concatenated sequence of syllabic stresses such that ``+`` means stressed and ``-`` means unstressed. For example, ``M:sub:-+`` refers to the set of all iambic words.

4. **Reflective Words** The symbol ``R`` refers to the set of all reflective words, i.e. words that are spelled the same forwards as backwards. Mathematically, if ``α[i]`` stands for the i:sup:`th` character in word ``α``, then a reflective word is defined as the words which satisfy the relation ``α[i] = α[l(α)-i-1]``. For example, ``nun`` is a reflective word.

5. **Invertible Words** The symbol ``I`` refers to the set of invertible words. Mathematically, ``I`` is the set of word ``α`` that satisfy the definition, ``α ∈ I ↔  inv(α) \in L``. For example, ``time`` is invertible word because ``inv(time) = emit`` and ``emit ∈ L`` whereas ``hello`` is not invertible because ``inv(hello) = olleh`` and ``olleh ∉ L``.

6. **Palindromes** The symbol P refers to the set of palindromes. Mathematically, a string ``x`` is palindromic if it satisfies the definition ``x ∈ P ↔ (ς(x) = inv(ς(x)))``. For example, ``borrow or rob`` is a palindrome because ``ς(borrow or rob) = inv(ς(borrow or rob)) = borroworrob``.

.. _plugin-lexicon-relations:

---------
Relations
---------

1. **Rhymes** The geometric symbol for the relation of parallel ``∥ (U+2225)`` is used to mean "*rhymes with*" in the context of linguistics. 

2. **Synonymity** The logical equivalence symbol ``≡ (U+2261)`` is used to mean "*has an equivalent meaning*" in the context of linguistics. This can be thought of as an extension of the relation of "*synonym*". For example, "*car*" and "*automobile*" satisfy this relation, but even more complex sentences like "*Venus is the Morning Star*" and "*Venus is the Evening Star*" are equivalent. Taken to the extreme, "*The man bought a sandwich*" and "*The sandwich, after being meticulously assembled by the delicatessen employee, was purchased by the man*" are both linguistic objects that satisfy this relation.

3. **Antonymity** The logical nonequivalence symbol ``≢ (U+2262)`` is used to mean "*has an opposite meaning*" in the context of linguistic. This can be thought of as an extension of the relation of "*antonym*". For example, "*big*" and "*small*" satisfy this relation, but even more complex sentences like "*A bird flying high*" and "*a fish swimming deep*" satisfy this relation.


.. _operations:

----------
Operations
----------

1. **String Length** The number of characters in a string ``x`` is denoted ``l(x)``.

2. **Word Length** The number of *non-overlapping* words in a string ``x`` is denoted ``w(x)``.

3. **String Inversion** A string inversion, ``inv(x)``, is an operation that reverses the order of characters in a string, e.g. ``inv(hello) = olleh``. 

4. **String Reduction** A string reduction, ``ς(x)``, is an operation that removes all delimiters from a string, but preserves the relative order of characters, e.g. ``ς(hello gemini how are you) = hellogeminihowareyou``.

5. **Selection** A selection, ``[λx: f(x)]``, is understood to be any single indeterminate element ``x`` that satisfies ``f(x)``. In other words, ``[λx: f(x)]`` is a single object, *not a set*. For example, ``[λx: x ∈ M:sub:+-]`` refers to an iambic word, e.g. ``import``. 

6. **Concatenation** For any two strings ``x`` and ``y``, their concatenation is written ``xy``. The operands of concatenation are often grouped with brackets, e.g. ``xy = [x][y]``.

7. **Succession** For any two strings ``x`` and ``y``, their succession, denoted, ``x.y`` is to mean the literal transcription of the strings on separate new lines. Exponents are used as shorthand for denoting multiple successions, e.g. ``line(x).line(x) = line(x)^2``

8. **Separation** For any two strings ``x`` and ``y``, their separation, denoated ``x + y`` is to meant the literal transcriptions of the strings on separate new lines with a blank line in between them (i.e., *separation* creates stanzas). Summations are used as shorthand for denoting multiple separations, ``Σ:sub:`1`:sup`n` x.y`` denotes ``n`` stanzas of couplets (two lines). 