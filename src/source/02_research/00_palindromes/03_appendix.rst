Appendix
========

This section contains notes and ideas that do not serve to establish the main results of the work, but the author believes may nevertheless prove useful in extending the formal theory into other epistemological domains.

Table of Contents
^^^^^^^^^^^^^^^^^
- Section A.I: Word Concatenation 
- Section A.II: Compound Words
- Section A.III: Sentence Language
- Section A.IV: Delimiter Count Function
- Section A.V: Palindromic Pairs

Section A.I: Word Concatenation
-------------------------------

.. note::

    Word concatenation is effectively dealt with in the formal system by Defintion 1.2.7 of the Limitation operation. This definition is retained in Appendix I in case it is required to refer to the concatenation of the Character-level representation of Words, i.e. after the effects of the Emptying Algorithm (Definition 1.1.2) have been applied to remove null semantic content, but before the introduction of the Limitation operation.

Concatenation was defined in Definition 1.1.1 in terms of Characters and Strings. Every Word is a String and every String has a Character-level set representation, so the operation of concatenation will not be materially altered to accomodate Words. However, as the analysis builds toward soldifying a theory of palindromes, the result of this essential operation will be given a slightly different formal representation. This representation will not change the operation in any way, but will instead enable a more descriptive theory to emerge when the concept of a Pairing Language is introduced.

