======================
Palindromic Structures
======================

Table of Contents
=================

Glossary
========

Notation 
--------

- Punctuation: ∎
- Logical Operations: ∀, ∃, ↔, →, ←. ∧, ∨
- Arithmetical Relations: ≠, =, ≥, ≤, +, -
- Sets: ∅, ℕ, N:sub:`i`
- Set Operations: ∪, ∩
- Set Relations: ∈, ∉, ⊆
- Strings: s, t, u
- Domain: S
- Alphabet: Σ
- Characters: 𝔞, 𝔟, 𝔠, ... , σ, ε
- Character Variables: ⲁ, ⲃ, ⲅ
- Language: L
- Words: a, b, c
- Word Variables: α, β, γ
- Character Index Notation: t[i]
- Word Classes: R, I
- Phrases of Word Length n: P:sub:`n`
- Lexicons: X:sub:`L`(n)
- Phrases Variables: p, q, r
- Sentences: ᚠ, ᚢ, ᚦ
- Sentence Variables: ζ, ξ
- Word Index Notation: ζ{i}
- Partial Sentence: ζ[:i], ζ[i:]
- Pivots: ω(ζ)
- Pivot Words: ζ{ω-}, ζ{ω+}
- Sentence Classes: A(n), K, P, PP, IP, P:sup:`-`, P:sup:`+`
- Categories: C:sub:`L`(m)
- Relations: ⊂:sub:`s`, (i/n/j):sub:`ζ`
- Functions: l(t), Λ(t), Δ(t)
- Operations: inv(s), ς(ζ), DΠ:sub:`i=1`:sup:`n` p(i), LΠ:sub:`i=1`:sup:`n` p(i)

Definitions 
-----------

- D 1.1.1: Concatenation: ut
- D 1.1.2: Character-Level Set Representation: **T**
- D 1.1.3: String Length: l(t)
- D 1.1.4: String Equality: u = t
- D 1.1.5: Character Index Notation: t[i]
- D 1.1.6: Consecutive Functions: f(i)
- D 1.1.7: Containment: u ⊂:sub:`s`
- D 1.2.1: Language: L
- D 1.2.2: Word: α
- D 1.2.3: Word Equality: α = β
- D 1.2.4: String Inversion: inv(s)
- D 1.2.5: Phrase: P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`) = (P:sub:`n`(1), )
- D 1.2.6: Lexicon: Χ:sub:`L`(n) = { P:sub:`n` | P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`) ∧ ∀ i ∈ N:sub:`n`: α:sub:`i` ∈ L } 
- D 1.2.7: Delimitation: DΠ:sub:`i=1`:sup:`n` p(i)
- D 1.2.8: Limitation: LΠ:sub:`i=1`:sup:`n` p(i)
- D 1.3.1: Reflective Words: α ∈ R ↔ ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1] 
- D 1.3.2: Invertible Words: α ∈ I ↔ inv(α) ∈ L
- D 2.1.1: Corpus: C:sub:`L`
- D 2.1.2: Sentence: ᚠ
- D 2.1.3: Word-Level Set Representation: W:sub:`ᚠ`
- D 2.1.4: Word Length: Λ(ζ)
- D 2.1.5: Word Index Notation: ζ{i}
- D 2.1.6: Intervention: (i/n/j):sub:`ζ`
- D 2.2.1: Semantic Coherence
- D 2.3.1: Admissible Sentences: t ∈ A(n) ↔ (∃ p ∈ Χ:sub:`L`(n): t = Π:sub:`i=1`:sup:`n` p(i)) ∧ (t ∈ C:sub:`L`)
- D 2.3.2: Invertible Sentences: ζ ∈ K ↔ inv(ζ) ∈ C:sub:`L`
- D 3.1.1: σ-Reduced Alphabet: Σ:sub:`σ` 
- D 3.1.2: σ-Reduction: ς(ζ)
- D 3.2.1: Palindromes: ζ ∈ P ↔ (ς(ζ) = inv(ς(ζ))) 
- D 3.2.2: Perfect Palindromes: ζ ∈ PP ↔ ζ = inv(ζ)
- D 3.2.3: Imperfect Palindromes: ζ ∈ P - PP
- D 3.2.4: Aspect
- D 3.2.5: Left Partial Sentence: Z[:n]
- D 3.2.6: Right Partial Sentence: Z[n:]
- D 3.2.7: Pivots: ω(ζ)
- D 3.2.8: Even Palindromes: ζ ∈ P:sup:`+` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k )] 
- D 3.2.9: Odd Palindromes: ζ ∈ P:sup:`-` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k + 1) ]
- D 3.2.10: Parity
- D 3.2.11: Pivot Words
- D A.1.1: Compound Words: η ∈ CW:sub:`L` ↔ [(∃ α, β ∈ L: η = αβ)  ∨  (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ)] ∧ (η ∈ L)
- D A.1.2: Compound Invertible Words: η ∈ CIW:sub:`L`  ↔ [ (η ∈ CW:sub:`L`)  ∧ (η ∈ I) ]
- D A.2.1: Delimiter Count Function: Δ(t) = | D:sub:`t` |
- D A.3.1: σ-Pairing Language: α ∈ L:sub:`σ` ↔ ∃ ζ ∈ C:sub:`L`: α = (ζ ⋅ Σ:sub:`σ`)
- D A.3.2: Palindromic Pairing Language: α ∈ L:sub:`P` ↔  ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)
- D A.4.1: Category: C:sub:`L`(m)

