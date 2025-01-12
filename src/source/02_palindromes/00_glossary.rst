.. _glossary:

Glossary
========

.. _notation:

Notation 
--------

- Punctuation: ∎
- Logical Operations: :math:`\forall`, :math:`\exists`, :math:`\leftrightarrow`, :math:`\to`, :math:`\leftarrow`, :math:`\land`, :math:`\lor`
- Arithmetical Relations: :math:`\neq`, :math:`=`, :math:`\geq`, :math:`\leq`, +, -
- Sets: :math:`\emptyset`, :math:`\mathbb{N}`, :math:`N_i`
- Set Operations: :math:`\cup`, :math:`\cap`
- Set Relations: :math:`\in`, :math:`\notin`, :math:`\subset`, :math:`\subseteq`
- Strings: s, t, u
- Domain: S
- Alphabet: :math:`\Sigma`
- Characters: :math:`\mathfrak{a}`, :math:`\mathfrak{b}`, :math:`\mathfrak{c}`, ... , :math:`\sigma`, :math:`\varepsilon`
- Character Variables: :math:`\iota`, :math:`\nu`, :math:`\omicron`, :math:`\rho`
- Language: L
- Words: a, b, c
- Word Variables: :math:`\alpha`, :math:`\beta`, :math:`\gamma`
- Character Index Notation: t[i]
- Word Classes: R, I
- Phrases of Word Length n: :math:`P_n`
- Lexicons: :math:`X_L (n)`
- Phrases Variables: p, q, r
- Sentences: ᚠ, ᚢ, ᚦ
- Sentence Variables: :math:`\zeta`, :math:`\xi`
- Word Index Notation: :math:`\zeta\{i\}`
- Partial Sentence: :math:`\zeta[:i]`, :math:`\zeta[i:]`
- Pivots: :math:`\Phi(\zeta)`
- Pivot Words: :math:`\zeta\{\Phi-\}`, :math:`\zeta\{\Phi+\}`
- Sentence Classes: :math:`A(n)`, K, P, PP, IP, :math:`P^-`, :math:`P^+`
- Categories: :math:`C_L(m)`
- Relations: :math:`\subset_s`, :math:`(i/n/j)_{\zeta}`
- Functions: l(t), :math:`\Lambda(t)`, :math:`\Delta(t)`
- Operations: inv(s), :math:`\varsigma(\zeta)`, :math:`D\Pi_{i=1}^{n} p(i)`, :math:`L\Pi_{i=1}^{n} p(i)`

.. _definitions:

Definitions 
-----------

