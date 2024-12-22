======================
Palindromic Structures
======================

The paper contains a formal method for analyzing palindromic structures. It is a work in progress. What follows should by no means be interpretted as a complete or consistent formal theory; it should be treated more like a rough draft. Many of the notions need further clarification and elaboration.  
    
The goal of this paper is to introduce formal constraints the palindromes in *any* language must satisfy independently of the semantic interpretation of their constituent words. These formal constraints will in turn lead to the identification of the main structural elements of palindromes. After a language is assumed and a class of words identified, these structural elements can be used as a basis for further semantical and statistical analysis of the assumed language. 

Section I: Defintions 
=====================

Section I.I: Strings
--------------------

The domain of discourse is composed of *Strings*. A String will be represented as follows, 

    1. String (*s*:sub:`1`, *s*:sub:`2`, *s*:sub:`3`): A lowercase English *s* with a subscript denotes a String. Sometimes the subscript will be dropped and *s* will be used. The letter *t* and *u* also reserved for Strings.

A String is regarded as a linguistic artifact that is defined by its *length*, its *Characters* and their *ordering*. It is assumed if one knows how many Characters are in a String, which Characters are in a String and in what order they occur, then one has all the information necessary to completely determine the String. This notion is made more precise in the following sections with the introduction of several definitions.

A *Word* will be considered a *type* of String. Colloquially, a word can be understood as a String with semantic content. The goal of the analysis is to describe the necessary syntactic conditions for a String to be considered a formal Word, without taking into account the semantic content that is assigned to through everyday use. In other words, the analysis assumes Words have already been selected from the set of all possible Strings and assigned interpretations. 

Characters
^^^^^^^^^^

A *Character* is the basic unit of a String. Characters will be represented as follows,

    1. Characters (*𝔞*, *𝔟*,  *𝔠*, etc. ): Lowercase Fraktur letters represent Characters. Subscripts will occassionally be used in conjunction with Fraktur letters to denote Characters, (*𝔞*:sub:`1`, *𝔞*:sub:`2`, ... ). 
    2. Empty (*ε*): The lowercase Greek letter epsilon, *ε*, represents the Empty Character.
    3. Delimiter (*σ*): The lowercase Greek letter sigma, *σ*, represents the Delimiter Character. 

In the case of English, Characters would correspond to letters such as "a", "b", "c", etc., the Empty Character would correspond to the null letter, "", and the Delimiter Character would correpond to the blank letter, " ".

The aggregate of all Characters is called an *Alphabet* and is denoted by an uppercase Sigma, **Σ**,

    Σ = { *ε*, *σ*, *𝔞*, *𝔟*,  *𝔠*, ... }

The number of elements in an Alphabet is denoted | Σ |. In general, throughout the course of this work, the cardinality of a set **A** will be denoted | A |. 

It will sometimes be necessary to refer to indeterminate Characters, so notation is introduced for Character Variables,

    4. Character Variables (*ⲁ*, *ⲃ*, *ⲅ*, etc. ): Lowercase Coptic letters will represent Character Variables, i.e. indeterminate Characters. Subscripts will occassionally be used with Coptic letters to denote Word Variables, (*ⲁ*:sub:`1`, *ⲁ*:sub:`2`, ... )

Concatenation 
^^^^^^^^^^^^^

Concatenation is considered the sole constitutive operation for the formation of Strings. It is taken as a primitive operation and should be understood as follows,

**Definition 1.1.1: Concatenation**  *𝔞𝔟* is the *concatenation* of *𝔞* and *𝔟*, denoted *concat(𝔞, 𝔟)* 

Colloquially, *concat(𝔞, 𝔟)* is the String that results from placing *𝔟* behind *𝔞*. The operation of concatenation will be expanded to a larger class of entities in the next section when the notion of a *Word* is further clarified, but its application will always be reducible to simple Character concatenation. This current definition of concatenation leads immediately to the dual *Laws of Nullity*, 

    1. *𝔞ε* = *𝔞*
    2. *ε𝔞* = *𝔞*
   
In other words, the operation of concatenating a Character with the Empty Character in either direction will leave the original Character unaltered. 

Notation
^^^^^^^^

It will sometimes be convenient to represent Words and Strings as ordered sets of Characters, rather than serialized concatenations of Characters. The two formulations are equivalent, but the set representation has advantages when it comes to quantification and symbolic logic. When a String or Word representation is intended to be interpretted as a set, it will be written in bold uppercase letters. For example, the String represented as the concatenated series *s_1* = *𝔞𝔟𝔠* would be represented in this formulation as a set of ordered pairs **S_1**, where the first coordinate encodes the position of the Character in the String,

    **S_1** = { (1, *𝔞*), (2, *𝔟*), (3, *𝔠*) }

Note, since sets do not preserve order, this would be equivalent to,

    { (3, *𝔠*), (2, *𝔟*), (1, *𝔞*) }

To simplify notation, it is sometimes beneficial to represent this set as a sequence that *does* preserve order as,

    **S_1** = (*𝔞*, *𝔟*, *𝔠*) 

Length
^^^^^^

The Empty Character *ε* will be necessary for defining the *pivot point* of a palindrome. While this addition to the Alphabet **Σ** is advantegous from the perspective of palindromic analysis, it presents a problem when defining the length of a String *s*. If *ε* is considered part of the Alphabet, the typical notion of a String's length is undefined, as *ε* can be concatenated an infinite number of times to *s* without altering its content. To explicate the notion of *length*, consider the constraints that must be placed on this concept in the palindromic system,

    - The length of the string "abc" is 3, as it contains three non-empty characters.
    - The length of the string "aεbεc" is still 3, as the empty characters (ε) are not counted.

This example motivates the following definition.

**Definition 1.1.2** The *length* of a String *t*, denoted *l(t)*, is defined as the number of non-Empty Characters in the sequence of concatenated Characters that make up the String. 