Let *α* and *β* be two words with the following Character level set representations:

    Α = { (1,  𝔞:sub:`1`), (2,  𝔞:sub:`2`), ... , (l(α),  𝔞:sub:`l(α)`) }

    Β = { (1, 𝔟:sub:`1``), (2, 𝔟:sub:`2`), ... , (l(β), 𝔟:sub:`l(β)`)}

By Definition 1.1.1, the concatenation of *α* and *β*, denoted by *αβ*, is the String *t* formed by appending the characters of *β* to the end of *α*. Formally, the set representation of *t* is given by,

    T = { (1, 𝔞:sub:`i`), (2,  𝔞:sub:`2`), ..., (l(α),  𝔞:sub:`l(α)`), (l(α) + 1, 𝔟:sub:`1`), (l(α) + 2, 𝔟:sub:`2`), ..., (l(α) + l(β), 𝔟:sub:`l(β)`)}

Note *t* is not necessarily a Word in the Language. 

Section A.II: Compound Words 
----------------------------

.. note::

    Part of the ambiguity in imperfect palindromes is that multiple different palindromes can map to the same σ-reduced form. When Delimiters are removed from a Sentence, a certain class of Words can remain in the Language, because their semantic content *"transmutes"*. In the author's opinion, the class of Compound Words bears some relation to palindromic structures, but the exact relation has yet to be uncovered.

**Definition A.2.1: Compound Words** η ∈ CW:sub:`L` ↔ [(∃ α, β ∈ L: η = αβ)  ∨  (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ)] ∧ (η ∈ L)

This formalization can be translated into natural language as follows: A Word *η* in a Language **L** is a Compound Word if and only if,

    1. Base Case (*∃ α, β ∈ L: η = αβ*) ∧ (η ∈ L):  *η* can be formed by concatenating two words from **L**, and *η* belongs to **L**.
    2. Recursive Step [ (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ) ∧ (η ∈ L) ]: *η* can be formed by concatenating a word from **L** with a Compound Word from **L**, and *η* belongs to **L**. ∎

The constraint *w ∈* **L** ensures that the concatenated String *η* is not just a String, but also a valid Word within the Language **L**.

**Examples**

*"teapot"* is a Compound Word because it can be formed by concatenating *"tea"* and *"pot"*, and *"racecar"* is itself a word in English.

*"nevertheless"* is a Compound Word formed from *"never"*, *"the"*, and *"less"*

*"formrat"* is not a Compound Word, even though it can be formed by concatenating Words from the Language, i.e. *"form"* and *"rat"* are both valid words, the concatenation *"formrat"* is not a valid Word in English.

**Definition A.2.2: Compound Invertible Words** η ∈ CIW:sub:`L`  ↔ [ (η ∈ CW:sub:`L`)  ∧ (η ∈ I) ]

In natural language: A word η in a language **L** is a Compound Invertible Word if and only if it is both a Compound Word and an Invertible Word. Using notation for set intersections, this definition can be revised to read,

    CIW:sub:`L` = CW:sub:`L` ∩ I ∎

**Example**

"racecar" is a compound invertible word because it's both a compound word and its own inverse.

Section A.III: Sentence Language
--------------------------------

**Definition A.3.1: Sentence Language**

A Sentence Language is defined as the set of unique Words which are contained in a Sentence *ζ*. **L**:sub:`ζ` denotes a Sentence Language.  

   α ∈ L:sub:`ζ` ↔ ∃ i ∈ N:sub:`Λ(ζ)`: α[i] ∈ W:sub:`ζ` ∎

**Theorem A.3.1** ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L

This theorem can be stated in natural language as follows: For any Sentence *ζ* in a Corpus **C**:sub:`L`, its Sentence Language is a subset of the Language **L**.

Assume *ζ ∈* **C**:sub:`L`. W:sub:`ζ` be the Word-level set representation of *ζ*, as specified in Definition 2.1.3. By Axiom S.3, every Word *α* in the Word-level set representation of *ζ* belongs to the Language **L**. Since every ordered element of W:sub:`ζ` that belongs to **L** also belongs to L:sub:`ζ` by Definition 2.3.3, it can concluded that L:sub:`ζ` is a subset of **L**. The only assumption on *ζ* is that is belongs to the Corpus, therefore this conclusion can be generalized to all Sentences in a Corpus,

    ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L 

In other words, every Sentence Language from a Corpus is a subset of the Language **L**. ∎


Section IV: Delimiter Count Function 
====================================

.. note::

    It is the author's opinion there is a type of *algebraic structure* embedded in Language through the constraints of syntax. This section highlights one of the functions defined within this structure. While the function is not required to prove the main results of this work about palindromes, it is an interesting function in its own right.

The study of Delimiter Characters in a Sentence bears study beyond its application to palindromic structures. The following section of the Appendix introduces a function for quantifying the number of Delimiters in a sentence. Various properties about this function are then proved, in particular how the function interacts with other linguistic operations and functions that have been defined in the main body of the work. 

Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.

**Definition A.4.1: Delimiter Count Function** Let *t* be a String with length *l(t)*. Let **T** be the Character-level representation of *t* with the Characters *𝔞*:sub:`i` denoting the *i*:sup:`th` character of the String *t*, where *1 ≤ i ≤ l(t)*,

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

**Theorem A.4.1** ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1

(TODO: I think this needs revised to be Λ(ζ) ≥ Δ(ζ) + 1 to account for edges where the sentence has multiple Delimiters in sequence, or has a Delimiter at the end or beginning of the String. 

This might be resolvable by introducing an assumption about the structure of a Sentence. Perhaps all Delimiters between two consecutive Words should be treated as a single Delimiter?)

In natural language, this theorem is stated: For any sentence *ζ* in a Corpus C:sub:`L`, the length of the Sentence is equal to its Delimiter count plus one.

Assume *ζ ∈* **C**:sub:`L`. Let *Δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the Character-level representation of ζ. Let **W**:sub:`ζ` be the word-level set representation of ζ. Recall **W**:sub:`ζ` is formed by splitting **Ζ** at each Delimiter Character *σ* with the Delimiting Algorithm in Definition 2.1.3.

Each word in **W**:sub:`ζ` corresponds to a contiguous subsequence of non-Empty, non-Delimiter Characters in **Ζ**.

Since Delimiters separate Words, and each Delimiter corresponds to one Word boundary, the number of Words in the Sentence is always one more than the number of delimiters. Therefore, the cardinality of **W**:sub:`ζ` (the number of words) is equal to the Delimiter count of *Δ(ζ)* plus one,

    | W:sub:`ζ` | = Λ(ζ) = Δ(ζ) + 1. ∎

The next two theorems establish the invariance of the Delimiter count under String Inversion for any String, and by extension, any Sentence.

**Theorem A.4.2** ∀ s ∈ S: Δ(s) = Δ(inv(s))

Let *t* be a string with length *l(t)*. Let *u = inv(t)*. By Definition 1.2.4,

    1. l(t) = l(u)
    2. ∀ i ∈ N:sub:`l(t)`: u[i] = t[l(t) - i + 1]

Let **D**:sub:`t` be the set of ordered pairs representing the positions of the Delimiter *σ* in *t*, and let **D**:sub:`u` be the corresponding set for *u*. Assume *(j, σ) ∈*  **D**:sub:`u`, then, by step 2,

    3. u[j] = t[l(t) - j  + 1]

This means that the Character at position *j* in the inverse string *t* is the Delimiter *σ*. Therefore, 

    4. (l(t) - j  + 1, σ) ∈* **D**:sub:`t`

Thus, it is shown that for every element *(j, σ) ∈*  **D**:sub:`u`, there exists a corresponding element *(i, σ) ∈* **D**:sub:`t`, where *i = l(t) - j + 1*. 

To make the mapping more explicit, define a function *f*: **D**:sub:`t` *→* **D**:sub:`u` as follows. For any (*i*, *σ*) ∈ **D**:sub:`t`, let 

    f((i, σ)) = (l(t) - i + 1, σ)
    
It will be shown that *f* is a bijection.

**Well Defined** If (*i*, *σ*) ∈ **D**:sub:`t`, then the Character at position *i* in *t* is *σ*. By step 2, the Character at position *l(t) - i + 1* in *u = inv(t)* is also *σ*. Therefore, 

    (l(t) - i + 1, σ) ∈ D:sub:`u`
    
In other words, *f* maps elements of **D**:sub:`t` to elements of **D**:sub:`u`. Thus, *f* is well defined.
 
**Injective** Suppose 

    f((i:sub:`1`, σ)) = f((i:sub:`2`, σ)). 
    
Then, it follows,

    (l(t) - i:sub:`1` + 1, σ) = (l(t) - i:sub:`2` + 1, σ). 
    
This in turn implies, 

    l(t) - i:sub:`1` + 1 = l(t) - i:sub:`2` + 1, 
    
So 
    i:sub:`1` = i:sub:`2`
    
Thus, 

    (i:sub:`1`, σ) = (i:sub:`2`, σ)
    
In other words, *f* is injective. 

**Surjective** Let *(j, σ)* be an arbitrary element of D:sub:`u`. Then the Character at position *j* in *u* is *σ*. Let 

    i = l(t) - j + 1. 
    
Then 

    j = l(t) - i + 1. 
    
By step 3, the Character at position *i* in *t* is also *σ*. So, 

    (i, σ) ∈ D:sub:t
    
And,

    f((i, σ)) = (l(t) - i + 1, σ) = (j, σ). 
    
Thus, *f* is surjective. 

This defines a bijective mapping between the elements of **D**:sub:`u` and **D**:sub:`t`. Since there's a one-to-one mapping between the elements of *D**:sub:`u` and **D**:sub:`t`, their cardinalities must be equal,

    1. | D:sub:`u` | = | D:sub:`s` |

By the definition of the delimiter count function, this means *Δ(u) = Δ(t)*. Since *u = inv(t)*, it has been shown *Δ(inv(s)) = Δ(s)*. 

Furthmore, an exact relationship has been estalished between the coordinates of Delimiters in Strings and their Inverses, 

    D:sub:`inv(t)` = { (l(t) - i + 1, σ) | (i, σ) ∈ D:sub:`t` } ∎

**Theorem A.4.3** ∀ ζ ∈ C:sub:`L`: Δ(ζ) = Δ(inv(ζ))

Definition 2.1.2, every Sentence is a String. Therefore, *ζ* is a String. By Theorem 2.4.2, 

    Δ(ζ) = Δ(inv(ζ))

Which is what was to be shown. ∎

**Theorem A.4.4** ∀ α ∈ L: Δ(α) = 0

Assume α ∈ L. By the Axiom W.1, if a string *s* belongs to the Language **L**, then it does not contain any Delimiter Characters

    s ∈ L → (∀ i ∈ N:sub:`l(s)`: 𝔞:sub:`i` ≠ σ )

Therefore, *α* does not contain any Delimiter Characters (*σ*). By Definition 2.4.1, *Δ(s)* counts the number of Delimiter Characters (*σ*) in a String *s*. Since *α* contains no Delimiter Characters, the delimiter count of *α* must be 0. Therefore, *Δ(α) = 0*. ∎

Theorem 2.4.5:

The proof is correct, but the explanation in the second paragraph could be improved. Instead of saying "Either each ⲁ:sub:i... is a Delimiter or it is a non-Delimiter," it would be clearer to say "Each character in Z is either a delimiter or part of a word in W:sub:ζ."
Revised Theorem 2.4.5 proof:

Assume ζ ∈ C:sub:L. Let Ζ be the Character-level representation of ζ,

1. **Z** = { (1, ⲁ:sub:`1`), (2, ⲁ:sub:`2`), ..., (l(ζ), ⲁ:sub:`l(ζ)`) }
Each character in Z is either a delimiter or part of a word in W:sub:ζ.

By Definition 2.4.1, the number of Delimiter Characters in ζ is Δ(ζ).

By Axiom W.1 (Discovery Axiom), words in L do not contain Delimiters. By Definition 2.1.3, the words in W:sub:ζ are obtained by splitting ζ  at the Delimiters. Therefore, the total number of non-Delimiter characters in ζ is the sum of the lengths of the words in W*:sub:ζ, which is Σ:sub:(i, α) ∈ W_ζ l(α).

Since every Character in ζ is either a Delimiter or part of a Word (and not both), the total number of Characters in ζ is the sum of the number of delimiters and the number of characters in words. By Definition 1.1.3, the total number of non-Empty characters in ζ is l(ζ). Therefore, the number of non-Empty Characters in ζ is equal to the number of Delimiters plus the sum of the lengths of the words in W*:sub:ζ.

2. ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`(i, α) ∈ W_ζ` l(α) ∎

**Theorem A.4.5** ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

In natural language, this theorem can be stated as follows: For every Sentence *ζ* in a Corpus C:sub:`L`, the String Length of the Sentence *l(ζ)* is equal to the delimiter count of the sentence *Δ(ζ)* plus the sum of the String Lengths of its Words.

Assume 

    1. ζ ∈ C:sub:`L`. 

Either each *ζ{i}* for *1 ≤ i ≤ l(ζ)* is Delimiter or it is a non-Delimiter, with no overlap. By Definition 2.4.1, the number of Delimiter Characters in *ζ* is Δ(*ζ*). 

By the Discovery Axiom W.1, words in **L** do not contain Delimiters. By Definition 2.1.3, the Words in **W**:sub:`ζ` are obtained by splitting *ζ*  at the Delimiters. Therefore, the total number of non-Delimiter characters in *ζ* is the sum of the Word Lengths l(ζ{i}) which is 

    2. Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Since every Character in *ζ* is either a Delimiter or part of a Word (and not both), the total number of Characters in *ζ* is the sum of the number of Delimiters and the number of Characters in Words. By Definition 1.1.3 of String Length, the total number of non-Empty characters in ζ is *l(ζ)*. Therefore, the number of non-Empty Characters in *ζ* is equal to the number of Delimiters plus the sum of its Word Lengths,

    3. ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ∎

**Theorem A.4.6** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Applying the results of Theorem A.4.1 and Theorem A.4.5, this theorem follows from simple algebraic manipulation. ∎

**Theorem A.4.7** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥  Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α)

Assume *ζ ∈* **C**:sub:`L`. By Theorem 2.2.4,
    
    1. Λ(ζ) ≥ 1

From Theorem A.4.6,

    2. l(ζ) + 1 - Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α) = Λ(ζ)

Combining step 1 and step 2, the theorem is obtained through simple algebraic manipulation,

    l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α) ∎

**Theorem A.4.8** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ)

Let ζ be an arbitrary Sentence in C:sub:`L`.

Let **W**:sub:`ζ`` be the Word-level representation of *ζ*. By Definition 2.1.4, *Λ(ζ) = *| W:sub:`ζ` |, which is the number of Words in *ζ* (Word Length). By Theorem 1.2.3 and the Discovery Axiom W.1, each Word in **W**:sub:`ζ` consists of one or more non-Empty Characters.

Therefore, the total number of non-Empty Characters in *ζ*, *l(ζ)* (String Length), must be greater than or equal to the number of Words in *ζ*, *Λ(ζ)* (Word Length). This can be more formally expressed using Theorem 2.1.1: 

     Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i}) ≥ Λ(ζ)

