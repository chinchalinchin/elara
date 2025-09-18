.. _palindromics-section-i:

Section I: Languages & Corpora
==============================

The goal of Section I is to establish the hierarchy of logical relations that govern Strings, Characters, Alphabets, Words, Languages, Sentences and Corpora. As each of these entities is introduced and defined, a new level of relations will be revealed and codified. Palindromic symmetries will manifest on each level, in slightly different but related forms. Each type of symmetry will involve, in some form or another, the concept of :ref:`String Inversion <palindromics-string-inversion>`, to be defined shortly. The essence of a Palindrome lies in binding together the syntactical symmetries at every linguistic layer into a semantic whole. Indeed, it will be seen the symmetrical structure required by Palindromes in turn requires these linguistic layers to have explicit relations and specific synactical properties, regardless of their semantic interpretation.

A *Word* will be considered a *type* of String. Colloquially, a Word can be understood as a String with semantic content, but as this formal system will establish, a Word is not distinguished solely by its semantic content, and in fact, it's semantic interpretation is dependent on prior syntactical conditions that differentiate Words from Strings; This fact is often not made explicit in formal treatmeants of language, but the study of palindromes makes this distinction critical. In the current work, Words will be treated as linguistic entities that are distinguishable by their non-zero length and lack of Delimiters.

Section I will elaborate the necessary syntactic conditions for a String to be considered a formal Word, without taking into account the semantic content that is assigned to it through colloquial use. In other words, this section seeks to formally disentangle the syntactical functions of Words and Strings. 

.. ...................................................
.. .................. SECTION I.I ....................
.. ...................................................

.. _palindromics-section-i-i:

Section I.I: Formalization
--------------------------

.. _palindromics-conventions:

-----------
Conventions
-----------

General conventions adopted throughout the course of this work are  given below.

1. :math:`N_n` will represent the set of natural numbers starting at 1 and ending at *n*, 

.. math::

    N_n = \{ 1, 2, ... , n \}

2. The cardinality of a set :math:`A` will be denoted :math:`\lvert A \rvert`

3. ∎ will be used to denote the ending of all definitions, examples and proofs. 

4. The terms "*set*" and "*class*" are used interchangeably. 

.. _palindromics-constants:

---------
Constants
---------

.. topic:: Constant: Empty Character

    **Empty Character**
        :math:`\varepsilon`

    The *Empty Character* is a null Character, or a Character that lacks content.

    In English, the Empty Character corresponds to an empty quote, "".

.. topic:: Constant: Delimiter Character

    **Delimiter**
        :math:`\sigma`
    
    The *Delimiter Character* (or just *the Delimiter*) is a Character used to separate the occurrence of Words in a String. This Character will play a central role in the development of palindromic structures. 
    
    In English, the Delimiter corresponds to an space " ".

.. _palindromics-terms:

-----
Terms
-----

.. topic:: Term: Strings
    **Strings**
        :math:`s_1, s_2, s_3, ...`

    The lowercase English letter :math:`s` with subscripts will be used to represent Strings.

    **String Variables**
        :math:`s, t, u, v, w, x, y, z`
    
    The lowercase English letters :math:`s, t, u, v, w` will represent Strings Variables, i.e indeterminate Strings. 

.. topic:: Term: Characters
    
    **Characters** 
        :math:`\mathfrak{a}, \mathfrak{b},  \mathfrak{c}, ...`
        :math:`\mathfrak{a}_1, \mathfrak{a}_2, \mathfrak{a}_3, ...`
    
    Lowercase Fraktur letters represent Characters. Subscripts will occasionally be used in conjunction with Fraktur letters to denote Characters at specific positions within Strings. 

    **Character Variables**
        :math:`\iota, \nu, \omicron, \rho`
        :math:`\iota_1, \iota_2, \iota_3, ...`

    The Lowercase Greek letters Rho, Omicron, Iota and Nu will represent Character Variables, i.e. indeterminate Characters. Subscripts will occasionally be used with Iota to denote Character Variables.

.. important::

    The exact meaning of these symbols should be attended with care. :math:`\mathfrak{a}, \mathfrak{b},  \mathfrak{c}, ...` represent Characters of the Alphabet and thus are all unique, each one representing a different linguistic element. When Character symbols are used with subscripts, :math:`\mathfrak{a}_1, \mathfrak{a}_2, \mathfrak{a}_3, ...`, they are being referenced in their capacity to be ordered within a String. With this notation, it is not necessarily implied :math:`\mathfrak{a}_1` and :math:`\mathfrak{a}_2` are unequal Character-wise, but that they are differentiated only by their relative order in a String.

    Likewise, when Character Variables are used with subscripts, it is meant to refer to the capacity of a Character Variable to be indeterminate at a *determinate position* within a String. 
    
    Moreover, the range of a Character Variable is understood to be the Alphabet :math:`\Sigma` from which it is being drawn.

.. topic:: Term: Words

    **Words**
        :math:`a, b, c, ...`
        :math:`a_1, a_2, a_3, ...`

    Lowercase English letters represent Words. Subscripts will occasionally be used to denote Words.

    **Word Variables**
        :math:`\alpha, \beta, \gamma, ...`
        :math:`\alpha_1, \alpha_2, \alpha_3`

    The Lowercase Greek letters Alpha, Beta and Gamma will represent variable Words, i.e. indeterminate Words. Subscripts will occasionally be used to denote Word Variables.

.. topic:: Term: Phrases

    **Phrase Variables**
        :math:`p, q, r`
        :math:`p_1, p_2, p_3`

    The lowercase English letters :math:`p, q, r` are reserved for Phrase variables, i.e. indeterminate Phrases. Subscripts will occasionally be used to denote Phrase Variables.

.. topic:: Term: Sentences
    
    **Sentences**
        :math:`ᚠ, ᚢ, ᚦ, ...`
        :math:`ᚠ_1, ᚠ_2, ᚠ_2`

    Anglo-Saxon Runes will represent Sentences. Subscripts will occasionally be used in conjunction with Runes to denote Sentences. 

    **Sentence Variables**
        :math:`\zeta, \xi`
        :math:`\zeta_1, \zeta_2, \zeta_3, ...`

    The lowercase Greek letter Zeta and Xi are reserved for indeterminate Sentences, i.e. Sentence Variables. Subscripts will occasionally be used in conjunction with Zeta to denote Sentence Variables

.. _palindromics-relations:

---------
Relations
---------

