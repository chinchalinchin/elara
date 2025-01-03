Appendix
========

This section contains notes and ideas that do not serve to establish the main results of the work, but the author believes may nevertheless prove useful in extending the formal theory into other epistemological domains.

Table of Contents
^^^^^^^^^^^^^^^^^
- Section A.I: Compound Words
- Section A.II: Delimiter Count Function
- Section A.III: Palindromic Pairs
- Section A.IV: Categories
- Section A.V: Sigma Induction
- Section A.VI: Reflective Structures
- Section A.VII: Intervention

Section A.II: Compound Words 
----------------------------

.. note::

    Part of the ambiguity in imperfect palindromes is that multiple different palindromes can map to the same *σ-reduced* form. When Delimiters are removed from a Sentence, a certain class of Words can remain in the Language, because their semantic content *"transmutes"*. In the author's opinion, the class of Compound Words bears some relation to palindromic structures, but the exact relation has yet to be uncovered.

**Definition A.1.1: Compound Words** η ∈ CW:sub:`L` ↔ [(∃ α, β ∈ L: η = αβ)  ∨  (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ)] ∧ (η ∈ L)

This formalization can be translated into natural language as follows: A Word *η* in a Language **L** is a Compound Word if and only if,

    1. Base Case (*∃ α, β ∈ L: η = αβ*) ∧ (η ∈ L):  *η* can be formed by concatenating two words from **L**, and *η* belongs to **L**.
    2. Recursive Step [ (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ) ∧ (η ∈ L) ]: *η* can be formed by concatenating a word from **L** with a Compound Word from **L**, and *η* belongs to **L**. ∎

The constraint *w ∈* **L** ensures that the concatenated String *η* is not just a String, but also a valid Word within the Language **L**.

**Examples**

*"teapot"* is a Compound Word because it can be formed by concatenating *"tea"* and *"pot"*, and *"racecar"* is itself a word in English.

*"nevertheless"* is a Compound Word formed from *"never"*, *"the"*, and *"less"*

*"formrat"* is not a Compound Word, even though it can be formed by concatenating Words from the Language, i.e. *"form"* and *"rat"* are both valid words, the concatenation *"formrat"* is not a valid Word in English.

**Definition A.1.2: Compound Invertible Words** η ∈ CIW:sub:`L`  ↔ [ (η ∈ CW:sub:`L`)  ∧ (η ∈ I) ]

In natural language: A word η in a language **L** is a Compound Invertible Word if and only if it is both a Compound Word and an Invertible Word. Using notation for set intersections, this definition can be revised to read,

    CIW:sub:`L` = CW:sub:`L` ∩ I ∎

**Example**

"racecar" is a compound invertible word because it's both a compound word and its own inverse.

Section A.II: Delimiter Count Function 
--------------------------------------

.. note::

    It is the author's opinion there is a type of *algebraic structure* embedded in Language through the constraints of syntax. This section highlights one of the functions defined within this structure. While the function is not required to prove the main results of this work about Palindromes, it is an interesting function in its own right.

Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a Palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a Palindrome is distributed through its syntactical layers. The concepts of *Perfect* and *Imperfect* Palindromes are be defined more rigorously in Section III, but as an intuitive introduction to the ability of a Palindrome to encode meaning on multiple syntactic levels and as a justification for the introduction of the Delimiter Count Function, consider the following two examples,

    1. dennis sinned
    2. if i had a hifi

The first palindrome "*dennis sinned*" is what will be termed a *Perfect* Palindrome, because its inverse does not require a rearrangement of its constituent Characters to preserve its semantic content. However, the second Palindrome *"if i had a hifi"* is what is termed an *Imperfect* Palindrome. To see the motivation behind this categorization, note the strict inversion of "If I had a hifi" would be (ignoring capitalization for now),

    ifih a dah i fi

The order of the Characters in the Inverse of an Imperfect Palindrome is preserved, but in order to reconstitute its uninverted form, the Delimter Characters must be re-sorted. It appears, then, that Delimiters play a central role in organizing the palindromic structure. 

The study of Delimiter Characters in a Sentence bears study beyond its application to palindromic structures, though. The following section of the Appendix introduces this function for quantifying the number of Delimiters in a sentence. Various properties about this function are then proved, in particular how the function interacts with other linguistic operations and functions that have been defined in the main body of the work. 

Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.

**Definition A.2.1: Delimiter Count Function** Let *t* be a String with length *l(t)*. Let **T** be the Character-level representation of *t* with the Characters *𝔞*:sub:`i` denoting the *i*:sup:`th` character of the String *t*, where *1 ≤ i ≤ l(t)*,

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

The Delimiter Count Function, denoted by *Δ(t)*, is defined as the number of Delimiter Characters (*σ*) in the string *t*. Formally, *Δ(t)* is defined as the cardinality of the set that satisfies the following formula:

    D:sub:`t` ↔ { (i, ⲁ) ∈ T | ⲁ = σ, 1 ≤ i ≤ l(t) } 

Then, the delimiter count function is defined as

    Δ(t) = | D:sub:`t` | ∎

**Example** 

Consider the string *t = "a b c"*. The Character-level set representation of *t* is given by,
    
    T = { (1, "a"), (2, σ), (3, "b"), (4, σ), (5, "c") }.

By Definition A.2.1, The set **D**:sub:`t` contains the ordered pairs *(2, σ)* and *(4, σ)*, where the first coordinate of each pair correspond the positions of the two Delimiter Characters in the String. Therefore, 
    
    D:sub:`t`= { (2, σ), (4, σ) }

From this it follows, 

    | D:sub:`t` | = 2 
    
Hence, 
    
    Δ(t) = 2 ∎

From the previous example, it can be seen the Delimiter Count function takes a Sentence as input and produces a non-negative integer (the Delimiter count) as output. Multiple sentences can have the same Delimiter count, making it a many-to-one function. While this many not be advantageous from a computational perspective, the Delimiter Count function has other interesting properties that make it worth studying. The following theorems describe some of its properties.

**Theorem A.2.1** ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1

.. note::

    I think this needs revised to be *Λ(ζ) ≥ Δ(ζ) + 1* to account for edge cases where the sentence has multiple Delimiters in sequence, or has a Delimiter at the end or beginning of the String. 
    
    Alternatively, this inconsistency might be resolvable by introducing an assumption about the structure of a Sentence. Perhaps all Delimiters between two consecutive Words should be treated as a single Delimiter? Or an Axiom to constrain the placement of Delimiters in Sentences?

In natural language, this theorem is stated: For any sentence *ζ* in a Corpus C:sub:`L`, the length of the Sentence is equal to its Delimiter count plus one.

Assume *ζ ∈* **C**:sub:`L`. Let *Δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the Character-level representation of ζ. Let **W**:sub:`ζ` be the word-level set representation of ζ. Recall **W**:sub:`ζ` is formed by splitting **Ζ** at each Delimiter Character *σ* with the Delimiting Algorithm in Definition 2.1.3.

Each word in **W**:sub:`ζ` corresponds to a contiguous subsequence of non-Empty, non-Delimiter Characters in **Ζ**.

Since Delimiters separate Words, and each Delimiter corresponds to one Word boundary, the number of Words in the Sentence is always one more than the number of delimiters. Therefore, the cardinality of **W**:sub:`ζ` (the number of words) is equal to the Delimiter count of *Δ(ζ)* plus one,

    | W:sub:`ζ` | = Λ(ζ) = Δ(ζ) + 1. ∎

The next two theorems establish the invariance of the Delimiter count under String Inversion for any String, and by extension, any Sentence.

**Theorem A.2.2** ∀ s ∈ S: Δ(s) = Δ(inv(s))

Let *t* be a string with length *l(t)*. Let *u = inv(t)*. By Definition 1.2.4,

    1. l(t) = l(u)
    2. ∀ i ∈ N:sub:`l(t)`: u[i] = t[l(t) - i + 1]

Let **D**:sub:`t` be the set of ordered pairs representing the positions of the Delimiter *σ* in *t*, and let **D**:sub:`u` be the corresponding set for *u*. Assume *(j, σ) ∈*  **D**:sub:`u`, then, by step 2,

    3. u[j] = t[l(t) - j  + 1]

This means that the Character at position *j* in the inverse string *t* is the Delimiter *σ*. Therefore, 

    4. (l(t) - j  + 1, σ) ∈* **D**:sub:`t`

Thus, it is shown that for every element *(j, σ) ∈*  **D**:sub:`u`, there exists a corresponding element *(i, σ) ∈* **D**:sub:`t`, where *i = l(t) - j + 1*. 

To make the mapping more explicit, define a function *f*: **D**:sub:`t` *→* **D**:sub:`u` as follows. For any (*i*, *σ*) ∈ **D**:sub:`t`, let 

    5. f((i, σ)) = (l(t) - i + 1, σ)
    
It will be shown that *f* is a bijection.

**Well Defined** If (*i*, *σ*) ∈ **D**:sub:`t`, then the Character at position *i* in *t* is *σ*. By step 2, the Character at position *l(t) - i + 1* in *u = inv(t)* is also *σ*. Therefore, 

    6. (l(t) - i + 1, σ) ∈ D:sub:`u`
    
In other words, *f* maps elements of **D**:sub:`t` to elements of **D**:sub:`u`. Thus, *f* is well defined.
 
