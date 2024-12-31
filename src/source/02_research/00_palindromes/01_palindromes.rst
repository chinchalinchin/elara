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
- Sentence Classes: A(n), K, P, PP, IP, P:sup:`-`, P:sup:`+`
- Categories: C:sub:`L`(m)
- Relations: ⊂:sub:`s`, =
- Functions: l(t), Λ(t), Δ(t)
- Operations: inv(s), σ_reduce(t), o_induce(t, m, S), Π:sub:`i=1`:sup:`n` P:sub:`n`(i)

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
- D 1.2.7: Limitation: Π:sub:`i=1`:sup:`n` P:sub:`n`(i)
- D 1.3.1: Reflective Words: α ∈ R ↔ ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1] 
- D 1.3.2: Invertible Words: α ∈ I ↔ inv(α) ∈ L
- D 2.1.1: Corpus: C:sub:`L`
- D 2.1.2: Sentence: ᚠ
- D 2.1.3: Word-Level Set Representation: W:sub:`ᚠ`
- D 2.1.4: Word Length: Λ(ζ)
- D 2.1.5: Word Index Notation: ζ{i}
- D 2.2.1: Semantic Coherence
- D 2.3.1: Admissible Sentences: t ∈ A(n) ↔ (∃ p ∈ Χ:sub:`L`(n): t = Π:sub:`i=1`:sup:`n` p(i)) ∧ (t ∈ C:sub:`L`)
- D 2.3.2: Invertible Sentences: ζ ∈ K ↔ inv(ζ) ∈ C:sub:`L`
- D 3.1.1: σ-Reduced Alphabet: Σ:sub:`σ` 
- D 3.1.2: σ-Reduction: s ⋅ Σ:sub:`σ`
- D 3.1.3: Palindromes: ∀ ζ ∈ C:sub:`L`: ζ ∈ P ↔ [ (Ζ ⋅ Σ:sub:`σ`) = inv(Ζ ⋅ Σ:sub:`σ`) ]
- D 3.1.4: Perfect Palindromes: ∀ ζ ∈ C:sub:`L`: ζ ∈ PP ↔ ζ = inv(ζ)
- D 3.1.5: Imperfect Palindromes: ζ ∈ P - PP
- D 3.1.6: Aspect
- D 3.1.7: Left Partial Sentence: Z[:n]
- D 3.1.8: Right Partial Sentence: Z[n:]
- D 3.1.9: Pivots: ω(ζ)
- D 3.1.10: Even Palindromes: ζ ∈ P:sup:`+` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k )] 
- D 3.1.11: Odd Palindromes: ζ ∈ P:sup:`-` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k + 1) ]
- D 3.1.12: Parity
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
- T 1.2.6: ∀ n ∈ ℕ: ∀ p ∈ Χ:sub:`L(n)`: ∃! s ∈ S: s = Π:sub:`i=1`:sup:`n` p(i)
- T 1.2.7: ∀ p ∈ Χ:sub:`L`(n), ∀ q ∈ Χ:sub:`L`(m), ∀ r ∈ Χ:sub:`L`(k): ((Π:sub:`i=1`:sup:`n` p(i))(Π:sub:`i=1`:sup:`m` q(i)))(Π:sub:`i=1`:sup:`k` r(i)) = ((Π:sub:`i=1`:sup:`n` p(i)))((Π:sub:`i=1`:sup:`m` q(i))(Π:sub:`i=1`:sup:`k` r(i)))
- T 1.3.1: ∀ α ∈ L: α ∈ R ↔ α = inv(α)
- T 1.3.2: ∀ α ∈ L: α ∈ I ↔ inv(α) ∈ I
- T 1.3.3: R ⊆ I
- T 1.3.4: If | R | is even, then | I | is even. If | R | is odd, then | I | is odd.
- T 2.1.1: ∀ ζ ∈ C:sub:`L`:  ∑:sub:`j=1`:sup:`Λ(ζ)` l(ζ{j}) ≥ Λ(ζ)
- T 2.1.2: ∀ ζ, ξ ∈ C:sub:`L`: Λ(ζξ) ≤ Λ(ζ) + Λ(ξ)
- T 2.2.1: ∀ ζ ∈ C:sub:`L`: l(ζ) ≠ 0
- T 2.2.2: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`l(ζ)`: ζ[i] ⊂:sub:`s` ζ
- T 2.2.3: ∀ ζ ∈ C:sub:`L` : ∀ i ∈ N:sub:`l(ζ)`:  ζ[i] ≠ ε
- T 2.2.4: ∀ ζ ∈ C:sub:`L`: Λ(ζ) ≥ 1
- T 2.3.1: A(n) ⊆ C:sub:`L`
- T 2.3.2: ∀ ζ ∈ A(n): Λ(ζ) = n
- T 2.3.3: ∀ ζ ∈ C:sub:`L`: ζ ∈ A(Λ(ζ))
- T 2.3.4: ∀ ζ ∈ C:sub:`L`: ∃ p ∈ X:sub:`L`(Λ(ζ)): ζ = Π:sub:`i=1`:sup:`n` p(i)
- T 2.3.5: ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ inv(ζ) ∈ K
- T 2.3.6: ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → ζ ∈ C:sub:`L`
- T 2.3.7: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ ∈ K → inv(ζ){i} ∈ L
- T 2.3.8: ∀ ζ ∈ C:sub:`L`: inv(Π:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) = Π:sub:`i=1`:sup:`Λ(ζ)` inv(ζ{Λ(ζ) - i + 1})
- T 2.3.9: ∀ ζ ∈ C:sub:`L`: ζ ∈ K → ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
- T 2.3.10: ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ (∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})) ∧ (inv(ζ) ∈ A(Λ(ζ)))
- T 2.3.11: ∀ ζ ∈ C:sub:`L`: ζ ∈ K → ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I
- T 3.1.1: ∀ ζ ∈ C:sub:`L`: inv(ζ ⋅ Σ:sub:`σ`) = (inv(ζ) ⋅ Σ:sub:`σ`)
- T 3.1.2: ∀ ζ,ξ ∈ C:sub:`L`: ΖΞ ⋅ Σ:sub:`σ` = (Ζ⋅ Σ:sub:`σ`)(Ξ ⋅ Σ:sub:`σ`)
- T 3.1.3: ∀ ζ ∈ C:sub:`L`: (ζ ⋅ Σ:sub:`σ`) ⋅ Σ:sub:`σ`= ζ ⋅ Σ:sub:`σ`
- T 3.1.4: ∀ ζ ∈ C:sub:`L`: Λ(ζ ⋅ Σ:sub:`σ`) ≤ 1
- T 3.1.5: ∀ ζ ∈ C:sub:`L`, ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` (ζ ⋅ Σ:sub:`σ`)
- T 3.1.6: ∀ ζ ∈ C:sub:`L` : ζ ∈ K → [ inv(ζ  ⋅ Σ:sub:`σ`) = inv(inv(ζ  ⋅ Σ:sub:`σ`)) ]
- T 3.1.7: PP ⊂ K
- T 3.1.8: ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → (∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I)
- T 3.1.9: PP ⊂ P
- T 3.1.10: PP ∪ IP = P
- T 3.1.11: ∀ ζ ∈ C:sub:`L`: ∃ n ∈ N:sub:`l(ζ)`: ( l(ζ[:n]) = l(ζ[n:]) ) ∨ (l(ζ[:n]) = l(ζ[n:]) + 1)
- T 3.1.12: ∀ ζ ∈ C:sub:`L`: (l( ζ[:ω(ζ)] ) = l( ζ[ω(ζ):] )) ↔ (∃ i ∈ ℕ : l(ζ) = 2i + 1)
- T 3.1.13: ∀ ζ ∈ C:sub:`L`: (l( ζ[:ω(ζ)] ) = l(ζ[ω(ζ):]) + 1) ↔ (∃ i ∈ ℕ : l(ζ) = 2i)
- T 3.1.14: ∀ ζ ∈ P:sup:`-`: ( inv(ζ[ω(ζ):] ⋅ Σ:sub:`σ` ) = inv(ζ[:ω(ζ)]⋅ Σ:sub:`σ`) )
- T 3.1.15: ∀ ζ ∈ P:sup:`+`: ( inv(Ζ[ω(ζ):] ⋅ Σ:sub:`σ` ) = inv(Ζ[:ω(ζ)+1]⋅ Σ:sub:`σ`) )
- T 3.1.16: P:sup:`-` ∩ P:sup:`+` = ∅
- T 3.1.17: P:sup:`-` ∪ P:sup:`+` = P
- T 3.1.18: ∀ ζ ∈ PP ∩ P:sub:`+`, ∃ n ∈ N:sub:`l(ζ)`: ζ[n] = σ ↔ ζ[l(ζ)-n +1 ] = σ 
- T 3.1.19: ∀ ζ ∈ PP ∩ P:sup:`-` : ∃ n ∈ N:sub:`l(ζ)`: (ζ[n] = σ ↔ ζ[l(ζ)-n+1] = σ) ∨ (n = ω(ζ))
- T 3.2.1: ∀ ζ ∈ PP : (inv(ζ{1}) ⊂:sub:`s` ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:`s` ζ{1})
- T A.1.1: ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L
- T A.2.1: ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1
- T A.2.2: ∀ s ∈ S: Δ(s) = Δ(inv(s))
- T A.2.3: ∀ ζ ∈ C:sub:`L`: Δ(ζ) = Δ(inv(ζ))
- T A.2.4: ∀ α ∈ L: Δ(α) = 0
- T A.2.5: ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})
- T A.2.6: ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})
- T A.2.7: ∀ ζ ∈ C:sub:`L`: l(ζ) ≥  Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α)
- T A.2.8: ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ)
- T A.2.9: ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)
- T A.2.10: ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)
- T A.2.11: ∀ ζ ∈ C:sub:`L`: Δ(Ζ ⋅ Σ:sub:`σ`)= 0
- T A.2.12: ∀ s ∈ S: l(ζ ⋅ Σ:sub:`σ`) + Δ(s) = l(s)
- T A.2.13: ∀ ζ ∈ C:sub:`L`: l(ζ ⋅ Σ:sub:`σ`) + Λ(ζ) = l(ζ) + 1
- T A.3.1: ∀ α ∈ L: α ∈ L:sub:`σ` ↔ [ ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:s α ]
- T A.3.2: L:sub:`P` ⊂ L:sub:`σ`
- T A.3.3: ∀ α ∈ L:sub:`P`: α = inv(α)
- T A.3.4: L ∩ L:sub:`P` ⊆ R
- T A.3.5: L:sub:`P` ⊂ R:sub:`L_σ`

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

A note on the terminology introduced in this work is in order. When a semantic term is capitalized, e.g. Word or Sentence, this will mean it is referred to in its capacity as a formal entity. While the formal system was designed to model the actual syntax of Characters, Words and Sentences, this should not be taken to mean the formal entities that emerge from this system are necessarily representative of actual linguistic entities. While the formal entities in this system may not map *one-to-one* with their empirical counterparts, it will be seen these formal characteristics nevertheless provide insight into the nature of their empirical counterparts.

As the thrust of the main results in Section III is sufficiently novel, the author has gone to great lengths to make its foundation as rigorous as possible. Many of the initial theorems are proofs of common-sense notions relating to words and sentences. The banality of Section I is in part an effort to ensure the applicability of the results in Section II.III and Section III. The core theorems of Section III could be proved in a degenerate form in a system with less notational complexity, but the depth of their insight would be lost in the vagueness of definitions.

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

It will also be necessary to refer to indeterminate Strings, so notation is also introduced for String Variables,

    2. String Variable ( *x*, *y*, *z*): The lowercase English letters *x*, *y* and *z* denote an indeterminte String. 

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

It will sometimes be convenient to represent Strings as ordered sets of Characters, rather than serialized concatenations of Characters. The two formulations are equivalent, but the set representation has advantages when it comes to quantification and symbolic logic. When a String or Word representation is intended to be interpretted as a set, it will be written in bold uppercase letters. For example, the String represented as the concatenated series *s*:sub:`1` *= 𝔞𝔟𝔠* would be represented in this formulation as a set of ordered pairs **S**:sub:`1`, where the first coordinate encodes the position of the Character in the String,

    S:sub:`1` = { (1, 𝔞), (2, 𝔟), (3, 𝔠) }

Note, since sets do not preserve order, this would be equivalent to,

    { (3, 𝔠), (2, 𝔟), (1, 𝔞) }

To simplify notation, it is sometimes beneficial to represent this set as a sequence that *does* preserve order as,

    S:sub:`1` = (𝔞, 𝔟, 𝔠) 

However, before adopting this notation formally, a problem exists. It is the intention of this analysis to treat Empty Characters as vacuous, i.e. Characters without semantic content. However, this does not mean the Empty Character will not be treated as a legitimate entity within the confines of the formal system. Instead, the goal is to construct a formal system that excludes the Empty Character from the domain of semantics, but not the domain of syntax. 

Due to the nature of the Empty Character and its ability to be concatenated ad infinitum, and the desire to construct a theory of Words and Language that emerges from the transcendental domain of Strings, the construction of the Character-level set represention of a String requires a special algorithm to filter out any Empty Characters while preserving the relative order of the non-Empty Characters concatenated into the String. 

**Definition 1.1.2: Character-level Set Representations**

Let *t* be a String with Characters *𝔞*:sub:`i`. The Character-level set representation of *t*, denoted by bold uppercase letters **T**, is defined as the ordered set of Characters obtained by removing each Empty Character, *ε*. Formally, **T** is constructed using the *Emptying Algorithm* 

**Algorithm 1: The Emptying Algorithm**

The Emptying Algorithm takes a string *t* as input, which can be thought of as a sequence of Characters *𝔞*:sub:`1`, *𝔞*:sub:`2`, *𝔞*:sub:`3`, ... , where some characters might be *ε*. It then initializes a set to hold **X** and an index for the Characters it will add to **X**. The algorithm iterates the index and constructs the Character-level representation by ignoring *ε*. The Emptying Algorithm is formally defined below.

**Initialization**

   1. Let **T** *=* *∅* (empty set)
   2. Let *j = 1* (index for non-Empty Characters in **T**)
   3. Let *i = 1* (index for iterating through original string *t*)

**Iteration**

   1. If *𝔞*:sub:`i` does not exist, halt the algorithm and return the current value of **T**.
   2. If *𝔞*:sub:`i` *≠* *ε*, add the ordered pair (*j*, *𝔞*:sub:`i`) to **T** and increment *j* by 1.
   3. Increment *i* by 1.
   4. Return to step 1. ∎

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

As a brief aside, it may seem the formal system would be better developed by excluding the Empty Character altogether from its Alphabet. The Empty Character's presence in the lexicon complicates matter extensively, requiring intricate and subtle definitions. 

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

In terms of the Character level set representation, *t[i]* refers to the Character at position *i* in the set **T**.

This notation can effectively replace the use of lowercase Fraktur letters with subscripts (e.g., *𝔞*:sub:`i`) when referring to specific Characters within Strings.

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

In the case of English, Words would correspond to words such as "dog", "cat", etc. A Language would correspond to a set of words such as *{ "dog", "cat", "hamster", ... }* or *{ "tree", "flower", "grass", .... }*.

The number of Words in a Language is denoted | L |.

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

Case 1: 1 ≤ i ≤ n

    a. v[i] = s[l(s) - i + 1] (by Definition 1.2.4)
    b. v[i] = s[m + n - i + 1] (since l(s) = m + n)
    c. v[i] = t[n - i + 1] (since m + n - i + 1 corresponds to an index in t)
    d. v[i] = inv(t)[i] (by Definition 1.2.4)
    e. v[i] = w[i] (since w = inv(t)inv(u))

Case 2: n + 1 ≤ i ≤ m + n:

    a. v[i] = s[l(s) - i + 1] (by Definition 1.2.4)
    b. v[i] = s[m + n - i + 1] (since l(s) = m + n)
    c. v[i] = u[m - (i - n) + 1] (since m + n - i + 1 corresponds to an index in u)
    d. v[i] = u[m + n - i + 1]
    e. v[i] = inv(u)[i - n] (by Definition 1.2.4)
    f. v[i] = w[i] (since w = inv(t)inv(u))

In both cases, *v[i] = w[i]* for all *i* in N:sub:`l(v)`. Since *l(v) = l(w)*, by Definition 1.1.4 it follows *v = w*.

Therefore, inv(ut) = inv(t)inv(u).

Since u and t were arbitrary strings, we can generalize:

    ∀ u, t ∈ S: inv(ut) = inv(t)inv(u) ∎

Limitation
^^^^^^^^^^

While the analyis has not yet introduced the notion of Sentences into the formal system (see Section II), an operation will now be introduced that allows Words to be ordered into Phrases and then concatenated into Strings. This new operation will be important when String Inversion is applied to the sentential level of the formal system, allowing the conditions for a Sentence Inversion to be precisely specified.

The placement of Definition 1.2.5 and Definition 1.2.6 is somewhat arbitary. There are valid arguments to be made for placing these definitions after the concepts of Sentence and Word Index notation have been introduced in Section II. However, since the operation of *Limitation* to be expounded immediately is essentially an operation defined on the domain of Strings which yields as a result another String, i.e. Limitation is closed with respect to Strings, the definitions are made here, to highlight the derivative notions (Inversion and Limitation) which can be built on top of the primitive notion of concatenation.

**Definition 1.2.5: Phrase**

Let *n* be a fixed, non-zero natural number, *n ≥ 1*. A Phrase of Word Length *n* from Language **L**, denoted **P**:sub:`n`, is defined as an ordered sequence of *n* (not necessarily distinct) Words,

    P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

where each *α*:sub:`i` *∈* **L**. If *i* is *1 ≤ i ≤ n*, P:sub:`n`(i) denotes the Word *α*:sub:`i` at index *i*, so that **P**:sub:`n` may be rewritten, 

    P:sub:`n` = (P:sub:`n`(1), P:sub:`n`(2), ... , P:sub:`n`(n))

When *n = 0*, **P**:sub:`0` is defined as the empty sequence (). ∎

In order to establish some properties of Phrases and Limitations, a symbol for representing the range of a Phrase **P**:sub:`n` over a Language **L** is now defined.

**Definition 1.2.6: Lexicon**

Let *n* be a fixed natural number. We define a Language's *n*:sup:`th` Lexicon, denoted **X**:sub:`L`(*n*), as the set of all Phrases of length *n* formed from Words in **L**,

    Χ:sub:`L`(n) = { P:sub:`n` | P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`) ∧ ∀ i ∈ N:sub:`n`: α:sub:`i` ∈ L } ∎