Let *ⲁ* be a character in the String *t*. Recall *t* has an equivalent set representation **T**,

    T = { (1, ⲁ:sub:`1``), (2, ⲁ:sub:`2`), ..., (l(t), ⲁ:sub:`l(t)`) }

Let **N**:sub:`t` be the set, 

    N:sub:`t`= { 1, 2, ... , l(t) }

Formally, we define the length of *t* to be cardinality of the set **E**:sub:`t` where **E**:sub:`t` satisfies the formula,

    (j, ⲁ) ∈ E:sub:`t` ↔ (∃i ∈ N:sub:`t`: ( (i, ⲁ) ∈ T) ∧ (ⲁ ≠ ε) ∧ (j = i) )

With this definition, the length of String in the formalization can be defined as,

    l(t) = | E:sub:`t` |

Note the E:sub:`t` is a set of *ordered pairs*, not a set of Characters. This allows for repeated Characters to be counted in a String's length.

**Example** t = "aabbcc"

The set representation of *t* is given by,

    T = { (1, a), (2, a), (3, b), (4, b), (5, c), (6, c) }.

By Definition 1.1.2, 

    E:sub:`t` = { (1, a), (2, a), (3, b), (4, b), (5, c), (6, c) }

Therefore, 

    | E:sub:`t` | = 6

This formulization, while perhaps prosaic, maps to the intuitive notion of a String's length, i.e. the number of non-empty Characters, while still allowing for a calculus of concatenation that involves Empty Characters.

Containment
^^^^^^^^^^^

Similar to the explication of *length*, the notion of a String *containing* another String must be made precise using the definitions introduced so far. It's important to note that in the current system the relation of *containment* is materially different from the standard subset relation between sets. For example, the set of characters in "rat" is a subset of the set of characters in "tart," but "rat" is not contained in "tart" because the order of the characters is different.

Consider the words "rat" and "strata". The word "rat" *is contained* in the word "strata", because the order of the string "rat" is preserved in "strata". An intuitive way of capturing this relationship is to map the indices of the Characters in "rat" to the indices of the Characters in "strata" which correspond to the indices in "rat". A cursory (but incorrect) definition of *containment* can then be attempted,

**Containment (Incorrect Version)** α ⊂:sub:`s` β

Let *α* and *β* be words represented as the sets of ordered pairs, *Α* and *Β*,

    Α = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ..., (l(α), 𝔞:sub:`l(α)`) }

    Β = { (1, 𝔟:sub:`1`), (2, 𝔟:sub:`2`), ..., (l(β), 𝔟:sub:`l(β)`) }

*α* is said to be *contained in β*, denoted by,

    α ⊂:sub:`s` β
    
If and only if there exists a strictly increasing function *f*: **N**:sub:`α` *→* **N**:sub:`β` such that:

    ∀ i ∈ N:`α`: a:sub:`i` = b:sub:`f(i)`

This definition essentially states that *α* is contained in *β* if there's a way to map the Characters of *α* onto a subsequence of the Characters in *β* while preserving their order. The function f** ensures that the Characters in *α* appear in the same order within *β*. While this definition is incorrect, the reason why this version of *containment* fails is instructive in developing better understanding of the subtelty involved in attempting its definition. 

First, consider an example where this definition correlates with the intuitive notion of *containment*. Let *α = "rat"* and *β = "strata"*. Then, these words can be represented in set notation as,

    Α = { (1, r), (2, a), (3, t) }
     
    Β = { (1, s), (2, t), (3, r), (4, a), (5, t), (6, a) }.

The function *f* defined as *f(1) = 3*, *f(2) = 4*, and *f(3) = 5* satisfies the condition in the proposed definition, as it maps the characters of "rat" onto the subsequence "rat" within "strata" while preserving their order. In addition, *f* is a strictly increasing function. Therefore, 

    "rat" ⊂:sub:`s` "strata".

Next, consider a counter-example. Let *α* = "bow" and *β* = "borrow". Then their corresponding set representations are given by,

    Α = { (1, b), (2, o), (3, w) }
     
    Β = { (1, b), (2, o), (3, r), (4, r), (5, o), (6, w) }

The function defined through *f(1) = 1*, *f(2) = 5* and  *f(3) = 6* satisfies the conditions of the proposed definition. However, intuitively, "bow" is *not contained* in the word "borrow". The reason the proposed definition has failed is now clear: the function *f* that is mapping "bow" to "borrow" skips over the indices 2, 3 and 4 in "borrow". In other words, in addition to being strictly increasing, the function *f* which maps the smaller word onto the larger word must also be *consecutive*. This insight can be incorporated into the definition of *containment* by first defining the notion of *consecutive*,

**Definition 1.1.3: Consecutive Functions** 

A function *f* is consecutive if it satisfies the formula,

    ∀ i, j ∈ N:sub:`α``:  (i < j) →  f(j) = f(i) + (j - i).  
    
This additional constraint on *f* ensures that the indices of the larger word in the containment relation are mapped in a sequential, unbroken order to the indices of the smaller word. This definition of *Consecutive Functions* can be immediately utilized to refine the notion of *containment*.

**Definition 1.1.4: Containment** α ⊂:sub:`s` β

Let *α* and *β* be words represented as the sets of ordered pairs *Α* and *Β*:

    Α = { (1, a:sub:`1`), (2, a:sub:`2`), ..., (l(α), a:sub:`l(α)`) }

    Β = { (1, b:sub:`1`), (2, b:sub:`2`), ..., (l(β), b:sub:`l(β)`) }

*α* is said to be *contained in β*, denoted by,

    α ⊂:sub:`s` β

If and only if there exists a strictly *increasing and consecutive* function *f*: **N**:sub:`α` *→* **N**:sub:`β` such that:

    ∀ i ∈ N:sub:`α`: a:sub:`i` = b:sub:`f(i)`

The notion of containment will be central to developing the logic of palindromic structures in the subsequent sections.

Cardinality
^^^^^^^^^^^

The set of all Strings is denoted **S**. The cardinality of **S** is denoted | S |.

It is assumed **S** is at least uncountably infinite. A rigorous proof of this fact would carry the current work too far into the realm of real analysis, but as motivation for this assumption, an informal proof is presented below based on Cantor's famous Diagonalization argument. 

**Theorem 1.1.1** | S | ≥ ℵ:sub:`1`

Assume, for the sake of contradiction, that the set of all Strings **S** is countable. This means the Strings can be listed them in some order, 

    s:sub:`1`, s:sub:`2`, s:sub:`3`, etc.

Now, construct a new String *t* as follows:

    1. The first character of t is different from the first character of s1.
    2. The second character of t is different from the second character of s2.
    3. etc.

This string *t* will be different from every string in **S** contradicting the assumption that we could list all possible strings. Therefore, **S** must be uncountable. ∎ 

Section I.II: Words
-------------------

While the notion of Characters maps almost exactly to the intuitive notion of letters in everyday use, the notion of a *Word* requires explication. 

If Characters are mapped to letters in the alphabet of a *Language* **L**, the set of all Strings would have as a subset the Language that is constructed through the alphabet.  The goal of this section is to introduce a series of constraints onto the set of all Strings that will filter out its elements that cannot belong to **L** based solely on their internal structure. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations. In other words, this analysis will proceed without assuming anything about the interpretation of the Words in the Language beyond the fact that they *are* Words of the Language.

To formalize these notion, the following symbolic representations are introduced, 

    1. Words (*a*, *b*, *c*, etc.): Lowercase English letters represent Words. Subscripts will occassionally be used to denote Words, (*a*:sub:`1`, *a*:sub:`2`, ... )
    2. Language (**L**): The uppercase English letter *L* in boldface represents a Language.

In the case of English, Words would correspond to words such as "dog", "cat", etc. A Language would correspond to a set of words such as { "dog", "cat", "hamster", ... } or { "tree", "flower", "grass", .... }.

The number of Words in a Language is denoted | **L** |. 

It will sometimes be necessary to refer to indeterminate Words, so notation is introduced for Word Variables,

    3. Word Variables (*α*, *β*, *γ*, etc. ): Lowercase Greek letters will represent variable words, i.e. indeterminate Words. Subscripts will occassionally be used to denote Word Variables, (*α*:sub:`1`, *α*:sub:`2`, ... ). The exceptions to this rule are *ζ*, *ξ* and *χ* which are reserved for Sentential Variables (see Section II.I for more information.)

The range of a Word Variable is understood to be the Language **L** from the Words are being drawn. 

With these definitions, the hierarchy of relationships that exist between a word *α*, its Language **L** and the set of all Strings **S** are given by,

    1. α ∈ L
    2. α ∈ S
    3. L ⊂ S

Axioms
^^^^^^

The goal of the current analysis is to leave the semantic interpretation of Words in a Language as ambiguous as possible. This ambiguity, it is hoped, will leave the results of the analysis applicable to palindromic structures in a variety of languages. This section details the minimal *necessary* assumptions that are placed on any String to be considered an element of a Language **L**, i.e. a Word. The axiom listed in this section is not *sufficient*; in other words, it is possible for a String to satisfy this axiom without being an element of a Language, but any Word that belongs to a Language must satisfy the axioms.

Let **L** be a Language. Let *s* be a String, not necessarily a member of **L**. Let *𝔞*:sub:`i` be the i:sup:`th` Character of the String *s*. Let *l(s)* be the length of *s*. Let *N*:sub:`s` be the set,

    { 1, 2, ... , l(s) }

**Axiom W.1: The Delimiter Axiom ** 

    s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ σ )

Additional axioms will be introduced in the natural progression of this work as the hierarchy of palindromic structure is codified. 

Inversion
^^^^^^^^^

Informally, the *Inverse* of a String is the reversed sequence of Characters in the String. The goal of this section is to define this notion precisely. In the process, the motivation for this definition will be elucidated. 

**Definition 1.2.1: String Inversion** Let *s* be a string with length *l(s)*. Let *𝔞*:sub:`i` be the *i*:sup:`th` character of the String *s*. Let **N**:sub:`s` be the set,

    { 1, 2, ... , l(s) }

Then, let *t* be a String with length *l(t)* and let *𝔟*:sub:`j` be the *j*:sup:`th` character of the String *t*. Let **N**:sub:`t` be the set,

    { 1, 2, ... , l(t)}. 
    
*t* is called the Inverse of *s* and is denoted *inv(s)* if it satisfies the following conditions, 

    1. l(t) = l(s) 
    2. ∀ i ∈ N:sub:`s`, j ∈ N:sub:`t`: [ ( j = l(s) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]

Since every Word is a String, the Inverse of Word is similarly defined, with the additional constraint that *s* belong to a Language **L**. The Inverse of a Word is easily understood through a few illustrative examples in English. The following table lists some words in English and their Inverses,

| Word | Inverse | 
| ---- | ------- |
| time | emit    |
| saw  | was     |
| raw  | war     |
| dog  | god     |
| pool | loop    |

However, this particular example is (intentionally) misleading. In this example, the Inverse of a word in English is also a word in English. In general, this property is not exhibited by the majority of words in any Language. In other words, every Word in an Language has an Inverse, but not every Inverse Word belongs to a Language. This phenomenon is exemplified in the following table,

| Word | Inverse | 
| ---- | ------- |
| cat  | x       |
| you  | x       |
| help | x       |
| door | x       |
| book | x       |

It should be clear the intent is to define a class of Words whose constituents belong to a class of *Invertible Words* if and only if their Inverse exists in the Language. As a first step towards this definition, String Inversion was introduced and formalized. In the next section, String Inversion will provide a subdomain in the domain of discourse over which to quantify the conditions that are to be imposed on the class of *Invertible Words*, i.e. the class of Words whose Inverses are also Words. 

Before defining the class of Invertible Words in the next section, this section is concluded with a theorem that strengthens the definition of String Inversion. This theorem will be used extensively in the subsequent sections.

**Theorem 1.2.1** *inv(inv(s)) = s*

Let *s* be a String with length *l(s)* and Characters *𝔞*:sub:`i`. Let **N**:sub:`s` be the set,

    { 1, 2, ... , l(s) }

Let *t = inv(s)* with length *l(t)* and Characters *𝔟*:sub:`j`. Let **N**:sub:`t` be the set,

    { 1, 2, ... , l(t) }

By the Definition 1.2.1,

    1. l(t) = l(s)
    2. ∀ i ∈ N:sub:`s`, ∀ j ∈ N:sub:`t`: [ (j = l(s) - i + 1) →  ( 𝔟:sub:`j` = *𝔞*:sub:`i` ) ]

Now, let *u = inv(t)* with length *l(u)* and Characters *𝔠*:sub:`k`. Let **N**:sub:`u` be the set,

    { 1, 2, ... , l(u) }

Applying Definition 1.2.1 again,

    1. l(u) = l(t)
    2. ∀ j ∈ N:sub:`t`, ∀ k ∈ N:sub:`u`: [ (k = l(t) - j + 1) → ( 𝔠:sub:`k` = 𝔟:sub:`j` ) ] 
 
Since *l(t) = l(s)* (step 1) and **N**:sub:`t` *=* **N**:sub:`s` (by definition of natural numbers), these substitions may be made in step 4,

    5. ∀ i ∈ N:sub:`s`, ∀ k ∈ N:sub:`u`: [ ( k = l(s) - (l(s) - i + 1) + 1 )  → ( 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` ) ]

The index *k* may be simplified,

    6. k = l(s) - l(s) + i - 1 + 1 = i

Therefore,
    
    7. ∀ i ∈ N:sub:`s`, ∀ k ∈ N:sub:`u`: [ ( k = i)  → ( 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` ) ]

This may be rewritten, noting the condition *k = i*,

    8. ∀ i ∈ N:sub:`s``: 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` ) 

Now, substitute the definition of 𝔟:sub:`j` from step 2 (where j = l(s) - i + 1) into the equation for  𝔠:sub:`k`,

    9. ∀ i ∈ N:sub:`s``: 𝔠:sub:`k` = 𝔞:sub:`i` 

Since *u* and *s* have the same length (l(u) = l(t) = l(s)) and the same characters in the same order (𝔠:sub:`k` = 𝔞:sub:`i`  for all i), it can be concluded that *u = s*. Recall that u = inv(t) and t = inv(s).  Substituting, the desired result is obtained, *inv(inv(s)) = s*. ∎ 

Section I.III: Word Classes 
---------------------------

It will be necessary to define special classes of Words in a Language to properly describe the Language's palindromic structure. These classes be used extensively in the next section.

Reflective Words 
^^^^^^^^^^^^^^^^

The concept of *Reflective Words* can be easily understood by examining some examples in English,


|    Word    |
| ---------- |
| mom        |
| dad        |
| noon       |
| racecar    |
| madam      |
| level      | 
| civic      |

From this list, it should be clear what is meant by the notion of *reflective*: Reflective Words are words that are unchanged by a String Inversion. This property will be formally defined as follows.

**Definition 1.3.1: Reflective Words** Let *α* be any word from Language **L**. Let *𝔞*:sub:`i` be the *i*:sup:`th` Character in *α*. Let *l(α)* be the length of *α*. Let **N**:sub:`α` be the set,

    { 1, 2, ... , l(α) }

Then the set of Reflective Words **R** is defined as the set of *α* which satisfy the open formula,

    α ∈ R ↔ [ ∀ i ∈ N:sub:`α`:  𝔞:sub:`i` = 𝔞:sub:`l(α) - i` ]

A Word *α* will be referred to *reflective* if it belongs to the class of Reflective Words. The following theorem is an immediate consequence of this definition.

**Theoreom 1.3.1** α ∈ R ↔ α = inv(α)

(→)  Assume *α ∈ R*. Let *𝔞*:sub:`i` be the Characters in *α*. By definition, 

    1. ∀ i ∈ N:sub:`α`: 𝔞:sub:`i` = 𝔞:sub:`l(α) - i`

Let *β = inv(α)*. Let 𝔟:sub:`j` be the Characters in *β*. By the definition of String Inversion:

    2. l(β) = l(α)
    3. ∀ i ∈ N:sub:`α`, ∀ j ∈ N:sub:`β`: [ ( j = l(α) - i + 1 ) →  ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]
   
Substitute *j = l(α) - i + 1* into the equation from step 3 and remove the quantifiation over *j*:

    4. ∀ i ∈ N:sub:`α`: 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`i`

Now, use the property of Reflective Words from step 1 (𝔞:sub:`i` = 𝔞:sub:`l(α) - i` ) and substitute it into the equation from step 4:

    5.  4. ∀ i ∈ N:sub:`α`: 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`

Note that the index on the left side of this equation (l(α) - i + 1) corresponds to the character at position *i* in the reversed string β.  This is because the index *j* in the definition of String Inversion maps to the *l(α) - i + 1*:sup:`th`` position in the original string.

Since 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`for all i ∈ N:sub:`α`, and both strings have the same length, we can conclude that each character in *α* is equal to the corresponding character in β. Therefore the desired result is obtained: *α = β = inv(α)*

(←) Assume α = inv(α)

Let *𝔞*:sub:`i` be the Characters in *α* and let *𝔟*:sub:`j` be the Characters in *inv(α)*. By definition of String Inversion,

    1. l(α) = l(inv(α))
    2. ∀ i ∈ N:sub:`α`, ∀ j ∈ N:sub:`inv(α)`: [ ( j = l(α) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]

Since *α = inv(α)*, 𝔞:sub:`j` can be substituted for 𝔟:sub:`j` in the step 2,

    3. ∀ i ∈ N:sub:`α`, ∀ j ∈ N:sub:`inv(α)`: [ ( j = l(α) - i + 1 ) → ( 𝔞:sub:`j` = 𝔞:sub:`i` ) ]

Since the conditional inside of the quantification is only true when *j = l(α) - i + 1*, *j* can be substituted into the consequent of the conditional and the quantification over *j* can be dropped. Therefore, step 3 can be rewritten as,

    4. ∀ i ∈ N:sub:`α`: 𝔞:sub:`l(α) - i + 1` =  𝔞:sub:`i`

Similar to the previous part of the proof, the index on the left side (*l(α) - i + 1*) corresponds to the Character at position *i* in the reversed string, which is *α* itself in this case. Therefore, 

    5. ∀ i ∈ N:sub:`α`: 𝔞:sub:`i` =  𝔞:sub:`a<sub>l(α) - i`

This condition satisfies the definition of Reflective Words, so *α ∈ R*. ∎ 

Invertible Words 
^^^^^^^^^^^^^^^^

As discussed previously, the concept of *Invertible* is exemplified in the pair of English words "*time*" and "*emit*". An *Invertible Word* is a Word whose inverse is part of the same Language **L**. This notion can now be made more precise with the terminology introduced in prior sections.

**Definition 1.3.2: Invertible Words** Let *α* be any Word in a Language **L**. Then the set of Invertible Words **I** is defined as the set of α which satisfy the open formula,

    α ∈ I ↔ inv(*α*) ∈ L 

A Word *α* will be referred to as *invertible* if it belongs to the class of Invertible Words.

This definition is immediately employed to derive the following theorems,

**Theorem 1.3.2** α ∈ I ↔ inv(α) ∈ I

Assume *α ∈ I*. By Definition 1.3.2,

    1. inv(α) ∈ L
    
Consider *inv(α)*. To show that it's invertible, it must be shown,

    2. inv(inv(α)) ∈ L. 

By Theorem 1.2.1,

    3. inv(inv(α)) = α
    
Since it is known *α ∈ L*, it follows,

    4. inv(inv(α)) ∈ L  
    
By the Definition 1.3.2, 

    5. inv(α) ∈ I
    
Therefore, *inv(α)* is also an Invertible Word. ∎ 

**Theorem 1.3.3** R ⊂ I

Assume *α ∈ R*. *𝔞*:sub:`i` be the Characters in *α*. By Definition 1.3.2,

    1. ∀ i ∈ N:sub:`α`: *𝔞*:sub:`i` = *𝔞*:sub:`l(α) - i``

Let *β = inv(α)* and let *𝔟*:sub:`j` be the Characters in *β*. By Definition 1.2.1,

    2. l(β) = l(α)
    3. ∀ i ∈ N:sub:`α`, ∀ j ∈ N:sub:`β``: (j = l(α) - i + 1) →  ( 𝔟:sub:`j` = 𝔞:sub:`i` )

Substitute (*j = l(α) - i + 1 *) into the consequent of the conditional in step 3 and drop the quantification over *j*,

    4. ∀ i ∈ N:sub:`α`:  𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`i`

Substituting the property of Reflective Words from step 2 into step 4,

    5. ∀ i ∈ N:sub:`α`:  𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`

Note that the index on the left side of the equation in step 5 (*l(α) - i + 1*) corresponds to the character at position *i* in the reversed string *β*.

Since *𝔟*:sub:`l(α) - i + 1` *= 𝔞*:sub:`l(α) - i` for *i ∈* **N**:sub:`α`, and both strings have the same length, we can conclude that each character in *α* is equal to the corresponding character in *β*. Therefore,

    6. α = β = inv(α)

By assumption, *α ∈ L*. From step 6, this implies *inv(α) ∈ L*. By Definition 1.3.2, this implies α ∈ I. In summary, the assumption α ∈ R implies α ∈ I. Therefore, every element in R is also an element in I, which means R ⊂ I. ∎ 

In the context of infinite sets such as **L** and **S**, "even" and "odd" refer to whether the set can be partitioned into two disjoint subsets of equal cardinality.

    1. Even Cardinality: An infinite set has even cardinality if it can be put into a one-to-one correspondence with itself, with each element paired with a distinct element.
    2. Odd Cardinality: An infinite set has odd cardinality if, after pairing each element with a distinct element, there is one element left over.

The set of non-reflective Invertible Words, **I** - **R** (where "-" represents the operation of set differencing), always has even cardinality because each word can be paired with its distinct inverse. The overall cardinality of **I** then depends on whether the set of Reflective Words, **R**, adds an "odd" element or not. This idea is captured in the next theorem.

**Theorem 1.3.4** If |R| is even, then |I| is even. If |R| is odd, then |I| is odd.

Partition the set of Invertible Words, **I**, into two disjoint subsets,

    1. **R**: The set of Reflective Words.
    2. **I** - **R**: The set of Invertible Words that are not Reflective.

For every word *α* in **I** *-* **R**, its inverse, *inv(α)*, is also in **I** *-* **R**. Furthermore, they form a distinct pair *(α, inv(α))*. This is because *α* is invertible but not reflective, so *α ≠ inv(α)*.

Since the elements of **I** *-* **R** can be grouped into distinct pairs, the cardinality |I - R| must be even.

The total number of Invertible Words is the sum of the number of Reflective Words and the number of Invertible Words that are not Reflective,

    3. |I| = |R| + |I - R|

Let |R| be even. Since |I - R| is always even, and the sum of two even numbers is even, |I| must also be even.

Let |R| be odd. Since |I - R| is always even, and the sum of an odd number and an even number is odd, |I| must also be odd. ∎ 

Section II: Sentences
=====================

The work so far has formally constructed a system for representing the primitive artifacts of a natural language, Characters (Alphabets) and Words (Language), without appealing to their interpretation in any way except insofar that it takes a stance on their *existence*. As the analysis moves up the chain of linguistic artifacts to the next highest level, Sentences, it is tempting to start incorporating semantic features into the theory. However, the objective is to derive palindromic conditions independent of a particular semantic interpretation. Therefore, as the analysis proceeds, special care will be given to the definition of a *Sentence*.

Section II.I: Definitions
-------------------------

Corpus
^^^^^^

The entire system so far constructed relies on the domain of **S**, the set of all Strings that can be formed from an Alphabet of Characters **Σ**. Attention has been confined to those entities that satisfy the Delimiter Axiom (*Axiom W.1*),

    s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ σ )

In other words, the definitions and theorems so far introduced deal with linguistics entities that do not possess a Delimiter Character. Delimiters will be of certain importance in describing palindromic structures, because Delimiters play a central role in the definition of the linguistic entity that will ultimately allow a palindrome to be rigorously defined, a *Sentence*. With that in mind, the concepts and definitions that pave the way to an explication of *Sentence* start with the definition of a *Corpus*.

**Definition 2.1.1: Corpus** The Corpus of Language **L** is denoted by **C**:sub:`L`. The Corpus set represents a collection of grammatically valid and semantically meaningful Strings.

From the definition, it can easily be seen the Corpus of a Language is a subset of the set of all possible Strings, **S**

   C**:sub:`L` ⊂ S 

Sentence
^^^^^^^^

Before proceeding with the definition of Sentences, some notation is introduced,

    1. Sentences (*ᚠ*, *ᚢ*, *ᚦ*, ... ): Anglo-Saxon (*Old English*) Runes represent a Sentence. Subscripts will occassionally be used in conjunction with Anglo-Saxon letters to denote Sentences, (*ᚠ*:sub:`1`, *ᚠ*:sub:`2`, ... ). 
    2. Sentential Variables (*ζ*, *ξ* *χ*): The lowercase Greek letters Zeta, Xi and Chi are reserved for indeterminate Sentences, i.e. Sentential Variables. Subscripts will occassionally be used in conjunction with these lowercase Greek letters to denote Sentential Variales, (*ζ*:sub:`1`, *ζ*:sub:`2`, ...)
    
**Definition 2.1.2: Sentence** A Sentence in Language **L** is an element of its Corpus. 

    ᚠ ∈ C:sub:`L`

From Definition 2.1 and Definition 2.2, it follows that a Sentence is a String,

    ᚠ ∈ S

It should be noted at this point that both Words and Sentences in the current formulation are elements of the same underlying set, the set of all Strings. This connection in the domain of Words and Sentences is what will allow the analysis to begin to construct the outline of palindromic structures in a Language and Corpus.

Notation
^^^^^^^^

In Section I.I, notation was introduced for representing Strings as a sets of ordered pairs. This form of representation provided a formal method for specifying various syntactical conditions and properties of Words. In a similar way, this method of set representation will now be leveraged to enrich the definition of a Sentence. Since all Sentences are Strings, all Sentences have Character-level set or sequence representations. This representation can be leveraged to construct a higher-level representation of Sentences as sets of Words. 

**Definition 2.1.3: Word-Level Representation of Sentences**

Let *ζ* be a Sentence in a Corpus C:sub:`L`. Let **Ζ** be the character-level set representation of *ζ*, i.e. an ordered sequence of Characters from the alphabet **Σ**. For example, if 𝔞:sub:`i` represent the Characters of **Σ**, a possible value of **Z** could be,

    Z = { (1, 𝔞:sub:`2`), (2, 𝔞:sub:`10`), (3, 𝔞:sub:`3`), ... }

Or using a sequence to implicitly represent the order,

    Z =  ( 𝔞:sub:`2`, 𝔞:sub:`10`, 𝔞:sub:`3` )

The word-level set representation of *ζ*, denoted by **W**:sub:`ζ`, is defined as the set of words obtained by splitting **Ζ** at each Delimiter Character, *σ*. Formally, **W**:sub:`ζ` is constructed using the *Delimiting Algorithm*,

**Definition 2.1.4: Delimiting Algorithm**

**Initialization**

Let **W**:sub:`ζ` = ∅ (the empty set).
   
**Iteration**  

1. For each contiguous subsequence of non-delimiter characters in **Ζ**, create a word *a* by applying the following mapping:

    Let the subsequence be (𝔞:sub:`k`, 𝔞:sub:`k+1`, ..., 𝔞:sub:`k+n`), where 𝔞:sub:`i` ≠ σ for k ≤ i ≤ k+n.

    Then, the corresponding word *a* is represented as the set:

        a = { (1, 𝔞:sub:`k`), (2, 𝔞:sub:`k+1`), ..., (n, 𝔞:sub:`k+n`) }

2. Add *a* to the set **W**:sub:`ζ`.

**Example** 

Let *ᚠ = "The dog runs"*. Then the Character level representation of  *ᚠ* is given by, 

    **ᚠ** = (T, h, e, σ, d, o, g, σ, r, u, n, s).

Then, applying the *Delimiting Algorithm*, its Word level representation is constructed, 

    **W**:sub:`ᚠ` = { "The", "dog", "runs" }.

Setion II.II: Sentence Classes 
------------------------------

Similarly to the classification of Words, Sentences will now be classified according to their syntactical properties. In particualr, in the study of palindromic structures, the notion of *Invertible Sentences* will be required. The definition, as is fitting in a work focused on palindromes, will mirror the definition of an *Invertible Word*

Invertible Sentences
^^^^^^^^^^^^^^^^^^^^

**Definition 2.2.2: Invertible Sentences** Let *ζ* be any Sentence in from a Corpus **C**:sub:`L`. Then the set of Invertible Sentences **K** is defined as the set of *ζ* which satisfy the open formula,

    ζ ∈ K ↔ inv(*ζ*) ∈ C:sub:`L`

A Sentence *ζ* will be referred to as *invertible* if it belongs to the class of Invertible Sentences.

This definition is immediately employed to derive the following theorems,

**Theorem 2.2.2** ζ ∈ K ↔ inv(ζ) ∈ K

(→) Assume ζ ∈ K

By Definition 2.2.2, the inverse of *ζ* belongs to the Corpus

    1. inv(ζ) ∈ C:sub:`L`

To show that inv(ζ) is invertible, it must be shown that,

    2. inv(inv(ζ)) ∈ C<sub>L</sub>.

From Theorem 1.2.1, for any string *s*, 

    3. inv(inv(s)) = s.  

By Definition 2.1.1 and Definition 2.1.1,

    4. ζ ∈ S

Where **S** is the set of all Strings. Therefore, it follows, 

    5. inv(inv(ζ)) = ζ.

From step 1 and step 5, it follows, 

    6. inv(inv(ζ)) ∈ C:sub:`L`

By Definition 2.2.2, this implies,

    7. inv(ζ) ∈ K.

(←) Assume inv(ζ) ∈ K

By Definition 2.2.2, 
    
    8. inv(inv(ζ)) ∈ C:sub:`L`

Applying Theorem 1.2.1,

    9. inv(inv(ζ)) = ζ.

From step 8 and step 9, it follows, 

    10. ζ ∈ C:sub:`L`

By Definition 2.2.2, it follows,

    11. ζ ∈ K.

Section II.III: Axioms 
----------------------

In Section I.II, the first axiom of the palindromic formal system was introduced. Now that definitions and notations have been introduced for Sentence and Corpus, the axioms may be expanded to further refine the character of the formal system being buitl. The Delimiter Axiom is reprinted below, so it may be considered in sequence with the other axioms.

**Axiom W.1: The Delimiter Axiom ** 

    s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ σ )

**Axiom S.1: The Containment Axiom**

    ∀ α ∈ L : ∃ ζ ∈ C:sub:`L` : α  ⊂:sub:`s` ζ

**Axiom S.2: The Extraction Axiom**

    ∀ ζ ∈ C:sub:`L` : ∀ α ∈ W:sub:`ζ`: α ∈ L

These axioms are used to prove the following theorems.

**Theorem 2.3.1** ∀ α : α ∈ W:sub:`ζ` → α ∈ L

The theorem can be stated in natural language as follows: If *α* belongs to the Word-level set representation of a Sentence *ζ*, then *α* belongs to the Language **L**.

Assume *α ∈* **W**:sub:`ζ`. In other words, *α* is a word in the Word-level set representation of the Sentence *ζ*. Since *ζ* is a Sentence, it belongs to the C:sub:`L`. Therefore, by the Axiom of Word Extraction, w ∈ L. ∎

**Theorem 2.2.2** ∀ ζ ∈ C:sub:`L`: W:sub:`ζ` ⊂ L

This theorem can be stated in natural language as follows: For any Sentence *ζ* in a Corpus **C**:sub:`L`, its Word-level set representation **W**:sub:`ζ` is a subset of the Language **L**.

Assume *ζ ∈* **C**:sub:`L`. W:sub:`ζ` be the Word-level set representation of *ζ*, as specified in Definition 2.1.3. By Axiom S.2, every Word *α* in the Word-level set representation of *ζ* belongs to the Language **L**. Since every element of W:sub:`ζ` belongs to **L**, we can conclude that W:sub:`ζ`  is a subset of **L**. The only assumption on *ζ* is that is belongs to the Corpus, therefore this conclusion can be generalized to all Sentences in a Corpus,

    ∀ ζ ∈ C:sub:`L`: W:sub:`ζ` ⊂ L 
    
In other words, every (Word-level set representation of a) Sentence from a Corpus is a subset of the Language **L**. ∎

When the terminology 

**Theorem 2.2.3** ζ ∈ K → ( ∀ α ∈ W:sub:`inv(ζ)`: α ∈ L)

This theorem can be stated in natural language as follows: If a Sentence *ζ* is invertible, then every word in its inverse, *inv(ζ)*, belongs to the Language **L**.

Assume *ζ ∈ K*. By Definition 2.2.2, t

    inv(ρ) ∈ C:sub:`L`

By Axiom S.3, every Word in the Word-level representation of inv(ρ) belongs to L. ∎

**Theorem 2.2.4** ζ ∈ K ↔ (∀ α ∈ W:sub:`ζ`: α ∈ I)

This theorem can be stated in natural language as follows: A Sentence is Invertible if and only if all its Words are Invertible.

(→) ζ ∈ K 

By Theorem 2.2.23, every Word in *inv(ζ)* belongs to **L**. Consider the Word-level representation of *ζ*

    W:sub:`ζ` = ( α:sub:`1`, α:sub:`2`, ... , α:sub:`n`)

Inversion of Sentence:  By the definition of sentence inversion, the word-level representation of inv(ρ) is (inv(w<sub>n</sub>), inv(w<sub>n-1</sub>), ..., inv(w<sub>1</sub>)).

Words in Inverse Belong to L: From step 1, we know that each of these inverted words (inv(w<sub>i</sub>)) belongs to L.

Definition of Invertible Words:  Since each inv(w<sub>i</sub>) ∈ L, by the definition of Invertible Words, each w<sub>i</sub> ∈ I.

Therefore: ∀ w ∈ W<sub>ρ</sub>: w ∈ I (all words in ρ are invertible).

(←) Assume ∀ w ∈ W<sub>ρ</sub>: w ∈ I (all words in ρ are invertible)

Word-Level Representation: Let ρ<sub>w</sub> = (w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub>) be the word-level representation of ρ.

Invertibility of Words: Since each w<sub>i</sub> ∈ I, by the definition of Invertible Words, each inv(w<sub>i</sub>) ∈ L.

Sentence Inversion: This means the sequence (inv(w<sub>n</sub>), inv(w<sub>n-1</sub>), ..., inv(w<sub>1</sub>)) is a valid sequence of words in L.

Grammatical Validity:  Since the inverted sequence is a valid sequence of words, and we haven't introduced any grammatical constraints yet, we can assume that the inverted sentence inv(ρ) is grammatically valid. (This assumption might need to be revisited when we introduce grammar rules later).

inv(ρ) ∈ C<sub>L</sub>: Since inv(ρ) is grammatically valid and composed of words from L, it belongs to the Corpus C<sub>L</sub>.

Definition of Invertible Sentences: Therefore, by the definition of Invertible Sentences, ρ ∈ I<sub>s</sub> (ρ is invertible).



Section II.IV: Delimiting
--------------------------

Now that the analysis has breached the level of Sentences, it begins to turn explicitly towards the consideration of palindromes and their structure. The next section will formally define palindromes and their properties. As preparation, this subsection will introduce an important tool that will be used to classify palindromes and provide insight into their structure.

Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a palindrome is distributed through its syntactical layers. The concepts of *perfect* and *imperfect* palindromes will be defined more rigorously in the following Section III, but as an intuitive introduction to this distinction and to help highlight the ability of a palindrome to encode meaning on multiple syntactic levels, consider the following two examples,

    1. Dennis sinned
    2. If I had a hifi

The first palindrome "*Dennis sinned*" is what will be termed a *perfect* palindrome, because its inverse does not require a rearrangement of its constituent Characters to preserve its semantic content. However, the second palindrome "If I had a hifi" is what will be termed an *imperfect* palindrome. To see the motivation behind this categorization, note the strict inversion of "If I had a hifi" would be (ignoring capitalization for now),

    Ifih a dah I fi

The order of the Characters in the Inverse of an imperfect palindrome is preserved, but in order to reconstitute its uninverted form, the characters must be re-sorted. It appears, then, that Delimiters play a central role in organizing the palindromic structure. In order to fully elucidate the structure of palindromes, it will be necessary to introduce into the discourse a method of referring to a Sentence's Delimiter count. 

Delimiter Count Function 
^^^^^^^^^^^^^^^^^^^^^^^^

As the introduction to this subsection made clear, it will be necessary to have a way of referencing the number of Delimiter Characters in a Sentence. Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.

**Definition 2.4.1: Delimiter Count Function** Let *t* be a String with length *l(t)*. Let *𝔞*:sub:`i` represent the *i*:sup:`th` character of the String *t*, where 

    i ∈ N:sub:`t` = { 1, 2, ..., l(t) }.

The delimiter count function, denoted by *δ(t)*, is defined as the number of Delimiter characters (*σ*) in the string *t*. Formally, *δ(t)* is defined as the cardinality of the set **D**:sub:`t` that satisfies the following formula:

    (j, ⲁ) ∈ D:sub:`t` ↔ (∃ i ∈ N:sub:`t` ( (i, ⲁ) ∈ T ) ∧ (ⲁ = σ) ∧ (j = i) )

where **T** is the set representation of the String *t*, 

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

Then, the delimiter count function is defined as

    δ(t) = | D:sub:`t` |

**Example** Consider the string *t = "a b c"*. The set representation of *t* is given by,
    
    T = { (1, a), (2, σ), (3, b), (4, σ), (5, c) }.

The set D:sub:`t` contains the ordered pairs *(2, σ)* and *(4, σ)*, where the first coordinate of the pair correspond the positions of the two Delimiter Characters in the String. Therefore, 
    
    D:sub:`t`= { (2, σ), (4, σ) }

From this it follows, | D:sub:`t` | is 2. Hence, *δ(s) = 2*.

The next theorem will be important for describing the structure of *imperfect palindromes*.

**Theorem 2.4.2** *δ(s) = δ(inv(s))*

Let *t* be a string with length *l(t)* and Characters denoted by *𝔞*:sub:`i`. Let **T** be the set representation of of *t* is given by,

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

Let *u = inv(t)* with Characters denoted by let *𝔟*:sub:`j`. By Definition 1.2.1,

    1. l(t) = l(u)
    2. ∀ i ∈ N:sub:`t`, ∀ j ∈ N:sub:`u`: [ ( j = l(s) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]

Let **D**:sub:`t` be the set of ordered pairs representing the positions of the Delimiter *σ* in *t*, and let D:sub:`u` be the corresponding set for *u*.

Assume *(j, σ) ∈*  **D**:sub:`u` . This means that the character at position *j* in the inverse string *t* is the Delimiter *σ*.

By the definition, *𝔟*:sub:`j` = *𝔞*:sub:`i` where *j = l(t) - i + 1*.  Since *𝔟*:sub:`j` *= σ*, we have *𝔞*:sub:`i`  *= σ*. This implies that the character at position *i* in the original string *t* is also a Delimiter.  Therefore, *(i, σ) ∈* **D**:sub:`t`

Thus, it is shown that for every element *(j, σ) ∈*  **D**:sub:`u`, there exists a corresponding element *(i, σ) ∈* **D**:sub:`t`, where *j = l(t) - i + 1*. This defines a one-to-one mapping between the elements of **D**:sub:`u` and **D**:sub:`t`. Since there's a one-to-one mapping between the elements of *D**:sub:`u` and **D**:sub:`t`, their cardinalities must be equal,

    3. | D:sub:`u` | = | D:sub:`s` |

By the definition of the delimiter count function, this means *δ(u) = δ(t)*. Since *u = inv(t)*, it has been shown *δ(inv(s)) = δ(s)*. ∎

**Theorem 2.4.3** δ(ζ) = δ(inv(ζ))

Definition 2.1.2, every Sentence is a String. Therefore, *ζ* is a String. By Theorem 2.4.2, 

    δ(ζ) = δ(inv(ζ))

Which is what was to be shown. ∎

Section III: Palindromic Structures
===================================

Section III.1: Pivots
--------------------

Let s be a palindromic string.

Part 1: If l(s) is even, then the pivot of s is the empty character (ε).
Part 2: If l(s) is odd, then the pivot of s is either the delimiter character (σ) or a character from the alphabet (𝔞, 𝔟, 𝔠, ...).
Proof:

Part 1 (Even Length):

Assume l(s) is even: This means l(s) = 2k for some integer k.

Palindrome Definition: By definition, a palindrome reads the same backward as forward. This implies that the first k characters of s must be the reverse of the last k characters.

Pivot Placement: To maintain this symmetry with an even number of characters, the pivot must lie exactly in the middle, between the two halves of the string. Since there's no character at this midpoint, the pivot must be the empty character (ε).

Part 2 (Odd Length):

Assume l(s) is odd: This means l(s) = 2k + 1 for some integer k.

Palindrome Definition: Again, the palindrome must read the same backward as forward. This implies that the first k characters are the reverse of the last k characters, with a single character remaining in the middle.

Pivot Placement: To maintain symmetry, this middle character must be the pivot. This character can be either:

Space Character (σ): If the palindrome has an odd number of words, the middle character might be a space.
Character from the Alphabet: If the palindrome has an odd number of characters within a single word, the middle character will be a letter from the alphabet.
Formalization:

We can express this theorem more formally using logical symbols:

∀s ( (l(s) is even) → (pivot(s) = ε) )
∀s ( (l(s) is odd) → (pivot(s) = σ) ∨ (pivot(s) ∈ {𝔞, 𝔟, 𝔠, ...}) )


Section III.3: Palindromic Classification 
-----------------------------------------

**Perfect Palindrome** A palindrome where the sequence of characters after the pivot is the exact inverse of the sequence of characters before the pivot.


**Imperfect Palindrome** A palindrome where the inverse of the sequence of characters on one side of the pivot is contained within the sequence of characters on the other side of the pivot.


Space Indeterminacy:

In imperfect palindromes like "borrow or rob," the inverse of the initial segment ("worrob") doesn't perfectly mirror the final segment ("rob") due to the space. However, the inverse of "rob" ("bor") is contained within "worrob."
Containment Constraint:

This leads to your insightful observation about the containment constraint. The possible interpretations of the inverse of the segment after the pivot must either contain or be contained by the inverse of the segment before the pivot.
Formalizing the Constraint:

We can formalize this constraint using our existing notation:

Let s be an imperfect palindrome with a Type 2 pivot. Let s1 be the substring before the pivot, and s2 be the substring after the pivot. Then:

inv(s1) ⊂ inv(s2)  OR  inv(s2) ⊂ inv(s1)

(where ⊂ denotes the substring relation)