**Injective** Suppose 

    7. f((i:sub:`1`, σ)) = f((i:sub:`2`, σ)). 
    
Then, it follows,

    8. (l(t) - i:sub:`1` + 1, σ) = (l(t) - i:sub:`2` + 1, σ). 
    
This in turn implies, 

    9. l(t) - i:sub:`1` + 1 = l(t) - i:sub:`2` + 1, 
    
So 
    10. i:sub:`1` = i:sub:`2`
    
Thus, 

    11. (i:sub:`1`, σ) = (i:sub:`2`, σ)
    
In other words, *f* is injective. 

**Surjective** Let *(j, σ)* be an arbitrary element of **D**:sub:`u`. Then the Character at position *j* in *u* is *σ*. Let 

    12. i = l(t) - j + 1. 
    
Then 

    13. j = l(t) - i + 1. 
    
By step 3, the Character at position *i* in *t* is also *σ*. So, 

    14. (i, σ) ∈ D:sub:t
    
And,

    15. f((i, σ)) = (l(t) - i + 1, σ) = (j, σ). 
    
Thus, *f* is surjective. 

This defines a bijective mapping between the elements of **D**:sub:`u` and **D**:sub:`t`. Since there's a one-to-one mapping between the elements of *D**:sub:`u` and **D**:sub:`t`, their cardinalities must be equal,

    16. | D:sub:`u` | = | D:sub:`s` |

By the definition of the delimiter count function, this means *Δ(u) = Δ(t)*. Since *u = inv(t)*, it has been shown *Δ(inv(s)) = Δ(s)*. 

Furthmore, an exact relationship has been estalished between the coordinates of Delimiters in Strings and their Inverses, 

    17. D:sub:`inv(t)` = { (l(t) - i + 1, σ) | (i, σ) ∈ D:sub:`t` } ∎

**Theorem A.2.3** ∀ ζ ∈ C:sub:`L`: Δ(ζ) = Δ(inv(ζ))

Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L`,

    1. ζ ∈ C:sub:`L`

By Definition 2.1.2, every Sentence is a String. Therefore, *ζ* is a String. By Theorem A.3.2, 

    1. Δ(ζ) = Δ(inv(ζ))

Which is what was to be shown. ∎

**Theorem A.2.4** ∀ α ∈ L: Δ(α) = 0

This theorem can be stated in natural language as follows: The Delimtier Count of any Word in a Language is zero.

Assume *α* is a Word in Language **L**,

    1. α ∈ L
    
By the Discovery Axiom W.1, all Words in Language do not have Delimiters,

    2. ∀ i ∈ N:sub:`l(s)`: α[i] ≠ σ

Therefore, *α* does not have any Delimiter Characters (*σ*). By Definition 2.4.1, *Δ(s)* counts the number of Delimiter Characters (*σ*) in a String *s*. Since *α* hasno Delimiter Characters, the Delimiter Count of *α* must be 0. Therefore,

    3. Δ(α) = 0 ∎

**Theorem A.2.5** ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

In natural language, this theorem can be stated as follows: For every Sentence in a Corpus, the String Length of the Sentence is equal to the Delimiter Count of the sentence plus the sum of the String Lengths of its Words.

Assume 

    1. ζ ∈ C:sub:`L`. 

Either each *ζ{i}* for *1 ≤ i ≤ l(ζ)* is Delimiter or it is a non-Delimiter, with no overlap. By Definition A.2.1, the number of Delimiter Characters in *ζ* is *Δ(ζ)*. 

By the Discovery Axiom W.1, words in **L** do not contain Delimiters. By Definition 2.1.3, the Words in **W**:sub:`ζ` are obtained by splitting *ζ*  at the Delimiters. Therefore, the total number of non-Delimiter characters in *ζ* is the sum of the Word Lengths l(ζ{i}) which is 

    2. Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Since every Character in *ζ* is either a Delimiter or part of a Word (and not both), the total number of Characters in *ζ* is the sum of the number of Delimiters and the number of Characters in Words. By Definition 1.1.3 of String Length, the total number of non-Empty characters in ζ is *l(ζ)*. Therefore, the number of non-Empty Characters in *ζ* is equal to the number of Delimiters plus the sum of its Word Lengths,

    3. ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ∎

**Theorem A.2.6** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Applying the results of Theorem A.2.1 and Theorem A.2.5, this theorem follows from simple algebraic manipulation. ∎

**Theorem A.2.7** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥  Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})

This theorem can be stated in natural language as follows: For any Sentence in the Corpus, its String Length is greater than or equal to the sum of the String Length of its Words. 

Assume *ζ ∈* **C**:sub:`L`. By Theorem A.2.4,
    
    1. Λ(ζ) ≥ 1

From Theorem A.2.6,

    2. l(ζ) + 1 - Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i}) = Λ(ζ)

Combining step 1 and step 2, the theorem is obtained through algebraic manipulation,

    l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α) ∎

**Theorem A.2.8** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ)

This theorem can be stated in natural language as follows: For any Sentence in a Corpus, its String Length is always greater than or equal to its Word Length.

Let *ζ* be an arbitrary Sentence in C:sub:`L`. Let **W**:sub:`ζ`` be the Word-level representation of *ζ*. By Definition 2.1.4, 

    1. Λ(ζ) = | W:sub:`ζ` |

By Theorem 1.2.3, each Word in **W**:sub:`ζ` consists of one or more non-Empty Characters. By Theorem 2.2.5, every Sentence is a Delimitation of its Words,

    2. ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

Where the operation of Delimitation inserts Delimiters between the Words of *ζ*. On the other hand, let *t* be the the Limitation of *ζ*,

    3. t = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

By Definition 1.2.7, Definition 1.2.8 and Definition 1.1.3 of String Length,

    4. l(DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) = l(ζ) ≥ l(t) = l(LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i})

By Definition 1.28,

    5. LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i} = (ζ{1})(ζ{2}) .... (ζ{Λ(ζ)-1})(ζ{Λ(ζ)})

By Theorem 1.1.1, 

    6. l((ζ{1})(ζ{2}) .... (ζ{Λ(ζ)-1})(ζ{Λ(ζ)})) = Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})

Therefore, combining steps 4 and 6

    7. l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Consider the summation,

    8. Σ:sub:`i = 1`:sup:`Λ(ζ)` 1

Clearly, since *l(ζ{i}) ≥ 1* for all *i*, it follows, 

    9. Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` 1

By the definition of summations, step 8 can be rewritten as,

    10. Σ:sub:`i = 1`:sup:`Λ(ζ)` 1 = 1 + 1 + 1 + .... + 1 = Λ(ζ)

Combining step 7, step 9 and  step 10,

    11. l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` 1 = Λ(ζ)

Since ζ was arbitrary, this can be generalized as,

    12. ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ) ∎

**Theorem A.2.9 (Informal)** ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

Let *u* and *t* be arbitrary strings in S. Let **U** and **T** be the Character-level representations of *u* and *t*, respectively:

    1. U = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(u)`)

    2. T = (𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)`)