Algorithms
----------

- A.1: Emptying Algorithm
- A.2: Delimiting Algorithm 
- A.3: Reduction Algorithm

Axioms 
------

- C.1: ∀ ⲁ ∈ Σ: ⲁ ∈ S
- W.1: ∀ α ∈ L: [ (l(α) ≠ 0) ∧ (∀ i ∈ N:sub:`l(α)`: α[i] ≠ σ) ]
- S.1: ( ∀ α ∈ L: ∃ ζ ∈ C:sub:`L``: α ⊂:sub:`s` ζ ) ∧ ( ∀ ζ ∈ C:sub:`L`: ∃ α ∈ L: α ⊂:sub:`s` ζ )
- S.2: ∀ ζ ∈ C:sub:`L` : ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ L

Theorems
--------

- T 1.1.1: ∀ u, t ∈ S: l(ut) = l(u) + l(t)
- T 1.1.2: | S | ≥ ℵ:sub:`1`
- T 1.1.3: ∀ s ∈ S: ε ⊂:sub:`s` s
- T 1.2.1: ∀ α ∈ L:  αε = εα = α
- T 1.2.2: ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: α[i] ⊂:sub:`s` α
- T 1.2.3: ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: α[i] ≠ ε
- T 1.2.4: ∀ s ∈ S: inv(inv(s)) = s
- T 1.2.5: ∀ u, t ∈ S: inv(ut) = inv(t)inv(u)
- T 1.2.6: ∀ u, t ∈ S : u ⊂:sub:`s` t ↔ inv(u) ⊂:sub:`s` inv(t) 
- T 1.2.7: ∀ t, u, v ∈ S : (t ⊂:sub:`s` u) ∧ (u ⊂:sub:`s` v) → (t ⊂:sub:`s` v) 
- T 1.2.8: ∀ n ∈ ℕ: ∀ p ∈ Χ:sub:`L(n)`: ∃! s ∈ S: s = DΠ:sub:`i=1`:sup:`n` p(i)
- T 1.2.9: ∀ n ∈ ℕ, ∀ p ∈ Χ:sub:`L(n)` ∃! s ∈ S: s = LΠ:sub:`i=1`:sup:`n` p(i)
- T 1.3.1: ∀ α ∈ L: α ∈ R ↔ α = inv(α)
- T 1.3.2: ∀ α ∈ L: α ∈ I ↔ inv(α) ∈ I
- T 1.3.3: R ⊆ I
- T 1.3.4: If | R | is even, then | I | is even. If | R | is odd, then | I | is odd.
- T 2.1.1: ∀ ζ ∈ C:sub:`L`:  ∑:sub:`j=1`:sup:`Λ(ζ)` l(ζ{j}) ≥ Λ(ζ)
- T 2.1.2: ∀ ζ, ξ ∈ C:sub:`L`: Λ(ζξ) ≤ Λ(ζ) + Λ(ξ)
- T 2.1.3: ∀ ζ ∈ C:sub:`L`: ∀ i, j ∈ N:sub:`Λ(ζ)`: i ≠ k → ∃ n ∈ N:sub:`l(ζ)`: (i/n/j):sub:`ζ`
- T 2.2.1: ∀ ζ ∈ C:sub:`L`: l(ζ) ≠ 0
- T 2.2.2: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`l(ζ)`: ζ[i] ⊂:sub:`s` ζ
- T 2.2.3: ∀ ζ ∈ C:sub:`L` : ∀ i ∈ N:sub:`l(ζ)`:  ζ[i] ≠ ε
- T 2.2.4: ∀ ζ ∈ C:sub:`L`: Λ(ζ) ≥ 1
- T 2.2.5: ∀ ζ ∈ C:sub:`L`: ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}
- T 2.3.1: A(n) ⊆ C:sub:`L`
- T 2.3.2: ∀ ζ ∈ A(n): Λ(ζ) = n
- T 2.3.3: ∀ ζ ∈ C:sub:`L`: ζ ∈ A(Λ(ζ))
- T 2.3.4: ∀ ζ ∈ C:sub:`L`: ∃ p ∈ X:sub:`L`(Λ(ζ)): ζ = DΠ:sub:`i=1`:sup:`n` p(i)
- T 2.3.5: ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ inv(ζ) ∈ K
- T 2.3.6: ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → ζ ∈ C:sub:`L`
- T 2.3.7: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ ∈ K → inv(ζ){i} ∈ L
- T 2.3.8: ∀ ζ ∈ C:sub:`L`: inv(DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) = DΠ:sub:`i=1`:sup:`Λ(ζ)` inv(ζ{Λ(ζ) - i + 1})
- T 2.3.9: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ ∈ K → inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
- T 2.3.10: ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ (∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})) ∧ (inv(ζ) ∈ A(Λ(ζ)))
- T 2.3.11: ∀ ζ ∈ C:sub:`L`: ζ ∈ K → ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I
- T 3.1.1: ∀ ζ ∈ C:sub:`L`: inv(ς(ζ)) = ς(inv(ζ))
- T 3.1.2: ∀ ζ, ξ ∈ C:sub:`L`: ς(ζξ) = (ς(ζ))(ς(ξ))
- T 3.1.3: ∀ ζ ∈ C:sub:`L`: ∀ ζ ∈ C:sub:`L`: ς(ς(ζ)) = ς(ζ)
- T 3.1.4: ∀ ζ ∈ C:sub:`L`: ∀ ζ ∈ C:sub:`L`: Λ(ς(ζ)) ≤ 1
- T 3.1.5: ∀ u, t ∈ S : u ⊂:sub:`s` t ↔ ς(u) ⊂:sub:`s` ς(t) 
- T 3.1.6: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` ς(ζ)
- T 3.1.7: ∀ ζ ∈ K: [ ς(ζ) = inv(inv(ς(ζ))) ]
- T 3.1.8: ∀ ζ ∈ C:sub:`L`: ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}
- T 3.1.9: ∀ n ∈ ℕ: ∀ p ∈ Χ:sub:`L(n)`: ς(DN:sub:`i=1`:sup:`n` p(i)) = LN:sub:`i=1`:sup:`n` p(i)
- T 3.1.10: ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ l(ς(ζ))
- T 3.2.1: PP ⊂ K
- T 3.2.2: ∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
- T 3.2.3:∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I
- T 3.2.4: PP ⊂ P
- T 3.2.5: PP ∪ IP = P
- T 3.2.6: ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i + 1 ) ∧ (l(ζ[:i+1]) = l(ζ[i+1:]))
- T 3.2.7: ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i) ∧ (l(ζ[:i]) + 1 = l(ζ[i:]))
- T 3.2.8: ∀ ζ ∈ C:sub:`L`: ∃ n ∈ N:sub:`l(ζ)`: ( l(ζ[:n]) = l(ζ[n:]) ) ∨ (l(ζ[:n]) + 1 = l(ζ[n:]))
- T 3.2.9: ∀ ζ ∈ C:sub:`L`: (∃ k ∈ ℕ : l(ζ) = 2k + 1) ↔ ω(ζ) = (l(ζ) + 1)/2
- T 3.2.10: ∀ ζ ∈ P:sup:`-`: ω(ζ) = (l(ζ) + 1)/2
- T 3.2.11: ∀ ζ ∈ C:sub:`L`: (∃ k ∈ ℕ : l(ζ) = 2k) ↔ ω(ζ) = l(ζ)/2
- T 3.2.12: ∀ ζ ∈ P:sup:`+`: ω(ζ) = l(ζ)/2
- T 3.2.13: l(ζ) + 1 = l(ζ[:ω(ζ)]) + l(ζ[ω(ζ):])
- T 3.2.14: 
- T 3.2.15: P:sup:`-` ∩ P:sup:`+` = ∅
- T 3.2.16: P:sup:`-` ∪ P:sup:`+` = P 
- T 3.3.1: ∀ ζ ∈ P: [ (inv(ζ{1}) ⊂:sub:s ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:s ζ{1}) ] ∧ [ (ζ{1} ⊂:sub:s inv(ζ{Λ(ζ)})) ∨ (ζ{Λ(ζ)} ⊂:sub:s inv(ζ{1})) ]
- T 3.3.2: ∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( (inv(ζ{ω-}) ⊂:sub:`s` ζ{ω+}) ∨ (inv(ζ{ω+}) ⊂:sub:`s` ζ{ω-}))
- T A.1.1: ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L
- T A.2.1: ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1
- T A.2.2: ∀ s ∈ S: Δ(s) = Δ(inv(s))
- T A.2.3: ∀ ζ ∈ C:sub:`L`: Δ(ζ) = Δ(inv(ζ))
- T A.2.4: ∀ α ∈ L: Δ(α) = 0
- T A.2.5: ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})
- T A.2.6: ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})
- T A.2.7: ∀ ζ ∈ C:sub:`L`: l(ζ) ≥  Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})
- T A.2.8: ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ)
- T A.2.9: ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)
- T A.2.10: ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)
- T A.2.11: ∀ ζ ∈ C:sub:`L`: Δ(Ζ ⋅ Σ:sub:`σ`)= 0
- T A.2.12: ∀ t ∈ S: l(ς(t)) + Δ(t) = l(t)
- T A.2.13: ∀ ζ ∈ C:sub:`L`: l(ς(t)) + Λ(ζ) = l(ζ) + 1
- T A.3.1: ∀ α ∈ L: α ∈ L:sub:`σ` ↔ [ ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:s α ]
- T A.3.2: L:sub:`P` ⊂ L:sub:`σ`
- T A.3.3: ∀ α ∈ L:sub:`P`: α = inv(α)
- T A.3.4: L ∩ L:sub:`P` ⊆ R
- T A.3.5: L:sub:`P` ⊂ R:sub:`L_σ`
- 
Introduction
============