By Theorem A.4.7, the result is obtained,

    l(ζ) ≥ Λ(ζ).

Therefore, for any Sentence ζ ∈ C:sub:`L`, its String Length is always greater than or equal to its Word Length. ∎

**Theorem 2.4.9** ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

Theorem 2.4.9: ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

Proof:

Let u and t be arbitrary strings in S.

Character-Level Representations: Let U and T be the character-level representations of u and t, respectively:

U = (ⲁ:sub:1, ⲁ:sub:2, ..., ⲁ:sub:l(u))
T = (𝔟:sub:1, 𝔟:sub:2, ..., 𝔟:sub:l(t))
Concatenation: The character-level representation of ut is:

UT = (ⲁ:sub:1, ⲁ:sub:2, ..., ⲁ:sub:l(u), 𝔟:sub:1, 𝔟:sub:2, ..., 𝔟:sub:l(t))
Delimiter Count: By Definition 2.4.1, Δ(u) is the number of delimiters in u, Δ(t) is the number of delimiters in t, and Δ(ut) is the number of delimiters in ut.

Key Observation: Since concatenation simply joins the two strings, the number of delimiters in ut is the sum of the number of delimiters in u and the number of delimiters in t.

Formal Argument:

Let D:sub:u be the set of indices of delimiters in u.
Let D:sub:t be the set of indices of delimiters in t.
Let D:sub:ut be the set of indices of delimiters in ut.
We can express these sets as:

D:sub:u = { i | 1 ≤ i ≤ l(u) and ⲁ:sub:i = σ }
D:sub:t = { j | 1 ≤ j ≤ l(t) and 𝔟:sub:j = σ }
D:sub:ut = { k | 1 ≤ k ≤ l(u) + l(t) and (k ≤ l(u) and UT[k] = σ) or (k > l(u) and UT[k] = σ) }
It's clear that D:sub:ut is the union of two disjoint sets:

The set of indices of delimiters in u (which is D:sub:u)
The set of indices of delimiters in t, shifted by l(u) (which corresponds to D:sub:t)
Therefore, |D:sub:ut| = |D:sub:u| + |D:sub:t|.

By the definition of the delimiter count function, Δ(u) = |D:sub:u|, Δ(t) = |D:sub:t|, and Δ(ut) = |D:sub:ut|.

Conclusion: Substituting these into the equation from Step 5, we get:

Δ(ut) = Δ(u) + Δ(t)
Since u and t were arbitrary strings, we can generalize:

*   ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)
This completes the proof. ∎

Explanation:

The proof relies on the fact that concatenation simply joins two strings without altering the number of delimiters in either string. Therefore, the total number of delimiters in the concatenated string is the sum of the delimiters in the individual strings.

Implications:

Additivity: This theorem demonstrates that the delimiter count function is additive with respect to concatenation. This is a significant property that further characterizes its behavior.


