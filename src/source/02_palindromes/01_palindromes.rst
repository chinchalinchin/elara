======================
Palindromic Structures
======================

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

As the thrust of the main results in Section III is sufficiently novel, the author has gone to great lengths to make its foundation as rigorous as possible. Many of the initial theorems are proofs of common-sense notions relating to words and sentences. The banality of Section I and parts of Section II is in part an effort to ensure the applicability across natural languages regarding the results shown in Section II.III and Section III. The core theorems of Section III could be proved in a degenerate form in a system with less notational complexity by assuming a specific language, but the depth of insight would be lost in the vagueness of definitions.

Section I: Definitions 
======================

Some general notation adopted throughout the course of this work is given below.

1. **N**:sub:`n` will represent the set of natural numbers starting at 1 and ending at *n*, 

    N:sub:`n`= { 1, 2, ... , n }

2. The cardinality of a set **A** will be denoted | A |

3. The ∎ symbol will be used to denote the ending of all Definitions, Examples and Proofs. 

4. The terms *"set"* and *"class"* are used interchangeably. 
   

Section I.I: Strings
--------------------

The domain of discourse is composed of *Strings*. A String will be represented as follows, 

    1. String (*s*:sub:`1`, *s*:sub:`2`, *s*:sub:`3`): A lowercase English *s* with a subscript denotes a String. Often the subscript will be dropped and *s* will be used. The letter *t*, *u*, *v* and *w* are also reserved for Strings.

A String is regarded as a linguistic artifact that is defined by its *length*, its *Characters* and their *ordering*. It is assumed if one knows how many Characters are in a String, which Characters are in a String and in what order they occur, then one has all the information necessary to completely determine the String. This notion is made more precise below with the introduction of several core definitions.

The set of all Strings is denoted **S**. At this point, nothing definitive can be asserted about the contents or cardinality of **S**. Once Characters are introduced and concatenation is defined, it will be possible to make claims regarding **S**.

The goal is to define all linguistics entities over the set of all Strings: Characters, Alphabets, Words, Languages, Sentences and Corpuses. As each of these entities is introduced and defined, a new level of relations will reveal itself. Palindromic symmetries will manifest on each level, in slightly different but related forms. Each type of symmetry will involve, in some form or another, the concept of *String Inversion*, to be defined shortly. The essence of a Palindrome lies in binding together the syntactical symmetries at every linguistic layer into a semantic whole. Indeed, it will be seen the symmetrical structure required by Palindromes in turn requires these linguistic layers to have specific synactical properties, regardless of their semantic interpretation.

A *Word* will be considered a *type* of String. Colloquially, a Word can be understood as a String with semantic content. The goal of this section is to describe the necessary syntactic conditions for a String to be considered a formal Word, without taking into account the semantic content that is assigned to it through everyday use. In other words, the analysis assumes Words have already been selected from the set of all possible Strings and assigned interpretations. 

Characters
^^^^^^^^^^

A *Character* is the basic unit of a String. Characters will be represented as follows,

    1. Characters (*𝔞*, *𝔟*,  *𝔠*, etc. ): Lowercase Fraktur letters represent Characters. Subscripts will occassionally be used in conjunction with Fraktur letters to denote Characters at specific positions within Strings, (*𝔞*:sub:`1`, *𝔞*:sub:`2`, ... ). 
    2. Empty (*ε*): The lowercase Greek letter epsilon, *ε*, represents the Empty Character.
    3. Delimiter (*σ*): The lowercase Greek letter sigma, *σ*, represents the Delimiter Character. 

In the case of English, Characters would correspond to letters such as "a", "b", "c", etc., the Empty Character would correspond to the null letter, "", and the Delimiter Character would correpond to the blank letter, " ". 

The exact meaning of these symbols should be attended with utmost care. *𝔞*, *𝔟*,  *𝔠*, etc., represent Characters of the Alphabet and thus are all unique, each one representing a different linguistic element. When Character symbols are used with subscripts, *𝔞*:sub:`1`, *𝔞*:sub:`2`, etc., they are being referenced in their capacity to be ordered within a String. With this notation, it is not necessarily implied 𝔞*:sub:`1` and *𝔞*:sub:`2` are unequal Character-wise, but that they are differentiated only by their relative order in a String.

The Empty Character also deserves special mention, since it represents a *null* Character. The Empty Character is to be understood as a Character with no semantic content. It can be added or subtracted from a String without altering it in any way. The domain of all Strings **S**, as will be shown in (the albeit informal) Theorem 1.1.2, is uncountably infinite. Beyond this, the Empty Character introduces further ambiguity when defining the concepts of Word and Language, since multiple Strings with the Empty Character, i.e. *𝔞ε*, *𝔞εε*, *𝔞εεε*, etc., can represent the same semantic content. In order to formally define these linguistic entities, the Empty Character must be excluded from the domain of Words and Language. 

Take note, at this point it is has not yet been shown that Characters are Strings; the preceding statements should be taken heuristically. This will be rectified in the next section with the formal definition of concatenation and the introduction of Character Axiom C.1. 

The aggregate of all Characters is called an *Alphabet* and is denoted by an uppercase Sigma, **Σ**,

    Σ = { *ε*, *σ*, *𝔞*, *𝔟*,  *𝔠*, ... }

It will sometimes be necessary to refer to indeterminate Characters, so notation is introduced for Character Variables,

    1. Character Variables (*ⲁ*, *ⲃ*, *ⲅ*, etc. ): Lowercase Coptic letters will represent Character Variables, i.e. indeterminate Characters. Subscripts will occassionally be used with Coptic letters to denote Word Variables, (*ⲁ*:sub:`1`, *ⲁ*:sub:`2`, ... )

Once again, it should be noted when Character Variables are used with subscripts, it is meant to refer to the capacity of a Character Variable to be indeterminate at a *determinate position* within a String. Moreover, the range of a Character Variable is understood to be the Alphabet **Σ** from which it is being drawn.

At this early stage, the formal system needs to introduce a notion of *equality* to make any significant headway. There will be a several types of equality defined within the system, but each new layer of equality will be built on top of the primitive notion of *Character Equalty* now introduced in the first preliminary Axiom to the formal system.

**Axiom C.0: The Equality Axiom**

For any Characters *ⲁ, ⲃ ∈* **Σ**, the notion of equality, denoted by *ⲁ = ⲃ*, is a primitive concept and assumed to be understood. It is further assumed that Character Equality is an equivalence relation, satisfying reflexivity, symmetry and transitivity,

    1. ∀ ⲁ ∈ Σ: ⲁ = ⲁ
    2. ∀ ⲁ, ⲃ ∈ Σ: ⲁ = ⲃ ↔ ⲃ = ⲁ
    3. ∀ ⲁ, ⲃ, ⲅ ∈ Σ: (ⲁ = ⲃ ∧ ⲃ = ⲅ) → (ⲁ = ⲅ) ∎ 

Concatenation 
^^^^^^^^^^^^^

Concatenation is considered the sole constitutive operation for the formation of Strings. It is taken as a primitive operation, but not an elementary operation. By this it is meant the notion of concatenation that is about to be adopted does not define concatenation solely in terms of Strings. Concatenation will be defined as a hetergeneous operation that is performed between Characters in a Alphabet and Strings.

**Definition 1.1.1: Concatenation**  

The result of *concatenating* any two Characters *ⲁ* and *ⲃ** is denoted *ⲁⲃ*. To make the operands of concatenation clear, parenthesis will sometimes be used to separate the Characters being concatenated, e.g. *ⲁ(ⲃ) = (ⲁ)ⲃ = (ⲁ)(ⲃ) = ⲁⲃ*. Character concatenation is defined inductively through the following schema,

    1. Basis Clause: ∀ ⲁ ∈ Σ: ⲁε = ⲁ
    2. Inductive Clause: ∀ ⲁ, ⲃ ∈ Σ, ∀ s ∈ S: ⲁ(ⲃs) = (ⲁⲃ)s
    3. Uniqueness Clause: ∀ ⲁ, ⲃ, ⲅ, ⲇ ∈ Σ: (ⲁⲃ = ⲅⲇ) → ((ⲁ = ⲅ) ∧ (ⲃ = ⲇ)) 
    4. Comprehension Clause: ∀ ⲁ ∈ Σ, ∀ s ∈ S: ⲁs ∈ S ∎

Colloquially, *ⲁⲃ* is the String that results from placing *ⲃ* behind *ⲁ*.

The first clause in Definition 1.1.1 is the basis step of induction which states any Character appended to the Empty Character is the Character itself. The second clause is the inductive step which allows the concatenation of Characters of arbitrary length into Strings through recursion.

The Uniqueness Clause states that if the concatenation of two characters *ⲁ* and *ⲃ* is equal to the concatenation of two other characters *ⲅ* and *ⲇ*, then it must be the case that *ⲁ* is equal to *ⲅ* and *ⲃ* is equal to *ⲇ*. In other words, there's only one set of Characters that can form a given String through concatenation.

It is assumed that the operation of concatenation is closed with respect to the set of all Strings **S**. In other words, concatenation will always yield a String. This assumption is partly captured in the Comprehension Clause of Definition 1.1.1. This clause ensures that the result of concatenating any Character with a String is a String. However, this clause in and of itself does not ensure the closure of **S** with respect to concatenation. In order to close **S** over concatenation, an additional assumption must be introduced. Before introducing this assumption in the form of an axiom, a brief explanation is required for this departure from convention.

Concatenation as it is normally found in the fields of automata theory or regular expressions is treated as a primitive operation performed between two string operands. Concatenation of multiple strings is then defined inductively, similary to Definition 1.1.1 but differing in the essential quality that it treats of only strings. The current formulation differs in that concatenation in this system is not conceived, at least in the primitive stage, as the "joining" of two or more Strings. Instead, the formal system under construction treats concatenation as an elementary operation that occurs between Characters and Strings, i.e. it is a *hetergeneous* operation.

The reason for this distinction will become clear as the formal theory begins to detail palindromic structures that display symmetry across linguistic levels. It should only be noted at this point that Definition 1.1.1 is a conscious decision to depart from convention.

To make this distinction plain, consider that given an Alphabet **Σ** and Definition 1.1.1, one still cannot say the result of a concatenation of two Characters is a String, nor make any claim about the contents of **S**, the set of all Strings. The Comprehension Clause of Definition 1.1.1 only states the result of concatenating a Character with a String is a String. It says nothing at all about whether or not single Characters themselves are Strings, and thus it says nothing about whether the result of concatenating two or more Characters is itself a String. 

In order to rectify this, the first (official) Axiom is now introduced.

**Axiom C.1: The Character Axiom**

    ∀ ⲁ ∈ Σ: ⲁ ∈ S

This Axiom states the intuitive notion that all Characters are Strings. This includes Empty Characters and Delimiter Characters. This Axiom, in conjunction with Definition 1.1.1, immediately populates the set of all Strings **S** with an uncountably infinite domain of objects (See Theorem 1.1.2 for an informal proof of this fact) consisting of every possible combination of Characters from the Alphabet, in every possible order. In other words, Axiom C.1 in conjunction with Definition 1.1.1 ensure the domain is non-Empty. 

**Example** Let *s = 𝔞𝔟𝔠* and *t = 𝔡𝔢𝔣*. The concatenation of these two Strings *st* is written,

    st = (𝔞𝔟𝔠)(𝔡𝔢𝔣) 
    
Using the inductive clause, this concatenation can be grouped into simpler concatenations as follows,    
    
    𝔞(𝔟(𝔠(𝔡(𝔢𝔣)))) = (((((𝔞𝔟)𝔠)𝔡)𝔢)𝔣) = 𝔞𝔟𝔠𝔡𝔢𝔣

Therefore, *st = 𝔞𝔟𝔠𝔡𝔢𝔣* ∎

Length
^^^^^^

It will sometimes be convenient to represent Strings as ordered sets of Characters, rather than serialized concatenations of Characters. The two formulations are equivalent, but the set representation has advantages when it comes to quantification and symbolic logic. When a String or Word representation is intended to be interpretted as a set, it will be written in bold uppercase letters. For example, the String represented as the concatenation *s*:sub:`1` *= 𝔞𝔟𝔠* would be represented in this formulation as a set of ordered pairs **S**:sub:`1`, where the first coordinate encodes the position of the Character in the String,

    S:sub:`1` = { (1, 𝔞), (2, 𝔟), (3, 𝔠) }

Note, since sets do not preserve order, this would be equivalent to,

    { (3, 𝔠), (2, 𝔟), (1, 𝔞) }

To simplify notation, it is sometimes beneficial to represent this set as a sequence that *does* preserve order as,

    S:sub:`1` = (𝔞, 𝔟, 𝔠) 

However, before adopting this notation formally, a problem exists. It is the intention of this analysis to treat Empty Characters as vacuous, i.e. Characters without semantic content. However, this does not mean the Empty Character will not be treated as a legitimate entity within the confines of the formal system. Instead, the goal is to construct a formal system that excludes the Empty Character from the domain of semantics, but not the domain of syntax. 

Due to the nature of the Empty Character and its ability to be concatenated ad infinitum, and the desire to construct a theory of Words and Language that emerges from the transcendental domain of Strings, the construction of the Character-level set representation of a String requires a special algorithm to filter out any Empty Characters while preserving the relative order of the non-Empty Characters concatenated into the String. 

Before presenting the *Emptying Algorithm* that will allow the construction of the Character-level representation of an arbitrary String, motivation for the particular form of the Emptying Algorithm is given by way of analogy to assembly language in computer science. 

At the most primitive level, iteration in assembly or machine language is essentially achieved through a combination of two components,

    1. Memory Addresses: Data, including Strings (which are just sequences of Characters), is stored in memory at specific addresses.
   
    2. Registers: The CPU has special memory locations called registers. Registers are used to hold, 

        - Data: Values being currently processed.
        - Pointers: Memory addresses of data being accessed.
        - Counters: Values used to keep track of the iteration's progress.
        - Instructions: The CPU executes a sequence of instructions.

The Instruction set consists of operations for,

   - Load data: Move data from memory to registers.
   - Store data: Move data from registers to memory.
   - Arithmetic operations: Perform calculations (like adding 1).
   - Conditional jumps: Change the flow of execution based on certain conditions (e.g., checking if a counter has reached a certain value).

At the assembly level, a typical algorithm for iterating through a String is given below (the semi-colon ";" denotes a code comment),