The goal of this paper is to introduce formal constraints the palindromes in *any* language and corpus must satisfy independently of the semantic interpretation of their constituent words and sentences. These formal constraints will in turn lead to the identification of the main structural elements of palindromes. After a language is assumed and a class of words identified, these structural elements can be used as a basis for further semantical and statistical analysis of the assumed language. 

At the outset, it must be stated the complexity of pursuing a complete theory of palindrome currently exceeds the mental capacities of the author. Palindromes are a rich and diverse linguistic species, appearing in many different shapes and sizes. Some of these guises are more amenable to analysis than others. 

This work will introduce the notions of a palindrome's core attributes: *aspect*, *parity*, *punctuality* and *case*. The first two attributes are within the scope of formal analysis. The third and fourth attributes, however, presents certain difficulties that will be more fully appreciated after the theory to describe the first two attributes has been solidifed. Suffice to say, it is the author's opinion these second two attributes of palindromes cannot be given an account unless semantic assumptions are introduced into the formal model.

To provide a overview of the theory of palindromic structures and give a general notion of what is meant by these attributes of a palindrome, consider three well-known examples,

- No devil lived on.
- Not on.
- Don't nod.

The first example is what will be termed a *perfect palindrome*. This sentence, ignoring case and punctuation, is a perfect mirror image of itself. The reversal of *"no devil lived on"* reads the same forwards as backwards. 

