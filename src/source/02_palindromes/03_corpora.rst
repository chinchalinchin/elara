
Section II: Corpora
===================

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

Section III: Delimiters
=======================

.. note::

    It is the author's opinion there is a type of *algebraic structure* embedded in Language through the constraints of syntax. This section highlights one of the functions defined within this structure. While the function is not required to prove the main results of this work about Palindromes, it is an interesting function in its own right.

Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a Palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a Palindrome is distributed through its syntactical layers. The concepts of *Perfect* and *Imperfect* Palindromes are be defined more rigorously in Section III, but as an intuitive introduction to the ability of a Palindrome to encode meaning on multiple syntactic levels and as a justification for the introduction of the Delimiter Count Function, consider the following two examples,

    1. dennis sinned
    2. if i had a hifi

The first palindrome "*dennis sinned*" is what will be termed a *Perfect* Palindrome, because its inverse does not require a rearrangement of its constituent Characters to preserve its semantic content. However, the second Palindrome *"if i had a hifi"* is what is termed an *Imperfect* Palindrome. To see the motivation behind this categorization, note the strict inversion of "If I had a hifi" would be (ignoring capitalization for now),

    ifih a dah i fi

The order of the Characters in the Inverse of an Imperfect Palindrome is preserved, but in order to reconstitute its uninverted form, the Delimter Characters must be re-sorted. It appears, then, that Delimiters play a central role in organizing the palindromic structure. 

The study of Delimiter Characters in a Sentence bears study beyond its application to palindromic structures, though. The following section of the Appendix introduces this function for quantifying the number of Delimiters in a sentence. Various properties about this function are then proved, in particular how the function interacts with other linguistic operations and functions that have been defined in the main body of the work. 

Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.

**Definition A.2.1: Delimiter Count Function** Let *t* be a String with length *l(t)*. Let **T** be the Character-level representation of *t* with the Characters *𝔞*:sub:`i` denoting the *i*:sup:`th` character of the String *t*, where *1 ≤ i ≤ l(t)*,

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

The Delimiter Count Function, denoted by *Δ(t)*, is defined as the number of Delimiter Characters (*σ*) in the string *t*. Formally, *Δ(t)* is defined as the cardinality of the set that satisfies the following formula:

    D:sub:`t` ↔ { (i, ⲁ) ∈ T | ⲁ = σ, 1 ≤ i ≤ l(t) } 

Then, the delimiter count function is defined as

    Δ(t) = | D:sub:`t` | ∎

**Example** 

Consider the string *t = "a b c"*. The Character-level set representation of *t* is given by,
    
    T = { (1, "a"), (2, σ), (3, "b"), (4, σ), (5, "c") }.

By Definition A.2.1, The set **D**:sub:`t` contains the ordered pairs *(2, σ)* and *(4, σ)*, where the first coordinate of each pair correspond the positions of the two Delimiter Characters in the String. Therefore, 
    
    D:sub:`t`= { (2, σ), (4, σ) }

From this it follows, 

    | D:sub:`t` | = 2 
    
Hence, 
    
    Δ(t) = 2 ∎

From the previous example, it can be seen the Delimiter Count function takes a Sentence as input and produces a non-negative integer (the Delimiter count) as output. Multiple sentences can have the same Delimiter count, making it a many-to-one function. While this many not be advantageous from a computational perspective, the Delimiter Count function has other interesting properties that make it worth studying. The following theorems describe some of its properties.

**Theorem A.2.1** ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1

.. note::

    I think this needs revised to be *Λ(ζ) ≥ Δ(ζ) + 1* to account for edge cases where the sentence has multiple Delimiters in sequence, or has a Delimiter at the end or beginning of the String. 
    
    Alternatively, this inconsistency might be resolvable by introducing an assumption about the structure of a Sentence. Perhaps all Delimiters between two consecutive Words should be treated as a single Delimiter? Or an Axiom to constrain the placement of Delimiters in Sentences?