.. code-block::

    ; Assume:
    ;   - String "abc" is stored at memory address STRING_START
    ;   - STRING_START: 'a', 'b', 'c', 0  (0 is a null terminator indicating the end)
    ;   - Register R1 will be used as a pointer (initially holds STRING_START)
    ;   - Register R2 will be used as a counter (initially holds 0)

    LOOP_START:
        LOAD R3, (R1)     ; Load the character at the address in R1 into R3
        CMP R3, 0        ; Compare R3 with the null terminator (0)
        JE LOOP_END      ; If R3 is 0 (equal), jump to LOOP_END
        ADD R1, 1        ; Increment R1 (move the pointer to the next character's address)
        ADD R2, 1        ; Increment the counter R2
        JMP LOOP_START   ; Jump back to LOOP_START
    LOOP_END:

A step-by-step breakdown of this algorithm is instructive for understanding how iterationg through String is implemented at the most basic level in the theory of computation. Each command in this assembly-like language is broken down as follows,

    1. R1 (pointer) is set to STRING_START.
    2. R2 (counter) is set to 0.
    3. LOOP_START: This is a label marking the beginning of the loop.
    4. LOAD R3, (R1): The Character at the memory address stored in R1 is loaded into register R3.
    5. CMP R3, 0: The character in R3 is compared to the null terminator (0).
    6. JE LOOP_END: If the comparison is equal (meaning we've reached the end of the string), the program jumps to the LOOP_END label.
    7. ADD R1, 1: This is the crucial step where the pointer is incremented. 1 is added to R1 because each Character occupies one memory location (in this simplified example). This moves the pointer to the next Character's address.
    8. ADD R2, 1: The counter is incremented.
    9. JMP LOOP_START: The program jumps back to the beginning of the loop.

The key idea is this algorithm is *"unaware"* of how *long* the String is that is stored in the *R1* register. The algorithm naively iterates over the data and then checks whether or not the data has been processed with the command *CMP R3, 0*, i.e. the algorithm checks whether or not the next Character in the String *exists*. 

By treating Strings as Characters stored sequentially in a data register, this algorithm is able to construct a representation of the String on a higher level, allowing for the definition of derivative concepts, like String Length. 

This insight leads directly to the definition of the Character-level set representation of a String and its construction via the Emptying Algorithm.

**Definition 1.1.2: Character-level Set Representations**

Let *t* be a String with Characters *𝔞*:sub:`i`. The Character-level set representation of *t*, denoted by bold uppercase letters **T**, is defined as the ordered set of Characters obtained by removing each Empty Character, *ε*. Formally, **T** is constructed using the *Emptying Algorithm* 

**Algorithm 1: The Emptying Algorithm**

The Emptying Algorithm takes a string *t* as input, which can be thought of as a sequence of Characters *𝔞*:sub:`1`, *𝔞*:sub:`2`, *𝔞*:sub:`3`, ... , where some characters might be *ε*. It then initializes a set to hold **X** and an index for the Characters it will add to **X**. The algorithm iterates the index and constructs the Character-level representation by ignoring *ε*. The Emptying Algorithm is formally defined below.

.. topic:: Algorithm Empty(t: String)

    # Input: A string t
    # Output: An ordered set T representing the character-level set representation of t

    # Initialization
    ## empty set to hold Character-level representation
    T ← ∅
    ## index for non-Empty Characters in T
    j ← 1 
    ## index for iterating through original String t
    i ← 1 

    # Iteration
    1. While 𝔞:sub:`i` exists:

        a. If 𝔞:sub:`i` ≠ ε:

            i. T ← { (j, 𝔞:sub:`i`) } ∪ T
            ii. j ← j + 1

        b. i ← i + 1

    1. Return T ∎

Step 1 in the Emptying Algorithm is essentially equivalent to a *try-catch* block in modern programming languages. Step 1 is materially different than comparing a Character in a String to the Empty Character. Step 1 relies on the idea that attempting to select a Character outside of the String is an undefined operation and will thus result in an error (i.e. a stack overflow). As the Characters in a String are iterated through, as long as the String is not infinite, the iteration will eventually reach the last Character, and once it tries to select the next Character, it will throw an error. 

This point is important because the Emptying Algorithm must remain *"unaware"* of String Length. The essence of the Emptying Algorithm is that it implicitly defines the length of the String as its number of non-Empty Characters, without explicitly stating that is what *String Length* is or how it is calculated. This is crucial to the formalization of Strings as ordered sequences of Characters, because it allows String Length to be defined without any circularity. In other words, this formalization avoids the vicous circle of defining the Character-level representation in terms of String Length and then defining String Length as the cardinality of the Character-level representation.

The following example illustrates a simple application of the Emptying Algorithm.

**Example**

Let *t = ("ab")(ε)("c")*.

   1. i = 1, 𝔞:sub:`1` = "a". Add (1, "a") to T. j increases to 2. i increases to 2.
   2. i = 2, 𝔞:sub:`2` = "b". Add (2, "b") to T. j increases to 3. i increases to 3.
   3. i = 3, 𝔞:sub:`3` = ε. Skip Empty Character. i increases to 4.
   4. i = 4, 𝔞:sub:`4` = "c". Add (3, "c") to T. j increases to 4. i increases to 5.
   5. i = 5, 𝔞:sub:`5` does not exist. Algorithm halts.  

The result returned by the Emptying Algorithm would then be,

    T = {(1, "a"), (2, "b"), (3, "c")} ∎

This method of abstraction and notation will be employed extensively in the subsequent proofs. It will be made more convenient with Character Index notation in the next section, after the preliminary notion of *String Length* is defined. However, in order to define String Length, a method of referring to a String as a set of ordered non-Empty Characters is required. The construction afforded by the Emptying Algorithm operating on any input String *t* will serve that purpose.  

As a brief aside, it may seem the formal system would be better developed by excluding the Empty Character altogether from its Alphabet. The Empty Character's presence in the Alphabet complicates matter extensively, requiring intricate and subtle definitions. 

The reasons for this are two-fold. First: the Empty Character *ε* will be necessary for defining the *Pivot* of a Palindrome, the point around which a certain class of Palindrome reflect. Second: Strings consisting of only the Empty Character are not a mere novelty of abstraction; They play a crucial role in computer science and database management. Any rigorous formal system that excludes the notion of an Empty Character will fail to describe the exact domain from which Language arises, and thus it may fail to account for pre-Language syntactical conditions that necessarily affect the formation of Language.

This approach is not without its challenges. As Definition 1.1.3 below will make clear, if *ε* is considered part of the Alphabet, the typical notion of a String's Length is undefined, as *ε* can be concatenated an infinite number of times to a String without altering its content. To explicate the notion of *length*, consider the constraints that must be placed on this concept in the palindromic system,

    - The length of the string "abc" is 3, as it contains three non-Empty Characters.
    - The length of the string "aεbεc" is still 3, as the Empty Characters (*ε*) are not counted.

This example motivates the following definition.

**Definition 1.1.3: String Length** 

Let *t* be a String. Let **T** be the Character-level set representation of *t* constructed through the Emptying Algorithm in Definition 1.1.2. The String Length of *t*, denoted *l(t)*, is the number which satisfies the following formula,

    l(t) = | T | ∎

**Example** 

Consider the String *t = ("aa")(ε)("b")(ε)("bcc")*

By Definition 1.1.3, 

    T = { (1, "a"), (2, "a"), (3, "b"), (4, "b"), (5, "c"), (6, "c") }

Therefore, 

    | T | = 6 ∎

This formalization of String Length, with the Emptying Algorithm, while perhaps prosaic, maps to the intuitive notion of a String's length, i.e. the number of non-Empty Characters, while still allowing for a calculus of concatenation that involves Empty Characters. For reasons that will become clear in Section II, *l(s)* will be called the *String Length* of a String s. 

To confirm Definitions 1.1.2 and 1.1.3 correspond to reality, a theorem confirming its expected behavior is now derived. Definition 1.1.3 ensures the String Length of concatenated Strings is equal to the sum of their individual String Lengths, as demonstrated by Theorem 1.1.1.

**Theorem 1.1.1** ∀ u, t ∈ S: l(ut) = l(u) + l(t)

Let *u* and *t* be arbitrary strings in **S**. Let **U** and **T** be the character-level representations of *u* and *t*, respectively,

    U = ( 𝔞:sub:`1`, 𝔞:sub:`2`, ... , 𝔞:sub:`l(s)`)

    T = ( 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)``)

Let *ut* be the concatenation of *u* and *t*. By Definition 1.1.1, the Character-level representation of *ut* is,

    UT = ( 𝔞:sub:`1`, 𝔞:sub:`2`, ..., 𝔞:sub:`l(s)`, 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)`)

By Definition 1.1.3, the String Length of a String is the number of indexed non-Empty Characters it contains. Thus, *l(u)* is the number of non-Empty Characters in *u*, *l(t)* is the number of non-Empty Characters in *t*, and *l(ut)* is the number of non-Empty Characters in *ut*.

Since concatenation simply joins Characters without adding or removing Characters, with the possible exception of Empty Characters through the Basis Clause of Definition 1.1.1, the non-Empty Characters in *ut* are precisely the non-Empty Characters from *u* followed by the non-Empty Characters from *t*.

Therefore, the total number of non-Empty Characters in *ut* is the sum of the number of non-Empty characters in *u* and the number of non-Empty Characters in *t*,

    l(ut) = l(u) + l(t)

Since *u* and *t* were arbitrary strings, this can be generalized,

*   ∀ u, t ∈ S: l(ut) = l(u) + l(t) ∎

With the concept of String Length now defined, it is also a simple matter to define String Equality in terms of Character Equality using the Equality Axiom C.0.

**Definition 1.1.4: String Equality**

Let *t* be a String. Let **T** be the Character-level set representation of *t* constructed through Definition 1.1.2,

    T = { (i, 𝔞:sub:`i`) | 1 ≤ i ≤ l(t) }
     
Let *u* be a String. Let **U** be the Character-level set representation of *u* constructed through Definition 1.1.2,

    U = { (i, 𝔟:sub:`j`) | 1 ≤ j ≤ l(u) }

The string *t* is said to be *equal* to String *u* if the Strings have equal length and the Characters at each corresponding index are equal. Formally, *t = u* if and only if,

    1. l(t) = l(u) (The String Lengths of t and u are equal)
    2. ∀ i ∈ N:sub:`l(t)`: 𝔞:sub:`i` = 𝔟:sub:`i` (The Characters at each corresponding index are equal) ∎

Finally, String Length provides the means for a quality-of-life enhancement to the formal system in the form of Character Index notation.

**Definition 1.1.5: Character Index Notation**

Let *t* be a string with Character-level representation **T**,
 
    T = (𝔞:sub:`1`, 𝔞:sub:`2`, ..., 𝔞:sub:`l(t)`). 
    
Then for any *i* such that *1 ≤ i ≤ l(t)*, *t[i]* is defined as *𝔞*:sub:`i`, where (*i*, *𝔞*:sub:`i`) *∈* **T**. ∎

Character Index notation will simplify many of the subsequent proofs, so it is worth taking a moment to become familiar with its usage. Indexing starts at 1, consistent with the definition of **N**:sub:`n` made in the preamble. So, *t[1]* is the first character of *t*, *t[2]* is the second, and so on.

In terms of the Character-level set representation, *t[i]* refers to the Character at position *i* in the set **T**. In other words, the notation *t[i]* implicitly assumes the String *t* has already been stripped of its Empty Characters through the Emptying Algorithm in Definition 1.1.2. This notation can effectively replace the use of lowercase Fraktur letters with subscripts (e.g., *𝔞*:sub:`i`) when referring to specific Characters within Strings.

**Example**

If s = "abc", then s[1] = "a", s[2] = "b", and s[3] = "c". ∎

With the notion of String Length established for each element in the domain and some of its basic properties established, the size of the domain itself, **S**, will now be elaborated in greater detail.
  
It is assumed **S** is at least uncountably infinite. A rigorous proof of this fact would carry the current work too far into the realm of real analysis, but as motivation for this assumption, an informal proof is presented below based on Cantor's famous diagonalization argument. 

**Theorem 1.1.2** | S | ≥ ℵ:sub:`1`

Assume, for the sake of contradiction, that the set of all Strings **S** is countable. This means the Strings can be listed in some order, 

    s:sub:`1`, s:sub:`2`, s:sub:`3`, etc.

Now, construct a new String *t* as follows:

    1. The first character of *t* is different from the first character of *s*:sub:`1`.
    2. The second character of *t* is different from the second character of *s*:sub:`2`.
    3. etc.

This string *t* will be different from every string in **S** contradicting the assumption that it was possible to list all strings. Therefore, **S** must be uncountable. ∎ 

Containment
^^^^^^^^^^^

Similar to the explication of *length*, the notion of a String *containing* another String must be made precise using the definitions introduced so far. It's important to note that in the current system the relation of *containment* is materially different from the standard subset relation between sets. For example, the set of characters in *"rat"* is a subset of the set of characters in *"tart"*, but *"rat"* is not contained in *"tart"* because the order of the characters is different.

Consider the Strings *"rat"* and *"strata"*. The string *"rat"* *is contained* in the String strata", because the order of the String *"rat"* is preserved in *"strata"*. An intuitive way of capturing this relationship is to map the indices of the Characters in *"rat"* to the indices of the Characters in *"strata"* which correspond to the indices in *"rat"*. A cursory (but incorrect) definition of *containment* can then be attempted, using this insight as a guide.

**Containment (Incorrect Version)** t ⊂:sub:`s` u

Let *t* and *u* be Strings. *t* is said to be *contained in u*, denoted by,

    t ⊂:sub:`s` u

If and only if there exists a strictly increasing function *f*: **N**:sub:`t` *→* **N**:sub:`u` such that:

    ∀ i ∈ N:sub:`l(t)`: t[i] = u[f(i)] ∎
    
This definition essentially states that *t* is contained in *u* if and only if there's a way to map the Characters of *t* onto a subsequence of the Characters in *u* while preserving their order. The function *f* ensures that the Characters in *t* appear in the same order within *u*. While this definition is incorrect, the reason why this version of *containment* fails is instructive in developing a better understanding of the subtlety involved in attempting its definition. 

First, consider an example where this definition correlates with the intuitive notion of *containment*. Let *t = "rat"* and *u = "strata"*. Then, these Strings can be represented in set notation as,

    T = { (1, "r"), (2, "a"), (3, "t") }
     
    U = { (1, "s'), (2, "t"), (3, "r"), (4, "a"), (5, "t"), (6, "a") }.

The function *f* defined as *f(1) = 3*, *f(2) = 4*, and *f(3) = 5* satisfies the condition in the proposed definition, as it maps the characters of *"rat"* onto the subsequence *"rat"* within *"strata"* while preserving their order. In addition, *f* is a strictly increasing function. Therefore, 

    "rat" ⊂:sub:`s` "strata".

Next, consider a counter-example. Let *t = "bow"* and *u = "borrow"*. Then their corresponding set representations are given by,

    T = { (1, "b"), (2, "o"), (3, "w") }
     
    U = { (1, "b'), (2, "o"), (3, "r"), (4, "r"), (5, "o"), (6, "w") }

The function defined through *f(1) = 1*, *f(2) = 5* and  *f(3) = 6* satisfies the conditions of the proposed definition. However, intuitively, *"bow"* is *not contained* in the word *"borrow"*. The reason the proposed definition has failed is now clear: the function *f* that is mapping *"bow"* to *"borrow"* skips over the Character indices 2, 3 and 4 in *"borrow"*. In other words, in addition to being strictly increasing, the function *f* which maps the smaller String onto the larger String must also be *consecutive*. This insight can be incorporated into the definition of *containment* by first defining the notion of *consecutive*,

**Definition 1.1.6: Consecutive Functions** 

A function *f* is consecutive over N:sub:`s` if it satisfies the formula,

    ∀ i, j ∈ N:sub:`s`:  (i < j) →  f(j) = f(i) + (j - i) ∎
    
This additional constraint on *f* ensures that the indices of the larger String in the containment relation are mapped in a sequential, unbroken order to the indices of the smaller String. This definition of *Consecutive Functions* can be immediately utilized to refine the notion of *containment*.

**Definition 1.1.7: Containment** t ⊂:sub:`s` u

Let *t* and *u* be Strings. *t* is said to be *contained in u*, denoted by,

    t ⊂:sub:`s` u

If and only if there exists a strictly *increasing and consecutive* function *f*: **N**:sub:`t` *→* **N**:sub:`u` such that:

    ∀ i ∈ N:sub:`l(t)`: t[i] = u[f(i)] ∎

The notion of containment will be central to developing the logic of palindromic structures in the subsequent sections. The next theorem establishes a fundamental property regarding containment.

**Theorem 1.1.3** ∀ s ∈ S: ε ⊂:sub:`s` s

Let *s* be an arbitrary string in **S**. By Definition 1.1.3, *l(ε) = 0*. Thus, **N**:sub:`l(ε)` *= ∅*.

The empty function *f: ∅ →* **N**:sub:`l(s)` vacuously satisfies the condition for containment (Definition 1.1.7), as there are no elements in the domain to violate the condition. Therefore, *ε ⊂*:sub:`s` *s*.

Since *s* was arbitrary, this can be generalized,
 
    ∀ s ∈ S: ε ⊂:sub:`s` s ∎

Section I.II: Words
-------------------

While the notion of Characters maps almost exactly to the intuitive notion of letters in everyday use, the notion of a *Word* requires explication. 

If Characters are mapped to letters in the Alphabet of a Language **L**, the set of all Strings would have as a subset the Language that is constructed through the Alphabet. The goal of this section is to define the syntactical properties of Words in **L** that differentiates them from Strings in **S** based solely on their internal cohesion as a linguistic unit. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations. In other words, this analysis will proceed without assuming anything about the interpretation of the Words in the Language beyond the fact that they *are* Words of the Language. The goal is to leave the semantic interpretation of Words in a Language as ambiguous as possible. This ambiguity, it is hoped, will leave the results of the analysis applicable to palindromic structures in a variety of languages, and perhaps make the formal system applicable to areas outside the realm of Palindromes.

**Definition 1.2.1: Language** 

A Language **L** is a set of Strings constructed through concatenation on an Alphabet **Σ** that are assigned semantic content. ∎

**Definition 1.2.2: Word** 

A Word is an element of a Language **L**. ∎

The following symbolic notation is introduced for these terms, 

    1. Words (*a*, *b*, *c*, etc.): Lowercase English letters represent Words. Subscripts will occassionally be used to denote Words, (*a*:sub:`1`, *a*:sub:`2`, ... )
    2. Language (**L**): The uppercase English letter *L* in boldface represents a Language.

In the case of English, Words would correspond to words such as "dog", "cat", etc. A Language would correspond to a set of words such as *{ "dog", "cat", "hamster", ... }* or *{ "tree", "flower", "grass", .... }*. The number of Words in a Language is denoted | L |.

Again, at the risk of unwarranted repetition, Language is assumed to be a *fixed set* known a priori to the construction of the current formal system. It not the goal of the formal system to describe the semantic conditions for a Word's eligibility in Language or how a Language is constructed from elementary Characters and Strings into a class of Words through systems like grammar or pragmatics, but rather, given a Language of Words, the formal system seeks to elaborate the syntactical conditions that are imposed on Language by its nature as a set of Strings with ordered Characters. 

Note, Definition 1.2.1 and Definition 1.2.2 relies on the idea that Words are Strings and their meaning is conveyed through the ordered sequence of its concatenated Characters. This necessarily precludes from the formal system any languages which do *not* use the ordering of Characters as the primary medium for representing Words. While edge cases like sign language exist, nevertheless, the sole constitutive feature of any natural is the *ordering* of some type of Character. In the case of sign language, a Character in the formal system might be identified with *"a configuration of fingers"* and a String might be identified with *"configurations over time"*.

It will sometimes be necessary to refer to indeterminate Words, so notation is introduced for Word Variables,

    1. Word Variables (*α*, *β*, *γ*, etc. ): Lowercase Greek letters will represent variable words, i.e. indeterminate Words. Subscripts will occassionally be used to denote Word Variables, (*α*:sub:`1`, *α*:sub:`2`, ... ). 

The exceptions to this rule for Lowercase Greek letters are Zeta and Xi, *ζ* and *ξ*, which are reserved for Sentential Variables (see Section II.I for more information.), Sigma and Epsilon, *σ* and *ε*, which are reserved for the Delimiter and Empty Character (see Section I.I for more information), and Omega, *ω*, which is reserved for the Palindromic Pivot (see Section III.II for more information).

The range of a Word Variable is understood to be the Language **L** from the Words are being drawn. 

With these definitions, the hierarchy of relationships that exist between a Word *α*, its Language **L** and the set of all Strings **S** is given by,

    1. α ∈ L
    2. α ∈ S
    3. L ⊂ S

To clarify the relationship between Strings, Words and Language in plain language,

    1. All Words belong to a Language.
    2. All Words belong to the set of all Strings
    3. Language is a subset of the set of all Strings.
    4. Not all Strings are Words. 

As mentioned several times, all objects in this formal system are defined on the domain of Strings through either the set relation of "belonging" or the set relation of "subset". Words and Characters are different types of Strings, while a Language is a subset of Strings. Because Words are Strings, defining their equality is a simple matter of referring back to the definition of String Equality.

**Definition 1.2.3: Word Equality**

Let *a* and *b* be words in **L**. Then *a = b* if and only if *a* and *b* are equal as Strings (according to Definition 1.1.4). ∎ 

The next axiom represents the minimal *necessary* assumptions that are placed on any String to be considered an element of a Language **L**, i.e. a Word. The axiom listed in this section is not *sufficient*; in other words, it is possible for a String to satisfy this axiom without being an element of a Language, but any Word that belongs to a Language must satisfy the axiom.

**Axiom W.1: The Discovery Axiom** 

    ∀ α ∈ L: (l(α) ≠ 0) ∧ (∀ i ∈ N:sub:`l(α)`: α[i] ≠ σ) ∎

There are two conjuncts in the Discovery Axiom and each of them captures a noteworthy assumption that is being made about Words in a Language. The first conjunct, (*l(α) ≠ 0*), will be used to prove some fundamental properties of Words in the next section. This condition that a Word's String Length cannot be equal to zero serves a dual purpose. First, by Definition 1.1.3, it ensures the Empty Character cannot be a Character in a Word (this fact will be more rigorously proven in Theorem 1.2.4 below), preventing vacuous semantic content. 

Second, in order for two Words to be distinguished as the same Word, there must be dimensions of comparision over which to assert the equality. One must have some criteria for saying *this* linguistic entity is equal to that *that* linguistic entity. String Length serves as one of the two dimensions for a Word necessary for a word to be "embodied" in a medium (the other being the inherent ordinality of Characters in a Word). In other words, the concept of String Length is foundational to the discovery of Words from the set of all Strings **S**. One must be able to discard those Strings possessing null content before one can engage in Language. 

While the definition of String Length and the first conjunct preclude the inclusion of the Empty Character in a Word, there is no such restriction on the Delimiter, hence the second conjunct of the Discovery Axiom. This conjunct captures the common-sense notion that a Word from a Language cannot contain a Delimiter; Instead, Delimiters are what separate Words from one another in a String. 

It is these two purely syntactical properties that allow a user of Language to separate Words from the arbitrary chaos of Strings, preparing them for the assignment of semantic content. 

Theorems
^^^^^^^^

The next theorems establish some basic results about Words in a Language within this formalization. All of these theorems should conform to the common sense notion of Words. 

**Theorem 1.2.1** ∀ α ∈ L:  αε = εα = α

This theorem can be stated in natural language as follows: For every Word in a Language, concatenating the Word with the empty String *ε* on either side results in the Word itself.

Let *α* be an arbitrary word in **L**. By Definition 1.2.2, *α* is a String of characters. By Definition 1.1.3, *l(α)* is the number of non-Empty Characters in *α*. 

Consider *ε*, the empty string. By Definition 1.1.3, *l(ε) = 0*. By Definition 1.1.1, the concatenation of any String *s* with *ε* results in a new string with the same Characters as *s* in the same order.

Therefore, *αε* and *εα* are both Strings with the same Characters as *α* in the same order. Since *α* is a Word in **L** and concatenation with *ε* does not change its length or order of Characters. Thus, by Definition 1.2.3, *αε = εα = α*.

Since *α* was arbitrary, this can be generalized: 

    ∀ α ∈ L: αε = εα = α ∎

**Theorem 1.2.2** ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: α[i] ⊂:sub:`s` α

This theorem can be stated in natural language as follows: All Characters in a Word are contained in the Word.

Assume *α* is a Word from Language **L**. By the Axiom W.1, *l(α) ≠ 0* and thus it must have at least one non-Empty Character *α[i]* for some non-zero *i*.

Consider the String *s* with a single Character *𝔟*:sub:`1` *= α[i]*.

    s = α[i]

Clearly, by Definition 1.1.3, *l(s) = 1*. To show that *s* is contained in *α*, a strictly increasing and consecutive function that maps the Characters in *s* to the Characters in *α* must be found. Since *l(s) = 1*, this can be defined simply as,

    f(1) = i

For any value of *i*. Therefore, by Definition 1.1.7,

    α[i] ⊂:sub:`s` α 
    
Since *α* and *i* are arbitary, this can be generalized, 

    ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: α[i] ⊂:sub:`s` α ∎

The next theorem, Theorem 1.2.3, is the direct result of defining String length as the number of non-Empty characters in a String and then defining containment based on String length. Careful inspection of Definition 1.1.7 will show that it depends on a precise notion of String Length. In other words, in the current formal system, containment is derivative of length. The order of definitions and axioms in any formal system of Language cannot be of an arbitary character. There is an inherent hierarchical structure in linguistics that must be captured and formalized in the correct order.

**Theorem 1.2.3**  ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: α[i] ≠ ε

Let *α* be an arbitrary word in **L**, and let *i* be a natural number such that 1 ≤ i ≤ l(α). By the Discovery Axiom W.1, it is known that *l(α) ≠ 0*.

By Definition 1.1.3, the length of a String is the number of non-Empty Characters it contains in its Character-level set representation **Α**. Since *l(α) > 0*, *α* must have at least one non-Empty character.

Since *1 ≤ i ≤ l(α)*, the Character at position *i* in *α*, denoted *α[i]*, exists and is non-Empty, *α[i] ≠ ε*. Since *α* and *i* are arbitrary, this can generalized,

    ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: α[i] ≠ ε ∎

Theorem 1.2.1 - 1.2.3 are the necessary logical pre-conditions for Words to arise from the domain of Strings. In essence, before Language can be distinguished from its uncountably infinite domain, a way of measuring String length must be introduced. This definition must prevent Empty Strings from entering into the Language, which would otherwise allow the annunciation of null content. Then it must be assumed for semantic content to be assigned to a series of concatenated Characters the length of that String must be non-zero. This is the meaning of the first conjunct in the Discovery Axiom W.1.

Language is materially different from its un-structured domain of Strings for this reason. Language does not possess null content. Language is measureable. Words in Language have String Length. Moreover, Words are delimited. In other words, Words are separable, distinct linguistic entities. These facts are guaranteed by the Discovery Axiom W.1 and Theorem 1.2.1 - Theorem 1.2.3. These results provide the canvas upon which the rest of the theory will be drawn.

There may appear to be a contradiction in the results of Theorem 1.1.3, which states the Empty Character is contained in every String, and Theorem 1.2.3, which states no Character in a Word can be the Empty Character. Every Word is a String, by Definition 1.2.2, so the results appear at odds. The solution to this apparent contradiction lies in how Characters and Strings have been formalized as distinct, but interrelated, terms. The contradiction is no longer a contradiction once the distinction between a String being contained in another String and a Character being a constituent element at a specific position with in a String is understood.

The containment relation *ε ⊂*:sub:`s` *s* refers to the Empty Character as a subsequence of *s*. The relation being expressed is about the sequence of Characters, and the Empty sequence is always a subsequence of any other sequence.

Theorem 1.2.3, on the other hand, refers to individual Characters at specific positions within a Word. It is a claim about the elements of the Character-level representation (e.g., the *ⲁ* in (*i*, *ⲁ*) *∈* **Z**).

Inversion
^^^^^^^^^

Before developing the palindromic structure and symmetries in Words and Language, an operation capable of describing this symmetry much be introduced. Informally, the *Inverse* of a String is the reversed sequence of Characters in a String. The goal of this section is to define this notion precisely. In the process, the motivation for this definition as it pertains to Words will be elucidated. 

**Definition 1.2.4: String Inversion** 

Let *s* be a string with length *l(s)*. Then, let *t* be a String with length *l(t)*.
    
*t* is called the Inverse of *s* and is denoted *inv(s)* if it satisfies the following conditions, 

    1. l(t) = l(s) 
    2. ∀ i ∈ N:sub:`l(s)`: t[i] = s[l(s) - i + 1]  ∎

Note the advantage of Character Index notation in stating this definition. The quantification in the second clause of Definition 1.2.4 can be made directly over the natural numbers, rather than the intermediary of the Character level set representation of *t* and *s*.

**Example**

Let *s = "abcde"* (*l(s) = 5*). Then *inv(s) = t = "edcba"*

    t[1] = s[5 - 1 + 1] = s[5] = "e"
    t[2] = s[5 - 2 + 1] = s[4] = "d"
    t[3] = s[5 - 3 + 1] = s[3] = "c"
    t[4] = s[5 - 4 + 1] = s[2] = "b"
    t[5] = s[5 - 5 + 1] = s[1] = "a" ∎

Since every Word is a String, the Inverse of Word is similarly defined, with the additional constraint that *s* belong to a Language **L**, i.e. by adding a third bullet to Definition 1.2.4 with *s ∈* **L**. The Inverse of a Word is easily understood through a few illustrative examples in English. The following table lists some words in English and their Inverses,

| Word | Inverse | 
| ---- | ------- |
| time | emit    |
| saw  | was     |
| raw  | war     |
| dog  | god     |
| pool | loop    |

However, this particular example is (intentionally) misleading. In this example, the Inverse of a word in English is also a word in English. In general, this property is not exhibited by the majority of Words in any Language. In other words, every Word in an Language has an Inverse but not every Inverse Word belongs to a Language. This phenomenon is exemplified in the following table,

| Word | Inverse | 
| ---- | ------- |
| cat  | x       |
| you  | x       |
| help | x       |
| door | x       |
| book | x       |

The intent is to define a class of Words whose elements belong to it if and only if their Inverse exists in the Language. As a first step towards this definition, String Inversion was introduced and formalized. In the next section, String Inversion will provide a subdomain in the domain of discourse over which to quantify the conditions that are to be imposed on the class of *Invertible Words*, i.e. the class of Words whose Inverses are also Words. 

Note, Invertible Words are often termed *semordnilaps* in linguistics. The terminology *invertible* is adopted here to emphasis the structural inversion that is occuring on the Character-level within this class of Words. 

Before defining the class of Invertible Words in the sequel, this section is concluded with theorems that strengthen the definition of String Inversion. These theorems will be used extensively in all that follows.

**Theorem 1.2.4** ∀ s ∈ S: inv(inv(s)) = s

Let *s* be a String with length *l(s)* and Characters *𝔞*:sub:`i`. 

Let *t = inv(s)* with length *l(t)* and Characters *𝔟*:sub:`j`.

By the Definition 1.2.4,

    1. l(t) = l(s)
    2. ∀ i ∈ N:sub:`l(s)`: t[i] = s[l(s) - i + 1]

Now, let *u = inv(t)* with length *l(u)*. Applying Definition 1.2.4 again,

    3. l(u) = l(t)
    4. ∀ j ∈ N:sub:`l(t)`: u[j] = t[l(t) - j + 1]

Since *l(t) = l(s) = l(u)* and **N**:sub:`l(t)` *=* **N**:sub:`l(s)` = **N**:sub:`l(u)`(from step 1, step 3 and by definition of natural numbers), these substitions may be made in step 4,

    5. ∀ j ∈ N:sub:`l(s)`: u[j] = s[l(s) - (l(t) - j + 1) + 1]

Simplifying the index on the right hand side,

    6. ∀ j ∈ N:sub:`l(s)`: u[j] = s[j]

Since *u* and *s* have the same length (*l(u) = l(t) = l(s)*) and the same Characters in the same order (*u[j] = s[j]* for all *i*), by Definition 1.1.4 of String Equality, it can be concluded that *u = s*. Recall that *u = inv(t)* and *t = inv(s)*. Substituting, the desired result is obtained, *inv(inv(s)) = s*. ∎ 

Two versions of Theorem 1.2.5 are given, the first using only the Character-level representation of a String, the second using Character Index notation. This is done to show the two formulations are equivalent, and it is a matter of personal preference which style of notation is employed. Throughout the rest of this work, the Character Index notation is primarily utilized, although there are several proofs that are better served by the Character-level representation.

**Theorem 1.2.5 (Character-level Representation)** ∀ u, t ∈ S: inv(ut) = inv(t)inv(u)

Let **U** be the Character level representation of *u*,

    1. U = (𝔞:sub:`1` , 𝔞:sub:`2` , ..., 𝔞:sub:`l(u)`)

Let **T** be the Character level representation of *t*,

    2. T = (𝔟:sub:`1`, 𝔟:sub:`2` , ... , 𝔟:sub:`l(t)`)

The Character level representation of *ut*, denoted **UT**, is then given by,

    3. UT = (𝔞:sub:`1` , 𝔞:sub:`2` , ..., 𝔞:sub:`l(u)`, 𝔟:sub:`1`, 𝔟:sub:`2` , ... , 𝔟:sub:`l(t)`)

By Definition 1.2.4 of String Inversion, the Character level representation of *inv(ut)* is the reversed sequence of **UT**,

    4. inv(UT) = ( 𝔟:sub:`l(t)`, ..., 𝔟:sub:`2` , 𝔟:sub:`1` , 𝔞:sub:`l(u)`, ..., 𝔞:sub:`2` , 𝔞:sub:`1`)

The Character level representation of *inv(U)*, denoted **inv(U)**,

    5. inv(U) = (𝔞:sub:`l(u)`, ..., 𝔞:sub:`2` , 𝔞:sub:`1`)

The Character-level representation of *inv(t)*, denoted **inv(T)** is 

    6. inv(T) = ( 𝔟:sub:`l(t)`, ..., 𝔟:sub:`2` , 𝔟:sub:`1` )

The Character-level representation of *inv(t)inv(u)* is:

    7. ( 𝔟:sub:`l(t)`, ..., 𝔟:sub:`2` , 𝔟:sub:`1`, 𝔞:sub:`l(u)`, ..., 𝔞:sub:`2` , 𝔞:sub:`1`)

Comparing the results from step 4 and step 7, it can be seen the Character-level representations of *inv(ut)* and *inv(t)inv(u)* are identical.

Therefore, *inv(ut) = inv(t)inv(u)*. ∎

**Theorem 1.2.5 (Character Index Notation)**: ∀ u, t ∈ S: inv(ut) = inv(t)inv(u)

Let *u* and *t* be arbitrary strings in **S**. Let *l(u) = m* and *l(t) = n*. Then, *l(ut) = m + n*, by Definition 1.1.3.

Let *s = ut*. Let *v = inv(s) = inv(ut)*. Let *w = inv(t)inv(u)*.

To prove show the theorem, it must be shown that *v = w*, which means, by Definition 1.1.4, it must be shown that 

    1. l(v) = l(w)
    2. ∀ i ∈ N:sub:`l(v)`: v[i] = w[i] 

By repeated applications of Definition 1.2.4, 

    3. l(v) = l(s) = l(ut) = m + n
    4. l(inv(t)) = l(t) = n
    5. l(inv(u)) = l(u) = m. 

From step 3 and step 4, it follows,
 
    5. l(w) = l(inv(t)inv(u)) = l(inv(t)) + l(inv(u)) = n + m = m + n.

From steps 4 and 5, it follows, 

    6. l(v) = l(w) = m + n.

Now it is to be shown that *v[i] = w[i]* for all *i* in N:sub:`l(v)`. Let *i* be an arbitrary index such that *1 ≤ i ≤ m + n*.

**Case 1**: *1 ≤ i ≤ n*

    a. v[i] = s[l(s) - i + 1] (by Definition 1.2.4)
    b. v[i] = s[m + n - i + 1] (since l(s) = m + n)
    c. v[i] = t[n - i + 1] (since m + n - i + 1 corresponds to an index in t)
    d. v[i] = inv(t)[i] (by Definition 1.2.4)
    e. v[i] = w[i] (since w = inv(t)inv(u))

**Case 2**: *n + 1 ≤ i ≤ m + n*:

    a. v[i] = s[l(s) - i + 1] (by Definition 1.2.4)
    b. v[i] = s[m + n - i + 1] (since l(s) = m + n)
    c. v[i] = u[m - (i - n) + 1] (since m + n - i + 1 corresponds to an index in u)
    d. v[i] = u[m + n - i + 1]
    e. v[i] = inv(u)[i - n] (by Definition 1.2.4)
    f. v[i] = w[i] (since w = inv(t)inv(u))

In both cases, *v[i] = w[i]* for all *i* in N:sub:`l(v)`. Since *l(v) = l(w)*, by Definition 1.1.4 it follows *v = w*. Therefore, 

    7. inv(ut) = inv(t)inv(u).

Since u and t were arbitrary strings, we can generalize:

    8. ∀ u, t ∈ S: inv(ut) = inv(t)inv(u) ∎

The next theorem establishes a brand of *"distributivity"* of String inversion over containment. 

**Theorem 1.2.6** ∀ u, t ∈ S : u ⊂:sub:`s` t ↔ inv(u) ⊂:sub:`s` inv(t) 

This theorem can be stated in natural language as follows: For any two Strings *u* and *t*, *u* is contained in *t* if and only if the Inverse of *u* is contained in the Inverse of *t*.

Let *u* and *t* be arbitrary Strings in **S**.

(→) Assume,

    1. u ⊂:sub:`s` t

By Definition 1.1.7, there exists a strictly increasing and consecutive function *f*: **N**:sub:`l(u)` *→* **N**:sub:`l(t)` such that,

    2. ∀ i ∈ N:sub:`l(u)`: u[i] = t[f(i)]

Let,

    3. v = inv(t)
    4. w = inv(u).

By Definition 1.2.4,

    5. ∀ i ∈ N:sub:`l(u)`: w[i] = inv(u)[i] = u[l(u) - i + 1]
    6. ∀ i ∈ N:sub:`l(t)`: v[i] = inv(t)[i] = t[l(t) - i + 1]

Define a function *g*: **N**:sub:`l(w)` → **N**:sub:`l(v)` as follows,

    7. g(i) = l(t) - f(l(u) - i + 1) + 1

This function maps the Character indices of *w* (the inverse of *u*) to the indices of *v* (the inverse of *t*).

**Increasing** To show *g* is strictly increasing, let

    8. i, j ∈ N:sub:`l(w)`

Such that *i < j*. Since *l(w) = l(u)*,

    9. i, j ∈ N:sub:`l(u)`

Because *f* is strictly increasing, and

    10. l(u) - j + 1 < l(u) - i + 1,

It follows,

    11. f(l(u) - j + 1) < f(l(u) - i + 1)
Therefore,

    12. l(t) - f(l(u) - i + 1) + 1 < l(t) - f(l(u) - j + 1) + 1

which means

    13. g(i) < g(j).

Thus, g is strictly increasing.

**Consecutive** To show *g* is consecutive, let

    14. i ∈ N:sub:`l(w)`

Such that *i < l(w)*. Then,

    15. g(i+1) = l(t) - f(l(u) - (i + 1) + 1) + 1
    16. g(i+1) = l(t) - f(l(u) - i - 1 + 1) + 1

Since f is consecutive, we have:

    17. f(l(u) - i - 1 + 1) = f(l(u) - i) + 1

Then,

    18. g(i+1) = l(t) - (f(l(u) - i) + 1) + 1
    19. g(i+1) = l(t) - f(l(u) - i)
    20. g(i+1) = l(t) - f(l(u) - i + 1) + 1 + 1 - 1
    21. g(i+1) = l(t) - f(l(u) - i + 1) + 1
    22. g(i+1) = g(i) + 1

Thus *g* is consecutive.

**Containment** Now, it must shown be that, 

    23.  ∀ i ∈ N:sub:`l(w)`: w[i] = v[g(i)]

By Definition 1.2.4,

    24. w[i] = u[l(u) - i + 1]

From step 2, it follows,

    25. w[i] = t[f(l(u) - i + 1)]

By definition of *g*,

    26. g(i) = l(t) - f(l(u) - i + 1) + 1

Rearranging,

    27. f(l(u) - i + 1) = l(t) - g(i) + 1

Substituting into step 25,

    28. w[i] = t[l(t) - g(i) + 1]

By Definition 1.2.4 and the definition of v,

    29. v[g(i)] = t[l(t) - g(i) + 1]

Therefore,

    30. w[i] = v[g(i)]

Since this holds for all *i* *∈* **N**:sub:`l(w)`, and g is a strictly increasing and consecutive function, by Definition 1.1.7, it follows,

    31. w ⊂:sub:`s` v

Therefore,

    32. inv(u) ⊂:sub:`s` inv(t)

(←) Assume

    1. inv(u) ⊂:sub:`s` inv(t)

By Theorem 1.2.4,

    2. inv(inv(u)) = u
    3. inv(inv(t)) = t

Therefore, using the result just proved in the (→) direction, it can be said since

    4. inv(u) ⊂:sub:`s` inv(t)

This implies,

    5. inv(inv(t)) ⊂:sub:`s` inv(inv(u))

Substituting in steps 2 and 3,

    6. t ⊂:sub:`s` u

Since both directions of the implication hold, it follows,

    7. ∀ u, t ∈ S: u ⊂:sub:`s` t ↔ inv(u) ⊂:sub:`s` inv(t) ∎

The next theorem establishes the *transivity* of containment over Strings. 

**Theorem 1.2.7** ∀ t, u, v ∈ S : (t ⊂:sub:`s` u) ∧ (u ⊂:sub:`s` v) → (t ⊂:sub:`s` v) 

This theorem can be stated in natural language as follows: For any Strings *t*, *u*, and *v* in **S**, if *t* is contained in *u* and *u* is contained in *v*, then *t* is contained in *v*.

Let *t*, *u*, and *v* be arbitrary Strings in **S** such that both of the following expressions are true,

    1. t ⊂:sub:`s` u
    2. u ⊂:sub:`s` v

By Definition 1.1.7 and step 1, there exists a strictly increasing and consecutive function *f*: **N**:sub:`l(t)` → **N**:sub:`l(u)` such that,

    3. ∀ i ∈ N:sub:`l(t)`: t[i] = u[f(i)]

Similarly, by Definition 1.1.7 and step 2, there exists a strictly increasing and consecutive function *g*: **N**:sub:`l(u)` → N:sub:`l(v)` such that:

    4. ∀ j ∈ N:sub:`l(u)`: u[j] = v[g(j)]

Define a new function *h*: **N**:sub:`l(t)` *→* **N**:sub:`l(v)` as the composition of *f* and *g*,

    5. ∀ j ∈ N:sub:`l(t)`: h(i) = g(f(i))

**Increasing** Let 

    6. i, j ∈ N:sub:`l(t)` 
    
Such that *i < j*. Since *f* is strictly increasing, 

    7. f(i) < f(j) 

Since *g* is strictly increasing, 

    8. g(f(i)) < g(f(j))
    
Therefore, 

    9. h(i) < h(j)
    
And *h* is strictly increasing.

**Consecutive** Let 

    10. i ∈ N:sub:`l(t)` 
    
Such that *i < l(t)*. Since *f* is consecutive, 

    11. f(i+1) = f(i) + 1 
    
Since *g* is consecutive, following from step 11,

    12. g(f(i+1)) = g(f(i) + 1) = g(f(i)) + 1
    
Therefore, 

    13. h(i+1) = h(i) + 1, and h is consecutive.

**Containment** Let 

    14. i ∈ N:sub:`l(t)` 
    
Then, by step 3

    15. t[i] = u[f(i)]

Since *f*: **N**:sub:`l(t)` *→* **N**:sub:`l(u)`, it follows that for all 

    16. ∀ i ∈ N:sub:`l(t)`: f(i) ∈ N:sub:`l(u)`

By step 16 and step 4,

    17. u[f(i)] = v[g(f(i))]

By definition of *h*,

    18. v[g(f(i))] = v[h(i)]

Therefore, 

    19. ∀ i ∈ N:sub:`l(t)`: t[i] = v[h(i)]

Since *h* is a strictly increasing and consecutive function from **N**:sub:`l(t)` to **N**:sub:`l(v)`, and *t[i] = v[h(i)]* for all *1≤ i ≤ l(t)*, by Definition 1.1.7,

    20. t ⊂:sub:`s` v.

Since *t*, *u*, and *v* were arbitrary Strings, this can be generalized as,

    21. ∀ t, u, v ∈ S : (t ⊂:sub:`s` u) ∧ (u ⊂:sub:`s` v) → (t ⊂:sub:`s` v) ∎

Phrases
^^^^^^^

While the analyis has not yet introduced the notion of Sentences into the formal system (see Section II), an operation will now be introduced that allows Words to be ordered into Phrases and then concatenated into Strings. This new operation will be important when String Inversion is applied to the sentential level of the formal system, allowing the conditions for a Sentence Inversion to be precisely specified.

The placement of Definition 1.2.5 and Definition 1.2.6 is somewhat arbitary. There are valid arguments to be made for placing these definitions after the concepts of Sentence and Word Index notation have been introduced in Section II. However, since the operation of *Delimitation* and *Limitations* to be expounded immediately are essentially an operation defined on the domain of Strings which yields as a result another String, i.e. Delimitation and Limitation are closed with respect to Strings, the definitions are made here, to highlight the derivative notions (Inversion, Delimitation and Limitations) which can be built on top of the primitive notion of concatenation.

**Definition 1.2.5: Phrase**

Let *n* be a fixed, non-zero natural number, *n ≥ 1*. A Phrase of Word Length *n* from Language **L**, denoted **P**:sub:`n`, is defined as an ordered sequence of *n* (not necessarily distinct) Words,

    P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

where each *α*:sub:`i` *∈* **L**. If *i* is *1 ≤ i ≤ n*, P:sub:`n`(i) denotes the Word *α*:sub:`i` at index *i*, so that **P**:sub:`n` may be rewritten, 

    P:sub:`n` = (P:sub:`n`(1), P:sub:`n`(2), ... , P:sub:`n`(n))

When *n = 0*, **P**:sub:`0` is defined as the empty sequence (). ∎

In order to establish some properties of Phrases, Delimitations and Limitations , a symbol for representing the range of a Phrase **P**:sub:`n` over a Language **L** is now defined.

**Definition 1.2.6: Lexicon**

Let *n* be a fixed natural number. We define a Language's *n*:sup:`th` Lexicon, denoted **X**:sub:`L`(*n*), as the set of all Phrases of length *n* formed from Words in **L**,

    Χ:sub:`L`(n) = { P:sub:`n` | P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`) ∧ ∀ i ∈ N:sub:`n`: α:sub:`i` ∈ L } ∎

