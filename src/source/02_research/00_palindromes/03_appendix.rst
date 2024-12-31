Appendix
========

This section contains notes and ideas that do not serve to establish the main results of the work, but the author believes may nevertheless prove useful in extending the formal theory into other epistemological domains.

Table of Contents
^^^^^^^^^^^^^^^^^
- Section A.I: Compound Words
- Section A.II: Delimiter Count Function
- Section A.III: Palindromic Pairs
- Section A.IV: Categories

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

Section II: Delimiter Count Function 
====================================

.. note::

    It is the author's opinion there is a type of *algebraic structure* embedded in Language through the constraints of syntax. This section highlights one of the functions defined within this structure. While the function is not required to prove the main results of this work about palindromes, it is an interesting function in its own right.

Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a palindrome is distributed through its syntactical layers. The concepts of *Perfect* and *Imperfect* palindromes are be defined more rigorously in  Section III, but as an intuitive introduction to the ability of a palindrome to encode meaning on multiple syntactic levels and as a justification for the introduction of the Delimiter Count Function, consider the following two examples,

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

**Example** Consider the string *t = "a b c"*. The Character-level set representation of *t* is given by,
    
    T = { (1, "a"), (2, σ), (3, "b"), (4, σ), (5, "c") }.

The set D:sub:`t` contains the ordered pairs *(2, σ)* and *(4, σ)*, where the first coordinate of each pair correspond the positions of the two Delimiter Characters in the String. Therefore, 
    
    D:sub:`t`= { (2, σ), (4, σ) }

From this it follows, | D:sub:`t` | is 2. Hence, *Δ(s) = 2*. ∎

From the previous example, it can be seen the Delimiter Count function takes a Sentence as input and produces a non-negative integer (the Delimiter count) as output. Multiple sentences can have the same Delimiter count, making it a many-to-one function. While this many not be advantageous from a computational perspective, the Delimiter Count function has other interesting properties that make it worth studying. The following theorems describe some of its properties.

**Theorem A.2.1** ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1

## TODO 
# I think this needs revised to be Λ(ζ) ≥ Δ(ζ) + 1 to account for edges where the sentence has multiple Delimiters in sequence, or has a Delimiter at the end or beginning of the String. 
# This might be resolvable by introducing an assumption about the structure of a Sentence. Perhaps all Delimiters between two consecutive Words should be treated as a single Delimiter?
## TODO

In natural language, this theorem is stated: For any sentence *ζ* in a Corpus C:sub:`L`, the length of the Sentence is equal to its Delimiter count plus one.

Assume *ζ ∈* **C**:sub:`L`. Let *Δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the Character-level representation of ζ. Let **W**:sub:`ζ` be the word-level set representation of ζ. Recall **W**:sub:`ζ` is formed by splitting **Ζ** at each Delimiter Character *σ* with the Delimiting Algorithm in Definition 2.1.3.

Each word in **W**:sub:`ζ` corresponds to a contiguous subsequence of non-Empty, non-Delimiter Characters in **Ζ**.

Since Delimiters separate Words, and each Delimiter corresponds to one Word boundary, the number of Words in the Sentence is always one more than the number of delimiters. Therefore, the cardinality of **W**:sub:`ζ` (the number of words) is equal to the Delimiter count of *Δ(ζ)* plus one,

    | W:sub:`ζ` | = Λ(ζ) = Δ(ζ) + 1. ∎

The next two theorems establish the invariance of the Delimiter count under String Inversion for any String, and by extension, any Sentence.

**Theorem A.3.2** ∀ s ∈ S: Δ(s) = Δ(inv(s))

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

Definition 2.1.2, every Sentence is a String. Therefore, *ζ* is a String. By Theorem 2.4.2, 

    18. Δ(ζ) = Δ(inv(ζ))

Which is what was to be shown. ∎

**Theorem A.2.4** ∀ α ∈ L: Δ(α) = 0

Assume α ∈ L. By the Axiom W.1, if a string *s* belongs to the Language **L**, then it does not contain any Delimiter Characters

    s ∈ L → (∀ i ∈ N:sub:`l(s)`: 𝔞:sub:`i` ≠ σ )

Therefore, *α* does not contain any Delimiter Characters (*σ*). By Definition 2.4.1, *Δ(s)* counts the number of Delimiter Characters (*σ*) in a String *s*. Since *α* contains no Delimiter Characters, the delimiter count of *α* must be 0. Therefore, *Δ(α) = 0*. ∎