In natural language, this theorem is stated: For any sentence *ζ* in a Corpus C:sub:`L`, the length of the Sentence is equal to its Delimiter count plus one.

Assume *ζ ∈* **C**:sub:`L`. Let *Δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the Character-level representation of ζ. Let **W**:sub:`ζ` be the word-level set representation of ζ. Recall **W**:sub:`ζ` is formed by splitting **Ζ** at each Delimiter Character *σ* with the Delimiting Algorithm in Definition 2.1.3.

Each word in **W**:sub:`ζ` corresponds to a contiguous subsequence of non-Empty, non-Delimiter Characters in **Ζ**.

Since Delimiters separate Words, and each Delimiter corresponds to one Word boundary, the number of Words in the Sentence is always one more than the number of delimiters. Therefore, the cardinality of **W**:sub:`ζ` (the number of words) is equal to the Delimiter count of *Δ(ζ)* plus one,

    | W:sub:`ζ` | = Λ(ζ) = Δ(ζ) + 1. ∎

The next two theorems establish the invariance of the Delimiter count under String Inversion for any String, and by extension, any Sentence.

**Theorem A.2.2** ∀ s ∈ S: Δ(s) = Δ(inv(s))

Let *t* be a string with length *l(t)*. Let *u = inv(t)*. By Definition 1.2.4,

    1. l(t) = l(u)
    2. ∀ i ∈ N:sub:`l(t)`: u[i] = t[l(t) - i + 1]

Let **D**:sub:`t` be the set of ordered pairs representing the positions of the Delimiter *σ* in *t*, and let **D**:sub:`u` be the corresponding set for *u*. Assume *(j, σ) ∈*  **D**:sub:`u`, then, by step 2,

    3. u[j] = t[l(t) - j  + 1]

This means that the Character at position *j* in the inverse string *t* is the Delimiter *σ*. Therefore, 

    4. (l(t) - j  + 1, σ) ∈* **D**:sub:`t`

Thus, it is shown that for every element *(j, σ) ∈*  **D**:sub:`u`, there exists a corresponding element *(i, σ) ∈* **D**:sub:`t`, where *i = l(t) - j + 1*. 

To make the mapping more explicit, define a function *f*: **D**:sub:`t` *→* **D**:sub:`u` as follows. For any (*i*, *σ*) ∈ **D**:sub:`t`, let 

    5. f((i, σ)) = (l(t) - i + 1, σ)
    
It will be shown that *f* is a bijection.

**Well Defined** If (*i*, *σ*) ∈ **D**:sub:`t`, then the Character at position *i* in *t* is *σ*. By step 2, the Character at position *l(t) - i + 1* in *u = inv(t)* is also *σ*. Therefore, 

    6. (l(t) - i + 1, σ) ∈ D:sub:`u`
    
In other words, *f* maps elements of **D**:sub:`t` to elements of **D**:sub:`u`. Thus, *f* is well defined.
 
**Injective** Suppose 

    7. f((i:sub:`1`, σ)) = f((i:sub:`2`, σ)). 
    
Then, it follows,

    8. (l(t) - i:sub:`1` + 1, σ) = (l(t) - i:sub:`2` + 1, σ). 
    
This in turn implies, 

    9. l(t) - i:sub:`1` + 1 = l(t) - i:sub:`2` + 1, 
    
So 
    10. i:sub:`1` = i:sub:`2`
    
Thus, 

    11. (i:sub:`1`, σ) = (i:sub:`2`, σ)
    
In other words, *f* is injective. 

**Surjective** Let *(j, σ)* be an arbitrary element of **D**:sub:`u`. Then the Character at position *j* in *u* is *σ*. Let 

    12. i = l(t) - j + 1. 
    
Then 

    13. j = l(t) - i + 1. 
    
By step 3, the Character at position *i* in *t* is also *σ*. So, 

    14. (i, σ) ∈ D:sub:t
    
And,

    15. f((i, σ)) = (l(t) - i + 1, σ) = (j, σ). 
    
Thus, *f* is surjective. 