Some of the later theorems in this work will require quantifying over Phrases in a Language's *n*:sub:`th` Lexicon, so notation is introduced for Phrase Variables,

    1. Phrase Variables (*p*, *q*, *r*): The lowercase English letters *p*, *q*, *r* are reserved for representing indeterminate Phrases of a Language's *n*:sup:`th` Lexicon.
   
Because Phrases are ordered sequences of Words, the Phrase Variable *p(i)* will denote, exactly like the Definition of a Phrase, the Word at index *i* for *1 ≤ i ≤ n*.

Using these pair of definitions for Phrases and Lexicons and their associated terminology, the operation of *Delimitation* is now defined over Phrases of fixed Word Length *n* in Definition 1.2.7.

**Definition 1.2.7: Delimitation**

Let *p* be a Phrase from a Language **L**'s *n*:sup:`th` Lexicon,

    p = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

The *Delimitation* of *p*, denoted *DΠ*:sub:`i=1`:sup:`n` *p(i)*, is defined recursively as:

    1. Empty Clause: DΠ:sub:`i=1`:sup:`0` p(i) = ε
    2. Basis Clause (n = 1): DΠ:sub:`i=1`:sup:`1` p(i) = α:sub:`1`
    3. Recursive Clause (n > 1): DΠ:sub:`i=1`:sup:`n` p(i) = (DΠ:sub:`i=1`:sup:`n-1` p(i))(σ)(α:sub:`n`) ∎

**Definition 1.2.8: Limitation**

Let *p* be a Phrase from a Language **L**'s *n*:sup:`th` Lexicon,

    p = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

The *Limitation* of *p*, denoted *LΠ*:sub:`i=1`:sup:`n` *p(i)*, is defined recursively as:

    1. Empty Clause: LΠ:sub:`i=1`:sup:`0` p(i) = ε
    2. Basis Clause (n = 1): LΠ:sub:`i=1`:sup:`1` p(i) = α:sub:`1`
    3. Recursive Clause (n > 1): LΠ:sub:`i=1`:sup:`n` p(i) = (LΠ:sub:`i=1`:sup:`n-1` p(i))(α:sub:`n`) ∎

The key difference between Definition 1.2.7 and Definition 1.2.8 is the presence of the Delimiter in the Recursive Clause. In other words, a Delimitation inserts a Delimiter between the Words it is concatenating, while a Limitation is simply a shorthand simply for concatenating a sequence of Words.

Before proving the existence of Delimitations and Limitations, an example of how they are constructed recursively is given below.

**Example**

Let 

    P:sub:`3` = ("mother", "may", "I")

Apply Definition 1.2.7 to construct the Delimitation of **P**:sub:`3`. The Basis Step yields,

    1. n = 1: DΠ:sub:`i=1`:sup:`1` α:sub:`i` = "mother" 

And then the Delimitation can be built up recursively using the Recursive Step repeatedly,

    2.  n = 2: DΠ:sub:`i=1`:sup:`2` α:sub:`i` = (DΠ:sub:`i=1`:sup:`1` α:sub:`i`)(σ)("may")= ("mother")(σ"may") = "mother"σ"may"
    3.  n = 3: DΠ:sub:`i=1`:sup:`3` α:sub:`i` = (DΠ:sub:`i=1`:sup:`2` α:sub:`i`)(σ)("I") = ("mother"σ"may")(σ"I") = "mother"σ"may"σ"I"

So the Delimitation of the Phrase is given by,

    4. Π:sub:`i=1`:sup:`3` α:sub:`i` = "mother may I" 

Similarly, the Limitation can be constructed recursive from the same Basis Step using Definition 1.2.8,

   5. n = 2: LΠ:sub:`i=1`:sup:`2` α:sub:`i` = (LΠ:sub:`i=1`:sup:`1` α:sub:`i`)("may")= ("mother")("may") = "mothermay"
   6. n = 3: LΠ:sub:`i=1`:sup:`3` α:sub:`i` = (LΠ:sub:`i=1`:sup:`2` α:sub:`i`)("I") = ("mothermay")("I") = "mothermayI" ∎

From this example, it should be clear what the Delimitation and Limitation operations represent within the formal system. Delimitation is a method of constructing a Sentence-like (see Section II.III for the formal difference between a Delimitation and Sentence) String from a sequence of words, while a Limitation is shorthand for iterated concatenation over a sequence of Words.

Note the previous example may be misleading in one important respect. A Delimitation is not necessarily "grammatical" or "meaningful". It may be a String of semantic Words without an accompanying interpretation on the Sentence level of the linguistic hierarchy. 

However, as the next theorems shows, the result of a Delimitation or Limitation is unique.

**Theorem 1.2.8** ∀ n ∈ ℕ, ∀ p ∈ Χ:sub:`L(n)` ∃! s ∈ S: s = DΠ:sub:`i=1`:sup:`n` p(i)

This theorem can be stated in natural language as follows: For every natural number n, and for every Phrase **P**:sub:`n` in the *n*:sup:`th` Lexicon of **L**, there exists a unique string *s* in **S** such that *s* is the Delimitation of **P**:sub:`n`.

Let *n* be an arbitrary natural number, and let **P**:sub:`n` be a Phrase of Word Length *n* in Language **L** from the Language's *n*:sup:`th` Lexicon, **X**:sub:`L`*(n)*,

    q. P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

The theorem will be proved using induction.

**Base Case (n = 1)**

By Definition 1.2.7,
    
    1. DΠ:sub:`i=1`:sup:`1` P:sub:`n(i)` = α:sub:`1`

Since *α*:sub:`1` is a word in **L** (by Definition 1.2.6 of Lexicon), it is also a String in S (by Definition 1.2.2). Thus, there exists a String *s = α*:sub:`1` such that 

    3. s = DΠ:sub:`i=1``:sup:`1` P:sub:`n(i)`.

Since the base case of Delimitation is defined as simple equality, the string s must be unique.

**Inductive Hypothesis**

Assume that for some *k ≥ 1*, there exists a unique string *s*:sub:`k` such that 

    4. s:sub:`k` = DΠ:sub:`i=1`:sup:`k` P:sub:`n(i)`

To complete the induction, it must be shown that there exists a unique string *s*:sub:`k+1` such that,
 
    5. s:sub:`k+1` = DΠ:sub:`i=1`:sup:`k+1` P:sub:`n(i)`

By Definition 1.2.7, 

    6. DΠ:sub:`i=1`:sup:`k+1` P:sub:`n(i)` = (DΠ:sub:`i=1`:sup:`k` P:sub:`n(i)`)(σ)(α:sub:`k+1`)

By inductive hypothesis,
    
    7. DΠ:sub:`i=1`:sup:`k` P:sub:`n(i)` = s:sub:`k`
    
Thus, *s*:sub:`k` is unique. Since *α*:sub:`k+1` is a Word in **L** (by the definition of **Χ**:sub:`L`*(n+1)*), it is also a unique String in S.

The concatenation of *s*:sub:`k`, *σ*, and *α*:sub:`k+1` is a unique string (by the Definition 1.1.1 of Concatenation and Definition 1.1.4 of String Equality).

Therefore, *s*:sub:`k+1` = (*s*:sub:`k`)(σ)(*α*:sub:`k+1`) is a unique string.

By induction, for every natural number *n*, and for every phrase **P**:sub:`n` in **Χ**:sub:`L(n)`, there exists a unique string *s* in **S** such that *s = DΠ*:sub:`i=1`:sup:`n` P:sub:`n(i)`. ∎

**Theorem 1.2.9** ∀ n ∈ ℕ, ∀ p ∈ Χ:sub:`L(n)` ∃! s ∈ S: s = LΠ:sub:`i=1`:sup:`n` p(i)

The proof of this theorem is almost exactly identical to Theorem 1.2.8, with the exception there is no Delimiter in step 6. ∎

Section I.III: Word Classes 
---------------------------

It will be necessary to define special classes of Words in a Language to properly describe the Language's palindromic structure. These classes, especially the class of Invertible Words, will be used extensively in the next sections. Reflective Words, however, will play a crucial role in this work's climatic theorem. 

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

From this list, it should be clear what is meant by the notion of *reflective*. Reflective Words are those Words whose meaning is unchanged by a String Inversion. However, the semantic content that is preserved under inversion is not the primitive property that primarily explains this invariance. The invariance of the semantic content under inversion is the result of Character level symmetries. 

Rather than attempt to define Reflective Words as the class of Words that are their own Inverses, a different approach will be taken that highlights the Character level symmetries that exist in these class of Words. It will then be proven the class of Words which satisfy this definition are exactly those Words that are their own Inverses.

**Definition 1.3.1: Reflective Words** 

The set of Reflective Words **R** is defined as the set of *α* which satisfy the open formula,

    α ∈ R ↔ ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1] ∎

A Word *α* will be referred to as *reflective* if it belongs to the class of Reflective Words. 

The following theorem is an immediate consequence of Definition 1.3.1 and Definition 1.2.4.

**Theorem 1.3.1** ∀ α ∈ L: α ∈ R ↔ α = inv(α)

In natural language, this theorem can be stated as: A Word in a Language is Reflective if and only if it is its own Inverse.

(→)  Assume *α ∈ R*. By Definition 1.3.1, 

    1. ∀ i ∈ N:sub:`l(α)`:  α[i] = α[l(α) - i + 1] 

Let *β = inv(α)*. By the Definition 1.2.4,

    2. l(β) = l(α)
    3. ∀ i ∈ N:sub:`l(α)`: ( β[i] = α[l(α) - i + 1] )

Substituting the property of Reflective Words from step 1 into step 3,

    4.  4. ∀ i ∈ N:sub:`l(α)`: β[i] = α[i]

Since *β[i] = α[i]* for all *i ∈* **N**:sub:`l(α)`, and both strings have the same length, by Definition 1.1.4, it can be concluded that *α = β*. Therefore the desired result is obtained, *α = β = inv(α)*.

(←) Assume *α = inv(α)*.  By Definition 1.2.4 of String Inversion,

    1. l(α) = l(inv(α))
    2. ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1]

But step 2 is exactly the definition of Reflective Words, so by Definition 1.3.1, *α ∈* **R** ∎ 

Invertible Words 
^^^^^^^^^^^^^^^^

As discussed previously, the concept of *invertible* is exemplified in pairs of English words, such as *"parts"* and *"strap"*, or *"repaid"* and *"diaper"*. If a Word can be inverted, this is not simply a syntactic operation, but a semantic one as well. An *Invertible Word* is a Word whose inverse is part of the same Language **L** as the original Word. This notion can now be made more precise with the terminology introduced in prior sections.

**Definition 1.3.2: Invertible Words** 

Let *α* be any Word in a Language **L**. Then the set of Invertible Words **I** is defined as the set of *α* which satisfy the open formula,

    α ∈ I ↔ inv(α) ∈ L ∎

A Word *α* will be referred to as *invertible* if it belongs to the class of Invertible Words.

Definition 1.3.2 is immediately employed to derive the following theorems.

**Theorem 1.3.2** ∀ α ∈ L: α ∈ I ↔ inv(α) ∈ I

(→) Assume *α ∈* **I**. By Definition 1.3.2,

    1. inv(α) ∈ L
    
Consider *inv(α)*. To show that it's invertible, it must be shown,

    2. inv(inv(α)) ∈ L. 

By Theorem 1.2.4,

    3. inv(inv(α)) = α
    
Since it is known *α ∈ L*, it follows,

    4. inv(inv(α)) ∈ L  
    
By the Definition 1.3.2, 

    5. inv(α) ∈ I
    
Therefore, *inv(α)* is also an Invertible Word. 

(←) Assume *inv(α)* is a Word in Language L and *inv(α) ∈* **I**. Then by Definition 1.3.2,

    1. inv(inv(α)) ∈ L

By Theorem 1.2.4,

    2. α ∈ L

To show *α* is invertible, it must be shown *inv(α) ∈* **L**, but this is exactly what has been assumed, so it follows immediately. 

Therefore, putting both directions of the equivalence together and generalizing over all Words in a Language, 

    ∀ α ∈ L: α ∈ I ↔ inv(α) ∈ I ∎ 

**Theorem 1.3.3** R ⊆ I

Assume *α ∈* **R**. By Definition 1.3.2,

    1. ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1]

Let *β = inv(α)*. By Definition 1.2.4,

    2. l(β) = l(α)
    3. ∀ j ∈ N:sub:`l(α)`: β[j] = α[l(α) - j + 1]

Substituting step 1 into step 3,

    4. ∀ i ∈ N:sub:`l(α)`:  β[j] = α[j]

Since both strings have the same length and the same Characters in the same order, by Definition 1.1.4, 

    5. α = β = inv(α)

By assumption, *α* is a Word from Language **L** that belongs to **R**. From step 5, this implies *inv(α)* is also part of the Language **L**. By Definition 1.3.2, this implies,

    6. α ∈ I 

In other words, 

    ∀ α ∈ L : α ∈ R → α ∈ I 

But this is exactly the definition of the subset relation in set theory. Therefore,

    R ⊆ I ∎ 

In the context of (potentially) infinite sets such as **L** and **S**, *"even"* and *"odd"* refer to whether the set can be partitioned into two disjoint subsets of equal cardinality.

    1. Even Cardinality: An infinite set has even cardinality if it can be put into a one-to-one correspondence with itself, with each element paired with a distinct element.
    2. Odd Cardinality: An infinite set has odd cardinality if, after pairing each element with a distinct element, there is one element left over.

The set of non-reflective Invertible Words, **I** - **R** (where "-" represents the operation of set differencing), always has even cardinality because each word can be paired with its distinct inverse. The overall cardinality of **I** then depends on whether the set of Reflective Words, **R**, adds an "odd" element or not. This idea is captured in the next theorem.

**Theorem 1.3.4** If | R | is even, then | I | is even. If | R | is odd, then | I | is odd.

Partition the set of Invertible Words, **I**, into two disjoint subsets,

    1. **R**: The set of Reflective Words.
    2. **I** - **R**: The set of Invertible Words that are not Reflective.

For every word *α* in **I** *-* **R**, its inverse, *inv(α)*, is also in **I** *-* **R**. Furthermore, they form a distinct pair *(α, inv(α))*. This is because *α* is invertible but not reflective, so *α ≠ inv(α)*.

Since the elements of **I** *-* **R** can be grouped into distinct pairs, the cardinality | I - R | must be even.

The total number of Invertible Words is the sum of the number of Reflective Words and the number of Invertible Words that are not Reflective,

    3. | I | = | R | + | I - R |

Let | R | be even. Since | I - R | is always even, and the sum of two even numbers is even, | I | must also be even.

Let | R | be odd. Since | I - R | is always even, and the sum of an odd number and an even number is odd, | I | must also be odd. ∎ 

Section II: Sentences
=====================

The work so far has formally constructed a system for representing the first two levels of artifacts from a natural language, Characters (Alphabet) and Words (Language), without appealing to their interpretation in any way except insofar that it takes a stance on the *existence* of an interpretation. As the analysis moves up the chain of linguistic artifacts to the next highest level, Sentences (Corpus), it is tempting to start incorporating semantic features into the theory. However, the objective is to derive palindromic conditions independent of a particular semantic interpretation. Therefore, as the analysis proceeds, special care will be given to the definition of a *Sentence* and its *Corpus*.

Section II.I: Definitions
-------------------------

The next level of the semantic hierarchy will now be constructed. Many of the definitions made in this subsection will not be referenced until the final section of this work, when the fundamental properties of Palindromes are established. They are given here, due to the natural progression of concept formation dictating they be defined after the notion of Sentence and Corpus is introduced.

Corpus
^^^^^^

The entire system so far constructed relies on the domain of **S**, the set of all Strings that can be formed from an Alphabet of Characters **Σ**. Attention has been confined to those entities that satisfy the Discovery Axiom W.1.

In other words, the definitions and theorems so far introduced deal with linguistics entities that do not possess a Delimiter Character. Delimiters will be of central importance in describing palindromic structures, because Delimiters play a central role in the definition of the linguistic entity that will ultimately allow a palindrome to be rigorously defined, a *Sentence*. With that in mind, the concepts and definitions that pave the way to an explication of *Sentence* start with the definition of a *Corpus*.

**Definition 2.1.1: Corpus** The Corpus of Language **L** is denoted by **C**:sub:`L`. The Corpus set represents a collection of grammatically valid and semantically meaningful Strings. ∎

From the definition, it can easily be seen the Corpus of a Language is a subset of the set of all possible Strings, **S**

   C:sub:`L` ⊂ S 

This aligns with the idea that the domain of entities in this formal system is defined either as a type of *element* of **S** or a type of *subset* of **S**.

Sentence
^^^^^^^^

Before proceeding with the definition of Sentences, some notation is introduced,

    1. Sentences (*ᚠ*, *ᚢ*, *ᚦ*, ... ): Anglo-Saxon (*Old English*) Runes represent a Sentence. Subscripts will occassionally be used in conjunction with Anglo-Saxon letters to denote Sentences, (*ᚠ*:sub:`1`, *ᚠ*:sub:`2`, ... ). 
    2. Sentential Variables (*ζ*, *ξ*): The lowercase Greek letter Zeta and Xi are reserved for indeterminate Sentences, i.e. Sentential Variables. Subscripts will occassionally be used in conjunction with Zeta to denote Sentential Variables, (*ζ*:sub:`1`, *ζ*:sub:`2`, ...)
    
**Definition 2.1.2: Sentence** A Sentence in Language **L** is an element of its Corpus. ∎

    ᚠ ∈ C:sub:`L`

From Definition 2.1 and Definition 2.2, it follows that a Sentence is a String,

    ᚠ ∈ S

It should be stressed, as had been made clear in previous comments, that Characters, Words and Sentences in the current formulation are elements of the same underlying set, the set of all Strings. This connection in the domain of Characters, Words and Sentences is what will allow the analysis to begin to construct the outline of palindromic structures in a Language and Corpus. To reiterate this hierarchy and precisely state how all the entities in this formal system are related,

    1. Strings: ⲁ, α, ζ
    2. Sets: Σ, L, C:sub:`L`
    3. Character Membership: ⲁ ∈ Σ
    4. Word Membership: α ∈ L
    5. Sentence Membership: ζ ∈ C:sub:`L`

To clarify the relationship between Strings, Characters, Alphabets, Words, Languages, Sentences and Corpus in plain language,

    1. All Characters, Words and Sentences are Strings.
    2. All Alphabets, Languages and Corpuses are sets of Strings.
    3. All Characters belong to an Alphabet.
    4. All Words belong to a Language.
    5. All Sentences belong to a Corpus.

This web of categorical relations represents the hierarchy of linguistic entities within the formal system. 

Notation
^^^^^^^^

In Section I.I, notation was introduced for representing Strings a a sets of ordered Characters. This form of representation provided a formal method for specifying various syntactical conditions and properties of Strings and Words. In particular, this method allowed a formal definition of String Length.  

In a similar way, a method of representing Sentences as sets will now be constructed to enrich the symbolic form given to a Sentence in this formal system. Since all Sentences are Strings, all Sentences have Character-level set or sequence representations, by the Emptying Algorithm. The Discovery Axiom W.1 allows the definition of an algorithm to parse the Words of a Sentence based purely on the presence of Delimiters. 

**Definition 2.1.3: Word-Level Set Representation**

Let *ζ* be a Sentence in a Corpus C:sub:`L`. Let **Ζ** be the Character-level set representation of *ζ*, i.e. an ordered sequence of Characters from the alphabet **Σ**. 

The Word-level set representation of *ζ*, denoted by **W**:sub:`ζ`, is defined as the ordered set of words obtained by splitting **Ζ** at each Delimiter Character, *σ*. Formally, **W**:sub:`ζ` is constructed using the *Delimiting Algorithm*.

**Algorithm 2: Delimiting Algorithm**

Consider a particular Sentence in the Corpus, *ᚠ*. The Delimiting Algorithm consists of initializing the values of several local variables and then iterating over the Character level set representation of a Sentence *ᚠ* until the Characters have been exhausted. The exact details are given below.

The Delimiting Algorithm takes a Sentence *ᚠ* from a Corpus as input, and applies the Emptying Algorithm to it to generate a sequence of non-Empty Characters. It then initializes a set **W**:sub:`ᚠ` and index for the Words it will add to **W**:sub:`ᚠ` . The algorithm iterates the index and constructs the Word-level representation by removing the Delimiter character. The Delimiting Algorithm is formally defined below.

.. topic:: Algorithm Delimit(t: String)
    
    # Input: A string t
    # Output: An ordered set W representing the Word-level set representation of t

    # Initialization
    ## Character-level representation of ᚠ
    1. ᚠ ← Empty(ᚠ)
    ## Initialize empty set to hold Word-level representation of ᚠ
    2. W ← ∅
    ## Initialize a counter j for Words
    3. j ← 1
    ## Initialize a counter i for characters
    4. i ← 1
    ## Initialize an empty string
    5. t ← ε

    # Iteration
    1. While i ≤ l(ᚠ):
   
        a. If ᚠ[i] ≠ σ:

            i. t ← (t)(ᚠ[i])

        b. Else:

            i. If l(t) > 0:

                1. Apply Basis Clause of Definition 1.1.1 to t.
                2. W ← W ∪ { (j, t) }
                3. j ← j + 1
   
            ii. t ← ε

        c. i ← i + 1

    # Finalization
    2. If l(t) > 0:
        a. W ← W ∪ { (j, t) }
        b. j ← j+1
    3. Return W ∎

Note the String which is initialized to hold the Sentence Characters in step *5* is set to an initial value of the Empty Character in the Initialization Block. Also note, the application of the Basis Clause in step *1.b.i.1* ensures this Empty Character is removed after each Word has been processed. This is required, because otherwise the last Word in the Word-level representation will have an Empty Character, which violates the results of Theorem 1.2.3.

The essence of the Delimiting Algorithm lies in the interplay of the Discovery Axiom W.1 and Definition 2.1.2 of a Sentence as a semantic String. In other words, by Definition 2.1.2 and by Definition 1.2.2, all Sentences and Words must be semantic. The only feature that differentiates them in their *"semanticality"* is the presence of a Delimiter (from a syntactical perspective, at any rate). Therefore, by the Discovery Axiom W.1, the Words which a Sentence contains must be exactly those Strings which are separated by the Delimiter Character. 

This formulation has the advantage of not taking a stance on the semantics of a particular language. It allows for the discovery of Words in a Language through the simple boundary of Delimiters within the Sentences of its Corpus. 

The following examples show how to apply the Delimiting Algorithm to construct the Word-level representation of a Sentence. 

**Example**

Let *ᚠ = (𝔞𝔟)(σ)(ε)(σ)(𝔟𝔞)*. Note *l(ᚠ) = 6*.

**Initialization**

During initialization, the Character-level set representation of *ᚠ* is constructed with Definition 1.1.2 using the Emptying Algorithm.

   1. **ᚠ** = (𝔞,𝔟,σ,σ,𝔟,𝔞)
   2. W:sub:`ᚠ` = ∅
   3. j = 1

**Iteration**

The following list shows the result of the algorithm after each iteration,

   1. j = 2, i = 4, t = 𝔞𝔟, W:sub:`ᚠ` = { (1, 𝔞𝔟) }
   2. j = 2, i = 5, t = σ, W:sub:`ᚠ` = { (1, 𝔞𝔟) }
   3. j = 3, i = 7, t = 𝔟𝔞, W:sub:`ᚠ` = { (1, 𝔞𝔟), (2, 𝔟𝔞) }

At which point *i > l(ᚠ)*, so the algorithm halts and returns,

    W:sub:`ᚠ` = { (1, 𝔞𝔟), (2, 𝔟𝔞) } ∎

**Example** 

Let *ᚠ = "The cat meows"*. Then the Character level representation of *ᚠ* is given by, 

    **ᚠ** = { (1, "T"), (2, "h"), (3,"e"), (4,σ), (5,"c"), (6,"a"), (7,"t"), (8,σ), (9,"m"), (10,"e"), (12,"o"), (13,"w"), (14,"s") }.

Then, applying the *Delimiting Algorithm*, its Word-level representation is constructed, 

    **W**:sub:`ᚠ` = { (1, "The"), (2, "cat"), (3, "meows") }. ∎

Similar to the Character-level set representation of String, where the Character position is encoded into the first coordinate, the Word-level set representation of a String encodes the presence of Delimiters through its first coordinate. Once Word Length is defined in the next section, a notational shortcut similar to Character Index Notation defined in Definition 1.1.5 will be use this method of Sentence representation to simplify many of the upcoming proofs.

There is a subtle assumption being made in the idea a Sentence can be reduced to a sequence of ordered Characters that deserves special mention, as this perhaps reasonable assumption implicitly elides a question of much greater complexity regarding where precisely the semantic information of a Sentence resides. To see what is meant by this, consider the three sentences from Latin,

- Puella canem videt. (Girl dog sees)
- Canem puella videt. (Dog girl sees)
- Videt puella canem. (Sees girl dog)

In some respect, all three of these sentences could be considered the *same* sentence, as the order of the words is not the primary bearer of semantic information. While the order of words lends itself to the *voice* and *tone* of the sentence, the meaning of the sentence does not primarily emerge through tis word order. Similar cases exist in any natural language that uses declensions to modify the syntactic function of words, such as Greek. 

The current formal system treats these sentences in Latin as distinct Sentences. If the Latin sentences in this example are to be identified as representatives of the same semantic *"token"*, this cannot occur on the Sentence level of this formal system's linguistic hierarchy. This example suggests Sentences are not the final level of the hierarchy, and that to find the source of meaning in a Sentence, another level must be constructed on top of it capable of identifying these different manifestations as the same *"token"*.

This example does not invalidate the analysis, but it does introduce subtlety that must be appreciated. These concerns must be kept in mind while the formal notion of a Sentence is developed.

Length
^^^^^^

The notion of String Length *l(s)* was introduced in Section I.I as a way of measuring the number of non-Empty Characters in a String *s*. In order to describe palindromic structures, a new notion of length will need introduced to accomodate a different *"spatial"* dimension in the domain of a Language and its Corpus: *Word Length*.

Intuitively, the length of a Sentence is the number of Words it contains. Since there is no analogue of Discovery Axiom W.1 for Sentences (nor should there be), this means Sentences may contain Delimiter Characters. The Words of a Language are separated by Delimiters in the Sentences of its Corpus. 

Definition 2.1.3 provide way of dispensing with the Delimiter Character in Sentences, while still retaining the information it provides about the demarcation of Words through the first coordinate of a Sentence's Word-level representation. With the Word-level set representation of Sentence in hand, it is a simple matter to define the notion of Word Length in the formal system.

**Definition 2.1.4: Word Length**

Let *ζ* be a Sentence in a **C**:sub:`L`. Let **W**:sub:`ζ` be the Word-level set representation of *ζ*, as defined in Definition 2.1.3. The Word Length of the Sentence *ζ*, denoted by *Λ(ζ)*, is defined as the cardinality of the set **W**:sub:`ζ`,

    Λ(ζ) = | W:sub:`ζ` | ∎

**Example**

Consider the Sentence *ᚠ = "the dog runs"*. Its Character-level set representation would be given by,

    **ᚠ** = { (0,"t"), (1,"h"), (2,"e"), (4,σ), (5, "d"), (6, "o"), (7, "g"), (8, σ), (9, "r"), (10, "u"), (11,"n"), (12,"s") }

Its Word-level set representation would be given by,

    W:sub:`ᚠ` = { (1, "the"), (2, "dog"), (3, "runs") }

Therefore, the length of the sentence is:

    Λ(ᚠ) = | W:sub:`ᚠ` | = 3

Note, in this example, 

    l(ᚠ) = 12 ∎

This example demonstrates the essential difference in the notions of length that have been introduced. It is worthwhile to clarify the distinction between these two conceptions. 

Let *t* be a String with Character-level representation **T** and Word-level representation **W**:sub:`t`. The hierarchy of its "spatial" dimensions is given below, in order of greatest to least (this fact is proven in Section II of the Appendix with Theorem A.4.8). Terminology is introduced in parenthesis to distinguish these notions of length,

   - l(t) (String Length): The number of non-Empty Characters contained in a String.
   - Λ(t) (Word Length): The number of Words contained in a String 

Note the first level is purely syntactical. Any String *t* will have a String Length *l(t)*. However, not every String possesses Word Length, *Λ(s)*. Word Length contains semantic information. While the presence of Word Length does not necessarily mean the String is semantically coherent (see Definition 2.2.1 for a precise definition of *semantic coherence*), e.g. "asdf dog fdsa", Word Length does signal an *extension* of Strings into the semantic domain.

Word Length can be used to simplify some of the complex notation the formal system has accumulated. Similar to the Character Index Notation, a way of referring to Words in Sentences within propositions without excessive quantification is now introduced through Word Index notation.

**Definition 2.1.5: Word Index Notation**

Let *ζ* be a Sentence with Word level set representation, **W**:sub:`ζ`,

    W:sub:`ζ` = (α:sub:`1`, α:sub:`2`, ... , α:sub:`Λ(ζ)`)

Then for any *j* such that *1 ≤ j ≤ Λ(ζ)*, the Word at index *j*, denoted ζ{j}, is defined as the Word which satisfies the following formula,

    ∀ (j, α:sub:`j`) ∈ W:sub:`ζ`: ζ{j} = α:sub:`j` . ∎

The following theorem uses this notation to proves an intuitive concept: the total number of Characters in all of the Words in a Sentence must exceed the number of Words in a Sentence (since there are no Words with a negative amount of Characters). 

**Theorem 2.1.1** ∀ ζ ∈ C:sub:`L`:  ∑:sub:`j=1`:sup:`Λ(ζ)` l(ζ{j}) ≥ Λ(ζ)

This theorem can be stated in natural language as follows: For any sentence *ζ* in Corpus **C**:sub:`L`, the sum of the String Lengths of the Words in *ζ* is always greater than the Word Length of *ζ*.

Assume ζ ∈ C:sub:`L`. Let *j* be a natural number such that *1 ≤ j ≤ Λ(ζ)*

For each ordered Word ζ{j} in ζ, its String Length *l(ζ{j})* must be greater 0 by the Discovery Axiom W.2 and Definition 1.1.3. Therefore, since each Word contributes at least a String Length of 1, the sum of the String Lengths *l(ζ{j})* must be greater than or equal to *Λ(ζ)*. ∎

Word Length and Word Index Notation can be used to define the notion of *Boundary Words*, which will be utilized in the main results about Palindromes. 

To illustrate another simplification effected by Index notation in formal proofs about Language, consider how laborious the proof of the following Theorem 2.1.2 would be without the ability to refer to Characters embedded in Strings and Words embedded in Sentences through Index notation. 

**Theorem 2.1.2** ∀ ζ, ξ ∈ C:sub:`L`: Λ(ζξ) ≤ Λ(ζ) + Λ(ξ)

Let *ζ* and *ξ* be arbitrary Sentences in **C**:sub:`L`. Let **W**:sub:`ζ` and **W**:sub:`ξ` be the Word-level representations of *ζ* and *ξ*, respectively. By Definition 2.1.4, 

    1. Λ(ζ) = | W:sub:`ζ` |
    2. Λ(ξ) = | W:sub:`ξ` |.

Let *ζξ* be the concatenation of *ζ* and *ξ*. When *ζ* is concatenated to *ξ*, there are several possible cases to consider. 

   - ζ[l(ζ)] = σ, ξ[1] = σ
   - ζ[l(ζ)] = σ, ξ[1] ≠ σ
   - ζ[l(ζ)] ≠ σ, ξ[1] = σ
   - ζ[l(ζ)] ≠ σ, ξ[1] ≠ σ

Case 1 - 3: In each of theses cases, the Words of *ζ* and the Words of *ξ* are still separated by at least one Delimiter. Therefore, no new Word is formed during concatenation, and the words in *ζξ* are simply the words of *ζ* followed by the words of *ξ*. Therefore, 

    3. Λ(ζξ) = Λ(ζ) + Λ(ξ).

Case 4: ζ[l(ζ)] ≠ σ, ξ[1] ≠ σ. 

In this case, a new Word may be formed during concatenation, but only if *ζ{Λ(ζ)}* concatenated with *ξ{1}* belongs to L (i.e., *(ζ{Λ(ζ)})(ξ{1})* if it is a compound Word). Let *t* be the String such,

    4. t = (ζ{Λ(ζ)})(ξ{1})

This result can be expressed,

    5. t ∈ L → Λ(ζξ) = Λ(ζ) + Λ(ξ) - 1.
    6. t ∉ L → Λ(ζξ) = Λ(ζ) + Λ(ξ).

In all cases, 

    Λ(ζξ) ≤ Λ(ζ) + Λ(ξ).

Since *ζ* and *ξ* were arbitrary sentences, this can be generalized,

    ∀ ζ, ξ ∈ C:sub:`L`: Λ(ζξ) ≤ Λ(ζ) + Λ(ξ) ∎

Word Length is fundamentally different to String Length with respect to the operation of concatenation. In Theorem 1.1.1, it was shown String Length sums over concatenation. Theorem 2.1.2 demonstrates the corresponding property is not necessarily true for Word Length. This is an artifact of the ability of concatenation to destroy semantic content.

Section II.II: Axioms 
----------------------

In Section I, the first three axioms of the formal system were introduced. Now that definitions and notations have been introduced for Sentence and Corpus, the axioms may be expanded to further refine the character of the system being built. The Equality, Character and Discovery Axiom are reprinted below, so they may be considered in sequence with the other axioms.

Note the Discovery Axiom has been revised to employ Character Index notation. 

**Axiom C.0: The Equality Axiom**

    1. ∀ ⲁ ∈ Σ: ⲁ = ⲁ
    2. ∀ ⲁ, ⲃ ∈ Σ: ⲁ = ⲃ ↔ ⲃ = ⲁ
    3. ∀ ⲁ, ⲃ ∈ Σ: (ⲁ = ⲃ ∧ ⲃ = ⲅ) → (ⲁ = ⲅ) ∎
   
**Axiom C.1: The Character Axiom**

    ∀ ⲁ ∈ Σ: ⲁ ∈ S ∎

**Axiom W.1: The Discovery Axiom ** 

    ∀ α ∈ L: [ (l(α) ≠ 0) ∧ (∀ i ∈ N:sub:`l(α)`: α[i] ≠ σ) ] ∎

**Axiom S.1: The Duality Axiom**

    ( ∀ α ∈ L: ∃ ζ ∈ C:sub:`L``: α ⊂:sub:`s` ζ ) ∧ ( ∀ ζ ∈ C:sub:`L`: ∃ α ∈ L: α ⊂:sub:`s` ζ ) ∎

