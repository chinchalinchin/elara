
.. _palindromics-section-i-i:

Section I.I: Formalization
==========================

.. note::

    All of the terminology presented in this section will be elaborated upon in the subsequent sections.

.. _palindromics-conventions:

Conventions
-----------

General conventions adopted throughout the course of this work are  given below.

1. :math:`N_n` will represent the set of natural numbers starting at 1 and ending at *n*, 

.. math::

    N_n = \{ 1, 2, ... , n \}

2. The cardinality of a set :math:`A` will be denoted :math:`\lvert A \rvert`

3. ∎ will be used to denote the ending of all examples and proofs. 

4. The terms "*set*" and "*class*" are used interchangeably. 

5. The Capital Gothic letters :math:`\mathfrak{F}, \mathfrak{G}` are reserved for functions. Functions will be written :math:`\mathfrak{F}: \mathbb{D} \to \mathbb{R}`, where :math:`\mathbb{D}` is the domain of the function and :math:`\mathbb{R}` is the co-domain of the function.

.. _palindromics-constants:

Constants
---------

.. _palindromics-empty-character:

.. topic:: Constant: Empty Character

    **Empty Character**
        :math:`\varepsilon`

    The *Empty Character* is a null Character, or a Character that lacks content.

.. warning::

    It is **incorrect** to treat the empty quotation marks "" as the English "*Empty Character*". Empty Characters **do not exist** in Language. In other words, :math:`\varepsilon` does not get assigned a value under an interpretation (model), unless :math:`\varepsilon` itself is being treated as a symbol. In such cases, :math:`\hat{\varepsilon}` will be used to refer to the *physical inscription* of the Character assigned to represent the Empty Character.


.. _palindromics-delimiter-character:

.. topic:: Constant: Delimiter Character

    **Delimiter**
        :math:`\sigma`
    
    The *Delimiter Character* (or just *the Delimiter*) is a Character used to separate the occurrence of Words in a String. This Character will play a central role in the development of palindromic structures. 
    
    Under the assignment :math:`L = L_{\text{english}}`, the Delimiter corresponds to an space " ".

.. _palindromics-terms:

Terms
-----

.. _palindromics-strings:

.. topic:: Term: Strings

    **Strings**
        - :math:`s_1, s_2, s_3, ...`

    The lowercase English letter :math:`s` with subscripts will be used to represent Strings.

    **String Variables**
        - :math:`s, t, u, v, w`
    
    The lowercase English letters :math:`s, t, u, v, w` will represent Strings Variables, i.e indeterminate Strings. 

.. _palindromics-characters:

.. topic:: Term: Characters
    
    **Characters** 
        - :math:`\mathfrak{a}, \mathfrak{b},  \mathfrak{c}, ...`
        - :math:`\mathfrak{a}_1, \mathfrak{a}_2, \mathfrak{a}_3, ...`
    
    Lowercase Fraktur letters represent Characters. Subscripts will occasionally be used in conjunction with Fraktur letters to denote Characters at specific positions within Strings. 

    **Character Variables**
        - :math:`\iota, \nu, \omicron, \rho`
        - :math:`\iota_1, \iota_2, \iota_3, ...`

    The Lowercase Greek letters Rho, Omicron, Iota and Nu will represent Character Variables, i.e. indeterminate Characters. Subscripts will occasionally be used with Iota to denote Character Variables.

.. important::

    The exact meaning of these symbols should be attended with care. :math:`\mathfrak{a}, \mathfrak{b},  \mathfrak{c}, ...` represent Characters of the Alphabet and thus are all unique, each one representing a different linguistic element. When Character symbols are used with subscripts, :math:`\mathfrak{a}_1, \mathfrak{a}_2, \mathfrak{a}_3, ...`, they are being referenced in their capacity to be ordered within a String. With this notation, it is not necessarily implied :math:`\mathfrak{a}_1` and :math:`\mathfrak{a}_2` are unequal Character-wise, but that they are differentiated only by their relative order in a String.

    Likewise, when Character Variables are used with subscripts, it is meant to refer to the capacity of a Character Variable to be indeterminate at a *determinate position* within a String. 
    
    Moreover, the range of a Character Variable is understood to be the Alphabet :math:`\Sigma` from which it is being drawn.