- D 1.1.1: Concatenation: ut
- D 1.1.2: Character-Level Set Representation: **T**
- D 1.1.3: String Length: l(t)
- D 1.1.4: String Equality: :math:`u = t`
- D 1.1.5: Character Index Notation: t[i]
- D 1.1.6: Consecutive Functions: f(i)
- D 1.1.7: Containment: :math:`t \subset_{s} u`
- D 1.2.1: Language: L
- D 1.2.2: Word: :math:`\alpha`
- D 1.2.3: Word Equality: :math:`\alpha = \beta`
- D 1.2.4: String Inversion: inv(s)
- D 1.2.5: Phrase: :math:`P_n = (\alpha_1, \alpha_2, ..., \alpha_n) = (P_n(1), )`
- D 1.2.6: Lexicon: :math:`\mathrm{X}_L(n) = \{ P_n | P_n = (\alpha_1, \alpha_2, ..., \alpha_n) \land \forall i \in \mathbb{N}_n: \alpha_i \in L \}`
- D 1.2.7: Delimitation: :math:`D\Pi_{i=1}^{n} p(i)`
- D 1.2.8: Limitation: :math:`L\Pi_{i=1}^{n} p(i)`
- D 1.3.1: Reflective Words: :math:`\alpha \in R \leftrightarrow \forall i \in \mathbb{N}_{l(\alpha)}: \alpha[i] = \alpha[l(\alpha) - i + 1]`
- D 1.3.2: Invertible Words: :math:`\alpha \in I \leftrightarrow \text{inv}(\alpha) \in L`
- D 2.1.1: Corpus: :math:`C_L`
- D 2.1.2: Sentence: ᚠ
- D 2.1.3: Word-Level Set Representation: :math:`W_{ᚠ}`
- D 2.1.4: Word Length: :math:`\Lambda(\zeta)`
- D 2.1.5: Word Index Notation: :math:`\zeta\{i\}`
- D 2.1.6: Intervention: :math:`(i/n/j)_\zeta`
- D 2.2.1: Semantic Coherence
- D 2.3.1: Admissible Sentences: :math:`t \in A(n) \leftrightarrow (\exists p \in \mathrm{X}_L(n): t = \Pi_{i=1}^{n} p(i)) \land (t \in C_L)`
- D 2.3.2: Invertible Sentences: :math:`\zeta \in K \leftrightarrow \text{inv}(\zeta) \in C_L`
- D 3.1.1: :math:`\sigma`-Reduced Alphabet: :math:`\Sigma_\sigma`
- D 3.1.2: :math:`\sigma`-Reduction: :math:`\varsigma(\zeta)`
- D 3.2.1: Delimiter Count Function: :math:`\Delta(t) = | D_t |`
- D 4.1.1: Palindromes: :math:`\zeta \in P \leftrightarrow (\varsigma(\zeta) = \text{inv}(\varsigma(\zeta)))`
- D 4.1.2: Perfect Palindromes: :math:`\zeta \in PP \leftrightarrow \zeta = \text{inv}(\zeta)`
- D 4.1.3: Imperfect Palindromes: :math:`\zeta \in P - PP`
- D 4.1.4: Aspect
- D 4.2.1: Left Partial Sentence: :math:`Z[:n]`
- D 4.2.2: Right Partial Sentence: :math:`Z[n:]`
- D 4.2.3: Pivots: :math:`\Phi(\zeta)`
- D 4.2.4: Even Palindromes: :math:`\zeta \in P_{+} \leftrightarrow [ (\zeta \in P) \land (\exists k \in \mathbb{N} : l(\zeta) = 2k )]`
- D 4.2.5: Odd Palindromes: :math:`\zeta \in P_{-} \leftrightarrow [ (\zeta \in P) \land (\exists k \in \mathbb{N} : l(\zeta) = 2k + 1) ]`
- D 4.2.6: Parity
- D 4.2.7: Pivot Words
- D 5.1.1: Lefthand Sentence Integrals: :math:`\Phi_{-}(\zeta,k) =  \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (l(\zeta[:i])/l(\zeta))`
- D 5.1.2: Righthand Sentence Integrals: :math:`\Phi_{+}(\zeta,k) =  \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (l(\zeta[i:])/l(\zeta))`
- D 5.2.1: Delimiter Mass: :math:`\mu_{-}(\zeta, i), \mu_{+}(\zeta, i)`
- D A.1.1: Compound Words: :math:`\eta \in CW_L \leftrightarrow [(\exists \alpha, \beta \in L: \eta = \alpha\beta) \lor (\exists \alpha \in L, \exists \gamma \in CW_L: \eta = \alpha\gamma)] \land (\eta \in L)`
- D A.1.2: Compound Invertible Words: :math:`\eta \in CIW_L \leftrightarrow [ (\eta \in CW_L) \land (\eta \in I) ]`
- D A.2.1: :math:`\sigma`-Pairing Language: :math:`\alpha \in L_\sigma \leftrightarrow \exists \zeta \in C_L: \alpha = \varsigma(\zeta)`
- D A.2.2: Palindromic Pairing Language: :math:`\alpha \in L_P \leftrightarrow \exists \zeta \in P: \alpha = (\varsigma(\zeta))`
- D A.3.1: Category: :math:`C_L(m)`
- D A.3.2: Categorical Size: :math:`\kappa`
- D A.4.1: :math:`\sigma`-Induction: :math:`\varsigma^{-1}(\zeta, m, T)`
- D A.5.1: Reflective Structure: :math:`s \in RS \leftrightarrow [\exists n \in \mathbb{N}, \exists p \in \mathrm{X}_L(n): (s = \Pi_{i=1}^{n} p(i)) \land (\varsigma(S) = \text{inv}(\varsigma(s)))]`

.. _algorithms:

Algorithms
----------

- A.1: Emptying Algorithm
- A.2: Delimiting Algorithm 
- A.3: Reduction Algorithm

.. _axioms:

Axioms 
------