**Axiom S.2: The Extraction Axiom**

    ∀ ζ ∈ C:sub:`L` : ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ L ∎

Two new axioms, the Duality Axiom S.1 and the Extraction Axiom S.2, have been added to the formal system to finalize its core assumptions. It is worth taking the time to analyze the structure, however minimal, these axioms imply must exist in any Language. It should be re-iterated that no assumptions have been made regarding the semantic content of a Language or its Corpus, so any insight that arises from these axioms is due to inherent linguistic structures (assuming these axioms capture the nature of real language). 

To briefly summarize the axioms previously introduced: The system *"initializes"* with the assumption of an equality relation and the selection of an Alphabet **Σ**. The Character Axiom ensures the domain of all Strings is populated. The Discovery Axiom ensures Words only traverse the set of Strings which do not contain Delimiters. With these axioms, still nothing has been said about *what* a Word is, except that it possesses a semantic character. To re-iterate, a Language and Corpus are fixed on top of the domain of all Strings outside of the system. 

The new axioms introduced in the formal system begin to characterize the syntactical properties of the next level in the lingustic hierarchy, while still maintaining their ambivalence on the semantic content contained within their respective categories.

The Duality Axiom S.1 bares a striking resemblance to the idea of *surjection* in real analysis. Recall, a function *f*: *X* → *Y* is called *surjective* if,

    ∀ y ∈ Y : ∃ x ∈ X : f(x) = y

Meaning, every element in the co-domain is mapped to at least one element in the domain. 

In a sense, the Duality Axiom S.1 asserts a type of *"double-surjectivity"* exists between the domain of Words and the co-domain of Sentences.  In plain language, the Duality Axiom asserts for every Word *α* in the Language **L**, there exists a sentence *ζ* in the Corpus **C**:sub:`L` such that *α* is contained in *ζ*, and for every Sentence *ζ* in the corpus **C**:sub:`L`, there exists a word *α* in the language **L** such that *α* is contained in *ζ*. 

However, there is a key difference between the notion of *surjection* in real analysis and the notion captured in the Duality Axiom S.1. Containment is not a strict equality relation. By Definition 1.1.6 and Definition 1.1.7, containment reduces to the existence of a mapping between Characters in different Strings. Due to the Discovery Axiom W.2, with the exception of Sentences consisting of a Single Word, a Word is contained in a Sentence but a Sentence is not contained in a Word. 

More plainly, the Duality Axiom S.1 states a Word cannot exist in a Language without being included in a Sentence of the Corpus, and a Sentence cannot exist in a Corpus without including a Word from the Language. This Axiom captures an inextricable duality between the metamathematical concepts of Sentence and Word, and the concepts of Language and Corpus: one cannot exist without implying the existence of the other. Words and Sentences do not exist in isolation. A Language and its Corpus require one another. 

The Extraction Axiom S.2 further strengthens the relationship that exists between a Corpus and Language. It states every Word in the Sentence of a Corpus must be included in a Language. This idea of being able *extract* the Words of a Language from a Sentence is captured in the terminology introduced in Definition 2.2.1 directly below. 
 
**Definition 2.2.1: Semantic Coherence** 

A Sentence *ᚠ* is *semantically coherent* in a Language **L** if and only if **W**:sub:`ᚠ` only contains words from Language **L**. 

A Corpus C:sub:`L` is *semantically coherent* in a Language **L** if and only if the Word-level set representation of all its Sentences are semantically coherent. ∎

The first theorems proven using these new axioms are analogous versions of the Word theorems Theorems 1.2.1 - 1.2.3 for Sentences. These theorems, like their Word counterparts, represent the logical pre-conditions for Sentences to arise in the domain of all Strings. 

**Theorem 2.2.1** ∀ ζ ∈ C:sub:`L`: l(ζ) ≠ 0

Let *ζ* be an arbitrary sentence in C:sub:`L`, and let *i* be a natural number such that *1 ≤ i ≤ l(ζ)*.

By the first conjunct of the Discovery Axiom W.1 and the second conjunct of the Duality Axiom S.2,

    1. ∃ α ∈ L: α ⊂:sub:`s` ζ 
    2. ∀ α ∈ L: l(α) ≠ 0

Therefore, by Definition 1.1.7, there exists a strictly increasing and consecutive function *f* such that,

    3. ∀ i ∈ N:sub:`l(α)`: α[i] = ζ[f(i)] 
    
By Theorem 1.2.3, 

    4. ∀ i ∈ N:sub:`l(α)`: α[i] ≠ ε

Therefore, combining steps 3 and 4,

    5. ∀ i ∈ N:sub:`l(α)`: ζ[f(i)] ≠ ε

Since, by step 2, *l(α) ≠ 0*, there must be some non-zero *i* that satisfies step 5. Therefore, there is at least one non-Empty Character in *ζ*, namely, *ζ[f(i)]*. The theorem is then proven by applying Definition 1.1.3 and Theorem 2.2.1,

    6. l(ζ) ≠ 0 ∎

**Theorem 2.2.2** ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`l(ζ)`: ζ[i] ⊂:sub:`s` ζ

Let *ζ* be an arbitrary sentence in C:sub:`L`, and let *i* be a natural number such that *1 ≤ i ≤ l(ζ)*. By Theorem 2.2.1 and Definition 1.1.3, there must be at least one non-Empty Character in *ζ*. Let *ζ[i]* be a non-Empty Character in *ζ*. Consider the string *s* consisting of the single character *ζ[i]*, *s = ζ[i]*. Clearly, by Definition 1.1.3, 

    1. l(s) = 1

Define a function *f: {1} → {i}* such that *f(1) = i*. This function is strictly increasing and consecutive. By Definition 1.1.6 and Definition 1.1.7, since there exists a strictly increasing and consecutive function *f* from the indices of *s* to the indices of *ζ*, and since the Character at position 1 in *s* is the same as the Character at position i in *ζ* (both are *ζ[i]*), we can conclude that *s* is contained in *ζ*. Therefore, 

    2. ζ[i] ⊂:sub:`s` ζ

Since *ζ* and *i* were arbitrary, this can be generalized, 

    3. ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`l(ζ)`: ζ[i] ⊂:sub:`s` ζ ∎

**Theorem 2.2.3** ∀ ζ ∈ C:sub:`L` : ∀ i ∈ N:sub:`l(ζ)`:  ζ[i] ≠ ε

Let *ζ* be an arbitrary sentence in **C**:sub:`L`, and let *i* be a natural number such that *1 ≤ i ≤ l(ζ)*. By Theorem 2.2.2, 

    1. ∀ i ∈ N:sub:`l(ζ)`: ζ[i] ⊂:sub:`s` ζ

By Definition 1.1.3, String Length is the number of non-Empty Characters in a String's Character-level set representation. Since *l(ζ) > 0*, *ζ* must have at least one non-Empty character.

Since *1 ≤ i ≤ l(ζ)*, the Character at position *i* in *α*, denoted *ζ[i]*, exists and is non-Empty by Definition 1.1.2. Therefore, 

    2. *ζ[i] ≠ ε*. 

Since *ζ* and *i* are arbitrary, this can generalized,

    ∀ α ∈ L : ∀ i ∈ N:sub:`l(ζ)`: ζ[i] ≠ ε ∎

**Theorem 2.2.4** ∀ ζ ∈ C:sub:`L`: Λ(ζ) ≥ 1

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. By the second conjunct of the Duality Axiom S.1,

    1. ∃ α ∈ L: α ⊂:sub:`s` ζ

By the first conjunct of the Discovery Axiom W.1,

    2. l(α) ≠ 0

Therefore, by Definition 1.1.7, there exists an *f* such that, 

    3. ∀ i ∈ N:sub:`l(α)`: α[i] = ζ[f(i)]

By Theorem 1.2.3, 

    4. ∀ i ∈ N:sub:`l(α)`: α[i] ≠ ε

Therefore, combining step 3 and 4,

    5. ∀ i ∈ N:sub:`l(α)`: ζ[f(i)] ≠ ε

Since *l(α) ≠ 0*, there is at least one non-Empty Character in *ζ* and therefore, by Definition 1.1.3,

    6. Λ(ζ) ≥ 1

Generalizing this over the Corpus,

    7. ∀ ζ ∈ C:sub:`L`: Λ(ζ) ≥ 1 ∎

**Theorem 2.2.5** ∀ ζ ∈ C:sub:`L`: ζ = DΠ:sub:`i=1`:sup:`n` ζ{i}

This theorem can be stated in natural language as follows: Every Sentence in the Corpus is the Delimitation of its own Words.

Assume 

    ζ ∈ C:sub:`L`

By Definition 2.1.3,

    W:sub:`ζ` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`Λ(ζ)`) 
    
where

    α:sub:`i` ∈ L.

By Definition 1.2.5, the sequence **W**:sub:`ζ` forms a phrase P:`sub:Λ(ζ)` of length *Λ(ζ)* where 

   ∀ i ∈ N:sub:`Λ(ζ)`: P:sub:`Λ(ζ)`(i) = α:sub:`i` 
    
By Definition 1.27, the Delimitation of P:sub:`Λ(ζ)` is,

    DΠ:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`Λ(ζ)`)

The delimitation reconstructs the original sentence ζ by including the delimiters between words. Therefore:

    ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i)

By Definition 2.1.5, 

    ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} = α:sub:`i`

Therefore,

    ζ = DΠ:sub:i=1:sup:`Λ(ζ)` ζ{i}

Since ζ was an arbitrary Sentence in the Corpus, this can be generalized,

    ∀ ζ ∈ C:sub:`L`: ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i} ∎

Section II.III: Sentence Classes 
--------------------------------

As the astute reader has no doubt surmised at this point, the foundational operation that defines a palindromic structure in linguistics is *inversion* (i.e. a method of reversal). What may not yet be clear is how this operation of inversion propagates through the hierarchy of entities defined over its domain. As this necessary structure of interdependent inversions between hierarchical layers becomes apparent, the mathematical description of a Palindrome will seen to be a *"recursion of inversions"*.

Theorems 2.3.9 - 2.3.11 of this subsection mark the first notable results obtained from the formal system. Their empirical truth in natural language represents confirmation of the formal system's construction. These theorems demonstrate the Character-level symmetries required by invertibility propagate up through the Word-level of linguistics and manifest in conditions that must be imposed on the Word-level structure of an Invertible Sentence.

Admissible Sentences
^^^^^^^^^^^^^^^^^^^^

The notion of an *Admissible Sentence* is required to prevent a certain class of Sentence inversions from invalidating the symmetry conditions of Palindromes derived in Section III. 

To see what is meant by this concept of *admissibility*, consider the English sentence,

    ᚠ = "strap on a ton".

The Inverse of this sentence, *inv(ᚠ)*, is *semantically coherent* (Definition 2.2.1). By this it is meant every word in its inversion is part of the English language,

    inv(ᚠ) = "not a no parts"

However, this is not enough to ensure *inv(ᚠ)* is part of the Corpus, as is apparent. *Semantic coherence* is a necessary but not sufficient condition for the Inverse of a Sentence to remain in the Corpus. In order to state the requirement that must be imposed on a Sentence to remain *admissible* after inversion, the concept of Delimitation introduced in Definition 1.2.7 must now be leveraged. 

**Definition 2.3.1: Admissible Sentences**

Let *p* be any Phrase from a Language's *n*:sup:`th` Lexicon **X**:sub:`L`(*n*). A String *t* is said to belong to the class of *Admissible Sentences of Word Length n* in Language **L**, denoted **A**(*n*), if it satisfies the following open formula

    t ∈ A(n) ↔ (∃ p ∈ Χ:sub:`L`(n): t = DΠ:sub:`i=1`:sup:`n` p(i)) ∧ (t ∈ C:sub:`L`) ∎

The notion of *admissibility* is a faint echo of *"grammaticality"*. As inversion is studied in the sentential level of the linguistic hierarchy, it is no longer permitted to ignore semantics in its entirety. Instead, semantics ingresses into the system as implicit properties the extensionally identified Sentences must obey. Before discussing this at greater length, several theorems are proved about classes of Admissible Sentences.

**Theorem 2.3.1** A(n) ⊆ C:sub:`L`

Let *t* be an arbitrary String such that *t* *∈* **A**(*n*). By Definition 2.3.1, this implies, *t* *∈* **C**:sub:`L`. Therefore,

    1. t ∈ A(n) → t ∈ C:sub:`L`

This is exactly the set theoretic definition of a subset. Thus,

    2. A(n) ⊆ C:sub:`L` ∎

Theorem 2.3.1 is the formal justification for quantifying Sentence Variables over the set of Admissible Sentences (i.e. all Admissable Sentences are in the Corpus), as in the following theorem.

**Theorem 2.3.2** ∀ ζ ∈ A(n): Λ(ζ) = n

Let *ζ* be an arbitrary sentence in **A**(*n*). By Definition 2.3.1, if *ζ* *∈* **A**(*n*), then there exists a Phrase *p* *∈* **Χ**:sub:`L`(*n*) such that 

    1. ζ ∈ C:sub:`L` ∧ ζ = DΠ:sub:`i=1`:sup:`n` p(i)

By Definition 1.2.5 and 1.2.6, a phrase *p* in **Χ**:sub:`L(n)` is an ordered sequence of *n* words such that *α*:sub:`i` *∈* **L**,

    p = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

By Definition 1.2.7, the Delimitation of *p* is given by,

    DΠ:sub:`i=1`:sup:`n` p(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`n`)

In other words, the Delimitation of *p* (which is equal to *ζ*) explicitly constructs a String with *n* Words separated by Delimiters.

By Definition 2.1.4, the Word Length *Λ(ζ)* is the number of Words in *ζ*. Since *ζ* is formed by limiting a Phrase with *n* Words, and the Delimitation process doesn't add or remove Words, the Word Length of *ζ* must be *n*. Therefore, 

    Λ(ζ) = n.

Since *ζ* was an arbitrary sentence in **A**(*n*), this can generalize as,

    ∀ ζ ∈ A(n): Λ(ζ) = n ∎

**Theorem 2.3.3** ∀ ζ ∈ C:sub:`L`: ζ ∈ A(Λ(ζ))

Let ζ be an arbitrary sentence in C:sub:`L`. By Definition 2.1.3, *ζ* has a Word-level representation,

    1. W:sub:`ζ` = (α:sub:`1`, α:sub:`2`, ... , α:sub:`Λ(ζ)`) 
    
Where each *α*:sub:`i` *∈* **L**. By Definition 1.2.5, the sequence (*α*:sub:`1`, *α*:sub:`2`, ... , *α*:sub:`Λ(ζ)`) forms a phrase **P**:sub:`Λ(ζ)` of length *Λ(ζ)* where P:sub:`Λ(ζ)`(i) = *α*:sub:`i` for all *i*, *1 ≤ i ≤ Λ(ζ)*.

By Definition 1.2,6, since **P**:sub:`Λ(ζ)` is a phrase of length *Λ(ζ)* and all its Words belong to L (by semantic coherence), then,

    2. P:sub:`Λ(ζ)` ∈ Χ:sub:`L`(Λ(ζ)).

By Definition 1.2.7, the Delimitation of P:sub:`Λ(ζ)` is:

    3. DΠ:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`Λ(ζ)`)

The Delimitation *DΠ*:sub:`i=1`:sup:`Λ(ζ)` **P**:sub:`Λ(ζ)`(*i*) reconstructs the original sentence *ζ*, including the Delimiters between Words. Therefore,

    4. ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i)

By Definition 2.3.1, a String *t* is an Admissible Sentence of Word Length *n* (*t* *∈* **A**(*n*)) if and only if there exists a phrase *p* *∈* **Χ**:sub:`L`(*n*) such that,

    5. t = DΠ:sub:`i=1`:sup:`n` p(i)
    6. t ∈ C:sub:`L`

By Definition 2.3.1, since the conjunction of the three facts is true,

    7. ζ ∈ C:sub:L
    8. ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i)
    9. P:sub:`Λ(ζ)` ∈ Χ:sub:`L`(Λ(ζ)) 
    
It follows from step 7 - step 9, *ζ* *∈* **A**(*Λ(ζ)*). Since *ζ* was an arbitrary sentence in C:sub:`L`, this can generalize as,

    ∀ ζ ∈ C:sub:L: ζ ∈ A(Λ(ζ)) ∎

**Theorem 2.3.4** ∀ ζ ∈ C:sub:`L`: ∃ p ∈ X:sub:`L`(Λ(ζ)): ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` p(i)

Let *ζ* be an arbitrary sentence in C:sub:`L`. By Definition 2.1.3, *ζ* has a Word-level representation,

    W:sub:`ζ`` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`Λ(ζ)`) 
    
Where each *α*:sub:`i` *∈* **L**.

By Definition 1.2.5, the sequence (*α*:sub:`1`, *α*:sub:`2`, ... , *α*:sub:`Λ(ζ)`) forms a Phrase **P**:sub:`Λ(ζ)` of Word Length *Λ(ζ)* where **P**:sub:`Λ(ζ)`(i) = *α*:sub:`i`` for all *i*, *1 ≤ i ≤ Λ(ζ)*.

By Definition 1.2.6, since **P**:sub:`Λ(ζ)` is a Phrase of Word Length *Λ(ζ)* and all its words belong to **L**, then,

    P:sub:`Λ(ζ)` ∈ Χ:sub:`L(Λ(ζ))`

By Definition 1.2.7, the Delimitation of **P**:sub:`Λ(ζ)` is,

    DΠ:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`Λ(ζ)`)

The Delimitation *DΠ*:sub:`i=1`:sup:`Λ(ζ)` **P**:sub:`Λ(ζ)`(i) reconstructs the original Sentence ζ, including the Delimiters between Words. Therefore:

    ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i)

It has been shown that for an arbitrary sentence *ζ* *∈* **C**:sub:`L`, there exists a Phrase *p* (specifically, **P**:sub:`Λ(ζ)`) in **Χ**:sub:`L`(Λ(ζ)) such that,
 
    ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` p(i). 
    
