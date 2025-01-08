.. _section-ii:

Section II: Corpora
===================

The work so far has formally constructed a system for representing the first two levels of artifacts from a natural language, Characters (Alphabet) and Words (Language), without appealing to their interpretation in any way except insofar that it takes a stance on the *existence* of an interpretation. As the analysis moves up the chain of linguistic artifacts to the next highest level, Sentences (Corpus), it is tempting to start incorporating semantic features into the theory. However, the objective is to derive palindromic conditions independent of a particular semantic interpretation. Therefore, as the analysis proceeds, special care will be given to the definition of a *Sentence* and its *Corpus*.

.. _section-ii-i:

Section II.I: Definitions
-------------------------

The next level of the semantic hierarchy will now be constructed. Many of the definitions made in this subsection will not be referenced until the final section of this work, when the fundamental properties of Palindromes are established. They are given here, due to the natural progression of concept formation dictating they be defined after the notion of Sentence and Corpus is introduced.

.. _corpus:

Corpus
^^^^^^

The entire system so far constructed relies on the domain of **S**, the set of all Strings that can be formed from an Alphabet of Characters :math:`\Sigma`. Attention has been confined to those entities that satisfy the :ref:`Discovery Axiom W.1 <axiom-w1>`.

In other words, the definitions and theorems so far introduced deal with linguistics entities that do not possess a Delimiter Character. Delimiters will be of central importance in describing palindromic structures, because Delimiters play a central role in the definition of the linguistic entity that will ultimately allow a palindrome to be rigorously defined, a *Sentence*. With that in mind, the concepts and definitions that pave the way to an explication of *Sentence* start with the definition of a *Corpus*.

.. _definition-2-1-1:

**Definition 2.1.1: Corpus** The Corpus of Language **L** is denoted by **C**:sub:`L`. The Corpus set represents a collection of grammatically valid and semantically meaningful Strings. ∎

From the definition, it can easily be seen the Corpus of a Language is a subset of the set of all possible Strings, **S**

.. math::

   C_L \subset S 

This aligns with the idea that the domain of entities in this formal system is defined either as a type of *element* of **S** or a type of *subset* of **S**.

.. _sentence:

Sentence
^^^^^^^^

Before proceeding with the definition of Sentences, some notation is introduced,

    1. Sentences (*ᚠ*, *ᚢ*, *ᚦ*, ... ): Anglo-Saxon (*Old English*) Runes represent a Sentence. Subscripts will occassionally be used in conjunction with Anglo-Saxon letters to denote Sentences, (*ᚠ*:sub:`1`, *ᚠ*:sub:`2`, ... ). 
    2. Sentential Variables (*ζ*, *ξ*): The lowercase Greek letter Zeta and Xi are reserved for indeterminate Sentences, i.e. Sentential Variables. Subscripts will occassionally be used in conjunction with Zeta to denote Sentential Variables, (*ζ*:sub:`1`, *ζ*:sub:`2`, ...)

.. _definition-2-1-2:

**Definition 2.1.2: Sentence** A Sentence in Language **L** is an element of its Corpus. ∎

.. math::

    \rune{f} \in C_L

From :ref:`Definition 2.1.1 <definition-2-1-1>` and :ref:`Definition 2.1.2 <definition-2-1-2>`, it follows that a Sentence is a String,

.. math::

    \rune{f} \in S

It should be stressed, as had been made clear in previous comments, that Characters, Words and Sentences in the current formulation are elements of the same underlying set, the set of all Strings. This connection in the domain of Characters, Words and Sentences is what will allow the analysis to begin to construct the outline of palindromic structures in a Language and Corpus. To reiterate this hierarchy and precisely state how all the entities in this formal system are related,

    1. Strings: ι, α, ζ
    2. Sets: Σ, L, C:sub:`L`
    3. Character Membership: :math:`\iota \in \Sigma`
    4. Word Membership: :math:`\alpha \in L`
    5. Sentence Membership: :math:`\zeta \in C_L`

To clarify the relationship between Strings, Characters, Alphabets, Words, Languages, Sentences and Corpus in plain language,

    1. All Characters, Words and Sentences are Strings.
    2. All Alphabets, Languages and Corpuses are sets of Strings.
    3. All Characters belong to an Alphabet.
    4. All Words belong to a Language.
    5. All Sentences belong to a Corpus.

This web of categorical relations represents the hierarchy of linguistic entities within the formal system. 

.. graphviz:: ../_static/dots/hierarchy.dot
    :caption: A diagram of the semantic hierarchy
    :alt: Semantic Hierarchy Diagram

.. _sentence-notation:

Notation
^^^^^^^^

In :ref:`Section I.I <section-i-i>`, notation was introduced for representing Strings a a sets of ordered Characters. This form of representation provided a formal method for specifying various syntactical conditions and properties of Strings and Words. In particular, this method allowed a formal definition of String Length.  

In a similar way, a method of representing Sentences as sets will now be constructed to enrich the symbolic form given to a Sentence in this formal system. Since all Sentences are Strings, all Sentences have Character-level set or sequence representations, by the Emptying Algorithm. The Discovery Axiom W.1 allows the definition of an algorithm to parse the Words of a Sentence based purely on the presence of Delimiters. 

.. _definition-2-1-3:

**Definition 2.1.3: Word-Level Set Representation**

Let *ζ* be a Sentence in a Corpus C:sub:`L`. Let **Ζ** be the Character-level set representation of *ζ*, i.e. an ordered sequence of Characters from the Alphabet **Σ**. 

The Word-level set representation of *ζ*, denoted by **W**:sub:`ζ`, is defined as the ordered set of words obtained by splitting **Ζ**  at each Delimiter Character, *σ*. Formally, **W**:sub:`ζ` is constructed using the *Delimiting Algorithm*.