The Character-level representation of *ut* is:

    3. UT = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(u)`, 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)``)

By Definition A.2.1, *Δ(u)* is the number of Delimiters in *u*, *Δ(t)* is the number of Delimiters in *t*, and *Δ(ut)* is the number of Delimiters in *ut*.

Since concatenation simply joins two Strings without adding or removing Characters, with the possible exception of Empty Characters through the Basis Clause of Definition 1.1.1, the number of Delimiters in *ut* is the sum of the number of Delimiters in *u* and the number of Delimiters in *t*. ∎

**Theorem A.2.9 (Formal)** ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

Let **D**:sub:`u` be the set of indices of Delimiters in *u*. Let **D**:sub:`t` be the set of indices of Delimiters in *t*. Let **D**:sub:`ut` be the set of indices of delimiters in *ut*,

    1. D:sub:`u` = { i | 1 ≤ i ≤ l(u) and u[i] = σ }
    2. D:sub:`t` = { j | 1 ≤ j ≤ l(t) and t[j] = σ }
    3. D:sub:`ut` = { k | (1 ≤ k ≤ l(u) + l(t)) ∧ ((k ≤ l(u) ∧ UT[k] = σ) ∨ (k > l(u) ∧ UT[k] = σ)) }
   
It is clear that D:sub:`ut` is the union of two disjoint sets, since the indices of the Delimiters in *t* have been shifted by *l(u)*. Therefore,

    | D:sub:`ut` | = | D:sub:`u` | + | D:sub:`t` |.

By Definition A.4.1, this is equivalent to,

    Δ(ut) = Δ(u) + Δ(t)

Since u and t were arbitrary strings, this can be generalized,

    ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t) ∎

**Theorem A.2.10** ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)

Let *u* and *t* be arbitrary strings in S.

By Theorem A.4.2,

    1. Δ(s) = Δ(inv(s)).

Therefore, 

    2. Δ(ut) = Δ(inv(ut)).

By Theorem A.2.9,
 
    3. Δ(ut) = Δ(u) + Δ(t).

Combining steps 2 and 3, it follows, 

    4. Δ(inv(ut)) = Δ(ut) = Δ(u) + Δ(t)

Since *u* and *t* were arbitrary strings, this can be generalized,

    5. ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t) ∎

**Theorem A.2.11** ∀ t ∈ S: Δ(ς(t)) = 0

This theorem can be stated in natural language as follows: For any String, the Delimiter Count of its *σ*-Reduction is 0.

Let t be an arbitrary string in **S**,

    1. t ∈ S

By Definition 3.1.2, *ς(t)* is the String obtained by removing all occurrences of the Delimiter character *σ* from *t*. By Definition A.2.1, Δ(t) is the number of Delimiter Characters *σ* in a String *t*. Since *ς(t)* has all its Delimiters removed, it contains no occurrences of the Character *σ*. Therefore, 

    2. Δ(ς(t)) = 0

Since *t* was an arbitrary string in **S**, this can be generalized over **S**,

    3. ∀ t ∈ S: Δ(ς(t)) = 0 ∎

**Theorem A.2.12** ∀ t ∈ S: l(ς(t)) + Δ(t) = l(t)

Translation: For any String, its String Length is equal to the String Length of its σ-reduction plus its Delimiter Count.

Let *t* be an arbitrary String in **S**,

   1. t ∈ S

By Definition 3.1.2, *ς(t)* is the String obtained by removing all occurrences of the Delimiter character *σ* from *t*.

By Definition A.2.1, *Δ(t)* is the number of Delimiter characters in *t*.

By Definition 1.1.3, *l(t)* is the total number of non-Empty Characters in *t*, including Delimiters.

Similarly, *l(ς(t))* is the number of non-DelimiterCcharacters in *t*.

Every Character in *t* is either a Delimiter or a non-Delimiter character. Therefore, the total number of characters in *t* is the sum of the number of non-delimiter characters and the number of delimiter characters.

Therefore,

    2. ∀ t ∈ S: l(ς(t)) + Δ(t) = l(t)

Since *t* was an arbitrary String, this can be generalized over **S**,

    1. ∀ s ∈ S: l(s) = l(ς(t)) + Δ(s)  ∎

Theorem A.2.12 expresses a fundamental relationship between the String Length of a String, the String Length of its σ-reduction, and its Delimiter Count. It essentially states that the original String Length can be decomposed into the String Length of the String without Delimiters (the *σ*-reduction) and the number of Delimiters that were removed (the Delimiter Count).

**Example**

Let *t = (𝔞)(σ)(𝔟)(σ)(𝔠)*. Then, by Definition 3.1.2,

    ς(t) = 𝔞𝔟𝔠

The following quantities can then be calculated,

    l(t) = 5    
    Δ(t) = 2
    l(ς(t))= 3

And indeed, 

    l(t) = l(ς(t)) + Δ(t) ∎

**Theorem A.2.13** ∀ ζ ∈ C:sub:`L`: l(ς(t)) + Λ(ζ) = l(ζ) + 1

Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L`,

    1. ζ ∈ C:sub:`L`

By Definition 2.1.2, every Sentence is a String. Therefore, Theorem A.2.12 may be applied to *ζ*

    2. l(ζ) = l(ς(ζ)) + Δ(ζ)

By Theorem A.2.1,

    3. Λ(ζ) = Δ(ζ) + 1

Rearranging,

    4. Δ(ζ) = Λ(ζ) - 1

Substituting the expression for *Δ(ζ)* from step 4 into the equation from step 2,

    5. l(ζ) = l(ς(ζ)) + (Λ(ζ) - 1)

Rearranging the terms, 

    6. l(ς(ζ)) + Λ(ζ) = l(ζ) + 1

Since ζ** was an arbitrary Sentence in **C**:sub:`L`, this can be generalized over the Corpus as,

    7. ∀ ζ ∈ C:sub:`L`: l(σ_reduce(ζ)) + Λ(ζ) = l(ζ) + 1 ∎

Section A.III: Palindromic Pairs
--------------------------------

The only constraint on a Language is that it must consist of Words. This is guaranteed by the Extraction Axiom S.2. The only constraint on Words is that they must not contain the Delimiter. This is guaranteed by the Delimiter Axiom W.1. 

Since *σ-reduction* removes the Delimiter Character when it projects a Sentence onto the *σ-reduced* Alphabet, this process can viewed as the construction of another formal Language. In other words, given a Language and Corpus, the operation of *σ-reduction* implies the existence of a second Language which encodes the original Sentences. This second Language loses much of its semantic coherence with respect to its "*mother*" Corpus, but it nevertheless contains semantic information. 

This idea motives the definition of a *σ-Pairing Language*.

**Definition A.3.1: σ-Pairing Language**

The σ-Pairing Language L:sub:`σ` of a Corpus C:sub:`L` is defined as the set of Words *α* that satisfy the following formula, 

    α ∈ L:sub:`σ` ↔ ∃ ζ ∈ C:sub:`L`: α = (ζ ⋅ Σ:sub:`σ`)

This definition captures the idea that the σ-Pairing Language consists of all the Strings that can be generated by applying σ-reduction to the Sentences in the Corpus. It directly links the elements of L:sub:σ to the σ-reduced forms of the Sentences, ensuring that the Pairing Language is derived from the original Corpus.

**Theorem A.3.1** ∀ α ∈ L: α ∈ L:sub:`σ` ↔ [ ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:s α ]

This theorem can be stated in natural language as follows: The *σ*-Pairing Language contains a Word *α* if and only if there exists a Sentence *ζ* and a Word *β* that belongs to Sentence *ζ* such that *α* is contained in *Ζ ⋅ Σ*:sub:`σ`.

(→) Assume,

    1. α ∈ L:sub:`σ`
    
By Definition A.1.1, 

    2. ∃ ζ ∈ C:sub:`L`: α = (Ζ ⋅ Σ:sub:`σ`).

By Definition (TODO) of *σ-reduction*, (*ζ* ⋅ **Σ**:sub:`σ`) is obtained by concatenating the Words *ζ{i}* for 1 ≤ i ≤ Λ(ζ) without Delimiters,

    3. α = (ζ ⋅ Σ:sub:`σ`) = (ζ{1})(ζ{2})...(ζ{n})

Since each *ζ{i}* is a contiguous subsequence of *α*, it follows from Theorem 1.2.2,

    4. ∀ i ∈ N:sub:`n`: ζ{i} ⊂:sub:`s` α.

Therefore, 

    5. ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` α 

(←) Assume,

    1. ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` α.

Let *ζ{i}* be the Word in *ζ* such that *1 ≤ i ≤ Λ(ζ)* and

    2. ζ{i} ⊂:sub:s α.

By Definition (TODO) of *σ-reduction*, (*ζ* ⋅ **Σ**:sub:`σ`) is obtained by concatenating the Words in *ζ{i}* without Delimiters,

    3. (ζ ⋅ Σ:sub:`σ`) = (ζ{1})(ζ{2})...(ζ{n})

Since *ζ{i}* *⊂*:sub:`s` *α* and *α* is a String formed by concatenating Words, it follows that *α* must be a contiguous subsequence of (*ζ* ⋅ **Σ**:sub:`σ`).

Since *α* is a contiguous subsequence of (ζ* ⋅ **Σ**:sub:`σ`) and both are Strings formed by concatenating the same Words in the same order (without Delimiters), it follows that,

    4. α = (ζ ⋅ Σ:sub:`σ`).

Therefore, by Definition 3.1.3,

    5. α ∈ L:sub:`σ` 

Since both directions of the implication has been proven, the theorem is established:

    ∀ α ∈ L: α ∈ L:sub:`σ` ↔ [ ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:s α ] ∎

This theorem effectively characterizes the elements of the σ-Pairing Language. It states that a String belongs to the σ-Pairing Language if and only if it contains a Word from some Sentence in the Corpus. This highlights the connection between the σ-Pairing Language and the original Language and Corpus.

**Definition A.3.2: Palindromic Pairing Language**

Definition A.1.4 is altered in the following definition to quantify over the set of Palindromes in a Corpus. The Pairing Language that results is denoted L:sub:`P`. The set of Words *α* which satisfy this definition are referred to as the Palindromic Pairing Language of Language **L**, 

    α ∈ L:sub:`P` ↔  ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)

In particuar, if *α ∈ L*:sub:`P`, *α* is called the *Palindromic Image* of the Sentences *ζ* which generate it.

This definition is used to prove the following theorems.

**Theorem A.3.2** L:sub:`P` ⊂ L:sub:`σ`

Assume 
    
    1. α ∈ L:sub:`P`

By Definition A.1.2,

    ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)

By Definition (TODO) of Palindromes, the set of Palindromes **P** is a subset of C:sub:`L`. Therefore, 

    ζ ∈ C:sub:`L`

From step 2 and step 3, by Definition A.1.1, it follows,

    α ∈ L:sub:`σ`.

Therefore, 
    
    α ∈ L:sub:`P` → α ∈ L:sub:`σ`
    
This is exactly the definitio of a subset,

    L:sub:`P` ⊂ L:sub:`σ`. ∎

**Theorem A.3.3**: ∀ α ∈ L:sub:`P`: α = inv(α)

This theorem can be stated in natural language as follows: All Words in a Palindromic Pairing Language are their own Inverses. 

Assume 

    1. α ∈ L:sub:`P`. 
    
By Definition A.1.2,

    2. ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)