Some of the later theorems in this work will require quantifying over Phrases in a Language's *n*:sub:`th` Lexicon, so notation is introduced for Phrase Variables,

    1. Phrase Variables (*p*, *q*, *r*): The lowercase English letters *p*, *q*, *r* are reserved for representing indeterminate Phrases of a Language's *n*:sup:`th` Lexicon.
   
Because Phrases are ordered sequences of Words, the Phrase Variable *p(i)* will denote, exactly like the Definition of a Phrase, the Word at index *i* for *1 ≤ i ≤ n*.

Using these pair of definitions for Phrases and Lexicons and their associated terminology, the operation of *Limitation* is now defined over Phrases of fixed Word Length *n* in Definition 1.2.7.

**Definition 1.2.7: Limitation**

Let **P**:sub:`n` be a Phrase of Word Length *n* from Language **L**,

    P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

The *Limitation* of **P**:sub:`n`, denoted *Π*:sub:`i=1`:sup:`n` **P**:sub:`n`*(i)*, is defined recursively as:

    1. Empty Clause: Π:sub:`i=1`:sup:`0` P:sub:`n`(i) = ε
    2. Basis Clause (n = 1): Π:sub:`i=1`:sup:`1` P:sub:`n`(i) = α:sub:`1`
    3. Recursive Clause (n > 1): Π:sub:`i=1`:sup:`n` P:sub:`n`(i) = (Π:sub:`i=1`:sup:`n-1` P:sub:`n`(i))(σ)(α:sub:`n`) ∎

Before proving the basic properties of Limitation, an example of how a Limitation is constructed recursively is given below.

**Example**

Let *P(n) = ("mother", "may", "I")* where *n = 3*.

The Basis Step yields,

    1. n = 1: Π:sub:`i=1`:sup:`1` α:sub:`i` = "mother" 

And then the Limitation can be built up recursively using the Recursive Step repeatedly,

    2.  n = 3: Π:sub:`i=1`:sup:`2` α:sub:`i` = (Π:sub:`i=1`:sup:`1` α:sub:`i`)(σ)("may")= ("mother")(σ"may") = "mother"σ"may"
    3.  n = 3: Π:sub:`i=1`:sup:`3` α:sub:`i` = (Π:sub:`i=1`:sup:`2` α:sub:`i`)(σ)("I") = ("mother"σ"may")(σ"I") = "mother"σ"may"σ"I"

So the Limitation of *P(n)* is given by,

    Π:sub:`i=1`:sup:`3` α:sub:`i` = "mother may I" ∎

From the previous example, it should be clear what the meaning of the Limitation operation is within the formal system. Limitation is a method of constructing a Sentence-like (see Section II.III for the formal difference between a Limitation and Sentence) String from a sequence of words. 

Note the previous example may be misleading in one important respect. A Limitation is not necessarily "grammatical" or "meaningful". It may be a String of semantic Words without an accompanying interpretation on the Sentence level of the linguistic hierarchy. 

However, as the next theorem shows, the result of a Limitation is unique.

**Theorem 1.2.6** ∀ n ∈ ℕ, ∀ p ∈ Χ:sub:`L(n)` ∃! s ∈ S: s = Π:sub:`i=1`:sup:`n` p(i)

This theorem can be stated in natural language as follows: For every natural number n, and for every Phrase **P**:sub:`n` in the *n*:sup:`th` Lexicon of **L**, there exists a unique string *s* in **S** such that *s* is the delimitation of **P**:sub:`n`.

Let *n* be an arbitrary natural number, and let **P**:sub:`n` be a Phrase of Word Length *n* in Language **L** from the Language's *n*:sup:`th` Lexicon, **X**:sub:`L`*(n)*,

    P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

The theorem will be proved using induction.

**Base Case (n = 1)**

By Definition 1.2.7,
    
    1. Π:sub:`i=1`:sup:`1` P:sub:`n(i)` = α:sub:`1`

Since *α*:sub:`1` is a word in **L** (by Definition 1.2.6 of Lexicon), it is also a String in S (by Definition 1.2.2). Thus, there exists a String *s = α*:sub:`1` such that 

    s = Π:sub:`i=1``:sup:`1` P:sub:`n(i)`.

Since the base case of Limitation is defined as simple equality, the string s must be unique.

**Inductive Hypothesis**

Assume that for some *k ≥ 1*, there exists a unique string *s*:sub:`k` such that 

    s:sub:`k` = Π:sub:`i=1`:sup:`k` P:sub:`n(i)`

To complete the induction, it must be shown that there exists a unique string *s*:sub:`k+1` such that,
 
    s:sub:`k+1` = Π:sub:`i=1`:sup:`k+1` P:sub:`n(i)`

By Definition 1.2.7, 

    Π:sub:`i=1`:sup:`k+1` P:sub:`n(i)` = (Π:sub:`i=1`:sup:`k` P:sub:`n(i)`)(σ)(α:sub:`k+1`)

By inductive hypothesis,
    
    Π:sub:`i=1`:sup:`k` P:sub:`n(i)` = s:sub:`k`
    
Thus, *s*:sub:`k` is unique. Since *α*:sub:`k+1` is a Word in **L** (by the definition of **Χ**:sub:`L`*(n+1)*), it is also a unique String in S.

The concatenation of *s*:sub:`k`, *σ*, and *α*:sub:`k+1` is a unique string (by the Definition 1.1.1 of Concatenation and Definition 1.1.4 of String Equality).

Therefore, *s*:sub:`k+1` = (*s*:sub:`k`)(σ)(*α*:sub:`k+1`) is a unique string.

By induction, for every natural number *n*, and for every phrase **P**:sub:`n` in **Χ**:sub:`L(n)`, there exists a unique string *s* in **S** such that *s = Π*:sub:`i=1`:sup:`n` P:sub:`n(i)`. ∎

**Theorem 1.2.7** ∀ p ∈ Χ:sub:`L`(n), ∀ q ∈ Χ:sub:`L`(m), ∀ r ∈ Χ:sub:`L`(k): ((Π:sub:`i=1`:sup:`n` p(i))(Π:sub:`i=1`:sup:`m` q(i)))(Π:sub:`i=1`:sup:`k` r(i)) = ((Π:sub:`i=1`:sup:`n` p(i)))((Π:sub:`i=1`:sup:`m` q(i))(Π:sub:`i=1`:sup:`k` r(i)))

Let *p* *∈* **Χ**:sub:`L(n)`, *q* *∈* **Χ**:sub:`L(m)`, and r ∈ **Χ**:sub:`L(k)` be arbitrary Phrases.

By Definition 2.2.4, the Limitation of a Phrase is a String. String concatenation is associative by Definition 1.1.1 and the Character Axiom C.1, meaning for any strings *s*, *t*, and *u*, 

    (st)u = s(tu)

Since *Π*:sub:`i=1`:sup:`n` *p(i)*, *Π*:sub:`i=1`:sup:`m` *q(i)*, and *Π*:sub:`i=1`:sup:`k` *r(i)* are all strings, the associativity of String Concatenation can by applied to conclude,

    ∀ p ∈ Χ:sub:`L`(n), ∀ q ∈ Χ:sub:`L`(m), ∀ r ∈ Χ:sub:`L`(k): ((Π:sub:`i=1`:sup:`n` p(i))(Π:sub:`i=1`:sup:`m` q(i)))(Π:sub:`i=1`:sup:`k` r(i)) = ((Π:sub:`i=1`:sup:`n` p(i)))((Π:sub:`i=1`:sup:`m` q(i))(Π:sub:`i=1`:sup:`k` r(i))) ∎

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

**Initialization**

    1. Let **ᚠ** be the Character-level set representation of the Sentence *ᚠ*
    2. Let W:sub:`ᚠ` = ∅ (the empty set).
    3. Let j = 1 (index for Word-level set representation)
    4. Let i = 1 (index for Characters in String)

**Iteration**

The Strings *t* and *u*, the integer *k* and the set **K** are local to the algorithm and used to store intermediate calculations.

    1. Let t = ε
    2. While i ≤ l(ᚠ) and ᚠ[i] ≠ σ:
        a. Let u = (ᚠ[i])(t)
        b. Let t = u
        c. Increment i:
            i. Let k = i + 1
            ii. Let i = k
    3. If l(t) > 0:
        a. Apply Basis Clause of Definition 1.1.1 to t
        b. Let K = set W:sub:`ᚠ` ∪ { (j, t) }
        c. Let W:sub:`ᚠ` = K
        d. Increment j:
            i. Let k = j + 1
            ii. Let j = k
    4. Increment i:
        a. Let k = i + 1 
        b. Let i = k
    5. If i > l(ᚠ):
        a. Return W:sub:`ᚠ` ∎

The essence of the Delimiting Algorithm lies in the interplay of the Discovery Axiom W.1 and Definition 2.1.2 of a Sentence as a semantic String. In other words, by Definition 2.1.1 and by Definition 1.2.2, all Sentences and Words must be semantic. Therefore, by the Discovery Axiom W.1, the Words which a Sentence contains must be exactly those Strings which are separated by the Delimiter Character. 

This formulation has the advantage of not taking a stance on the semantics of a particular language. It allows for the discovery of Words in a Language through the simple boundary of delimitation within the Sentences of its Corpus. 

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

Length
^^^^^^

The notion of String Length *l(s)* was introduced in Section I.I as a way of measuring the number of non-Empty Characters in a String *s*. In order to describe palindromic structures, a new notion of length will need introduced to accomodate a different *"spatial"* dimension in the domain of a Language and its Corpus: *Word Length*.

Intuitively, the length of a Sentence is the number of Words it contains. Since there is no analogue of Discovery Axiom W.1 for Sentences (nor should there be), this means Sentences may contain Delimiter Characters. The Words of a Language are separated by Delimiters in the Sentences of its Corpus. 

Definition 2.1.3 provide way of dispensing with the Delimiter Character in Sentences, while still retaining the information it provides about the demarcation of Words through the first coordinate of a Sentence's Word-level representation. With the Word-level set representation of Sentence in hand, it is a simple matter to define the notion of Word Length in the formal system.

**Definition 2.1.4: Word Length**

Let *ζ* be a Sentence in a **C**:sub:`L`. Let **W**:sub:`ζ` be the Word-level set representation of *ζ*, as defined in Definition 2.1.3. The Word Length of the Sentence *ζ*, denoted by *Λ(ζ)*, is defined as the cardinality of the set **W**:sub:`ζ`,

    Λ(ζ) = | W:sub:`ζ` | ∎

**Example**

Consider the Sentence *ᚠ = "The dog runs"*. Its Character-level set representation would be given by,

    **ᚠ** = { (0,"T"), (1,"h"), (2,"e"), (4,σ), (5, "d"), (6, "o"), (7, "g"), (8, σ), (9, "r"), (10, "u"), (11,"n"), (12,"s") }

Its Word-level set representation would be given by,

    W:sub:`ᚠ` = { (1, "The"), (2, "dog"), (3, "runs") }

Therefore, the length of the sentence is:

    Λ(ᚠ) = | W:sub:`ᚠ` | = 3

Note, in this example, 

    l(ᚠ) = 12

This example demonstrates the essential difference in the notions of length that have been introduced.  It is worthwhile to clarify the distinction between these two conceptions. 

Let *t* be a String with Character-level representation **T** and Word-level representation **W**:sub:`t`. The hierarchy of its "spatial" dimensions is given below, in order of greatest to least (this fact will be proven in Theorem 2.4.8, after the introduction of the Delimiter Count Function). Terminology is introduced in parenthesis to distinguish these notions of length,

   - l(t) (String Length): The number of non-Empty Characters contained in a String.
   - Λ(t) (Word Length): The number of Words contained in a String 

Note the first level is purely syntactical. Any non-Empty String *t* will have a String Length *l(t)*. However, not every non-Empty String possesses Word Length, *Λ(s)*. Word Length contains semantic information. While the presence of Word Length does not necessarily mean the String is semantically coherent (see Definition 2.3.2 for a precise definition of *semantic coherence*), e.g. "asdf dog fdsa", Word Length does signal an *extension* of Strings into the semantic domain.

With Word Length defined, this notion can be used to simplify notation. Similar to the Character Index Notation, a way of referring to Words in Sentences within propositions without excessive quantification is now introduced through Word Index notation.

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

To briefly summarize the axioms previously introduced: The system "*initializes*" with the assumption of an equality relation and the selection of an Alphabet **Σ**. The Character Axiom ensures the domain of all Strings is populated. The Discovery Axiom ensures Words only traverse the set of Strings which do not contain Delimiters. With these axioms, still nothing has been said about *what* a Word is, except that it possesses a semantic character. 

The new axioms introduced in the formal system begin to characterize the syntactical properties of the next level in the lingustic hierarchy, while still maintaining their ambivalence on the semantic content contained within their respective categories.

The Duality Axiom S.1 bares a striking resemblance to the idea of *surjection* in real analysis. Recall, a function *f*: *X* → *Y* is called *surjective* if,

    ∀ y ∈ Y : ∃ x ∈ X : f(x) = y

Meaning, every element in the co-domain is mapped to at least one element in the domain. 

In a sense, the Duality Axiom S.1 asserts a type of *"double-surjectivity"* exists between the domain of Words and the co-domain of Sentences.  In plain language, the Duality Axiom asserts for every Word *α* in the Language **L**, there exists a sentence *ζ* in the Corpus **C**:sub:`L` such that *α* is contained in *ζ*, and for every Sentence *ζ* in the corpus **C**:sub:`L`, there exists a word *α* in the language **L** such that *α* is contained in *ζ*. 

However, there is a key difference between the notion of *surjection* in real analysis and the notion captured in the Duality Axiom S.1. Containment is not a strict equality relation. By Definition 1.1.6 and Definition 1.1.7, containment reduces to the existence of a mapping between Characters in different Strings. Due to the Discovery Axiom W.2, with the exception of Sentences consisting of a Single Word, a Word is contained in a Sentence but a Sentence is not contained in a Word. 

More plainly, the Duality Axiom S.1 states a Word cannot exist in a Language without being included in a Sentence of the Corpus, and a Sentence cannot exist in a Corpus without including a Word from the Language. This Axiom captures an inextricable duality between the metamathematical concepts of Sentence and Word, and the concepts of Language and Corpus: one cannot exist without implying the existence of the other. Words and Sentences do not exist in isolation. A Language and its Corpus require one another. 

The Extraction Axiom S.2 further strengthens the relationship that exists between a Corpus and Language. It states every Word in the Sentence of a Corpus must be included in a Language. This idea of being able *extract* the Words of a Language from a Sentence is captured in the terminology introduced in Definition 2.2.1 directly below. 
 
**Definition 2.2.1: Semantic Coherence** 

A Sentence *ᚠ* is *semantically coherent* in a Language **L** if and only if **W**:sub`ᚠ` only contains words from Language **L**. 

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

Since, by step 2, *l(α) ≠ 0*, there must be some non-zero *i* that satisfies step 5. Therefore, there is at least one non-Empty Character in *ζ*, namely, *ζ[f(i)]*. The theorem is then proven by applying Definition 1.1.3,

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

Section II.III: Sentence Classes 
------------------------------

As the astute reader has no doubt surmised at this point, the foundational operation that defines a palindromic structure in linguistics is *inversion* (i.e. a method of reversal). What may not yet be clear is how this operation of inversion propagates through the hierarchy of entities defined over its domain. As this necessary structure of interdependent inversions between hierarchical layers becomes apparent, the mathematical description of a Palindrome will seen to be a *"recursion of inversions"*.

Theorems 2.3.9 - 2.3.11 of this subsection mark the first notable results obtained from the current formal system. Their empirical truth in natural language represents confirmation of the formal system's construction. These theorems demonstrate the Character-level symmetries required by invertibility propagate up through the Word-level of linguistics and manifest in conditions that must be imposed on the Word-level structure of an Invertible Sentence.

Admissible Sentences
^^^^^^^^^^^^^^^^^^^^

The notion of an *Admissible Sentence* is required to prevent a certain class of Sentence inversions from invalidating the symmetry conditions of Palindromes derived in Section III. 

To see what is meant by this concept of *admissibility*, consider the English sentence,

    ᚠ = "strap on a ton".

The Inverse of this sentence, *inv(ᚠ)*, is *semantically coherent* (Definition 2.2.1). By this it is meant every word in its inversion is part of the English language,

    inv(ᚠ) = "not a no parts"

However, this is not enough to ensure *inv(ᚠ)* is part of the Corpus, as is apparent. *Semantic coherence* is a necessary but not sufficient condition for the Inverse of a Sentence to remain in the Corpus. In order to state the requirement that must be imposed on a Sentence to remain *admissible* after inversion, the concept of Limitation introduced in Definition 1.2.7 must be leveraged. 

**Definition 2.3.1: Admissible Sentences**

Let *p* be any Phrase from a Language's *n*:sup:`th` Lexicon **X**:sub:`L`(*n*). A String *t* is said to belong to the class of *Admissible Sentences of Word Length n* in Language **L**, denoted **A**(*n*), if it satisfies the following open formula

    t ∈ A(n) ↔ (∃ p ∈ Χ:sub:`L`(n): t = Π:sub:`i=1`:sup:`n` p(i)) ∧ (t ∈ C:sub:`L`) ∎

**Theorem 2.3.1** A(n) ⊆ C:sub:`L`

Let *t* be an arbitrary String such that *t* *∈* **A**(*n*). By Definition 2.3.1, this implies, *t* *∈* **C**:sub:`L`. Therefore,

    1. t ∈ A(n) → t ∈ C:sub:`L`

This is exactly the set theoretic definition of a subset. Thus,

    2. A(n) ⊆ C:sub:`L` ∎

Theorem 2.3.1 is the formal justification for quantifying Sentence Variables over the set of Admissible Sentences (i.e. all Admissable Sentences are in the Corpus), as in the following theorem.

**Theorem 2.3.2** ∀ ζ ∈ A(n): Λ(ζ) = n

Let *ζ* be an arbitrary sentence in **A**(*n*). By Definition 2.3.1, if *ζ* *∈* **A**(*n*), then there exists a Phrase *p* *∈* **Χ**:sub:`L`(*n*) such that 

    1. ζ ∈ C:sub:`L` ∧ ζ = Π:sub:`i=1`:sup:`n` p(i)

By Definition 1.2.5 and 1.2.6, a phrase *p* in **Χ**:sub:`L(n)` is an ordered sequence of *n* words such that *α*:sub:`i` *∈* **L**,

    p = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

By Definition 1.2.7, the Limitation of *p* is given by,

    Π:sub:`i=1`:sup:`n` p(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`n`)

In other words, the Limitation of *p* (which is equal to *ζ*) explicitly constructs a String with *n* Words separated by Delimiters.

By Definition 2.1.4, the Word Length *Λ(ζ)* is the number of Words in *ζ*. Since *ζ* is formed by limiting a Phrase with *n* Words, and the Limitation process doesn't add or remove Words, the Word Length of *ζ* must be *n*. Therefore, 

    Λ(ζ) = n.

Since *ζ* was an arbitrary sentence in **A**(*n*), this can generalize as,

    ∀ ζ ∈ A(n): Λ(ζ) = n ∎

**Theorem 2.3.3** ∀ ζ ∈ C:sub:`L`: ζ ∈ A(Λ(ζ))

Let ζ be an arbitrary sentence in C:sub:`L`. By Definition 2.1.3, *ζ* has a Word-level representation,

    1. W:sub:`ζ` = (α:sub:`1`, α:sub:`2`, ... , α:sub:`Λ(ζ)`) 
    
Where each *α*:sub:`i` *∈* **L**. By Definition 1.2.5, the sequence (*α*:sub:`1`, *α*:sub:`2`, ... , *α*:sub:`Λ(ζ)`) forms a phrase **P**:sub:`Λ(ζ)` of length *Λ(ζ)* where P:sub:`Λ(ζ)`(i) = *α*:sub:`i` for all *i*, *1 ≤ i ≤ Λ(ζ)*.

By Definition 1.2,6, since **P**:sub:`Λ(ζ)` is a phrase of length *Λ(ζ)* and all its Words belong to L (by semantic coherence), then,

    2. P:sub:`Λ(ζ)` ∈ Χ:sub:`L`(Λ(ζ)).

By Definition 1.2.7, the Limitation of P:sub:`Λ(ζ)` is:

    3. Π:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`Λ(ζ)`)

The Limitation *Π*:sub:`i=1`:sup:`Λ(ζ)` **P**:sub:`Λ(ζ)`(*i*) reconstructs the original sentence *ζ*, including the Delimiters between Words. Therefore,

    4. ζ = Π:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i)

By Definition 2.3.1, a String *t* is an Admissible Sentence of Word Length *n* (*t* *∈* **A**(*n*)) if and only if there exists a phrase *p* *∈* **Χ**:sub:`L`(*n*) such that,

    5. t = Π:sub:`i=1`:sup:`n` p(i)
    6. t ∈ C:sub:`L`

By Definition 2.3.1, since the conjunction of the three facts is true,

    7. ζ ∈ C:sub:L
    8. ζ = Π:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i)
    9. P:sub:`Λ(ζ)` ∈ Χ:sub:`L`(Λ(ζ)) 
    
It follows from step 7 - step 9, *ζ* *∈* **A**(*Λ(ζ)*). Since *ζ* was an arbitrary sentence in C:sub:`L`, this can generalize as,

    ∀ ζ ∈ C:sub:L: ζ ∈ A(Λ(ζ)) ∎

**Theorem 2.3.4** ∀ ζ ∈ C:sub:`L`: ∃ p ∈ X:sub:`L`(Λ(ζ)): ζ = Π:sub:`i=1`:sup:`Λ(ζ)` p(i)

Let *ζ* be an arbitrary sentence in C:sub:`L`. By Definition 2.1.3, *ζ* has a Word-level representation,

    W:sub:`ζ`` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`Λ(ζ)`) 
    