.. _delimiting_algorithm:

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
    6. While i ≤ l(ᚠ):
   
        a. If ᚠ[i] ≠ σ:

            i. t ← (t)(ᚠ[i])

        b. Else:

            i. If l(t) > 0:

                1. Apply Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>` to t.
                2. W ← W ∪ { (j, t) }
                3. j ← j + 1
   
            ii. t ← ε

        c. i ← i + 1

    # Finalization
    7. If l(t) > 0:
        a. W ← W ∪ { (j, t) }
        b. j ← j+1
    8. Return W ∎

.. graphviz:: ../_static/dots/delimiting.dot
    :caption: A diagram of the Delimiting Algorithm
    :alt: Delimiting Algorithm Diagram

Note the String which is initialized to hold the Sentence Characters in step *5* is set to an initial value of the Empty Character in the Initialization Block. Also note, the application of the Basis Clause in step *1.b.i.1* ensures this Empty Character is removed after each Word has been processed. This is required, because otherwise the last Word in the Word-level representation will have an Empty Character, which violates the results of :ref:`Theorem 1.2.3 <theorem-1-2-3>`.

The essence of the Delimiting Algorithm lies in the interplay of the :ref:`Discovery Axiom W.1 <axiom-w1>` and :ref:`Definition 2.1.2 <definition-2-1-2>` of a Sentence as a semantic String. :ref:`Definition 2.1.2 <definition-2-1-2>`, like :ref:`Definition 1.2.2 <definition-1-2-2>`, ensures all Sentences and Words are semantic. The only feature that differentiates Sentence and Words in their *"semanticality"* is the presence of a Delimiter (from a syntactical perspective, at any rate). Therefore, by the :ref:`Discovery Axiom W.1 <axiom-w1>`, the Words which a Sentence contains must be exactly those Strings which are separated by a Delimiter Character. 

This formulation has the advantage of not taking a stance on the semantics of a particular language. It allows for the discovery of Words in a Language through the simple boundary of Delimiters within the Sentences of its Corpus. 

The following examples show how to apply the Delimiting Algorithm to construct the Word-level representation of a Sentence. 

**Example**

Let *ᚠ = (𝔞𝔟)(σ)(ε)(σ)(𝔟𝔞)*. Note *l(ᚠ) = 6*.

**Initialization**

During initialization, the Character-level set representation of *ᚠ* is constructed with :ref:`Definition 1.1.2 <definition-1-1-2>` using the Emptying Algorithm, which strips it of its Empty Characters,

.. math::

   1. {\large\rune{f}} = (\mathfrak{a},\mathfrak{b},\sigma,\sigma,\mathfrak{b},\mathfrak{a})
   
.. math::

   2. W_{\rune{f}} = \emptyset
   
.. math::

   3. j = 1

**Iteration**

The following list shows the result of the algorithm after each iteration,

.. math::

   1. j = 2, i = 4, t = \mathfrak{ab}, W_{\rune{f}} = \{ (1, \mathfrak{ab}) \}

.. math::

   2. j = 2, i = 5, t = \sigma, W_{\rune{f}} = \{ (1, \mathfrak{ab}) \}
   
.. math::

   3. j = 3, i = 7, t = \mathfrak{ba}, W_{\rune{f}} = \{ (1, \mathfrak{ab}), (2, \mathfrak{ba}) }

At which point :math:`i > l(\rune{f})`, so the algorithm halts and returns,

.. math::

    W_{\rune{f}} = { (1, \mathfrak{ab}), (2, \mathfrak{ba}) } ∎

**Example** 

Let *ᚠ = "the cat meows"*. Then the Character level representation of *ᚠ* is given by, 

.. math::

    {\large\rune{f}} = { (1, \text{"t"}), (2, \text{"h"}), (3,\text{"e"}), (4,\sigma), (5,\text{"c"}), (6,\text{"a"}), (7,\text{"t"}), (8,\sigma), (9,\text{"m"}), (10,\text{"e"}), (12,\text{"o"}), (13,\text{"w"}), (14,\text{"s"}) }.

Then, applying the *Delimiting Algorithm*, its Word-level representation is constructed, 

.. math::

    W_{\rune{f}} = \{ (1, \text{"the"}), (2, \text{"cat"}), (3, \text{"meows"}) \} 
    
∎

Similar to the Character-level set representation of String, where the Character position is encoded into the first coordinate, the Word-level set representation of a String encodes the presence of Delimiters through its first coordinate. Once Word Length is defined in the next section, a notational shortcut similar to Character Index Notation defined in :ref:`Definition 1.1.5 <definition-1-1-5>` will use this method of Sentence representation to simplify many of the upcoming proofs.

There is a subtle assumption being made in the idea a Sentence can be reduced to a sequence of ordered Words that deserves special mention, as this perhaps reasonable assumption implicitly elides a question of much greater complexity regarding where precisely the semantic information of a Sentence resides. To see what is meant by this, consider the three sentences from Latin,

- Puella canem videt. (Girl dog sees)
- Canem puella videt. (Dog girl sees)
- Videt puella canem. (Sees girl dog)

Latin, like many other natural languages, uses declensions to imbue words with syntactic functions. In some respect, all three of these sentences could be considered the *same* sentence, as the order of the words is not the primary bearer of semantic information; the suffixes do all of the work. While the order of words lends itself to the *voice* and *tone* of the sentence, the meaning of the sentence does not primarily emerge through its Word order. Similar cases exist in any natural language that uses declensions to modify the syntactic function of words, such as Greek. 

The current formal system treats these sentences in Latin as distinct Sentences. If the Latin sentences in this example are to be identified as representatives of the same semantic *"token"*, this cannot occur on the Sentence level of this formal system's linguistic hierarchy. This example suggests Sentences are not the final level of the hierarchy, and that to find the source of meaning in a Sentence, another level must be constructed on top of it capable of identifying these different manifestations as the same *"token"*.

This example does not invalidate the analysis, but it does introduce subtlety that must be appreciated. These concerns must be kept in mind while the formal notion of a Sentence is developed.

.. _word-length:

Word Length
^^^^^^^^^^^

The notion of String Length *l(s)* was introduced in :ref:`Section I.I <section-i-i>` as a way of measuring the number of non-Empty Characters in a String *s*. In order to describe palindromic structures, a new notion of length will need introduced to accomodate a different *"spatial"* dimension in the domain of a Language and its Corpus: *Word Length*.

Intuitively, the length of a Sentence is the number of Words it contains. Since there is no analogue of :ref:`Discovery Axiom W.1 <axiom-w1>` for Sentences (nor should there be), this means Sentences may contain Delimiter Characters. The Words of a Language are separated by Delimiters in the Sentences of its Corpus. 

:ref:`Definition 2.1.3 <definition-2-1-3>` provides a way of dispensing with the Delimiter Character in Sentences, while still retaining the information they provides about the demarcation of Words through the first coordinate of a Sentence's Word-level representation. With the Word-level set representation of Sentence in hand, it is a simple matter to define the notion of Word Length in the formal system.

.. _definition-2-1-4:

**Definition 2.1.4: Word Length**

Let *ζ* be a Sentence in a **C**:sub:`L`. Let **W**:sub:`ζ` be the Word-level set representation of *ζ*, as defined in :ref:`Definition 2.1.3 <definition-2-1-3>`. The Word Length of the Sentence *ζ*, denoted by :math:`\Lambda(\zeta)`, is defined as the cardinality of the set **W**:sub:`ζ`,

.. math::

    \Lambda(\zeta) = | W_{\zeta} | 
    
∎

**Example**

Consider the Sentence *ᚠ = "the dog runs"*. Its Character-level set representation would be given by,

.. math::

    \large\rune{f} = \{ (0,\text{"t"}), (1,\text{"h"}), (2,\text{"e"}), (4,\sigma), (5, \text{"d"}), (6, \text{"o"}), (7, \text{"g"}), (8, \sigma), (9, \text{"r"}), (10, \text{"u"}), (11,\text{"n"}), (12,\text{"s"}) \}

Its Word-level set representation would be given by,

.. math::

    W_{\rune{f}} = \{ (1, \text{"the"}), (2, \text{"dog"}), (3, \text{"runs"}) \}

Therefore, the length of the sentence is:

.. math::

    \Lambda(\rune{f}) = | W_{\rune{f}} | = 3

Note, in this example, 

.. math::

    l(\rune{f}) = 12 
    
∎

This example demonstrates the essential difference in the notions of length that have been introduced. It is worthwhile to clarify the distinction between these two conceptions. 

Let *t* be a String with Character-level representation **T** and Word-level representation **W**:sub:`t`. The hierarchy of its "spatial" dimensions is given below, in order of greatest to least (this fact is proven in :ref:`Section III.II <section-iii-ii>` with :ref:`Theorem 3.2.8 <theorem-3-2-8>`). Terminology is introduced in parenthesis to distinguish these notions of length,

   - l(t) (String Length): The number of non-Empty Characters contained in a String.
   - Λ(t) (Word Length): The number of Words contained in a String 

Note the first level is purely syntactical. Any String *t* will have a String Length *l(t)*. However, not every String possesses Word Length, *Λ(s)*. Word Length contains semantic information. While the presence of Word Length does not necessarily mean the String is semantically coherent (see :ref:`Definition 2.2.1 <definition-2-2-1>` for a precise definition of *semantic coherence*), e.g. "asdf dog fdsa", Word Length does signal an *extension* of Strings into the semantic domain.

Word Length can be used to simplify some of the complex notation the formal system has accumulated. Similar to the Character Index Notation, a way of referring to Words in Sentences within propositions without excessive quantification is now introduced through Word Index notation.

.. _definition-2-1-5:

**Definition 2.1.5: Word Index Notation**

Let *ζ* be a Sentence with Word level set representation, **W**:sub:`ζ`,

.. math::

    W_{\zeta} = (\alpha_1, \alpha_r, ... , \alpha_{\Lambda(\zeta))

Then for any *j* such that :math:`1 \leq j \leq \Lambda(\zeta)`, the Word at index *j*, denoted *ζ{j}*, is defined as the Word which satisfies the following formula,

.. math::

    \forall (j, \alpha_j) \in W_{\zeta}: \zeta\{j\} = \alpha_j
    
∎

The following theorem uses this notation to proves an intuitive concept: the total number of Characters in all of the Words in a Sentence must exceed the number of Words in a Sentence (since there are no Words with a negative amount of Characters). 

.. _theorem-2-1-1:

**Theorem 2.1.1** :math:`\forall \zeta \in C_{L}:  \sum_{j=1}^{\Lambda(\zeta)} l(\zeta\{j\}) \geq \Lambda(\zeta)`

This theorem can be stated in natural language as follows: For any sentence *ζ* in Corpus **C**:sub:`L`, the sum of the String Lengths of the Words in *ζ* is always greater than the Word Length of *ζ*.

Assume :math:`\zeta \in C_L`. Let *j* be a natural number such that :math:`1 ≤ j ≤ \Lambda(\zeta)`

For each ordered Word *ζ{j}* in *ζ*, its String Length *l(ζ{j})* must be greater 0 by the :ref:`Discovery Axiom W.1 <axiom-w1>` and :ref:`Definition 1.1.3 <definition-1-1-3>`. Therefore, since each Word contributes at least a String Length of 1, the sum of the String Lengths *l(ζ{j})* must be greater than or equal to *Λ(ζ)*. ∎

Word Length and Word Index Notation can be used to define the notion of *Boundary Words*, which will be utilized in the main results about Palindromes. 

To illustrate another simplification effected by Index notation in formal proofs about Language, consider how laborious the proof of the following :ref:`Theorem 2.1.2 <theorem-2-1-1>` would be without the ability to refer to Characters embedded in Strings and Words embedded in Sentences through Index notation. 

.. _theorem-2-1-2:

**Theorem 2.1.2** :math:`\forall \zeta, \xi \in C_{L}: \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)`

Let *ζ* and *ξ* be arbitrary Sentences in **C**:sub:`L`. Let **W**:sub:`ζ` and **W**:sub:`ξ` be the Word-level representations of *ζ* and *ξ*, respectively. By Definition 2.1.4, 

.. math::

    1. \Lambda(\zeta) = | W_{\zeta} |

.. math::

    2. \Lambda(\zeta) = | W_{\xi} |

Let *ζξ* be the concatenation of *ζ* and *ξ*. When *ζ* is concatenated to *ξ*, there are several possible cases to consider. 

   - ζ[l(ζ)] = σ, ξ[1] = σ
   - ζ[l(ζ)] = σ, ξ[1] ≠ σ
   - ζ[l(ζ)] ≠ σ, ξ[1] = σ
   - ζ[l(ζ)] ≠ σ, ξ[1] ≠ σ

**Case 1 - 3**: In each of theses cases, the Words of *ζ* and the Words of *ξ* are still separated by at least one Delimiter. Therefore, no new Word is formed during concatenation, and the words in *ζξ* are simply the words of *ζ* followed by the words of *ξ*. Therefore, 

.. math::

    3. \Lambda(\zeta\xi) = \Lambda(\zeta) + \Lambda(\xi).

**Case 4**: ζ[l(ζ)] ≠ σ, ξ[1] ≠ σ. 

In this case, a new Word may be formed during concatenation, but only if *ζ{Λ(ζ)}* concatenated with *ξ{1}* belongs to L (i.e., *(ζ{Λ(ζ)})(ξ{1})* if it is a compound Word). Let *t* be the String such,

.. math::

    4. t = (\zeta\{\Lambda(\zeta)})(\xi\{1\})

This result can be expressed,

.. math::

    5. t \in L \to \Lambda(\zeta\xi) = \Lambda(\zeta) + \Lambda(\xi) - 1.
    
.. math::

    6. t \notin L \to \Lambda(\zeta\xi) = \Lambda(\zeta) + \Lambda(\xi).

In all cases, 

.. math::

    \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi).

Since *ζ* and *ξ* were arbitrary sentences, this can be generalized over the Corpus,

.. math::

    \forall \zeta, \xi \in C_L: \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi) 
    
∎

Word Length is fundamentally different to String Length with respect to the operation of concatenation. In :ref:`Theorem 1.1.1 <theorem-1-1-1>`, it was shown String Length sums over concatenation. :ref:`Theorem 2.1.2 <theorem-2-1-2>` demonstrates the corresponding property is not necessarily true for Word Length. This is an artifact of the ability of concatenation to destroy semantic content.

.. _intervention:

Intervention
^^^^^^^^^^^^

Colloquially, in the Sentence, *"never a dull day"*, the ordered Characters *"a"*,*"d"*,*"u"*,*"l"*, *"l"* are between the Words *"never"* and *"day"*. The concept of *Intervention* is introduced into the formal system to explicate this everyday notion of *"betweenness"*. A precise definition of what it means for a Character to *intervene* two Words in a Sentence is given using the operation of Delimitation introduced in :ref:`Definition 1.2.7 <definition-1-2-7>`.

.. _definition-2-1-6:

**Definition 2.1.6: Intervention**

Let *ζ* be a Sentence in C:sub:`L`. The Character *ζ[k]* is said to *intervene* the Words *ζ{i}* and *ζ{j}*, denoted as *(i/k/j)*:sub:`ζ`, if the following condition holdS

.. math::

   l(D\Pi_{x=1}^{i} \zeta(x)) < k < l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1 ∎

The meaning of :ref:`Definition 2.1.6 <definition-2-1-6>` is not immediately intuitive, so a an explanation and thorough example are now presented to show how the definition corresponds to the common-sense notion of a Character falling between two Words in a Sentence.

Analyzing each component of the inequality in :ref:`Definition 2.1.6 <definition-2-1-6>`: 

- :math:`l(D\Pi_{x=1}^{i} \zeta(x))`: This represents the length of the Delimitation of the first i words of the sentence ζ. In simpler terms, it's the length of the string up to and including the i-th word, including the delimiters.

- k: This is the index of the character in question, ζ[k].
  
- :math:`l(\zeta) - l(D\Pi_{x=1}^{Λ(ζ) - j + 1} inv(ζ)(x)) + 1`: This is the most complex component for the formula, so it deserves a finer analysis,
    
    1. :math:`\Lambda(\zeta) - j + 1`: This calculates the index of the word in the reversed sentence that corresponds to the j:sup:`th` word in the original sentence.
   
    2. :math:`D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)`: This is the Delimitation of the first :math:`(\Lambda(\zeta) - j + 1)` Words of the Inverse of the Sentence *ζ*. This will correspond to the beginning portion of the reversed Sentence up to the Word that corresponds to the j:sup:`th` Word in the original Sentence.
   
    3. :math:`l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x))`: This is the length of the initial portion of the reversed Sentence.
   
    4. :math:`l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1 \text{inv}(\zeta)(x))`: This subtracts the length of the initial portion of the reversed sentence from the total length of the original sentence. This gives us the length of the remaining portion of the original sentence, starting from the character after the word corresponding to j in the original sentence.
   
    5. :math:`l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta)} - j + 1 \text{inv}(\zeta)(x)) + 1`: Finally, add 1 to get the index of the first Character after the word corresponding to j in the original sentence.

To aid in the comprehension of the concept being captured with Definition 2.1.6, the following example shows how to calculate an Intervention.

**Example** 

Let *ᚠ = "repaid a regal leper"*. Note the String and Word Lengths are given by,

.. math::

    l(\rune{f}) = 20
    
.. math::

    \Lambda(\rune{f}) = 4
    
The Word-level representation of this Sentence is given by,

.. math::

    W_{\rune{f}} = \{ (1, \text{"repaid"}), (2, \text{"a"}), (3, \text{"regal"}), (4, \text{"leper"}) \}

Note :math:`\text{inv}(\rune{f}) = \text{"repel lager a diaper"}`. This is an example of an Invertible Sentence that maintains *semantic coherence* (i.e. all of its inverted Words are Words in the Language; see :ref:`Definition 2.2.1 <definition-2-2-1>` in the next subsection for a more formal definition of *semantic coherence*), but lacks *admissibility* (i.e. it is not a grammatical or syntactical sentence; see :ref:`Definition 2.3.1 <definition-2-3-1>` for a formal definition of *admissibility*.) The Word-level representation of the Inverse is given by,

    W_{inv(\rune{f})} = \{ (1, \text{"repel"}), (2, \text{"lager"}), (3, \text{"a"}), (4, \text{"diaper}) \}
    
To see how Definition 2.1.6 can be used to assert a Character falls between two Words in a sentence, calculate the following Delimitations and String Lengths.

Consider the words *"a"* and *"leper"*. *"a"* corresponds to the Word Index 2,

.. math::

    \rune{f}\{2\} = \text{"a"}

Calculating the left-hand side of the inequality in Definition 2.1.6,

.. math::

    D\Pi_{x=1}^{2} \rune{f}(x) = \text{"repaid a"}

.. math::
    
    l(D\Pi_{x=1}^{2} \rune{f}(x)) = 8

The String Length of this Delimitation is exactly equal to the Sentence Length *up to and including the Word at Index 2*. Now note *"leper"* occupies the Word Index 4, 

.. math::

    \rune{f}\{4\} = \text{"leper"}

This corresponds to a :math:`j = 4` in :ref:`Definition 2.1.6 <definition-2-1-6>`. The upperhand limit in the Delimitation on the right-hand side of the inequality in :ref:`Definition 2.1.6 <definition-2-1-6>` is given by,

.. math::

    \Lambda(\rune{f}) - j + 1 = 4 -  4 + 1 = 1

Therefore, the corresponding Delimitation of the Inverse Sentence for :ref:`Definition 2.1.6 <definition-2-1-6>` is given by,

.. math::

    D\Pi_{x=1}^{1} \text{inv}(\rune{f})(x) = \text{"repel"}

.. math::

    l(D\Pi_{x=1}^{1} \text{inv}(\rune{f})(x)) = 5

Working from the back of the Sentence, the String Length of this Delimitation is exactly equal to the Sentence Length *up to and including the Word at Index 4*. Calculating the right-hand side of the inequality in :ref:`Definition 2.1.6 <definition-2-1-6>`, 

.. math::

    l(\rune{f}) - l(D\Pi_{x=1}^{1} \text{inv}(\rune{f})(x)) + 1 = 20 - 5 + 1 = 16

By :ref:`Definition 2.1.6 <definition-2-1-6>`, the Characters *ᚠ[k]* between the indices of 8 and 16 (exclusive) *intervene* *ᚠ{2}* and *ᚠ{4}*, namely, 

    - ᚠ[9] = " "
    - ᚠ[10] = "r"
    - ᚠ[11] = "e"
    - ᚠ[12] = "g"
    - ᚠ[13] = "a"
    - ᚠ[14] = "l"
    - ᚠ[15] = " "

Therefore,

    - (2/9/4):sub:`ᚠ` (the 9:sup:`th` Character is between the second and fourth Word)
    - (2/10/4):sub:`ᚠ` (the 10:sup:`th` Character is between the second and fourth Word)
    - etc. 

.. graphviz:: ../_static/dots/intervention.dot
    :caption: A diagram of the Intervention relation
    :alt: Intervention Diagram

∎

As motivation for the first theorem on Interventions and a further clarification to show how Intervention and Delimitation are closely related, consider the following example.

**Example**

Let *ᚠ = "the world divides into facts"*. Then 

.. math::

    \Lambda(\rune{f}) = 5

.. math::

    l(\rune{f}) = 28

Consider what happens when the limits of the Delimitation of a Sentence and the Delimitation of its Inverse are such that :math:`i = j` in the :ref:`Definition 2.1.6 <definition-2-1-6>`. Let :math:`i = j = 2`, i.e. consider the second Word in the Sentence, *"world"*. The relation of Intervention that obtains between *"world"* and itself should evaluate to false. In other words, no Characters intervene between a Word and itself. 

The Delimitation of the Sentence up to the Second Word is given by,

.. math::

    D\Pi_{x=1}^{2} \rune{f}(x) = \text{"the world"}

The Delimitation of the Inverse Sentence up to the correspond index of the Second Word (e.g., :math:`5 - 2 + 1 = 4`) is given by (Note the Inverse Sentence is not a Sentence in a Corpus, nor does it possess semantic coherence),

.. math::

    D\Pi_{x=1}^{5 - 2 + 1} \text{inv}(\rune{f}(x)) = D\Pi_{x=1}^{4} \text{inv}(\rune{f}(x)) = \text{"stcaf otni sedivid dlrow"}

Therefore,

.. math::

    l(D\Pi_{x=1}^{2} \rune{f}(x)) = 9

.. math::

    l(D\Pi_{x=1}^{4} \text{inv}(\rune{f}(x))) = 24

The sum of these String Lengths is given by,

.. math::

    l(D\Pi_{x=1}^{2} \rune{f}(x)) + l(D\Pi_{x=1}^{4} \text{inv}(\rune{f}(x))) = 9 + 24 = 33

Since the total String Length of both Delimitation exceeds the String Length of the entire Sentence, there does not exist a Character Index *k* such that *k* can be said to intervene the Word at index :math:`i = j = 2`. ∎

This example provides justification for the next theorem.

.. _theorem-2-1-3:

**Theorem 2.1.3** :math:`\forall \zeta \in C_{L}: \forall i, j \in N_{\Lambda(\zeta)}: i \neq k \to \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta}`

This theorem can be stated in natural language as follows: For any Sentence in a Corpus, there exists a Character that intervenes two Words in the Sentence if and only the Words occupy different positions. Note this doesn't exclude possibility the Words at different positions are the same Word.

Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L` and let *i* and *j* be natural numbers such that,