Therefore,

    ∀ ζ ∈ C:sub:`L`: ∃ p ∈ Χ:sub:`L`(Λ(ζ)): ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` p(i) ∎

The condition of *admissibility*, as will be seen in Theorem 2.3.11, prevents the *"inversion propagation"* from being a purely syntactical operation. The Inverse of a Sentences must also be Admissible in the Corpus in order to be considered an Invertible Sentence (Definition 2.3.2 in the next section). This represents a rupture or division from the realm of syntax not seen at the Word level of the linguistic hierarcy when considering the operation of inversion. In order to fully specify the conditions for Sentence invertibility, one must be able to elaborate on what it means to call a Sentence *"admissible"*; in other words, there must be grammatical rules that identify an inverted Sentence as belonging to the Corpus over and above the syntactical conditions that are imposed by invertibility.

However, this does not mean *"grammaticality"* is equivalent to *"admissibility"*. As the final section of the work will make clear, there are possible avenues available to formal analysis for parsing the concept of *"admissibility"* into finer partitions such as *"syntactical admissibility"* and *"semantic admissiblity"*. In this way, the origin of meaning in a Sentence can be narrowed down by filtering out the syntactical considerations.

Invertible Sentences
^^^^^^^^^^^^^^^^^^^^

Similarly to the progression of Words and their related concepts in the previous section, a special class of Sentences will now be classified according to their syntactical properties. In the study of palindromic structures, the notion of *Invertible Sentences* is essential. The definition, as is fitting in a work focused on palindromes, will mirror Definition 1.3.2 of an *Invertible Word*.

The notion of Invertible Sentences will first be defined extensionally, and then clarified heuristically. The following definition and theorem mirror the mechanics of Definition 1.3.2 and Theorem 1.3.2 almost exactly.

**Definition 2.3.2: Invertible Sentences** 

Let *ζ* be any Sentence in from a Corpus **C**:sub:`L`. Then the set of Invertible Sentences **K** is defined as the set of *ζ* which satisfy the open formula,

    ζ ∈ K ↔ inv(ζ) ∈ C:sub:`L`

A Sentence *ζ* will be referred to as *invertible* if it belongs to the class of Invertible Sentences. ∎

This definition is immediately employed to derive the following theorems,

**Theorem 2.3.5** ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ inv(ζ) ∈ K

Let *ζ* be any Sentence from Corpus **C**:sub:`L`.

(→) Assume ζ ∈ K

By Definition 2.3.2, the inverse of *ζ* belongs to the Corpus

    1. inv(ζ) ∈ C:sub:`L`

To show that inv(ζ) is invertible, it must be shown that,

    2. inv(inv(ζ)) ∈ C:sub:`L`

From Theorem 1.2.4, for any string *s*, 

    3. inv(inv(s)) = s.  

By Definition 2.1.1,

    1. ζ ∈ S

Where **S** is the set of all Strings. Therefore, it follows, 

    5. inv(inv(ζ)) = ζ.

From step 1 and step 5, it follows, 

    6. inv(inv(ζ)) ∈ C:sub:`L`

By Definition 2.3.2, this implies,

    7. inv(ζ) ∈ K.

(←) Assume inv(ζ) ∈ K

By Definition 2.3.2, 
    
    8. inv(inv(ζ)) ∈ C:sub:`L`

Applying Theorem 1.2.4,

    9. inv(inv(ζ)) = ζ.

From step 8 and step 9, it follows, 

    10. ζ ∈ C:sub:`L`

By Definition 2.3.2, it follows,

    11. ζ ∈ K. 

Putting both direction of the equivalence together, the theorem is shown,

    12. ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ inv(ζ) ∈ K ∎

**Theorem 2.3.6** ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → ζ ∈ C:sub:`L`

Let *ζ* be any Sentence from Corpus **C**:sub:`L` such that *inv(ζ) ∈ K*. Then, by Definition 2.3.2,

    1. inv(inv(ζ)) ∈ C:sub:`L`

By Theorem 1.2.4,

    2. inv(inv(ζ)) = ζ

Therefore, combining step 1 and step 2,

    3. ζ ∈ C:sub:`L` 

It follows, 

    4. ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → ζ ∈ C:sub:`L` ∎

The notion of Invertible Sentences is not as intuitive as the notion of Invertible Words. This is due to the fact the condition of *invertibility* is not a weak condition; indeed, Sentences that are not invertible far outnumber Sentences that are invertible in a given Language (for all known natural languages, at any rate; it is conceivable a purely formal system with no semantic content or general applicability could be constructed with invertibility in mind). 

To see how strong of a condition invertibility is, the author challenges the reader to try and construct an invertible sentence in English (or whatever their native tongue might be). Section IV contains a list of Invertible Words and Reflective Words. These can be used as a "palette" for the exercise. The exercise is worthwhile, because it forces the reader to think about the mechanics of sentences and how a palindrome resides in the intersection of semantics and syntax.  

Consider the following examples phrases from English,

- no time
- dog won 
- not a ton 

All of these phrases may be *inverted* to produce semantically coherent phrases in English, 

- emit on
- now god
- not a ton 

Note the last item in this list is an example of what this work has termed a Perfect Palindrome. These examples were specially chosen to highlight the connection that exists between the class of Perfect Palindromes and the class of Invertible Sentences. It appears, based on this brief and circumstantial analysis, that *Perfect Palindromes* are a subset of a larger class of Sentences, namely, Invertible Sentences.

Due to the definition of Sentences as semantic constructs and the definition of Invertible Sentences as Sentences whose Inverses belong to the Corpus, this means Invertible Sentences are exactly those Sentences that maintain *semantic coherence* (Definition 2.2.1) and *admissibility* (Definition 2.3.1) under inversion. In order for a Sentence to be invertible it must possess symmetry on both the Character-level and the Word-level, while maintaining a semantic structure at the Sentence level that accomodates this symmetry. This connection between the symmetries in the different linguistic levels of an Invertible Sentence will be formalized and proven by the end of this subsection.

**Theorem 2.3.7** ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ ∈ K → inv(ζ){i} ∈ L

Let *ζ* be a Sentence from Corpus **C**:sub:`L`. Assume *ζ* *∈* **K** . By Definition 2.3.2,

    1. inv(ζ) ∈ C:sub:`L`

By the Extraction Axiom S.2,

    2. ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} ∈ L 
 
Therefore, 

    3. ζ ∈ K → inv(ζ){i} ∈ L 

Since *ζ* was arbitrary, this can be generalized over the Corpus,

    4. ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ ∈ K → inv(ζ){i} ∈ L ∎

The next theorem shows how the inversion "distributes" over the Words of a Delimited Sentence.

**Theorem 2.3.8** ∀ ζ ∈ C:sub:`L`: inv(DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) = DΠ:sub:`i=1`:sup:`Λ(ζ)` inv(ζ{Λ(ζ) - i + 1})

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. Let *n = Λ(ζ)*. By Definition 2.1.4, this is the Word Length of *ζ*.  Let *s* denote the deDelimitation of *ζ* as follows:

    1. s = DΠ:sub:`i=1`:sup:`n` ζ{i} = (ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{n})

By Theorem 1.2.5, for any two Strings *u* and *t*, *inv(ut) = inv(t)inv(u)*. Apply this property repeatedly to construct *inv(s)*,

    2. inv(s) = inv((ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{n}))

Which reduces to,

    3. inv(s) = (inv(ζ{n}))(inv(σ))(inv(ζ{n-1}))(inv(σ)) ... (inv(ζ{2}))(inv(σ))(inv(ζ{1}))

Since σ is a single character, inv(σ) = σ,

    4. inv(s) = (inv(ζ{n}))(σ)(inv(ζ{n-1}))(σ) ... (σ)(inv(ζ{2}))(σ)(inv(ζ{1}))

Note that the right-hand side now has the form of a Delimitation, but with the order of Words reversed and each Word inverted.

Re-index the terms on the right-hand side to match the form of the Delimitation definition, Definition 1.2.7. Let *j = n - i + 1*. Then, as *i* goes from 1 to *n*, *j* goes from *n* to 1,

    5. inv(s) = (inv(ζ{j:sub:`n`}))(σ)(inv(ζ{j:sub:`n-1`}))(σ) ... (σ)(inv(ζ{j:sub:`2`}))(σ)(inv(ζ{j:sub:`1`}))

Where j:sub:`i` is obtained by simply substituting *n-i+1* for j. Using the Definition of DeDelimitation, the right-hand side becomes,

    6. inv(s) = DΠ:sub:`j=1`:sup:`n` inv(ζ{n - j + 1})

Recall that *s = DΠ*:sub:`i=1`:sup:`n` *ζ{i}*. Substitute this back into the equation and re-index the right-hand side for consistency to get,

    7. inv(DΠ:sub:`i=1`:sup:`n` ζ{i}) = DΠ:sub:`i=1`:sup:`n` inv(ζ{n - i + 1})

Since *ζ* was an arbitrary sentence, this can be generalized,

    8. ∀ ζ ∈ C:sub:`L`: inv(DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) = DΠ:sub:`i=1`:sup:`Λ(ζ)` inv(ζ{Λ(ζ) - i + 1}) ∎

As noted in previous aside, the condition of Invertibility is strong. While the Inverse of every Sentence is defined in the domain of Strings, an Inverse Sentence does not necessarily belong to the Corpus of its uninverted form. Therefore, when a Sentence is Invertible, it will exhibit syntactical symmetries at not just the Character level, but also at the individual Word level. Before moving onto to the last batch of theorems in this section, a digression into their motivation is in order, as it will help highlight the interplay of syntactic symmetries that give rise to palindromes.

Consider the Sentences from the English language, *ᚠ = "this is a test"*, *ᚢ = "live on"*,* and *ᚦ = "step on no pets"*. Their Character-level representations would be,

    **ᚠ** = ("t", "h", "i", "s", σ, "i", "s", σ, "a", σ, "t", "e", "s", "t")

    **ᚢ** = ("l", "i", "v", "e", σ, "o", "n")

    **ᚦ** = ("s", "t", "e", "p", σ, "o", "n", σ, "n", "o", σ, "p", "e", "t", "s")

The Character-level representation of their Inverses, would be,

    **inv(ᚠ)** = ("t", "s", "e", "t", σ, "a", σ, "s", "i", σ, "s", "i", "h", "t")

    **ing(ᚢ)** = ("n", "o", σ, "e", "v", "i", "l")

    **inv(ᚦ)** = ("s", "t", "e", "p", σ, "o", "n", σ, "n", "o", σ, "p", "e", "t", "s")

In the case of *ᚠ*, it's *inv(ᚠ)* is not a Sentence in the Corpus, since none of the Words in it belong to the Language (English). Notice that the Delimiters (*σ*) still appear at the same indices in both *ᚠ* and *inv(ᚠ)*, just in reversed order. In *ᚠ*, the Delimiters are at indices 4, 7, and 9. In *inv(ᚠ)*, the Delimiters are at indices 9, 7, and 4 (counting from the beginning of the reversed string). So, while the sequence of Delimiters is reversed, their positions relative to the beginning and end of the String remain the same. Since the Delimiting Algorithm identifies Words based on Delimiter positions, this means application of the algorithm to the reversed Character-level representation, results in the same limiting of the linguistic "*entities*" (Strings) which correspond to Words, but in reversed order and inverted.

In the case of *ᚢ*, it's *inv(ᚢ)* belongs to the Corpus, since all of its Words belong to the Language (English) and have semantic coherence in *ᚢ*, and the inverted Sentence is admissible. This means *ᚢ* belongs to the class of Invertible Sentences in English. Take note, none of the Words that belong to *ᚢ* (or more precisely, to one of the ordered pairs of **W**:sub:`ᚢ`) belong to *inv(ᚢ)* (or more precisely, to one of the ordered pairs of **W**:sub:`inv(ᚢ)`). However, there does appear to be a relationship between the Words which appear in *ᚢ* and *inv(ᚢ)*, namely, they must be Invertible. The Word *"live"* inverts into *"evil"*, while *"on"* inverts into *"no"*. In other words, based on this preliminary heuristic analysis, if a Sentence is to be Invertible, the Words which belong to it must belong to the class of Invertible Words **I**.

In the case of *ᚦ*, a similar situation is found. Each Word in *ᚦ* is Invertible and pairs with its Inverse Word in *inv(ᚦ)*, e.g. *"pets"* and *"step"* form an Invertible pair, etc. This means, for the same reasons as *ᚢ*, *ᚦ* belongs to the class of Invertible Sentences. However, there is a symmetry embodied in *ᚦ* over and above the pairing of its constituent Words into Invertible pairs. Not only is *inv(ᚦ)* a Sentence in the Corpus, but it's equal to *ᚦ* itself. Indeed, *ᚦ* belongs to a special class of English sentences: Palindromes. 

Note, in order for the Sentence to invert, i.e. the case of *ᚢ* and *ᚦ*, the order of the Words in the inverted Sentences must be the reversed order of the inverted Words in the uninverted Sentence. In other words, the inversion defined on the String *"propagates"* up through the levels of the semantic hierarchy and manifests at each level in the form of a semantic inversion. This will be discussed in greater detail after the next theorems are established.

These last theorems encapsulate these important properties of Invertible Sentences. When Palindromes are formally defined in the next section, these theorems will be used extensively to prove the main results of this work. 

**Theorem 2.3.9** ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ ∈ K → inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})

Let *ζ* be an arbitrary Invertible Sentence in **C**:sub:`L` for *i* such that *1 ≤ i ≤ Λ(ζ)*. By Definition 2.2.2, 

    1. inv(ζ) ∈ C:sub:`L`.

By the Extraction Axiom S.2, 

    2. ζ{i} ∈ L. 

By Definition 1.3.2, a Word *α* is invertible if and only if both *α* and its inverse, *inv(α)*, are in **L**,

    3. α ∈ I ↔ inv(α) ∈ L

Therefore, since **L** is closed under inversion for Invertible Words , 

    4. inv(ζ{i}) ∈ L.

*inv(ζ)* can be constructed by concatenating the inverses of the words in ζ in reverse order, with delimiters inserted appropriately. Since by step 1 *inv(ζ)* is a Sentence in the Corpus, **W**:sub:`inv(ζ)` can be constructed by the Delimiting Algorithm (Definition 2.1.3). 

    5. W:sub:`inv(ζ)` = (inv(ζ{Λ(ζ)}), inv(ζ{Λ(ζ)-1}), ..., inv(ζ{1}))

By Definition 2.1.9, 

    6. inv(ζ){i} = inv(ζ{Λ(ζ)-i+1})

Generalization: Since ζ and i were arbitrary, this can be generalized,

    7. ∀ ζ ∈ C:sub:L: ζ ∈ K → ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1}) ∎

A brief interjection is necessary to discuss the significance of Theorem 2.3.8. The result shown in Theorem 2.3.8 is a direct result of the *"propagation of inversion"* mentioned in the introduction to this subsection.

As Theorem 1.3.1 showed, Definition 1.3.1 of Reflective Words is equivalent to a definition that simply requires *α* satisfy the String equality relation, 

    α = inv(α)

Another way of stating this is through logical equivalence, as Theorem 1.3.2 shows,

    α ∈ L ↔ inv(α) ∈ L
    
In turn, Definition 1.2.4 of String Inversion states in order for this to be the case, it must also be the case its Character satisfy,

    α[i] = α[l(α) - i + 1] 

In other words, a Word is its own Inverse exactly when its Characters are in inverted orders. 

In a similar fashion, as Theorems 2.3.3 and 2.3.4 demonstrate by way of syllogism, a Sentence in a Corpus is invertible if its Inverse belongs to the Corpus,

    ζ ∈ C:sub:`L` ↔ inv(ζ) ∈ C:sub:`L`

Theorem 2.3.8 *"propagates"* the Character-level symmetries up through the Words in the Sentence, by stating the Words in an invertible Sentence must be inverted Words of the Sentence in reversed order,

    inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})

An imporant note to make is the *direction* of the implication in Theorem 2.3.9. A bidirectional equivalence would allow one to infer from the above equation that a Sentence is invertible. However, the direction of Theorem 2.3.9 cannot be strengthened, as the following Theorem 2.3.10 makes clear.

Theorem 2.3.10 also makes clear why Definition 2.3.1 of Admissible Sentence of Word Length *n* is essential to understanding invertibility. 

**Theorem 2.3.10** ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ (∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})) ∧ (inv(ζ) ∈ A(Λ(ζ)))

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus C:sub:`L`, *ζ* is invertible if and only if,

(→) Let ζ be an arbitrary invertible sentence in C:sub:`L`.

    1. The i:sup:`th` Word of inv(ζ) is the inverse of the (Λ(ζ) - i + 1):sup:`th` Word of ζ
    2. inv(ζ) is an admissible sentence of word length Λ(ζ).

Since ζ ∈ K, by Definition 2.3.2, 

    3. inv(ζ) ∈ C:sub:`L`.

By Theorem 2.3.5, the Words in the *inv(ζ)* must be in the reversed order of the inverted Words in *ζ*,

    4. ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})

By Theorem 2.3.4, the inverse of *ζ*, *inv(ζ)*, can be expressed as the DeDelimitation of the inverses of the Words of *ζ* in reverse order,

    5. inv(ζ) = DΠ:sub:`i=1`:sup:`Λ(ζ)` inv(ζ{Λ(ζ) - i + 1})

This is equivalent to,

    6. inv(ζ) = DΠ:sub:`i=1`:sup:`Λ(ζ)` inv(ζ){i}

Since *inv(ζ)* *∈* **C**:sub:`L` by assumption (step 1) and *inv(ζ)* has the same Word Length as *ζ* which is *Λ(ζ)*, and *inv(ζ)* is a Delimitation of Words from **L**, by Definition 2.3.1, it follows that,

    7. inv(ζ) ∈ A(Λ(ζ)).

Therefore, both conditions hold, 

    8. ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
    9. inv(ζ) ∈ A(Λ(ζ))

(←) Assume that for an arbitrary sentence *ζ* *∈* **C**:sub:`L`, the following holds,

    1. ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
    2. inv(ζ) ∈ A(Λ(ζ))


By Definition 2.3.1, since *inv(ζ)* *∈* **A**(*Λ(ζ)*), it follows immediately, 

    3. inv(ζ) ∈ C:sub:`L`

By Definition 2.3.2, it follows, 

    4. ζ ∈ K

Therefore, the bidirectional theorem holds. ∎

Just as the notion of Word Length introduced a dimension of *"semanticality"* to the formal system, so too does the notion of an Admissible Sentence introduce a dimension of *"grammaticality"*. Theorem 2.3.10 takes no stance on what constitutes an Admissible Sentence, what sort of grammatical forms and structures might define this notion, except to say it must be the result of a Delimitation of Words that belongs to the Corpus. 

The significance of Theorem 2.3.10 is the additional syntactical constraint that is imposed over and above *admissibility* into a Corpus when a Sentence under goes inversion. Not only must the Inverse Sentence possess *admissibility*, the pre-cursor to *grammaticality*, but it must also display Word-level symmetry. This is definitively confirmed by Theorem 2.3.11.

**Theorem 2.3.11** ∀ ζ ∈ C:sub:`L`: ζ ∈ K → ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I

This theorem can be stated in natural language as follows: For every Invertible Sentence *ζ* in the Corpus **C**:sub:`L`, every Word in *ζ* is an Invertible Word.

Let *ζ* be an arbitrary Invertible Sentence in C:sub:`L`, and let *i* be a natural number such that *1 ≤ i ≤ Λ(ζ)*. Since *ζ* *∈* **K**, by Definition 2.3.2, 

    1. inv(ζ) ∈ C:sub:`L`.

By Definition 2.1.5, *ζ{i}* refers to the Word at index *i* in the Word-level representation of *ζ*. By Theorem 2.3.9,

    2. ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})

By the Extraction Axiom S.2, since *ζ* *∈* **C**:sub:`L`, all Words in its Word-level representation belong to **L**. Therefore, *ζ{i}* *∈* **L** for all *i* such that *1 ≤ i ≤ Λ(ζ)*.

Since *inv(ζ)* *∈* **C**:sub:`L` (from step 1) and each word *inv(ζ){i}* is the inverse of a word in ζ (from step 2), by Axiom S.2, all the Words in the Word-level representation of *inv(ζ)* belong to L,

    3. inv(ζ){i} ∈ L

By Definition 1.3.2 of Invertible Words, this means that *ζ{i}* is an Invertible Word. Therefore, *ζ{i}* *∈* **I**. Since *ζ* and *i* were arbitrary, this can generalize, 

    ∀ ζ ∈ C:sub:`L`: ζ ∈ K → ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I ∎

The contrapositive of Theorem 2.3.10 provides a schema for searching for Invertible Sentences. If any of Words in a Sentence are not Invertible, then the Sentence is not Invertible. In other words, it suffices to find a single word in a Sentence that is not Invertible to show the entire Sentence is not Invertible.

Section III: Palindromic Structures
===================================

As mentioned in the introduction of this work, the structure of palindromes is described through the combination of four different attributes or dimensions: *aspect*, *parity*, *case* and *punctuality*. The framework has now been developed to classify the first two palindromic properties with more precision.

Unfortunately, as far as the author knows, punctuation and capitalization are syntactic bearers of semantic meaning that cannot be reduced to purely formal considerations. Both punctuality and case require additional axioms to describe the unique structuring they impose on a Language and its Corpus. In the author's opinion, it is impossible to disentangle these linguistic phenomenon from the realm of semantics.

In what follows, two things are implicitly assumed. These assumptions are made explicit here, so the scope of the results can be properly understood. First, the Alphabet **Σ** is assumed to contain no punctuation marks beyond the Delimiter Character (if one is inclined it to consider a form of punctuation). Second, it is assumed every Character in **Σ** is distinct, meaning all matters of case are ignored. To rephrase the same idea more precisely: there is no assumed semantic relation between Characters in the Alphabet that would allow the identification of distinct Characters as different *cases* of the same Character.

With these assumptions, the analysis is confined to the dimensions of *aspect* and *parity*, which will be defined in the following subsections. After the results are derived, consideration will be given to future work that could potentially integrate semantic considerations into the formal framework of palindromic structures to account for the dimensions of punctuality and case, in addition to symmetries above the Sentence level that might be incorporated into the conditions for Palindromes.

Section III.I: σ-Reductions 
----------------------------

The mathematical study of palindromes will revolve around a novel linguistic operation, termed a *σ*-reduction. This operation will allow the semantic content of a palindrome to be projected onto an Alphabet that preserves the order of its Characters under String Inversion, allowing for a precise definition of a palindrome within a purely formal language.

Definitions
^^^^^^^^^^^

Before defining a *σ*-reduction, the preliminary concept of a *σ-reduced Alphabet* must be introduced. The following definition serves as the basis for constructing the operation of *σ*-reduction.

As has been seen with examples of Imperfect Palindromes like *"borrow or rob"*, a palindromic structure can have its Delimiter Character scrambled in the inversion of its form, i.e. *"bor ro worrob"*, making it lose semantic coherence. Imperfect Palindromes must be rearranged Delimter-wise to retrieve the original form of the Sentence. However, String Inversion preserves the relative order of the non-Delimiter Characters in a palindromic String, so the process of reconstitution is only a matter of resorting the Delimiter characters. This invariance of the Character order, while the Word order is scrambled by Delimiter, suggests palindromes might be more easily defined without the obstacle of the Delimiter.

**Definition 3.1.1: σ-Reduced Alphabet**

A *σ-reduced Alphabet* is an Alphabet Σ that has had its Delimiter character removed, so that it only consists of non-Delimiter characters. A sigma-reduced Alphabet is denoted Σ:sub:`σ`. Formally,

    Σ:sub:`σ` = Σ - { σ } ∎

In order to define palindromes in all of their varieties, perfect or imperfect, the semantic incoherence that is introduced by the inversion of Imperfect Palindromes must be removed. This is accomplished through the introduction of the operation of *sigma reduction*.

**Definition 3.1.2: σ-Reduction**

Let *t* be a String with length *l(t)* and Character-level representation 

    1. t = { (1,𝔞:sub:`1`) , (2, 𝔞:sub:`2`) , ... , (l(t), 𝔞:sub:`l(t)`) } 
    2. 𝔞:sub:`i` ∈ Σ.

The *σ*-reduction of *t*, denoted by the lowercase Greek final Sigma, *ς(t)*, maps the String *t* to a new String *u* in the *σ*-reduced alphabet **Σ**:sub:`σ` by removing all occurrences of the Delimiter Character. Formally, *ς(t)* is defined and constructed using the *Reduction Algorithm*,

**Reduction Algorithm**

**Algorithm 3: Reduction Algorithm**

The Reduction Algorithm takes in a String *t* as input. It initializes the values of several local variables and then iterates over the Character-level set representation of the String *t* until the Characters have been exhausted. It then returns the *σ-reduced* String *s* that corresponds to the String *t*. The exact details are given below.

.. topic:: Algorithm Reduce(t: String)

    # Input: A String t
    # Output: A String s that represents the σ-reduction of t

    # Initialization
    ## Character-level representation of s
    1. s ← Empty(s)
    ## Index to iterate over input String
    2. i ← 1
    ## Empty string to store σ-reduced String
    3. t ← ε            

    # Iteration
    4. While i ≤ l(s):
        
        a. If s[i] ≠ σ:
            
            i. t ← (t)(s[i])
        
        c. i ← i + 1

    # Finalization
    5. If l(t) > 0:
        
        a. Apply Basis Clause of Definition 1.1.1 to t
    
    6. Return t ∎

Note the String *s* which is initialized to hold the *σ*-reduced String is set equal to the value of the Empty Character. The conditional application of the Basis Clause of Concatenation in step 1 of the Finalization Block ensures this Character is removed from the output of the Reduction Algorithm, if the input string contained at least one non-Empty Character. Otherwise, the Reduction Algorithm returns an Empty Character. From this, it is clear if a String only contains Delimiters,

    ε = ς(σ) = ς(σσ) = ς(σσσ) = ... 

From which, it follows, by Definition 1.1.3 of String Length, the String Length of a reduced Delimiter is simply zero,

    l(ς(σ)) = 0

Moreover, since by Discovery Axiom W.1., Words do not contain Delimiters, for any Word *α* in Language **L**,

    ς(α) = α

Again, from Definition 1.1.3, the String Length of a reduced Word is simply the String Length of the Word,

    l(ς(α)) = l(α)

A subtlety of the Reduction Algorithm should be noted. While *ς(σ) = ε* and *ς(α) = α*, it does not follow the *σ*-reduction of a Word concatenated with the Delimiter is the concatenation of that Word with the Empty Character. In other words, the following holds,

    ς(ασ) ≠ αε

This is because of the condition *(j > 1)* in the Finalization Block of the Reduction ensures Empty Characters are stripped from *t* when the input String contains atleast one non-Empty Character that has been concatenated into the *σ*-reduction String. 

The more complicated properties of *σ*-reductions are proved in the theorems that follow. Before moving onto the proofs, the following example shows how to apply the Reduction Algorithm to construct the *σ*-reduction of a String.

**Example**

Let *s = "a b c"* be a String from the Alphabet *Σ = { "", " " , "a", "b", "c" }*. Note in this example *σ = " "* and *l(s) = 5*. The value of the variables in the Reduction Algorithm after each iteration are given below,

    1. i = 2, t = ε"a"
    2. i = 3, t = ε"a"
    3. i = 4, t = ε"ab"
    4. i = 5, t = ε"ab"
    5. i = 5, t = "abc"
        
The result of the σ-reduction of *s* is thus given by,

    ς(s) = "abc" ∎

A *σ*-reduction can be thought of as a linguistic operation analogous to vector projection. While not a strict mathematical equivalence, this conception of *σ*-reduction captures the idea of transforming a String from its original form (with Delimiters) onto a reduced space (without Delimiters), similar to how a vector can be projected onto a subspace.

The *σ*-reduced Alphabet (**Σ**:sub:`σ`) can be seen as a subspace within this higher-dimensional space, consisting of only the non-Delimiter dimensions. The sigma reduction function (*ς(s)*) acts as a projection operator, mapping the String onto this subspace by eliminating the components corresponding to the Delimiter character (*σ*).

Note that a *σ*-reduction is not a one-to-one operation. It is possible for the *σ*-reduction of a palindrome to map onto a totally different sentence, not necessarily a palindrome.

As an example, consider the (partial, ignoring punctuality) Palindromes *ᚠ = "madam im adam"* and *ᚢ = "mad am i madam"*. The *σ*-reduction of both of these Sentences would map to the *σ-reduced* value of *madamimadam".

Both the Palindrome and the alternative Sentence (which also happens to be a Palindrome) have the same *σ*-reduction, despite having different meanings and grammatical structures. This highlights the ambiguity that can arise from removing spaces, as the original Word boundaries and Sentence structure are lost.

Theorems 
^^^^^^^^

The following theorems establish the basic properties of *σ*-reductions. 

**Theorem 3.1.1** ∀ ζ ∈ C:sub:`L`: inv(ς(ζ)) = ς(inv(ζ))

Let *ζ* be an arbitrary sentence in C:sub:`L`. Let *s* be the *σ*-reduction of *ζ*,

    1. s = ς(ζ)

Let *t* be the Inverse of *s*,

    2. t = inv(s).

Let *u* be the Inverse of *ζ*,

    3. u = inv(ζ). 
    
Let *v* be the *σ*-reduction of *u*,

    4. v = ς(u) = ς(inv(ζ)) 

Since *s* contains only the non-Delimiter characters of *ζ* in their original order, and *t* is the reversed sequence of Characters in *s*, *t* contains only the non-Delimiter characters of *ζ* in reversed order.

Similarly, since *u* is the reverse sequence of Characters in *ζ*, and *v* is obtained by removing Delimiters from *u*, *v* also contains only the non-Delimiter characters of *ζ* in the reversed order.

Therefore, by Definition 1.1.4, *t* and *v* must be the same String, as they both contain the same Characters in the same order. Since *t = v*, 

    1. inv(ς(ζ)) = ς(inv(ζ))

Since ζ was an arbitrary sentence in C:sub:`L`, this can be generalized,

    1. ∀ ζ ∈ C:sub:`L`: inv(ς(ζ)) = ς(inv(ζ)) ∎

This corollary is essential because it allows free movement between the Inverse of a *σ*-reduction and the *σ*-reduction of an Inverse. In other words, Theorem 3.1.1 establishes the commutativity of *σ*-reduction over inversion and visa versa. 

As the theorems in this section will make clear, there exists a unique type of algebraic structure that links the operations of *σ*-reduction, inversion and concatenation. The properties of this algebraic structure will be necessary for establishing the results in the next subsection.

The next theorem demonstrates how *σ*-reduction interacts with concatenation.

**Theorem 3.1.2** ∀ ζ, ξ ∈ C:sub:`L`: ς(ζξ) = (ς(ζ))(ς(ξ))

Let *ζ* and *ξ* be arbitrary sentences in **C**:sub:`L`. Let **Ζ** and **Ξ** be the character-level representations of *ζ* and *ξ*, respectively,

    1. Ζ = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(ζ)`)

    2. Ξ = (𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(ξ))`

Let *ζξ* be the concatenation of *ζ* and *ξ*. The character-level representation of *ζξ* is,

    3. ΖΞ = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(ζ)`, 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(ξ)`)

Let *s* be the σ-reduction of *ζξ*. Let *t* be the *σ*-reduction of *ζ*. Let *u* be the *σ*-reduction of *ζξ*,

    4. s = ς(ζξ)
    5. t = ς(ζ)
    6. u = ς(ξ)

Let *v* be the concatenation of the Strings *t* and *u*,

    7. v = tu = (ς(ζ))(ς(ξ))

Since *σ*-reduction only removes Delimiters and doesn't change the order of non-Delimiter Characters, the non-Delimiter characters in *s* (the *σ*-reduction of *ζξ*) are the same as the non-Delimiter Characters in *ζ* followed by the non-Delimiter Characters in ξ.

The non-Delimiter characters in *v*, the concatenation of *ς(ζ)* and *ς(ξ)*, are also the non-Delimiter characters in *ζ* followed by the non-delimiter characters in *ξ*.

Therefore, by Definition 1.1.4, *s* and *v* must be the same String, as they both contain the same Characters in the same order (the non-Delimiter Characters of *ζ* followed by the non-Delimiter characters of *ξ*). Since *s = v*, 

    8. ς(ζξ) = (ς(ζ))(ς(ξ))

Since ζ and ξ were arbitrary sentences in C:sub:L, this can be generalized,

    9. ∀ ζ, ξ ∈ C:sub:`L`: ς(ζξ) = (ς(ζ))(ς(ξ)) ∎

Theorem 3.1.2 further demonstrates the *algebraic* nature of *σ*-reduction and the other String operations. It shows that *σ*-reduction *distributes* over concatenation, just as inversion "distributes" (in a reversed way) over concatenation (Theorem 1.2.5). These properties suggest that *σ*-reduction, inversion and concatenation are not just arbitrary operations but instead are deeply connected to the underlying structure of Strings and Sentences.

As another example of this *"linguistic algebraic structure"*, the following theorem might be termed the *"Idempotency of σ-reduction"* or the *"σ-reduction Idempotence Property"*.

**Theorem 3.1.3** ∀ ζ ∈ C:sub:`L`: ς(ς(ζ)) = ς(ζ)

Let *ζ* be an arbitrary Sentence in **C**:sub:`L`. Let s be the *σ*-reduction of *ζ*,

    1. s = ς(ζ)

Let *t* be the *σ*-reduction of *s*,

    2. t = ς(s) = ς(ς(ζ))

Since *s* is the result of applying a *σ*-reduction to *ζ*, it contains no Delimiter Characters (σ).

When *s* is *σ*-reduced (to get *t*), the Reduction Algorithm in Definition 3.1.2 iterates through the Characters of *s*. Since s has no Delimiters, the condition if *s[i] ≠ σ* in the algorithm will always be true, and every character of *s* will be concatenated to the initially empty string *t*. Therefore, by Definition 1.1.4, *t* will be identical to *s*, as it contains the same Characters in the same order. Thus,

    1. ς(ς(ζ)) = ς(ζ)

Since ζ was an arbitrary sentence in C:sub:L, this can be generalized,

    4. ∀ ζ ∈ C:sub:`L`: ς(ς(ζ)) = ς(ζ) ∎

**Theorem 3.1.4** ∀ ζ ∈ C:sub:`L`: Λ(ς(ζ)) ≤ 1

Let *ζ* be an arbitrary sentence in C:sub:`L`. By the Duality Axiom S.1, every Sentence in C:sub:`L` must contain at least one word from L. 

By Definition 3.1.2, *ς(ζ)* removes all Delimiters from *ζ*. Therefore, *ς(ζ)* consists of the Characters of the words in *ζ* concatenated together without any delimiters.

By the Discovery Axiom W.1., Words in **L** cannot contain Delimiters.

By Definition 2.1.4, the Word Length *Λ(s)* of a String *s* counts the number of Words in *s*, where Words are separated by Delimiters.

If *ζ* contains only one Word, then *ς(ζ)* will be that Word,

    1. Λ(ς(ζ)) = 1

If *ζ* contains multiple Words, then *ς(ζ)* will be a concatenation of those words without Delimiters. This concatenated String may or may not be a valid Word in **L**.

If the concatenated String is a valid Word in **L**, then,

    2. Λ(ς(ζ)) = 1

If the concatenated String is not a valid Word in **L**, then,

    3. Λ(ς(ζ)) = 0

Therefore, in all possible cases,

    Λ(ς(ζ)) ≤ 1.

Since *ζ* was an arbitrary sentence in **C**:sub:`L`, this can be generalized, 

    ∀ ζ ∈ C:sub:`L`: Λ(ς(ζ)) ≤ 1. ∎


**Theorem 3.1.5** ∀ u, t ∈ S : u ⊂:sub:`s` t ↔ ς(u) ⊂:sub:`s` ς(t) 

This theorem can be stated in natural language as follows: For any two Strings *u* and *t*, *u* is contained in *t* if and only if the *σ*-reduction of *u* is contained in the *σ*-reduction of *t*.

Let *u* and *t* be arbitrary strings in **S**.

(→) Assume 

    1. u ⊂:sub:`s` t.

By Definition 1.1.7, there exists a strictly increasing and consecutive function *f*: N:sub:`l(u)` → N:sub:`l(t)` such that,

    2. ∀ i ∈ N:sub:`l(u)`: u[i] = t[f(i)]

Let 

    3. s = ς(u) 
    4. v = ς(t).

By the Definition 3.1.2 of *σ*-reduction, *s* is obtained by removing all Delimiters from *u*, and *v* is obtained by removing all Delimiters from *t*.

Since *u* is contained in *t*, the non-Delimiter Characters of *u* appear in *t* in the same order. The function *f* maps the indices of these Characters.

Define a function *g*: **N**:sub:`l(s)` → **N**:sub:`l(v)` that maps the indices of *s* to the indices of *v*. In other words, if *i* is an index in *s*, then *g(i)* is the index in *v* that corresponds to the same non-Delimiter character.

Since *f* is strictly increasing and consecutive, and *σ*-reduction only removes Delimiters, *g* will also be strictly increasing and consecutive. (*g* essentially compresses the mapping of *f* by skipping over the Delimiter indices and offseting).

For any index *i* in *s*, 

    5. s[i] = u[j] 
    
for some j. Moreover, 

    6. u[j] = t[f(j)]. 
    
Since *s* and *v* are *σ*-reduced, *s[i]* and *v[g(i)]* correspond to the same non-Delimiter Character, and g(i) is constructed such that 

    7. v[g(i)] = t[f(j)]. 
    
Therefore, 

    8. s[i] = v[g(i)].

Since g is a strictly increasing and consecutive function and s[i] = v[g(i)], by Definition 1.1.7, 

    9. s ⊂:sub:`s` v
    
From which it follows,

    10. ς(u) ⊂:sub:`s` ς(t).

(←) Assume 

    1. ς(u) ⊂:sub:`s` ς(t).

By Definition 1.1.7, there exists a strictly increasing and consecutive function *g*: **N**:sub:`l(ς(u))` → **N**:sub:`l(ς(t))` such that:

    2. ∀ i ∈ N:sub:`l(ς(u))`: ς(u)[i] = ς(t)[g(i)]

Define a function *f*: N:sub:`l(u)` → N:sub:`l(t)` that maps the indices of *u* to the indices of *t* by essentially "re-inserting" the delimiters. For each non-Delimiter character in *u* (and corresponding index in *ς(u)*), *f* will map to the corresponding index in *t*. For Delimiter characters in *u*, *f* will map to an index in *t* that preserves the order and consecutiveness.

Since *g* is strictly increasing and consecutive, and the Delimiters are only removed, not reordered, the function *f* will also be strictly increasing and consecutive.

For each index *i* in *u*, *u[i]* will either be a non-Delimiter or a Delimiter Character.

If *u[i]* is a non-Delimiter character, it corresponds to a Character in *ς(u)*, and by the properties of *g* and *f*, the following holds for some *j*,

    3. u[i] = ς(u)[j] = ς(t)[g(j)] = t[f(i)] 

If *u[i]* is a Delimiter, then by the construction of *f*, it will be mapped to a corresponding Delimiter in *t*, so 

    4. u[i] = t[f(i)]

Since *f* is a strictly increasing and consecutive function and *u[i] = t[f(i)]* for all *i* *∈* **N**:sub:`l(u)`, by Definition 1.1.7,

    5. u ⊂:sub:`s` t.

Since both directions of the implication hold, it can be concluded,

    6. ∀ u, t ∈ S : u ⊂:sub:`s` t ↔ ς(u) ⊂:sub:`s` ς(t) ∎

During a *σ*-reduction, Theorem 3.1.4 demonstrates information is lost with respect to the following semantic categories,

  - Word Boundaries: The spaces between words, which are crucial for parsing and understanding the sentence, are eliminated.
  - Sentence Structure: The grammatical structure of the sentence, the relationships between words and phrases, becomes ambiguous.
  - Prosody and Rhythm: The pauses and intonation that contribute to the meaning and expression of the sentence are lost.

However, some semantic information is preserved. The individual words themselves, or at least their character sequences, remain present in the *σ-reduced* string. The next theorem proves semantic content is retained during the *σ*-reduction of a Sentence.

**Theorem 3.1.6** ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` ς(ζ)

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus **C**:sub:`L`, and for every Word *ζ{i}* in the Word-level representation of *ζ*, *ζ{i}* is contained in *ς(ζ)*.

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. By Theorem 2.2.4, it is known at least one Word must exist in *ζ*. Let *ζ{i}* be one of the Words in the sequence of Words that form *ζ*. 