.. topic:: Relation: Character Equality

    For any Characters :math:`\iota, \nu \in \Sigma`, the notion of equality, denoted by :math:`\iota = \nu`, is a primitive concept and assumed to be understood. It is further assumed that Character Equality is an equivalence relation, satisfying reflexivity, symmetry and transitivity,

        1. :math:`\forall \iota \in \Sigma : \iota = \iota`
        2. :math:`\forall \iota, \nu \in \Sigma : \iota = \nu \leftrightarrow \nu = \iota`
        3. :math:`\forall \iota, \nu, \omicron \in \Sigma : (\iota = \nu \land \nu = \omicron) \to (\iota = \omicron)`

.. _palindromics-sets:

----
Sets
----

.. topic:: Set: Finite Strings

    **Finite Strings** 
        :math:`S`

    The *set of all finite Strings* will be regarded as the domain of discourse. 

.. topic:: Set: Alphabet

    **Alphabet**
        :math: `\Sigma`

    The aggregate of all non-Empty Characters is called an *Alphabet*.

.. topic:: Set: Language

    **Language**
        :math:`L`

    The aggregate of all Words is called a *Language*. Subscripts may be used to indicate a particular Language, e.g. :math:`L_{\text{english}}`

.. topic:: Set: Corpus

    **Corpus**
        :math:`C`

    The aggregate of all Sentences is called a *Corpus*.

.. ...................................................
.. .................. SECTION I.II ...................
.. ...................................................

.. _palindromics-strings:

Section I.II: Strings
---------------------

All non-Empty Characters belong to the Alphabet,

.. math::

    \Sigma = \{ \mathfrak{a}, \mathfrak{b}, \mathfrak{c}, ... \}

It is assumed a Delimiter element is non-Empty and belongs to the Alphabet. 

.. _palindromics-axiom-c-1:

.. topic:: Axiom C.1: Delimiter Axiom 

    .. math::

        \sigma \in \Sigma

The aggregate of the Alphabet and the Empty Character is referred to as the *Total Alphabet* and is denoted,

.. math::

    \Sigma_{e} = \Sigma \cup \{ \varepsilon \}

In addition, it is assumed all elements of the Total Alphabet are Strings.

.. _palindromics-axiom-c-2:

.. topic:: Axiom C.2: Character Axiom 

    .. math::
        
        \forall \iota \in \Sigma_{e}: \iota \in S

A Character is the basic unit of a String. In order to construct a String or set of Strings, an Alphabet must be selected. A String is regarded as a linguistic artifact or inscription that is defined entirely by its Characters and their ordering. 

In order to construct more complicated Strings, the operation of concatenation must be defined.

.. _palindromics-concatenation:

-------------
Concatenation
-------------

.. _palindromics-definition-1-2-1:

.. topic:: Definition 1.2.1: Concatenation

    The result of concatenating any two Strings :math:`s` and :math:`t` is denoted :math:`st`. To make the operands clear, parenthesis will sometimes be used, e.g. :math:`s(t) = (s)t = st`. Concatenation is defined inductively through the following schema,

    1. Basis: 
        - :math:`\forall s \in S: s\varepsilon = {\varepsilon}s = s`
    2. Induction: 
        - :math:`\forall s,t,u \in S: (st)u = s(tu)`

Many of the results of regular expressions and automata theory are taken as given and will not be proved, such as the closure of concatenation over :math:`S` (i.e., concatenating two Strings will always yield a String).

**Example** Let :math:`s_1 = \mathfrak{abc}` and :math:`s_2 = \mathfrak{def}`. The concatenation of these two Strings :math:`{s_1}{s_2}` is written,

.. math::

    {s_1}{s_2} = (\mathfrak{abc})(\mathfrak{def}) 
    
Using the Inductive Clause, this concatenation can be grouped into simpler concatenations as follows,    
    
.. math::

    \mathfrak{a}(\mathfrak{b}(\mathfrak{c}(\mathfrak{d}(\mathfrak{ef})))) = (((((\mathfrak{ab})\mathfrak{c})\mathfrak{d})\mathfrak{e})\mathfrak{f}) = \mathfrak{abcdef}

By :ref:`Character Axiom <palindromics-axiom-c-2>`, all Characters are Strings and concatenation is closed under :math:`S`, therefore, :math:`\mathfrak{ef} \in S`. As each nested concatenation is evaluated, the Induction clause in :ref:`palindromics-definition-1-2-1` ensures the next level of concatenation is a String. 

As a result, :math:`{s_1}{s_2} = \mathfrak{abcdef}` and :math:`{s_1}{s_2} \in S` 

∎

.. _palindromics-string-length:

-------------
String Length
-------------

The length of a String is defined as its number of non-Empty Characters.

.. _palindromics-definition-1-2-2:

.. topic:: Definition 1.2.2: String Length

    Let :math:`s = uv` such that :math:`u \in S` and :math:`v \in \Sigma_{e}`. The String Length of :math:`s`, denoted :math:`l(s)`, is defined inductively using the following schema,

    1. Basis: 
        - :math:`l(\varepsilon) = 0`
    2. Induction: 
        - :math:`v = \varepsilon \implies l(s) = l(u)`
        - :math:`v \neq \varepsilon \implies l(s) = l(u) + 1`

**Example** Let :math:`s_1 = \mathfrak{abc}\varepsilon\mathfrak{def}`. Using the :ref:`definition of concatenation <palindromics-definition-1-2-1>`, this can be grouped as :math:`s_1 = (\mathfrak{abc}\varepsilon\mathfrak{de})(\mathfrak{f})`.

Applying the :ref:`definition of String Length <palindromics-definition-1-2-2>` to :math:`\mathfrak{f}` where :math:`u = \mathfrak{f}` and :math:`v = \varepsilon`,

.. math::

    l(\mathfrak{f}) = l(\varepsilon) + 1 = 0 + 1 = 1

.. note::
    
    This same logic generalizes to all Alphabetic Characters,

    .. math::

        \forall \iota in \Sigma: l(\iota) = 1

Applying the :ref:`definition of String Length <palindromics-definition-1-2-2>` with :math:`u = \mathfrak{abc}\varepsilon\mathfrak{de}` and :math:`v = \mathfrak{f}`,

.. math::

    l(\mathfrak{abc}\varepsilon\mathfrak{def}) = l(\mathfrak{abc}\varepsilon\mathfrak{de}) + 1

The first term on the righthand side can be evaluated by applying the :ref:`definition of String Length <palindromics-definition-1-2-2>` with :math:`u = \mathfrak{abc}\varepsilon\mathfrak{d}` and :math:`v = \mathfrak{e}`,

.. math::

    l(\mathfrak{abc}\varepsilon\mathfrak{def}) = (l(\mathfrak{abc}\varepsilon\mathfrak{d}) + 1) + 1

Continuing in this fashion, the result is essentially calculated,

.. math::

    l(s_1) = 6

∎

The definition of String length allows an important shorthand to be defined. This notation introduces nothing new into the system, but significantly improves the readability of proofs.