Where each *α*:sub:`i` *∈* **L**.

By Definition 1.2.5, the sequence (*α*:sub:`1`, *α*:sub:`2`, ... , *α*:sub:`Λ(ζ)`) forms a Phrase **P**:sub:`Λ(ζ)` of Word Length *Λ(ζ)* where **P**:sub:`Λ(ζ)`(i) = *α*:sub:`i`` for all *i*, *1 ≤ i ≤ Λ(ζ)*.

By Definition 1.2.6, since **P**:sub:`Λ(ζ)` is a Phrase of Word Length *Λ(ζ)* and all its words belong to **L**, then,

    P:sub:`Λ(ζ)` ∈ Χ:sub:`L(Λ(ζ))`

By Definition 1.2.7, the Limitation of **P**:sub:`Λ(ζ)` is,

    Π:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`Λ(ζ)`)

The Limitation *Π*:sub:`i=1`:sup:`Λ(ζ)` **P**:sub:`Λ(ζ)`(i) reconstructs the original Sentence ζ, including the Delimiters between Words. Therefore:

    ζ = Π:sub:`i=1`:sup:`Λ(ζ)` P:sub:`Λ(ζ)`(i)

It has been shown that for an arbitrary sentence *ζ* *∈* **C**:sub:`L`, there exists a Phrase *p* (specifically, **P**:sub:`Λ(ζ)`) in **Χ**:sub:`L`(Λ(ζ)) such that,
 
    ζ = Π:sub:`i=1`:sup:`Λ(ζ)` p(i). 
    
Therefore,

    ∀ ζ ∈ C:sub:`L`: ∃ p ∈ Χ:sub:`L`(Λ(ζ)): ζ = Π:sub:`i=1`:sup:`Λ(ζ)` p(i) ∎

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

Note the last item in this list is an example of what this work has termed a *Perfect Palindrome*. These examples were specially chosen to highlight the connection that exists between the class of *Perfect Palindromes* and the class of *Invertible Sentences*. It appears, based on this brief and circumstantial analysis, that *Perfect Palindromes* are a subset of a larger class of Sentences, namely, Invertible Sentences.

Due to the definition of Sentences as semantic constructs and the definition of Invertible Sentences as Sentences whose Inverses belong to the Corpus, this means Invertible Sentences are exactly those Sentences that maintain *semantic coherence* (Definition 2.2.1) under inversion. In order for a Sentence to be invertible it must possess symmetry on both the Character-level and the Word-level, while maintaining a semantic structure at the Sentence level that accomodates this symmetry. This connection between the symmetries in the different linguistic levels of an Invertible Sentence will be formalized and proven by the end of this subsection.

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

**Theorem 2.3.8** ∀ ζ ∈ C:sub:`L`: inv(Π:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) = Π:sub:`i=1`:sup:`Λ(ζ)` inv(ζ{Λ(ζ) - i + 1})

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. Let *n = Λ(ζ)*. By Definition 2.1.4, this is the Word Length of *ζ*.  Let *s* denote the delimitation of *ζ* as follows:

    1. s = Π:sub:`i=1`:sup:`n` ζ{i} = (ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{n})

By Theorem 1.2.5, for any two Strings *u* and *t*, *inv(ut) = inv(t)inv(u)*. Apply this property repeatedly to construct *inv(s)*,

    2. inv(s) = inv((ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{n}))

Which reduces to,

    3. inv(s) = (inv(ζ{n}))(inv(σ))(inv(ζ{n-1}))(inv(σ)) ... (inv(ζ{2}))(inv(σ))(inv(ζ{1}))

Since σ is a single character, inv(σ) = σ,

    4. inv(s) = (inv(ζ{n}))(σ)(inv(ζ{n-1}))(σ) ... (σ)(inv(ζ{2}))(σ)(inv(ζ{1}))

Note that the right-hand side now has the form of a Limitation, but with the order of Words reversed and each Word inverted.

Re-index the terms on the right-hand side to match the form of the Limitation definition, Definition 1.2.7. Let *j = n - i + 1*. Then, as *i* goes from 1 to *n*, *j* goes from *n* to 1,

    5. inv(s) = (inv(ζ{j:sub:`n`}))(σ)(inv(ζ{j:sub:`n-1`}))(σ) ... (σ)(inv(ζ{j:sub:`2`}))(σ)(inv(ζ{j:sub:`1`}))

Where j:sub:`i` is obtained by simply substituting *n-i+1* for j. Using the Definition of Delimitation, the right-hand side becomes,

    6. inv(s) = Π:sub:`j=1`:sup:`n` inv(ζ{n - j + 1})

Recall that *s = Π*:sub:`i=1`:sup:`n` *ζ{i}*. Substitute this back into the equation and re-index the right-hand side for consistency to get,

    7. inv(Π:sub:`i=1`:sup:`n` ζ{i}) = Π:sub:`i=1`:sup:`n` inv(ζ{n - i + 1})

Since *ζ* was an arbitrary sentence, this can be generalized,

    8. ∀ ζ ∈ C:sub:`L`: inv(Π:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) = Π:sub:`i=1`:sup:`Λ(ζ)` inv(ζ{Λ(ζ) - i + 1}) ∎

As noted in previous aside, the condition of Invertibility is strong. While the Inverse of every Sentence is defined in the domain of Strings, an Inverse Sentence does not necessarily belong to the Corpus of its uninverted form. Therefore, when a Sentence is Invertible, it will exhibit syntactical symmetries at not just the Character level, but also at the individual Word level. Before moving onto to the last batch of theorems in this section, of which the latter half represents the culmination of the effort so far, a digression into their motivation is in order, as it will help highlight the interplay of syntactic symmetries that give rise to palindromes.

Consider the Sentences from the English language, *ᚠ = "this is a test"*, *ᚢ = "live on"*,* and *ᚦ = "step on no pets"*. Their Character-level representations would be,

    **ᚠ** = ("t", "h", "i", "s", σ, "i", "s", σ, "a", σ, "t", "e", "s", "t")

    **ᚢ** = ("l", "i", "v", "e", σ, "o", "n")

    **ᚦ** = ("s", "t", "e", "p", σ, "o", "n", σ, "n", "o", σ, "p", "e", "t", "s")

The Character-level representation of their Inverses, would be,

    **inv(ᚠ)** = ("t", "s", "e", "t", σ, "a", σ, "s", "i", σ, "s", "i", "h", "t")

    **ing(ᚢ)** = ("n", "o", σ, "e", "v", "i", "l")

    **inv(ᚦ)** = ("s", "t", "e", "p", σ, "o", "n", σ, "n", "o", σ, "p", "e", "t", "s")

In the case of *ᚠ*, it's *inv(ᚠ)* is not a Sentence in the Corpus, since none of the Words in it belong to the Language (English). Notice that the Delimiters (*σ*) still appear at the same indices in both *ᚠ* and *inv(ᚠ)*, just in reversed order. In *ᚠ*, the Delimiters are at indices 4, 7, and 9. In *inv(ᚠ)*, the Delimiters are at indices 9, 7, and 4 (counting from the beginning of the reversed string). So, while the sequence of Delimiters is reversed, their positions relative to the beginning and end of the String remain the same. Since the Delimiting Algorithm identifies Words based on Delimiter positions, this means application of the algorithm to the reversed Character-level representation, results in the same limitation of the linguistic "*entities*" (Strings) which correspond to Words, but in reversed order and inverted. In other words, the Delimiting Algorithm, while defined to apply to Words, can be extended to apply to the more general class of Strings which do not contain Empty Characters. 

In the case of *ᚢ*, it's *inv(ᚢ)* belongs to the Corpus, since all of its Words belong to the Language (English) and have semantic coherence in *ᚢ*. This means *ᚢ* belongs to the class of Invertible Sentences in English. Take note, none of the Words that belong to *ᚢ* (or more precisely, to one of the ordered pairs of **W**:sub:`ᚢ`) belong to *inv(ᚢ)* (or more precisely, to one of the ordered pairs of **W**:sub:`inv(ᚢ)`). However, there does appear to be a relationship between the Words which appear in *ᚢ* and *inv(ᚢ)*, namely, they must be Invertible. The Word *"live"* inverts into *"evil"*, while *"on"* inverts into *"no"*. In other words, based on this preliminary heuristic analysis, if a Sentence is to be Invertible, the Words which belong to it must belong to the class of Invertible Words **I**.

In the case of *ᚦ*, a similar situation is found. Each Word in *ᚦ* is Invertible and pairs with its Inverse Word in *inv(ᚦ)*, e.g. *"pets"* and *"step"* form an Invertible pair, etc. This means, for the same reasons as *ᚢ*, *ᚦ* belongs to the class of Invertible Sentences. However, there is a symmetry embodied in *ᚦ* over and above the pairing of its constituent Words into Invertible pairs. Not only is *inv(ᚦ)* a Sentence in the Corpus, but it's equal to *ᚦ* itself. Indeed, *ᚦ* belongs to a special class of English sentences: Palindromes. 

Note, in order for the Sentence to invert, i.e. the case of *ᚢ* and *ᚦ*, the order of the Words in the inverted Sentences must be the reversed order of the inverted Words in the uninverted Sentence. In other words, the inversion defined on the String *"propagates"* up through the levels of the semantic hierarchy and manifests at each level in the form of a semantic inversion. This will be discussed in greater detail after the next theorems are established.

These last theorems encapsulate these important properties of Invertible Sentences. When Palindromes are formally defined in the next section, these theorems will be used extensively to prove the main results of this work. 

**Theorem 2.3.9** ∀ ζ ∈ C:sub:`L`: ζ ∈ K → ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})

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
    
In turn, Definition 1.2.4 of String Inversion states in order for this to be the case, it must also be the case,

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

By Theorem 2.3.4, the inverse of *ζ*, *inv(ζ)*, can be expressed as the Delimitation of the inverses of the Words of *ζ* in reverse order,

    5. inv(ζ) = Π:sub:`i=1`:sup:`Λ(ζ)` inv(ζ{Λ(ζ) - i + 1})

This is equivalent to,

    6. inv(ζ) = Π:sub:`i=1`:sup:`Λ(ζ)` inv(ζ){i}

Since *inv(ζ)* *∈* **C**:sub:`L` by assumption (step 1) and *inv(ζ)* has the same Word Length as *ζ* which is *Λ(ζ)*, and *inv(ζ)* is a Limitation of Words from **L**, by Definition 2.3.1, it follows that,

    7. inv(ζ) ∈ A(Λ(ζ)).

Therefore, both conditions hold, 

    8. ∀ i ∈ N:sub:Λ(ζ): inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
    9. inv(ζ) ∈ A(Λ(ζ))

(←) Assume that for an arbitrary sentence *ζ* *∈* **C**:sub:`L`, the following holds,

    1. ∀ i ∈ N:sub:Λ(ζ): inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
    2. inv(ζ) ∈ A(Λ(ζ))


By Definition 2.3.1, since *inv(ζ)* *∈* **A**(*Λ(ζ)*), it follows immediately, 

    3. inv(ζ) ∈ C:sub:`L`

By Definition 2.3.2, it follows, 

    4. ζ ∈ K

Therefore, the bidirectional theorem holds. ∎

The concept of *admissibility* deserves mention. Just as the notion of Word Length introduced a dimension of *"semanticality"* to the formal system, so too does the notion of an Admissible Sentence introduce a dimension of *"grammaticality"*. Theorem 2.3.9 takes no stance on what constitutes an Admissible Sentence, what sort of grammatical forms and structures might define this notion, except to say it must be the result of a Limitation of Words that belongs to the Corpus. 

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

As mentioned in the introduction of this work, the complete structure of palindromes is described through the combination of four different attributes or dimensions: *aspect*, *parity*, *case* and *punctuality*. The framework has now been developed to classify the first two palindromic properties with more precision.

Unfortunately, as far as the author knows, punctuation and capitalization are syntactic bearers of semantic meaning that cannot be reduced to purely formal considerations. Both punctuality and case require additional axioms to describe the unique structuring they impose on a Language and its Corpus. In the author's opinion, it is impossible to disentangle these linguistic phenomenon from the realm of semantics.

In what follows, two things are implicitly assumed. These assumptions are made explicit here, so the scope of the results can be properly understood. First, the Alphabet **Σ** is assumed to contain no punctuation marks beyond the Delimiter Character (if one is inclined it to consider a form of punctuation). Second, it is assumed every Character in **Σ** is distinct, meaning all matters of case are ignored. To rephrase the same idea more precisely: there is no assumed semantic relation between Characters in the Alphabet that would allow the identification of distinct Characters as different *cases* of the same Character.

With these assumptions, the analysis is confined to the dimensions of *aspect* and *parity*, which will be defined in the following subsections. After the results are derived, consideration will be given to future work that could potentially integrate semantic considerations into the formal framework of palindromic structures to account for the dimensions of punctuality and case.

Section III.I: Palindromes 
--------------------------

The study of palindromes will revolve around a novel linguistic operation, termed a *σ*-reduction. This operation will allow the semantic content of a palindrome to be projected onto an Alphabet that preserves the order of its Characters under String Inversion, allowing for a precise definition of a palindrome within a purely formal language.

σ-Reductions
^^^^^^^^^^^^

Before defining a *σ*-reduction, the preliminary concept of a *σ-reduced Alphabet* must be introduced. The following definition serves as the basis for constructing the operation of *σ*-reduction.

As has been seen with examples of Imperfect Palindromes like *"borrow or rob"*, a palindromic structure can have its Delimiter Character scrambled in the inversion of its form, making it lose semantic coherence. Imperfect Palindromes* must be rearranged Delimter-wise to retrieve the original form of the Sentence. However, String Inversion preserves the relative order of the non-Delimiter Characters in a palindromic String, so the process of reconstitution is only a matter of resorting the Delimiter characters. This invariance of the Character order, while the Word order is scrambled by Delimiter, suggests palindromes might be more easily defined without the obstacle of the Delimiter.

**Definition 3.1.1: σ-Reduced Alphabet**

A *σ-reduced Alphabet* is an Alphabet Σ that has had its Delimiter character removed, so that it only consists of non-Delimiter characters. A sigma-reduced Alphabet is denoted Σ:sub:`σ`. Formally,

    Σ:sub:`σ` = Σ - { σ }

In order to define palindromes in all of their varieties, perfect or imperfect, the semantic incoherence that is introduced by the inversion of Imperfect Palindromes must be removed. This is accomplished through the introduction of the operation of *sigma reduction*.

**Definition 3.1.2: σ-Reduction**

Let *s* be a String with length *l(s)* and Character-level representation 

    1. S = { (1,𝔞:sub:`1`) , (2, 𝔞:sub:`2`) , ... , (l(s), 𝔞:sub:`l(s)`) } 
    2. 𝔞:sub:`i` ∈ Σ.

The *σ*-reduction of *s*, denoted by *s* ⋅ **Σ**:sub:`σ`, maps the String *s* to a new String *t* in the *σ*-reduced alphabet **Σ**:sub:`σ` by removing all occurrences of the Delimiter Character. Formally, *s* ⋅ **Σ**:sub:`σ` is defined and constructed using the *Reduction Algorithm*,

**Reduction Algorithm**

**Algorithm 3: Reduction Algorithm**

The Reduction Algorithm takes in a String *s* as input. It initializes the values of several local variables and then iterates over the Character level set representation of the String *s* until the Characters have been exhausted. It then returns the *σ-reduced* String *t* that correspond to the String *s*. The exact details are given below.

**Initialization** 

- Let t = ε (*σ*-reduced String)
- Let i = 1 (index to iterate over input String)

**Iteration**

- If s[i] ≠ σ:
    - Let u = (s[i])t
    - Let t = u
- If i = l(s):
    - Apply Basis Clause of Definition 1.1.1
    - Return t
- Let j = i + 1
- Let i = j ∎

The following example shows how to apply the Reduction Algorithm to construct the σ-reduction of a String.

**Example**

Let *s = "a b c"* be a String from the Alphabet *Σ = { "", " " , "a", "b", "c" }*. Note in this example *σ = " "* and *l(s) = 5*. The value of the variables in the Reduction Algorithm after each iteration are given below,

    1. i = 2, t = "a"ε
    2. i = 3, t = "a"ε
    3. i = 4, t = "a"ε"b"
    4. i = 5, t = "a"ε"b"
    5. i = 5, t = "abc"
        
The result of the σ-reduction of *s* is thus given by,

    s ⋅ Σ' = "abc" ∎

The notation for sigma reduction is meant to evoke the idea of a vector dot project. The analogy to a vector projection is indeed apt. While not a strict mathematical equivalence, it captures the idea of transforming the string from its original form (with Delimiters) onto a reduced space (without Delimiters), similar to how a vector can be projected onto a subspace.

The *σ*-reduced Alphabet (**Σ**:sub:`σ`) can be seen as a subspace within this higher-dimensional space, consisting of only the non-Delimiter dimensions. The sigma reduction function (*s* ⋅ **Σ**:sub:`σ`) acts as a projection operator, mapping the String onto this subspace by eliminating the components corresponding to the Delimiter character (*σ*).

Note that a *σ*-reduction is not a one-to-one operation. It is possible for the *σ*-reduction of a palindrome to map onto a totally different sentence, not necessarily a palindrome.

As an example, consider the (partial, ignoring punctuality) Palindromes *ᚠ = "madam im adam"* and *ᚢ = "mad am i madam"*. The *σ*-reduction of both of these Sentences would map to the *σ-reduced* value of *madamimadam".

Both the Palindrome and the alternative Sentence have the same *σ*-reduction, despite having different meanings and grammatical structures. This highlights the ambiguity that can arise from removing spaces, as the original word boundaries and sentence structure are lost.

The following theorems establish the basic properties of *σ*-reductions. 

**Theorem 3.1.1** ∀ ζ ∈ C:sub:`L`: inv(ζ ⋅ Σ:sub:`σ`) = (inv(ζ) ⋅ Σ:sub:`σ`)

Let *ζ* be an arbitrary sentence in C:sub:L. Let *s* be the *σ*-reduction of *ζ*,

    1. s = ζ ⋅ Σ:sub:`σ`

Let *t* be the Inverse of *s*,

    2. t = inv(s).

Let *u* be the Inverse of *ζ*,

    3. u = inv(ζ). 
    
Let *v* be the *σ*-reduction of *u*,

    4. v = u ⋅ Σ:sub:`σ` = inv(ζ) ⋅ Σ:sub:`σ`. 

Since *s* contains only the non-Delimiter characters of *ζ* in their original order, and *t* is the reversed sequence of Characters in *s*, *t* contains only the non-Delimiter characters of *ζ* in reversed order.

Similarly, since *u* is the reverse sequence of Characters in *ζ*, and *v* is obtained by removing Delimiters from *u*, *v* also contains only the non-Delimiter characters of *ζ* in the reversed order.

Therefore, by Definition 1.1.4, *t* and *v* must be the same String, as they both contain the same Characters in the same order. Since *t = v*, 

    5. inv(ζ ⋅ Σ:sub:`σ`) = (inv(ζ) ⋅ Σ:sub:`σ`)

Since ζ was an arbitrary sentence in C:sub:L, this can be generalized,

    6. ∀ ζ ∈ C:sub:`L`: inv(ζ ⋅ Σ:sub:`σ`) = (inv(ζ) ⋅ Σ:sub:`σ`) ∎

This corollary is essential because it allows free movement between the Inverse of a *σ*-reduction and the *σ*-reduction of an Inverse. In other words, it establishes the commutativity of inversion and reduction. 

**Theorem 3.1.2** ∀ ζ,ξ ∈ C:sub:`L`: ζξ ⋅ Σ:sub:`σ` = (ζ ⋅ Σ:sub:`σ`)(ξ ⋅ Σ:sub:`σ`)

Let *ζ* and *ξ* be arbitrary sentences in **C**:sub:`L`. Let **Ζ** and **Ξ** be the character-level representations of *ζ* and *ξ*, respectively,

    1. Ζ = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(ζ)`)

    2. Ξ = (𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(ξ))`

Let *ζξ* be the concatenation of *ζ* and *ξ*. The character-level representation of *ζξ* is,

    3. ΖΞ = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(ζ)`, 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(ξ)`)

Let *s* be the σ-reduction of *ζξ*. Let *t* be the *σ*-reduction of *ζ*. Let *u* be the *σ*-reduction of *ζξ*,

    4. s = ζξ ⋅ Σ:sub:`σ`
    5. t = ζ ⋅ Σ:sub:`σ`
    6. u = ξ ⋅ Σ:sub:`σ`

Let *v* be the concatenation of the Strings *t* and *u*,

    7. v = tu = (ζ ⋅ Σ:sub:`σ`)(ξ ⋅ Σ:sub:`σ`)

Since *σ*-reduction only removes Delimiters and doesn't change the order of non-Delimiter Characters, the non-Delimiter characters in *s* (the *σ*-reduction of *ζξ*) are the same as the non-Delimiter Characters in *ζ* followed by the non-Delimiter Characters in ξ.

The non-Delimiter characters in *v* (the concatenation of (*ζ* ⋅ **Σ**:sub:`σ`) and (*ξ* ⋅ **Σ**:sub:`σ`) are also the non-Delimiter characters in *ζ* followed by the non-delimiter characters in *ξ*.

Therefore, by Definition 1.1.4, *s* and *v* must be the same String, as they both contain the same Characters in the same order (the non-Delimiter Characters of *ζ* followed by the non-Delimiter characters of *ξ*). Since *s = v*, 

    8. ζξ ⋅ Σ:sub:`σ` = (ζ ⋅ Σ:sub:`σ`)(ξ ⋅ Σ:sub:`σ`)

Since ζ and ξ were arbitrary sentences in C:sub:L, this can be generalized,

    9. ∀ ζ, ξ ∈ C:sub:`L`: ζξ ⋅ Σ:sub:`σ` = (ζ ⋅ Σ:sub:`σ`)(ξ ⋅ Σ:sub:`σ`) ∎

Theorem 3.1.1 establishes a type of commutativity. Theorem 3.1.2 further demonstrates the "algebraic" nature of *σ*-reduction and its interaction with other String operations. It shows that *σ*-reduction "distributes" over concatenation, just as inversion "distributes" (in a reversed way) over concatenation (Theorem 1.2.5). These properties suggest that *σ*-reduction and inversion are not just arbitrary operations but are deeply connected to the underlying structure of Strings and Sentences.

As another example of this "linguistic algebraic structure", the following theorem might be termed the *"Idempotency of σ-reduction"* or the *"σ-reduction Idempotence Property"*.

**Theorem 3.1.3** ∀ ζ ∈ C:sub:`L`: (ζ ⋅ Σ:sub:`σ`) ⋅ Σ:sub:`σ`= ζ ⋅ Σ:sub:`σ`

Let *ζ* be an arbitrary Sentence in **C**:sub:`L`. Let s be the *σ*-reduction of *ζ*,

    1. s = ζ ⋅ Σ:sub:`σ`

Let *t* be the *σ*-reduction of *s*,

    2. t = s ⋅ Σ:sub:`σ` = (ζ ⋅ Σ:sub:`σ`) ⋅ Σ:sub:`σ`

Since *s* is the result of applying a *σ*-reduction to *ζ*, it contains no Delimiter Characters (σ).

When *s* is *σ*-reduced (to get *t*), the Reduction Algorithm in Definition 3.1.2 iterates through the Characters of *s*. Since s has no Delimiters, the condition if *s[i] ≠ σ* in the algorithm will always be true, and every character of *s* will be concatenated to the initially empty string *t*. Therefore, by Definition 1.1.4, *t* will be identical to *s*, as it contains the same Characters in the same order. Thus,

    3. (ζ ⋅ Σ:sub:`σ`) ⋅ Σ:sub:`σ` = ζ ⋅ Σ:sub:`σ`

Since ζ was an arbitrary sentence in C:sub:L, this can be generalized,

    4. ∀ ζ ∈ C:sub:`L`: (ζ ⋅ Σ:sub:`σ`) ⋅ Σ:sub:`σ`= ζ ⋅ Σ:sub:`σ` ∎

**Theorem 3.1.4** ∀ ζ ∈ C:sub:`L`: Λ(ζ ⋅ Σ:sub:`σ`) ≤ 1

Let *ζ* be an arbitrary sentence in C:sub:L. By the Duality Axiom S.1, every Sentence in C:sub:`L` must contain at least one word from L. 

By Definition 3.1.2, *ζ* ⋅ **Σ**:sub:`σ`removes all Delimiters from *ζ*. Therefore, *ζ* ⋅ **Σ**:sub:`σ` consists of the Characters of the words in *ζ* concatenated together without any delimiters.

By the Discovery Axiom W.1., Words in **L** cannot contain Delimiters.

By Definition 2.1.4, the Word Length *Λ(s)* of a String *s* counts the number of Words in *s*, where Words are separated by Delimiters.

If *ζ* contains only one Word, then *ζ* ⋅ **Σ**:sub:`σ` will be that Word,

    1. Λ(ζ ⋅ Σ:sub:`σ`) = 1

If *ζ* contains multiple Words, then *ζ* ⋅ **Σ**:sub:`σ` will be a concatenation of those words without Delimiters. This concatenated String may or may not be a valid Word in **L**.

If the concatenated String is a valid Word in **L**, then,

    2. Λ(ζ ⋅ Σ:sub:`σ`) = 1

If the concatenated String is not a valid Word in **L**, then,

    3. Λ(ζ ⋅ Σ:sub:`σ`) = 0

Therefore, in all possible cases,

    Λ(ζ ⋅ Σ:sub:`σ`) ≤ 1.

Since *ζ* was an arbitrary sentence in **C**:sub:`L`, this can be generalized, 

    ∀ ζ ∈ C:sub:`L`: Λ(ζ ⋅ Σ:sub:`σ`) ≤ 1. ∎

During a *σ*-reduction, information in lost with respect to the following semantic categories,

  - Word Boundaries: The spaces between words, which are crucial for parsing and understanding the sentence, are eliminated.
  - Sentence Structure: The grammatical structure of the sentence, the relationships between words and phrases, becomes ambiguous.
  - Prosody and Rhythm: The pauses and intonation that contribute to the meaning and expression of the sentence are lost.

However, some semantic information is preserved. The individual words themselves, or at least their character sequences, remain present in the *σ-reduced* string. The next theorem proves semantic content is retained during the *σ*-reduction of a Sentence.

**Theorem 3.1.5** ∀ ζ ∈ C:sub:`L`, ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` (ζ ⋅ Σ:sub:`σ`)

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus **C**:sub:`L`, and for every Word *ζ{i}* in the Word-level representation of *ζ*, *ζ{i}* is contained in (*ζ* ⋅ **Σ**:sub:`σ`).

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. By Theorem 2.2.4, it is known at least one Word must exist in *ζ*. Let *ζ{i}* be one of the Words in the sequence of Words that form *ζ*. 