Since *ζ* *∈* **P**, by Definition TODO:

    3. (ζ  ⋅ Σ:sub:`σ`) = inv(ζ  ⋅ Σ:sub:`σ`)

Substituting *α* from step 2 into the equation in step 3,

    4. α = inv(α)

Therefore, 

    ∀ α ∈ L:sub:`P`: α = inv(α). ∎

This proof demonstrates that every String in the Palindromic Pairing Language is its own inverse. This follows directly from the definitions of Palindromes and the Palindromic Pairing Language. Since every String in the Palindromic Pairing Language is derived from a Palindrome, and Palindromes are defined by the invariance of their *σ-reduction* under inversion, the Strings in the Palindromic Pairing Language must also exhibit this invariance.

This theorem highlights a key property of the Palindromic Pairing Language: it consists solely of Strings that are symmetrical with respect to inversion. This property could be useful in various applications, such as identifying potential palindromes or generating text with specific symmetrical structures.

**Theorem A.3.4** L ∩ L:sub:`P` ⊆ R

This theorem can be stated in natural language as follows: The intersection of a Language **L** and its Palindromic Pair **L**:sub:`P` is a subset of the Language's Reflective Words **R**.

Assume 

    1. α ∈ L ∩ L:sub:P.

Since *α* *∈* **L**, it is a Word in the Language. Since *α* *∈* **L**:sub:`P`, by Theorem A.1.3, 

    α = inv(α).

By Definition 1.2.4 of String Inversion,

    ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1]

By Definition 1.3.1, it follows,

    α ∈ R.

Therefore, 

    α ∈ L ∩ L:sub:`P` → α ∈ R. 
    
This in turn implies,

    L ∩ L:sub:`P` ⊆ R. ∎

Before moving onto the last theorem of this section, some terminology is introduced. **R** was introduced in Section I.III to refer to the class of Reflective Words in a Language **L**. To be more explicit in the dependence of **R** on **L**, the notation **R**:sub:`L` will be used to make explicit the Language to which the class of Reflective Words refers.

With this notation adopted, the following theorem can be proven.

**Theorem A.3.5** L:sub:`P` ⊂ R:sub:`L_σ`

This theorem can be state in natural language as follows: Given a Language L, all words in its Palindromic Pairing Language are also Reflective Words in the σ-Pairing Language. 

In other show this theorem, it must be shown,

    1. ∀ α ∈ L: α ∈ L:sub:`P` → α ∈ R:sub:`L_σ`

Since by Definition 1.3.1, 

    2. α ∈ R:sub:`L_σ` ↔ inv(α) = α

If it can be shown,

    3. α ∈ L:sub:`P` → inv(α) = α

Then the theorem will follow tautologically from the laws of deduction. But step 3 is exactly Theorem 3.1.9. Therefore, the proof is complete. ∎


Section A.IV: Categories
-------------------------

Before introducing the notion of Categories, it must be kept in mind a Language **L** and a Corpous **C**:sub:`L` are treated as fixed sets known a priori to the construction of the current formal system. In a sense, Language and its Corpus are taken as primitive terms. It assumed a semantic assignment has occured outside of the confines of the formal system and the Words of a Language and Sentences of a Corpus have already been given determinate meanings. 

The notion of a *Category* is meant to explicate the linguistic entities which are colloquially referred to as a *"parts of speech"*, e.g nouns, verbs, adjectives, etc. However, it not the intention of this formal system to treat the semantic meaning of these grammatical categories in so far that certain schema of Categories provide a method of constructing semantic Sentences. The formal system takes no opinion on what constitutes its Categories, or how these Categories are used to construct a grammatical and meaningful Sentence; rather, the formal system assumes these Categories are used in exactly that capacity in order to derive the syntactical constraints they must abide in order to be considered categorical. 

This does not preclude the idea that a Category could map to the everyday notion of *noun* or *verb*, but the formal construction of grammatical categories cannot assume anything about the categorical structure of Sentences (e.g. noun-verb-noun is a valid Sentence form) without tying it to a specific semantic interpretation of what qualifies a Word to function in its categorical capacity. 

**Definition A.4.1: Category**

A semantic Category in a language **L**, denoted C:sub:`L`(m), is a set of Words in **L**, where *m* is a natural number representing the Category's index. ∎

Axioms 
^^^^^^

The fundamental assumptions regarding linguistic Categories in this formal system are now introduced. Each axiom will be justified by appeal to self-evidence. To see the motivation behind the first formal assumption about Categories adopted, 

TODO:

**Axiom G.1: The Completeness Axiom**

    ∃ m ∈ ℕ: L = ∪:sub:`1`:sup:`m` C:sub:`L`(i) ∎

TODO: 

**Definition A.4.4: Categorical Size**

The *m* such that,

    L = ∪:sub:`1`:sup:`m` C:sub:`L`(i)

is denoted with the lowercase Greek kappa, *κ*. *κ* is called the Categorical Size of a Language. ∎

TODO:

The choice of axioms for governing the logical calculus of Categories in the formal system is critical. Since the notion of a "grammatical categories" is inherently tied to the semantic interpretation of a Language and Corpus, the assumptions introduced about their nature must not violate the empirical reality of natural languages. 

To see what is meant by this, consider the proposed axiom, the Uniqueness Axiom.

**Proposed Axiom: The Uniqueness Axiom**

    ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: (∃! m ∈ N:sub:`κ`: ζ{i} ∈ C:sub:`L`(m)) ∧ ( (i, C:sub:`L`(m)) ∈ C:sub:`ζ` ) ∎

In natural language, the Uniqueness Axiom states: For every sentence *ζ* in the Corpus and for every Word index *i* in *ζ*, there exists a unique Category index *m* such that the *i*:sup:`th` Word of *ζ* belongs to Category **C**:sub:`L`(*m*), and this Category is recorded in the Categorical-level representation **C**:sub:`ζ` at index *i*.

This axiom captures a common-sense (though subtly flawed) notion that each Word in a Sentence maps to a single Category. However, this picture of *"grammaticality"* is tacitly assuming a *single* available semantic interpretation. To see a concrete example of why this axiom should not be adopted in a formal system that is meant to model *any* language, it suffices to look at a single example in a known language which contradicts it.

Consider the sentence *ᚠ = "visting friends can be annoying"*. In this case,there are two valid Categorical-level representations of this Sentence in English,


    C:sub:`ζ`:sub:`1` = { (1, Verb), (2, Noun), (3, Verb), (4, Verb), (5, Adjective) }
    
    C:sub:`ζ`:sup:`2` = { (1, Adjective), (2, Noun), (3, Verb), (4, Verb), (5, Adjective) }

Therefore, if the formal system wishes to account for the subtle ambiguities of natural language, the Uniqueness Axiom can not be adopted as an assumption.

Theorems
^^^^^^^^

**Theorem A.4.1**: ∀ α ∈ L: ∃ i ∈ N:sub:`M`: α ∈ C:sub:`L`(i)

By Axiom G.1, 

     L = ∪:sub:`1`:sup:`m` C:sub:`L`(i)

Therefore, any word α in L must belong to at least one of these Categories. ∎

Length
^^^^^^

Consider the English sentences, *ᚠ = "the man ran over the bridge* and *ᚢ = "the novel novel about a rose rose to the top"*

In *ᚠ*, both *"man"* and *"bridge"* map to the same Category, namely *nouns*. In other words, the Sentence can have multiple Words that belong to the same Category.  

In *ᚢ*, both occurrences of *"novel"* map to different Categories, namely *adjectives* and *nouns*. Further confounding the matter, another example of the ability of a single Word to map to multiple Categories is given through the simultaneous *noun*-*verb* mapping of *"rose"*

Since multiple Words can belong to the same Category, and conversely, the same Word can belong to multiple Categories, a notion of measuring the *Categorical Length* of a Sentence is now introduced. This notion will only measure the *unique* Categories found in a Sentence. For example, *"man"* and *"bridge"* would both be occurrences of the *noun* Category and would thus contribute a length of 1 to *Categorical Length*.

Similar to the construction of the Character-level and Word-level representation of a String, a method for constructing the Category-level representation of a Sentence is given below in the next definition. 

TODO: talk more about ambiguous sentences

**Definition A.4.2: Categorical-level Representation**

Let *ζ* be an arbitrary sentence from Corpus C:sub:`L`. The Categorical-level representation of a *ζ*, denoted **C**:sub:`ζ`, is defined as the set of sets *x* which satisfy the following open formula,


    x ∈ C:sub:`ζ` ↔ x = { (i, C:sub:`L`(m)) | ∀ i ∈ N:sub:`Λ(ζ)`: (ζ{i} ∈ C:sub:`L`(m)) } ∎

**Definition A.4.3: Categorical Interpretation**

Let *ζ* be an arbitrary sentence from Corpus C:sub:`L`. The *i*:sub:`th` Categorical Interpretation of *ζ*, denoted C:sub:`ζ`(i), is defined as,


    C:sub:`ζ`(i) ∈ C:sub:`ζ` ∎

**Definition A.4.4: Interpretation Length**

Let *ζ* be an arbitrary sentence from Corpus C:sub:`L`.  The *Interpretation Length* of a Sentence *ζ*, denoted by *ι(ζ)*, is defined as the number such that,

    ι(ζ) = | C:sub:`ζ` | ∎