**Theorem 2.4.10** ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)

Theorem 2.4.10: ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)

Proof:

Let u and t be arbitrary strings in S.

Theorem 2.4.2 (Invariance under Inversion): We know from Theorem 2.4.2 that Δ(s) = Δ(inv(s)) for any string s.

Applying Invariance to ut: Therefore, Δ(ut) = Δ(inv(ut)).

Theorem 2.4.9 (Additivity over Concatenation): We also know from Theorem 2.4.9 that Δ(ut) = Δ(u) + Δ(t).

Substitution: Substituting the result from Step 3 into Step 2, we get:

Δ(inv(ut)) = Δ(ut) = Δ(u) + Δ(t)
Conclusion: Therefore, we have shown that:

Δ(inv(ut)) = Δ(u) + Δ(t)
Since u and t were arbitrary strings, we can generalize:

*   ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)
This completes the proof. ∎

Explanation:

The proof simply combines the two previously established properties:

The delimiter count of a string is the same as the delimiter count of its inverse.
The delimiter count of a concatenation is the sum of the delimiter counts of the individual strings.


Section A.V: Palindromic Pairs
------------------------------

The only constraint on a Language is that it must consist of Words. This is guaranteed by the Extraction Axiom S.2. The only constraint on Words is that they must not contain the Delimiter. This is guaranteed by the Delimiter Axiom W.1. 