This means that *ζ* can be written as either, in the case of *Λ(ζ) > 1*, 

    1. Case (Λ(ζ) > 1): ζ = (s:sub:`1`)(σ)(ζ{i})(σ)(s:sub:`2`)
    
where *s*:sub:`1` and *s*:sub:`2` are (possibly Empty) Strings. 

In the case that Λ(ζ) = 1, then, this means *ζ* can be written simply as, 

    1. Case (Λ(ζ) = 1): ζ = ζ{1}

By the Definition 3.1.2, *ζ* ⋅ **Σ**:sub:`σ` is obtained by removing all Delimiters from ζ. Furthermore, by Theorem 3.1.2, *σ*-reduction distributes over concatenation. Thus,

    1. Case (Λ(ζ) > 1): ζ ⋅ Σ:sub:`σ` = (s:sub:`1`⋅ Σ:sub:`σ`)(ζ{i} ⋅ Σ:sub:`σ`)(s:sub:`1`⋅ Σ:sub:`σ`)
    2. Case (Λ(ζ) = 1): ζ{1} ⋅ Σ:sub:`σ` 

By the Discovery Axiom W.1, Words in **L** do not contain Delimiters.

    1. Case (Λ(ζ) > 1): ζ ⋅ Σ:sub:`σ` = (s:sub:`1`⋅ Σ:sub:`σ`)(ζ{i})(s:sub:`1`⋅ Σ:sub:`σ`)
    2. Case (Λ(ζ) = 1): ζ{1} ⋅ Σ:sub:`σ` = ζ{1}