.. _palindromics-definition-1-2-3:

.. topic:: Definition 1.2.3: Character Index Notation

    Let :math:`s \in S`. Let :math:`i \in \mathbb{N}` such that :math:`1 \leq i \leq l(s)`. The Character at index :math:`i` in :math:`s`, denoted :math:`s[i]`, is defined inductively using the schema, 

    1. Basis:
        - If :math:`s = \varepsilon`, :math:`s[i]` is not defined.
    2. Induction: Let :math:`s = uv` where :math:`v \in \Sigma_{e}`.
        - If :math:`i = l(s)` and :math:`v \neq \varepsilon`, :math:`s[i] = v`
        - If :math:`i \neq l(s)` or :math:`v = \varepsilon`, then :math:`s[i] = u[i]`

.. note::

    The notation :math:`s[i]` is borrowed directly from string slicing in computer science.

The following example shows how the definition of Character indexing "*skips*" over the physical index of Empty Characters and assigns a logical index to any non-Empty Characters in a String.

**Example** Let :math:`s_1 = \mathfrak{ab}\varepsilon\mathfrak{c}`. By :ref:`the definition of String Length <palindromics-definition-1-2-2>`, :math:`l(s_1) = 3`. 

Consider :math:`s_1[3]`. Apply :ref:`the definition of Character Index Notation <palindromics-definition-1-2-3>` with :math:`u_1 =\mathfrak{ab}\varepsilon` and :math:`v_1 = \mathfrak{c}`. :math:`i = l(s_1)` and :math:`v_1 \neq \varepsilon`, therefore, by the Induction clause, :math:`s[3] = \mathfrak{c}`.

Consider :math:`s_1[2]`. Apply :ref:`the definition of Character Index Notation <palindromics-definition-1-2-3>` with :math:`u_1 =\mathfrak{ab}\varepsilon` and :math:`v_1 = \mathfrak{c}`. At this step, :math:`v_1 \neq \varepsilon` but :math:`i \neq l(s_1)`, so the :math:`s_1[i] = u_1[i]`. Note :math:`l(u_1) = 2`.

To find :math:`u_1[i]`, let :math:`u_1 = {u_2}{v_2}` where :math:`u_2 = \mathfrak{ab}` and :math:`v_2 = \varepsilon`. At this step, :math:`i = l(u_1)`, but :math:`v_2 = \varepsilon`, therefore :math:`u_1[i] = u_2[i]`. Note :math:`l(u_2) = 2`.

To find :math:`u_2[i]`, let :math:`u_2 = {u_3}{v_3}` where :math:`u_3 = \mathfrak{a}` and :math:`v_3 = \mathfrak{b}`. At this step, :math:`i = l(u_2)` and :math:`v_3 \neq \varepsilon`, therefore :math:`u_2[i] = v_3 = \mathfrak{b}`.

From this, it follows, :math:`s_1[2] = u_1[2] = u_2[2] = v_3 = \mathfrak{b}`.

∎

The first theorem confirms the well known result that String Length sums over concatenation within the formal system.

.. _palindromics-theorem-1-2-1:

.. topic:: Theorem 1.2.1
    
    The String Length of the concatenation of String :math:`s` and String :math:`t` is equal to the sum of their String Lengths.

    .. math::
        
        \for all s,t \in S: l(st) = l(s) + l(t)

**Proof** The proof proceeds by induction on :math:`t`.

:underline:`Basis`: Let :math:`t = \varepsilon` and :math:`s \in S`. Consider :math:`st = s\varepsilon`.

By the :ref:`basis clause of concatenation <palindromics-definition-1-2-1>`, :math:`s\varepsilon = s`. By the :ref:`basis clause of String Length <palindromics-definition-1-2-2>`, :math:`l(\varepsilon) = 0`. It follows from the basic laws of arithmetic,

.. math::

    l(s\varepsilon) = l(s)  = l(s) + 0 

.. math::

    = l(s) + l(\varepsilon) = l(s) + l(t)

Therefore, the base case, :math:`l(st) = l(s) + l(t)`, holds.

:underline:`Induction`: Let :math:`s, t \in S` and `u \in \Sigma_{e}`. Assume :math:`l(st) = l(s) + l(t)`. Let :math:`v = tu` and consider,

.. math::

    l(sv) = l(s(tu)) = l((st)u)

If :math:`u = \varepsilon`, then applying the argument of the base case,

.. math::

    l(sv) = l((st)u) = l(st) + l(\varepsilon) 

.. math::

    = l(st) = l(s) + l(t)

Where the last equality follows from the inductive hypothesis. Note :math:`t = t\varepsilon = tu = v` by the :ref:`basis clause of concatenation <palindromics-definition-1-2-1>`. From this, it follows the inductive step is established for :math:`u = \varepsilon`,

.. math::

    l(sv) = l(s) + l(v)

If :math:`u \neq \varepsilon`, then it follows from the :ref:`induction clause of String Length <palindromics-definition-1-2-2>`,

.. math::

    l((st)u) = l(st) + 1 = l(s) + l(t) + 1 \quad \text{ (1) }

Where the last equality follows from the inductive hypothesis. Consider the quantity :math:`l(tu)`. By the :ref:`induction clause of String Length <palindromics-definition-1-2-2>`,

.. math::

    l(tu) = l(t) + 1

Adding :math:`l(s)` to both sides,

.. math::

    l(s) + l(tu) = l(s) + l(t) + 1 \quad \text{ (2) }

Comparing the RHS of (1) and (2), it follows the LHS are equal,

.. math::

    l(stu) = l(s) + l(tu)

Summarizing, if :math:`l(st) = l(s) + l(t)` and :math:`u \in \Sigma_{e}`, then :math:`l(stu) = l(s) + l(tu)`. Therefore, the inductive step is established. 

Since the basis case and inductive step have both been established, it follows from the principle of finite induction,

.. math::

    \for all s,t \in S: l(st) = l(s) + l(t)

∎

.. _palindromics-string-equality:

---------------
String Equality
---------------

Two Strings are said to be equal if they have the same length and their corresponding *Alphabetic Characters* (:math:`\iota \in Sigma`) are equal.

.. _palindromics-definitions-1-2-4:

.. topic:: Definition 1.2.4: String Equality

    Let :math:`s, t \in S`. Let :math:`n \in \mathbb{N}`. :math:`s` and :math:`t` are said to be equal when the following conditions hold,

    - :math:`l(s) = l(t) = n`
    - :math:`\forall i \in N_n: s[i] = t[i]`

**Example** Let :math:`s_1 = \mathfrak{ab}` and :math:`s_2 = \mathfrak{a}\varepsilon\mathfrak{b}`. By :ref:`the definition of String Length <palindromics-definition-1-2-2>`,