This defines a bijective mapping between the elements of **D**:sub:`u` and **D**:sub:`t`. Since there's a one-to-one mapping between the elements of *D**:sub:`u` and **D**:sub:`t`, their cardinalities must be equal,

    16. | D:sub:`u` | = | D:sub:`s` |

By the definition of the delimiter count function, this means *Δ(u) = Δ(t)*. Since *u = inv(t)*, it has been shown *Δ(inv(s)) = Δ(s)*. 

Furthmore, an exact relationship has been estalished between the coordinates of Delimiters in Strings and their Inverses, 

    17. D:sub:`inv(t)` = { (l(t) - i + 1, σ) | (i, σ) ∈ D:sub:`t` } ∎

**Theorem A.2.3** ∀ ζ ∈ C:sub:`L`: Δ(ζ) = Δ(inv(ζ))

Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L`,

    1. ζ ∈ C:sub:`L`

By Definition 2.1.2, every Sentence is a String. Therefore, *ζ* is a String. By Theorem A.3.2, 

    1. Δ(ζ) = Δ(inv(ζ))

Which is what was to be shown. ∎

**Theorem A.2.4** ∀ α ∈ L: Δ(α) = 0

This theorem can be stated in natural language as follows: The Delimtier Count of any Word in a Language is zero.

Assume *α* is a Word in Language **L**,

    1. α ∈ L
    
By the Discovery Axiom W.1, all Words in Language do not have Delimiters,

    2. ∀ i ∈ N:sub:`l(s)`: α[i] ≠ σ

Therefore, *α* does not have any Delimiter Characters (*σ*). By Definition 2.4.1, *Δ(s)* counts the number of Delimiter Characters (*σ*) in a String *s*. Since *α* hasno Delimiter Characters, the Delimiter Count of *α* must be 0. Therefore,

    3. Δ(α) = 0 ∎

**Theorem A.2.5** ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

In natural language, this theorem can be stated as follows: For every Sentence in a Corpus, the String Length of the Sentence is equal to the Delimiter Count of the sentence plus the sum of the String Lengths of its Words.

Assume 

    1. ζ ∈ C:sub:`L`. 

Either each *ζ{i}* for *1 ≤ i ≤ l(ζ)* is Delimiter or it is a non-Delimiter, with no overlap. By Definition A.2.1, the number of Delimiter Characters in *ζ* is *Δ(ζ)*. 

By the Discovery Axiom W.1, words in **L** do not contain Delimiters. By Definition 2.1.3, the Words in **W**:sub:`ζ` are obtained by splitting *ζ*  at the Delimiters. Therefore, the total number of non-Delimiter characters in *ζ* is the sum of the Word Lengths l(ζ{i}) which is 

    2. Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Since every Character in *ζ* is either a Delimiter or part of a Word (and not both), the total number of Characters in *ζ* is the sum of the number of Delimiters and the number of Characters in Words. By Definition 1.1.3 of String Length, the total number of non-Empty characters in ζ is *l(ζ)*. Therefore, the number of non-Empty Characters in *ζ* is equal to the number of Delimiters plus the sum of its Word Lengths,

    3. ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ∎

**Theorem A.2.6** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Applying the results of Theorem A.2.1 and Theorem A.2.5, this theorem follows from simple algebraic manipulation. ∎

**Theorem A.2.7** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥  Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})

This theorem can be stated in natural language as follows: For any Sentence in the Corpus, its String Length is greater than or equal to the sum of the String Length of its Words. 

Assume *ζ ∈* **C**:sub:`L`. By Theorem A.2.4,
    
    1. Λ(ζ) ≥ 1

From Theorem A.2.6,

    2. l(ζ) + 1 - Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i}) = Λ(ζ)

Combining step 1 and step 2, the theorem is obtained through algebraic manipulation,

    l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α) ∎

**Theorem A.2.8** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ)

This theorem can be stated in natural language as follows: For any Sentence in a Corpus, its String Length is always greater than or equal to its Word Length.

Let *ζ* be an arbitrary Sentence in C:sub:`L`. Let **W**:sub:`ζ`` be the Word-level representation of *ζ*. By Definition 2.1.4, 

    1. Λ(ζ) = | W:sub:`ζ` |