This means that *ζ* can be written as either, in the case of *Λ(ζ) > 1*, 

    1. Case (Λ(ζ) > 1): ζ = (s:sub:`1`)(σ)(ζ{i})(σ)(s:sub:`2`)
    
where *s*:sub:`1` and *s*:sub:`2` are (possibly Empty) Strings. 

In the case that Λ(ζ) = 1, then, this means *ζ* can be written simply as, 

    1. Case (Λ(ζ) = 1): ζ = ζ{1}

By the Definition 3.1.2, *ς(ζ)* is obtained by removing all Delimiters from *ζ*. Furthermore, by Theorem 3.1.2, *σ*-reduction distributes over concatenation. Thus,

    1. Case (Λ(ζ) > 1): ς(ζ) = (ς(s:sub:`1`))(ς(ζ{i}))(ς(s:sub:`1`))
    2. Case (Λ(ζ) = 1): ς(ζ{1})

By the Discovery Axiom W.1, Words in **L** do not contain Delimiters.

    1. Case (Λ(ζ) > 1): ς(ζ) = (ς(s:sub:`1`))(ζ{i})(ς(s:sub:`1`))
    2. Case (Λ(ζ) = 1): ς(ζ{1}) = ζ{1}

Therefore, by the definition of Containment (Definition 1.1.4):

    1. Case (Λ(ζ) > 1): ζ{i} ⊂:sub:`s` ς(ζ)
    2. Case (Λ(ζ) = 1): ζ{1} ⊂:sub:`s` ς(ζ) 

In both cases, there is a Word in *ζ* that is contained in the *σ*-reduction of *ζ*. Since *ζ* was arbitrary, this can generalize as,

    ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` ς(ζ) ∎

As one of the final precursors to a formal explication of palindromic structures, this next theorem shows how *σ*-reduction behaves over the class of Invertible Sentences, an extremely important class for understanding the mechanics of Palindromes.

**Theorem 3.1.7** ∀ ζ ∈ K: [ ς(ζ) = inv(inv(ς(ζ))) ]

In natural language, this theorem can be stated in natural language as follows: If a Sentence in a Corpus is invertible, then its invertibility is invariant under *σ*-reduction.

Assume 

    1. ζ ∈ K

In other words, assume that *ζ* is an Invertible Sentence. By Theorem 2.3.7, since *ζ* is invertible, all its Words are also Invertible,
 
    2. ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → inv(ζ){i} ∈ L

The σ-reduction of *ζ*, *ς(ζ)*, is obtained by removing all Delimiters from ζ. Since no Word contains Delimiters (by Discovery Axiom W.1), the *σ*-reduction concatenates the Words of *ζ*,

    3. ς(ζ)= (ζ{1})(ζ{2})...(ζ{Λ(ζ)})

Applying Theorem 1.2.5 repeatedly,

    4. inv(ς(ζ)) = inv((ζ{1})(ζ{2})...(ζ{Λ(ζ)}))

To get,

    5.  inv(ς(ζ))  = (inv(ζ{Λ(ζ)})) ... (inv(ζ{2}))(inv((ζ{1})))

Applying a second Inversion,

    6. inv(inv(ς(ζ))) = inv((inv(ζ{Λ(ζ)})) ... (inv(ζ{2}))(inv((ζ{1}))))

Applying Theorem 1.2.5 again,

    7. inv(inv(ς(ζ))) = (inv(inv((ζ{1})))) (inv(inv((ζ{2}))))...(inv(inv((ζ{Λ(ζ)}))))

Finally, applying Theorem 1.2.4 (*inv(inv(s)) = s*)

    8. inv(inv(ς(ζ))) = (ζ{1})(ζ{2})...(ζ{Λ(ζ)})

Therefore, combining step 3 and step 8

    9. ς(ζ) = inv(inv(ς(ζ))). ∎

The contrapositive of this theorem, much like the contrapositive of Theorem 2.3.6, provides a schema for searching the *σ-reduced* space for Invertible Sentences. The domain of this space reduces the complexity of searching for palindromic strings. Potential palindromic candidates can be projected into the *σ-reduced* spaced, and then filtered by those whose *σ*-reduction whose Inverse does not equal itself. 

The final theorems in this section, Theorems 3.1.8 - 3.1.9, provide a method for constructing the *σ*-reduction of a Sentence through iterated concatenation. These theorem leverage the operations of Delimitation and Limitation introduced in Definitions 1.2.7 - 1.2.8.

**Theorem 3.1.8** ∀ ζ ∈ C:sub:`L`: ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

This theorem can be stated in natural language as follows: The *σ*-reduction of a Sentence is the Limitation of its Words.

Assume,

    1. ζ ∈ C:sub:`L`

By Definition 2.1.3, 

    2. W:sub:`ζ` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`Λ(ζ)`)

Where,

    3. ∀ i ∈ N:sub:`Λ(ζ)`: α:sub:`i` ∈ L.

By Theorem 2.3.4, ζ can be expressed as the Delimitation of its words:

    4. ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i} = (ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{Λ(ζ)})

By Definition 3.1.2, *ς(ζ)* removes all Delimiters from *ζ*. Applying *σ*-reduction to the expression step 4,

    5. ς(ζ) = ς((ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{Λ(ζ)}))

By repeated application of Theorem 3.1.2, i.e. by distributing the *σ*-reduction,

    6. ς(ζ) = (ς(ζ{1}))(ς(σ))(ς(ζ{2}))(ς(σ)) ... (ς(σ))(ς(ζ{Λ(ζ)}))

Since 

    7. ς(σ) = ε

This can be rewritten with the Basis Clause of Concatenation,

    8. ς(ζ) = (ς(ζ{1}))(ς(ζ{2}))...(ς(ζ{Λ(ζ)}))

By Definition 3.1.2 and the Discovery Axiom W.1.,

    9. ∀ i ∈ N:sub:`Λ(ζ)`: ς(ζ{i}) = ζ{i}

Therefore,
   
    10. ς(ζ) = (ζ{1})(ζ{2})...(ζ{Λ(ζ)})

By Definition 1.2.8, the right-hand side is the Limitation of the words in **W**:sub:`ζ`,

    11. ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

Since *ζ* was an arbitrary Sentence in this Corpus, this can be generalized,

    12. ∀ ζ ∈ C:sub:`L`: ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i} ∎

Theorem 3.1.8 establishes an important formula for the construction of *σ*-reductions. The Reduction Algorithm targets Strings as input, i.e. it processes sequential Characters in a String. If an ordered sequence of Words is already at hand, without Theorem 3.1.8, it would be required to reconstruct the String which corresponds to the sequence and process it through the Reduction Algorithm. Rather than applying the Reduction Algorithm everytime a *σ*-reduction is required, Theorem 3.1.8 provides a schema for the construction of *σ*-reductions through the process of Limitation.

Compare Theorem 3.1.8 to Theorem 2.2.5, reprinted below for reference,

    ζ = DΠ:sub:`i=1`:sup:`n` ζ{i}

In other words, taking the *σ*-reduction of a Sentence converts the Delimitation of its Words into a Limitation. This follows directly from the Definitions of Limitation and Delimitation. The next theorem proves this relationship for the more general case of *any* ordered sequence of Words, not necessarily a semantically coherent and admissible Sentence.

**Theorem 3.1.9** ∀ n ∈ ℕ: ∀ p ∈ Χ:sub:`L(n)`: ς(DΠ:sub:`i=1`:sup:`n` p(i)) = LΠ:sub:`i=1`:sup:`n` p(i)

This theorem can be stated in natural language as follows: the *σ*-reduction of a Delimitation of a Phrase is equal to a Limitation of the same Phrase.

Let *n* be an arbitrary natural number, and let *p* be an arbitrary Phrase from a Language's *n*:sup:`th` Lexicon, 

    1. p ∈ Χ:sub:L(n)
    2. p = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`).

By Definition 1.2.7, 

    3. DΠ:sub:`i=1`:sup:`n` p(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`n`)

Applying Definition 3.1.2 of *σ*-reduction to the Delimitation and applying the Basis Clause of Definition 1.1.1,

    4. ς(DΠ:sub:`i=1`:sup:`n` p(i)) = (α:sub:`1`)(α:sub:`2`)... (α:sub:`n`)

By Definition 1.2.8,

    5. LΠ:sub:`i=1`:sup:`n` p(i) = (α:sub:`1`)(α:sub:`2`) ... (α:sub:`n`)

By repeated application of Theorem 1.1.1 to step 4,

    6. ς(DΠ:sub:`i=1`:sup:`n` p(i)) = Σ:sub:`i=1`:sup:`n` α:sub:`i`

By repeated application of Theorem 1.1.1 to step 5,

    7. l((α:sub:`1`)(α:sub:`2`)... (α:sub:`n`)) = Σ:sub:`i=1`:sup:`n` α:sub:`i`

Comparing step 6 to step 7 and noting the *α*:sub:`i` is in the same position the same for all *1 ≤ i ≤ n*, it follows by Definition 1.1.4 of String Equality, 

    8. ς(DΠ:sub:`i=1`:sup:`n` p(i)) = LΠ:sub:`i=1`:sup:`n` p(i)

Since n and p were arbitrary, this can be generalized,

    9. ∀ n ∈ ℕ: ∀ p ∈ Χ:sub:`L(n)`: ς(DΠ:sub:`i=1`:sup:`n` p(i)) = LΠ:sub:`i=1`:sup:`n` p(i) ∎

The relationship between σ-reductions, Limitations and Delimitations provides an easy method for establishing the relationship between the String Length of a Sentence and the String Length of its σ-reduced form. 

**Theorem 3.1.10** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ l(ς(ζ))

Let ζ be an arbitrary Sentence in the Corpus. By Theorem 3.1.8,

    1. ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

By Theorem 2.2.5,

    2. ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

Since the only different between Definition 1.2.7 and 1.2.8 is that Delimitations insert a Delimiter while Limitations simply concatenate, it must follow,

    3. l(DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) ≥ LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

From this, step 1 and step 2, it follows, 

    4. l(ζ) ≥ l(ς(ζ))

Since ζ was arbitary, this can be generalized, 

    5. ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ l(ς(ζ)) ∎

Section III.II: Palindromes 
---------------------------

The current analysis now turns towards its culmination, using the notions that have been developed up to this point to define the mathematical structure of Palindromes. To motivate the next definition, consider how the operation of *σ*-reduction "*projects*" Palindromes onto an Alphabet where their symmetry is preserved.

Consider a Perfect Palindrome like *ᚠ = "strap on no parts"*,

    ς(ᚠ)= "straponnoparts"

    inv(ς(ᚠ)) = "straponnoparts"

In other words, the *σ*-reduction and the inversion of its *σ*-reduction projection result in the same String.

Consider an Imperfect Palindrome like *ᚢ = "borrow or rob"*,

    ς(ᚢ) = "borroworrob"

    inv(ς(ᚢ)) = "borroworrob"

Again, the *σ*-reduction eliminates the Delimiters, and the inversion of the *σ*-reduction captures the mirrored relationship between the words, even if the exact Character sequence isn't identical to the original Palindrome. Nevertheless, the *order* of the Characters is preserved. 

These examples lead directly to the next, important definition.

**Definition 3.2.1: Palindromes**

Palindromes are defined as the set of Sentences **P** that satisfy the following formula,

    ∀ ζ ∈ C:sub:`L`: ζ ∈ P ↔ (ς(ζ) = inv(ς(ζ))) ∎

This definition distills the core property of Palindromes, their symmetrical nature, by focusing on the sequence of Characters without the ambiguity of Delimiters. The use of set notation and logical operations provides a mathematically rigorous and unambiguous definition. Moreover, this definition can be easily adapted to different languages by simply defining the appropriate Alphabet **Σ** and the corresponding *σ-reduced* alphabet **Σ**:sub:`σ`

Definition 3.2.1 highlights the core feature of Palindromes: invariance under transformation. A Palindrome remains a Palindrome even when projected onto the *σ-reduced* Alphabet, demonstrating a structural integrity that's independent of the specific Alphabet that is used to represent it.

The condition *ς(ζ) = inv(ς(ζ)) = ς(inv(ζ))*, where the last equality follows from Theorem 3.1.1, can be seen as defining an equivalence relation on the set of Sentences, where Sentences are equivalent if inversion and *σ*-reduction *commute* over them.

This definition highlights that Palindromes possess a structure that is preserved even under the transformation of *σ*-reduction, demonstrating that their palindromic nature is not dependent on the presence of Delimiters. Moreover, it suggests Palindromes are an artifact of a *"hidden"* algebraic structure embedded into linguistics.

Aspect
^^^^^^

The first classification of Palindromes is now introduced.

**Definition 3.2.2: Perfect Palindromes**

Perfect Palindromes are defined as the set of Sentences **PP** that satisfy the following formula,

    ∀ ζ ∈ C:sub:`L`: ζ ∈ PP ↔ ζ = inv(ζ) ∎

Note the name given to this class of Sentences is premature. While the terminology will prove to be accurate, at this point in the analysis, one must be careful not to confuse Perfect Palindromes with Palindromes. It has not yet been shown the class of Sentences which satisfy Definition 3.2.2 also satisfy 3.1.3. Before moving onto this verification, the motivation for Definition 3.2.2 will briefly be explained.

Definition 3.2.2 implicitly captures the Character-level symmetry that's characteristic of Perfect Palindromes. If a Sentence is its own inverse, it means that the sequence of Characters reads the same backward as forward. It also implicitly captures the Word-level symmetry, as the inversion operation takes into account the reversal of Words within the Sentence, by Theorems 2.3.9 - 2.3.11. A Perfect Palindrome is a confluence of symmetries, a *"singularity"* of reflected inversion at every level of the linguistic hierarchy.

The following theorems will be used to validate the proposed class **PP** does indeed satisfy Definition 3.2.1, and thus Perfect Palindromes are a subset of the class of Palindromes in any Language and its Corpus.

**Theorem 3.2.1** PP ⊂ K

In natural language, this theorem can be stated as follows: Perfect Palindromes are a subset of the Invertible Sentences in a Corpus. 

Assume *ζ* is arbitrary Sentence in **C**:sub:`L` such that,

    1. ζ ∈ PP

This means *ζ* is a Perfect Palindrome, so by Definition 3.2.2, 

    2. ζ = inv(ζ).

Since *ζ* is a Perfect Palindrome, it is also a Sentence, and therefore,

    3. ζ ∈ C:sub:`L`
    
Because *ζ = inv(ζ)* and *ζ ∈* **C**:sub:`L`, it follows,

    4. inv(ζ) ∈ C:sub:`L`.

By Definition 2.3.2 of Invertible Sentences, 

    5. inv(ζ) ∈ C:sub:`L` ↔ ζ ∈ K

Therefore, 

    6. ζ ∈ PP → ζ ∈ K. 
    
This in turn implies,

    7. PP ⊂ K ∎

The connection between Invertible Sentences and Palindromes is thus established with Theorem 3.2.1. All Perfect Palindromes are Invertible Sentences, but not all Invertible Sentences are Perfect Palindromes. This in turn leads to the next two theorems which demonstrate the connection between Palindromes and Invertible Words. 

**Theorem 3.2.2** ∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})

This theorem can be stated in natural language as follows: If a Sentence is a Perfect Palindrome, then the *i*:sup:`th` Word of its Inverse is the Inverse of the Sentence's *Λ(ζ) - i + 1*:sup:`th` Word. 

Let ζ be an arbitrary Sentence in the Corpus such that it is a Perfect Palindrome,

    1. ζ ∈ PP

By Theorem 3.2.1 

    1. PP ⊂ K

By Theorem 2.3.9,

    ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})  ∎

**Theorem 3.2.3** ∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I

This theorem can be stated in natural language as follows: If a Sentence is a Perfect Palindrome, then all of its Words are Invertible. 

Recall the definition of a subset,

    1. A ⊂ B ↔ (∀ x: x ∈ A → x ∈ B)

Applying this definition to Theorem 3.2.1, 
    
    2. ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → ζ ∈ K

From Theorem 2.3.11, it is known the consequent of this conditional implies the following,

    3. ∀ ζ ∈ C:sub:`L`: ζ ∈ K → (∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I)

Recall the tautology of *Hypothetical Syllogisms*, for any propositions *p*, *q* and *r*,

    4. ( p → q ∧ q → r ) → (q → r)

Applying this tautological law to step 2 and step 3,

    5. ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → (∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I)

This can be rewritten using the rules of quantifiers,

    6. ∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I

Which is what was to be shown. ∎ 

It is now shown using the previous theorems that Perfect Palindromes are in fact a subset of the set that implicitly satisfies Definition 3.2.1.

**Theorem 3.2.4**  PP ⊂ P

Assume *ζ* is arbitrary Sentence in **C**:sub:`L` such that,

    1. ζ ∈ PP 
    
This means *ζ* is a Perfect Palindrome, so by Definition 3.2.2, 

    2. ζ = inv(ζ).

Applying a *σ*-reduction to both sides of the equation,

    3. ς(ζ) = ς(inv(ζ))

By Theorem 3.1.1, 

    4. ς(inv(ζ)) = inv(ς(ζ))

Combining steps 3 and 4, 

    5. ς(ζ) = inv(ς(ζ))

Step 4 exactly satisfies the condition for *ζ* to be a Palindrome according to Definition 3.2.1. Therefore, 

    6. ζ ∈ P.

Since *ζ* was an arbitrary Perfect Palindrome, it been shown that,

    7. ζ ∈ PP → ζ ∈ P
    
This in turn implies,

    8. PP ⊂ P ∎

Now that Perfect Palindromes have been shown to satisfy Definition 3.2.1, it is a simple matter of defining Imperfect Palindromes as those Palindromes which are *not* Perfect.

**Definition 3.2.3: Imperfect Palindromes**

Imperfect Palindromes are defined as the set of Sentences **IP** that satisfy the following open formula,

    ζ ∈ P - PP ∎

Definition 3.2.3 is not an explicit definition. It does not say how the class of Imperfect Palindromes are constructed. It only says those Palindromes which are not their own Inverses in the Corpus (i.e. are not Perfect) can have their symmetry under inversion preserved by a reduction to the *σ*-reduced Alphabet. 

This gives a way of identifying Sentences such as *ᚠ = "to oscillate metallic soot"* and *ᚢ = "rats live on no evil star"* as representatives of the same class, namely Palindromes, but with different *aspects*. *ᚢ* is Perfect, while *ᚠ* requires a *σ*-reduction. 

**Theorem 3.2.5** PP ∪ IP = P

Follows immediately from Theorem 3.2.4, Definition 3.2.3, and the fact that PP and IP are disjoint (by the definition of set difference). ∎

Since PP and IP are non-overlapping by Definition 3.2.3 and their union encompasses the entire class of Palindromes by Theorem 3.2.3, these two sets form a partition of the class of Palindromes. The following definition and terminology is introduced to help describe this partitioning.

**Definition 3.2.4: Aspect**

A Palindrome ζ is said to have a *perfect aspect* or *be perfect* if and only if,

    ζ ∈ PP 

A Palindrome ζ is said to have an *imperfect aspect* or *be imperfect* if and only if,

    ζ ∈ IP ∎

Thus, the first partitioning of the class of Palindromes has been discovered. The next section will detail the second partitioning of Palindromes: *parity*.

Parity
^^^^^^

One partitioning, or dimension, of Palindromes has been introduced through the concept of *aspect*. A Palindrome can either be perfect or imperfect, but not both. In this section, the definitions and theorems for uncovering the second partitioning of Palindromes, *parity*, will be developed.

In order to develop the notion of parity, a formal method of referring to the *left* and *right* halves of a Sentence must be introduced. This new notation can be seen as an extension of Character Index Notation introduced in Definition 1.1.5.

**Definition 3.2.5: Left Partial Sentence**

Let ζ be a Sentence in C:sub:`L` with Character-level representation **Z**,

    Z  = (ⲁ:sub:`1` , ⲁ:sub:`2` , ... , ⲁ:sub:`l(ζ)`).