The second example is what will be termed an *imperfect palindrome*. This sentence, even ignoring the mitigations of case and punctuation, is not an *exact* mirror image of itself. The strict reversal of "not on" is "no ton". The spaces in the reversed sentence need un-scrambled in order to retrieve the semantic content. However, the reversed string is not precisely *devoid* of semantic content. The relative order of the characters is still preserved in the string; it is only the spaces which need re-arranged. 

This distinction between *perfect* and *imperfect* is termed a palindrome's *aspect*. The *aspect* denotes the type of symmetry displayed by the palindrome. This symmetry is a measure of how much semantic content is preserved under sentence reversal. 

This insight into the *aspect* of a palindrome will lead to the introduction of a linguistic operation termed a *sigma reduction*. This operation will in turn lead to a formal definition of palindromes that describes their syntactical structure in terms of delimiters (spaces) and inversions (sentence reversal).

The *parity* of a palindrome is related to its *palindromic pivot*, or its point of symmetry.  In other words, a palindrome is type of sentence that has a "*center*". This "*center*" will be termed its *pivot*. The *parity* of a palindrome is determined by its length, which manifests as the type of pivot that describes it symmetry. For example, the sentence "*no devil lived on*" with character length 19 reflects around the pivot of " ", the sentence's central character, whereas the sentence "*not on*" with character length 6 reflects around an empty character "" between "t" and " ". From this example, it can be seen that depending on the parity of the sentence length, the palindromic pivot will either be a character in the sentence, or an empty character that acts as a boundary between two actual characters in the sentence. 