By Theorem 1.2.3, each Word in **W**:sub:`ζ` consists of one or more non-Empty Characters. By Theorem 2.2.5, every Sentence is a Delimitation of its Words,

    2. ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

Where the operation of Delimitation inserts Delimiters between the Words of *ζ*. On the other hand, let *t* be the the Limitation of *ζ*,

    3. t = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

By Definition 1.2.7, Definition 1.2.8 and Definition 1.1.3 of String Length,

    4. l(DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) = l(ζ) ≥ l(t) = l(LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i})

By Definition 1.28,

    5. LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i} = (ζ{1})(ζ{2}) .... (ζ{Λ(ζ)-1})(ζ{Λ(ζ)})

By Theorem 1.1.1, 

    6. l((ζ{1})(ζ{2}) .... (ζ{Λ(ζ)-1})(ζ{Λ(ζ)})) = Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})

Therefore, combining steps 4 and 6

    7. l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Consider the summation,

    8. Σ:sub:`i = 1`:sup:`Λ(ζ)` 1

Clearly, since *l(ζ{i}) ≥ 1* for all *i*, it follows, 

    9. Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` 1

By the definition of summations, step 8 can be rewritten as,

    10. Σ:sub:`i = 1`:sup:`Λ(ζ)` 1 = 1 + 1 + 1 + .... + 1 = Λ(ζ)

Combining step 7, step 9 and  step 10,

    11. l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` 1 = Λ(ζ)

Since ζ was arbitrary, this can be generalized as,

    12. ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ) ∎

**Theorem A.2.9 (Informal)** ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

Let *u* and *t* be arbitrary strings in S. Let **U** and **T** be the Character-level representations of *u* and *t*, respectively:

    1. U = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(u)`)

    2. T = (𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)`)