.. math::

    1. \zeta \in C_L
    
.. math::

    2. i, j \in N_{\Lambda(\zeta)}
   
(→) Assume 

.. math::

    3. i \neq j

Without loss of generality (since the case :math:`i > j` is symmetrical), assume 

.. math::

    4. i < j

By :ref:`Theorem 2.3.4 <theorem-2-3-4>`, 

.. math::

    5. \zeta = D\Pi_{x=1}^{\Lambda(\zeta)} p(x)

Where 

.. math::
    
    6. p \in X_L(\Lambda(\zeta))`

By :ref:`Definition 1.2.7 <definition-1-2-7>` of Delimitation, this means 

.. math::

    7. \zeta = (\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{\Lambda\(ζ)\}) 

By step 5, *ζ{i}* comes before *ζ{j}* in the Sentence *ζ*. By the :ref:`Discovery Axiom W.1 <axiom-w1>`, there must be at least one delimiter character between *ζ{i}* and *ζ{j}* because they are distinct Words in a valid Sentence. 

Let *σ* be a delimiter Character between *ζ{i}* and *ζ{j}*. Let *k be the index of this σ in the character-level representation of ζ (i.e., *ζ[k] = σ*).

By the :ref:`Definition 1.2.7 <definition-1-2-7>` of Delimitations, 

.. math::

    8. l(D\Pi_{x=1}^{i} \zeta(x)) 
    
Will give the index of the last character of ζ{i}. Since σ comes after ζ{i}, it follows,

.. math::

    9. l(D\Pi_{x=1}^{i} \zeta(x)) < k

Similarly, 

.. math::

    10. l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1 
    
Gives the index of the first Character after the Word corresponding to *ζ{j}* in the original sentence. Since σ comes before this character, it follows,

.. math::

    11. k < l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1

Therefore, by :ref:`Definition 2.1.6 <definition-2-1-6>`, 

.. math::

    12. (i/k/j)_{\zeta}

Thus,

.. math::

    13. \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta}

(←) Assume a Character exists at index *n* in *ζ* such that it that intervenes *ζ{i}* and *ζ{j}*,

.. math::

    1. \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta}

By :ref:`Definition 2.1.6 <definition-2-1-6>`,

.. math::

    2. l(D\Pi_{x=1}^{i} \zeta(x)) < n < l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1

Assume, for the sake of contradiction, that :math:`i = j`.

.. math::

    3. l(D\Pi_{x=1}^{i} \zeta(x)) < n < l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x)) + 1

Now, consider the term :math:`l(D\Pi_{x=1}^{i} \zeta(x))`. This represents the String Length of the Delimitation of the first *i* words of *ζ*. By the :ref:`Definition 1.2.7 <definition-1-2-7>` of Delimitations, this includes the lengths of the first *i* words and the lengths of the :math:`(i - 1)` delimiters between them.

Similarly, consider the term :math:`l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x))`. This represents the String Length of the Delimitation of the first *Λ(ζ) - i + 1* words of *inv(ζ)*.  Since *inv(ζ)* has the same words as *ζ* but inverted and in reverse order, this is equivalent to the String Length of the uninverted Sentence up to the *i*:sup:`th` word of *ζ*, measured from the last Character in the String.

The sum of the String Lengths of these two portions of the Sentence *ζ* is always greater than the String Length of the Sentence, 

.. math::

    4. l(D\Pi_{x=1}^{i} \zeta(x)) + l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x)) >  l(\zeta) 

This follows from the fact that these two portions of ζ are overlapping since both  include terms for *ζ{i}* (:math:`\text{inv}(\zeta)\{\Lambda(\zeta) - i + 1}` would be the corresponding Word in the Delimitation of the Inverse). From step 4, it then follows,

.. math::

    5. l(D\Pi_{x=1}^{i} \zeta(x)) > l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x))  
    
Adding 1 to both sides maintains the inequality in step 5,

.. math::

    6. l(D\Pi_{x=1}^{i} \zeta(x)) + 1 > l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x)) + 1

Combining this with the left-hand side of the inequality in step 5, we get:

.. math::

    7. l(D\Pi_{x=1}^{i} \zeta(x)) < n < l(D\Pi_{x=1}^{i} \zeta(x)) + 1
   
But String Lengths are integers, and by the laws of arithmetic, there cannot exists a natural number between two numbers that are successors of one another. A contradiction has been dervied. Therefore, the assumption that :math:`i = j` must be false.

.. math::

    8. i \neq j.

With both directions of the equivalence proven, since *ζ*, *i*, and *j* were arbitrary, this can be generalized over the Corpus, 

.. math::

    \forall \zeta \in C_L: \forall i, j \in N_{\Lambda(zeta)}: i \neq j ↔ \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta} 
    
∎

.. _section-ii-ii:

Section II.II: Axioms 
----------------------

In :ref:`Section I <section-i>`, the first three axioms of the formal system were introduced. Now that definitions and notations have been introduced for Sentence and Corpus, the axioms may be expanded to further refine the character of the system being built. The Equality, Character and Discovery Axiom are reprinted below, so they may be considered in sequence with the other axioms.

Note the Discovery Axiom has been revised to employ Character Index notation. 

.. _axiom-c0-2:

**Axiom C.0: The Equality Axiom**

.. math::

    1. \forall \iota \in \Sigma: \iota = \iota

.. math::

    2. \forall \iota, \nu \in \Sigma: \iota = \nu ↔ \nu = \iota
    
.. math::

    3. \forall \iota, \nu, \omicron \in \Sigma: (\iota = \nu \land \nu = \omicron) \to (\iota = \omicorn) 

∎

.. _axiom-c1-2:

**Axiom C.1: The Character Axiom**

.. math::

    \forall \iota \in \Sigma: \iota \in S 
    
∎

.. _axiom-w1-2:

**Axiom W.1: The Discovery Axiom ** 

.. math::

    \forall \alpha \in L: [ (l(\alpha) \neq 0) \land (\forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma) ] 
    
∎

.. _axiom-s1:

**Axiom S.1: The Duality Axiom**

.. math::

    ( \forall \alpha \in L: \exists \zeta \in C_L: \alpha \subset_s \zeta ) ∧ ( \forall \zeta \in C_L: \exists \alpha \in L: \alpha \subset_s \zeta ) 
    
∎

.. _axiom-s2:

**Axiom S.2: The Extraction Axiom**

.. math::

    \forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in L 
    
∎

Two new axioms, the :ref:`Duality Axiom S.1 <axiom-s1>` and the :ref:`Extraction Axiom S.2 <axiom-s2>`, have been added to the formal system to finalize its core assumptions. It is worth taking the time to analyze the structure, however minimal, these axioms imply must exist in any Language. It should be re-iterated that no assumptions have been made regarding the semantic content of a Language or its Corpus, so any insight that arises from these axioms is due to inherent linguistic structures (assuming these axioms capture the nature of real language). 

To briefly summarize the axioms previously introduced: The system *"initializes"* with the assumption of an equality relation and the selection of an Alphabet **Σ**. The Character Axiom ensures the domain of all Strings is populated. The Discovery Axiom ensures Words only traverse the set of Strings which do not contain Delimiters. With these axioms, still nothing has been said about *what* a Word is, except that it possesses a semantic character. To re-iterate, a Language and Corpus are fixed on top of the domain of all Strings outside of the system. 

The new axioms introduced in the formal system begin to characterize the syntactical properties of the next level in the lingustic hierarchy, while still maintaining their ambivalence on the semantic content contained within their respective categories.

The :ref:`Duality Axiom S.1 <axiom-s1>` bares a striking resemblance to the idea of *surjection* in real analysis. Recall, a function :math:`f: X \to Y` is called *surjective* if,

.. math::

    \forall y \in Y: \exists x \in X : f(x) = y

Meaning, every element in the co-domain is mapped to at least one element in the domain. 

In a sense, the :ref:`Duality Axiom S.1 <axiom-s1>` asserts a type of *"double-surjectivity"* exists between the domain of Words and the co-domain of Sentences.  In plain language, the :ref:`Duality Axiom <axiom-s1>` asserts for every Word *α* in the Language **L**, there exists a sentence *ζ* in the Corpus **C**:sub:`L` such that *α* is contained in *ζ*, and for every Sentence *ζ* in the corpus **C**:sub:`L`, there exists a word *α* in the language **L** such that *α* is contained in *ζ*. 

However, there is a key difference between the notion of *surjection* in real analysis and the notion captured in the Duality Axiom S.1. Containment is not a strict equality relation. By :ref:`Definition 1.1.6 <definition-1-1-6>` and :ref:`Definition 1.1.7 <definition-1-1-7>`, containment reduces to the existence of a mapping between Characters in different Strings. Due to the :ref:`Discovery Axiom W.2 <axiom-w2>`, with the exception of Sentences consisting of a Single Word, a Word is contained in a Sentence but a Sentence is not contained in a Word. 

More plainly, the :ref:`Duality Axiom S.1 <axiom-s1>` states a Word cannot exist in a Language without being included in a Sentence of the Corpus, and a Sentence cannot exist in a Corpus without including a Word from the Language. This Axiom captures an inextricable duality between the metamathematical concepts of Sentence and Word, and the concepts of Language and Corpus: one cannot exist without implying the existence of the other. Words and Sentences do not exist in isolation. A Language and its Corpus require one another. 

The :ref:`Extraction Axiom S.2 <axiom-s2>` further strengthens the relationship that exists between a Corpus and Language. It states every Word in the Sentence of a Corpus must be included in a Language. This idea of being able *extract* the Words of a Language from a Sentence is captured in the terminology introduced in :ref:`Definition 2.2.1 <definition-2-2-1>` directly below. 
 
.. _definition-2-2-1:

**Definition 2.2.1: Semantic Coherence** 

A Sentence *ᚠ* is *semantically coherent* in a Language **L** if and only if **W**:sub:`ᚠ` only contains words from Language **L**. 

A Corpus C:sub:`L` is *semantically coherent* in a Language **L** if and only if the Word-level set representation of all its Sentences are semantically coherent. ∎

.. _sentence_theorems:

Theorems
^^^^^^^^

The first theorems proven using these new axioms are analogous versions of the Word theorems :ref:`Theorems 1.2.1 <theorem-1-2-1>` - :ref:`1.2.3 <theorem-1-2-3>` for Sentences. These theorems, like their Word counterparts, represent the logical pre-conditions for Sentences to arise in the domain of all Strings. 

.. _theorem-2-2-1:

**Theorem 2.2.1** :math:`\forall \zeta \in C_L: l(\zeta) \neq 0`

Let *ζ* be an arbitrary sentence in C:sub:`L`, and let *i* be a natural number such that :math:`1 \leq i \leq l(\zeta)`.

By the second conjunct of the :ref:`Duality Axiom S.2 <axiom-s2>` and the first conjunct of the :ref:`Discovery Axiom W.1 <axiom-w1>`,

.. math::

    1. \exists \alpha \in L: \alpha \subset_s \zeta 
    
.. math::

    2. \forall \alpha \in L: l(\alpha) \neq 0

Therefore, by :ref:`Definition 1.1.7 <definition-1-1-7>`, there exists a strictly increasing and consecutive function *f* such that,

.. math::

    3. \forall i \in N_{l(\alpha)}: \alpha[i] = \zeta[f(i)] 
    
By :ref:`Theorem 1.2.3 <theorem-1-2-3>`, 

.. math::

    4. \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon

Therefore, combining steps 3 and 4,

.. math::

    5. \forall i \in N_{\alpha}: \zeta[f(i)] \neq ε

Since, by step 2, :math:`l(\alpha) \neq 0`, there must be some non-zero *i* that satisfies step 5. Therefore, there is at least one non-Empty Character in *ζ*, namely, *ζ[f(i)]*. The theorem is then proven by applying :ref:`Definition 1.1.3 <definition-1-1-3>`,

.. math::

    1. l(\zeta) \neq 0 

∎

.. _theorem-2-2-2:

**Theorem 2.2.2** :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \zeta[i] \subset_s \zeta`