**Theorem A.2.5** ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

In natural language, this theorem can be stated as follows: For every Sentence *ζ* in a Corpus C:sub:`L`, the String Length of the Sentence *l(ζ)* is equal to the delimiter count of the sentence *Δ(ζ)* plus the sum of the String Lengths of its Words.

Assume 

    1. ζ ∈ C:sub:`L`. 

Either each *ζ{i}* for *1 ≤ i ≤ l(ζ)* is Delimiter or it is a non-Delimiter, with no overlap. By Definition 2.4.1, the number of Delimiter Characters in *ζ* is Δ(*ζ*). 

By the Discovery Axiom W.1, words in **L** do not contain Delimiters. By Definition 2.1.3, the Words in **W**:sub:`ζ` are obtained by splitting *ζ*  at the Delimiters. Therefore, the total number of non-Delimiter characters in *ζ* is the sum of the Word Lengths l(ζ{i}) which is 

    2. Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Since every Character in *ζ* is either a Delimiter or part of a Word (and not both), the total number of Characters in *ζ* is the sum of the number of Delimiters and the number of Characters in Words. By Definition 1.1.3 of String Length, the total number of non-Empty characters in ζ is *l(ζ)*. Therefore, the number of non-Empty Characters in *ζ* is equal to the number of Delimiters plus the sum of its Word Lengths,

    3. ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ∎

**Theorem A.2.6** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Applying the results of Theorem A.4.1 and Theorem A.4.5, this theorem follows from simple algebraic manipulation. ∎

**Theorem A.2.7** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥  Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α)

Assume *ζ ∈* **C**:sub:`L`. By Theorem 2.2.4,
    
    1. Λ(ζ) ≥ 1

From Theorem A.4.6,

    2. l(ζ) + 1 - Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α) = Λ(ζ)

Combining step 1 and step 2, the theorem is obtained through simple algebraic manipulation,

    l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α) ∎

**Theorem A.2.8** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ)

Let ζ be an arbitrary Sentence in C:sub:`L`.

Let **W**:sub:`ζ`` be the Word-level representation of *ζ*. By Definition 2.1.4, *Λ(ζ) = *| W:sub:`ζ` |, which is the number of Words in *ζ* (Word Length). By Theorem 1.2.3 and the Discovery Axiom W.1, each Word in **W**:sub:`ζ` consists of one or more non-Empty Characters.

Therefore, the total number of non-Empty Characters in *ζ*, *l(ζ)* (String Length), must be greater than or equal to the number of Words in *ζ*, *Λ(ζ)* (Word Length). This can be more formally expressed using Theorem 2.1.1: 

     Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i}) ≥ Λ(ζ)

By Theorem A.4.7, the result is obtained,

    l(ζ) ≥ Λ(ζ).

Therefore, for any Sentence ζ ∈ C:sub:`L`, its String Length is always greater than or equal to its Word Length. ∎

**Theorem A.2.9 (Informal)** ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

Let *u* and *t* be arbitrary strings in S. Let **U** and **T** be the Character-level representations of *u* and *t*, respectively:

    U = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(u)`)

    T = (𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)`)

The Character-level representation of *ut* is:

    UT = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(u)`, 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)``)

By Definition A.4.1, *Δ(u)* is the number of Delimiters in *u*, *Δ(t)* is the number of Delimiters in *t*, and *Δ(ut)* is the number of Delimiters in *ut*.

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

*   ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t) ∎

**Theorem A.2.10** ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)

Let *u* and *t* be arbitrary strings in S.

By Theorem A.4.2,

    1. Δ(s) = Δ(inv(s)).

Therefore, 

    2. Δ(ut) = Δ(inv(ut)).

By Theorem 2.4.9,
 
    3. Δ(ut) = Δ(u) + Δ(t).

Combining steps 2 and 3, it follows, 

    Δ(inv(ut)) = Δ(ut) = Δ(u) + Δ(t)

Since u and t were arbitrary strings, this can be generalized,

    ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t) ∎

**Theorem A.2.11** ∀ ζ ∈ C:sub:`L`: Δ(Ζ ⋅ Σ:sub:`σ`)= 0

Theorem 3.1.15: ∀ s ∈ S: Δ(σ_reduce(s)) = 0

Proof:

Let s be an arbitrary string in S.

Definition of σ-reduction: By Definition 3.1.2, σ_reduce(s) is the string obtained by removing all occurrences of the delimiter character σ from s.

Definition of Delimiter Count: By Definition 2.4.1, Δ(t) is the number of delimiter characters σ in a string t.

