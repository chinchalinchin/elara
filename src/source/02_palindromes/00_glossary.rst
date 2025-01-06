.. _glossary:

Glossary
========

.. _notation:

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

.. _definitions:

Definitions 
-----------

- D 1.1.1: Concatenation: ut
- D 1.1.2: Character-Level Set Representation: **T**
- D 1.1.3: String Length: l(t)
- D 1.1.4: String Equality: u = t
- D 1.1.5: Character Index Notation: t[i]
- D 1.1.6: Consecutive Functions: f(i)
- D 1.1.7: Containment: :math:`t \subset_{s} u`
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
- D 3.2.1: Delimiter Count Function: Δ(t) = | D:sub:`t` | 
- D 4.1.1: Palindromes: ζ ∈ P ↔ (ς(ζ) = inv(ς(ζ))) 
- D 4.1.2: Perfect Palindromes: ζ ∈ PP ↔ ζ = inv(ζ)
- D 4.1.3: Imperfect Palindromes: ζ ∈ P - PP
- D 4.1.4: Aspect
- D 4.1.5: Left Partial Sentence: Z[:n]
- D 4.1.6: Right Partial Sentence: Z[n:]
- D 4.1.7: Pivots: ω(ζ)
- D 4.1.8: Even Palindromes: ζ ∈ P:sup:`+` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k )] 
- D 4.1.9: Odd Palindromes: ζ ∈ P:sup:`-` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k + 1) ]
- D 4.1.10: Parity
- D 4.1.11: Pivot Words
- D 5.1.1: Lefthand Sentence Integrals: Ω:sub:`-`(ζ,k) =  Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (l(ζ[:i])/l(ζ))
- D 5.1.2: Righthand Sentence Integrals: Ω:sub:`+`(ζ,k) =  Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (l(ζ[i:])/l(ζ))
- D 5.2.1: Delimiter Mass: μ:sub:`-`(ζ, i), μ:sub:`+`(ζ, i)
-
- D A.1.1: Compound Words: η ∈ CW:sub:`L` ↔ [(∃ α, β ∈ L: η = αβ)  ∨  (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ)] ∧ (η ∈ L)
- D A.1.2: Compound Invertible Words: η ∈ CIW:sub:`L`  ↔ [ (η ∈ CW:sub:`L`)  ∧ (η ∈ I) ]
- D A.2.1: σ-Pairing Language: α ∈ L:sub:`σ` ↔ ∃ ζ ∈ C:sub:`L`: α = (ζ ⋅ Σ:sub:`σ`)
- D A.2.2: Palindromic Pairing Language: α ∈ L:sub:`P` ↔  ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)
- D A.3.1: Category: C:sub:`L`(m)
- D A.3.2: Categorical Size: κ
- D A.4.1: σ-Induction: ς:sup:`-1`(ζ, m, T)
- D A.5.1: Reflective Structure:  s ∈ RS ↔ [∃ n ∈ ℕ, ∃ p ∈ Χ:sub:`L`(n): (s = Π:sub:`i=1`:sup:`n` p(i)) ∧ (ς(S) = inv(ς(s)))]

.. _algorithms:

Algorithms
----------

- A.1: Emptying Algorithm
- A.2: Delimiting Algorithm 
- A.3: Reduction Algorithm

.. _axioms:

Axioms 
------

- Character Axiom C.1: :math:`\forall ⲁ \in \Sigma: ⲁ \in S`
- Discover Axiom W.1: :math:`\forall \alpha \in L: [ (l(\alpha) \neq 0) \land (\forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma) ]`
- Duality Axiom S.1: :math:`( \forall \alpha \in L: \exists \zeta \in C_{L}: \alpha \subset_{s} \zeta ) \land ( \forall \zeta \in C_{L}: \exists \alpha \in L: \alpha \subset_{s} \zeta )`
- Extraction Axiom S.2: :math:`\forall \zeta \in C_{L} : \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in L`
.. _theorems:

Theorems
--------