Let *ζ* be an arbitrary sentence in C:sub:`L`, and let *i* be a natural number such that :math:`1 \leq i \leq l(\zeta)`. By :ref:`Theorem 2.2.1 <theorem-2-2-1>` and :ref:`Definition 1.1.3 <definition-1-1-3>`, there must be at least one non-Empty Character in *ζ*. Let *ζ[i]* be a non-Empty Character in *ζ*. Consider the string *s* consisting of the single character *ζ[i]*, :math:`s = \zeta[i]`. Clearly, by :ref:`Definition 1.1.3 <definition-1-1-3>`, 

.. math::

    1. l(s) = 1

Define a function :math:`f: \{1\} \to \{i\}` such that :math:`f(1) = i`. This function is strictly increasing and consecutive. By :ref:`Definition 1.1.6 <definition-1-1-6>` and :ref:`Definition 1.1.7 <definition-1-1-7>`, since there exists a strictly increasing and consecutive function *f* from the indices of *s* to the indices of *ζ*, and since the Character at position 1 in *s* is the same as the Character at position i in *ζ* (both are *ζ[i]*), we can conclude that *s* is contained in *ζ*. Therefore, 

.. math::

    2. \zeta[i] \subset_s \zeta

Since *ζ* and *i* were arbitrary, this can be generalized, 

