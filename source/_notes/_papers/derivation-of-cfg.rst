Derivation of Context Free Grammars
===================================

.. topic:: Outline

    I. Foundational Concepts: Strings & Concatenation

    Primitives

    - Character (ι)
    - Empty Character (ε)
    - Delimiter Character (σ)
    - String (s)

    Definitions

    - Definition 1.1.1: Concatenation
    - Definition 1.1.2: Character-level Set Representations
    - Definition 1.1.3: String Length (l)
    - Definition 1.1.4: String Equality

    Axioms

    - Axiom C.0: The Equality Axiom
    - Axiom C.1: The Character Axiom

    Theorems

    - Theorem 1.1.1: l(ut)=l(u)+l(t)

    II. Core String Operations & Their Properties

    Definitions

    - Definition 1.1.5: Character Index Notation
    - Definition 1.2.4: String Inversion (inv)
    - Definition 3.1.2: σ-Reduction (ς)

    Theorems

    - Theorem 1.2.5: inv(ut)=inv(t)inv(u)
    - Theorem 3.1.2: ς(ζξ)=(ς(ζ)ς(ξ))

    III. The Commutativity Principle

    Theorems:

    - Theorem 3.1.1: inv(ς(ζ))=ς(inv(ζ))

    IV. From Words to Admissible Sentences

    Axioms

    - Axiom W.1: The Discovery Axiom

    Definitions

    - Definition 1.2.1: Language (L)
    - Definition 1.2.2: Word (α)
    - Definition 2.1.2: Sentence (ζ)
    - Definition 2.1.3: Word-Level Set Representation (W_ζ)
    - Definition 2.1.4: Word Length (Λ)
    - Definition 1.2.5: Phrase (P_n): Defines an ordered sequence of words.
    - Definition 1.2.6: Lexicon (X_L(n)): Defines the set of all possible phrases of a given length.
    - Definition 1.2.7: Delimitation (DΠ): Defines the operation of joining words in a phrase with delimiters (σ) to form a string.
    - Definition 2.3.1: Admissible Sentences (A(n)): This definition can now be properly stated, as it depends directly on Lexicons and Delimitations.

    V. Definition of a Palindrome

    Definitions

    - Definition 4.1.1: Palindromes (P): The central definition, which states that a sentence is a palindrome if its σ-reduced form is equal to its own inverse (ζ∈P↔(ς(ζ)=inv(ς(ζ)))).

    VI. Final Theorem: The Recursive Structure

    Theorems

    - Theorem 6.1.1: ∀ζ:sub:`1`, ζ:sub:`2` ∈ P: (ζ:sub:`1`​)(ζ:sub:`2`)(ζ:sub:`1`) ∈  (Λ(ζ:sub:`1`) + Λ(ζ:sub:`2`) + Λ(ζ:sub:`1`))→ (ζ:sub:`1`​)(ζ:sub:`2`)(ζ:sub:`1`) ∈ P