As it will turn out, this example of parity is oversimplified, due to the complications introduced by the aspect of a palindrome. The pivot of a palindrome cannot be rigorously defined until the semantic content of a palindrome's *imperfection* is reconstituted somehow.

The third example of "*Don't nod*" demonstrates the deepening ambiguity of introducing punctuation to palindromes. The reversal of this sentence is the opaque *"don t'nod"*. Now, in addition to the scrambling of the spaces, the reversed string must also have its punctuation re-sorted. There is no formal method known to the author for dealing with these types of ambiguities that depend entirely on the semantic interpretation of the language under consideration, such as the rules of contractions. The *punctuality* of a palindrome can only be described by introducing semantics into the theory.

Similarly, the fourth attribute of palindromes, *case*, is a semantic construct that possesses no unifying syntactical properties across languages (as far as the author knows). *Case* is a semantic relationship that identifies characters in an alphabet as different manifestations of the same underlying semantic entity, i.e. *"a"* and *"A"* are regard as different *"modes"* of the same letter. This information is not present in the syntax of a language and is an extra assumption that must be modeled accordingly.

The aim of this analysis is to develop a theory of palindromes *independent* of semantic interpretation. In other words, formalizing a theory of palindromes that describes the logical structure of their aspect and parity is the goal of the current analysis. For this reason, all complications that arise from case and punctuality are ignored. The examples that are considered in the following section only deal with sentences that are meaningful without the considerations of case or punctuations.

This restriction to *aspect* and *parity* may appear restrictive; Indeed, it may be argued by introducing this restriction to the formal theory that is about to developed, it has no application to actual language. To this argument, it should be countered the structures uncovered in this restricted subset of language must nevertheless preserve their structure when embedded into the whole of language.

A note on the terminology introduced in this work is in order. When a semantic term is capitalized, e.g. Word or Sentence, this will mean it is referred to in its capacity as a formal entity. While the formal system was designed to model the actual syntax of Characters, Words and Sentences, this should not be taken to mean the formal entities that emerge from this system are necessarily representative of actual linguistic entities. While the formal entities in this system may not map *one-to-one* with their empirical counterparts, it will be seen their characteristics nevertheless provide insight into the nature of their empirical counterparts.

As the thrust of the main results in Section IV is sufficiently novel, the author has gone to great lengths to make its foundation as rigorous as possible. Many of the initial theorems are proofs of common-sense notions relating to words and sentences. The banality of Section I and parts of Section II is in part an effort to ensure the applicability across natural languages regarding the results shown in Section II.III and Section III. The core theorems of Section III could be proved in a degenerate form in a system with less notational complexity by assuming a specific language, but the depth of insight would be lost in the vagueness of definitions.