The Character-level representation of *ut* is:

    3. UT = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(u)`, 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)``)

By Definition A.2.1, *Δ(u)* is the number of Delimiters in *u*, *Δ(t)* is the number of Delimiters in *t*, and *Δ(ut)* is the number of Delimiters in *ut*.

Since concatenation simply joins two Strings without adding or removing Characters, with the possible exception of Empty Characters through the Basis Clause of Definition 1.1.1, the number of Delimiters in *ut* is the sum of the number of Delimiters in *u* and the number of Delimiters in *t*. ∎

**Theorem A.2.9 (Formal)** ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

Let **D**:sub:`u` be the set of indices of Delimiters in *u*. Let **D**:sub:`t` be the set of indices of Delimiters in *t*. Let **D**:sub:`ut` be the set of indices of delimiters in *ut*,

    1. D:sub:`u` = { i | 1 ≤ i ≤ l(u) and u[i] = σ }
    2. D:sub:`t` = { j | 1 ≤ j ≤ l(t) and t[j] = σ }
    3. D:sub:`ut` = { k | (1 ≤ k ≤ l(u) + l(t)) ∧ ((k ≤ l(u) ∧ UT[k] = σ) ∨ (k > l(u) ∧ UT[k] = σ)) }
   
It is clear that D:sub:`ut` is the union of two disjoint sets, since the indices of the Delimiters in *t* have been shifted by *l(u)*. Therefore,

    | D:sub:`ut` | = | D:sub:`u` | + | D:sub:`t` |.

By Definition A.4.1, this is equivalent to,

    Δ(ut) = Δ(u) + Δ(t)

Since u and t were arbitrary strings, this can be generalized,

    ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t) ∎

**Theorem A.2.10** ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)

Let *u* and *t* be arbitrary strings in S.

By Theorem A.4.2,

    1. Δ(s) = Δ(inv(s)).

Therefore, 

    2. Δ(ut) = Δ(inv(ut)).

By Theorem A.2.9,
 
    3. Δ(ut) = Δ(u) + Δ(t).

Combining steps 2 and 3, it follows, 

    4. Δ(inv(ut)) = Δ(ut) = Δ(u) + Δ(t)

Since *u* and *t* were arbitrary strings, this can be generalized,

    5. ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t) ∎

**Theorem A.2.11** ∀ t ∈ S: Δ(ς(t)) = 0

This theorem can be stated in natural language as follows: For any String, the Delimiter Count of its *σ*-Reduction is 0.

Let t be an arbitrary string in **S**,

    1. t ∈ S

By Definition 3.1.2, *ς(t)* is the String obtained by removing all occurrences of the Delimiter character *σ* from *t*. By Definition A.2.1, Δ(t) is the number of Delimiter Characters *σ* in a String *t*. Since *ς(t)* has all its Delimiters removed, it contains no occurrences of the Character *σ*. Therefore, 

    2. Δ(ς(t)) = 0

Since *t* was an arbitrary string in **S**, this can be generalized over **S**,

    3. ∀ t ∈ S: Δ(ς(t)) = 0 ∎

**Theorem A.2.12** ∀ t ∈ S: l(ς(t)) + Δ(t) = l(t)

Translation: For any String, its String Length is equal to the String Length of its σ-reduction plus its Delimiter Count.

Let *t* be an arbitrary String in **S**,

   1. t ∈ S

By Definition 3.1.2, *ς(t)* is the String obtained by removing all occurrences of the Delimiter character *σ* from *t*.

By Definition A.2.1, *Δ(t)* is the number of Delimiter characters in *t*.

By Definition 1.1.3, *l(t)* is the total number of non-Empty Characters in *t*, including Delimiters.

Similarly, *l(ς(t))* is the number of non-DelimiterCcharacters in *t*.

Every Character in *t* is either a Delimiter or a non-Delimiter character. Therefore, the total number of characters in *t* is the sum of the number of non-delimiter characters and the number of delimiter characters.

Therefore,

    2. ∀ t ∈ S: l(ς(t)) + Δ(t) = l(t)

Since *t* was an arbitrary String, this can be generalized over **S**,

    1. ∀ s ∈ S: l(s) = l(ς(t)) + Δ(s)  ∎

Theorem A.2.12 expresses a fundamental relationship between the String Length of a String, the String Length of its σ-reduction, and its Delimiter Count. It essentially states that the original String Length can be decomposed into the String Length of the String without Delimiters (the *σ*-reduction) and the number of Delimiters that were removed (the Delimiter Count).

**Example**

Let *t = (𝔞)(σ)(𝔟)(σ)(𝔠)*. Then, by Definition 3.1.2,

    ς(t) = 𝔞𝔟𝔠

The following quantities can then be calculated,

    l(t) = 5    
    Δ(t) = 2
    l(ς(t))= 3

And indeed, 

    l(t) = l(ς(t)) + Δ(t) ∎

**Theorem A.2.13** ∀ ζ ∈ C:sub:`L`: l(ς(t)) + Λ(ζ) = l(ζ) + 1

Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L`,

    1. ζ ∈ C:sub:`L`

By Definition 2.1.2, every Sentence is a String. Therefore, Theorem A.2.12 may be applied to *ζ*

    2. l(ζ) = l(ς(ζ)) + Δ(ζ)

By Theorem A.2.1,

    3. Λ(ζ) = Δ(ζ) + 1

Rearranging,

    4. Δ(ζ) = Λ(ζ) - 1

Substituting the expression for *Δ(ζ)* from step 4 into the equation from step 2,

    5. l(ζ) = l(ς(ζ)) + (Λ(ζ) - 1)

Rearranging the terms, 

    6. l(ς(ζ)) + Λ(ζ) = l(ζ) + 1

Since ζ** was an arbitrary Sentence in **C**:sub:`L`, this can be generalized over the Corpus as,

    7. ∀ ζ ∈ C:sub:`L`: l(σ_reduce(ζ)) + Λ(ζ) = l(ζ) + 1 ∎