.. math::

    3. \forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \zeta[i] \subset_s \zeta 

∎

.. _theorem-2-2-3:

**Theorem 2.2.3** :math:`\forall \zeta \in C_{L} : \forall i \in N_{l(\zeta)}:  \zeta[i] \neq \varepsilon`

Let *ζ* be an arbitrary sentence in **C**:sub:`L`, and let *i* be a natural number such that :math:`1 \leq i \leq l(\zeta)`. By :ref:`Theorem 2.2.2 <theorem-2-2-2>`, 

.. math::
    
    1. \forall i \in N_{l(\zeta)}: \zeta[i] subset_s \zeta

By :ref:`Definition 1.1.3 <definition-1-1-3>`, String Length is the number of non-Empty Characters in a String's Character-level set representation. Since :math:`l(\zeta) > 0`, *ζ* must have at least one non-Empty character.

Since :math:`1 \leq i \leq l(\zeta)`, the Character at position *i* in *α*, denoted *ζ[i]*, exists and is non-Empty by :ref:`Definition 1.1.2 <definition-1-1-2>`. Therefore, 

.. math::

    2. \zeta[i] \neq \varepsilon 

Since *ζ* and *i* are arbitrary, this can generalized,

.. math::

    3. \forall \alpha \in L: \forall i \in N_{l(\zeta)}: \zeta[i] \neq \varepsilon 

∎

.. _theorem-2-2-4:

**Theorem 2.2.4** :math:`\forall \zeta \in C_{L}: \Lambda(\zeta) \geq 1`

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. By the second conjunct of the :ref:`Duality Axiom S.1 <axiom-s1>`,

.. math::

    1. \exists \alpha \in L: \alpha \subset_s \zeta

By the first conjunct of the :ref:`Discovery Axiom W.1 <axiom-w1>`,

.. math::

    2. l(\alpha) \neq 0

Therefore, by :ref:`Definition 1.1.7 <definition-1-1-7>`, there exists an *f* such that, 

.. math::

    3. \forall i \in N_{l(\alpha)}: \alpha[i] = \zeta[f(i)]

By :ref:`Theorem 1.2.3 <theorem-1-2-3>`, 

.. math::

    4. \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon

Therefore, combining step 3 and 4,

.. math::

    5. \forall i \in N_{l(\alpha)}: \zeta[f(i)] \neq \varepsilon

Since :math:`l(\alpha) \neq 0`, there is at least one non-Empty Character in *ζ* and therefore, by :ref:`Definition 1.1.3 <definition-1-1-3>`,

.. math::

    6. \Lambda(\zeta) \geq 1

Generalizing this over the Corpus,

.. math::
    
    7. \forall \zeta \in C_L: \Lambda(\zeta) \geq 1 

∎

.. _theorem-2-2-5:

**Theorem 2.2.5** :math:`\forall \zeta \in C_L: \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`

This theorem can be stated in natural language as follows: Every Sentence in the Corpus is the Delimitation of its own Words.

Assume 

.. math::

    1. ζ \in C_L

By :ref:`Definition 2.1.3 <definition-1-2-3>`,

.. math::

    2. W_{\zeta} = (\alpha_1, \alpha_2, ..., \alpha_{\Lambda(\zeta)}) 
    
where

.. math::

    3. \alpha_i \in L.

By :ref:`Definition 1.2.5 <definition-1-2-5>`, the sequence **W**:sub:`ζ` forms a phrase P:sub:`Λ(ζ)` of length *Λ(ζ)* where,

.. math::

   4. \forall i \in N_{\Lambda(\zeta)}: P_{\Lambda(\zeta)}(i) = \alpha_i 
    
By :ref:`Definition 1.2.7 <definition-1-2-7>`, the Delimitation of P:sub:`Λ(ζ)` is,

.. math::

    4. D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)} (i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_{\Lambda(\zeta)})

The Delimitation reconstructs the original Sentence *ζ* by including the Delimiters between Words. Therefore,

.. math::

    5. \zeta = D\Pi_{i=1}^{\Lambda(\zeta) P_{\Lambda(\zeta)} (i)

By :ref:`Definition 2.1.5 <definition-2-1-5>`, 

.. math::

    6. \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} = \alpha_i

Therefore,

.. math::
    
    7. \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}

Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,

.. math::

    8. \forall \zeta \in C_L: \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\} 

∎

.. _section-ii-iii:

Section II.III: Sentence Classes 
--------------------------------

As the astute reader has no doubt surmised at this point, the foundational operation that defines a palindromic structure in linguistics is *inversion* (i.e. a method of reversal). What may not yet be clear is how this operation of inversion propagates through the hierarchy of entities defined over its domain. As this necessary structure of interdependent inversions between hierarchical layers becomes apparent, the mathematical description of a Palindrome will seen to be a *"recursion of inversions"*.

:ref:`Theorems 2.3.9 <theorem-2-3-9>` - :ref:`2.3.11 <theorem-2-3-11>` of this subsection mark the first notable results obtained from the formal system. Their empirical truth in natural language represents confirmation of the formal system's construction. These theorems demonstrate the Character-level symmetries required by invertibility propagate up through the Word-level of linguistics and manifest in conditions that must be imposed on the Word-level structure of an Invertible Sentence.

.. _admissible-sentences:

Admissible Sentences
^^^^^^^^^^^^^^^^^^^^

The notion of an *Admissible Sentence* is required to prevent a certain class of Sentence inversions from invalidating the symmetry conditions of Palindromes derived in :ref:`Section IV <section-iv>`. 

To see what is meant by this concept of *admissibility*, consider the English sentence,

.. math::

    \rune{f} = \text{"strap on a ton"}

The Inverse of this sentence, *inv(ᚠ)*, is *semantically coherent* (:ref:`Definition 2.2.1 <definition-2-2-1>`). By this it is meant every word in its inversion is part of the English language,

.. math::

    \text{inv}(\rune{f}) = \text{"not a no parts"}

However, this is not enough to ensure *inv(ᚠ)* is part of the Corpus, as is apparent. *Semantic coherence* is a necessary but not sufficient condition for the Inverse of a Sentence to remain in the Corpus. In order to state the requirement that must be imposed on a Sentence to remain *admissible* after inversion, the concept of Delimitation introduced in :ref:`Definition 1.2.7 <definition-1-2-7>` must now be leveraged. 

.. _definition-2-3-1:

**Definition 2.3.1: Admissible Sentences**

Let *p* be any Phrase from a Language's *n*:sup:`th` Lexicon **X**:sub:`L`(*n*). A String *t* is said to belong to the class of *Admissible Sentences of Word Length n* in Language **L**, denoted **A**(*n*), if it satisfies the following open formula

.. math::

    t \in A(n) \leftrightarrow (\exists p \in X_L(n): t = D\Pi_{i=1}^{n} p(i)) \land (t \in C_L)

∎

The notion of *admissibility* is a faint echo of *"grammaticality"*. As inversion is studied at the sentential level of the linguistic hierarchy, it is no longer permitted to ignore semantics in its entirety. Instead, semantics ingresses into the system as implicit properties the extensionally identified Sentences must obey. Before discussing this at greater length, several theorems are proved about classes of Admissible Sentences.

.. _theorem-2-3-1:

**Theorem 2.3.1** :math:`A(n) \subseteq C_{L}`

Let *t* be an arbitrary String such that :math:`t \in A(n)`. By :ref:`Definition 2.3.1 <definition-2-3-1>`, this implies, :math:`t \in C_L`. Therefore,

.. math::

    1. t \in A(n) \to t \in C_L

This is exactly the set theoretic definition of a subset. Thus,

.. math::

    2. A(n) \subseteq C_L 

∎

:ref:`Theorem 2.3.1 <theorem-2-3-1>` is the formal justification for quantifying Sentence Variables over the set of Admissible Sentences (i.e. all Admissable Sentences are in the Corpus), as in the following theorem.

.. _theorem-2-3-2:

**Theorem 2.3.2** :math:`\forall \zeta \in A(n): \Lambda(\zeta) = n`

Let *ζ* be an arbitrary sentence in **A**(*n*). By :ref:`Definition 2.3.1 <definition-2-3-1>`, if *ζ* *∈* **A**(*n*), then there exists a Phrase :math:`p \in X_L(n)` such that 

.. math::

    1. (\zeta \in C_L) \land (\zeta = D\Pi_{i=1}^{n} p(i))

By :ref:`Definition 1.2.5 <definition-1-2-5>` and :ref:`Definition 1.2.6 <definition-1-2-6>`, a phrase *p* in :math:`X_L(n)` is an ordered sequence of *n* words such that :math:`\alpha_i \in L`,

.. math::

    2. p = (\alpha_1, \alpha_2, ..., \alpha_n)

By :ref:`Definition 1.2.7 <definition-1-2-7>`, the Delimitation of *p* is given by,

.. math::

    3. D\Pi_{i=1}^{n} p(i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_n)

In other words, the Delimitation of *p* (which is equal to *ζ*) explicitly constructs a String with *n* Words separated by Delimiters.

By :ref:`Definition 2.1.4 <definition-2-1-4>`, the Word Length *Λ(ζ)* is the number of Words in *ζ*. Since *ζ* is formed by limiting a Phrase with *n* Words, and the Delimitation process doesn't add or remove Words, the Word Length of *ζ* must be *n*. Therefore, 

.. math::

    4. \Lambda(\zeta) = n.

Since *ζ* was an arbitrary sentence in **A**(*n*), this can generalize as,

.. math::

    5. \forall \zeta \in A(n): \Lambda(\zeta) = n ∎

.. _theorem-2-3-3:

**Theorem 2.3.3** :math:`\forall \zeta \in C_{L}: \zeta \in A(\Lambda(\zeta))`