.. math::

    l(s_1) = l(s_2) = 2 = n

Now, :math:`N_n = { 1, 2 }`. By the :ref:`definition of Character Indices <palindromics-1-2-3>`,

.. math::

    s_1[1] = s_2[1] = \mathfrak{a}

.. math::

    s_1[2] = s_2[2] = \mathfrak{b}

Therefore, :math:`\forall i \in N_n: s_1[i] = s_2[1]`. It follows from these facts and application of :ref:`the definition of String Equality <palindromics-definition-1-2-4>`,

.. math::

    s_1 = s_2

∎

.. _palindromics-containment:

-----------
Containment
-----------

The notion of *containment* is the formal explication of the colloquial relation of "*being a substring of*". 

.. _palindromics-definition-1-2-5:

.. topic:: Definition 1.2.5: Containment

    Let :math:`u,v \in S`. The relation of *containment*, denoted :math:`u \subset_s v`, is said to obtain between :math:`u` and :math:`v` when the following open formula in :math:`u,v` is satisfied,

    .. math::

        u \subset_s v \equiv \exists w_1, w_2 \in S: v = {w_1}u{w_2}


**Example** Let :math:`s_1 = \mathfrak{abcdef}`. Then the truth of the following propositions can be verified using the given values of :math:`w_1` and :math:`w_2` in :math:`the definition of containment <palindromics-definition-1-2-5>`.

- :math:`\mathfrak{ab} \subset_s s_1`, where :math:`w_1 = \varepsilon` and :math:`w_2 = \mathfrak{cdef}`.
- :math:`\mathfrak{cde} \subset_s s_1`, where :math:`w_1 = \mathfrak{ab}` and :math:`w_2 = \mathfrak{f}`.
- :math:`\not (\mathfrak{g} \subset_s s_1)`, for any :math:`w_1, w_2`

∎

.. topic:: Theorem 1.2.2

    The Empty Character is contained in every String.

    .. math::

        \forall s \in S: \varepsilon \subset_s s

**Proof** Let :math:`s \in S`. By the :ref:`definition of concatenation <palindromics-definition-1-2-1>`, 

.. math::

    \varepsilon = \varepsilon\varepsilon

Therefore,

.. math::

    s = {\varepsilon}s = {\varepsilon\varepsilon}s

Let :math:`w_1 = \varepsilon` and :math:`w_2 = s`. Then, :math:`s = {w_1}\varepsilon{w_2}`. By the :math:`definition of containment <palindromics-definition-1-2-5>`, 

.. math::

    \varepsilon \subset_s s

∎

.. _palindromics-string-inversion:

----------------
String Inversion
----------------

.. _palindromics-definition-1-2-6:

.. topic:: Definition 1.2.6: String Inversion

    Let :math:`s, t \in S`. Let :math:`n \in \mathbb{N}`:math:`t` is called the *inverse* of :math:`s`, denoted `s^{-1}` if the following conditions hold,

    - :math:`l(s) = l(t) = n`
    - :math:`\forall i \in N: t[i] = s[n - i + 1]`

**Example** Let :math:`s_1 = \mathfrak{abc}`. Let :math:`s_2 = {s_1}^{-1}`. The inverse can be constructed through its Character Indices by applying :ref:`the definition of String Inversion <palindromics-definition-1-2-6>`,

.. math::

    s_2[1] = s_1[3 - 1 + 1] = s_1[3] = \mathfrak{c}

.. math::

    s_2[2] = s_1[3 - 2 + 1] = s_1[2] = \mathfrak{b}

.. math::

    s_2[3] = s_1[3 - 3 + 1] = s_1[1] = \mathfrak{c}

∎

.. _palindromics-theorem-1-2-3:

.. topic:: Theorem 1.2.3

    The inverse of an inverse is the original String. 

    .. math::

        \forall s \in S: (s^{-1})^{-1} = s

**Proof** Let :math:`s \in S`. Let :math:`t = s^{-1}`. Let :math:`n = l(s)`. By the :ref:`definition of String Inversion <palindromics-definition-1-2-6>`,

.. math:: 

    l(t) = l(s) = n \quad \text{ (1) }

.. math::

    \forall i \in N_n: t[i] = s[n - i + 1] \quad \text{ (2) }

Let :math:`u = t^{-1}`. Applying :ref:`definition of String Inversion <palindromics-definition-1-2-6>` again,

.. math::

    l(u) = l(t) = n \quad \text{ (3) }

.. math::

    \forall j \in N_n: u[j] = t[n - j + 1] \quad \text{ (4) }

Plugging :math:`i = n - j + 1` into (2) and substituting into (4),

.. math::

    \forall j \in N_n: u[j] = s[n - (n - j + 1) + 1] = s[j] \quad \text{ (5) }

Moreover, from (1) and (3), it follows, 

.. math::

    l(s) = l(u) \quad \text{ (6) }

By the :ref:`definition of String Equality <palindromics-definition-1-2-4>`, (5) and (6) together imply,

.. math::

    u = t^{-1} = (s^{-1})^{-1} = s

Therefore,

.. math:: 

    \forall s: (s^{-1})^{-1} = s

∎

.. topic:: Theorem 1.2.4

    The inverse of a concatenation of two String is the concatenation of their inverses in the reversed order.

    .. math::

        \forall s,t \in S: (st)^{-1} = (t^{-1})(s^{-1})

**Proof** Let :math:`s,t \in S`. Let :math:`u = st`. Let :math:`m = l(s)` and :math:`n = l(t)`. Let :math:`u = st`. By :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>`,

.. math::

    l(u) = l(st) = l(s) + l(t) = m + n

Let :math:`v = u^{-1} = (st)^{-1}`. Let :math:`w = (t)^{-1}(s)^{-1}`.  By repeated application of :ref:`definition of String Inversion <palindromics-definition-1-2-6>`,

.. math::

    l(v) = l(st) = m + n \quad \text{ (1) \}

.. math::

    l((t)^{-1}) = l(t) = n 

.. math::

    l((s)^{-1}) = l(s) = m 

Using these results and applying :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>` to :math:`w`,

.. math::

    l(w) = l((s)^{-1}) + l((t)^{-1}) = m + n \quad \text{ (2) }

From (1) and (2), it follows, 

.. math::

    l(v) = l(w) \quad \text{ (3) }

Let :math:`i \in N_{m+n}`.

.. CASE 1

:underline:`Case 1`: :math:`i \leq i \leq n`

By :ref:`definition of String Inversion <palindromics-definition-1-2-6>`,

    v[i] = u[m + n - i + 1]

By assumption :math:`i \leq n` or :math:`n - i \geq 0`, therefore,