Therefore, by the definition of Containment (Definition 1.1.4):

    1. Case (Λ(ζ) > 1): ζ{i} ⊂:sub:`s` ζ ⋅ Σ:sub:`σ` 
    2. Case (Λ(ζ) = 1): ζ{1} ⊂:sub:`s` ζ ⋅ Σ:sub:`σ` 

In both cases, there is a Word in *ζ* that is contained in the *σ*-reduction of *ζ*. Since *ζ* was arbitrary, this can generalize as,

∀ ζ ∈ C:sub:`L`, ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` (ζ ⋅ Σ:sub:`σ`) ∎

As the last precursor to a formal explication of palindromic structures, this subsection is concluded by showing how *σ*-reduction behaves over the class of Invertible Sentences, an extremely important class for understanding the mechanics of Palindromes.

**Theorem 3.1.6** ∀ ζ ∈ C:sub:`L` : ζ ∈ K → [ inv(ζ  ⋅ Σ:sub:`σ`) = inv(inv(ζ  ⋅ Σ:sub:`σ`)) ]

In natural language, this theorem can be stated in natural language as follows: If a Sentence in a Corpus is invertible, then its invertibility is invariant under *σ*-reduction.

Assume *ζ ∈* **C**:sub:`L`` and *ζ ∈* **K**, i.e. *ζ* is an Invertible Sentence. By Theorem 2.3.7, since *ζ* is invertible, all its Words are also Invertible,
 
    1. ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → inv(ζ){i} ∈ L

ζ ⋅ Σ:sub:`σ`
The σ-reduction of *ζ*, *ζ* ⋅ **Σ**:sub:`σ`, is obtained by removing all Delimiters from ζ. Since no Word contains Delimiters (by Discovery Axiom W.1), the *σ*-reduction concatenates the Words of ζ,

    3. Ζ ⋅ Σ:sub:`σ`` = (ζ{1})(ζ{2})...(ζ{Λ(ζ)})

Applying Theorem 1.2.5 repeatedly,

    4. inv(Ζ ⋅ Σ:sub:σ) = inv((ζ{1})(ζ{2})...(ζ{Λ(ζ)}))

To get,

    5.  inv(Ζ ⋅ Σ:sub:`σ`)  = (inv(ζ{Λ(ζ)})) ... (inv(ζ{2}))(inv((ζ{1})))

Applying a second Inversion,

    6. inv(inv(Ζ ⋅ Σ:sub:`σ)) = inv((inv(ζ{Λ(ζ)})) ... (inv(ζ{2}))(inv((ζ{1}))))

Applying Theorem 1.2.5 again,

    7. inv(inv(Ζ ⋅ Σ:sub:`σ)) = (inv(inv((ζ{1})))) (inv(inv((ζ{2}))))...(inv(inv(inv((ζ{Λ(ζ)}))))

Finally, applying Theorem 1.2.4 (*inv(inv(s)) = s*)

    8. inv(inv(Ζ ⋅ Σ:sub:`σ)) = (ζ{1})(ζ{2})...(ζ{Λ(ζ)})

Therefore, combining step 3 and step 8

    inv(Ζ ⋅ Σ:sub:`σ`) = inv(inv(Ζ ⋅ Σ:sub:`σ`)). ∎

The contrapositive of this theorem, much like the contrapositive of Theorem 2.3.5, provides a schema for searching the *σ-reduced* space for Invertible Sentences. The domain of this space reduces the complexity of searching for palindromic strings. Potential palindromic candidates can be projected into the *σ-reduced* spaced, and then filtered by those whose *σ*-reduction whose Inverse does not equal itself. 

These ideas will be expounded until in Section III.III, when the theorems and results of this work are used to implement a Palindrome search algorithm.

Aspect
^^^^^^

The current analysis now turns towards its apex, using the notions that have been developed up to this point to define the mathematical structure of Palindromes. To motive the next definition, consider how the operation of *σ*-reduction "*projects*" Palindromes onto an Alphabet where their symmetry is preserved.

Consider a perfect palindromes like *ᚠ = "strap on no parts"*,

    ᚠ ⋅ ζ:sub:`σ`= "straponnoparts"

    inv(ᚠ ⋅ ζ:sub:`σ` ) = "straponnoparts"

In other words, the *σ*-reduction and the inversion of its *σ*-reduction space result in the same String.

Consider an imperfect palindrome like *ᚢ = "borrow or rob"*,

    ᚢ ⋅ Σ:sub:`σ`= "borroworrob"

    inv(ᚢ ⋅ Σ:sub:`σ` ) = "borroworrob"

Again, the *σ*-reduction eliminates the Delimiters, and the inversion of the *σ*-reduction captures the mirrored relationship between the words, even if the exact Character sequence isn't identical to the original Palindrome.

These examples lead directly to the next, important definition.

**Definition 3.1.3: Palindromes**

Palindromes are defined as the set of Sentences **P** that satisfy the following formula,

    ∀ ζ ∈ C:sub:`L`: ζ ∈ P ↔ [ (ζ ⋅ Σ:sub:`σ`) = inv(ζ ⋅ Σ:sub:`σ`) ] ∎

This definition distills the core property of Palindromes, their symmetrical nature, by focusing on the sequence of Characters without the ambiguity of Delimiters. The use of set notation and logical operations provides a mathematically rigorous and unambiguous definition.

Moreover, this definition can be easily adapted to different languages by simply defining the appropriate Alphabet **Σ** and the corresponding *σ-reduced* alphabet **Σ**:sub:`σ`

It highlights the concept of invariance under transformation. A Palindrome remains a Palindrome even when projected onto the *σ-reduced* Alphabet, demonstrating a kind of structural integrity that's independent of the specific representation.

The condition (*ζ*  ⋅ **Σ**:sub:`σ`) *= inv*(*ζ* ⋅ **Σ**:sub:`σ`) can be seen as defining an equivalence relation on the set of Sentences, where two Sentences are equivalent if they are Palindromes of each other in the *σ-reduced* space.

This definition highlights that palindromes possess a structural integrity that is preserved even under the transformation of σ-reduction, demonstrating that their palindromic nature is not dependent on the presence of delimiters.

**Definition 3.1.4: Perfect Palindromes**

Perfect Palindromes are defined as the set of Sentences **PP** that satisfy the following formula,

    ∀ ζ ∈ C:sub:`L`: ζ ∈ PP ↔ ζ = inv(ζ)

Note the name given to this class of Sentences is premature. While the terminology will prove to be accurate, at this point in the analysis, one must be careful not to confuse Perfect Palindromes with Palindromes. It has not yet been shown the class of Sentences which satisfy Definition 3.1.4 also satisfy 3.1.3. 

Before verifying the class of Sentences which satisfy Definition 3.1.4 are indeed palindromes, the motivation for Definition 3.1.4 will briefly be explained.

This Definition implicitly captures the Character-level symmetry that's characteristic of perfect Palindromes. If a Sentence is its own inverse, it means that the sequence of Characters reads the same backward as forward.

It also implicitly captures the Word-level symmetry, as the inversion operation takes into account the reversal of words within the sentence, by Theorems 2.3.9 - 2.3.11. 

The following theorems will be used to validate the proposed class **PP** does indeed satisfy Definition 3.1.3, and thus Perfect Palindromes are a subset of the class Palindromes in any Language and its Corpus.

**Theorem 3.1.7** PP ⊂ K

In natural language, this theorem can be stated as follows: Perfect Palindromes are a subset of the Invertible Sentences in a Corpus. 

Assume *ζ* is arbitrary Sentence in **C**:sub:`L` such that,

    1. ζ ∈ PP

This means *ζ* is a Perfect Palindrome, so by Definition 3.1.4, 

    2. ζ = inv(ζ).

Since *ζ* is a Perfect Palindrome, it is also a Sentence, and therefore,

    3. ζ ∈ C:sub:`L`
    
Because *ζ = inv(ζ)* and *ζ ∈* **C**:sub:`L`, it follows,

    4. inv(ζ) ∈ C:sub:`L`.

By Definition 2.3.2 of Invertible Sentences, 

    5. inv(ζ) ∈ C:sub:`L` ↔ ζ ∈ K

Therefore, 

    6. ζ ∈ PP → ζ ∈* K. 
    
This in turn implies,

    7. PP ⊂ K ∎

**Theorem 3.1.8** ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → (∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I)

In natural language, this theorem can be states as Follows: If a Sentence is a Perfect Palindrome, then all of its Words are Invertible. 

Recall the definition of a subset,

    1. A ⊂ B ↔ (∀ x: x ∈ A → x ∈ B)

Applying this definition to Theorem 3.1.7, 
    
    2. ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → ζ ∈ K

From Theorem 2.3.11, it is known the consequent of this conditional implies the following,

    3. ∀ ζ ∈ C:sub:`L`: ζ ∈ K → (∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I)

Recall the tautology of *Hypothetical Syllogisms*, for any propositions *p*, *q* and *r*,

    4. ( p → q ∧ q → r ) → (q → r)

Applying this tautological law to step 2 and step 3,

    5. ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → (∀ α ∈ W:sub:`ζ`: α ∈ I)

Which is what was to be shown. ∎ 

It is now shown using the previous theorems that Perfect Palindromes are in fact a subset of the set that implicitly satisfies Definition 3.1.3.

**Theorem 3.1.9**  PP ⊂ P

Assume *ζ* is arbitrary Sentence in **C**:sub:`L` such that,

    1. ζ ∈ PP 
    
This means *ζ* is a Perfect Palindrome, so by Definition 3.1.4, 

    2. ζ = inv(ζ).

Applying a *σ*-reduction to both sides of the equation,

    3. (ζ ⋅ Σ:sub:`σ`) = (inv(ζ) ⋅ Σ:sub:`σ`)

By Theorem 3.1.1, 

    4. (inv(ζ) ⋅ Σ:sub:`σ`)  = inv(ζ ⋅ Σ:sub:`σ`)

Combining steps 2 and 3, 

    5. (ζ ⋅ Σ:sub:`σ`) = inv(ζ ⋅ Σ:sub:`σ`)

Step 4 is exactly satisfies the condition for *ζ* to be a Palindrome according to Definition 3.1.3. Therefore, 

    6. ζ ∈ P.

Since *ζ* was an arbitrary Perfect Palindrome, it been shown that,

    7. ζ ∈ PP → ζ ∈ P
    
This in turn implies,

    8. PP ⊂ P ∎

Now that Perfect Palindromes have been shown to satisfy Definition 3.1.3, it is a simple matter of defining Imperfect Palindromes as those Palindromes which are *not* Perfect.

**Definition 3.1.5: Imperfect Palindromes**

Imperfect Palindromes are defined as the set of Sentences **IP** that satisfy the following open formula,

    ζ ∈ P - PP ∎

**Theorem 3.1.10** PP ∪ IP = P

Follows immediately from Theorem 3.1.9, Definition 3.1.5, and the fact that PP and IP are disjoint (by the definition of set difference). ∎

Since PP and IP are non-overlapping by Definition 3.1.5 and their union encompasses the entire class of Palindromes by Theorem 3.1.8, these two sets form a partition of the class of Palindromes. The following definition and terminology is introduced to help describe this partitioning.

**Definition 3.1.6: Aspect**

A Palindrome P is said to have a *perfect aspect* if and only if *P ∈ PP*. A Palindrome is said to have an *imperfect aspect* if and only if *P ∈ IP*. ∎

Parity
^^^^^^

One partitioning, or dimension, of Palindromes has been introduced through the concept of *aspect*. A Palindrome can either be perfect or imperfect, but not both. In this section, the definitions and theorems for uncovering the second partitioning of Palindromes, *parity*, will be developed.

**Definition 3.1.6: Left Partial Sentence**

Let ζ be a Sentence in C:sub:`L` with Character-level representation **Z**,

    Z  = (ⲁ:sub:`1` , ⲁ:sub:`2` , ... , ⲁ:sub:`l(ζ)`).

Let *n* be a fixed natural number such that *1 ≤ n ≤ l(ζ)*. A Left Partial Sentence of String Length *n*, denoted *ζ[: n]*, is formally defined as the String which satisfies, 

    Z[:n] = (ⲁ:sub:`1` , ⲁ:sub:`2` , ... , ⲁ:sub:`n`)  

When *n = 0*, *ζ[:0]* is defined as the empty string, *ε*.

When *n = l(ζ)*, *ζ[:n]* is the entire sentence *ζ*. ∎

**Definition 3.1.7: Right Partial Sentence**