Let ζ be an arbitrary sentence in C:sub:`L`. By :ref:`Definition 2.1.3 <definition-2-1-3>`, *ζ* has a Word-level representation,

.. math::

    1. W_{\zeta} = (\alpha_1, \alpha_2, ... , \alpha_{\Lambda(\zeta)}) 
    
Where each :math:`\alpha_i \in L`. By :ref:`Definition 1.2.5 <definition-1-2-5>`, the sequence :math:`(\alpha_1, \alpha_2, ... , \alpha_{\Lambda(\zeta)})` forms a phrase **P**:sub:`Λ(ζ)` of length *Λ(ζ)* where :math:`P_{\Lambda(\zeta)(i) = \alpha_i` for all *i*, :math:`1 \leq i \leq \Lambda(\zeta)`.

By :ref:`Definition 1.2.6 <definition-1-2-6>`, since **P**:sub:`Λ(ζ)` is a phrase of length *Λ(ζ)* and all its Words belong to **L** (by semantic coherence), then,

.. math::

    2. P_{\Lambda(\zeta)} \in X_L(\Lambda(\zeta)).

By :ref:`Definition 1.2.7 <definition-1-2-7>`, the Delimitation of P:sub:`Λ(ζ)` is:

.. math::

    3. D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)}(i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_{\Lambda(\zeta)})

The Delimitation :math:`D\Pi_{i=1}^{\Lambda(\zeta) P_{\Lambda(\zeta)} (i)` reconstructs the original sentence *ζ*, including the Delimiters between Words. Therefore,

.. math::

    4. \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)}(i)

By :ref:`Definition 2.3.1 <definition-2-3-1>`, a String *t* is an Admissible Sentence of Word Length *n* (:math:`t \in A(n)`) if and only if there exists a phrase :math:`p \in X_L(n)` such that,

.. math::

    5. t = D\Pi_{i=1}^{n} p(i)
    
.. math::

    6. t \in C_L

As a direct consequence of :ref:`Definition 2.3.1 <definition-2-3-1>`, since the conjunction of the following three facts is true,

.. math::

    7. \zeta \in C_L
    
.. math::
    
    8. \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)} (i)
   
.. math::

    9.  P_{\Lambda(\zeta)} \in X_L(\Lambda(\zeta)) 
    
It follows from step 7 - step 9, :math:`\zeta \in A(\Lambda(\zeta))`. Since *ζ* was an arbitrary Sentence in C:sub:`L`, this can generalize over the Corpus,

.. math::

    10. \forall \zeta \in C_L: \zeta \in A(\Lambda(\zeta)) 

∎

.. _theorem-2-3-4:

**Theorem 2.3.4** :math:`\forall \zeta \in C_L: \exists p \in X_L(\Lambda(\zeta)): \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} p(i)`

Let *ζ* be an arbitrary sentence in C:sub:`L`. By :ref:`Definition 2.1.3 <definition-2-1-3>`, *ζ* has a Word-level representation,

.. math::

    1. W_{\zeta} = (\alpha_1, \alpha_2, ..., \alpha_{\Lambda(\zeta)}) 
    
Where each :math:`\alpha_i \in L`.

By :ref:`Definition 1.2.5 <definition-1-2-5>`, the sequence :math:`(\alpha_1, \alpha_2, ... , \alpha_{\Lambda(\zeta)})` forms a Phrase **P**:sub:`Λ(ζ)` of Word Length *Λ(ζ)* where :math:`P_{\Lambda(\zeta)}(i) = \alpha_i` for all *i*, :math:`1 \leq i \leq \Lambda(\zeta)`.

By :ref:`Definition 1.2.6 <definition-1-2-6>`, since **P**:sub:`Λ(ζ)` is a Phrase of Word Length *Λ(ζ)* and all its words belong to **L**, then,

.. math::

    2. P_{\Lambda(\zeta)} \in X_L(\Lambda(\zeta))

By :ref:`Definition 1.2.7 <definition-1-2-7>`, the Delimitation of **P**:sub:`Λ(ζ)` is,

.. math::

    3. D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)} (i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_{\Lambda(\zeta)})

The Delimitation :math:`D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)}(i)` reconstructs the original Sentence *ζ*, including the Delimiters between Words. Therefore:

.. math::

    4. \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)}(i)

It has been shown that for an arbitrary Sentence :math:`ζ \in C_L`, there exists a Phrase *p* (specifically, **P**:sub:`Λ(ζ)`) in :math:`X_L(\Lambda(\zeta))` such that,
 
.. math::

    5. \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} p(i). 
    
Therefore, generalizing this over the Corpus,

.. math::

    \forall \zeta \in C_L: \exists p \in X_L(\Lambda(\zeta)): \zeta = D\Pi_{i=1}^{\Lambda(\zeta) p(i) 
    
∎

The condition of *admissibility*, as will be seen in :ref:`Theorem 2.3.11 <theorem-2-3-11>`, prevents the *"inversion propagation"* from being a purely syntactical operation. The Inverse of a Sentence must also be Admissible in the Corpus in order to be considered an Invertible Sentence (:ref:`Definition 2.3.2 <definition-2-3-2>` in the next section). This represents a rupture or division from the realm of syntax not seen at the Word level of the linguistic hierarcy when considering the operation of inversion. In order to fully specify the conditions for Sentence invertibility, one must be able to elaborate what it means to call a Sentence *"admissible"*; in other words, there must be grammatical rules that identify an inverted Sentence as belonging to the Corpus over and above the syntactical conditions that are imposed by invertibility.

However, this does not mean *"grammaticality"* is equivalent to *"admissibility"*. As the final section of the work will make clear, there are possible avenues available to formal analysis for parsing the concept of *"admissibility"* into finer partitions such as *"syntactical admissibility"* and *"semantic admissiblity"*. In this way, the origin of meaning in a Sentence can be narrowed down by filtering out its syntactical origins.

.. _invertible-sentences:

Invertible Sentences
^^^^^^^^^^^^^^^^^^^^

Similarly to the progression of Words and their related concepts in the previous section, a special class of Sentences will now be classified according to their syntactical properties. In the study of palindromic structures, the notion of *Invertible Sentences* is essential. The definition, as is fitting in a work focused on palindromes, will mirror :ref:`Definition 1.3.2 <definition-1-3-2>` of an *Invertible Word*.

The notion of Invertible Sentences will first be defined extensionally, and then clarified heuristically. The following definition and theorem mirror the mechanics of :ref:`Definition 1.3.2 <definition-1-3-2>` and :ref:`Theorem 1.3.2 <theorem-1-3-2>` almost exactly.

.. _definition-2-3-2:

**Definition 2.3.2: Invertible Sentences** 

Let *ζ* be any Sentence in from a Corpus **C**:sub:`L`. Then the set of Invertible Sentences **K** is defined as the set of *ζ* which satisfy the open formula,

.. math::

    \zeta \in K \leftrightarrow \text{inv}(\zeta) \in C_L

A Sentence *ζ* will be referred to as *Invertible* if it belongs to the class of Invertible Sentences. ∎

This definition is immediately employed to derive the following theorems.

.. _theorem-2-3-5:

**Theorem 2.3.5** :math:`\forall \zeta \in C_L: \zeta \in K \leftrightarrow \text{inv}(\zeta) \in K`

Let *ζ* be any Sentence from Corpus **C**:sub:`L`.

(→) Assume :math:`\zeta \in K`

By :ref:`Definition 2.3.2 <definition-2-3-2>`, the inverse of *ζ* belongs to the Corpus

.. math::

    1. \text{inv}(\zeta) \in C_L

To show that *inv(ζ)* is invertible, it must be shown that,

.. math::

    2. \text{inv}(\text{inv}(\zeta)) \in C_L

From :ref:`Theorem 1.2.4 <theorem-1-2-4>`, for any string *s*, 

.. math::

    3. \text{inv}(\text{inv}(s)) = s.  

By :ref:`Definition 2.1.1 <definition-2-1-1>`,

.. math::

    4. \zeta \in S

Where **S** is the set of all Strings. Therefore, it follows, 

.. math::

    5. \text{inv}(\text{inv}(\zeta)) = \zeta

From step 1 and step 5, it follows, 

.. math::

    6. \text{inv}(\text{inv}(\zeta)) \in C_L

By :ref:`Definition 2.3.2 <definition-2-3-2>`, this implies,

.. math::

    7. \text{inv}(\zeta) \in K.

(←) Assume :math:`\text{inv}(\zeta) \in K`

By :ref:`Definition 2.3.2 <definition-2-3-2>`, 
    
.. math::

    8. \text{inv}(\text{inv}(\zeta)) \in C_L

Applying :ref:`Theorem 1.2.4 <theorem-1-2-4>`,

.. math::

    9. \text{inv}(\text{inv}(\zeta)) = \zeta.

From step 8 and step 9, it follows, 

.. math::

    10. \zeta \in C_L

By :ref:`Definition 2.3.2 <definition-2-3-2>`, it follows,

.. math::

    11. \zeta \in K. 

Putting both direction of the equivalence together and generalizing over the Corpus, the theorem is shown,

.. math::

    12. \forall \zeta \in C_L: \zeta \in K \leftrightarrow \text{inv}(\zeta) \in K 

∎

.. _theorem-2-3-6:

**Theorem 2.3.6** :math:`\forall \zeta \in C_L: \text{inv}(\zeta) \in K \to \zeta \in C_L`

Let *ζ* be any Sentence from Corpus **C**:sub:`L` such that :math:`\text{inv}(\zeta) \in K`. Then, by :ref:`Definition 2.3.2 <definition-2-3-2>`,

.. math::

    1. \text{inv}(\text{inv}(\zeta)) \in C_L

By :ref:`Theorem 1.2.4 <theorem-1-2-4>`,

.. math::

    2. \text{inv}(\text{inv}(\zeta)) = \zeta

Therefore, combining step 1 and step 2,

.. math::

    3. \zeta \in C_L 

It follows, 

.. math::

    4. \forall \zeta \in C_L: \text{inv}(\zeta) \in K \to \zeta \in C_L 

∎

The notion of Invertible Sentences is not as intuitive as the notion of Invertible Words. This is due to the fact the condition of *invertibility* is not a weak condition; indeed, Sentences that are not invertible far outnumber Sentences that are invertible in a given Language (for all known natural languages, at any rate; it is conceivable a purely formal system with no semantic content or general applicability could be constructed with invertibility in mind). 

To see how strong of a condition invertibility is, the author challenges the reader to try and construct an invertible sentence in English (or whatever their native tongue might be). :ref:`Section IX <section-ix>` contains a list of Invertible Words and Reflective Words. These can be used as a "palette" for the exercise. The exercise is worthwhile, because it forces the reader to think about the mechanics of sentences and how a palindrome resides in the intersection of semantics and syntax.  

Consider the following examples phrases from English,

- no time
- dog won 
- not a ton 

All of these phrases may be *inverted* to produce semantically coherent phrases in English, 

- emit on
- now god
- not a ton 

Note the last item in this list is an example of what this work has termed a Perfect Palindrome. These examples were specially chosen to highlight the connection that exists between the class of Perfect Palindromes and the class of Invertible Sentences. It appears, based on this brief and circumstantial analysis, that Perfect Palindromes are a subset of a larger class of Sentences, namely, Invertible Sentences.

Due to the definition of Sentences as semantic constructs and the definition of Invertible Sentences as Sentences whose Inverses belong to the Corpus, this means Invertible Sentences are exactly those Sentences that maintain *semantic coherence* (:ref:`Definition 2.2.1 <definition-2-2-1>`) and *admissibility* (:ref:`Definition 2.3.1 <definition-2-3-1>`) under inversion. In order for a Sentence to be Invertible it must possess symmetry on both the Character-level and the Word-level, while maintaining a semantic structure at the Sentence level that accomodates this symmetry. This connection between the symmetries in the different linguistic levels of an Invertible Sentence will be formalized and proven by the end of this subsection. The next series of theorems, :ref:`Theorems 2.3.7 <theorem-2-3-7>` - :ref:`2.3.8 <theorem-2-3-8>` are as the preparatory foundation for establishing this symmetrry. 

.. _theorem-2-3-7:

**Theorem 2.3.7** :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} \in L`

Let *ζ* be a Sentence from Corpus **C**:sub:`L`. Assume :math:`ζ \in K` . By :ref:`Definition 2.3.2 <definition-2-3-2>`,

.. math::

    1. \text{inv}(\zeta) \in C_L

By the :ref:`Extraction Axiom S.2 <axiom-s2>`,

.. math::

    2. \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} \in L 
 
Therefore, 

.. math::

    3. \zeta \in K \to \text{inv}(\zeta)\{i\} \in L 

Since *ζ* was arbitrary, this can be generalized over the Corpus,

.. math::

    4. \forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} \in L 

∎

The next theorem shows how the inversion "distributes" over the Words of a Delimited Sentence.

.. _theorem-2-3-8:

**Theorem 2.3.8** :math:`\forall \zeta \in C_L: \text{inv}(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. Let :math:`n = \Lambda(\zeta)`. By :ref:`Definition 2.1.4 <definition-2-1-4>`, this is the Word Length of *ζ*.  Let *s* denote the Delimitation of *ζ* as follows:

.. math::

    1. s = D\Pi_{i=1}^{n} \zeta\{i\} = (\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{n\})

By :ref:`Theorem 1.2.5 <theorem-1-2-5>`, for any two Strings *u* and *t*, :math:`inv(ut) = inv(t)inv(u)`. Apply this property repeatedly to construct *inv(s)*,

.. math::

    2. \text{inv}(s) = \text{inv}((\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{n\}))

Which reduces to,

.. math::

    3. \text{inv}(s) = (\text{inv}(\zeta\{n\}))(\text{inv}(\sigma))(\text{inv}(\zeta\{n-1\}))(\text{inv}(\sigma)) ... (\text{inv}(\zeta\{2\}))(\text{inv}(\sigma))(\text{inv}(\zeta\{1\}))

Since *σ* is a single character, :math:`\text{inv}(\sigma) = \sigma`,

.. math::

    4. \text{inv}(s) = (\text{inv}(\zeta\{n\}))(\sigma)(\text{inv}(\zeta\{n-1\}))(\sigma) ... (\sigma)(\text{inv}(\zeta\{2\}))(\sigma)(\text{inv}(\zeta\{1\}))

Note that the right-hand side now has the form of a Delimitation, but with the order of Words reversed and each Word inverted.

Re-index the terms on the right-hand side to match the form of the Delimitation definition, :ref:`Definition 1.2.7 <definition-1-2-7>`. Let :math:`j = n - i + 1`. Then, as *i* goes from 1 to *n*, *j* goes from *n* to 1,

.. math::

    5. \text{inv}(s) = (\text{inv}(ζ\{j_n\}))(\sigma)(\text{inv}(\zeta\{j_{n-1}\}))(\sigma) ... (\sigma)(\text{inv}(\zeta\{j_2\}))(\sigma)(\text{inv}(\zeta\{j_1\}))

Where *j*:sub:`i` is obtained by simply substituting :math:`j = n - i + 1`. Using :ref:`Definition 1.2.7 <definition-1-2-7>` of Delimitations, the right-hand side becomes,

.. math::

    6. \text{inv}(s) = D\Pi_{j=1}^{n} \text{inv}(\zeta\{n - j + 1\})

Recall that :math:`s = D\Pi_{i=1}^{n} \zeta\{i\}`. Substitute this back into the equation and re-index the right-hand side for consistency to get,

.. math::

    7. \text{inv}(D\Pi_{i=1}^{n} \zeta\{i\}) = D\Pi_{i=1}^{n} \text{inv}(\zeta\{n - i + 1\})

Since *ζ* was an arbitrary sentence, this can be generalized over the Corpus,

.. math::

    8. \forall \zeta \in C_L: \text{inv}(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\}) 