Since *σ-reduction* removes the Delimiter Character when it projects a Sentence onto the *σ-reduced* Alphabet, this process can viewed as the construction of another formal Language. In other words, given a Language and Corpus, the operation of *σ-reduction* implies the existence of a second Language which encodes the original Sentences. This second Language loses much of its semantic coherence with respect to its "*mother*" Corpus, but it nevertheless contains semantic information. 

This idea motives the definition of a *σ-Pairing Language*.

**Definition A.5.1: σ-Pairing Language**

The σ-Pairing Language L:sub:`σ` of a Corpus C:sub:`L` is defined as the set of Words *α* that satisfy the following formula, 

    α ∈ L:sub:`σ` ↔ ∃ ζ ∈ C:sub:`L`: α = (ζ ⋅ Σ:sub:`σ`)

This definition captures the idea that the σ-Pairing Language consists of all the Strings that can be generated by applying σ-reduction to the Sentences in the Corpus. It directly links the elements of L:sub:σ to the σ-reduced forms of the Sentences, ensuring that the Pairing Language is derived from the original Corpus.

**Theorem A.5.1** ∀ α ∈ L: α ∈ L:sub:`σ` ↔ [ ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:s α ]

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

**Definition A.5.2: Palindromic Pairing Language**

Definition A.1.4 is altered in the following definition to quantify over the set of Palindromes in a Corpus. The Pairing Language that results is denoted L:sub:`P`. The set of Words *α* which satisfy this definition are referred to as the Palindromic Pairing Language of Language **L**, 

    α ∈ L:sub:`P` ↔  ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)

In particuar, if *α ∈ L*:sub:`P`, *α* is called the *Palindromic Image* of the Sentences *ζ* which generate it.

This definition is used to prove the following theorems.

**Theorem A.5.2** L:sub:`P` ⊂ L:sub:`σ`

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

**Theorem A.5.3**: ∀ α ∈ L:sub:`P`: α = inv(α)

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

**Theorem A.5.4** L ∩ L:sub:`P` ⊆ R

This theorem can be stated in natural language as follows: The intersection of a Language **L** and its Palindromic Pair **L**:sub:`P` is a subset of the Language's Reflective Words **R**.

Assume α ∈ L ∩ L:sub:P: This is a good starting point. It means α is both a Word in the Language and a String in the Palindromic Pairing Language.
Word: You correctly state that since α ∈ L, it is a Word in the Language.
Inverse Exists: You also correctly state that since α ∈ L:sub:P, it must equal its own inverse (α = inv(α)). This follows from Theorem 3.1.9.
Reflective Word: While your conclusion is correct, we need to explicitly connect the properties in steps 2 and 3 to the definition of Reflective Words (Definition 1.3.1).
Refined Proof:

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

**Theorem A.5.5** L:sub:`P` ⊂ R:sub:`L_σ`

This theorem can be state in natural language as follows: Given a Language L, all words in its Palindromic Pairing Language are also Reflective Words in the σ-Pairing Language. 

In other show this theorem, it must be shown,

    1. ∀ α ∈ L: α ∈ L:sub:`P` → α ∈ R:sub:`L_σ`

Since by Definition 1.3.1, 

    2. α ∈ R:sub:`L_σ` ↔ inv(α) = α

If it can be shown,

    3. α ∈ L:sub:`P` → inv(α) = α

Then the theorem will follow tautologically from the laws of deduction. But step 3 is exactly Theorem 3.1.9. Therefore, the proof is complete. ∎