Let *n* be a fixed natural number such that *1 ≤ n ≤ l(ζ)*. A Left Partial Sentence of the *n*:sup:`th` Character, denoted *ζ[:n]*, is formally defined as the sequence of Characters which satisfies, 

    Z[:n] = (ⲁ:sub:`1` , ⲁ:sub:`2` , ... , ⲁ:sub:`n`)  

When *n = 0*, *ζ[:0]* is defined as the empty string, *ε*.

When *n = l(ζ)*, *ζ[:n]* is the entire sentence *ζ*. ∎

**Definition 3.2.6: Right Partial Sentence**

Let ζ be a Sentence in C:sub:`L` with Character-level representation **Z**,

    Z  = (ⲁ:sub:`1` , ⲁ:sub:`2` , ... , ⲁ:sub:`l(ζ)`).

Let *n* be a fixed natural number such that *1 ≤ n ≤ l(ζ)*. A Right Partial Sentence of the *n*:sup:`th` Character, denoted *ζ[n:]*, is formally defined as the String which satisfies, 

    ζ[n:] = (ⲁ:sub:`n`, ⲁ:sub:`n+1`, ..., ⲁ:sub:`l(ζ)`)

where n is a natural number such that 1 ≤ n ≤ l(ζ) + 1.

When n = 1, ζ[1:] is the entire sentence ζ.

When n = l(ζ) + 1, ζ[n:] is defined as the empty string, ε. ∎

**Example**

Consider the Sentence *ᚠ = "form is the possibility of structure"*. Note, *l(ᚠ) = 36* and *Λ(ᚠ) = 6*. Then, 

    1. ᚠ[:2] = "fo"
    2. ᚠ[2:] = "orm is the possibility of structure"
    3. ᚠ[:4] = "form"
    4. ᚠ[10:] = "he possibility of structure" ∎

The notation *ζ[n:]* and *Z[:n]* is analogous to array slicing notation found in many programming languages. It indicates a substring is being taken starting from a position *n* Characters from the one end of the String up to the other end of the String, the direction depending on whether the Partial Sentence is Left or Right.

Take note, Partial Sentences are not necessarily a Word or a sequence of Words. A Left Partial Sentence will only be semantically coherent if the Character at *n* is a Delimiter, if the Character at *n* is the last Character of a Word or Sentence, or if the Partial Sentence "slices" a compound Word at exactly the correct position in Word. Simarily, a Right Partial Sentence will only be semantically coherent if *n* is the first Character in a Word or Sentence, or if the index slices a compound Word. 

Note, regardless of the value of *n*,

    l(ζ[:n]) = n

    l(ζ[n:]) = l(ζ) - n + 1

This relation bears a similarity to Definition 1.2.4 of String Inversion and Definition 1.3.1 of Reflective Words, both of which require Character-level inversions,

    α[i] = α[l(α) - 1 + 1]

A Palindrome is a type of inversion. In a Palindrome, the requirement that individual Characters must maintain their symmetry across its String Length is extended up to the Sentence level through the requirement that, based on the parity of the Palindrome, the Partial Sentences on either side of the Sentence's center must be mirror images of one another. 

Note that Definition 3.2.5 and Definition 3.2.6 are given in terms of Sentences because they will be applied primarily to Sentences, but there is nothing inherently in the definitions which prevents the Partial Notation from being applied to Strings that have been stripped of their Empty Characters via the Emptying Algorithm for the construction of their Character-level representation (Definition 1.1.2). In other words, Definition 3.2.5 and Definition 3.2.6 operate on a String's Character-level representation, not the String itself. This is an important distinction to be made (one that must be made for Character Index Notation and Word Index Notation as well). Partial Sentences (and Character Index Notation and Word Index Notation) are abstractions defined on a representation of a String that has been processed through the Emptying and Delimiting Algorithm.

The next two theorems leverage this insight and establish the fundamental relationship between Left and Right Partial Sentences. In addition, they prove the existence of a natural number that acts as the mid-point of the Sentence's String Length. This in turn will allow for a definition of a Sentence's *Pivot* as the center of a Sentence.

**Theorem 3.2.6** ∀ ζ ∈ C:sub:`L`:  ∀ i ∈ N:sub:`l(ζ)`: inv(ζ)[:i] = ζ[l(ζ) - i + 1:]

Let *ζ* be an arbitrary Sentence in the Corpus,

    1. ζ ∈ C:sub:`L`

Let *i* be a natural number such that,

    2. i ∈ N:sub:`l(ζ)`

By Definition 1.2.4 of String Inversion, the Inverse of *ζ*, denoted *inv(ζ)*, is formed by reversing the order of the Characters in *ζ*.

By Definition 3.2.5, the Left Partial Sentence of *inv(ζ)* up to index i, denoted *inv(ζ)[:i]*, consists of the first *i* characters of *inv(ζ),

    3. inv(ζ)[:i] = (inv(ζ)[1], inv(ζ)[2], ..., inv(ζ)[i])

By Definition 1.2.4, for any Character index j in inv(ζ):

    4. inv(ζ)[j] = ζ[l(ζ) - j + 1]

Applying this to each Character in inv(ζ)[:i], we get:

    5. inv(ζ)[:i] = (ζ[l(ζ)], ζ[l(ζ) - 1], ..., ζ[l(ζ) - i + 1])

Now, consider the Right Partial Sentence of *ζ* starting at index *l(ζ) - i + 1*, denoted *ζ[l(ζ) - i + 1:]*. By Definition 3.2.6, this consists of the characters from index *l(ζ) - i + 1* to the end of *ζ*,

    6. ζ[l(ζ) - i + 1:] = (ζ[l(ζ) - i + 1], ζ[l(ζ) - i + 2], ..., ζ[l(ζ)])

Notice that the sequence of Characters in *inv(ζ)[:i]* (from step 4) is the reverse of the sequence of Characters in *ζ[l(ζ) - i + 1:]* (from step 5).

Since *inv(ζ)* is the Inverse of *ζ*, the Characters in these two sequences are identical, just in reverse order.

Therefore, *inv(ζ)[:i]* and *ζ[l(ζ) - i + 1:]* have the same Characters in the same order. Furthermore, 

    7. l(inv(ζ)[:i]) = i
    8. l(ζ[l(ζ) - i + 1:]) = l(ζ) - (l(ζ) - i + 1) + 1 = i

Therefore, by definition 1.1.4 means they are equivalent as Strings,

    9. inv(ζ)[:i] = ζ[l(ζ) - i + 1:]

Since ζ and i were arbitrary, this can generalize over the Corpus, 

    10.  ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`l(ζ)`: inv(ζ)[:i] = ζ[l(ζ) - i + 1:] ∎

**Theorem 3.2.7** ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i + 1) ∧ (l(ζ[:i+1]) = l(ζ[i+1:]))

This theorem can be stated in natural language as follows: For any Sentence in the Corpus, its String Length is odd if and only if the String Length of the Left Partial Sentence of Length *i+1* is equal to the String Length of the Right Partial Sentence starting at index *i+1*.

(→) Let ζ be an arbitrary sentence in C:sub:`L` with odd length,

    1. ∃ i ∈ ℕ: l(ζ) = 2i + 1

Let

    2. n = i + 1. 

Since *i* is a natural number, *n* is also a natural number (by the property of integer succession). From step 1 and step 2, it follows

    3. 1 ≤ n ≤ l(ζ)

Thus, 

    4. n ∈ N:sub:`l(ζ)`.

The Left Partial Sentence of String Length *n* is then given by,

    5. ζ[:n] = ζ[:i+1]
    
By Definition 3.2.5 of Left Partial Sentences, 

    6. l(ζ[:i+1]) = i + 1.

The Right Partial Sentence is given by,

    7. ζ[n:] = ζ[i+1:]
    
By the definition of Right Partial Sentences, 

    8. l(ζ[i+1:]) = l(ζ) - n + 1 = (2i + 1) - (i + 1) + 1 = i + 1

Therefore, 

    9. l(ζ[:i+1]) = l(ζ[i+1:]) = i + 1.

From this it follows, 

    10. ∃ i ∈ N:sub:`l(ζ)`: (l(ζ[:i+1]) = l(ζ[i+1:])).

(←) Let *ζ* be an arbitrary sentence in **C**:sub:`L` such that,

    1. ∃ 1 ∈ N:sub:`l(ζ)`: (l(ζ[:i+1]) = l(ζ[i+1:])).

By the Definitions 3.1.7 and 3.1.8,

    2. l(ζ[:i+1]) = i+1

    3. l(ζ[i+1:]) = l(ζ) - (i+1) + 1

Putting step 1, step 2 and step 3 together, 

    4. i+1 = l(ζ) - (i+1) + 1

From which it follows algebraically, 

    5. l(ζ) = 2n + 1.

Therefore l(ζ) is odd. Putting both directions of the proof together and generalizing over all Sentences in the Corpus,

    6. ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i + 1 ) ∧ (l(ζ[:i+1]) = l(ζ[i+1:]))  ∎

**Theorem 3.2.8** ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i) ∧ (l(ζ[:i]) + 1 = l(ζ[i:]))

This theorem can be stated in natural language as follows: For any Sentence in the corpus, its String Length is even if and only if the String Length of the Left Partial Sentence of Length *i* plus 1 is equal to the String Length of the Right Partial Sentence starting at index *i*.

(→) Let *ζ* be an arbitrary sentence in **C**:sub:`L` such that there exists a natural number *i* with the following condition,
 
    1. l(ζ) = 2i.

Then let,

    2. n = i. 

Since *i* is a natural number, it follows from step 2 that,

    3. 1 ≤ n ≤ l(ζ)

From which it follows, 

    4. n ∈ N:sub:`l(ζ)`

The Left Partial Sentence of String Length *n* is then given by,

    5. ζ[:n] = ζ[:i]

By Definition 3.2.5, 

    6. l(ζ[:i]) = i

The Right Partial Sentence is given by,

    7. ζ[n:] = ζ[i:].

By Definition 3.2.6, 

    8. l(ζ[i:]) = l(ζ) - i + 1 = 2i - i + 1 = i + 1

Therefore, 

    9. l(ζ[:n]) + 1 = l(ζ[n:]) = i + 1

This shows found an *n* (specifically, *n = i*) exists such that 

    10. l(ζ[:n]) + 1 = l(ζ[n:])

Therefore, 

    11. ∃ n ∈ N:sub:`l(ζ)`: (l(ζ[:n]) + 1 = l(ζ[n:]))

(←) Let *ζ* be an arbitrary sentence in C:sub:`L` such that, 

    1. ∃ n ∈ N:sub:`l(ζ)`: (l(ζ[:n]) + 1 = l(ζ[n:]))

By Definition 3.2.5 and Definition 3.2.6,

    2. l(ζ[:n]) = n
    3. l(ζ[n:]) = l(ζ) - n + 1

Combining step 1, step 2 and step 3, 

    4. n + 1 = l(ζ) - n + 1

Solving for l(ζ),

    5. l(ζ) = 2n

Thus, l(ζ) is even. Since both directions of the implication hold, it can be concluded,

    ∀ ζ ∈ C:sub:`L`: (∃ i ∈ ℕ: l(ζ) = 2i) ↔ (∃ n ∈ N:sub:`l(ζ)`: (l(ζ[:n]) + 1 = l(ζ[n:]))) ∎

**Theorem 3.2.9** ∀ ζ ∈ C:sub:`L`: ∃ n ∈ N:sub:`l(ζ)`: (l(ζ[:n]) = l(ζ[n:])) ∨ (l(ζ[:n]) + 1 = l(ζ[n:]))

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus, there exists a natural number *n* (between *1* and the length of *ζ*, inclusive) such that either the String Length of its Left Partial Sentence is equal to the String Length of its Right Partial Sentence, or the String Length of the Left Partial Sentence is one more than the String Length of the Right Partial Sentence.

Let ζ be an arbitrary sentence in C:sub:`L`. Let,

    1. l(ζ) = k

If k is even, let 

    2. n = k/2

Then 

    3. l(ζ[:n]) = n = k/2

And 

    4. l(ζ[n:]) = k - n + 1 = k - k/2 = (k + 1)/2

Therefore, 

    5. l(ζ[:n]) + 1 = l(ζ[n:])

If k is odd, let 

    6. n = (k + 1)/2

Then 

    7. l(ζ[:n]) = n = (k + 1)/2

And 

    8. l(ζ[n:]) = k - n  + 1 = k - (k + 1)/2  + 1= (k - 1)/2 + 1 = (k + 1)/2

Therefore, 

    9. l(ζ[:n]) = l(ζ[n:])

In both cases, an *n* has been found that satisfies the condition in the theorem. Since *ζ* was an arbitrary Sentence, this can generalize over the Corpus,

    10. ∀ ζ ∈ C:sub:`L`: ∃ n ∈ N:sub:`l(ζ)`: ( l(ζ[:n]) = l(ζ[n:]) ) ∨ ( l(ζ[:n]) + 1 = l(ζ[n:]) ) ∎

Theorems 3.2.7 - 3.2.9 conjunctively establish the existence of a natural number that can reliably be called the center, or *Pivot*, of any Sentence in a Corpus. This leads to the following definition. 

**Definition 3.2.7: Pivots** 

The Pivot of a Sentence *ζ*, denoted *ω(ζ)*, is defined as the natural number such that the following formula is true,

   (l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) ) ∨ (l(ζ[:ω(ζ)]) + 1 = l(ζ[ω(ζ):])) 
   
Using Theorem 3.2.7 and Theorem 3.2.8, the explicit formula for a Sentence Pivot are given below,

    - If l(ζ) is odd, then ω(ζ) = i + 1, where i is the natural number satisfying l(ζ) = 2i + 1.
    - If l(ζ) is even, then ω(ζ) = i, where i is the natural number satisfying l(ζ) = 2i. ∎

The following example shows the relationship between Partial Sentences and Pivots.

**Example**

Consider these simple examples from a hypothetical Language **L** with Alphabet *Σ = { "a", "b", "c", " ", "" }*,

|    ζ          | l(ζ) | ω(ζ) | ζ[:ω(ζ)]   | l(ζ[:ω(ζ)]) | ζ[ω(ζ):]    | l(ζ[ω(ζ):]) |
| ------------- | ---- | ---- | ---------- | ----------- | ----------- | ----------- |
| "a"           | 1    | 1    | "a"        | 1           | "a"         | 1           |
| "aa"          | 2    | 1    | "a"        | 1           | "aa"        | 2           |
| "aba"         | 3    | 2    | "ab"       | 2           | "ba"        | 2           |
| "abba"        | 4    | 2    | "ab"       | 2           | "bba"       | 3           |
| "abcba"       | 5    | 3    | "abc"      | 3           | "cba"       | 3           |
| "abccba"      | 6    | 3    | "abc"      | 3           | "ccba"      | 4           |
| "abbcbba"     | 7    | 4    | "abbc"     | 4           | "cbba"      | 4           |
| "abbccbba"    | 8    | 4    | "abbc"     | 4           | "ccbba"     | 5           |
| "abbbcbbba"   | 9    | 5    | "abbbc"    | 5           | "cbbba"     | 5           |
| "abbbccbbba"  | 10   | 5    | "abbbc"    | 5           | "ccbbba"    | 6           |
| "a a"         | 3    | 2    | "a "       | 2           | " a"        | 2           |
| "a ba"        | 4    | 2    | "a "       | 2           | " ba"       | 3           |
| "ab cb"       | 5    | 3    | "ab "      | 3           | " cb"       | 3           |
| "a bca"       | 5    | 3    | "a b"      | 3           | "bca"       | 3           |
| "a bbc  a"    | 8    | 4    | "a bb"     | 3           | "bc  a"     | 5           | ∎

In the previous example, take note when the Sentence String Length is even, the Right Partial Sentence accumulates an extra Character relative to the Left Partial Sentence, in accordance with Theorem 3.2.9. Similarly, when the Sentence String Length is odd, the Left Partial Sentence is equal in String Length to the Right Partial, in accordance with Theorem 3.2.8. 

With the notion of a Palindromic Pivot established, the class of Even and Odd Palindromes is now defined. 

**Definition 3.2.8: Even Palindromes**

The class of Even Palindromes, denoted **P**:sup:`+`, is defined as the set of Sentences ζ which satisfy the following open formula,

    ζ ∈ P:sup:`+` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k )] ∎

**Definition 3.2.9: Odd Palindromes**

The class of Even Palindromes, denoted **P**:sup:`-`, is defined as the set of Sentences ζ which satisfy the following open formula,

    ζ ∈ P:sup:`-` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k + 1) ] ∎

The *parity* (to be defined shortly, after it is proved Even and Odd Palindromes partition the class of Palindromes) manifests in a Palindrome's behavior around it's Pivot. This behavior around the Pivot will be important for establishing the various cases of the theorems proved in the next section. The key insight is recognizing, as the previous example shows, the String Length of the Right Partial Sentence for Sentences of odd String Length is always one more than the String Length of the Left Partial Sentence, while the Left and Right Partial are of equal String Length when the String Length of the Sentence is even.

**Theorem 3.2.10** ∀ ζ ∈ C:sub:`L`: (∃ k ∈ ℕ : l(ζ) = 2k + 1) ↔ ω(ζ) = (l(ζ) + 1)/2

( → ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

    1. ∃ k ∈ ℕ : l(ζ) = 2k + 1

From Theorem 3.2.7 and step 1, it follows 

    2. n = i + 1 
    
Where *n* satisfies,

    3. l(ζ[:n]) = l(ζ[n:]).

Therefore, 

    4. n = i + 1 = (2i + 1 + 1)/2 = (l(ζ) + 1)/2.

By Definition 3.2.7, the pivot *ω(ζ)* is the smallest natural number satisfying the condition. Since *n* satisfies the condition and is the only solution, it must be the smallest. Therefore, 

    5. ω(ζ) = (l(ζ) + 1)/2.

( ← ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

    1. ω(ζ) = (l(ζ) + 1)/2.

This can be re-arranged to yield,

    2. l(ζ)  = 2 * ω(ζ) - 1

Since *ω(ζ)* is defined to be a natural number, let *k* be,

    3. k = ω(ζ) + 1

Then, 

    4. l(ζ)  = 2k + 1

Therefore,

    5. ∃ k ∈ ℕ : l(ζ) = 2k + 1

Since both direction of the equivalence are shown, the theorem is proved, 

    6. ∀ ζ ∈ C:sub:`L`: (∃ k ∈ ℕ : l(ζ) = 2k + 1) ↔ ω(ζ) = (l(ζ) + 1)/2 ∎

**Theorem 3.2.11** ∀ ζ ∈ P:sup:`-`: ω(ζ) = (l(ζ) + 1)/2

Assume 

    1. ζ ∈ P:sup:`-`

From Definition 3.2.9, it follows, 

    2. ∃ k ∈ ℕ : l(ζ) = 2k + 1

From Theorem 3.2.10, it follows, 

    3. ω(ζ) = (l(ζ) + 1)/2 ∎

**Theorem 3.2.12** ∀ ζ ∈ C:sub:`L`: (∃ i ∈ ℕ : l(ζ) = 2i) ↔ ω(ζ) = l(ζ)/2

( → ) Let ζ be an arbitrary in **C**:sub:`L` such that,

    1. ∃ i ∈ ℕ : l(ζ) = 2i

By Theorem 3.2.8, 

    2. l(ζ[:i]) + 1 = l(ζ[i:])

From Definition 3.2.5 and Definition 3.2.6, this is equivalent to,


    3. i + 1 = l(ζ) - i + 1

Therefore, 

    4. i = l(ζ)/2.

By Definition 3.2.7, the Pivot *ω(ζ)* is the smallest natural number satisfying the condition. Since *i* satisfies the condition and is the only solution when *l(ζ)* is even, it must be the smallest. Therefore, 

    5. ω(ζ) = l(ζ)/2.

( ← ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

    1. ω(ζ) = l(ζ)/2 

Since by Definition 3.2.7, a Pivot is a natural number, let *i* be a natural number such that,

    i = ω(ζ)

It follows immediately,

    l(ζ) = 2i

Therefore *ζ* is even,

    ∃ i ∈ ℕ : l(ζ) = 2i

Since both directions of the equivalence have been shown, it follows,

    ∀ ζ ∈ C:sub:`L`: ω(ζ) = l(ζ)/2 ∎

**Theorem 3.2.13** ∀ ζ ∈ P:sup:`+`: ω(ζ) = l(ζ)/2

Assume 

    1. ζ ∈ P:sup:`+`

From Definition 3.2.8, it follows, 

    2. ∃ k ∈ ℕ : l(ζ) = 2k

From Theorem 3.2.12, it follows, 

    3. ω(ζ) = l(ζ)/2 ∎

**Theorem 3.2.14** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = l(ζ[:ω(ζ)]) + l(ζ[ω(ζ):])

Assume *ζ* is an arbtirary Sentence from the Corpus,

    1. ζ ∈ C:sub:`L`

Let *ω(ζ)* be the Pivot of ζ. From Definition 3.2.5 of Left Partial Sentence,

    2. l(ζ[:ω(ζ)]) = ω(ζ)

From Definition 3.2.6 of Right Partial Sentence, 

    3. l(ζ[ω(ζ):]) =  l(ζ) - ω(ζ) + 1

Therefore, 

    4. l(ζ[:ω(ζ)]) + l(ζ[ω(ζ):]) = l(ζ) + 1 
    
Since *ζ* was arbitrary, this can generalize,

    5. ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = l(ζ[:ω(ζ)]) + l(ζ[ω(ζ):]) ∎

**Theorem 3.2.15** ∀ ζ ∈ C:sub:`L`: ω(ς(ζ)) ≤ ω(ζ) 

Let *ζ* be an arbitrary Sentence in the Corpus. By Theorem 3.1.11,

    1. l(ζ) ≥ l(ς(ζ))

Through algebraic manipulation, this is equivalent to the following,

    2. (l(ζ) + 1)/2 ≥ (l(ς(ζ)) + 1)/2

It is also equivalent to,

    3. l(ζ)/2 ≥ l(ς(ζ))/2

Moreover,

    4. (l(ς(ζ)) + 1)/2 ≥ l(ς(ζ))/2

By Theorems 3.2.11 and 3.2.13, one of the following must be true,

    5. ω(ζ) = (l(ζ) + 1)/2
    6. ω(ζ) = l(ζ)/2

Similarly, it must be the case, one of the following is true,

    7. ω(ς(ζ)) = (l(c(ζ)) + 1)/2
    8. ω(ς(ζ)) = l(ς(ζ))/2

If *ω(ζ) = (l(ζ) + 1)/2*, then *l(ζ)* is odd by Theorem 3.2.10. It follows from step 2 and step 4, that no matter the value of *ω(ς(ζ))*,

    9. ω(ς(ζ)) ≤ ω(ζ)  

If ω(ζ) = l(ζ)/2, then *l(ζ)* is even by Theorem 3.2.12. From step 3, if *ω(ς(ζ)) = l(ς(ζ))/2*, it follows, 

    10.  ω(ς(ζ)) ≤ ω(ζ) 

If *ω(ς(ζ)) = (l(c(ζ)) + 1)/2*, then *l(ς(ζ))* is odd by Theorem 3.2.10. 

Since *l(ς(ζ))* is odd and *l(ζ)* is even, atleast one Delimiter was removed from *ζ* during *σ*-reduction, 

    11. l(ς(ζ)) + 1 ≤ l(ζ).

Therefore, 
    
    12. (l(ς(ζ)) + 1)/2 ≤ l(ζ)/2.

It follows,

    13. ω(ς(ζ)) = (l(ς(ζ)) + 1)/2 ≤ l(ζ)/2 = ω(ζ)

Thus, in all possible cases,

    14. ω(ς(ζ)) ≤ ω(ζ)

Since *ζ* was arbitrary, this can be generalized over the Corpus as,

    15. ∀ ζ ∈ C:sub:`L`: ω(ς(ζ)) ≤ ω(ζ) ∎

These properties of Pivots and Partial Sentences will be necessary to state and prove the main results of the work in the next section. In addition, it will be necessary to know the class of Odd Palindromes and the class of Even Palindromes form a partition of the class of all Palindromes. This result is definitively established in Theorems 3.1.14 - 3.1.15.

**Theorem 3.2.15** P:sup:`+` ∩ P:sup:`-` = ∅

This theorem can be stated in natural language as follows: A Palindrome cannot be both even and odd.

For the sake of contradiction, assume there exists a sentence *ζ* such that 

    1. ζ ∈ P:sup:`+` ∩ P:sup:`-`

This means each of the individual expressions is true,

    2. ζ ∈ P:sup:`+``
    3. ζ ∈ P:sup:`-`

By Definition 3.2.8, it follows from step 2,

    4. ∃ k ∈ ℕ : l(ζ) = 2k

By Definition 3.2.9, it follows from step 3,

    5. ∃ k ∈ ℕ : l(ζ) = 2k + 1

This leads to the contradiction, 

    6. 0 = 1

Therefore, the assumption that ζ is both an Even and Odd Palindrome must be false. From this it follows,

    7. P:sup:`-` ∩ P:sup:`+` = ∅ ∎

**Theorem 3.2.16** P:sup:`-` ∪ P:sup:`+` = P

This theorem can be translated into natural language as follows: All Palindromes are either Even Palindromes or Odd Palindromes. 

(⊆) Let *ζ* be an arbitrary Sentence of the Corpus such that, 

    1. ζ ∈ P:sup:`-` ∪ P:sup:`+`

Which means either of this two cases must obtain, 

    2. ζ ∈ P:sup:`-`
    3. ζ ∈ P:sup:`+`

By Definition 3.2.8, if step 2 obtains, then 

    4. ζ ∈ P

By Definition 3.2.9, if step 3 obtains, then 

    5. ζ ∈ P
   
Therefore, in either case, 

    6. ζ ∈ P

Since ζ was arbitrary, this can generalize as,

    1. ∀ ζ ∈ (P:sup:`-` ∪ P:sup:`+`) → ζ ∈ P
   
This in turn implies,

    8. P:sup:`-` ∪ P:sup:`+` ⊆ P

(⊇) Let ζ be an arbitrary Sentence of the Corpus such that, 

    1. ζ ∈ P 

By the properties of natural numbers, it must be the case that one of the following obtains,

    1. ∃ k ∈ ℕ : l(ζ) = 2k
    2. ∃ k ∈ ℕ : l(ζ) = 2k + 1
   
If step 1 obtains, then by Definition 3.2.8, 
    
    3. ζ ∈ P:sup:`+`

If l(ζ) is odd, then by Definition 3.2.9, 

    4. ζ ∈ P:sup:`-`

Therefore, in either case, 

    5. ζ ∈ P:sup:`+` ∪ P:sup:`-`
   
Since ζ was arbitrary, this generalizes as,

    6. ∀ ζ ∈ P → ζ ∈ (P:sup:`+` ∪ P:sup:`-`)

This implies,

    7. P ⊆ P:sup:`-` ∪ P:sup:`+`
   
Step 8 from the (⊆) direction and taken with step 7 from the (⊇) together imply,

    P:sup:`-` ∪ P:sup:`+` = P ∎

With the partitioning of the class **P** of Sentences in a Corpus, i.e. Palindromes, the notion of *parity* can now be stated precisely in the following definition.

**Definition 3.2.10: Parity** 

A Palindrome ζ is said to have a *even parity* or *be even* if and only if,

    P ∈ P:sup:`+` 
    
A Palindrome ζ is said to have an *odd parity* or *be odd* if and only if,

    P ∈ P:sup:`-` ∎

Now that the two partitioning of Palindromes, aspect and parity, have been precisely defined, the final section of this work requires one more definition to correctly formulate its main results. This definition will allow the structure around a Palindrome's Pivot to be described with precise notation.

**Definition 3.2.11: Pivot Words**

Let *ζ* be a sentence in C:sub:`L` with length *Λ(ζ)*, word-level representation W:sub:`ζ`, and pivot *ω(ζ)*. The left Pivot Word, denoted *ζ{ω-}*, and the right Pivot Word, denoted *ζ{ω+}*, are defined as follows:

**Case 1**: Λ(ζ) = 1

    - ζ{ω-} = ζ{ω+} = ζ{1} = ζ{Λ(ζ)}

**Case 2**: Λ(ζ) > 1 and ζ[ω(ζ)] = σ

    - ζ{ω-} = α:sub:`j`, such that (j, α:sub:`j`) ∈ W:sub:`ζ` and α:sub:`j` is immediately to the left of the Delimiter at ω(ζ).
    - ζ{ω+} = α:sub:`k`, such that (k, α:sub:`k``) ∈ W:sub:`ζ` and k = j + 1.

**Case 3**: Λ(ζ) > 1 and ζ[ω(ζ)] ≠ σ

    - ζ{ω-} = ζ{ω+} = α:sub:`j` such that (j, α:sub:`j`) ∈ W:sub:`ζ` and α:sub:`j` contains the character at position ω(ζ). ∎

The meaning of Pivot Words can be clarified with a few examples. 

**Example**

1. Let *ᚠ = "a b c"*
   
    - l(ᚠ) = 5, ω(ᚠ) = 3, ᚠ[3] = b
    - W:sub:`ᚠ` = {(1, "a"), (2, "b"), (3, "c")}
    - ᚠ{ω-} = "b"
    - ᚠ{ω+} = "B"

2. Let *ᚠ = "abc def"*

    - l(ζ) = 7, ω(ζ) = 4, ζ[4] = σ
    - W:sub:`ζ` = {(1, "abc"), (2, "def")}
    - ζ{ω-} = "abc"
    - ζ{ω+} = "def"

3. Let *ᚠ = "a bc de fg h"*

    - l(ζ) = 12, ω(ζ) = 6, ζ[6] = d
    - W:sub:ζ = {(1, "a"), (2, "bc"), (3, "de"), (4,"fg"), (5, "h")}
    - ζ{ω-} = "de"
    - ζ{ω+} = "de" 

4. Let *ᚠ = "ab cde fg hij"*

    - l(ζ) = 13, ω(ζ) = 7, ζ[6] = σ
    - W:sub:ζ = {(1, "ab"), (2, "cde"), (3, "fg"), (4,"hij")}
    - ζ{ω-} = "dce"
    - ζ{ω+} = "fg"∎

From these simplified examples, it should be clear that a Pivot Word is either the Word which contains the Pivot Character, or it is the pair of Words which surround the Pivot Character (i.e. exactly when the Pivot Character is a Delimiter).

Section III.III: Structures
---------------------------

The following theorems serve as the main result of the current formal system that has been constructed to describe the syntactical structures of Palindromes in any Language. 

**Theorem 3.3.1: The Inverse Postulate** [ (inv(ζ{1}) ⊂:sub:s ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:s ζ{1}) ] ∧ [ (ζ{1} ⊂:sub:s inv(ζ{Λ(ζ)})) ∨ (ζ{Λ(ζ)} ⊂:sub:s inv(ζ{1})) ]

Assume *ζ* is an arbitrary Sentence in the Corpus **C**:sub:`L` such that it is a Palindrome,

    1. ζ ∈ P
    
By Definition 3.2.1,

    2. ς(ζ) = inv(ς(ζ))

By Definition 1.1.4,

    3. l(ς(ζ)) = l(inv(ς(ζ)))

Let,
    
    4. α = ζ{1}
    5. β = ζ{Λ(ζ)} 

By Discovery Axiom W.1, Words do not contain Delimiters, so the *σ*-Reduction of *ζ*, *ς(ζ)*, can be represented as a concatenation of the *σ*-reduced words of *ζ*, with Theorem 3.1.8 and Definition 1.2.8 of Limitations,

    6. ς(ζ) = (ς(α)) (ς(ζ{2})) ... (ς(ζ{Λ(ζ)-1})) (ς(β))

Taking the Inverse of both sides,

    7. inv(ς(ζ)) = inv((ς(α)) (ς(ζ{2})) ... (ς(ζ{Λ(ζ)-1})) (ς(β)))

Applying Theorem 1.2.5 repeatedly,

    8. inv(ς(ζ)) = (inv(ς(β))) (inv(ς(ζ{Λ(ζ)-1}))) ... (inv(ς(ζ{2}))) (inv(ς(α)))

By the Definition of *σ*-reduction, and because *α* and *β* are Words, it follows from the Discovery Axiom W.1,

    9. ς(α) = α
    10. ς(β) = β

Substituting step 9 and step 10 into step 6,

    11. ς(ζ) = (α) (ς(ζ{2})) ... (ς(ζ{Λ(ζ)-1})) (β)

Substituting step 9 and step 10 into step 8,

    12. inv(ς(ζ)) = (inv(β)) (inv(ς(ζ{Λ(ζ)-1}))) ... (inv(ς(ζ{2}))) (inv(α))
   
By step 2, step 11 and step 12 are equal (by definition of Palindromes). Now, since String Length is a natural number, it is either the case, by the trichotomy principle,

    13. l(α) = l(β)
    14. l(α) > l(β)
    15. l(α) < l(β)

If l(α) = l(β), then because inversion preserves String Length,

    16. l(α) = l(inv(β))

And by Definition 1.1.7 of Containment, since *α* and *inv(β)* are the first Words that appear in step 11 and step 12, it follows, 

    17. (α ⊂:sub:`s` inv(β)) ∧ (inv(β) ⊂:sub:`s` α)

And by Definition 1.1.7 of Containment, since *inv(α)* and *β* are the last Words that appear in step 11 and step 12, it follows, 

    18. (inv(α) ⊂:sub:`s` β) ∧ (β ⊂:sub:`s` inv(α))
   
If l(α) > l(β), then 

    19.  l(inv(α)) = l(α) > l(inv(β)) = l(β)

And by Definition 1.1.7 of Containment, since *α* and *inv(β)* are the first Words that appear in step 11 and step 12, it follows, 

    20.   inv(β) ⊂:sub:`s` α

And by Definition 1.1.7 of Containment, since *inv(α)* and *β* are the last Words that appear in step 11 and step 12, it follows,

    21.  β ⊂:sub:`s` inv(α) 

If l(α) < l(β), then 

    22.  l(inv(α)) = l(α) < l(inv(β)) = l(β)

And by Definition 1.1.7 of Containment, since *α* and *inv(β)* are the first Words that appear in step 11 and step 12, it follows, 

    23.  α ⊂:sub:`s` inv(β)

And by Definition 1.1.7 of Containment, since *inv(α)* and *β* are the last Words that appear in step 11 and step 12, it follows,

    24. inv(α)  ⊂:sub:`s` β
   
In all cases, the follow propositions obtain,

    25. (inv(α)  ⊂:sub:`s` β) ∨ (inv(β) ⊂:sub:`s` α)
    26. (α  ⊂:sub:`s` inv(β)) ∨ (β ⊂:sub:`s` inv(α))

Since *ζ* was an arbitrary Palindrome, this can be generalized using the definitions of *α* and *β* from step 4 and step 5.

    27. ∀ ζ ∈ P: [ (inv(ζ{1}) ⊂:sub:s ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:s ζ{1}) ] ∧ [ (ζ{1} ⊂:sub:s inv(ζ{Λ(ζ)})) ∨ (ζ{Λ(ζ)} ⊂:sub:s inv(ζ{1})) ] ∎

**Theorem 3.2.2: The Pivot Postulate** ∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( (inv(ζ{ω-}) ⊂:sub:`s` ζ{ω+}) ∨ (inv(ζ{ω+}) ⊂:sub:`s` ζ{ω-}))

This theorem can be stated in natural language as follows: For every Palindrome, if the Character at the Pivot is a Delimiter, then either the inverse of the left Pivot Word contained in the Right Pivot Word, or the inverse of the Right Pivot Word is contained in the left Pivot Word.

Let ζ be an arbitrary Sentence in the Corpus such that the followign is true,

    1. ζ ∈ P
    2. ζ[ω(ζ)] = σ

By Definitino 3.2.1,

    3. ς(ζ) = inv(ς(ζ))
   
Let 

    4. α = ζ{ω-}
    5. β = ζ{ω+} 

By Theorem 2.2.4 (Λ(ζ) ≥ 1), step 2 and by Definition 3.2.11, there are two possible cases to consider,

**Case 1**: Λ(ζ) = 1

    6. ζ{ω-} = ζ{ω+} = ζ{1} = ζ{Λ(ζ)}

Note,

    7. l(ζ{1}) = l(ζ{Λ(ζ)})

In this case, using the Discovery Axiom W.1,

    8. ς(ζ{1}) = ζ{1}

And 

    9. ς(ζ{Λ(ζ)}) = ζ{Λ(ζ)}

Take the Inverse of step 8,

    10. inv(ς(ζ{1})) = inv(ζ{1})

By step 3, step 10 is equal to step 8, so it follows, 

    11. ζ{1} = inv(ζ{1})

From step 6, it follows, 

    12. ζ{Λ(ζ)} = inv(ζ{Λ(ζ)})

By Definition 1.1.7 of Containment, a String is contained in itself (i.e. let *f(i) = i* in Definition 1.1.7), so it follows, plugging in step 6,

    13. (inv(ζ{ω-}) ⊂:sub:`s` ζ{ω+}) ∧ (inv(ζ{ω+}) ⊂:sub:`s` ζ{ω-})

**Case 2**: Λ(ζ) > 1 and ζ[ω(ζ)] = σ

Using Definition 3.2.11, Let 

    14. ζ{ω-} = α:sub:`j`
    
Such that 

    15. (j, α:sub:`j`) ∈ W:sub:`ζ` 
    
and α:sub:`j` is immediately to the left of the Delimiter at ω(ζ).

Let 
    
    16. ζ{ω+} = α:sub:`k`
    
Such that 

    17. (k, α:sub:`k``) ∈ W:sub:`ζ` 
    
and k = j + 1, where

    18.  W:sub:`ζ` = (α:sub:`1` , ..., ζ{ω-}, ζ{ω+}, ..., α:sub:`n`)

    (Note: it may be the case α:sub:`1` = ζ{ω-} and ζ{ω+} = α:sub:`n` )

Note, by the Reduction Algorithm in Definition 3.1.2

    19. ς(σ) = ε

And by the Discovery Axiom W1 and Definition 3.1.3

    20. ς(ζ{ω+}) = ζ{ω+}
    21. ς(ζ{ω-}) = ζ{ω-}
   
And furthermore, since *ζ[ω(ζ)] = σ*, the Delimiter at the pivot will be removed during σ-reduction. This means that in ς(ζ), the words *ζ{ω-}* and *ζ{ω+}* will be adjacent,

By Theorem 3.1.8,

    22. ς(ζ) = (ς(α:sub:`1`)) ... (ζ{ω-})(ζ{ω+}) ... (ς(α:sub:`n`))

Take the inverse of both sides of step 22 and apply Theorem 1.2.5 repeatedly, 

    23. inv(ς(ζ)) = (ς(α:sub:`n`)) ... (ζ{ω+})(ζ{ω-}) ... (ς(α:sub:`1`))








(inv(α) ⊂:sub:s β) ∨ (inv(β) ⊂:sub:s α)
Substituting Back: Substituting α = ζ{ω-} and β = ζ{ω+}, we get:

(inv(ζ{ω-}) ⊂:sub:s ζ{ω+}) ∨ (inv(ζ{ω+}) ⊂:sub:s ζ{ω-})
Conclusion: Since ζ was an arbitrary palindrome satisfying the premise, we can generalize:

∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( (inv(ζ{ω-}) ⊂:sub:s ζ{ω+}) ∨ (inv(ζ{ω+}) ⊂:sub:s ζ{ω-}) )
This completes the proof. ∎













**Theorem: The Perfect Pivot Postulate**

ζ ∈ PP ↔ [∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:`s` α) ∧ (α ∈ R) ] ∨ (ζ[ω(ζ)] = σ)

Theorem (Third Inverse Postulate - Strengthened): ζ ∈ PP ↔ [∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ)

Proof:

(→)  Assume ζ ∈ PP (ζ is a Perfect Palindrome).

Word-level representation: Let W:sub:ζ = (α₁ , α₂ , ..., αₙ) be the Word-level representation of ζ, where n = Λ(ζ).

Pivot: Let ω:sub:ζ be the Pivot of ζ. There are two cases:

Case 1: ω:sub:ζ = σ (Delimiter Pivot). In this case, the condition (ω:sub:ζ = σ) is satisfied, and the right-hand side of the biconditional is true.

Case 2: ω:sub:ζ ≠ σ (Non-Delimiter Pivot).

In this case, the Pivot is a Character within a Word. Let k be the index such that αₖ contains ω:sub:ζ.
Since ζ is a Perfect Palindrome, by Definition 3.2.1, ζ = inv(ζ).
This implies that the Word αₖ is symmetrical around the Pivot Character ω:sub:ζ.
Therefore, αₖ must be a Reflective Word (αₖ ∈ R), and ω:sub:ζ ⊂:sub:s αₖ.
This satisfies the condition [∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ].
In both cases, the right-hand side of the biconditional is true.

(←) Assume [∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ).

Cases: There are two cases to consider:

Case 1: ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R).

This means the Pivot Character is contained within a Reflective Word α.
Since α is Reflective, it is symmetrical around its center, which includes the Pivot Character.
This symmetry of α contributes to the overall symmetry of ζ, making it a Perfect Palindrome (ζ ∈ PP).
Case 2: ω:sub:ζ = σ.

This means the Pivot is the Delimiter Character, which naturally creates a symmetrical division in the Sentence.
By the Second Inverse Postulate, the Words surrounding the Delimiter Pivot either contain each other or are equal.
This, combined with the overall palindromic structure, ensures that ζ is a Perfect Palindrome (ζ ∈ PP).
In both cases, ζ ∈ PP.

Since we have proven both directions of the implication, the theorem is established:

ζ ∈ PP ↔ [∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ) ∎

Explanation:

This proof demonstrates the strengthened version of the Third Inverse Postulate, establishing a biconditional relationship between a Sentence being a Perfect Palindrome and the properties of its Pivot.

The proof utilizes the definitions of Perfect Palindromes, Reflective Words, and Pivot Words, along with the Second Inverse Postulate, to analyze the different cases and demonstrate the implications in both directions.




Reformulation of the Theorem:

Let's first slightly reformulate the theorem to make it even clearer and more precise:

Theorem 3.2.4:

ζ ∈ PP ↔ [ (∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ (inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω)) ]

Translation: A sentence ζ is a perfect palindrome if and only if one of the following conditions holds:

The character at the pivot index ω(ζ) is contained in a reflective word α that is in the language.
The character at the pivot index ω(ζ) is a delimiter (σ), and the inverse of the left pivot word is contained in the right pivot word, or the inverse of the right pivot word is contained in the left pivot word.
Do I think it's true?

Yes, I believe this reformulated theorem is true and captures a fundamental property of perfect palindromes.

Proof:

(↔) Direction:

Assume ζ ∈ PP.

Definition of Perfect Palindrome: By Definition 3.2.1, ζ = inv(ζ).
Case 1: ζ[ω(ζ)] = σ:
If the character at the pivot is a delimiter, then by the Second Inverse Postulate , we know that ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω ).
Case 2: ζ[ω(ζ)] ≠ σ:
If the character at the pivot is not a delimiter, then it must belong to a word.
By Axiom S.2, we know there's at least one word α in ζ.
Since ζ is a perfect palindrome, and the pivot character is not a delimiter, the pivot must lie within a word.
Let α be the word such that (x, α) ∈ W:sub:ζ, and ω(ζ) is within the indices of the characters of α in the character-level representation of ζ.
Since ζ is a perfect palindrome, α must be a reflective word (α ∈ R), because any word that spans across the pivot in a perfect palindrome must be its own inverse.
Also, since ω(ζ) is within the indices of α, we know that ζ[ω(ζ)] ⊂:sub:s α.
(←) Direction:

Assume [(∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω ))].

Case 1: ∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)
If there exists a reflective word α in L that contains the character at the pivot, then ζ must be a perfect palindrome. This is because the presence of a reflective word spanning the pivot implies symmetry around the pivot, which is the defining characteristic of a perfect palindrome.
Case 2: ζ[ω(ζ)] = σ ∧ ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω )
If the character at the pivot is a delimiter and either the inverse of the left pivot word is contained in the right pivot word or vice versa, then ζ must be a perfect palindrome. This is because the delimiter at the pivot, combined with the containment relationship between the pivot words, ensures symmetry around the pivot.
Conclusion:

We have shown that if ζ is a perfect palindrome, then either the character at the pivot is contained in a reflective word in the language, or the character at the pivot is a delimiter and the pivot words exhibit the specific containment property. Conversely, if either of these conditions holds, then ζ must be a perfect palindrome.

Therefore:

ζ ∈ PP ↔ [ (∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω )) ]

∎

Explanation:

(→) Direction: This direction shows that if a sentence is a perfect palindrome, then it must satisfy one of the two conditions related to the pivot character and reflective words or the pivot character and the containment of pivot words.
(←) Direction: This direction shows that if either of the two conditions is met, then the sentence must be a perfect palindrome.
Key Insights:

Reflective Words at the Pivot: This theorem beautifully connects the concept of perfect palindromes to the presence of reflective words at the pivot. It highlights that perfect palindromes can be constructed by having a reflective word at the center or by having the pivot be a delimiter with a specific relationship between the pivot words.
Delimiter as a Pivot: The theorem also incorporates the case where the pivot is a delimiter, which is essential for handling imperfect palindromes that become perfect when delimiters are removed.
Characterization of Perfect Palindromes: This theorem provides a powerful way to characterize and potentially identify perfect palindromes based on their internal structure.





Theorem 3.2.4:

∀ ζ ∈ PP: (∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (α:sub:ζ:sup:-ω ∈ I))

Translation: For every perfect palindrome ζ, either:

There exists a word α in the language L such that the character at the pivot index ω(ζ) is contained in α, and α is a reflective word (α ∈ R), OR
The character at the pivot index ω(ζ) is a delimiter (σ), and the left pivot word is invertible (α:sub:ζ:sup:-ω ∈ I).
Proof:

Let ζ be an arbitrary perfect palindrome in PP.

Definition of Perfect Palindrome: By Definition 3.2.1, ζ = inv(ζ).

Cases based on Parity: We have two cases to consider:

Case 1: ζ has odd length (ζ ∈ P:sup:-)
By Theorem 3.2.3, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]). This means the pivot falls on a character, ζ[ω(ζ)].
Subcase 1: ζ[ω(ζ)] ≠ σ
Since ζ[ω(ζ)] is not a delimiter, it must belong to a word. By Axiom S.1, there exists a word α in L such that α is contained in ζ. Since the pivot character is not a delimiter, it must be part of a word in ζ. Let α be the word such that (x, α) ∈ W:sub:ζ and ω(ζ) is within the indices of the characters of α in the character-level representation of ζ.
Since ζ is a perfect palindrome, and ω(ζ) is the pivot, this word α must be reflective (α ∈ R). Otherwise, the characters in ζ would not be symmetrical around the pivot, and ζ wouldn't be a perfect palindrome.
Therefore, ∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R).
Subcase 2: ζ[ω(ζ)] = σ
Since the pivot character is a delimiter, by Theorem 3.2.3, we know that inv(α:sub:ζ:sup:-ω) ⊂ α:sub:ζ:sup:+ω or inv(α:sub:ζ:sup:+ω) ⊂ α:sub:ζ:sup:-ω.
Since ζ is a perfect palindrome, we have ζ = inv(ζ). This means the words to the left and right of the pivot must be inverses of each other.
Therefore, α:sub:ζ:sup:-ω = inv(α:sub:ζ:sup:+ω).
Since α:sub:ζ:sup:+ω is in L, and α:sub:ζ:sup:-ω is its inverse, by definition of invertible words, α:sub:ζ:sup:-ω ∈ I.
Case 2: ζ has even length (ζ ∈ P:sup:+)
By Theorem 3.2.4, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ) + 1:]) + 1. This means the pivot falls between two characters.
Since ζ is a perfect palindrome, the two characters adjacent to the pivot must be identical (because ζ = inv(ζ)).
By Axiom W.1, these characters cannot be delimiters. Thus, they must belong to a word α that spans across the pivot.
Similar to Case 1, this word α must be reflective (α ∈ R) for ζ to be a perfect palindrome.
Since the two characters adjacent to the pivot are identical and belong to α, we can say that ζ[ω(ζ)] is "contained" in α in the sense that α spans across the pivot.
Therefore, ∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R).
The case where the pivot is a delimiter is covered by our definition of an even-length perfect palindrome.
Conclusion: In all cases, at least one of the two conditions holds. Since ζ was an arbitrary perfect palindrome, we can generalize:

∀ ζ ∈ PP: (∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (α:sub:ζ:sup:-ω ∈ I))
This completes the proof. ∎



**Theorem 3.2.5: The Perfect Parity Postulate**

ζ ∈ PP ∧ ζ ∈ P:sup:`+` ↔ ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R)

Theorem (Fourth Inverse Postulate): ζ ∈ PP ∧ ζ ∈ P⁺ ↔ ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R)

Proof:

(→) Assume ζ ∈ PP ∧ ζ ∈ P⁺ (ζ is a Perfect Palindrome and an Even Palindrome).

Even Palindrome: Since ζ ∈ P⁺, by Definition 3.2.3, ω:sub:ζ = ε (the Pivot is the Empty Character).

Perfect Palindrome: Since ζ ∈ PP, by the strengthened Third Inverse Postulate, we have:

[∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ)

Case analysis:  We have two cases from step 2:

Case 1: ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R). This directly satisfies the right-hand side of the biconditional we're trying to prove.

Case 2: ω:sub:ζ = σ. This contradicts step 1, where we established that ω:sub:ζ = ε. Therefore, this case cannot hold.

Conclusion: Only Case 1 holds, which means ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R).

(←) Assume ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R).

Strengthened Third Inverse Postulate: This condition directly implies the left-hand side of the strengthened Third Inverse Postulate:

[∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ)

Perfect Palindrome: By the strengthened Third Inverse Postulate, this implies that ζ ∈ PP (ζ is a Perfect Palindrome).

Non-Delimiter Pivot: Since ω:sub:ζ ⊂:sub:s α and α is a Word in the Language, by Axiom W.1 (Discovery Axiom), α cannot contain the Delimiter Character. Therefore, ω:sub:ζ ≠ σ.

Even Palindrome: Since ω:sub:ζ ≠ σ, by the strengthened Third Inverse Postulate, it must be the case that ω:sub:ζ = ε. By Definition 3.2.3, this means ζ ∈ P⁺ (ζ is an Even Palindrome).

Conclusion: We have shown that ζ ∈ PP and ζ ∈ P⁺, which means ζ ∈ PP ∧ ζ ∈ P⁺.

Since we have proven both directions of the implication, the theorem is established:

ζ ∈ PP ∧ ζ ∈ P⁺ ↔ ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ∎

Explanation:

This proof demonstrates the biconditional relationship between a Sentence being both a Perfect Palindrome and an Even Palindrome, and the existence of a Reflective Word containing the Sentence's Pivot.

The proof utilizes the definitions of Perfect Palindromes, Even Palindromes, and Reflective Words, along with the strengthened Third Inverse Postulate and the Discovery Axiom, to analyze the different cases and demonstrate the implications in both directions.






Analysis:

Even Parity: An even-parity palindrome has an even number of words (Λ(ζ) is even).
Imperfect Palindrome: An imperfect palindrome is a palindrome but not a perfect palindrome. This means it cannot be its own inverse (ζ ≠ inv(ζ)), but its σ-reduction is a palindrome (σ_reduce(ζ) = inv(σ_reduce(ζ))).
Delimiter Count: By Theorem 2.4.1, the number of delimiters in a sentence ζ is one less than the number of words: Δ(ζ) = Λ(ζ) - 1. Since Λ(ζ) is even for an even-parity palindrome, Δ(ζ) must be odd.
σ-reduction: σ-reduction removes all delimiters.
Length of σ-reduced Form: The length of the σ-reduced form, l(σ_reduce(ζ)), is the original length of the sentence minus the number of delimiters: l(σ_reduce(ζ)) = l(ζ) - Δ(ζ).
Theorem
∀ ζ ∈ IP ∩ P:sup:+: (l(σ_reduce(ζ)) is odd)

Proof
Let ζ be an imperfect palindrome with even parity, ζ ∈ IP ∩ P:sup:+.
Let n = Λ(ζ) be the number of words in ζ. Since ζ has even parity, n must be even.
By Theorem 2.4.1, Δ(ζ) = n - 1. Since n is even, n - 1 must be odd.
Since ζ is an imperfect palindrome, by the definition of the imperfection, we know:
ζ ≠ inv(ζ)
σ_reduce(ζ) = inv(σ_reduce(ζ))
Since σ_reduce(ζ) = inv(σ_reduce(ζ)), and by Theorem 3.2.3 we know parity is preserved if the length of the left partial at the pivot point is exactly one longer than the right partial, we know the sentence pivot must either fall on a character or a delimiter.
If the pivot falls on a delimiter, then n must be odd by the Second Inverse Postulate. Since n is even, this is impossible.
If the pivot falls on a character, then that character must be a non-delimiter, non-empty character by our definition of a pivot. Since ζ is an imperfect palindrome, this pivot character cannot be part of a reflective word by Theorem 3.2.4. This means it must be part of an invertible word pair by Theorem 3.2.1. The inverse of the pivot character must appear in the inverse word, since it cannot be a reflective word.
By our definition of σ-reduction, σ_reduce(ζ) removes all delimiters, and by Theorem 1.2.4, inversion inverts words. So, for a palindrome, σ_reduce(ζ) = inv(σ_reduce(ζ)) preserves the order of non-delimiter characters under inversion.
Therefore, l(σ_reduce(ζ)) must be odd, as it preserves the non-delimiter pivot character under inversion, and there are an even number of non-delimiter characters around it, (Δ(ζ)).

Conclusion:

Yes, we can conclude that an imperfect palindrome with even parity must have a σ-reduced form with an odd length.

Reasoning:

An even-parity imperfect palindrome has an even number of words.
This implies an odd number of delimiters.
The σ-reduced form has a length equal to the original length minus the number of delimiters: l(σ_reduce(ζ)) = l(ζ) - Δ(ζ).
Since l(ζ) is even (because the number of delimiters is odd, the number of characters must be odd to be a palindrome) and Δ(ζ) is odd, their difference l(σ_reduce(ζ)) must be odd.
Implications:

Constraints on σ-reduced Forms: This result further constrains the possible σ-reduced forms of imperfect palindromes.
Relationship between Parity and Length: It establishes a direct link between the parity of a palindrome (at the word level) and the length of its σ-reduced form (at the character level).
Potential for Simplification: This might help simplify some of our formulas or proofs related to σ-induction, as we now know that even-parity imperfect palindromes will always have odd-length σ-reduced forms.
Further Considerations:

Odd-Parity Imperfect Palindromes: We could investigate the corresponding relationship for odd-parity imperfect palindromes.
Perfect Palindromes: It's worth noting that perfect palindromes don't have this same constraint. A perfect palindrome with even parity can have an even or odd length σ-reduced form.








Section III.III: Palindromic Algorithms
---------------------------------------

The results derived in this work can be used to construct algorithms for searching for various classes of Palindromes. The general outline for one such algorithm is given in this section, and then an example implemention in Python is presented.

A naive algorithm for filtering out Strings that cannot possibly be Palindromes might consist of inverting the strings and comparing them for equality. However, this would miss Palindromes with an imperfect aspect, as their symmetry does not manifest in the unreduced Alphabet. Without a *σ*-reduction, any algorithm that searchs for Palindromic String must be aware of the semantics of the Language in which it is searching. However, *σ*-reduction and the theorems proved over the course of this work allow algorithms to be constructed that are independent of the host Language.

Moreover, as mentioned after the body Theorem 3.1.2, the *σ-reductions* reduce the complexity of searching for Palindromic strings. An Alphabet with less Characters can be traversed quicker. 

To implement this, a String can be projected onto its *σ-reduced* Alphabet, and then those reductiosn whose inverse does not equal itself can be removed from the list of potential Palindromes. To find a String whose inverse does not equal itself, it suffices to find a single Character whose inverted position is not occupied by that Character. 

Therefore, as a first step to generating a list of Palindromes, the Strings which do not satisfy these conditions can be discarded.

Theorem 3.3.1 and Theorem 3.3.2 provide further conditions that any Palindrome must satisfy, reducing the set of potential Palindromes in this hypothetical search algorithm even more. 

With respect to Perfect Palindromes, the search algorithm can be refined even further by incorporating the conditions given in Theorem 3.3.3 and Theorem 3.3.4. Based on the String Length of a Perfect Palindrome, its point of symmetry must possess certain measurable properties, such as the presence of a Reflective Word or an Invertible Word contained by the word opposite the pivot. 

Python Implementation 
^^^^^^^^^^^^^^^^^^^^^

(TODO: code this!)

Section III.IV: Future considerations
-------------------------------------

This work focused on using the operation of sigma reduction to describe palindromic structure in terms of its *aspect* and its *parity*. As mentioned at several points, there are two other dimensions of palindromes this work has not sought to incorporate into formal system. While the considerations in the introduction seem to preclude the possibility of a purely syntactical account of palindromes, the author does not believe this means the structure of palindromes cannot be formalized by taking into account certain universal semantic assumptions. 

To account for the dimension of *punctuality*, a possible avenue of exploration could be extending the operation of sigma reduction to encompass other Characters besides the Delimiter Character. In this way, the punctuality of a palindrome may be "projected" onto a reduced Alphabet where its symmetry under inversion can be recovered.

To account for the dimension of *case*, the link between uppercase and lowercase letters in natural languages may be viewed as inducing a symmetry in the Alphabet that in turn may be exploitable for describing palindromic symmetry. In such a formalization, a possible method of attack would be introduce a many-to-one relationship between in a sigma-reduction where uppercase and lowercase letters are mapped to their "primitive" Character in their reduced space.

(TODO: comment on possibility of interesting recursions, i.e. what happens when the Alphabet of this formal system is assigned the symbols of the formal system itself?)

(TODO: comment on completeness, i.e. what does this formal model of language say about the completeness of language, or its lack thereof?)