∎

As noted in previous aside, the condition of Invertibility is strong. While the Inverse of every Sentence is defined in the domain of Strings, an Inverse Sentence does not necessarily belong to the Corpus of its uninverted form. Therefore, when a Sentence is Invertible, it will exhibit syntactical symmetries at not just the Character level, but also at the individual Word level. Before moving onto to the last batch of theorems in this section, a digression into their motivation is in order, as it will help highlight the interplay of syntactic symmetries that give rise to palindromes.

Consider the Sentences from the English language, :math:`\rune{f} = \text{"this is a test"}`, :math:`\rune{u} = \text{"live on"}`, and :math:`\rune{th} = \text{"step on no pets"}`. Their corresponding Character-level representations are given by,

.. math::

    {\large\rune{f}} = (\text{"t"}, \text{"h"}, \text{"i"}, \text{"s"}, \sigma, \text{"i"}, \text{"s"}, \sigma, \text{"a"}, \sigma, \text{"t"}, \text{"e"}, \text{"s"}, \text{"t"})

.. math::

    {\large\rune{u}} = (\text{"l"}, \text{"i"}, \text{"v"}, \text{"e"}, \sigma, \text{"o"}, \text{"n"})

.. math::

    {\large\rune{th}} = (\text{"s"}, \text{"t"}, \text{"e"}, \text{"p"}, \sigma, \text{"o"}, \text{"n"}, \sigma, \text{"n"}, \text{"o"}, \sigma, \text{"p"}, \text{"e"}, \text{"t"}, \text{"s"})

The Character-level representation of their Inverses, would be,

.. math::

    {\large\text{inv}(\large\rune{f})} = (\text{"t"}, \text{"s"}, \text{"e"}, \text{"t"}, \sigma, \text{"a"}, \sigma, \text{"s"}, \text{"i"}, \sigma, \text{"s"}, \text{"i"}, \text{"h"}, \text{"t"})

.. math::

    {\large\text{inv}(\rune{u})} = (\text{"n"}, \text{"o"}, \sigma, \text{"e"}, \text{"v"}, \text{"i"}, \text{"l"})

.. math::

    {\large\text{inv}(\rune{th})} = (\text{"s"}, \text{"t"}, \text{"e"}, \text{"p"}, \sigma, \text{"o"}, \text{"n"}, \sigma, \text{"n"}, \text{"o"}, \sigma, \text{"p"}, \text{"e"}, \text{"t"}, \text{"s"})

In the case of *ᚠ*, *inv(ᚠ)* is not a Sentence in the Corpus, since none of the Words in it belong to the Language (English). Notice that the Delimiters (*σ*) still appear at the same indices in both *ᚠ* and *inv(ᚠ)*, just in reversed order. In *ᚠ*, the Delimiters are at indices 4, 7, and 9. In *inv(ᚠ)*, the Delimiters are at indices 9, 7, and 4 (counting from the ending of the reversed string). So, while the sequence of Delimiters is reversed, their positions relative to the beginning and end of the String remain the same. Since the Delimiting Algorithm identifies Words based on Delimiter positions, this means application of the algorithm to the reversed Character-level representatio results in the same delimiting of the linguistic "*entities*" (Strings) which correspond to Words, but in reversed order and inverted.

In the case of *ᚢ*, *inv(ᚢ)* belongs to the Corpus, since all of its Words belong to the Language (English) and have semantic coherence in *ᚢ*, and the inverted Sentence is admissible. This means *ᚢ* belongs to the class of Invertible Sentences in English. Take note, none of the Words that belong to *ᚢ* (or more precisely, to one of the ordered pairs of **W**:sub:`ᚢ`) belong to *inv(ᚢ)* (or more precisely, to one of the ordered pairs of **W**:sub:`inv(ᚢ)`). However, there does appear to be a relationship between the Words which appear in *ᚢ* and *inv(ᚢ)*, namely, they must be Invertible. The Word *"live"* inverts into *"evil"*, while *"on"* inverts into *"no"*. In other words, based on this preliminary heuristic analysis, if a Sentence is to be Invertible, the Words which belong to it must belong to the class of Invertible Words **I**.

In the case of *ᚦ*, a similar situation is found. Each Word in *ᚦ* is Invertible and pairs with its Inverse Word in *inv(ᚦ)*, e.g. *"pets"* and *"step"* form an Invertible pair, etc. This means, for the same reasons as *ᚢ*, *ᚦ* belongs to the class of Invertible Sentences. However, there is a symmetry embodied in *ᚦ* over and above the pairing of its constituent Words into Invertible pairs. Not only is *inv(ᚦ)* a Sentence in the Corpus, but it's equal to *ᚦ* itself. Indeed, *ᚦ* belongs to a special class of English sentences: Palindromes. 

Note, in order for the Sentence to invert, i.e. the case of *ᚢ* and *ᚦ*, the order of the Words in the inverted Sentences must be the reversed order of the inverted Words in the uninverted Sentence. In other words, the inversion defined on the String *"propagates"* up through the levels of the semantic hierarchy and manifests at each level in the form of a semantic inversion. This will be discussed in greater detail after the next theorems are established.