.. math::

    m + n - i \geq m

Increasing the LHS of this inequality does not affect the truth of its assertion,

.. math::

    m + n - i + 1 \geq m

From this, :math:`u = st` and :math:`l(s) = m`, it follows that :math:`u[m + n - i + 1]` is an index in :math:`t`, 

.. math::

    v[i] = t[n - i + 1] \quad \text{ (4) }

Consider :math:`w[i]`. Since :math:`l((t)^{-1}) = n` and :math:`i \leq n`, it follows that :math:`w[i] = (t^{-1})[i]`. By :ref:`definition of String Inversion <palindromics-definition-1-2-6>`,

.. math::

    w[i] = t^{-1}[i] = t[n - i + 1] \quad \text{ (5) }

Combining (4) and (5),

.. math::

    v[i] = w[i] \quad \text{ (6) }

Applying the :ref:`definition of String Equality <palindromics-definition-1-2-3>`, (3) and (6) imply,

.. math::

    v = w

.. CASE 2

:underline:`Case 2`: :math:`n + 1 \leq i \leq m + n`

By :ref:`definition of String Inversion <palindromics-definition-1-2-6>`,

    v[i] = u[m + n - i + 1]

By assumption :math:`i \geq n + 1` or :math:`n - i + 1 \leq 0`, therefore,

.. math::

    m + n - i + 1 \leq m 

From this, :math:`u = st` and :math:`l(s) = m`, it follows that :math:`u[m + n - i + 1]` is an index in :math:`s`,

.. math::

    v[i] = s[m + n - i + 1] \quad \text{ (7) } 

Consider :math:`w[i]`. Since :math:`l((t)^{-1}) = n` and :math:`i \geq n`, it follows that :math:`w[i] = (s^{-1})[i - n]`. By :ref:`definition of String Inversion <palindromics-definition-1-2-6>`,

.. math::

    w[i] = s^{-1}[i-n] = s[m - (i - n) + 1]

.. math::

    w[i] = s[m + n - i + 1] \quad \text{ (8) }

Combining (7) and (8),

.. math::

    v[i] = w[i] \quad \text{ (9) \}

Applying the :ref:`definition of String Equality <palindromics-definition-1-2-3>`, (3) and (6) imply,

.. math::

    v = w

In both cases, the theorem is proved. Summarizing and generalizing,

.. math::

    \forall s,t \in S: (st)^{-1} = (t^{-1})(s^{-1})

∎

.. ...................................................
.. .................. SECTION I.III ..................
.. ...................................................

.. _palindromics-section-i-iii:

Section I.III: Words
--------------------

.. important::

    To reiterate the introduction to this section, the current formal system does not seek to describe a generative grammar. Its theorems cannot be used as schema for generating grammatical sentences. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations.

A Word is a type of String constructed through concatenation that has been assigned by semantic content. A Language is the aggregate of all Words.

.. math::

    \forall \alpha \in L: \alpha \in S

Or equivalently,

.. math::

    L \subset S

It is assumed Words cannot have a String Length of 0.

.. _palindromics-axiom-w-1:

.. topic:: Axiom W.1: Measureable Axiom

    .. math::

        \forall \alpha \in L: l(\alpha) \neq 0

It is further assumed that no Character in a Word can be a Delimiter.

.. _palindromics-axiom-w-2:

.. topic:: Axiom W.2: Discovery Axiom

    .. math::

       \forall \alpha in L: \forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma

.. _palindromics-word-classes:

------------
Word Classes 
------------

.. _palindromics-definition-1-3-1:

.. topic:: Definition 1.3.1: Reflective Words

    Let :math:`\alpha \in L`. :math:`\alpha` belongs to the set of Reflective Words, denoted :math:`R`, if it satisfies the open formula,

    .. math::

        \alpha \in R \equiv \alpha = {\alpha}^{-1}

    A Word will be referred to as *reflective* if it belongs to the class of Reflective Words.

**Example** The following table lists some reflective English words.

.. list-table:: 
    :widths: 50
    :header-rows: 1
    
    * - Word
    * - mom
    * - dad
    * - noon
    * - racecar
    * - madam
    * - level
    * - civic

∎

.. _palindromics-definition-1-3-2:

.. topic:: Definition 1.3.2: Invertible Words

    Let :math:`\alpha \in L`. :math:`\alpha` belongs to the set of Invertible Words, denoted :math:`I`, if it satisfies the open formula,

    .. math::

        \alpha \in I \equiv {\alpha}^{-1} \in L

    A Word will be referred to as *invertible* if it belongs to the class of Invertible Words.

.. important::

    A Word is invertible if and only if its inverse belongs to the Language. 

**Example** The following table lists some English words and their inverses (where applicable).

.. list-table::
    :widths: 20 20
    :header-rows: 1

    * - Word
      - Inverse
    * - time
      - emit
    * - saw
      - was
    * - raw
      - war
    * - dog
      - god
    * - pool
      - loop
    * - cat
      - x
    * - you
      - x
    * - help
      - x
    * - door
      - x
    * - book
      - x

∎

.. note::

    Invertible Words are often called *semiordnilaps* in other fields of study.

.. topic:: Theorem 1.3.1

    A Word is invertible if and only if its inverse is invertible.

    .. math::

        \forall \alpha \in L: \alpha \in I \equiv {\alpha}^{-1} \in I

**Proof** Let :math:`\alpha \in L`.

(:math:`\rightarrow`) Assume :math:`\alpha \in I`. By :ref:`the definition of invertible Words <palindromics-definition-1-3-2>`,

.. math::

    {\alpha}^{-1} \in L

By :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`,

.. math::

    ({\alpha}^{-1})^{-1} = \alpha

Therefore, by assumption,

.. math::

    ({\alpha}^{-1})^{-1} \in L

By :ref:`the definition of invertible Words <palindromics-definition-1-3-2>`,

.. math::

    {\alpha}^{-1} \in I

(:math:`\leftarrow`) Assume :math:`{\alpha}^{-1} \in L` such that :math:`{\alpha}^{-1} \in I`. By :ref:`the definition of invertible Words <palindromics-definition-1-3-2>`,

.. math::

    ({\alpha}^{-1})^{-1} \in L

By :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`,

.. math::

    \alpha \in L 

Since :math:`{\alpha}^{-1} \in L` by assumption, it follows immediately from :ref:`the definition of invertible Words <palindromics-definition-1-3-2>`,

.. math::

    \alpha \in I

Summarizing and generalizing,

.. math::

    \forall \alpha \in L: \alpha \in I \equiv {\alpha}^{-1} \in I

∎

.. _palidromics-theorem-1-3-2:

.. topic:: Theorem 1.3.2

    Reflective Words are a subset of Invertible Words.

    .. math::

        R \subset I