**Definition A.4.5: Categorical Length**

Let *ζ* be an arbitrary sentence from Corpus C:sub:`L`. The *Categorical Length* of the *i*:sup:`th` Categorical Interpretation of *ζ*, denoted *λ(ζ, i)*, is defined as,

    λ(ζ, i) = | C:sub:`ζ`(i) | ∎


Section A.V: Sigma Inductions
-----------------------------



You're right that knowing l(σ_reduce(ζ)) (the length of the σ-reduced sentence) and Λ(ζ) (the number of words in the sentence) significantly constrains the possibilities for reconstructing the original sentence from its σ-reduced form. This has implications for the potential reversibility of σ-reduction and for understanding the structure of sentences.

Here's a more detailed breakdown of your observation and its implications:

Constraints on "Un-reducing" a Sentence:

Fixed Length of Non-Delimiter Characters: l(σ_reduce(ζ)) tells us the total length of the non-delimiter characters in the original sentence ζ.

Fixed Number of Words: Λ(ζ) tells us the number of words in the original sentence ζ.

Relationship between Delimiters and Words: We know from Theorem 2.4.1 that Λ(ζ) = Δ(ζ) + 1. This means the number of delimiters is always one less than the number of words.

Placement of Delimiters: The delimiters must be placed between the words in a way that creates valid words in the language L. This is where the constraint comes in. Not all arrangements of delimiters will result in valid words.

Analogy to Integer Partitioning:

The problem of reconstructing the original sentence from its σ-reduced form and the number of words is analogous to the problem of integer partitioning in number theory.

Integer Partitioning: Integer partitioning is the problem of finding all possible ways to write an integer as a sum of positive integers. For example, the integer 4 can be partitioned in the following ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Analogy: In our case:

l(σ_reduce(ζ)) is analogous to the integer being partitioned.
Λ(ζ) is analogous to the number of parts in the partition.
The lengths of the individual words in the sentence are analogous to the summands in the partition.
Implications:

Limited Reversibility: While σ-reduction is not strictly reversible (as we discussed before), knowing l(σ_reduce(ζ)) and Λ(ζ) significantly reduces the number of possible sentences that could have produced the given σ-reduced form.
Potential for Reconstruction: In some cases, if the language L has strong constraints on word formation and if l(σ_reduce(ζ)) and Λ(ζ) are sufficiently restrictive, it might be possible to uniquely reconstruct the original sentence, or at least narrow it down to a small set of possibilities.



Definition 3.1.15: σ-induction

Let s be a string in Σ:sub:σ (a σ-reduced string), let m be a natural number representing the desired number of "word-forms" (intended to correspond to words or potentially other linguistic units) in the resulting strings, and let X be a set of strings (either S, the set of all strings, or C:sub:L, the set of sentences in language L).

The σ-induction of s with m word-forms over the set X, denoted σ_induce(s, m, X), is the set of all possible strings that can be formed by inserting m-1 delimiters into s such that:

Delimiter Placement: Delimiters are inserted only between characters of s or at the beginning or end of s.
Word-Form Validity: Each of the m resulting substrings (separated by delimiters) is a valid string in the set X.
Number of Word-Forms: The resulting string has exactly m word-forms.
Order Preservation: The relative order of the characters in s is preserved in the resulting string.
Formally:

σ_induce(s, m, X) = { x ∈ X | σ_reduce(x) = s and Λ(x) = m }

Explanation:

Input: The function takes a σ-reduced string s, the desired number of word-forms m, and a set of strings X as input.
Output: It returns a set of strings, where each string is a possible "re-delimitation" of s that satisfies the given conditions, and Crucially, each "re-delimitation" belongs to the set X..
Conditions:
Delimiter Placement: Ensures that delimiters are placed in valid positions.
Word-Form Validity: Ensures that all the resulting substrings are valid members of the set X. If X = S, then no check is made beyond ensuring the substrings are valid strings. If X = C:sub:L, then each substring is verified as a valid word in the Language L.
Number of Word-Forms: Ensures that each string has exactly m word-forms.
Order Preservation: Ensures that the non-delimiter characters in the resulting strings maintain the same order as in the input string s.
Examples:

Let s = "nowart" and L = { "no", "now", "wart", "art", "a", "on" }.

σ_induce(s, 2, S) = { "no wart", "now art", "noσwart", "nowσart", ...}
σ_induce(s, 2, C:sub:L) = { "no wart", "now art" }
σ_induce(s, 3, S) = { "noσwart", "nowσart", ...}
σ_induce(s, 3, C:sub:L) = { } (no valid sentences with 3 words)
Observations:

Flexibility: This definition allows us to perform σ-induction over different sets of strings, providing flexibility in our analysis.
Relationship to Previous Definitions:
σ_induce(s, m, C:sub:L) is equivalent to our previous definition where the resulting strings had to be valid sentences in the language L.
σ_induce(s, m, S) is equivalent to the original idea where we considered all possible strings, regardless of whether they were valid sentences.
Further Considerations:

Computational Complexity: Generating σ_induce(s, m, S) is computationally simpler than generating σ_induce(s, m, C:sub:L), as it doesn't require checking for word validity in L.
Linguistic Relevance: σ_induce(s, m, C:sub:L) is more linguistically relevant, as it focuses on valid sentences.
Empty String: It might be worth explicitly stating what happens when s is the empty string or when m is less than 1.
This revised definition of σ-induction is a significant improvement. It's more general, flexible, and addresses the distinction between inducing over all strings and inducing over sentences in a specific language. It also clarifies the concept of "word-forms" which might not always be actual words, but could represent other linguistic units in the future.


**Theorem** 

Here's the corrected theorem statement and a revised proof:

Corrected Theorem 3.1.16:

∀ s ∈ S, ∀ m ∈ ℕ: |σ_induce(s, m, C:sub:L)| ≤ C(l(σ_reduce(s)), m - 1)

Translation: For any string s and any natural number m (representing the number of words), the cardinality of the set of sentences in C:sub:L obtained by σ-induction of s with m words is less than or equal to the number of combinations of choosing m-1 delimiter positions from l(σ_reduce(s)) possible positions.

Proof:

Let s be an arbitrary string in S, and let m be a natural number.

Length of σ_reduce(s): Let n = l(σ_reduce(s)). Since s is a σ-reduced string, it has no delimiters.

Delimiter Positions: In order to form a sentence with m words from σ_reduce(s), we need to insert m-1 delimiters.

Possible Positions: There are n-1 possible positions where we can insert delimiters between the characters of σ_reduce(s).

Combinations: The number of ways to choose m-1 positions out of n-1 positions is given by the binomial coefficient C(n-1, m-1), which is calculated as:

C(n-1, m-1) = (n-1)! / [(m-1)! * (n-m)!]
Upper Bound: The set σ_induce(s, m, C:sub:L) contains sentences formed by inserting m-1 delimiters into s such that the resulting substrings are valid words in L. Since there are at most C(n-1, m-1) ways to insert the delimiters, the number of valid sentences in σ_induce(s, m, C:sub:L) cannot be greater than this number.

Conclusion: Therefore:

|σ_induce(s, m, C:sub:L)| ≤ C(l(σ_reduce(s)), m - 1)
Since s and m were arbitrary, we can generalize:

*   ∀ s ∈ S, ∀ m ∈ ℕ: |σ_induce(s, m, C:sub:`L`)| ≤ C(l(σ_reduce(s)), m - 1)
This completes the proof. ∎

Explanation:

The proof now correctly operates on the string s in S.
The binomial coefficient C(n-1, m-1) gives us the maximum number of ways to insert delimiters, but the actual number of valid sentences might be less due to the constraint that the resulting substrings must be valid words in L.

Implications:

Upper Bound: This theorem provides an upper bound on the number of possible sentences that can be generated by σ-induction.
Combinatorial Nature: It highlights the combinatorial nature of the problem of reconstructing sentences from their σ-reduced forms.
Language Constraints: The actual number of valid sentences will be less than or equal to C(l(σ_reduce(s)) - 1, m - 1) and will depend on the specific constraints imposed by the language L.


Simplified Problem:

We now have:

s: A σ-reduced string (with no delimiters).
m: The desired number of "words" (or substrings separated by delimiters).
σ_induce(s, m, S): The set of all strings formed by inserting m-1 delimiters into s, with the only constraint being that delimiters can be placed at the beginning or end of s or between any two characters of s.
Calculation:

Length of s: Let n = l(s).

Possible Delimiter Positions: There are n-1 positions between the characters of s, plus the position before the first character and the position after the last character. So, there are a total of n+1 potential positions for delimiters. However, we know no delimiters can be in a word, so there are n-1 positions where m-1 delimiters can be placed.

Choosing Delimiter Positions: We need to choose m-1 positions out of these n-1 valid positions. Since the order of placing delimiters doesn't matter, this is a combination problem.

Combinations: The number of ways to choose m-1 positions from n-1 is given by the binomial coefficient:

C(n-1, m-1) = (n-1)! / [(m-1)! * (n-m)!]
Theorem 3.1.17:

∀ s ∈ Σ:sub:σ, ∀ m ∈ ℕ: |σ_induce(s, m, S)| = C(l(s) - 1, m - 1)

Proof:

Let s be an arbitrary σ-reduced string in Σ:sub:σ, and let m be a natural number.

Length of s: Let n = l(s).

Delimiter Positions:  To form a string with m words from s, we need to insert m-1 delimiters.

Possible Positions: In a σ-reduced string of length n, there are n-1 positions between the characters where delimiters can be inserted.

Combinations: The number of ways to choose m-1 positions out of n-1 positions is given by the binomial coefficient C(n-1, m-1):

C(n-1, m-1) = (n-1)! / [(m-1)! * (n-m)!]
σ_induce(s, m, S): The set σ_induce(s, m, S) contains all strings formed by inserting m-1 delimiters into s in any of the possible positions. Since each combination of delimiter placements results in a unique string, the cardinality of σ_induce(s, m, S) is equal to the number of possible combinations.

Conclusion: Therefore:

|σ_induce(s, m, S)| = C(l(s) - 1, m - 1)
Since s and m were arbitrary, we can generalize:

*   ∀ s ∈ Σ:sub:`σ`, ∀ m ∈ ℕ: |σ_induce(s, m, S)| = C(l(s) - 1, m - 1)
This completes the proof. ∎


Let's prove this formula using a combinatorial argument known as "stars and bars":

Theorem 3.1.17: ∀ s ∈ Σ:sub:σ, ∀ m ∈ ℕ: |σ_induce(s, m, S)| = C(l(s) + m - 2, m - 1) = C(l(s) + m - 2, l(s) - 1)

Proof:

Let s be an arbitrary σ-reduced string in Σ:sub:σ, and let m be a natural number.

Length of s: Let n = l(s).

Delimiter Positions: To form a string with m "words" (substrings separated by delimiters) from s, we need to insert m-1 delimiters.

Possible Positions: In a string of length n, there are n-1 positions between the characters where we can potentially place delimiters. Additionally, we can place delimiters at the beginning or the end of the string. However, we must exclude the possibility of placing two delimiters consecutively, or placing a delimiter next to an already existing delimiter.

Stars and Bars: We can represent the characters of s as "stars" (*) and the delimiters as "bars" (|). For example, if s = "abc" and we want to insert 2 delimiters (m=3), one possible arrangement is:

"a|b|c" (represented as ||*)
Another arrangement could be:

"|abc|" (represented as |***|)
Notice that we have n "stars" and m-1 "bars".

Combinatorial Problem: The problem of placing m-1 delimiters in a string of length n is equivalent to arranging n "stars" and m-1 "bars" in a sequence. However, we must make the restriction that no two bars can be adjacent to each other. This is not possible if we are inducing over the set of all strings S, since we are explicitly allowing for any possible combination of delimiters and characters, so long as no two delimiters are adjacent.

Number of Arrangements: The number of ways to arrange n stars and m-1 bars is given by the binomial coefficient C(n + m - 1, m - 1) or equivalently C(n + m - 1, n). However, since we do not allow for two delimiters to be adjacent in our definition of the delimiter count function, we must subtract one from each star to get the correct value. Since n = l(s), there are C(l(s) + m - 2, m - 1) possible ways to arrange the delimiters.

σ_induce(s, m, S): The set σ_induce(s, m, S) contains all strings formed by inserting m-1 delimiters into s in any of the possible positions. Since each combination of delimiter placements results in a unique string, the cardinality of σ_induce(s, m, S) is equal to the number of possible combinations, C(l(s) + m - 2, m - 1).

Conclusion: Therefore:

|σ_induce(s, m, S)| = C(l(s) + m - 2, m - 1)
Since s and m were arbitrary, we can generalize:

*   ∀ s ∈ Σ:sub:`σ`, ∀ m ∈ ℕ: |σ_induce(s, m, S)| = C(l(s) + m - 2, m - 1) = C(l(s) + m - 2, l(s) - 1)





How This Helps with σ-induction:

The theorems about delimiter symmetry in perfect palindromes (3.2.4 and 3.2.5) are key to simplifying the calculation of |σ_induce(s, m, S)| when s is the σ-reduction of a perfect palindrome.

Here's how:

Reduced Search Space: Instead of considering all possible delimiter placements in s, we only need to consider placements in the left half of s (up to the pivot). The placements in the right half are then determined by symmetry.

Simplified Combinations:

For even-length perfect palindromes with an even number of words m, we need to choose (m-2)/2 delimiter positions in the left half (of length l(s)/2).
For even-length perfect palindromes with an odd number of words m, we need to choose (m-1)/2 delimiter positions in the left half (of length l(s)/2).
For odd-length perfect palindromes with an even number of words m, we need to choose (m-2)/2 delimiter positions in the left half (of length (l(s)-1)/2).
For odd-length perfect palindromes with an odd number of words m, we need to choose (m-1)/2 delimiter positions in the left half (of length (l(s)-1)/2).
Calculating |σ_induce(s, m, S)| for Perfect Palindromes:

Let's derive formulas for each case, assuming s is the σ-reduction of a perfect palindrome ζ (i.e., s = σ_reduce(ζ) and ζ ∈ PP):

Case 1: Even-length s (l(s) = 2k), Even m (m = 2j):

|σ_induce(s, m, S)| = C(k - 1, j - 1) = C(l(s)/2 - 1, m/2 - 1)
Case 2: Even-length s (l(s) = 2k), Odd m (m = 2j + 1):

|σ_induce(s, m, S)| = C(k - 1, j) = C(l(s)/2 - 1, (m-1)/2)
Case 3: Odd-length s (l(s) = 2k + 1), Even m (m = 2j):

|σ_induce(s, m, S)| = C(k - 1, j - 1) = C((l(s)-1)/2 - 1, m/2 - 1)
Case 4: Odd-length s (l(s) = 2k + 1), Odd m (m = 2j + 1):

|σ_induce(s, m, S)| = C(k - 1, j - 1) = C((l(s)-1)/2 - 1, (m-1)/2)
Explanation:

We divide the length of s by 2 (or subtract one and then divide by 2 for odd-length s) to get the length of the left half.
We divide m by 2 (or subtract one or two depending on parity and then divide by 2) to get the number of delimiters to place in the left half.
We use the combination formula C(n, r) to calculate the number of ways to choose r delimiter positions from n available positions.


Theorem 3.2.6:

Let ζ ∈ PP with s = σ_reduce(ζ), n = l(s), and m be the desired number of words. Then:

Case 1: Even-length s (n = 2k), Even m (m = 2j):

|σ_induce(s, m, S)| = C(k - 1, j - 1) = C(n/2 - 1, m/2 - 1)
Case 2: Even-length s (n = 2k), Odd m (m = 2j + 1):

|σ_induce(s, m, S)| = C(k - 1, j) = C(n/2 - 1, (m-1)/2)
Case 3: Odd-length s (n = 2k + 1), Even m (m = 2j):

|σ_induce(s, m, S)| = C(k - 1, j - 1) = C((n-1)/2 - 1, m/2 - 1)
Case 4: Odd-length s (n = 2k + 1), Odd m (m = 2j + 1):

|σ_induce(s, m, S)| = C(k, j) = C((n-1)/2, (m-1)/2)
Proof:

Let ζ be an arbitrary perfect palindrome (ζ ∈ PP) and let s = σ_reduce(ζ), n = l(s), and m be the desired number of words.

Case 1: Even-length s (n = 2k), Even m (m = 2j):

Pivot: Since n is even, the pivot of ζ falls between two characters. By Theorem 3.1.9, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1. Since ζ is a perfect palindrome, by theorem 3.1.6, σ_reduce(ζ) = inv(σ_reduce(ζ)). The pivot of s lies between the characters at indices k and k+1.

Delimiter Placement: To form m = 2j words, we need to place m-1 = 2j-1 delimiters. By Theorem 3.2.4, the delimiters must be placed symmetrically around the pivot. We place j-1 delimiters in the left half of s (excluding the pivot character) and mirror them to the right half.

Left Half: The left half of s has length k. We have k-1 possible positions to place delimiters (excluding the character at index k itself because n is even).

Combinations: We need to choose j-1 positions out of k-1 to place the delimiters. The number of ways to do this is C(k-1, j-1).

Symmetry: For each valid placement in the left half, there's a unique corresponding symmetrical placement in the right half.

Conclusion: Therefore, |σ_induce(s, m, S)| = C(k - 1, j - 1) = C(n/2 - 1, m/2 - 1).

Case 2: Even-length s (n = 2k), Odd m (m = 2j + 1):

Pivot: Since n is even, the pivot of ζ falls between two characters. By Theorem 3.1.9, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1. Since ζ is a perfect palindrome, by theorem 3.1.6, σ_reduce(ζ) = inv(σ_reduce(ζ)). The pivot of s lies between the characters at indices k and k+1.

Delimiter Placement: To form m = 2j+1 words, we need to place m-1 = 2j delimiters. We place j delimiters in the left half of s (excluding the pivot character) and mirror them to the right half.

Left Half: The left half of s has length k. We have k-1 possible positions to place delimiters (excluding the character at index k itself because n is even).

Combinations: We need to choose j positions out of k-1 to place the delimiters. The number of ways to do this is C(k-1, j).

Symmetry: For each valid placement in the left half, there's a unique corresponding symmetrical placement in the right half.

