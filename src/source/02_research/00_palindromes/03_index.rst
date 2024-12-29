Definitions 
- D 1.1.1: Concatenation
- D 1.1.2: Character-Level Set Representation
- D 1.1.3: String Length: l(t)
- D 1.1.4: String Equality
- D 1.1.5: Character Index Notation: t[i]
- D 1.1.6: Consecutive Functions
- D 1.1.7: Containment
- D 1.2.1: Language
- D 1.2.2: Word
- D 1.2.3: Word Equality
- D 1.2.4: String Inversion
- D 1.2.5: Phrase
- D 1.2.6: Delimitation
- D 1.3.1: Reflective Words: α ∈ R ↔ ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1] 
- D 1.3.2: Invertible Words: α ∈ I ↔ inv(α) ∈ L
- D 2.1.1: Corpus
- D 2.1.2: Sentence
- D 2.1.3: Word-Level Set Representation
- D 2.1.4: Word Length: Λ(ζ)
- D 2.1.5: Word Index Notation: ζ{i}
- D 2.2.1: Semantic Coherence
- D 2.3.1: Fathomable Sentences: 
- D 2.3.2: Invertible Sentences: ζ ∈ K ↔ inv(ζ) ∈ C:sub:`L`

Algorithms 
- A.1: Emptying Algorithm
- A.2: Delimiting Algorithm 
- 
Axioms 
- C.1: ∀ ⲁ ∈ Σ: ⲁ ∈ S
- W.1: ∀ α ∈ L: [ (l(α) ≠ 0) ∧ (∀ i ∈ N:sub:`l(α)`: α[i] ≠ σ) ]
- S.1: ( ∀ α ∈ L: ∃ ζ ∈ C:sub:`L``: α ⊂:sub:`s` ζ ) ∧ ( ∀ ζ ∈ C:sub:`L`: ∃ α ∈ L: α ⊂:sub:`s` ζ )
- S.2: ∀ ζ ∈ C:sub:`L` : ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ L

Theorems
- T 1.1.1: ∀ u, t ∈ S: l(ut) = l(u) + l(t)
- T 1.1.2: | S | ≥ ℵ:sub:`1`
- T 1.1.3: ∀ s ∈ S: ε ⊂:sub:`s` s
- T 1.2.1: ∀ α ∈ L:  αε = εα = α
- T 1.2.2: ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: α[i] ⊂:sub:`s` α
- T 1.2.3: ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: α[i] ≠ ε
- T 1.2.4: ∀ s ∈ S: inv(inv(s)) = s
- T 1.2.5: ∀ u, t ∈ S: inv(ut) = inv(t)inv(u)
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
- T 2.3.1: ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ inv(ζ) ∈ K
- T 2.3.2: ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → ζ ∈ C:sub:`L`
- T 2.3.3: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ ∈ K → inv(ζ){i} ∈ L
- T 2.3.4: ∀ ζ ∈ C:sub:`L`: ζ ∈ K ↔ ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})