These last theorems encapsulate these important properties of Invertible Sentences. When Palindromes are formally defined in the next section, these theorems will be used extensively to prove the main results of this work. 

.. _theorem-2-3-9:

**Theorem 2.3.9** :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`

Let *ζ* be an arbitrary Invertible Sentence in **C**:sub:`L` for *i* such that :math:`1 \leq i \leq \Lanbda(\zeta)`. By :ref:`Definition 2.2.2 <definition-2-2-2>`, 

.. math::

    1. \text{inv}(\zeta) \in C_L.

By the :ref:`Extraction Axiom S.2 <axiom-s2>`, 

.. math::

    2. \zeta\{i\} \in L. 

By :ref:`Definition 1.3.2 <definition-1-3-2>`, a Word *α* is invertible if and only if both *α* and its inverse, *inv(α)*, are in **L**,

.. math::

    3. \alpha \in I \leftrightarrow \text{inv}(\alpha) \in L

Therefore, since **L** is closed under inversion for Invertible Words , 

.. math::

    4. \text{inv}(\zeta\{i\}) \in L.

*inv(ζ)* can be constructed by concatenating the inverses of the words in ζ in reverse order, with delimiters inserted appropriately. Since by step 1 *inv(ζ)* is a Sentence in the Corpus, **W**:sub:`inv(ζ)` can be constructed by the Delimiting Algorithm (:ref:`Definition 2.1.3 <definition-2-1-3>`). 

.. math::

    5. W_{\text{inv}(\zeta)} = (\text{inv}(\zeta\{\Lambda(\zeta)\}), \text{inv}(\zeta{\Lambda(\zeta)-1\}), ..., \text{inv}(\zeta\{1\}))

By :ref:`Definition 2.1.9 <definition-2-1-9>`, 

.. math::

    6. \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta)-i+1\})

Since *ζ* and *i* were arbitrary, this can be generalized over the Corpus,

.. math::

    1. forall \zeta \in C_L: \zeta \in K \leftarrow \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\}) 

∎

A brief interjection is necessary to discuss the significance of :ref:`Theorem 2.3.9 <theorem-2-3-9>`. The result shown in :ref:`Theorem 2.3.9 <theorem-2-3-9>` is a direct result of the *"propagation of inversion"* mentioned in the introduction to this subsection.

As :ref:`Theorem 1.3.1 <theorem-1-3-1>` showed, :ref:`Definition 1.3.1 <definition-1-3-1>` of Reflective Words is equivalent to a definition that simply requires *α* satisfy the String equality relation, 

.. math::

    \alpha = \text{inv}(\alpha)

Another way of stating this is through logical equivalence, as :ref:`Theorem 1.3.2 <theorem-1-3-2>` shows,

.. math::

    \alpha \in L \leftrightarrow \text{inv}(\alpha) \in L
    
In turn, :ref:`Definition 1.2.4 <definition-1-2-4>` of String Inversion states in order for this to be the case, it must also be the case its Character satisfy,

.. math::

    \alpha[i] = \alpha[l(\alpha) - i + 1] 

In other words, a Word is its own Inverse exactly when its Characters are in inverted orders. 

In a similar fashion, as :ref:`Theorem 2.3.5 <theorem-2-3-5>` and :ref:`Theorem 2.3.6 <theorem-2-3-6>` demonstrate by way of syllogism, a Sentence in a Corpus is invertible if its Inverse belongs to the Corpus,

.. math::

    \zeta \in C_L \leftrightarrow \text{inv}(\zeta) \in C_L

:ref:`Theorem 2.3.9 <theorem-2-3-9>` *"propagates"* the Character-level symmetries up through the Words in the Sentence, by stating the Words in an invertible Sentence must be inverted Words of the Sentence in reversed order,

.. math::

    \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})

An imporant note to make is the *direction* of the implication in :ref:`Theorem 2.3.9 <theorem-2-3-9>` . A bidirectional equivalence would allow one to infer from the above equation that a Sentence is invertible. However, the direction of :ref:`Theorem 2.3.9 <theorem-2-3-9>`  cannot be strengthened, as the following :ref:`Theorem 2.3.10 <theorem-2-3-10>` makes clear.

:ref:`Theorem 2.3.10 <theorem-2-3-10>` also makes clear why :ref:`Definition 2.3.1 <definition-2-3-1>` of Admissible Sentence of Word Length *n* is essential to understanding invertibility. 

.. _theorem-2-3-10:

**Theorem 2.3.10** :math:`\forall \zeta \in C_L: \zeta \in K \leftrightarrow (\forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})) \land (\text{inv}(\zeta) \in A(\Lambda(\zeta)))`

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus C:sub:`L`, *ζ* is invertible if and only if Words are inverted order and its Inverse is admissible.

(→) Let ζ be an arbitrary Invertible Sentence in C:sub:`L`,

.. math::

    1. \zeta \in K

By :ref:`Theorem 2.3.9 <theorem-2-3-9>`, the *i*:sup:`th` Word of *inv(ζ)* is the inverse of the *(Λ(ζ) - i + 1)*:sup:`th` Word of *ζ*

.. math::

    2. \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
   
Furthermore, by :ref:`Theorem 2.3.3 <theorem-2-3-3>`, since *inv(ζ)* is in the Corpus, *inv(ζ)* is an Admissible Sentence of word length *Λ(ζ)*.

.. math::

    3. \zeta \in A(\Lambda(\zeta))

Since :math:`\zeta \in K`, by :ref:`Definition 2.3.2 <definition-2-3-2>`, 

.. math::

    4. \text{inv}(\zeta) \in C_L.

By :ref:`Theorem 2.3.8 <theorem-2-3-8>`, the inverse of *ζ*, *inv(ζ)*, can be expressed as the Delimitation of the inverses of the Words of *ζ* in reverse order,

.. math::

    5. \text{inv}(\zeta) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})

This is equivalent to,

.. math::

    6. \text{inv}(\zeta) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta)\{i\}

Since :math:`\text{inv}(\zeta) \in C_L` by assumption (step 1) and *inv(ζ)* has the same Word Length as *ζ* which is *Λ(ζ)*. 

Because *inv(ζ)* is a Delimitation of Words from **L**, by :ref:`Definition 2.3.1 <definition-2-3-1>`, it follows that,

.. math::

    7. \text{inv}(\zeta) \in A(\Lambda(\zeta)).

Therefore, both conditions hold, 

.. math::

    8. \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
    
.. math::

    9. \text{inv}(\zeta) \in A(\Lambda(\zeta))

(←) Assume that for an arbitrary Sentence :math:`\zeta \in C_L`, the following holds,

.. math::

    10. \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
    
.. math::

    11. \text{inv}(\zeta) \in A(\Lambda(\zeta))


By :ref:`Definition 2.3.1 <definition-2-3-1>`, since :math:`\text{inv}(\zeta) \in A(\Lambda(\zeta))`, it follows immediately, 

.. math::

    12. \text{inv}(\zeta) \in C_L

By :ref:`Definition 2.3.2 <definition-2-3-2>`, it follows, 

.. math::

    13. \zeta \in K

Therefore, both directions of the equivalence have been shown. Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus, 

.. math::

    \forall \zeta \in C_L: \zeta \in K \leftrightarrow (\forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})) \land (\text{inv}(\zeta) \in A(\Lambda(\zeta)))

∎

Just as the notion of Word Length introduced a dimension of *"semanticality"* to the formal system, so too does the notion of an Admissible Sentence introduce a dimension of *"grammaticality"*. :ref:`Theorem 2.3.10 <theorem-2-3-10>` takes no stance on what constitutes an Admissible Sentence, what sort of grammatical forms and structures might define this notion, except to say it must be the result of a Delimitation of Words that belongs to the Corpus. 

The significance of :ref:`Theorem 2.3.10 <theorem-2-3-10>` is the additional syntactical constraint that is imposed over and above *admissibility* onto a Corpus when a Sentence under goes inversion. Not only must the Inverse Sentence possess *admissibility*, the pre-cursor to *grammaticality*, but it must also display Word-level symmetry. This is definitively confirmed by :ref:`Theorem 2.3.11 <theorem-2-3-11>`.

.. _theorem-2-3-11:

**Theorem 2.3.11** :math:`\forall \zeta \in C_L: \zeta \in K \to \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I`

This theorem can be stated in natural language as follows: For every Invertible Sentence *ζ* in the Corpus **C**:sub:`L`, every Word in *ζ* is an Invertible Word.

Let *ζ* be an arbitrary Invertible Sentence in C:sub:`L`, and let *i* be a natural number such that :math:`1 \leq i \leq \Lambda(\zeta)`. Since :math:`\zeta \in K`, by :ref:`Definition 2.3.2 <definition-2-3-2>`, 

.. math::

    1. \text{inv}(\zeta) \in C_L

By :ref:`Definition 2.1.5 <definition-2-1-5>`, *ζ{i}* refers to the Word at index *i* in the Word-level representation of *ζ*. By :ref:`Theorem 2.3.9 <theorem-2-3-9>`,

.. math:: 

    2. \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})

By the :ref:`Extraction Axiom S.2 <axiom-s2>`, since :math:`\zeta \in C_L`, all Words in its Word-level representation belong to **L**. Therefore, :math:`\zeta\{i\} \in L` for all *i* such that :math:`1 \leq i \leq \Lambda(\zeta)`.

Since :math:`\text{inv}(\zeta) \in C_L` (from step 1) and each word *inv(ζ){i}* is the inverse of a word in ζ (from step 2), by :ref:`Extraction Axiom S.2 <axiom-s2>`, all the Words in the Word-level representation of *inv(ζ)* belong to L,

.. math::

    3. \text{inv}(\zeta)\{i\} \in L

By :ref:`Definition 1.3.2 <definition-1-3-2>` of Invertible Words, this means that *ζ{i}* is an Invertible Word. Therefore, :math:`\zeta\{i\} \in I`. Since *ζ* and *i* were arbitrary, this can generalize, 

.. math::

    \forall \zeta \in C_L: \zeta \in K \leftrightarrow \forall i \in N_{\Lambda(\zeta)}`: \zeta\{i\} \in I 
 
∎

The contrapositive of :ref:`Theorem 2.3.11 <theorem-2-3-11>` provides a schema for searching for Invertible Sentences. If any of Words in a Sentence are not Invertible, then the Ssentence is not Invertible. In other words, it suffices to find a single word in a Sentence that is not Invertible to show the entire Sentence is not Invertible.