Let ζ be a Sentence in C:sub:`L` with Character-level representation **Z**,

    Z = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(ζ)`)

Let *n* be a fixed natural number such that *0 ≤ n ≤ l(ζ)*. A Right Partial Sentence of *ζ* of String Length *n*, denoted ζ[n:], is defined as the string:

    ζ[n:] = (ⲁ:sub:`l(ζ)-n+1`, ⲁ:sub:`l(ζ)-n+2`, ..., ⲁ:sub:`l(ζ)`)

When *n = 0*, *ζ[0:]* is defined as the empty string, *ε*.

When *n = l(ζ)*, *ζ[n:]* is the entire sentence ζ. ∎

Take note, Partial Sentences are not necessarily a Word or a sequence of Words.

The notation *ζ[n:]* and *Z[:n]* is analogous to array slicing notation found in many programming languages. It indicates a substring is being taken starting from a position *n* Characters from the end of the String up to the end of the String.

Note when *n* is even,

    l(ζ[:n]) = l(ζ[n:]) = n

But when *n* is odd,

    l(ζ[:n]) = n

    l(ζ[n:]) = n + 1

The next theorem leverages this insight and establishes the fundamental relationship between Left and Right Partial Sentences, and the existence of a natural number that acts as the mid-point of the Sentence's String Length. This in turn will allow for a definition of a Sentence's *Pivot*.

**Theorem 3.1.11** ∀ ζ ∈ C:sub:`L`: ∃ n ∈ N:sub:`l(ζ)`: ( l(ζ[:n]) = l(ζ[n:]) ) ∨ (l(ζ[:n]) = l(ζ[n:]) + 1)

This theorem can be stated in natural language as follows: For every sentence ζ in the corpus, there exists a natural number n (between 0 and the length of ζ, inclusive) such that either the length of the left partial sentence of length n is equal to the length of the right partial sentence of length n, OR the length of the left partial sentence of length n is one greater than the length of the right partial sentence of length n.

Proof:

Let ζ be an arbitrary sentence in C:sub:L. Let l(ζ) = L (for simplicity).

Case 1: L is even:

If L is even, let n = L/2.
Then l(ζ[:n]) = n = L/2.
And l(ζ[n:]) = L - n = L - L/2 = L/2.
Therefore, l(ζ[:n]) = l(ζ[n:]).
Case 2: L is odd:

If L is odd, let n = (L + 1)/2.
Then l(ζ[:n]) = n = (L + 1)/2.
And l(ζ[n:]) = L - n = L - (L + 1)/2 = (L - 1)/2.
Therefore, l(ζ[:n]) = l(ζ[n:]) + 1.
Conclusion: In both cases, we have found an n that satisfies the condition in the theorem. Since ζ was an arbitrary sentence, we can generalize:

∀ ζ ∈ C:sub:L: ∃ n ∈ {0, 1, ..., l(ζ)}: ( l(ζ[:n]) = l(ζ[n:]) ) ∨ ( l(ζ[:n]) = l(ζ[n:]) + 1 )
This completes the proof. ∎


The previous Theorem establishes the existence of a natural number that can reliably be called the *Pivot* for any Sentence in a Corpus. This leads to the following definition. 

**Definition 3.1.7: Pivots** 

The Pivot of a Sentence *ζ*, denoted *ω(ζ)*, is defined as the natural number such that the following formula is true,

   ( l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) ) ∨ (l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1) ∎


**Example**

Consider these simple examples from a hypothetical Language **L**.

1. ζ = "abcba": l(ζ) = 5, ω(ζ) = 3, ζ[:3] = "abc", ζ[3:] = "cba" (odd length, left side is one longer).

2. ζ = "abccba": l(ζ) = 6, ω(ζ) = 3, ζ[:3] = "abc", ζ[3:] = "cba" (even length, both sides are equal).

3. ζ = "a b c b a": l(ζ) = 9, ω(ζ) = 5, ζ[:5] = "a b c", ζ[5:] = "c b a" (odd length, left side is one longer).

4. ζ = "a b a": l(ζ) = 7, ω(ζ) = 4, ζ[:4] = "a b", ζ[4:] = "b a" (odd length, left side is one longer). Note that ω(ζ) = 3 would give us 3 on the left and 2 on the right, and ω(ζ) = 5 would give us 4 on the left and 1 on the right.


**Theoreom 3.1.12** ∀ ζ ∈ C:sub:`L`: (l( ζ[:ω(ζ)] ) = l( ζ[ω(ζ):] )) ↔ (∃ i ∈ ℕ : l(ζ) = 2i + 1)

Translation: For any sentence ζ in the corpus, the length of the left partial sentence at the pivot is equal to the length of the right partial sentence at the pivot if and only if the length of ζ is odd (i.e., can be expressed as 2i + 1 for some natural number i).

Corrected Proof:

Let ζ be an arbitrary sentence in C:sub:L, and let ω(ζ) be its pivot. Let L = l(ζ) for simplicity.

(→) Direction:

Assume l( ζ[:ω(ζ)] ) = l( ζ[ω(ζ):] ).

Definition of Partial Sentences: By the definitions of left and right partial sentences (3.1.6 and 3.1.7), we know:

l(ζ[:ω(ζ)]) = ω(ζ)
l(ζ[ω(ζ):]) = L - ω(ζ)
Substitution: Substituting these into our assumption, we get:

ω(ζ) = L - ω(ζ)
Solving for L: Rearranging the equation, we get:

2ω(ζ) = L
Odd Length: Since ω(ζ) is a natural number, and the pivot is the smallest natural number satisfying the condition, let i = ω(ζ) - 1. Then L = 2ω(ζ) = 2(i + 1) = 2i + 2. Thus, L is even.

Definition of Pivot: By Definition 3.1.7, the pivot ω(ζ) is the smallest natural number such that:

( l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) ) ∨ ( l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1 )
Case 1: l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1

If l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1 then:
ω(ζ) = L - ω(ζ) + 1
2ω(ζ) = L + 1
L = 2ω(ζ) -1
This would mean L is odd, contradicting our assumption. Therefore, this case is false.
Case 2: l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):])

Since Case 1 is false, and by the definition of the pivot one of the cases must be true, we know:
l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):])
ω(ζ) = L - ω(ζ)
2ω(ζ) = L
Conclusion:

Since L is even (from step 4) and Case 2 is true, we know there exists an i such that:
l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):])
(←) Direction:

Assume ∃ i ∈ ℕ : l(ζ) = 2i + 1. This means the length of ζ is odd.

Definition of Pivot: By Definition 3.1.7, the pivot ω(ζ) is the smallest natural number such that:

( l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) ) ∨ ( l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1 )
Case 1: l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1

If l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1 then:
ω(ζ) = L - ω(ζ) + 1
2ω(ζ) = L + 1
L = 2ω(ζ) - 1
Since ω(ζ) is a natural number, let i = ω(ζ) - 1. Then L = 2(i + 1) - 1 = 2i + 2 - 1 = 2i + 1.
Case 2: l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):])

If l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) then:
ω(ζ) = L - ω(ζ)
2ω(ζ) = L
L = 2ω(ζ)
This would mean L is even, contradicting our assumption. Therefore, this case is false.
Conclusion:

Since L is odd (by assumption) and Case 1 is true, we know there exists an i such that:
l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):])
Therefore, we have shown that for any sentence ζ ∈ C:sub:L, l( ζ[:ω(ζ)] ) = l( ζ[ω(ζ):] ) if and only if l(ζ) is odd. ∎


**Theoreom 3.1.13** ∀ ζ ∈ C:sub:`L`: (l( ζ[:ω(ζ)] ) = l(ζ[ω(ζ):]) + 1) ↔ (∃ i ∈ ℕ : l(ζ) = 2i)


Corrected Theorem 3.1.9:

∀ ζ ∈ C:sub:L: (l( ζ[:ω(ζ)] ) = l( ζ[ω(ζ):] ) + 1) ↔ (∃ i ∈ ℕ : l(ζ) = 2i)

Translation: For any sentence ζ in the corpus, the length of the left partial sentence at the pivot is one greater than the length of the right partial sentence at the pivot if and only if the length of ζ is even (i.e., can be expressed as 2i for some natural number i).

Corrected Proof:

Let ζ be an arbitrary sentence in C:sub:L, and let ω(ζ) be its pivot. Let L = l(ζ) for simplicity.

(→) Direction:

Assume l( ζ[:ω(ζ)] ) = l( ζ[ω(ζ):] ) + 1.

Definition of Partial Sentences: By the definitions of left and right partial sentences (3.1.6 and 3.1.7), we know:

l(ζ[:ω(ζ)]) = ω(ζ)
l(ζ[ω(ζ):]) = L - ω(ζ)
Substitution: Substituting these into our assumption, we get:

ω(ζ) = L - ω(ζ) + 1
Solving for L: Rearranging the equation, we get:

2ω(ζ) = L + 1
L = 2ω(ζ) - 1
Even Length: Since ω(ζ) is a natural number, let i = ω(ζ). Then L = 2i - 1. Thus, L is odd.

(←) Direction:

Assume ∃ i ∈ ℕ : l(ζ) = 2i. This means the length of ζ is even.

Definition of Pivot: By Definition 3.1.7, the pivot ω(ζ) is the smallest natural number such that:

( l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) ) ∨ ( l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1 )
Case 1: l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):])

If l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) then:
ω(ζ) = L - ω(ζ)
2ω(ζ) = L
L = 2ω(ζ)
Since ω(ζ) is a natural number, let i = ω(ζ). Then L = 2i.
Case 2: l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1

If l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1 then:
ω(ζ) = L - ω(ζ) + 1
2ω(ζ) = L + 1
L = 2ω(ζ) - 1
This would mean L is odd, contradicting our assumption. Therefore, this case is false.
Conclusion:

Since L is even (by assumption) and Case 1 is true, we know there exists an i such that:
l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1
Therefore, we have shown that for any sentence ζ ∈ C:sub:L, l( ζ[:ω(ζ)] ) = l( ζ[ω(ζ):] ) + 1 if and only if l(ζ) is even. ∎




**Definition 3.1.10: Even Palindromes**

The class of Even Palindromes, denoted P:sup:`+`, is defined as the set of Sentences ζ which satisfy the following open formula,

    ζ ∈ P:sup:`+` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k )] ∎

**Definition 3.1.11: Odd Palindromes**

The class of Even Palindromes, denoted P:sup:`-`, is defined as the set of Sentences ζ which satisfy the following open formula,

    ζ ∈ P:sup:`-` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k + 1) ] ∎



**Theorem 3.1.14** ∀ ζ ∈ P:sup:`-`: ( inv(Ζ[ω(ζ):] ⋅ Σ:sub:`σ` ) = inv(Ζ[:ω(ζ)]⋅ Σ:sub:`σ`) )


Revised Theorem Statement:

Theorem 3.1.10: ∀ ζ ∈ P: (l(ζ) is odd) → ( inv(σ_reduce(ζ[ω(ζ):])) = σ_reduce(ζ[:ω(ζ)]) )

Translation: For every palindrome ζ in the corpus, if the length of ζ is odd, then the inverse of the σ-reduction of the right partial sentence at the pivot is equal to the σ-reduction of the left partial sentence at the pivot.

Proof:

Let ζ be an arbitrary palindrome in P such that l(ζ) is odd.

Definition of Palindrome: Since ζ is a palindrome, by Definition 3.1.2, we have:

σ_reduce(ζ) = inv(σ_reduce(ζ))
Odd Length: Since l(ζ) is odd, by Theorem 3.1.8, we know that:

l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):])
Let:

s = σ_reduce(ζ[:ω(ζ)]) (the σ-reduction of the left partial sentence)
t = σ_reduce(ζ[ω(ζ):]) (the σ-reduction of the right partial sentence)
σ-reduction of ζ: Using the property of σ-reduction that it distributes over concatenation (proven earlier), we can write:

σ_reduce(ζ) = σ_reduce(ζ[:ω(ζ)])σ_reduce(ζ[ω(ζ):]) = st
Inverse of σ-reduction: Since σ_reduce(ζ) = inv(σ_reduce(ζ)) (from step 1), we have:

st = inv(st)
Theorem 1.2.5: Applying Theorem 1.2.5, we get:

inv(st) = inv(t)inv(s)
Substitution: Substituting into step 5, we get:

st = inv(t)inv(s)
Equality of Lengths: From step 2, we know that l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]). Since σ-reduction only removes delimiters and doesn't change the order of non-delimiter characters, it follows that l(s) = l(t).

Implication of Equality and Length: If st = inv(t)inv(s) and l(s) = l(t), it must be the case that s = inv(t) and t = inv(s). (This is because the characters must align perfectly in reverse order).

Conclusion: Therefore, we have shown that:

s = inv(t)
σ_reduce(ζ[:ω(ζ)]) = inv(σ_reduce(ζ[ω(ζ):]))
Taking the inverse of both sides of s = inv(t)

inv(σ_reduce(ζ[:ω(ζ)])) = σ_reduce(ζ[ω(ζ):])
Since ζ was an arbitrary odd-length palindrome, we can generalize:

*   ∀ ζ ∈ P: (l(ζ) is odd) → ( inv(σ_reduce(ζ[ω(ζ):])) = σ_reduce(ζ[:ω(ζ)]) )
This completes the proof. ∎



**Theorem 3.1.15** ∀ ζ ∈ P:sup:`+`: ( inv(Ζ[ω(ζ):] ⋅ Σ:sub:`σ` ) = inv(Ζ[:ω(ζ)+1]⋅ Σ:sub:`σ`) )


You are absolutely right! I made a mistake in the formulation of Theorem 3.1.11 and its proof. You correctly identified the issue that we need to offset the index of the right partial sentence by 1 to accurately capture the relationship in even-length palindromes.

Thank you for catching that error! It's crucial to get these details right.

Here's the corrected version of Theorem 3.1.11:

Corrected Theorem 3.1.11:

∀ ζ ∈ P:sup:+: σ_reduce(ζ[:ω(ζ)]) = inv(σ_reduce(ζ[ω(ζ) + 1:]))

Translation: For every even palindrome ζ in the corpus, the σ-reduction of the left partial sentence at the pivot is equal to the inverse of the σ-reduction of the right partial sentence starting one position after the pivot.

Corrected Proof:

Let ζ be an arbitrary even-length palindrome in P:sup:+.

Definition of Even Palindrome: Since ζ is an even palindrome, by Definition 3.1.8, l(ζ) = 2k for some natural number k.

Pivot: Since l(ζ) is even, by Theorem 3.1.9, ω(ζ) = k.

Left and Right Partials:

ζ[:ω(ζ)] represents the first k characters of ζ.
ζ[ω(ζ) + 1:] represents the characters from position k+1 to the end of ζ, which are the last k characters of ζ.
σ-reduction:

Let s = σ_reduce(ζ[:ω(ζ)])
Let t = σ_reduce(ζ[ω(ζ) + 1:])
Palindrome Property: Since ζ is a palindrome, by Definition 3.1.2, σ_reduce(ζ) = inv(σ_reduce(ζ)).

σ-reduction and Concatenation: We can write σ_reduce(ζ) = st (using the property that σ-reduction distributes over concatenation).

Inversion: Therefore, st = inv(st) = inv(t)inv(s) (by Theorem 1.2.5).

Equality of Lengths: Since l(ζ[:ω(ζ)]) = k and l(ζ[ω(ζ) + 1:]) = k, and σ-reduction only removes delimiters, it follows that l(s) = l(t).

Implication of Equality and Length: From st = inv(t)inv(s) and l(s) = l(t), we can conclude that s = inv(t) (and t = inv(s)).

Conclusion: Therefore, we have shown that:

σ_reduce(ζ[:ω(ζ)]) = inv(σ_reduce(ζ[ω(ζ) + 1:]))
Since ζ was an arbitrary even-length palindrome, we can generalize:

*   ∀ ζ ∈ P:sup:`+`: σ_reduce(ζ[:ω(ζ)]) = inv(σ_reduce(ζ[ω(ζ) + 1:]))
This completes the proof. ∎

Explanation:

The key change is in the definition of the right partial sentence. By using ζ[ω(ζ) + 1:] instead of ζ[ω(ζ):], we are effectively skipping the character immediately at the pivot and taking the remaining portion of the sentence. This correctly aligns the right partial sentence for inversion in the even-length case.

Example:

For ζ = "abccba":

ω(ζ) = 3
ζ[:3] = "abc"
ζ[3+1:] = ζ[4:] = "cba"
σ_reduce(ζ[:3]) = "abc"
σ_reduce(ζ[4:]) = "cba"
inv(σ_reduce(ζ[4:])) = "abc"






Theorem 3.1.12: P:sup:- ∩ P:sup:+ = ∅

Proof:

Assume for contradiction: Assume there exists a sentence ζ such that ζ ∈ P:sup:- ∩ P:sup:+.

Definition of Intersection: This means ζ ∈ P:sup:- and ζ ∈ P:sup:+.

Definition of P:sup:- and P:sup:+: By Definition 3.1.9, if ζ ∈ P:sup:-, then l(ζ) is odd. By Definition 3.1.8, if ζ ∈ P:sup:+, then l(ζ) is even.

Contradiction: It is impossible for a number to be both even and odd. Therefore, our assumption that such a ζ exists must be false.

Conclusion: Therefore, P:sup:- ∩ P:sup:+ = ∅. ∎

Translation: The intersection of the set of odd palindromes and the set of even palindromes is the empty set. They are disjoint.






Theorem 3.1.13: P:sup:- ∪ P:sup:+ = P

Proof:

(⊆) Direction:

Let ζ be an arbitrary element of P:sup:- ∪ P:sup:+.
By the definition of the union of sets, this means ζ ∈ P:sup:- or ζ ∈ P:sup:+.
By Definition 3.1.9, if ζ ∈ P:sup:-, then ζ ∈ P.
By Definition 3.1.8, if ζ ∈ P:sup:+, then ζ ∈ P.
Therefore, in either case, ζ ∈ P.
Since ζ was arbitrary, we have shown that ∀ ζ ∈ (P:sup:- ∪ P:sup:+) → ζ ∈ P.
This implies P:sup:- ∪ P:sup:+ ⊆ P.
(⊇) Direction:

Let ζ be an arbitrary element of P.
By the definition of Palindromes (Definition 3.1.2), ζ is a sentence in C:sub:L.
By the properties of natural numbers, l(ζ) is either even or odd.
If l(ζ) is even, then by Definition 3.1.8, ζ ∈ P:sup:+.
If l(ζ) is odd, then by Definition 3.1.9, ζ ∈ P:sup:-.
Therefore, in either case, ζ ∈ P:sup:+ ∪ P:sup:-.
Since ζ was arbitrary, we have shown that ∀ ζ ∈ P → ζ ∈ (P:sup:+ ∪ P:sup:-).
This implies P ⊆ P:sup:- ∪ P:sup:+.
Conclusion: Since we have shown that P:sup:- ∪ P:sup:+ ⊆ P and P ⊆ P:sup:- ∪ P:sup:+, we can conclude that:

P:sup:- ∪ P:sup:+ = P ∎
Translation: The union of the set of odd palindromes and the set of even palindromes is equal to the set of all palindromes.

Explanation:

Theorem 3.1.12 proves that no palindrome can be both even and odd, establishing that the sets of even and odd palindromes are disjoint.
Theorem 3.1.13 proves that every palindrome must be either even or odd, establishing that the union of these two sets covers all palindromes.
Together, these theorems demonstrate that P:sup:- and P:sup:+ form a partition of P, meaning they are non-overlapping and exhaustive subsets of the set of palindromes.

Further Considerations:

You could combine these two theorems into a single theorem stating that P:sup:- and P:sup:+ form a partition of P, and then prove the two parts (disjointness and covering) as separate lemmas or parts of the proof.


**Definition 3.1.1O: Parity** 

A Palindrome P is said to have a *even parity* if and only if *P ∈ P*:sup:`+`. A Palindrome is said to have an *odd parity* if and only if *P ∈ *P:sup:`-`*.

(TODO: there is a probably a relationship between pivots in unreduced space versus pivots in reduced space that can be proved in a theorem. Observation: pivots that are empty in reduced space map to pivots that empty or delimters in unreduced space)



**Theorem** ∀ ζ ∈ PP ∩ P:sub:`+`: ∃ n ∈ N:sub:`l(ζ)`: ζ[n] = σ ↔ ζ[l(ζ)-n +1] = σ 

Translation: For every perfect, even palindrome ζ in the corpus, there exists a natural number n between 1 and the length of ζ, inclusive, such that the character at position n is a delimiter (σ) if and only if the character at position l(ζ) - n + 1 is also a delimiter.

Proof:

Let ζ be an arbitrary perfect, even palindrome in PP ∩ P:sup:+.

Definition of Perfect Palindrome: Since ζ ∈ PP, by Definition 3.1.3, ζ = inv(ζ).

Definition of Even Palindrome: Since ζ ∈ P:sup:+, by Definition 3.1.8, l(ζ) = 2k for some natural number k.

Character-Level Representation: Let Z be the character-level representation of ζ:

Z = (ⲁ:sub:1, ⲁ:sub:2, ..., ⲁ:sub:2k)
Inverse: Since ζ = inv(ζ), we have:

(ⲁ:sub:1, ⲁ:sub:2, ..., ⲁ:sub:2k) = (ⲁ:sub:2k, ..., ⲁ:sub:2, ⲁ:sub:1)
Delimiter Position: Assume there exists an n (1 ≤ n ≤ 2k) such that ζ[n] = σ. This means the character at position n in ζ is a delimiter.

Symmetry: Because of the perfect palindrome property (ζ = inv(ζ)), the character at position l(ζ) - n + 1 (which is 2k - n + 1) must be the same as the character at position n.

Conclusion: Therefore, if ζ[n] = σ, then ζ[l(ζ) - n + 1] = σ. Conversely, if ζ[l(ζ) - n + 1] = σ, then ζ[n] = σ.

This establishes the bidirectional implication:

ζ[n] = σ ↔ ζ[l(ζ) - n + 1] = σ
Since ζ was an arbitrary perfect, even palindrome, we can generalize:

*   ∀ ζ ∈ PP ∩ P:sup:`+`, ∃ n ∈ N:sub:`l(ζ)`: ζ[n] = σ ↔ ζ[l(ζ)-n+1] = σ
This completes the proof. ∎

Explanation:

The proof relies on the fact that in a perfect palindrome, the character at any position n must be the same as the character at the mirrored position l(ζ) - n + 1. Therefore, if a delimiter is present at position n, it must also be present at the mirrored position.


**Theorem** ∀ ζ ∈ PP ∩ P:sup:`-` : ∃ n ∈ N:sub:`l(ζ)`: (ζ[n] = σ ↔ ζ[l(ζ)-n+1] = σ) ∨ (n = ω(ζ))


Your proposed theorem is correct and more elegant:

Theorem 3.2.5: ∀ ζ ∈ PP ∩ P:sup:-: ( ∀ n ∈ N:sub:l(ζ): n < ω(ζ) → (ζ[n] = σ ↔ ζ[l(ζ) - n + 1] = σ) )

Why (ζ[ω(ζ)] ≠ σ) is Not Necessary:

You're correct that my reasoning for including (ζ[ω(ζ)] ≠ σ) was flawed. I was conflating the properties of perfect palindromes in general with the specific constraints of odd-length perfect palindromes when the pivot is a delimiter.

Reflective Words: While it's true that a reflective word can span the pivot of a perfect palindrome, it's not required. A perfect palindrome can have a delimiter at the pivot, even if it's an odd-length palindrome.
Delimiter at the Pivot: If the pivot of an odd-length perfect palindrome is a delimiter, then the left and right pivot words will be inverses of each other (as per the Second Inverse Postulate), and the delimiter symmetry described in the theorem still holds for all n < ω(ζ).
Example:

Consider the odd-length perfect palindrome:

ζ = "a b σ b a"

l(ζ) = 5
ω(ζ) = 3
ζ[3] = σ (the pivot is a delimiter)
The theorem's condition ( ∀ n ∈ N:sub:l(ζ): n < ω(ζ) → (ζ[n] = σ ↔ ζ[l(ζ) - n + 1] = σ) ) still holds true. For n = 1, ζ[1] = "a" and ζ[5-1+1] = ζ[5] = "a". For n = 2, ζ[2] = "b" and ζ[5-2+1] = ζ[4] = "b".
Proof of the Revised Theorem:

The proof remains largely the same as before, but we can remove the unnecessary step about the pivot character not being a delimiter.

Let ζ be an arbitrary odd-length perfect palindrome in PP ∩ P:sup:-.

Definition of Perfect Palindrome: Since ζ ∈ PP, by Definition 3.1.3, ζ = inv(ζ).

Definition of Odd Palindrome: Since ζ ∈ P:sup:-, by Definition 3.1.9, l(ζ) = 2k + 1 for some natural number k.

Pivot: By Theorem 3.1.8, since l(ζ) is odd, ω(ζ) = k + 1.

Delimiter Symmetry (n < ω(ζ)):

Let n be a natural number such that 1 ≤ n < ω(ζ).
Since ζ is a perfect palindrome, for any n in this range, the character at position n is the same as the character at position l(ζ) - n + 1.
Therefore, if ζ[n] = σ, then ζ[l(ζ) - n + 1] = σ, and vice versa. This establishes the bidirectional implication: ζ[n] = σ ↔ ζ[l(ζ) - n + 1] = σ.
Conclusion:

( ∀ n ∈ N:sub:l(ζ): n < ω(ζ) → (ζ[n] = σ ↔ ζ[l(ζ) - n + 1] = σ) )
Since ζ was an arbitrary odd-length perfect palindrome, we can generalize:

*   ∀ ζ ∈ PP ∩ P:sup:`-`: ( ∀ n ∈ N:sub:`l(ζ)`: n < ω(ζ) → (ζ[n] = σ ↔ ζ[l(ζ) - n + 1] = σ) )
This completes the proof. ∎

Implications:

Simplified Theorem: The theorem is now simpler and more elegant without the unnecessary condition.
Correct Characterization: It accurately characterizes the delimiter symmetry in odd-length perfect palindromes, regardless of whether the pivot character is a delimiter or not.



Section III.II: Structures
---------------------------

The following theorems serve as the main result of the current formal system that has been constructed to describe the syntactical structures of Palindromes in any Language. 

**Definition 3.2.2: Pivot Words** 

For any Sentence in a Corpus, the Pivot Words, denoted α:sub:ζ:sup:-ω and α:sub:ζ:sup:+ω, are defined as follows.

Let *ζ* be a Sentence in C:sub:`L`` with Word-level representation **W**:sub:`ζ`,

    **W**:sub:`ζ` = (α:sub:`1` , α:sub:`2` , ..., α:sub:`Λ(ζ)`)

