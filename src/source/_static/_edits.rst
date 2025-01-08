Removed: Word Concatenation
---------------------------

.. note::

    Word concatenation is effectively dealt with in the formal system by Defintion 1.2.7 of the Limitation operation. This definition is retained in Appendix I in case it is required, before the introduction of the Limitation operation, to refer to the concatenation of the Character-level representation of Words, i.e. after the effects of the Emptying Algorithm (Definition 1.1.2) have been applied to remove null semantic content.

Concatenation was defined in Definition 1.1.1 in terms of Characters and Strings. Every Word is a String and every String has a Character-level set representation, so the operation of concatenation will not be materially altered to accomodate Words. However, as the analysis builds toward soldifying a theory of palindromes, the result of this essential operation will be given a slightly different formal representation. This representation will not change the operation in any way, but will instead enable a more descriptive theory to emerge when the concept of a Pairing Language is introduced.

**Definition A.1.1: Word Concatenation**

Let *α* and *β* be two words with the following Character level set representations:

    Α = { (1,  𝔞:sub:`1`), (2,  𝔞:sub:`2`), ... , (l(α),  𝔞:sub:`l(α)`) }

    Β = { (1, 𝔟:sub:`1``), (2, 𝔟:sub:`2`), ... , (l(β), 𝔟:sub:`l(β)`)}

By Definition 1.1.1, the concatenation of *α* and *β*, denoted by *αβ*, is the String *t* formed by appending the characters of *β* to the end of *α*. Formally, the set representation of *t* is given by,

    T = { (1, 𝔞:sub:`i`), (2,  𝔞:sub:`2`), ..., (l(α),  𝔞:sub:`l(α)`), (l(α) + 1, 𝔟:sub:`1`), (l(α) + 2, 𝔟:sub:`2`), ..., (l(α) + l(β), 𝔟:sub:`l(β)`)} ∎

Note *t* is not necessarily a Word in the Language. 


Removed: Sentence Language
--------------------------

**Definition A.2.1: Sentence Language**

A Sentence Language is defined as the set of unique Words which are contained in a Sentence *ζ*. **L**:sub:`ζ` denotes a Sentence Language.  

   α ∈ L:sub:`ζ` ↔ ∃ i ∈ N:sub:`Λ(ζ)`: α[i] ∈ W:sub:`ζ` ∎

**Theorem A.3.1** ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L

This theorem can be stated in natural language as follows: For any Sentence *ζ* in a Corpus **C**:sub:`L`, its Sentence Language is a subset of the Language **L**.

Assume *ζ ∈* **C**:sub:`L`. W:sub:`ζ` be the Word-level set representation of *ζ*, as specified in Definition 2.1.3. By Axiom S.3, every Word *α* in the Word-level set representation of *ζ* belongs to the Language **L**. Since every ordered element of W:sub:`ζ` that belongs to **L** also belongs to L:sub:`ζ` by Definition 2.3.3, it can concluded that L:sub:`ζ` is a subset of **L**. The only assumption on *ζ* is that is belongs to the Corpus, therefore this conclusion can be generalized to all Sentences in a Corpus,

    ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L 

In other words, every Sentence Language from a Corpus is a subset of the Language **L**. ∎


Removed: Right Partial Sentence
-------------------------------

.. note::
    
    This was the original definition of Right Partial Sentence, where the index was measured from the right-hand side, to highlight the symmetry of palindromic pivots. It is retained here in case there is a reason for switching back to this form of the definition.

**Definition 3.1.7: Right Partial Sentence**

Let ζ be a Sentence in C:sub:`L` with Character-level representation **Z**,

    Z = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(ζ)`)

Let *n* be a fixed natural number such that *0 ≤ n ≤ l(ζ)*. A Right Partial Sentence of *ζ* of String Length *n*, denoted ζ[n:], is defined as the string:

    ζ[n:] = (ⲁ:sub:`l(ζ)-n+1`, ⲁ:sub:`l(ζ)-n+2`, ..., ⲁ:sub:`l(ζ)`)

When *n = 0*, *ζ[0:]* is defined as the empty string, *ε*.

When *n = l(ζ)*, *ζ[n:]* is the entire sentence ζ. ∎


Removed: Associativity of Limitations
-------------------------------------

**Theorem 1.2.9** ∀ p ∈ Χ:sub:`L`(n), ∀ q ∈ Χ:sub:`L`(m), ∀ r ∈ Χ:sub:`L`(k): ((Π:sub:`i=1`:sup:`n` p(i))(Π:sub:`i=1`:sup:`m` q(i)))(Π:sub:`i=1`:sup:`k` r(i)) = ((Π:sub:`i=1`:sup:`n` p(i)))((Π:sub:`i=1`:sup:`m` q(i))(Π:sub:`i=1`:sup:`k` r(i)))

Let *p* *∈* **Χ**:sub:`L(n)`, *q* *∈* **Χ**:sub:`L(m)`, and r ∈ **Χ**:sub:`L(k)` be arbitrary Phrases.

By Definition 2.2.4, the Limitation of a Phrase is a String. String concatenation is associative by Definition 1.1.1 and the Character Axiom C.1, meaning for any strings *s*, *t*, and *u*,

    (st)u = s(tu)

Since *Π*:sub:`i=1`:sup:`n` *p(i)*, *Π*:sub:`i=1`:sup:`m` *q(i)*, and *Π*:sub:`i=1`:sup:`k` *r(i)* are all Strings, the associativity of String Concatenation can by applied to conclude,

    ∀ p ∈ Χ:sub:`L`(n), ∀ q ∈ Χ:sub:`L`(m), ∀ r ∈ Χ:sub:`L`(k): ((Π:sub:`i=1`:sup:`n` p(i))(Π:sub:`i=1`:sup:`m` q(i)))(Π:sub:`i=1`:sup:`k` r(i)) = ((Π:sub:`i=1`:sup:`n` p(i)))((Π:sub:`i=1`:sup:`m` q(i))(Π:sub:`i=1`:sup:`k` r(i))) ∎

Removed: Symmetry of Delimiters
-------------------------------

**Theorem 3.3.1** ∀ ζ ∈ PP: ∃ i ∈ N:sub:`l(ζ)`: ζ[i] = σ ↔ ζ[l(ζ)- i + 1] = σ 

This theorem can be stated in natural language as follows: For every Perfect Palindrome ζ in the Corpus, every Delimiter at index *i* must have a corresponding Delimiter at index *l(ζ) - i + 1*.

Let *ζ* be an arbitrary Sentence in the Corpus such that,

    1. ζ ∈ PP 
   
From step 1 and Definition 3.2.2,

    2. ζ = inv(ζ).

From step 2 and the Definition 1.2.4, it is follows,

    3. ζ[i] = ζ[l(ζ) - i + 1]

Assume there exists an *i* (1 ≤ i ≤ l(ζ)) such that,

    5. ζ[i] = σ

From step 3 and step 4, it immediately follows, 

    6. ζ[l(ζ) - i + 1] = σ

Conversely, if 

    7. ζ[l(ζ) - i + 1] = σ

Then by step 3, it immediately follows,

    8. ζ[i] = σ.

This can be generalized as follows,

    9. ∀ ζ ∈ PP: ∃ i ∈ N:sub:`l(ζ)`: ζ[i] = σ ↔ ζ[l(ζ)-i+1] = σ ∎

It now shown for every Perfect Palindrome, the inverse of Each word is mirrored by the inverse of the corresponding Word at the opposite end of the Sentence. This property is a direct consequence of the fact that Perfect Palindromes are a subset of Invertible Sentences.

Removed: String Variables
-------------------------

It will also be necessary to refer to indeterminate Strings, so notation is also introduced for String Variables,

    2. String Variable ( *x*, *y*, *z*): The lowercase English letters *x*, *y* and *z* denote an indeterminte String. 

Removed: Intervention Theorem
-----------------------------

.. _theorem_2_1_4:

**Theorem 2.1.4** ∀ ζ ∈ C:sub:`L`: ∀ i, j, k ∈ N:sub:`Λ(ζ)`: ∃ n, m ∈ N:sub:`l(ζ)`: (((i/n/j):sub:`ζ`) ∧ ((j/m/k):sub:`ζ`)) → (n < m)

TODO

Removed: Markdown Tables
------------------------

|  k    |  ᚠ[k] |  l(ᚠ[:k]) | l(ᚠ[k:]) |  Δ(ᚠ[k]) | Ω:sub:`-`(ᚠ ,k) | Ω:sub:`+`(ᚠ ,k) |
| ----- | ----- | --------- | -------- | -------- | --------------- | --------------- |
|  1    |  "l"  |  1        |  9       |  0       |  0              | 0               |
|  2    |  "i"  |  2        |  8       |  0       |  0              | 0               |
|  3    |  "v"  |  3        |  7       |  0       |  0              | 0               |
|  4    |  "e"  |  4        |  6       |  0       |  0              | 0               |
|  5    |  " "  |  5        |  5       |  1       |  (5/9)          | (5/9)           |
|  6    |  "e"  |  6        |  4       |  0       |  (5/9)          | (5/9)           |
|  7    |  "v"  |  7        |  3       |  0       |  (5/9)          | (5/9)           |
|  8    |  "i"  |  8        |  2       |  0       |  (5/9)          | (5/9)           |
|  9    |  "l"  |  9        |  1       |  0       |  (5/9)          | (5/9)           |

|  k    |  ᚠ[k] |  l(ᚠ[:k]) | l(ᚠ[k:]) |  Δ(ᚠ[k]) | Ω:sub:`-`(ᚠ ,k) | Ω:sub:`+`(ᚠ ,k) |
| ----- | ----- | --------- | -------- | -------- | --------------- | --------------- |
|  1    |  "w"  |  1        |  17      |  0       |  0              |  0              |
|  2    |  "e"  |  2        |  16      |  0       |  0              |  0              |
|  3    |  " "  |  3        |  15      |  1       |  (3/17)         |  (15/17)        |
|  4    |  "p"  |  4        |  14      |  0       |  (3/17)         |  (15/17)        |
|  5    |  "a"  |  5        |  13      |  0       |  (3/17)         |  (15/17)        |
|  6    |  "n"  |  6        |  12      |  0       |  (3/17)         |  (15/17)        |
|  7    |  "i"  |  7        |  11      |  0       |  (3/17)         |  (15/17)        |
|  8    |  "c"  |  8        |  10      |  0       |  (3/17)         |  (15/17)        |
|  9    |  " "  |  9        |  9       |  1       |  (12/17)        |  (24/17)        |
|  10   |  "i"  |  19       |  8       |  0       |  (12/17)        |  (24/17)        |
|  11   |  "n"  |  11       |  7       |  0       |  (12/17)        |  (24/17)        |
|  12   |  " "  |  12       |  6       |  1       |  (24/17)        |  (30/17)        |
|  13   |  "a"  |  13       |  5       |  0       |  (24/17)        |  (30/17)        |
|  14   |  " "  |  14       |  4       |  1       |  (38/17)        |  (34/17)        |
|  15   |  "p"  |  15       |  3       |  0       |  (38/17)        |  (34/17)        |
|  16   |  "e"  |  16       |  2       |  0       |  (38/17)        |  (34/17)        |
|  17   |  "w"  |  17       |  1       |  0       |  (38/17)        |  (34/17)        |

|  k    |  ᚠ[k] |  l(ᚠ[:k]) | l(ᚠ[k:]) |  Δ(ᚠ[k]) | Ω:sub:`-`(ᚠ ,k) | Ω:sub:`+`(ᚠ ,k) |
| ----- | ----- | --------- | -------- | -------- | --------------- | --------------- |
|  1    |  "d"  |  1        |  26      |  0       |  0              |  0              |
|  2    |  "r"  |  2        |  25      |  0       |  0              |  0              |
|  3    |  "a"  |  3        |  24      |  0       |  0              |  0              |
|  4    |  "w"  |  4        |  23      |  0       |  0              |  0              |
|  5    |  " "  |  5        |  22      |  1       |  (5/26)         |  (22/26)        |
|  6    |  "n"  |  6        |  21      |  0       |  (5/26)         |  (22/26)        |
|  7    |  "o"  |  7        |  20      |  0       |  (5/26)         |  (22/26)        |
|  8    |  " "  |  8        |  19      |  1       |  (13/26)        |  (41/26)        |
|  9    |  "d"  |  9        |  18      |  0       |  (13/26)        |  (41/26)        |
|  10   |  "r"  |  19       |  17      |  0       |  (13/26)        |  (41/26)        |
|  11   |  "a"  |  11       |  16      |  0       |  (13/26)        |  (41/26)        |
|  12   |  "y"  |  12       |  15      |  0       |  (13/26)        |  (41/26)        |
|  13   |  " "  |  13       |  14      |  1       |  (26/26)        |  (55/26)        |
|  14   |  "a"  |  14       |  13      |  0       |  (26/26)        |  (55/26)        |
|  15   |  " "  |  15       |  12      |  1       |  (41/26)        |  (67/26)        |
|  16   |  "y"  |  16       |  11      |  0       |  (41/26)        |  (67/26)        |
|  17   |  "a"  |  17       |  10      |  0       |  (41/26)        |  (67/26)        |
|  18   |  "r"  |  18       |  9       |  0       |  (41/26)        |  (67/26)        |
|  19   |  "d"  |  19       |  8       |  0       |  (41/26)        |  (67/26)        |
|  20   |  " "  |  20       |  7       |  1       |  (61/26)        |  (74/26)        |
|  21   |  "o"  |  21       |  6       |  0       |  (61/26)        |  (74/26)        |
|  22   |  "n"  |  22       |  5       |  0       |  (61/26)        |  (74/26)        |
|  23   |  "w"  |  23       |  4       |  0       |  (61/26)        |  (74/26)        |
|  24   |  "a"  |  24       |  3       |  0       |  (61/26)        |  (74/26)        |
|  25   |  "r"  |  25       |  2       |  0       |  (61/26)        |  (74/26)        |
|  26   |  "d"  |  26       |  1       |  0       |  (61/26)        |  (74/26)        | 

|  k  |  ᚠ[k] |  inv(ᚠ)[k] | l(ᚠ[:k])  | l(ᚠ[k:]) |  Δ(ᚠ[k]) | Δ(inv(ᚠ)[k]) | Ω:sub:`-`(ᚠ ,k) | Ω:sub:`+`(ᚠ ,k) | Δ(ᚠ[:k]) | Δ(inv(ᚠ)[:k]) | Ω:sub:`-`(inv(ᚠ) , k) | Ω:sub:`+`(inv(ᚠ) , k) |
| --- | ----- | ---------  | --------- | -------- | -------- | ------------ | --------------- | --------------- | -------- | ------------- | --------------------- | --------------------- |
|  1  |  "d"  |    "d"     |  1        |  26      |  0       |  0           |  0              |  0              | 0        | 0             |  0                    |  0                    |
|  2  |  "r"  |    "r"     |  2        |  25      |  0       |  0           |  0              |  0              | 0        | 0             |  0                    |  0                    |
|  3  |  "a"  |    "a"     |  3        |  24      |  0       |  0           |  0              |  0              | 0        | 0             |  0                    |  0                    |
|  4  |  "w"  |    "w"     |  4        |  23      |  0       |  0           |  0              |  0              | 0        | 0             |  0                    |  0                    | 
|  5  |  " "  |    "n"     |  5        |  22      |  1       |  0           |  (5/26)         |  (22/26)        | 1        | 0             |  0                    |  0                    | 
|  6  |  "n"  |    "o"     |  6        |  21      |  0       |  0           |  (5/26)         |  (22/26)        | 1        | 0             |  0                    |  0                    |
|  7  |  "o"  |    " "     |  7        |  20      |  0       |  1           |  (5/26)         |  (22/26)        | 1        | 1             |  (7/26)               |  (20/26)              |
|  8  |  " "  |    "d"     |  8        |  19      |  1       |  0           |  (13/26)        |  (41/26)        | 2        | 1             |  (7/26)               |  (20/26)              |
|  9  |  "d"  |    "r"     |  9        |  18      |  0       |  0           |  (13/26)        |  (41/26)        | 2        | 1             |  (7/26)               |  (20/26)              |
|  10 |  "r"  |    "a"     |  10       |  17      |  0       |  0           |  (13/26)        |  (41/26)        | 2        | 1             |  (7/26)               |  (20/26)              |
|  11 |  "a"  |    "y"     |  11       |  16      |  0       |  0           |  (13/26)        |  (41/26)        | 2        | 1             |  (7/26)               |  (20/26)              |
|  12 |  "y"  |    " "     |  12       |  15      |  0       |  1           |  (13/26)        |  (41/26)        | 2        | 2             |  (19/26)              |  (32/26)              |
|  13 |  " "  |    "a"     |  13       |  14      |  1       |  0           |  (26/26)        |  (55/26)        | 3        | 2             |  (19/26)              |  (32/26)              |
|  14 |  "a"  |    " "     |  14       |  13      |  0       |  1           |  (26/26)        |  (55/26)        | 3        | 3             |  (33/26)              |  (46/26)              |
|  15 |  " "  |    "y"     |  15       |  12      |  1       |  0           |  (41/26)        |  (67/26)        | 4        | 3             |  (33/26)              |  (46/26)              |
|  16 |  "y"  |    "a"     |  16       |  11      |  0       |  0           |  (41/26)        |  (67/26)        | 4        | 3             |  (33/26)              |  (46/26)              |
|  17 |  "a"  |    "r"     |  17       |  10      |  0       |  0           |  (41/26)        |  (67/26)        | 4        | 3             |  (33/26)              |  (46/26)              | 
|  18 |  "r"  |    "d"     |  18       |  9       |  0       |  0           |  (41/26)        |  (67/26)        | 4        | 3             |  (33/26)              |  (46/26)              | 
|  19 |  "d"  |    " "     |  19       |  8       |  0       |  1           |  (41/26)        |  (67/26)        | 4        | 4             |  (52/26)              |  (54/26)              |
|  20 |  " "  |    "o"     |  20       |  7       |  1       |  0           |  (61/26)        |  (74/26)        | 5        | 4             |  (52/26)              |  (54/26)              |
|  21 |  "o"  |    "n"     |  21       |  6       |  0       |  0           |  (61/26)        |  (74/26)        | 5        | 4             |  (52/26)              |  (54/26)              |
|  22 |  "n"  |    " "     |  22       |  5       |  0       |  1           |  (61/26)        |  (74/26)        | 5        | 5             |  (74/26)              |  (59/26)              |
|  23 |  "w"  |    "w"     |  23       |  4       |  0       |  0           |  (61/26)        |  (74/26)        | 5        | 5             |  (74/26)              |  (59/26)              |
|  24 |  "a"  |    "a"     |  24       |  3       |  0       |  0           |  (61/26)        |  (74/26)        | 5        | 5             |  (74/26)              |  (59/26)              |
|  25 |  "r"  |    "r"     |  25       |  2       |  0       |  0           |  (61/26)        |  (74/26)        | 5        | 5             |  (74/26)              |  (59/26)              |
|  26 |  "d"  |    "d"     | 26        |  1       |  0       |  0           |  (61/26)        |  (74/26)        | 5        | 5             |  (74/26)              |  (59/26)              |

