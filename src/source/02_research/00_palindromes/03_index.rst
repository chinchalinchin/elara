Glossary
========

Notation 
--------

- Punctuation: ∎
- Logical Operations: ∀, ∃, ↔, →, ∧, ∨
- Arithmetical Relations: ≠, =, ≥, ≤, +, -
- Sets: ∅, ℕ, N:sub:`i`
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
- Sentence Classes: A(n), K, P, PP, IP, P:sup:`-`, P:sup:`+`
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
- D 1.2.8: Limitation: Π:sub:`i=1`:sup:`n` P:sub:`n`(i)
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

Algorithms
----------

- A.1: Emptying Algorithm
- A.2: Delimiting Algorithm 

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
- T 1.2.6: ∀ n ∈ ℕ, ∀ P:sub:`n` ∈ Χ:sub:`L(n)` ∃! s ∈ S: s = Π:sub:`i=1`:sup:`n` P:sub:`n`(i)
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
- T 2.3.3: ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ inv(ζ) ∈ K
- T 2.3.4: ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → ζ ∈ C:sub:`L`
- T 2.3.5: ∀ ζ ∈ C:sub:`L`: ζ ∈ K → ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
- T 2.3.6: ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ (∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})) ∧ (inv(ζ) ∈ A(Λ(ζ)))