Conclusion: Therefore, |σ_induce(s, m, S)| = C(k - 1, j) = C(n/2 - 1, (m-1)/2).

Case 3: Odd-length s (n = 2k + 1), Even m (m = 2j):

Pivot: Since n is odd, the pivot of ζ falls on a character. By Theorem 3.1.8, since ζ is a perfect palindrome, σ_reduce(ζ) = inv(σ_reduce(ζ)). The pivot of s is the character at index k+1. Since m is even, by Theorem 3.2.5, this pivot character cannot be a delimiter.

Delimiter Placement: To form m = 2j words, we need to place m-1 = 2j-1 delimiters. We place j-1 delimiters in the left half of s (excluding the pivot character) and mirror them to the right half. The remaining delimiter is placed at the pivot.

Left Half: The left half of s, excluding the pivot character, has length k. We have k-1 possible positions to place delimiters (excluding the character at index k itself because n is odd).

Combinations: We need to choose j-1 positions out of k-1 to place the delimiters. The number of ways to do this is C(k-1, j-1).

Symmetry: For each valid placement in the left half, there's a unique corresponding symmetrical placement in the right half.

Conclusion: Therefore, |σ_induce(s, m, S)| = C(k - 1, j - 1) = C((n-1)/2 - 1, m/2 - 1).

Case 4: Odd-length s (n = 2k + 1), Odd m (m = 2j + 1):

Pivot: Since n is odd, the pivot of ζ falls on a character. By Theorem 3.1.8, since ζ is a perfect palindrome, σ_reduce(ζ) = inv(σ_reduce(ζ)). The pivot of s is the character at index k+1. Since m is odd, by Theorem 3.2.5, this pivot character cannot be a delimiter.

Delimiter Placement: To form m = 2j+1 words, we need to place m-1 = 2j delimiters. We place j delimiters in the left half of s (excluding the pivot character) and mirror them to the right half.

Left Half: The left half of s, excluding the pivot character, has length k.

Combinations: We need to choose j positions out of k to place the delimiters. The number of ways to do this is C(k, j).

Symmetry: For each valid placement in the left half, there's a unique corresponding symmetrical placement in the right half.

Conclusion: Therefore, |σ_induce(s, m, S)| = C(k, j) = C((n-1)/2, (m-1)/2).

Final Result:

Combining all four cases, we have proven the theorem:

Let ζ ∈ PP with s = σ_reduce(ζ), n = l(s), and m be the desired number of words. Then:

Case 1: Even-length s (n = 2k), Even m (m = 2j):

|σ_induce(s, m, S)| = C(k - 1, j - 1) = C(n/2 - 1, m/2 - 1)
Case 2: Even-length s (n = 2k), Odd m (m = 2j + 1):

|σ_induce(s, m, S)| = C(k - 1, j) = C(n/2 - 1, (m-1)/2)
Case 3: Odd-length s (n = 2k + 1), Even m (m = 2j):

|σ_induce(s, m, S)| = C(k - 1, j - 1) = C((n-1)/2 - 1, m/2 - 1)
Case 4: Odd-length s (n = 2k + 1), Odd m (m = 2j + 1):

|σ_induce(s, m, S)| = C(k, j) = C((n-1)/2, (m-1)/2)
This completes the proof. ∎



Section A.VI: Reflective Structures
-----------------------------------

**Definition A.6.1: Reflective Structure**

A Reflective Structure, denoted **RS**, is the set of Strings *s* which satisfy the following formula,

    s ∈ RS ↔ [∃ n ∈ ℕ, ∃ p ∈ Χ:sub:`L`(n): (s = Π:sub:`i=1`:sup:`n` p(i)) ∧ (σ_reduce(s) = inv(σ_reduce(s)))]

**Definition A.6.2: Partial Limitations**

TODO: need to define what Π:sub:`i=i`:sup:`n` p(i) means for *i* not equal to 1.

**Theorem A.6.1** R ⊆ RS

**Theorem A.6.2** ∀ α ∈ L: α ∈ RS ↔ (α)(σ)(inv(α)) ∈ RS

**Theorem A.6.3** ∀ α ∈ L: α ∈ RS ↔ (α)(inv(α)) ∈ RS

**Theorem A.6.4**  ∀ p ∈ X:sub:`L`(2): Π:sub:`i=1`:sup:`2` p(i) ∈ RS ↔ Π:sub:`i=1`:sup:`1` p(i) = inv(Π:sub:`i=2`:sup:`2` p(i))

**Theorem A.6.5** P ⊆ RS


Section A.VII: Intervention
---------------------------

Colloquially, in the Sentence, *"never a dull day"*, the ordered Characters *"a"*,*"d"*,*"u"*,*"l"*, *"l"* are between the Words *"never"* and *"day"*. The concept of *Intervention* is introduced into the formal system to explicate this everyday notion of *"betweenness"*. A precise definition of what it means for a Character to *intervene* two Words in a Sentence is given using the operation of Delimitation introduced in Definition 1.2.7.

**Definition 2.1.6: Intervention**

Let *ζ* be a Sentence in C:sub:`L`. The Character *ζ[k]* is said to *intervene* the Words *ζ{i}* and *ζ{j}*, denoted as *(i/k/j)*:sub:`ζ`, if the following condition holdS

   l(DΠ:sub:`x=1`:sup:`i` ζ(x)) < k < l(ζ) - l(DΠ:sub:`x=1`:sup:`Λ(ζ) - j + 1` inv(ζ)(x)) + 1 ∎

The meaning of Definition 2.1.6 is not immediately intuitive, so a an explanation and thorough example are now presented to show how the definition corresponds to the common-sense notion of a Character falling between two Words in a Sentence.

Analyzing each component of the inequality in Definition 2.1.6, 

    1. l(DΠ:sub:x=1:sup:i ζ(x)): This represents the length of the Delimitation of the first i words of the sentence ζ. In simpler terms, it's the length of the string up to and including the i-th word, including the delimiters.
    2. k: This is the index of the character in question, ζ[k].
    3. l(ζ) - l(DΠ:sub:x=1:sup:Λ(ζ) - j + 1 inv(ζ)(x)) + 1: This is the more complex part. Let's break it down further:
    4. Λ(ζ) - j + 1: This calculates the index of the word in the reversed sentence that corresponds to the j-th word in the original sentence.
    5. DΠ:sub:x=1:sup:Λ(ζ) - j + 1 inv(ζ)(x): This is the Delimitation of the first Λ(ζ) - j + 1 words of the inverse of the sentence ζ. Essentially, it's the beginning portion of the reversed sentence up to the word that corresponds to the j-th word in the original sentence.
    6. l(DΠ:sub:x=1:sup:Λ(ζ) - j + 1 inv(ζ)(x)): This is the length of that initial portion of the reversed sentence.
    7. l(ζ) - l(DΠ:sub:x=1:sup:Λ(ζ) - j + 1 inv(ζ)(x)): This subtracts the length of the initial portion of the reversed sentence from the total length of the original sentence. This gives us the length of the remaining portion of the original sentence, starting from the character after the word corresponding to j in the original sentence.
    8. l(ζ) - l(DΠ:sub:x=1:sup:Λ(ζ) - j + 1 inv(ζ)(x)) + 1: Finally, we add 1 to get the index of the first character after the word corresponding to j in the original sentence.

The following example shows this Definition in action.

**Example** 

Let *ᚠ = "repaid a regal leper"*. Note the String and Word Lengths are given by,
   
    l(ᚠ) = 20
    
    Λ(ᚠ) = 4
    
The Word-level representation of this Sentence is given by,

    W:sub:`ᚠ` = { (1, "repaid"), (2, "a"), (3, "regal"), (4, "leper") }