**Proof** Let :math:`\alpha in R` and :math:`l(\alpha) = n`. By :ref:`the definition of Reflective Words <palindromics-definition-1-3-1>`,

.. math::

    \alpha = \alpha^{-1}

Since :math:`\alpha \in L` by assumption, it follows :math:`\alpha in I`. In other words,

.. math::

    \alpha \in R \implies \alpha \in I

But this is exactly the definition of the subset relation in set theory, therefore,

.. math::

    R \subset I

∎

.. _palindromics-limitations:

-----------
Limitations
-----------

.. _palindromics-definition-1-3-3:

.. topic:: Definition 1.3.3: Phrases

    Let :math:`n \in \mathbb{N}`. A Phrase of Word Length :math:`n`, denoted :math:`P_n`, is defined as an ordered sequence of :math:`n` Words, not necessarily distinct,

    .. math::

        P_n = { (i, \alpha_i) \mid i \in N_n \land \alpha \in L \} 

    .. math::

        P_n = (\alpha_1, \alpha_2, ..., \alpha_n)

    where each :math:`\alpha_i \in L`. If :math:`1 \leq i \leq n`, :math:`P_n(i)` denotes the Word :math:`\alpha_a` at index :math:`i` of the Phrase, so the Phrase may be written,

    .. math::

        P_n = (P_n(1), P_n(2), ... P_n(n))

    When :math:`n = 0`, a Phrase is defined to be :math:`\varnothing`,

    .. math::

        P_0 = \varnothing

.. _palindromics-definition-1-3-4:

.. topic:: Definition 1.3.4: Lexicons

    Let :math:`n \in \mathbb{N}`. A Language's :math:`n^{\text{th}}` Lexicon, denoted :math:`L_n`, is defined as the set of all Phrases of length :math:`n`,

    .. math::

        L_n = \{ p \mid \forall p: p = P_n \}

.. _palindromics-definition-1-3-5:

.. topic:: Defintion 1.3.5: Limitation 
    
    Let :math: `p \in L_n`. The Limitation of :math:`p`, denoted :math:`\Pi_{i=1}^{n} p(i)` is defined inductively using the following schema,

    - Empty: :math:`\Pi_{i=1}^{0} p(i) = \varepsilon`
    - Basis: :math:`\Pi_{i=1}^{1} p(i) = \alpha_1`
    - Induction: :math:`\Pi_{i=1}^{n} p(i) = (\Pi_{i=1}^{n-1} p(i))\alpha_n`

.. _palindromics-definition-1-3-6:

.. topic:: Definition 1.3.6: Delimitation

    Let :math: `p \in L_n`. The Delimitation of :math:`p`, denoted :math:`\bar{\Pi}_{i=1}^{n} p(i)` is defined inductively using the following schema,

    - Empty: :math:`\bar{\Pi}_{i=1}^{0} p(i) = \varepsilon`
    - Basis: :math:`\bar{\Pi}_{i=1}^{1} p(i) = \alpha_1`
    - Induction: :math:`\bar{\Pi}_{i=1}^{n} p(i) = (\Pi_{i=1}^{n-1} p(i))\sigma\alpha_n`

.. note::

    The key difference between a :ref:`Limitation <palindromics-definition-1-3-5>` and a :ref:`Delimitation <palindromics-definition-1-3-6>` is the presence of the Delimiter in the Induction clause. In other words, a Limitation is shorthand for iterated concatenation of Words, whereas Delimitation inserts Delimiters inbetween each Word is the Lexicon.

**Example** Let

.. math::

    P_3 = (\text{"mother"}, \text{"may"}, \text{"I"})

Apply the Basis clause :ref:`of the definition of Delimitations <palindromics-definition-1-3-5>` ,

.. math::

    n = 1: \bar{\Pi}_{i=1}^{1} \alpha_i = \text{"mother"} 

The Delimitation can then be built up recursively using the Induction clause,

.. math::

    n = 2: \bar{\Pi}_{i=1}^{2} \alpha_i = (\bar{\Pi}_{i=1}^{1} \alpha_i)(\sigma)(\text{"may"})= (\text{"mother"})(\sigma\text{"may"}) = \text{"mother"}\sigma\text{"may"}
    
.. math::

    n = 3: \bar{\Pi}_{i=1}^{3} \alpha_i = (\bar{\Pi}_{i=1}^{2} \alpha_i)(\sigma)(\text{"I"}) = (\text{"mother"}\sigma\text{"may"})(\sigma\text{"I"}) = \text{"mother"}\sigma\text{"may"}\sigma\text{"I"}

So the Delimitation of the Phrase is shown to be,

.. math::

    \bar{\Pi}_{i=1}^{3} \alpha_i = \text{"mother may I"} 

Similarly, the Limitation can be constructed using the Basis and Induction clause of :ref:`the definition of Limitations <definition-1-3-5>`,

.. math::

    n = 2: \Pi_{i=1}^{2} \alpha_i = (\Pi_{i=1}^{1} \alpha_i)(\text{"may"})= (\text{"mother"})(\text{"may"}) = \text{"mothermay"}
   
.. math::

    n = 3: \Pi_{i=1}^{3} \alpha_i = (\Pi_{i=1}^{2} \alpha_i)(\text{"I"}) = (\text{"mothermay"})(\text{"I"}) = \text{"mothermayI"} 

.. important::

    The result of a Delimitation or a Limitation is a String. Since Delimitation and Limitation are shorthand for different sequences of concatenation, their closure over :math:`S` is guaranteed by the closure of concatenation over :math:`S`

∎

.. ...................................................
.. .................. SECTION I.IV ...................
.. ...................................................

.. _palindromics-section-i-iv:

Section I.IV: Sentences
-----------------------

A Sentence is a Delimitation of Words over a Phrase in the Language's Lexicon for any value of :math:`n \geq 1`. 

.. warning::

    This statement should not be interpretted as a schema for generating grammatical sentences. In general, Delimitations are *not* grammatical. However, all grammatical sentences *are* Delimitations.
    
    In other words, this statement should be interpretted as a necessary syntactic pre-condition a Sentence must satisfy before it may be assigned semantic content.

A Corpus is the aggregate of all Sentences.

.. math::

    \forall \zeta in C: \exists n: \zeta = \bar{\Pi}_i^{n} p(i)

.. note::

    The value of :math:`n` in the preceding equation will be further specified after several definitions and theorems. It will be shown to be directly and necessarily related to the Word structure of :math:`\zeta`.

The full semantic hierarchy has now been formalized. The hierarchy is summarized in the following diagram,

.. graphviz:: ../../_static/dot/palindromes/hierarchy.dot
    :caption: A diagram of the semantic hierarchy
    :alt: Semantic Hierarchy Diagram