- T 1.1.1: :math:`\forall u, t \in S : l(ut) = l(u) + l(t)`
- T 1.1.2: :math:`| S | \geq \aleph_{1}`
- T 1.1.3: :math:`\forall s \in S: \varepsilon \subset_{s} s`
- T 1.2.1: :math:`\forall \alpha \in L:  \alpha \varepsilon = \varepsilon \alpha = \alpha`
- T 1.2.2: :math:`\forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \subset_{s} \alpha`
- T 1.2.3: :math:`\forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon`
- T 1.2.4: :math:`\forall s \in S: \text{inv}(\text{inv}(s)) = s`
- T 1.2.5: :math:`\forall u, t \in S: \text{inv}(ut) = \text{inv}(t)\text{inv}(u)`
- T 1.2.6: :math:`\forall u, t \in S : u \subset_{s} t \leftrightarrow \text{inv}(u) \subset_{s} \text{inv}(t)`
- T 1.2.7: :math:`\forall t, u, v \in S : (t \subset_{s} u) \land (u \subset_{s} v) \rightarrow (t \subset_{s} v)`
- T 1.2.8: :math:`\forall n \in \mathbb{N}: \forall p \in \Chi_{L(n)}: \exists! s \in S: s = D\Pi_{i=1}^{n} p(i)`
- T 1.2.9: :math:`\forall n \in \mathbb{N}, \forall p \in \Chi_{L(n)} \exists! s \in S: s = L\Pi_{i=1}^{n} p(i)`
- T 1.3.1: :math:`\forall \alpha \in L: \alpha \in R \leftrightarrow \alpha = \text{inv}(\alpha)`
- T 1.3.2: :math:`\forall \alpha \in L: \alpha \in I \leftrightarrow \text{inv}(\alpha) \in I`
- T 1.3.3 :math:`R \subseteq I`
- T 1.3.4: If | R | is even, then | I | is even. If | R | is odd, then | I | is odd.
- T 2.1.1: :math:`\forall \zeta \in C_{L}:  \sum_{j=1}^{\Lambda(\zeta)} l(\zeta\{j\}) \geq \Lambda(\zeta)`
- T 2.1.2: :math:`\forall \zeta, \xi \in C_{L}: \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)`
- T 2.1.3: :math:`\forall \zeta \in C_{L}: \forall i, j \in \mathbb{N}_{\Lambda(\zeta)}: i \neq k \rightarrow \exists n \in \mathbb{N}_{l(\zeta)}: (i/n/j)_{\zeta}`
- T 2.2.1: :math:`\forall \zeta \in C_{L}: l(\zeta) \neq 0`
- T 2.2.2: :math:`\forall \zeta \in C_{L}: \forall i \in \mathbb{N}_{l(\zeta)}: \zeta[i] \subset_{s} \zeta`
- T 2.2.3: :math:`\forall \zeta \in C_{L} : \forall i \in \mathbb{N}_{l(\zeta)}:  \zeta[i] \neq \varepsilon`
- T 2.2.4: :math:`\forall \zeta \in C_{L}: \Lambda(\zeta) \geq 1`
- T 2.2.5: :math:`\forall \zeta \in C_{L}: \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`
- T 2.3.1: :math:`A(n) \subseteq C_{L}`
- T 2.3.2: :math:`\forall \zeta \in A(n): \Lambda(\zeta) = n`
- T 2.3.3: :math:`\forall \zeta \in C_{L}: \zeta \in A(\Lambda(\zeta))`
- T 2.3.4: :math:`\forall \zeta \in C_{L}: \exists p \in X_{L}(\Lambda(\zeta)): \zeta = D\Pi_{i=1}^{n} p(i)`
- T 2.3.5: :math:`\forall \zeta \in C_{L}: \zeta \in K \leftrightarrow \text{inv}(\zeta) \in K`
- T 2.3.6: :math:`\forall \zeta \in C_{L}: \text{inv}(\zeta) \in K \rightarrow \zeta \in C_{L}`
- T 2.3.7: :math:`\forall \zeta \in C_{L}: \forall i \in \mathbb{N}_{\Lambda(\zeta)}: \zeta \in K \rightarrow \text{inv}(\zeta)\{i\} \in L`
- T 2.3.8: :math:`\forall \zeta \in C_{L}: \text{inv}(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
- T 2.3.9: :math:`\forall \zeta \in C_{L}: \forall i \in \mathbb{N}_{\Lambda(\zeta)}: \zeta \in K \rightarrow \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
- T 2.3.10: :math:`\forall \zeta \in C_{L}: \zeta \in K \leftrightarrow (\forall i \in \mathbb{N}_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})) \land (\text{inv}(\zeta) \in A(\Lambda(\zeta)))`
- T 2.3.11: :math:`\forall \zeta \in C_{L}: \zeta \in K \rightarrow \forall i \in \mathbb{N}_{\Lambda(\zeta)}: \zeta\{i\} \in I`