- Character Axiom C.1: :math:`\forall \iota \in \Sigma: \iota \in S`
- Discover Axiom W.1: :math:`\forall \alpha \in L: [ (l(\alpha) \neq 0) \land (\forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma) ]`
- Duality Axiom S.1: :math:`( \forall \alpha \in L: \exists \zeta \in C_{L}: \alpha \subset_{s} \zeta ) \land ( \forall \zeta \in C_{L}: \exists \alpha \in L: \alpha \subset_{s} \zeta )`
- Extraction Axiom S.2: :math:`\forall \zeta \in C_{L} : \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in L`
- Finite Axiom S.3: :math:`\exists N \in \mathbb{N}: \forall \zeta \in C_L, l(\zeta) \leq N`

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
- T 1.2.7: :math:`\forall t, u, v \in S : (t \subset_{s} u) \land (u \subset_{s} v) \to (t \subset_{s} v)`
- T 1.2.8: :math:`\forall n \in \mathbb{N}: \forall p \in X_L(n): \exists! s \in S: s = D\Pi_{i=1}^{n} p(i)`
- T 1.2.9: :math:`\forall n \in \mathbb{N}: \forall p \in X_L(n): \exists! s \in S: s = L\Pi_{i=1}^{n} p(i)`
- T 1.3.1: :math:`\forall \alpha \in L: \alpha \in R \leftrightarrow \alpha = \text{inv}(\alpha)`
- T 1.3.2: :math:`\forall \alpha \in L: \alpha \in I \leftrightarrow \text{inv}(\alpha) \in I`
- T 1.3.3 :math:`R \subseteq I`
- T 1.3.4: If | R | is even, then | I | is even. If | R | is odd, then | I | is odd.
- T 2.1.1: :math:`\forall \zeta \in C_L:  \sum_{j=1}^{\Lambda(\zeta)} l(\zeta\{j\}) \geq \Lambda(\zeta)`
- T 2.1.2: :math:`\forall \zeta, \xi \in C_L: \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)`
- T 2.1.3: :math:`\forall \zeta \in C_L: \forall i, j \in N_{\Lambda(\zeta)}: i \neq k \to \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta}`
- T 2.2.1: :math:`\forall \zeta \in C_L: l(\zeta) \neq 0`
- T 2.2.2: :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \zeta[i] \subset_s \zeta`
- T 2.2.3: :math:`\forall \zeta \in C_L : \forall i \in N_{l(\zeta)}:  \zeta[i] \neq \varepsilon`
- T 2.2.4: :math:`\forall \zeta \in C_L: \Lambda(\zeta) \geq 1`
- T 2.2.5: :math:`\forall \zeta \in C_L: \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`
- T 2.3.1: :math:`A(n) \subseteq C_{L}`
- T 2.3.2: :math:`\forall \zeta \in A(n): \Lambda(\zeta) = n`
- T 2.3.3: :math:`\forall \zeta \in C_L: \zeta \in A(\Lambda(\zeta))`
- T 2.3.4: :math:`\forall \zeta \in C_L: \exists p \in X_L(\Lambda(\zeta)): \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} p(i)`
- T 2.3.5: :math:`\forall \zeta \in C_L: \zeta \in K \leftrightarrow \text{inv}(\zeta) \in K`
- T 2.3.6: :math:`\forall \zeta \in C_L: \text{inv}(\zeta) \in K \to \zeta \in C_L`
- T 2.3.7: :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} \in L`
- T 2.3.8: :math:`\forall \zeta \in C_L: \text{inv}(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
- T 2.3.9: :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
- T 2.3.10: :math:`\forall \zeta \in C_L: \zeta \in K \leftrightarrow (\forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})) \land (\text{inv}(\zeta) \in A(\Lambda(\zeta)))`
- T 2.3.11: :math:`\forall \zeta \in C_L: \zeta \in K \to \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I`
- T 3.1.1: :math:`\forall \zeta \in C_L: \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta))`
- T 3.1.2: :math:`\forall \zeta, \xi \in C_L: \varsigma(\zeta\xi) = (\varsigma(\zeta))(\varsigma(\xi))`
- T 3.1.3: :math:`\forall \zeta \in C_L: \varsigma(\varsigma(\zeta)) = \varsigma(\zeta)`
- T 3.1.4: :math:`\forall \zeta \in C_L: \Lambda(\varsigma(\zeta)) \leq 1`
- T 3.1.5: :math:`\forall u, t \in S : u \subset_s t \leftrightarrow \varsigma(u) \subset_s \varsigma(t)`
- T 3.1.6: :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \subset_s \varsigma(\zeta)`
- T 3.1.7: :math:`\forall \zeta \in K: [ \varsigma(\zeta) = \text{inv}(\text{inv}(\varsigma(\zeta))) ]`
- T 3.1.8: :math:`\forall \zeta \in C_L: \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`
- T 3.1.9: :math:`\forall n \in \mathbb{N}: \forall p \in \mathrm{X}_{L(n)}: \varsigma(D\Pi_{i=1}^{n} p(i)) = L\Pi_{i=1}^{n} p(i)`
- T 3.1.10: :math:`\forall \zeta \in C_L: l(\zeta) \geq l(\varsigma(\zeta))`
- T 3.2.1: :math:`\forall \zeta \in C_L: \Lambda(\zeta) = \Delta(\zeta) + 1`
- T 3.2.2: :math:`\forall s \in S: \Delta(s) = \Delta(\text{inv}(s))`
- T 3.2.3: :math:`\forall \zeta \in C_L: \Delta(\zeta) = \Delta(\text{inv}(\zeta))`
- T 3.2.4: :math:`\forall \alpha \in L: \Delta(\alpha) = 0`
- T 3.2.5: :math:`\forall \zeta \in C_L: l(\zeta) = \Delta(\zeta) + \sum_{i = 1}^{\Lambda(\zeta)} l(\zeta\{i\})`
- T 3.2.6: :math:`\forall \zeta \in C_L: l(\zeta) + 1 = \Lambda(\zeta) + \sum_{i = 1}^{\Lambda(\zeta)} l(\zeta\{i\})`
- T 3.2.7: :math:`\forall \zeta \in C_L: l(\zeta) \geq \sum_{i = 1}^{\Lambda(\zeta)} l(\zeta\{i\})`
- T 3.2.8: :math:`\forall \zeta \in C_L: l(\zeta) \geq \Lambda(\zeta)`
- T 3.2.9: :math:`\forall u, t \in S: \Delta(ut) = \Delta(u) + \Delta(t)`
- T 3.2.10: :math:`\forall u, t \in S: \Delta(\text{inv}(ut)) = \Delta(u) + \Delta(t)`
- T 3.2.11: :math:`\forall \zeta \in C_L: \Delta(\varsigma(\zeta))= 0`
- T 3.2.12: :math:`\forall t \in S: l(\varsigma(t)) + \Delta(t) = l(t)`
- T 3.2.13: :math:`\forall \zeta \in C_L: l(\varsigma(t)) + \Lambda(\zeta) = l(\zeta) + 1`
- T 4.1.1: :math:`PP \subset K`
- T 4.1.2: :math:`\forall \zeta \in PP: \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
- T 4.1.3: :math:`\forall \zeta \in PP: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I`
- T 4.1.4: :math:`PP \subset P`
- T 4.1.5: :math:`PP \cup IP = P`
- T 4.2.1: :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \text{inv}(\zeta)[:i] = \zeta[l(\zeta) - i + 1:]`
- T 4.2.2: :math:`\forall \zeta \in C_L: \exists i \in N: (l(\zeta) = 2i + 1 ) \land (l(\zeta[:i+1]) = l(\zeta[i+1:]))`
- T 4.2.3: :math:`\forall \zeta \in C_L: \exists i \in N: (l(\zeta) = 2i) \land (l(\zeta[:i]) + 1 = l(\zeta[i:]))`
- T 4.2.4: :math:`\forall \zeta \in C_L: \exists n \in N_{l(\zeta)}: ( l(\zeta[:n]) = l(\zeta[n:]) ) \lor (l(\zeta[:n]) + 1 = l(\zeta[n:]))`
- T 4.2.5: :math:`\forall \zeta \in C_L: (\exists k \in N : l(\zeta) = 2k + 1) \leftrightarrow \Phi(\zeta) = \frac{l(\zeta) + 1}{2}`
- T 4.2.6: :math:`\forall \zeta \in P_{-}: \Phi(\zeta) = \frac{l(\zeta) + 1}{2}`
- T 4.2.7: :math:`\forall \zeta \in C_L: (\exists k \in \mathbb{N} : l(\zeta) = 2k) \leftrightarrow \Phi(\zeta) = \frac{l(\zeta)}{2}`
- T 4.2.8: :math:`\forall \zeta \in P_{+}: \Phi(\zeta) = \frac{l(\zeta)}{2}`
- T 4.2.9: :math:`\forall \zeta \in C_L: l(\zeta) + 1 = l(\zeta[:\Phi(\zeta)]) + l(\zeta[\Phi(\zeta):])`
- T 4.2.10: :math:`\forall \zeta \in C_L: \Phi(\varsigma(\zeta)) \leq \Phi(\zeta)`
- T 4.2.11: :math:`\forall \zeta in C_L: \zeta[\Phi(\zeta)] \neq \text{inv}(\zeta)[\Phi(\zeta)]) \to (\exists k \in \mathbb{N}: l(\zeta) = 2k)`
- T 4.2.12: :math:`\forall \zeta \in C_L: (\exists k \in \mathbb{N}: l(\zeta)=2k) \to \text{inv}(\zeta)[\Phi(\zeta)] = \zeta[\Phi(\zeta)+1]`
- T 4.2.13: :math:`P_{-} \cap P^+ = \emptyset`
- T 4.2.14: :math:`P_{-} \cup P^+ = P`
- T 4.3.1: :math:`\forall \zeta \in P: [ (\text{inv}(\zeta\{1\}) \subset_s \zeta\{\Lambda(\zeta)\}) \vee (\text{inv}(\zeta\{\Lambda(\zeta)\}) \subset_s \zeta\{1\}) ] \land [ (\zeta\{1\} \subset_s \text{inv}(\zeta\{\Lambda(\zeta)\})) \vee (\zeta\{\Lambda(\zeta)\} \subset_s \text{inv}(\zeta\{1\})) ]`
- T 4.3.2: :math:`\forall \zeta \in P: (\zeta[\Phi(\zeta)] = \sigma) \to ( (\text{inv}(\zeta\{\Phi-\}) \subset_s \zeta\{\Phi+\}) \vee (\text{inv}(\zeta\{\Phi+\}) \subset_s \zeta\{\Phi-\}))`
- T 5.1.1: :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (l(\zeta[:i])/l(\zeta)) = \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (i/l(\zeta))`
- T 5.1.2: :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (l(\zeta[i:])/l(\zeta)) = \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot ((l(\zeta) - i + 1)/l(\zeta))`
- T 5.1.3: :math:`\forall \zeta \in C_L: \Sigma_{i=1}^{\Phi(\zeta)} \mu_{+}(\zeta, i) > \Sigma_{i=\Phi(\zeta)+1}^{l(\zeta)} \mu_{-}(\zeta, i) \leftrightarrow \Phi_{+}(\zeta,l(\zeta)) > \Phi_{-}(\zeta,l(\zeta))`
- T 5.2.1: :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\zeta, k) \geq 0 \land \Phi_{+}(\zeta,) \geq 0`
- T 5.2.2: :math:`\forall \zeta in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\varsigma(\zeta), k) = \Phi_{+}(\varsigma(\zeta), k) = 0`
- T 5.2.3: :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\text{inv}(\zeta), k) = \Sigma_{i=1}^{k} \Delta(\text{inv}(\zeta)[i]) \cdot (i/l(\zeta))`
- T 5.2.4: :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{+}(\text{inv}(\zeta), k) = \Sigma_{i=1}^{k} \Delta(\text{inv}(\zeta)[i]) \cdot ((l(\zeta) - i + 1)/l(\zeta))`
- T 5.2.5: :math:``
- T 5.2.6; :math:`\forall \zeta \in PP: \forall i \in N_{l(\zeta)}: \Phi_{-}(\zeta,i) = \Phi_{+}(\zeta,i)`
- T A.1.1: :math:`\forall \zeta \in C_L: L_\zeta \subset L`
- T A.2.1: :math:`\forall \alpha \in L: \alpha \in L_\sigma \leftrightarrow [ \exists \zeta \in C_L: \exists i \in N_{\Lambda(\zeta)}: \zeta\{i\} \subset_s \alpha ]`
- T A.2.2: :math:`L_P \subset L_\sigma`
- T A.2.3: :math:`\forall \alpha \in L_P: \alpha = \text{inv}(\alpha)`
- T A.2.4: :math:`L \cap L_P \subseteq R`
- T A.2.5: :math:`L_P \subset R_{L_\sigma}`
- T A.3.1: :math:`\forall \alpha \in L: \exists i \in N_\kappa: \alpha \in C_L(i)`