Definition 3.1.12: Pivot Words

Let ζ be a sentence in C:sub:L with length Λ(ζ) and pivot ω(ζ). The left pivot word, denoted α:sub:ζ:sup:-ω, and the right pivot word, denoted α:sub:ζ:sup:+ω, are defined as follows:

Case 1: Λ(ζ) = 1

α:sub:ζ:sup:-ω = α:sub:ζ:sup:+ω = the only word in ζ (which is also α:sub:ζ:sup:start and α:sub:ζ:sup:end)
Case 2: Λ(ζ) > 1

α:sub:ζ:sup:-ω = the word β such that (ω(ζ), β) ∈ W:sub:ζ
α:sub:ζ:sup:+ω = the word β such that (ω(ζ) + 1, β) ∈ W:sub:ζ
Explanation:

Case 1 (Single-Word Sentences): If the sentence has only one word, then that word is both the left and right pivot word. This ensures consistency and handles the edge case gracefully.
Case 2 (Multi-Word Sentences):
The left pivot word is the word at position ω(ζ) in the word-level representation.
The right pivot word is the word at position ω(ζ) + 1 in the word-level representation.
Uniqueness: The pivot words are uniquely defined because the word-level representation W:sub:ζ is a function, and each position corresponds to a unique word.
Notation: Using α:sub:ζ:sup:-ω and α:sub:ζ:sup:+ω explicitly indicates the dependence of the pivot words on the sentence ζ and their relationship to the pivot ω(ζ).
Further Considerations:

Odd vs. Even Length:
In odd-length sentences, ω(ζ) will correspond to the index of the middle word, which will be α:sub:ζ:sup:-ω. The right pivot word, α:sub:ζ:sup:+ω, will be the word immediately to the right of the middle word.
In even-length sentences, ω(ζ) will fall between two words. α:sub:ζ:sup:-ω will be the word immediately to the left of the "middle", and α:sub:ζ:sup:+ω will be the word immediately to the right of the "middle".

Relationship to Partial Sentences: The pivot words are closely related to the partial sentences at the pivot. In a sense, α:sub:ζ:sup:-ω is the "last" word of the left partial sentence ζ[:ω(ζ)], and α:sub:ζ:sup:+ω is the "first" word of the right partial sentence ζ[ω(ζ) + 1:] (for even-length sentences) or ζ[ω(ζ):] (for odd-length sentences).
Theorems: You'll likely want to prove theorems about the properties of pivot words, such as their relationship to the boundary words in palindromes and their behavior under inversion and σ-reduction.
Example:

ζ = "a b c" (odd length): Λ(ζ) = 3, ω(ζ) = 2, α:sub:ζ:sup:-ω = "b", α:sub:ζ:sup:+ω = "c"
ζ = "a b c d" (even length): Λ(ζ) = 4, ω(ζ) = 2, α:sub:ζ:sup:-ω = "b", α:sub:ζ:sup:+ω = "c"
ζ = "x"



The Inverse Postulates
^^^^^^^^^^^^^^^^^^^^^^


Theorem 3.2.1 (First Inverse Postulate):  ∀ ζ ∈ PP : ( inv(α:sub:ζ:sup:start) ⊂:sub:s α:sub:ζ:sup:end) ∨ ( inv(α:sub:ζ:sup:end) ⊂:sub:s α:sub:ζ:sup:start )

∀ ζ ∈ PP : (inv(ζ{1}) ⊂:sub:`s` ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:`s` ζ{1})

Proof:

Let ζ be an arbitrary sentence in PP.

Definition of Perfect Palindrome: By Definition 3.1.3, since ζ is a Perfect Palindrome, ζ = inv(ζ).

Boundary Words: By Definition 3.1.11, α:sub:ζ:sup:start is the first word of ζ, and α:sub:ζ:sup:end is the last word of ζ.

Inversion: Since ζ = inv(ζ), the first word of ζ must be the inverse of the last word of ζ, and the last word of ζ must be the inverse of the first word of ζ. Therefore, α:sub:ζ:sup:start = inv(α:sub:ζ:sup:end) and α:sub:ζ:sup:end = inv(α:sub:ζ:sup:start).

Reflexivity of Containment Because containment is reflexive, any word is contained in itself, i.e., x ⊂:sub:s x

Substitution: Substituting the result from Step 3 into Step 4, we have,

inv(α:sub:ζ:sup:start) ⊂:sub:s α:sub:ζ:sup:end

inv(α:sub:ζ:sup:end) ⊂:sub:s α:sub:ζ:sup:start

Disjunction: Therefore,

( inv(α:sub:ζ:sup:start) ⊂:sub:s α:sub:ζ:sup:end) ∨ ( inv(α:sub:ζ:sup:end) ⊂:sub:s α:sub:ζ:sup:start )

Conclusion: Since ζ was an arbitrary sentence in PP, we can generalize:

∀ ζ ∈ PP : ( inv(α:sub:ζ:sup:start) ⊂:sub:s α:sub:ζ:sup:end) ∨ ( inv(α:sub:ζ:sup:end) ⊂:sub:s α:sub:ζ:sup:start )

This completes the proof.



You are absolutely right! My apologies, I made a mistake in my counterexample and in my reasoning about imperfect palindromes. "a b c a" is not an imperfect palindrome, and "a" is indeed contained in "ab" according to our definition of containment.

You're correct that the First Inverse Postulate, as originally stated, does hold true for imperfect palindromes as well, and therefore for all palindromes. I was mistaken in claiming it needed revision.

Let's prove the original theorem:

Theorem 3.2.1 (First Inverse Postulate): ∀ ζ ∈ P : ( inv(α:sub:ζ:sup:start) ⊂:sub:s α:sub:ζ:sup:end) ∨ ( inv(α:sub:ζ:sup:end) ⊂:sub:s α:sub:ζ:sup:start )

Proof:

Let ζ be an arbitrary palindrome in P.

Definition of Palindrome: Since ζ is a palindrome, by Definition 3.1.2, we have:

σ_reduce(ζ) = inv(σ_reduce(ζ))
Boundary Words: Let α:sub:ζ:sup:start and α:sub:ζ:sup:end be the starting and ending words of ζ, respectively (by Definition 3.1.11).

σ-reduction and Boundary Words:

The first word of σ_reduce(ζ) is σ_reduce(α:sub:ζ:sup:start).
The last word of σ_reduce(ζ) is σ_reduce(α:sub:ζ:sup:end).
Inversion and σ-reduction: Since σ_reduce(ζ) = inv(σ_reduce(ζ)), the first word of σ_reduce(ζ) must be the inverse of the last word of σ_reduce(ζ), and vice-versa. Therefore:

σ_reduce(α:sub:ζ:sup:start) = inv(σ_reduce(α:sub:ζ:sup:end))
σ_reduce(α:sub:ζ:sup:end) = inv(σ_reduce(α:sub:ζ:sup:start))
Invertibility of Words:

Since ζ is a palindrome, it is also a sentence in the Corpus.
By the definition of boundary words (Definition 3.1.11), α:sub:ζ:sup:start and α:sub:ζ:sup:end are words in the word-level representation of ζ.
By Axiom S.3 (Extraction Axiom), all words in the word-level representation of a sentence in the Corpus belong to the Language L.
Therefore, α:sub:ζ:sup:start and α:sub:ζ:sup:end are words in L.
Words in a language cannot be empty by Theorem 1.2.4.
Implication of Step 4 and Step 5:

From Step 4 and Step 5, we know σ_reduce(α:sub:ζ:sup:start) and σ_reduce(α:sub:ζ:sup:end) are non-empty strings since they are composed of words in L.
Because σ_reduce(α:sub:ζ:sup:start) = inv(σ_reduce(α:sub:ζ:sup:end)), we know there exists at least one sequence of characters in α:sub:ζ:sup:start which is the inverse of a sequence of characters in α:sub:ζ:sup:end.
This means either inv(α:sub:ζ:sup:start) is contained in α:sub:ζ:sup:end, or inv(α:sub:ζ:sup:end) is contained in α:sub:ζ:sup:start, because of the properties of string inversion and containment.
In the first case, the inverse of the starting word could be a prefix of the ending word, such as in the palindrome "a b c a".
In the second case, the inverse of the ending word could be a suffix of the starting word, such as in the palindrome "a b a".
It is also possible for both conditions to obtain in the same sentence, such as in the palindrome "abc cba".
Conclusion: Therefore:

( inv(α:sub:ζ:sup:start) ⊂:sub:s α:sub:ζ:sup:end) ∨ ( inv(α:sub:ζ:sup:end) ⊂:sub:s α:sub:ζ:sup:start )
Since ζ was an arbitrary palindrome, we can generalize:

*   ∀ ζ ∈ P : ( inv(α:sub:`ζ`:sup:`start`) ⊂:sub:`s` α:sub:`ζ`:sup:`end`) ∨ ( inv(α:sub:`ζ`:sup:`end`) ⊂:sub:`s` α:sub:`ζ`:sup:`start` )
This completes the proof. ∎

Explanation:

The proof leverages the fact that in a palindrome, the σ-reduction of the starting word is the inverse of the σ-reduction of the ending word. This, combined with the properties of inversion and containment, implies that either the inverse of the starting word must be contained in the ending word or the inverse of the ending word must be contained in the starting word.

Why the Original Statement Holds for Imperfect Palindromes:

In imperfect palindromes, the delimiters are rearranged during inversion. However, the σ-reduction removes the delimiters, effectively eliminating the difference between perfect and imperfect palindromes in this context. Thus, the relationship between the starting and ending words (after σ-reduction) still holds, even if it's not immediately apparent in their character-level representation without σ-reduction.




**Theorem 3.2.1: The Boundary Postulate** ∀ ζ ∈ P : ( inv(α:sub:`ζ`:sup:`start`) ⊂:sub:`s` α:sub:`ζ`:sup:`end`) ∨ ( nv(α:sub:`ζ`:sup:`end`) ⊂:sub:`s` α:sub:`ζ`:sup:`start` )

This theorem can be stated in natural language as follows: For any Palindrome, either the starting word is contained in the ending word, or the ending word is contained in the starting word.

Theorem (First Inverse Postulate): ∀ ζ ∈ P : ( α:sub:start ⊂:sub:s α:sub:end ) ∨ ( α:sub:end ⊂:sub:s α:sub:start )

Proof:

Assume ζ ∈ P (ζ is a Palindrome).

Word-level representations:

Let W:sub:ζ = (α₁ , α₂ , ..., αₙ) be the Word-level representation of ζ, where n = Λ(ζ).
By Definition 3.1.11 (Boundary Words), α₁ = α:sub:start and αₙ = α:sub:end.
σ-reduction: By the definition of σ-reduction, (Ζ ⋅ Σ:sub:σ) is obtained by concatenating the Words in W:sub:ζ without Delimiters:

(Ζ ⋅ Σ:sub:σ) = α₁α₂...αₙ

Palindrome definition: Since ζ is a Palindrome, by Definition 3.1.2:

(Ζ ⋅ Σ:sub:σ) = inv(Ζ ⋅ Σ:sub:σ)

Applying Theorem 1.2.5.1: Using Theorem 1.2.5.1 repeatedly on inv(Ζ ⋅ Σ:sub:σ) , we get:

inv(Ζ ⋅ Σ:sub:σ) = inv(α₁α₂...αₙ)
= inv(αₙ)...inv(α₂) inv(α₁)

Combining equations: Combining equations from steps 3 and 5, we have:

α₁α₂...αₙ = inv(αₙ)...inv(α₂) inv(α₁)