The following lists group the objects of the formal system by type,

1. Strings: :math:`\iota, \alpha, \zeta`
2. Sets: :math:`\Sigma, L, C`
3. Character Membership: :math:`\iota \in \Sigma`
4. Word Membership: :math:`\alpha \in L`
5. Sentence Membership: :math:`\zeta \in C`

These observations can be translated into English as follows,

1. All Characters, Words and Sentences are Strings.
2. All Alphabets, Languages and Corpuses are sets of Strings.
3. All non-Empty Characters belong to an Alphabet.
4. All Words belong to a Language.
5. All Sentences belong to a Corpus.

.. _palindromics-word-length:

-----------
Word Length
-----------

.. _palindromics-definition-1-4-1:

.. topic:: Definition 1.4.1: Word Length

    Let :math:`s \in S` and :math:`n \in N` such that :math:`\zeta = \bar{\Pi}_{i=1}^n p(i)`. The Word Length of :math:`zeta`, denoted :math:`\Lambda(\zeta)`, is defined inductively through the following schema,

    - Basis: If :math:`\neq(\sigma \subset_s s)`,
        - If :math:`s = \varepsilon` or :math:`s \notin L`, :math:`\Lambda(s) = 0`
        - If :math:`s \in L`, :math:`\Lambda(s) = 1`
    - Induction: 
        - If :math:`s = {\sigma}{v}`, or if :math:`s = {u}{\sigma}{v}` and :math:`u \notin L`, then :math:`\Lambda(s) = \Lambda(v)`
        - If :math:`s = {u}{\sigma}{v}` and :math:`u \in L`, then :math:`\Lambda(s) = \Lambda(v) + 1`

.. important::

    The Induction clause of Word Length relies on the :ref:`Discovery Axiom <palindromics-axiom-w-2>` and the :ref:`Measureable Axiom <palindromics-axiom-w-1>` to ensure for any Strings :math:`u \in L`, :math:`\neg(\sigma \subset_s u)` and :math:`u \neq \varepsilon`.

**Example** Let :math:`ᚠ = \text{"truth is beauty"}`.

Let :math:`u_1 = \text{"truth"}` and :math:`v_1 = \text{"is beauty"}`. Then :math:`u_1 \in L_{\text{english}}` and :math:`ᚠ = (u_1)(\varsigma)(v_1)`. Apply the Induction clause of :ref:`the definition of Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(ᚠ) = \Lambda(v_1) + 1

Let :math:`u_2 = \text{"is"}` and :math:`\v_2 = \text{"beauty"}`. 

.. important::

    A selection of :math:`u_2 = \text{"i"}` or :math:`u_2 = \text{"is be"}` would not satisfy the condition :math:`s = {u}{\sigma}{v}` in the Induction clause, which requires :math:`u` and :math:`v` to be delimited with :math:`\varsigma`.

Then :math:`u_2 \in L_{\text{english}}` and :math:`v_1 = (u_2)(\varsigma)(v_2)`. Apply the Induction clause of :ref:`the definition of Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(v_1) = \Lambda(v_2) + 1

Finally, note :math:`v_2 \in L_{\text{english}}` and apply the Basis clause to :math:`v_2`,

.. math::

    \Lambda(v_2) = 1

Putting the recursion together,

.. math::

    \Lambda(ᚠ) = (1 + 1) + 1 = 3

∎

**Example** Let :math:`ᚠ = \text{"palindromes vorpal semiordinlap"}`

Let :math:`u_1 = \text{"palindromes"}` and :math:`v_1 = \text{"vorpal semiordinlap"}`. Then :math:`u_1 \in L_{\text{english}}` and :math:`ᚠ = (u_1)(\varsigma)(v_1)`. Apply the Induction clause of :ref:`the definition of Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(ᚠ) = \Lambda(v_1) + 1

Let :math:`u_2 = \text{"vorpal"}` and :math:`\v_2 = \text{"semiordinlap"}`. Then :math:`u_2 \notin L_{\text{english}}` and :math:`v_1 = (u_2)(\varsigma)(v_2)`. Apply the Induction clause of :ref:`the definition of Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(v_1) = \Lambda(v_2)

Finally, note :math:`v_2 \in L_{\text{english}}` and apply the Basis clause to :math:`v_2`,

.. math::

    \Lambda(v_2) = 1

Putting the recursion together,

.. math::

    \Lambda(ᚠ) = (1 + 1) = 2

∎

.. important::

    As these examples demonstrate, the Word Length of a String is always *relative* to a given a Language. A subscript will be used to denote whether a Word Length is relative to a particular language, 
    
    .. math::
        
        \Lambda_{\text{english}}(\text{"closing sale"}) = 2

    Whereas,

    .. math::

        \Lambda_{\text{italian}}(\text{"closing sale"}) = 1

.. _palindromics-definition-1-4-2:

.. topic:: Definition 1.4.2: Word Index Notation

    The Word at index :math:`i` in a String :math:`s \in S`, denoted :math:`s[[1]]`, is defined inductively using the following schema,

    - Basis: 
        - :math:`s[[i]] = s` if and only if :math:`i = 1` and :math:`s \in L`
        - Otherwise, :math:`s[[i]]` is undefined.
    - Induction:
        - If :math:`s = {\sigma}{v}`, or if :math:`s = {u}{\sigma}{v}` and :math:`u \notin L`, then :math:`s[[i]] = v[[i]]`
        - If :math:`s = {u}{\sigma}{v}`, :math:`u \in L` and :math:`i = 1`, then :math:`s[[i]] = u`
        - If :math:`s = {u}{\sigma}{v}`, :math:`u \in L` and :math:`i > 1`, then :math:`s[[i]] = v[[i-1]]`

**Example** Let :math:`ᚠ = \text{"observe how system into system runs"}`. Consider :math:`ᚠ[[3]]`.

Let :math:`u_1 = \text{"observe"}` and :math:`v_1 = \text{"how system into system runs"}`. Then :math:`ᚠ = {u_1}\varsigma{v_1}`, :math:`u_1 \in L` and :math:`3 > 1`. Therefore, by the Induction clause of :ref:`the definition of Word Indices <palindromics-definition-1-4-2>`,

.. math::

    ᚠ[[3]] = v_1[[3-1]] = v_1[[2]]

At the next step, let :math:`u_2 = \text{"how"}` and :math:`v_2 = \text{"system into system runs"}`. Then :math:`v_1 = {u_2}\varsigma{v_2}`, :math:`u_2 \in L` and :math:`2 > 1`,

.. math::

    v_1[[2]] = v_2[[1]]