Absence of Delimiters: Since σ_reduce(s) has all its delimiters removed, it contains no occurrences of the character σ.

Conclusion: Therefore, the number of delimiters in σ_reduce(s) is 0.

Δ(σ_reduce(s)) = 0
Since s was an arbitrary string in S, we can generalize:

*   ∀ s ∈ S: Δ(σ_reduce(s)) = 0
This completes the proof. ∎


**Theorem A.2.12** ∀ s ∈ S: l(ζ ⋅ Σ:sub:`σ`) + Δ(s) = l(s)

Theorem 3.1.16: ∀ s ∈ S: l(s) = l(σ_reduce(s)) + Δ(s)

Translation: For any string s, the length of s is equal to the length of its σ-reduction plus the number of delimiters in s.

Proof:

Let s be an arbitrary string in S.

Definition of σ-reduction: By Definition 3.1.2, σ_reduce(s) is obtained by removing all delimiter characters (σ) from s.

Definition of Delimiter Count: By Definition 2.4.1, Δ(s) is the number of delimiter characters in s.

Length of s: The length of s, denoted l(s), is the total number of characters in s, including delimiters.

Length of σ_reduce(s): The length of σ_reduce(s), denoted l(σ_reduce(s)), is the number of non-delimiter characters in s.

Key Observation: Every character in s is either a delimiter or a non-delimiter character. Therefore, the total number of characters in s is the sum of the number of non-delimiter characters and the number of delimiter characters.

Conclusion: From steps 3, 4, and 5, we can conclude:

l(s) = l(σ_reduce(s)) + Δ(s)
Since s was an arbitrary string, we can generalize:

*   ∀ s ∈ S: l(s) = l(σ_reduce(s)) + Δ(s)
This completes the proof. ∎

Explanation:

This theorem expresses a fundamental relationship between the length of a string, the length of its σ-reduction, and its delimiter count. It essentially states that the original length of a string can be decomposed into the length of the string without delimiters (the σ-reduction) and the number of delimiters that were removed.


Example:

Let s = "a σ b σ σ c".

l(s) = 7
σ_reduce(s) = "abc"
l(σ_reduce(s)) = 3
Δ(s) = 3
And indeed, l(s) = l(σ_reduce(s)) + Δ(s)  =>  7 = 3 + 4.


**Theorem A 2.13** ∀ ζ ∈ C:sub:`L`: l(ζ ⋅ Σ:sub:`σ`) + Λ(ζ) = l(ζ) + 1

Let ζ be an arbitrary sentence in C:sub:L.

Theorem 3.1.16: We know from Theorem 3.1.16 that for any string s:

l(s) = l(σ_reduce(s)) + Δ(s)
Applying Theorem 3.1.16 to ζ:  Applying this to our sentence ζ, we get:

l(ζ) = l(σ_reduce(ζ)) + Δ(ζ)
Theorem 2.4.1: We also know from Theorem 2.4.1 that for any sentence ζ in the corpus:

Λ(ζ) = Δ(ζ) + 1
Rearranging Theorem 2.4.1: We can rearrange this to get:

Δ(ζ) = Λ(ζ) - 1
Substitution: Substituting the expression for Δ(ζ) from Step 4 into the equation from Step 2, we get:

l(ζ) = l(σ_reduce(ζ)) + (Λ(ζ) - 1)
Rearranging: Rearranging the terms, we get:

l(σ_reduce(ζ)) + Λ(ζ) = l(ζ) + 1
Conclusion: Since ζ was an arbitrary sentence in C:sub:L, we can generalize:

∀ ζ ∈ C:sub:L: l(σ_reduce(ζ)) + Λ(ζ) = l(ζ) + 1
This completes the proof. ∎

Explanation:

The proof combines the relationship between the length of a string and its σ-reduction (Theorem 3.1.16) with the relationship between the number of words in a sentence and its delimiter count (Theorem 2.4.1). By substituting and rearranging, we arrive at the correct equation.

Why the original equation was slightly incorrect:

The original equation, l(ζ): l(σ_reduce(ζ)) + Λ(ζ) = l(ζ) + 1, was incorrect because it added l(ζ) to both sides without proper justification. The correct derivation involves substituting for Δ(ζ) and then rearranging.

Implications:

This corrected theorem establishes a precise relationship between the length of a sentence, the length of its σ-reduction, and the number of words in the sentence. This is another useful tool for analyzing the structure of sentences and, in particular, palindromes.



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