- T 3.1.1: ∀ ζ ∈ C:sub:`L`: inv(ς(ζ)) = ς(inv(ζ))
- T 3.1.2: ∀ ζ, ξ ∈ C:sub:`L`: ς(ζξ) = (ς(ζ))(ς(ξ))
- T 3.1.3: ∀ ζ ∈ C:sub:`L`: ς(ς(ζ)) = ς(ζ)
- T 3.1.4: ∀ ζ ∈ C:sub:`L`: Λ(ς(ζ)) ≤ 1
- T 3.1.5: ∀ u, t ∈ S : u ⊂:sub:`s` t ↔ ς(u) ⊂:sub:`s` ς(t) 
- T 3.1.6: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` ς(ζ)
- T 3.1.7: ∀ ζ ∈ K: [ ς(ζ) = inv(inv(ς(ζ))) ]
- T 3.1.8: ∀ ζ ∈ C:sub:`L`: ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}
- T 3.1.9: ∀ n ∈ ℕ: ∀ p ∈ Χ:sub:`L(n)`: ς(DN:sub:`i=1`:sup:`n` p(i)) = LN:sub:`i=1`:sup:`n` p(i)
- T 3.1.10: ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ l(ς(ζ))
- T 3.2.1: ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1
- T 3.2.2: ∀ s ∈ S: Δ(s) = Δ(inv(s))
- T 3.2.3: ∀ ζ ∈ C:sub:`L`: Δ(ζ) = Δ(inv(ζ))
- T 3.2.4: ∀ α ∈ L: Δ(α) = 0
- T 3.2.5: ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})
- T 3.2.6: ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})
- T 3.2.7: ∀ ζ ∈ C:sub:`L`: l(ζ) ≥  Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})
- T 3.2.8: ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ)
- T 3.2.9: ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)
- T 3.2.10: ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)
- T 3.2.11: ∀ ζ ∈ C:sub:`L`: Δ(Ζ ⋅ Σ:sub:`σ`)= 0
- T 3.2.12: ∀ t ∈ S: l(ς(t)) + Δ(t) = l(t)
- T 3.2.13: ∀ ζ ∈ C:sub:`L`: l(ς(t)) + Λ(ζ) = l(ζ) + 1
- 
- T 3.2.1: PP ⊂ K
- T 3.2.2: ∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})
- T 3.2.3:∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I
- T 3.2.4: PP ⊂ P
- T 3.2.5: PP ∪ IP = P
- T 3.2.6: ∀ ζ ∈ C:sub:`L`:  ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ)[:i] = ζ[l(ζ) - i + 1:]
- T 3.2.7: ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i + 1 ) ∧ (l(ζ[:i+1]) = l(ζ[i+1:]))
- T 3.2.8: ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i) ∧ (l(ζ[:i]) + 1 = l(ζ[i:]))
- T 3.2.9: ∀ ζ ∈ C:sub:`L`: ∃ n ∈ N:sub:`l(ζ)`: ( l(ζ[:n]) = l(ζ[n:]) ) ∨ (l(ζ[:n]) + 1 = l(ζ[n:]))
- T 3.2.10: ∀ ζ ∈ C:sub:`L`: (∃ k ∈ ℕ : l(ζ) = 2k + 1) ↔ ω(ζ) = (l(ζ) + 1)/2
- T 3.2.11: ∀ ζ ∈ P:sup:`-`: ω(ζ) = (l(ζ) + 1)/2
- T 3.2.12: ∀ ζ ∈ C:sub:`L`: (∃ k ∈ ℕ : l(ζ) = 2k) ↔ ω(ζ) = l(ζ)/2
- T 3.2.13: ∀ ζ ∈ P:sup:`+`: ω(ζ) = l(ζ)/2
- T 3.2.14: ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = l(ζ[:ω(ζ)]) + l(ζ[ω(ζ):])
- T 3.2.15: ∀ ζ ∈ C:sub:`L`: ω(ς(ζ)) ≤ ω(ζ) 
- T 3.2.16: P:sup:`-` ∩ P:sup:`+` = ∅
- T 3.2.17: P:sup:`-` ∪ P:sup:`+` = P
- T 3.3.1: ∀ ζ ∈ P: [ (inv(ζ{1}) ⊂:sub:s ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:s ζ{1}) ] ∧ [ (ζ{1} ⊂:sub:s inv(ζ{Λ(ζ)})) ∨ (ζ{Λ(ζ)} ⊂:sub:s inv(ζ{1})) ]
- T 3.3.2: ∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( (inv(ζ{ω-}) ⊂:sub:`s` ζ{ω+}) ∨ (inv(ζ{ω+}) ⊂:sub:`s` ζ{ω-}))
- 
- T 5.2.1: ∀ ζ ∈ C:sub:`L`: ∀ k ∈ N:sub:`l(ζ)`: Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (l(ζ[:i])/l(ζ)) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (i/l(ζ))
- T 5.2.2: ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`l(ζ)`: Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (l(ζ[i:])/l(ζ)) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ))
- T 5.2.3: ∀ ζ ∈ C:sub:`L``: Σ:sub:`i=1`:sup:`ω(ζ)` μ:sub:`+`(ζ, i)  > Σ:sub:`i=ω(ζ)+1`:sup:`l(ζ)` μ:sub:`-`(ζ, i) ↔ Ω:sub:`+`(ζ,l(ζ)) > Ω:sub:`-`(ζ,l(ζ))
- T 5.2.4: ∀ ζ ∈ C:sub:`L`: ∀ k ∈ N:sub:`l(ζ)`: Ω:sub:`-`(ς(ζ),k) = Ω:sub:`+`(ς(ζ),k) = 0
- T 5.2.5: ∀ ζ ∈ PP: ∀ i ∈ N:sub:`l(ζ)`: Ω:sub:`-`(ζ,i) = Ω:sub:`+`(ζ,i)
- 
- T 5.4.1: ∀ ζ ∈ C:sub:`L`: ∀ k ∈ N:sub:`l(ζ)`: Ω:sub:`-`(inv(ζ), k) = Σ:sub:`i=1`:sup:`k` Δ(inv(ζ)[i]) * (i/l(ζ))
- T 5.4.2: ∀ ζ ∈ C:sub:`L`: ∀ k ∈ N:sub:`l(ζ)`: Ω:sub:`+`(inv(ζ), k) = Σ:sub:`i=1`:sup:`k` Δ(inv(ζ)[i]) * ((l(ζ) - i + 1)/l(ζ))
- 
- T A.1.1: ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L
- T A.2.1: ∀ α ∈ L: α ∈ L:sub:`σ` ↔ [ ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:s α ]
- T A.2.2: L:sub:`P` ⊂ L:sub:`σ`
- T A.2.3: ∀ α ∈ L:sub:`P`: α = inv(α)
- T A.2.4: L ∩ L:sub:`P` ⊆ R
- T A.2.5: L:sub:`P` ⊂ R:sub:`L_σ`
- T A.3.1: ∀ α ∈ L: ∃ i ∈ N:sub:`κ`: α ∈ C:sub:`L`(i) 