At the next step, let :math:`u_3 = \text{"system"}` and :math:`v_3 = \text{"into system runs"}`. Then :math:`v_2 = {u_3}\varsigma{v_3}`, :math:`u_3 \in L` but :math:`1 = 1`, therefore,

.. math::

    ᚠ[[3]] = v_1[[2]] = v_2[[1]] = u_3 = \text{"system"}

∎

**Example** Let :math:`ᚠ = \text{"the gobberwarts with my blurglecruncheon"}`. Consider :math:`ᚠ[2]`.

Let :math:`u_1 = \text{"the"}` and :math:`v_1 = \text{"gobberwarts with my blurglecruncheon"}`. Then :math:`ᚠ = {u_1}\varsigma{v_1}`, :math:`u_1 \in L` and :math:`2 > 1`. Therefore, by the Induction clause of :ref:`the definition of Word Indices <palindromics-definition-1-4-2>`,

.. math::

    ᚠ[[2]] = v_1[[2-1]] = v_1[[1]]

At the next step, let :math:`u_2 = \text{"gobberwarts"}` and :math:`v_2 = \text{"with my blurglecruncheon"}`. Then :math:`v_1 = {u_2}\varsigma{v_2}` but :math:`u_2 \notin L` and :math:`1 = 1`, so by the first condition of the Induction clause,

.. math::

    v_1[[1]] = v_2[[1]]

At the next step, let :math:`u_3 = \text{"with"}` and :math:`v_3 = \text{"my blurglecruncheon"}`. Then :math:`v_2 = {u_3}\varsigma{v_3}`, :math:`u_3 \in L` and :math:`1 = 1`. So, the second condition of the Induction clause,

.. math::

    ᚠ[[2]] = v_1[[1]] = v_2[[1]] = u_3 = \text{"with"}

∎

The next theorems that will not be required for the final postulates are given next, but they are given to indicate the type of results that may be established regarding the concept of Word Length. The results will be stated without proof. For the curious reader, the details can be found in :ref:`Appendix I.II: Omitted Proofs <palindromics-appendix-i-ii>`.

.. _palindromics-theorem-1-4-1:

.. topic:: Theorem 1.4.1

    The sum of the String Lengths of the Words in a Sentence is atleast as great as the Word Length of the Sentence.

    .. math::

        \forall \zeta in C: \sum_{j=1}^{\Lambda(\zeta)} l(\zeta[[j]]) \geq \Lambda(\zeta)

.. _palindromics-theorem-1-4-2:

.. topic:: Theorem 1.4.2

    The Word Length of the concatenation of two Sentences is no more than the sum of their individual Word Lengths.

    .. math::

        \forall \zeta, \xi \in C: \Lamdba(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)

.. note::

    The edge case of compound Words (e.g. "*daylight*") makes the proof :ref:`Theorem 1.4.2 <palindromics-theorem-1-4-2>` particularly interesting, demonstrating Word Length is fundamentally different than String Length with respect to the operation of concatenation. In :ref:`Theorem 1.2.1 <palindromics-theorem-1-1-1>`, it was shown String Length sums over concatenation. :ref:`Theorem 1.4.1 <theorem-1-4-1>` demonstrates the corresponding property is not necessarily true for Word Length. This is an artifact of the potential destruction of semantic content upon concatenation.

.. _palindromics-sentence-axioms:

---------------
Sentence Axioms
---------------

.. _palindromics-axiom-s-1:

.. topic:: Axiom S.1: Sentence Duality Axiom

    For every Word in the Language, there exists a Sentence in the Corpus that contains it.

    .. math::

        \forall \alpha \in L: \exists \zeta \in C: \alpha \subset_s \zeta 

.. _palindromics-axiom-s-2:

.. topic:: Axiom S.2: Word Duality Axiom

    For every Sentence in the Corpus, there exists a Word in the Language which is contained in it.

    .. math::

        \forall \zeta \in C: \exists \alpha \in L: \alpha \subset_s \zeta

.. note::

    The Duality Axioms are reminiscent of the relation of surjectivity in real analysis. However, containment is not a strict equality relation so this resemblance should not be taken too far. 

.. _palindromics-axiom-s-3:

.. topic:: Axiom S.3: Comprehension Axiom

    Every Word in a Sentence of the Corpus belongs to the Language.

    .. math::

        \forall \zeta \in C: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \in L

The following theorem is proved in :ref:`Appendix I.II: Omitted Proofs <palindromics-appendix-i-ii>`, as it is not required for the results in :ref:`Section IV <palindromics-section-iv>`. This theorem demonstrates the relationship between a Delimitation and Word Length that was pointed out in the introduction of this subsection.

.. _palindromics-theorem-1-4-3:

.. topic:: Theorem 1.4.3

    .. math::

        \forall \zeta \in C: \zeta = \bar{\Pi}_{i=1}^{\Lambda(\zeta)} \zeta[[i]]

.. _palindromics-sentence-classes:

----------------
Sentence Classes
----------------

.. _palindromics-definition-1-4-3:

.. topic:: Definition 1.4.3: Admissible Sentences

    TODO

**Example** Let :math:`ᚠ = \text{"strap on a ton"}`.

TODO

.. _palindromics-theorem-1-4-4:

.. topic:: Theorem 1.4.4

    All Admissible Sentences of a given Word Length belongs to the Corpus,

    .. math::

        A_n \subset C

**Proof** TODO

.. _palindromics-definition-1-4-4:

.. topic:: Definition 1.4.4

    Let :math:`\zeta \in C`. Then the set of Invertible Sentences, denoted :math:`K`, is defined as the set which satisfy the following open formula,

    .. math::

        \zeta \in \K \equiv {\zeta}^{-1} \in C

    A Sentence that belongs to :math:`K` will be referred to as "*invertible*".

.. _palindromics-theorem-1-4-5:

.. topic:: Theorem 1.4.5

    A Sentence is invertible if and only if its inverse is invertible.

    .. math::

        \forall \zeta in C: \zeta \in K \equiv {\zeta}^{-1} \in K

**Proof** TODO


.. _palindromics-theorem-1-4-6:

.. topic:: Theorem 1.4.7

    If a Sentence in the Corpus is invertible, then all of the Words are also invertible.

    .. math::

        \forall \zeta in K: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \in I

**Proof** TODO

.. _palindromics-theorem-1-4-7:

.. topic:: Theorem 1.4.7

    If a Sentence is invertible, then the :math:`i^{\text{th}}` Word in its inverse Sentence is equal to the inverse of the :math:`i^{\text{th}}`-to-last Word in the Sentence.

    .. math::

        \forall \zeta \in K: \forall i \in N_{\Lambda(\zeta)}: {\zeta}^{-1}[[i]] = (\zeta[[i]])^{-1}

**Proof** TODO