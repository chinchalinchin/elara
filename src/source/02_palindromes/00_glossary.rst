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