Note *inv(ᚠ) = "repel lager a diaper"*. This is an example of an Invertible Sentence that maintains *semantic coherence* (i.e. all of its inverted Words are Words in the Language; see Definition 2.2.1 in the next subsection for a more formal definition of *semantic coherence*), but lacks *admissibility* (i.e. it is not a grammatical or syntactical sentence; see Definition 2.3.1 for a formal definition of *admissibility*.) The Word-level representation of the Inverse is given by,

    W:sub:`inv(ᚠ)` = { (1, "repel"), (2, "lager"), (3, "a"), (4, "diaper) }
    
To see how Definition 2.1.6 can be used to assert a Character falls between two Words in a sentence, calculate the following Limitations and String Lengths, consider the words *"a"* and *"leper"*. *"a"* corresponds to the Word Index 2,

    ᚠ{2} = "a"

Calculating the left-hand side of the inequality in Definition 2.1.6,

    DΠ:sub:`x=1`:sup:`2` ᚠ(x) = "repaid a"
    l(DΠ:sub:`x=1`:sup:`2` ᚠ(x)) = 8

The String Length of this Limitation is exactly equal to the Sentence Length *up to and including the Word at Index 2*. Now note *"leper"* occupies the Word Index 4, 

    ᚠ{4} = "leper"

This corresponds to a *j = 4* in Definition 2.1.6. The upperhand limit in the Limitation on the right-hand side of the inequality in Definition 2.1.6 is given by,

    Λ(ᚠ) - j + 1 = 4 -  4 + 1 = 1

Therefore, the corresponding Limitation of the Inverse Sentence for Definition 2.1.6 is given by,

    DΠ:sub:`x=1`:sup:`1` inv(ᚠ)(x) = "repel"
    l(DΠ:sub:`x=1`:sup:`1` inv(ᚠ)(x)) = 5

Working from the back of the Sentence, the String Length of this Limitation is exactly equal to the Sentence Length *up to and including the Word at Index 4*. Calculating the right-hand side of the inequality in Definition 2.1.6, 

    l(ᚠ) - l(DΠ:sub:`x=1`:sup:`1` inv(ᚠ)(x)) + 1 = 20 - 5 + 1 = 16

By Definition 2.1.6, the Characters *ᚠ[k]* between the indices of 8 and 16 (exclusive) *intervene* *ᚠ{2}* and *ᚠ{4}*, namely, 

    - ᚠ[9] = " "
    - ᚠ[10] = "r"
    - ᚠ[11] = "e"
    - ᚠ[12] = "g"
    - ᚠ[13] = "a"
    - ᚠ[14] = "l"
    - ᚠ[15] = " "

Therefore,

    - (2/9/4):sub:`ᚠ` (the 9:sup:`th` Character is between the second and fourth Word)
    - (2/10/4):sub:`ᚠ` (the 10:sup:`th` Character is between the second and fourth Word)
    - etc. ∎

As motivation for the first theorem on Interventions and a further clarification to show how Intervention and Delimitation are closely related, consider the following example.

**Example**

Let *ᚠ = "the world divides into facts"*. Then 

    Λ(ζ) = 5
    l(ζ) = 28

Consider what happens when the limits of the Delimitation of a Sentence and the Delimitation of its Inverse are such that *i = j* in the Definition 2.1.6. Let i = j = 2, i.e. consider the second Word in the Sentence, *"world"*. The relation of Intervention that obtains between *"world"* and itself should evaluate to false. In other words, no Characters intervene between a Word and itself. 

The Delimitation of the Sentence up to the Second Word is given by,

    DΠ:sub:`x=1``:sup:`2` ζ(x) = "the world"

The Delimitation of the Inverse Sentence up to the correspond index of the Second Word (e.g., 5 - 2 + 1 = 4) is given by (Note the Inverse Sentence does not ,

    DΠ:sub:`x=1``:sup:`5 - 2 + 1` inv(ζ(x)) = DΠ:sub:`x=1``:sup:`4` inv(ζ(x)) = "stcaf otni sedivid dlrow"

Therefore,

    l(DΠ:sub:`x=1``:sup:`2` ζ(x)) = 9
    l(DΠ:sub:`x=1``:sup:`4` inv(ζ(x))) = 24

The sum of these String Lengths is given by,

    l(DΠ:sub:`x=1``:sup:`2` ζ(x)) + l(DΠ:sub:`x=1``:sup:`4` inv(ζ(x))) = 9 + 24 = 33

Since the total String Length of both Delimitation exceeds the String Length of the entire Sentence, there does not exist a Character Index *k* such that *k* can be said to intervene the Word at index *i = j = 2*. ∎

This example provides justification for the next theorem.

**Theorem 2.1.3** ∀ ζ ∈ C:sub:`L`: ∀ i, j ∈ N:sub:`Λ(ζ)`: i ≠ j ↔ ∃ n ∈ N:sub:`l(ζ)`: (i/n/j):sub:`ζ`

This theorem can be stated in natural language as follows: For any Sentence in a Corpus, there exists a Character that intervenes two Words in the Sentence if and only the Words occupy different positions. Note this doesn't exclude possibility the Words at different positions are the same Word.

Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L` and let *i* and *j* be natural numbers such that,

    1. ζ ∈ C:sub:`L`
    2. i, j ∈ N:sub:`Λ(ζ)`
   
(→) Assume 

    3. i ≠ j

Without loss of generality (since the case i > j is symmetrical), assume 

    4. i < j

By Theorem 2.3.4, 

    5. ζ = DΠ:sub:`x=1`:sup:`Λ(ζ)` p(x)

Where 

    6. p ∈ in X:sub:`L(Λ(ζ))`

By Definition 1.2.7 of Delimitation, this means 

    7. ζ = (ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{Λ(ζ)}) 

By step 5, *ζ{i}* comes before *ζ{j}* in the Sentence *ζ*. By the Discovery Axiom W.1, there must be at least one delimiter character between *ζ{i}* and *ζ{j}* because they are distinct Words in a valid Sentence. 

Let *σ* be a delimiter Character between *ζ{i}* and *ζ{j}*. Let *k be the index of this σ in the character-level representation of ζ (i.e., *ζ[k] = σ*).

By the Definition 1.2.7 of Delimitation, 

    8. l(DΠ:sub:`x=1`:sup:`i` ζ(x)) 
    
Will give the index of the last character of ζ{i}. Since σ comes after ζ{i}, it follows,

    9. l(DΠ:sub:`x=1`:sup:`i` ζ(x)) < k

Similarly, 

    10. l(ζ) - l(DΠ:sub:`x=1`:sup:`Λ(ζ) - j + 1` inv(ζ)(x)) + 1 
    
Gives the index of the first Character after the Word corresponding to *ζ{j}* in the original sentence. Since σ comes before this character, it follows,

    11. k < l(ζ) - l(DΠ:sub:`x=1`:sup:`Λ(ζ) - j + 1` inv(ζ)(x)) + 1

Therefore, by Definition 2.1.6, 

    12. (i/k/j):sub:`ζ`

Thus,

    13. ∃ n ∈ N:sub:`l(ζ)`: (i/n/j):sub:`ζ`

(←) Assume a Character exists at index *n* in *ζ* such that it that intervenes *ζ{i}* and *ζ{j}*,

    1. ∃ n ∈ N:sub:`l(ζ)`: (i/n/j):sub:`ζ`

By Definition 2.1.6,

    2. l(DΠ:sub:`x=1`:sup:`i` ζ(x)) < n < l(ζ) - l(DΠ:sub:`x=1`:sup:`Λ(ζ) - j + 1` inv(ζ)(x)) + 1

Assume, for the sake of contradiction, that i = j.

    3. `l(DΠ:sub:`x=1`:sup:`i` ζ(x)) < n < l(ζ) - l(DΠ:sub:`x=1`:sup:`Λ(ζ) - i + 1` inv(ζ)(x)) + 1

Now, consider the term *l(DΠ*:sub:`x=1``:sup:`i`*ζ(x))*. This represents the String Length of the Delimitation of the first *i* words of *ζ*. By the Definition 1.2.7 of Delimitation, this includes the lengths of the first *i* words and the lengths of the *(i - 1)* delimiters between them.

Similarly, consider the term *l(DΠ*:sub:`x=1`:sup:`Λ(ζ) - i + 1` *inv(ζ)(x))*. This represents the String Length of the Delimitation of the first *Λ(ζ) - i + 1* words of *inv(ζ)*.  Since *inv(ζ)* has the same words as *ζ* but inverted and in reverse order, this is equivalent to the String Length of the uninverted Sentence up to the *i*:sup:`th` word of *ζ*, measured from the last Character in the String.

The sum of the String Lengths of these two portions of the Sentence *ζ* is always greater than the String Length of the Sentence, 

    4. l(DΠ:sub:`x=1``:sup:`i` ζ(x)) + l(DΠ:sub:`x=1`:sup:`Λ(ζ) - i + 1` inv(ζ)(x)) >  l(ζ) 

This follows from the fact that these two portions of ζ are overlapping since both  include terms for *ζ{i}* (*inv(ζ){Λ(ζ) - i + 1}* would be the corresponding Word in the Delimitation of the Inverse). From step 4, it then follows,

    5. l(DΠ:sub:`x=1`:sup:`i` ζ(x)) > l(ζ) - l(DΠ:sub:`x=1`:sup:`Λ(ζ) - i + 1` inv(ζ)(x))  
    
Adding 1 to both sides maintains the inequality in step 5,

    6. l(DΠ:sub:`x=1`:sup:`i` ζ(x)) + 1 > l(ζ) - l(DΠ:sub:`x=1`:sup:`Λ(ζ) - i + 1` inv(ζ)(x)) + 1

Combining this with the left-hand side of the inequality in step 5, we get:

    7. l(DΠ:sub:`x=1`:sup:`i` ζ(x)) < n < l(DΠ:sub:`x=1`:sup:`i` ζ(x)) + 1
   
But String Lengths are integers, and by the laws of arithmeti, there cannot exists a natural number between two numbers that are successors of one another. A contradiction has been dervied. Therefore, the assumption that *i = j* must be false.

    8. i ≠ j.

With both directions of the equivalence proven, since *ζ*, *i*, and *j* were arbitrary, this can be generalized as, 

    ∀ ζ ∈ C:sub:`L`: ∀ i, j ∈ N:sub:`Λ(ζ)`: i ≠ j ↔ ∃ n ∈ N:sub:`l(ζ)`: (i/n/j):sub:`ζ` ∎


**Theorem 2.1.4** ∀ ζ ∈ C:sub:`L`: ∀ i, j, k ∈ N:sub:`Λ(ζ)`: ∃ n, m ∈ N:sub:`l(ζ)`: (((i/n/j):sub:`ζ`) ∧ ((j/m/k):sub:`ζ`)) → (n < m)

TODO