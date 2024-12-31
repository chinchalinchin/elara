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