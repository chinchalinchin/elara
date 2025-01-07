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