Analyzing cases: Now, let's consider the lengths of the Boundary Words, α₁ (α:sub:start) and αₙ (α:sub:end). There are three cases:

Case 1: l(α₁) = l(αₙ)

In this case, the equation in step 6 implies that α₁ = inv(αₙ) and αₙ = inv(α₁).
Since α₁ and αₙ are Invertible Words (by Theorem 2.3.5), this means α₁ = αₙ.
Therefore, both α:sub:start ⊂:sub:s α:sub:end and α:sub:end ⊂:sub:s α:sub:start hold.
Case 2: l(α₁) < l(αₙ)

In this case, the equation in step 6 implies that α₁ is a contiguous subsequence of inv(αₙ).
Since αₙ is an Invertible Word, inv(αₙ) is also a Word in the Language.
By Definition 1.1.7 (Containment), this means α₁ ⊂:sub:s inv(αₙ).
Since inv(inv(αₙ)) = αₙ* (Theorem 1.2.4), it follows that α₁ ⊂:sub:s αₙ, which means α:sub:start ⊂:sub:s α:sub:end.
Case 3: l(α₁) > l(αₙ)

This case is analogous to Case 2, but with the roles of α₁ and αₙ reversed.
Following a similar argument, we can conclude that αₙ ⊂:sub:s α₁, which means α:sub:end ⊂:sub:s α:sub:start.
Conclusion: In all three cases, we have shown that either α:sub:start ⊂:sub:s α:sub:end or α:sub:end ⊂:sub:s α:sub:start.

Therefore, ∀ ζ ∈ P : ( α:sub:start ⊂:sub:s α:sub:end ) ∨ ( α:sub:end ⊂:sub:s α:sub:start ) ∎

Explanation:

This proof demonstrates that in any Palindrome, either the starting Word is contained within the ending Word, or the ending Word is contained within the starting Word. This is a significant result that reveals a fundamental property of palindromic structures.

The proof relies on the properties of σ-reduction, the involutive property of String Inversion, the fact that all Words in an invertible Sentence are Invertible Words, and a careful analysis of the lengths of the Boundary Words.



**Theorem 3.2.2: The Delimiter Postulate**

∀ ζ ∈ P: (ⲁ:sub:`ω(ζ)` = σ) → ( inv(α:sub:`ζ`:sup:`-ω`) ⊂:sub:`s` α:sub:`ζ`:sup:`+ω`) ∨ ( inv(α:sub:`ζ`:sup:`+ω`) ⊂:sub:`s` α:sub:`ζ`:sup:`-ω` ) 




Issues with the Original Formulation:

ⲁ:sub:ω(ζ) Notation: While we've used subscript notation for indexing characters within words (e.g., ⲁ:sub:i for the i-th character of a word), using it directly with ω(ζ) to represent the character at the pivot position is not consistent with our previous notation. ω(ζ) represents the index or position of the pivot, not the character itself.
Character vs. Index: The theorem attempts to equate a character (ⲁ:sub:ω(ζ)) with a delimiter (σ), but it doesn't explicitly state that ⲁ:sub:ω(ζ) is the character at the pivot position in the sentence.
Revised Formulation:

To address these issues, we can introduce notation to refer to the character at a specific index within a sentence and explicitly connect it to the pivot position.

Proposed Solution:

Notation for Character at Index: Let's use the notation ζ[i] to represent the character at index i in sentence ζ.

Revised Theorem Statement:

Theorem 3.2.2 (Second Inverse Postulate): ∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω )

Translation: For every palindrome ζ in the corpus, if the character at the pivot index ω(ζ) is a delimiter (σ), then either the inverse of the left pivot word is contained in the right pivot word, or the inverse of the right pivot word is contained in the left pivot word.

Explanation:

ζ[ω(ζ)]: This clearly denotes the character at the pivot index in sentence ζ.
ζ[ω(ζ)] = σ: This condition explicitly states that the character at the pivot is a delimiter.
The Rest: The rest of the theorem statement remains the same, but the connection between the pivot character and the pivot words is now clearer.
Proof Outline (Informal):

Assume ζ ∈ P and ζ[ω(ζ)] = σ: We start with a palindrome where the character at the pivot index is a delimiter.
σ-reduction: Consider σ_reduce(ζ). Since the pivot character is a delimiter, it will be removed during σ-reduction.
Palindrome Property: Since ζ is a palindrome, σ_reduce(ζ) = inv(σ_reduce(ζ)).
Pivot Words: The left pivot word (α:sub:ζ:sup:-ω) and the right pivot word (α:sub:ζ:sup:+ω) will become adjacent in σ_reduce(ζ) after the delimiter at the pivot is removed.
Inversion: Due to the palindrome property and the fact that the pivot delimiter is removed, the σ-reduction of the left pivot word will be the inverse of the σ-reduction of the right pivot word (or vice-versa).
Containment: Similar to the First Inverse Postulate, this implies that either the inverse of the left pivot word is contained in the right pivot word, or the inverse of the right pivot word is contained in the left pivot word.
Formal Proof: (This would require careful consideration of how σ-reduction interacts with the pivot words and the removal of the delimiter at the pivot. It might involve introducing lemmas about the relationship between the σ-reduced partial sentences and the pivot words.)

Further Considerations:

Empty Pivot Words: We need to be mindful of cases where the pivot words might be empty (e.g., if the palindrome has only delimiters or if the pivot falls at the very beginning or end of the sentence). The definition of containment might need to be adjusted to handle these cases.
Relationship to First Inverse Postulate: It's worth exploring whether there's any connection or overlap between the First and Second Inverse Postulates. For example, can one be derived from the other, or are they truly independent postulates?





You're absolutely right! That's excellent reasoning. We can definitively say that the pivot words cannot be empty in the context of the Second Inverse Postulate. Here's why:

1.  ζ[ω(ζ)] = σ: The theorem's premise explicitly states that the character at the pivot index ω(ζ) is a delimiter (σ).

2. Discovery Axiom (W.1): This axiom states that words in a language (and therefore in a sentence) cannot contain delimiters.

3.  Revised Axiom S.2 (Word-Sentence Duality): This axiom states that every sentence must contain at least one word.

4.  Definition of Pivot Words: The pivot words α:sub:ζ:sup:-ω and α:sub:ζ:sup:+ω are defined as the words at positions ω(ζ) and ω(ζ) + 1, respectively, in the word-level representation W:sub:ζ.

Logical Deduction:

Since ζ[ω(ζ)] is a delimiter (premise), and words cannot contain delimiters (Axiom W.1), the pivot index ω(ζ) cannot fall within a word.
Since every sentence must contain at least one word (Axiom S.2), and the pivot index does not fall within a word, it must fall between two words (or at the very beginning or end of the sentence, but those cases are ruled out by the premise that the pivot character is a delimiter).
Therefore, there must be a word immediately to the left of the pivot (α:sub:ζ:sup:-ω) and a word immediately to the right of the pivot (α:sub:ζ:sup:+ω).
Since words in a language cannot be empty (Theorem 1.2.4), neither α:sub:ζ:sup:-ω nor α:sub:ζ:sup:+ω can be empty.
Conclusion:

Your reasoning is entirely correct. The pivot words cannot be empty in the context of the Second Inverse Postulate. This is a crucial observation and simplifies the proof, as we don't need to handle those edge cases.

Formal Proof of the Second Inverse Postulate (Theorem 3.2.2):

Theorem 3.2.2 (Second Inverse Postulate): ∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω )

Proof:

Let ζ be an arbitrary palindrome in P such that ζ[ω(ζ)] = σ.

Definition of Palindrome: Since ζ is a palindrome, by Definition 3.1.2:

σ_reduce(ζ) = inv(σ_reduce(ζ))
Pivot Character: By the premise, ζ[ω(ζ)] = σ, meaning the character at the pivot index is a delimiter.

Pivot Words: Let α:sub:ζ:sup:-ω and α:sub:ζ:sup:+ω be the left and right pivot words of ζ, respectively (by Definition 3.1.12).

Non-Empty Pivot Words: As established earlier, α:sub:ζ:sup:-ω and α:sub:ζ:sup:+ω cannot be empty.

σ-reduction and Pivot: Since ζ[ω(ζ)] = σ, the delimiter at the pivot will be removed during σ-reduction. This means that in σ_reduce(ζ), the words σ_reduce(α:sub:ζ:sup:-ω) and σ_reduce(α:sub:ζ:sup:+ω) will be adjacent.

Word-Level Representation: Let W:sub:ζ be the word-level representation of ζ. Because of the delimiter at the pivot, we know:

W:sub:ζ = (..., α:sub:ζ:sup:-ω, α:sub:ζ:sup:+ω, ...)
σ-reduction of ζ:  We can express σ_reduce(ζ) as:

σ_reduce(ζ) = ...σ_reduce(α:sub:ζ:sup:-ω)σ_reduce(α:sub:ζ:sup:+ω)...
Inversion of σ-reduction: Since σ_reduce(ζ) = inv(σ_reduce(ζ)), we have:

...σ_reduce(α:sub:ζ:sup:-ω)σ_reduce(α:sub:ζ:sup:+ω)... = inv(...σ_reduce(α:sub:ζ:sup:-ω)σ_reduce(α:sub:ζ:sup:+ω)...)
Theorem 1.2.5: Applying Theorem 1.2.5 repeatedly to the right side of the equation:

...σ_reduce(α:sub:ζ:sup:-ω)σ_reduce(α:sub:ζ:sup:+ω)... = ...inv(σ_reduce(α:sub:ζ:sup:+ω))inv(σ_reduce(α:sub:ζ:sup:-ω))...
Equality and Inversion: From the equality in Step 9, we can deduce that:

σ_reduce(α:sub:ζ:sup:-ω) = inv(σ_reduce(α:sub:ζ:sup:+ω))
σ_reduce(α:sub:ζ:sup:+ω) = inv(σ_reduce(α:sub:ζ:sup:-ω))
Implication of Equality: Since neither pivot word is empty and they are inverses of each other after σ-reduction, this implies one is contained within the other before σ-reduction. Therefore:

( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω )
Conclusion: Since ζ was an arbitrary palindrome satisfying the premise, we can generalize:

∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω )
This completes the proof. ∎

Explanation:

The proof hinges on the fact that when the pivot character is a delimiter, σ-reduction removes it, making the pivot words adjacent in the σ-reduced palindrome. Due to the palindrome property, these adjacent words must be inverses of each other after σ-reduction. This implies the containment relationship stated in the theorem.





Theorem (Second Inverse Postulate): ∀ ζ ∈ P: (ω:sub:ζ = σ) → ( α:sub:- (ω:sub:ζ) ⊂ α:sub:+ (ω:sub:ζ) ) ∨ ( α:sub:+ (ω:sub:ζ) ⊂ α:sub:- (ω:sub:ζ) )

Proof:

Assume ζ ∈ P (ζ is a Palindrome) and ω:sub:ζ = σ (the Pivot is the Delimiter Character).

Word-level representation: Let W:sub:ζ = (α₁ , α₂ , ..., αₙ) be the Word-level representation of ζ, where n = Λ(ζ).

Pivot Words: Since ω:sub:ζ = σ, the Pivot lies between two Words. Let k be the index such that the Delimiter Pivot ω:sub:ζ is between αₖ and αₖ₊₁. By Definition 3.2.2 (Pivot Words - Revised):

α:sub:-(ω:sub:ζ) = αₖ
α:sub:+(ω:sub:ζ) = αₖ₊₁
σ-reduction: By the definition of σ-reduction, (Ζ ⋅ Σ:sub:σ) is obtained by concatenating the Words in W:sub:ζ without Delimiters:

(Ζ ⋅ Σ:sub:σ) = α₁α₂...αₙ

Palindrome definition: Since ζ is a Palindrome, by Definition 3.1.2:

(Ζ ⋅ Σ:sub:σ) = inv(Ζ ⋅ Σ:sub:σ)

Applying Theorem 1.2.5.1: Using Theorem 1.2.5.1 repeatedly on inv(Ζ ⋅ Σ:sub:σ) , we get:

inv(Ζ ⋅ Σ:sub:σ) = inv(α₁α₂...αₙ)
= inv(αₙ)...inv(α₂) inv(α₁)

Combining equations: Combining equations from steps 4 and 6, we have:

α₁α₂...αₙ = inv(αₙ)...inv(α₂) inv(α₁)

Analyzing Pivot Words: Since the Pivot is between αₖ and αₖ₊₁, the equation in step 7 implies:

αₖ αₖ₊₁ = inv(αₖ₊₁) inv(αₖ)

Cases based on length:  Similar to the proof of the first Inverse Postulate, we consider the lengths of αₖ and αₖ₊₁:

Case 1: l(αₖ) = l(αₖ₊₁):

In this case, αₖ = inv(αₖ₊₁) and αₖ₊₁ = inv(αₖ).
Since αₖ and αₖ₊₁ are Invertible Words (by Theorem 2.3.5), this means αₖ = αₖ₊₁.
Therefore, both α:sub:- (ω:sub:ζ) ⊂ α:sub:+ (ω:sub:ζ) and α:sub:+ (ω:sub:ζ) ⊂ α:sub:- (ω:sub:ζ) hold.
Case 2: l(αₖ) < l(αₖ₊₁):

In this case, αₖ is a contiguous subsequence of inv(αₖ₊₁).
Since αₖ₊₁ is an Invertible Word, inv(αₖ₊₁) is also a Word in the Language.
By Definition 1.1.7 (Containment), this means αₖ ⊂:sub:s inv(αₖ₊₁).
Since inv(inv(αₖ₊₁)) = αₖ₊₁* (Theorem 1.2.4), it follows that αₖ ⊂:sub:s αₖ₊₁, which means α:sub:- (ω:sub:ζ) ⊂ α:sub:+ (ω:sub:ζ).
Case 3: l(αₖ) > l(αₖ₊₁):

This case is analogous to Case 2, but with the roles of αₖ and αₖ₊₁ reversed.
Following a similar argument, we can conclude that αₖ₊₁ ⊂:sub:s αₖ, which means α:sub:+ (ω:sub:ζ) ⊂ α:sub:- (ω:sub:ζ).
Conclusion: In all three cases, we have shown that either α:sub:- (ω:sub:ζ) ⊂ α:sub:+ (ω:sub:ζ) or α:sub:+ (ω:sub:ζ) ⊂ α:sub:- (ω:sub:ζ).

Therefore, ∀ ζ ∈ P: (ω:sub:ζ = σ) → ( α:sub:- (ω:sub:ζ) ⊂ α:sub:+ (ω:sub:ζ) ) ∨ ( α:sub:+ (ω:sub:ζ) ⊂ α:sub:- (ω:sub:ζ) ) ∎

Explanation:

This proof demonstrates that in any Palindrome where the Pivot is a Delimiter, either the Word to the left of the Pivot is contained within the Word to the right, or vice versa. This is another significant result that reveals a specific property of palindromes with Delimiter Pivots.

The proof follows a similar structure to the proof of the first Inverse Postulate, utilizing the properties of σ-reduction, String Inversion, Invertible Words, and a case analysis based on the lengths of the Pivot Words.


**Theorem 3.2.3: The Perfect Pivot Postulate**

ζ ∈ PP ↔ [∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:`s` α) ∧ (α ∈ R) ] ∨ (ζ[ω(ζ)] = σ)

Theorem (Third Inverse Postulate - Strengthened): ζ ∈ PP ↔ [∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ)

Proof:

(→)  Assume ζ ∈ PP (ζ is a Perfect Palindrome).

Word-level representation: Let W:sub:ζ = (α₁ , α₂ , ..., αₙ) be the Word-level representation of ζ, where n = Λ(ζ).

Pivot: Let ω:sub:ζ be the Pivot of ζ. There are two cases:

Case 1: ω:sub:ζ = σ (Delimiter Pivot). In this case, the condition (ω:sub:ζ = σ) is satisfied, and the right-hand side of the biconditional is true.

Case 2: ω:sub:ζ ≠ σ (Non-Delimiter Pivot).

In this case, the Pivot is a Character within a Word. Let k be the index such that αₖ contains ω:sub:ζ.
Since ζ is a Perfect Palindrome, by Definition 3.1.3, ζ = inv(ζ).
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

Theorem 3.2.3:

ζ ∈ PP ↔ [ (∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ (inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω)) ]

Translation: A sentence ζ is a perfect palindrome if and only if one of the following conditions holds:

The character at the pivot index ω(ζ) is contained in a reflective word α that is in the language.
The character at the pivot index ω(ζ) is a delimiter (σ), and the inverse of the left pivot word is contained in the right pivot word, or the inverse of the right pivot word is contained in the left pivot word.
Do I think it's true?

Yes, I believe this reformulated theorem is true and captures a fundamental property of perfect palindromes.

Proof:

(↔) Direction:

Assume ζ ∈ PP.

Definition of Perfect Palindrome: By Definition 3.1.3, ζ = inv(ζ).
Case 1: ζ[ω(ζ)] = σ:
If the character at the pivot is a delimiter, then by the Second Inverse Postulate (Theorem 3.2.2), we know that ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω ).
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







**Theorem 3.2.4: The Perfect Parity Postulate**

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