.. _palindromics-words:

.. topic:: Term: Words

    **Words**
        - :math:`a, b, c, ...`
        - :math:`a_1, a_2, a_3, ...`

    Lowercase English letters represent Words. Subscripts will occasionally be used to denote Words.

    **Word Variables**
        - :math:`\alpha, \beta, \gamma, ...`
        - :math:`\alpha_1, \alpha_2, \alpha_3, ...`

    The Lowercase Greek letters Alpha, Beta and Gamma will represent variable Words, i.e. indeterminate Words. Subscripts will occasionally be used to denote Word Variables.

.. _palindromics-phrases:

.. topic:: Term: Phrases

    **Phrase Variables**
        - :math:`p, q, r`
        - :math:`p_1, p_2, p_3, ...`

    The lowercase English letters :math:`p, q, r` are reserved for Phrase variables, i.e. indeterminate Phrases. Subscripts will occasionally be used to denote Phrase Variables.

.. _palindromics-sentences:

.. topic:: Term: Sentences
    
    **Sentences**
        - :math:`ᚠ, ᚢ, ᚦ, ...`
        - :math:`ᚠ_1, ᚠ_2, ᚠ_2, ...`

    Anglo-Saxon Runes will represent Sentences. Subscripts will occasionally be used in conjunction with Runes to denote Sentences. 

    **Sentence Variables**
        - :math:`\zeta, \xi`
        - :math:`\zeta_1, \zeta_2, \zeta_3, ...`

    The lowercase Greek letter Zeta and Xi are reserved for indeterminate Sentences, i.e. Sentence Variables. Subscripts will occasionally be used in conjunction with Zeta to denote Sentence Variables.

.. _palindromics-sets:

Sets
----

.. _palindromics-finite-strings:

.. topic:: Set: Finite Strings

    **Finite Strings** 
        - :math:`S`

    The set of *all finite Strings* will be regarded as the domain of discourse. 

    **Canon**
        - :math:`\mathbb{S}`

    The *Canon* is the image of :math:`S` under Canonization.

.. _palindromics-alphabet:

.. topic:: Set: Alphabet

    **Alphabet**
        - :math:`\Sigma`

    The aggregate of all non-Empty Characters is called the *Alphabet*.

    **Total Alphabet**
        - :math:`\Sigma_e`

    The aggregate of all Characters is called the *Total Alphabet*

.. _palindromics-language:

.. topic:: Set: Language

    **Language**
        - :math:`L`

    The aggregate of all Words is called the *Language*. Subscripts may be used to indicate a particular Language, e.g. :math:`L_{\text{english}}`

.. _palindromics-phrase-set:

.. topic:: Set: Phrase

    **Phrase**
        - :math:`P_n`, where :math:`n \in \mathbb{N}`

    An ordered set of Words is called a *Phrase*. The subscript :math:`n` is a natural number denoting the number Words in the Phrase.

.. _palindromics-lexicon:

.. topic:: Set: Lexicon

    **Lexicon**
        - :math:`L_n`, where :math:`n \in \mathbb{N}`

    The aggregate of all Phrases of Word Length n is called a *Lexicon*. The subscript :math:`n` is a natural number denoting the number of Words in each Phrase of the Lexicon.

.. _palindromics-dialect:

.. topic:: Set: Dialect

    **Dialect**
        - :math:`D`

    The aggregate of all Limitations is a Dialect.

.. _palindromics-corpus:

.. topic:: Set: Corpus

    **Corpus**
        - :math:`C`

    The aggregate of all Sentences is called a *Corpus*.