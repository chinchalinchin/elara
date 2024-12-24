======================
Palindromic Structures
======================

.. warning::
    
    The paper contains the draft of formal method for analyzing palindromic structures. It is a work in progress. What follows should by no means be interpretted as a complete or consistent formal theory; it should be treated more like a very rough draft. Many of the notions need further clarification and elaboration.  
    
The goal of this paper is to introduce formal constraints the palindromes in *any* language and corpus must satisfy independently of the semantic interpretation of their constituent words and sentences. These formal constraints will in turn lead to the identification of the main structural elements of palindromes. After a language is assumed and a class of words identified, these structural elements can be used as a basis for further semantical and statistical analysis of the assumed language. 

At the outset, it must be stated the complexity of pursuing a complete theory of palindrome currently exceeds the mental capacities of the author. Palindromes are a rich and diverse linguistic species, appearing in many different shapes and sizes. Some of these guises are more amenable to analysis than others. 

This work will introduce the notions of a palindrome's core attributes: *aspect*, *parity*, *punctuality* and *case*. The first two attributes are within the scope of formal analysis. The third and fourth attributes, however, presents certain difficulties that will be more fully appreciated after the theory to describe the first two attributes has been solidifed. Suffice to say, it is the author's opinion these second two attributes of palindromes cannot be given an account unless semantic assumptions are introduced into the formal model.

To provide a overview of the theory of palindromic structures and give a general notion of what is meant by these attributes of a palindrome, consider three well-known examples,

- No devil lived on.
- Not on.
- Don't nod.

The first example is what will be termed a *perfect palindrome*. This sentence, ignoring case and punctuation, is a perfect mirror image of itself. The reversal of "no devil lived on" reads the same forwards as backwards. 

The second example is what will be termed an *imperfect palindrome*. This sentence, even ignoring the mitigations of case and punctuation, is not an *exact* mirror image of itself. The strict reversel of "not on" is "no ton". The spaces in the reversed sentence need un-scrambled in order to retrieve the semantic content. However, the reversed string is not precisely *devoid* of semantic content. The relative order of the characters is still preserved in the string; it is only the spaces which need re-arranged. 

This distinction between *perfect* and *imperfect* is termed a palindrome's *aspect*. The *aspect* denotes the type of symmetry displayed by the palindrome. This symmetry is a measure of how much semantic content is preserved under sentence reversal. 

This insight into the *aspect* of a palindrome will lead to the introduction of a linguistic operation termed *sigma reduction*. This operation will in turn lead to a formal definition of palindromes that describes their syntactical structure in terms of delimiters (spaces) and inversions (sentence reversal).

The *parity* of a palindrome is related to its *palindromic pivot*, or its point of symmetry.  In other words, a palindrome is type of sentence that has a "*center*". This "*center*" will be termed its *pivot*. The *parity* of a palindrome is determined by its length, which manifests as type of pivot that describes it symmetry. For example, the sentence "*no devil lived on*" with character length 19 reflects around the pivot of " ", the sentence's central character, whereas the sentence "*not on*" with character length 6 reflects around an empty character "" between "t" and " ". From this example, it can be seen that depending on the parity of the sentence length, the palindromic pivot will either be a character in the sentence, or an empty character that acts as a boundary between two actual characters in the sentence. 

As it will turn out, this example of parity is oversimplified, due to the complications introduced by the aspect of a palindrome. The pivot of a palindrome cannot be rigorously defined until the semantic content of a palindrome's *imperfection* is reconstituted somehow.

The third example of "*Don't nod*" demonstrates the deepening ambiguity of introducing punctuation to palindromes. The reversal of this sentence is the opaque "don t'nod" Now, in addition to the scrambling of the spaces, the reversed string must also have its punctuation re-sorted. There is no formal method known to the author of dealing with these types of ambiguities that depend entirely on the semantic interpretation of the language under consideration, such as rules of contractions. The *punctuality* of a palindrome can only be described by introducing semantics into the theory.

Similarly, the fourth attribute of palindromes, *case*, is a semantic construct that possesses no unifying syntactical properties across languages (as far as the author knows). *Case* is a semantic relationship that identifies characters in an alphabet as different manifestations of the same underlying semantic entity, i.e. "a" and "A" are the "*same*" letter. This information is not present in the syntax of a language and is an extra assumption that must be modeled accordingly.

The aim of this analysis is to develop a theory of palindromes *independent* of semantic interpretation. In other words, formalizing a theory of palindromes that describes the logical structure of their aspect and parity is the goal of the current analysis. For this reason, all complications that arise from case and punctuality are ignored. The examples that are considered only deal with sentences that are meaningful without the considerations of case or punctuations.

This restriction to *aspect* and *parity* may appear restrictive; Indeed, it may be argued by introducing this restriction to the formal theory that is about to developed, it has no application to actual language. To this argument, it should be countered the structures uncovered in this restricted subset of language must nevertheless preserve their structure when embedded into the whole of language. 
  
Section I: Defintions 
=====================

Section I.I: Strings
--------------------

The domain of discourse is composed of *Strings*. A String will be represented as follows, 

    1. String (*s*:sub:`1`, *s*:sub:`2`, *s*:sub:`3`): A lowercase English *s* with a subscript denotes a String. Sometimes the subscript will be dropped and *s* will be used. The letter *t* and *u* also reserved for Strings.

A String is regarded as a linguistic artifact that is defined by its *length*, its *Characters* and their *ordering*. It is assumed if one knows how many Characters are in a String, which Characters are in a String and in what order they occur, then one has all the information necessary to completely determine the String. This notion is made more precise in the following sections with the introduction of several definitions.

A *Word* will be considered a *type* of String. Colloquially, a word can be understood as a String with semantic content. The goal of the analysis is to describe the necessary syntactic conditions for a String to be considered a formal Word, without taking into account the semantic content that is assigned to through everyday use. In other words, the analysis assumes Words have already been selected from the set of all possible Strings and assigned interpretations. 

Characters
^^^^^^^^^^

A *Character* is the basic unit of a String. Characters will be represented as follows,

    1. Characters (*𝔞*, *𝔟*,  *𝔠*, etc. ): Lowercase Fraktur letters represent Characters. Subscripts will occassionally be used in conjunction with Fraktur letters to denote Characters, (*𝔞*:sub:`1`, *𝔞*:sub:`2`, ... ). 
    2. Empty (*ε*): The lowercase Greek letter epsilon, *ε*, represents the Empty Character.
    3. Delimiter (*σ*): The lowercase Greek letter sigma, *σ*, represents the Delimiter Character. 

In the case of English, Characters would correspond to letters such as "a", "b", "c", etc., the Empty Character would correspond to the null letter, "", and the Delimiter Character would correpond to the blank letter, " ".

The aggregate of all Characters is called an *Alphabet* and is denoted by an uppercase Sigma, **Σ**,

    Σ = { *ε*, *σ*, *𝔞*, *𝔟*,  *𝔠*, ... }

The number of elements in an Alphabet is denoted | Σ |. In general, throughout the course of this work, the cardinality of a set **A** will be denoted | A |. 

It will sometimes be necessary to refer to indeterminate Characters, so notation is introduced for Character Variables,

    4. Character Variables (*ⲁ*, *ⲃ*, *ⲅ*, etc. ): Lowercase Coptic letters will represent Character Variables, i.e. indeterminate Characters. Subscripts will occassionally be used with Coptic letters to denote Word Variables, (*ⲁ*:sub:`1`, *ⲁ*:sub:`2`, ... )

Concatenation 
^^^^^^^^^^^^^

Concatenation is considered the sole constitutive operation for the formation of Strings. It is taken as a primitive operation, but not an elementary operation. By this it is meant the notion of concatenation that is about to be adopted does not define concatenation solely in terms of Strings. Concatenation will be defined as a hetergeneous operation that is performed between Characters in Alphabet and Strings.

**Definition 1.1.1: Concatenation**  The result of *concatenating* any two Characters *ⲁ* and *ⲃ** is denoted *ⲁⲃ*. To make the operands of concatenation clear, parentheis will sometimes be used to separate the Characters being concatenated, *ⲁ(ⲃ) = (ⲁ)ⲃ = ⲁⲃ*.

Colloquially, *ⲁ* is the String that results from placing *ⲃ* behind *ⲁ*. More formally, Character concatenation is defined inductively through the following schema,

    1. Basis Clause: ∀ ⲁ ∈ Σ: ⲁε = ⲁ
    2. Inductive Clause: ∀ ⲁ, ⲃ, ⲅ ∈ Σ: ⲁ(ⲃⲅ) = (ⲁⲃ)ⲅ
    3. Comprehension Clause: ∀ ⲁ ∈ Σ, ∀ s ∈ S: ⲁs ∈ S
    4. Uniqueness Clause: ∀ ⲁ, ⲃ, ⲅ, ⲇ ∈ Σ: (ⲁⲃ = ⲅⲇ) → ((ⲁ = ⲅ) ∧ (ⲃ = ⲇ))

The first clause is the basis step of induction which states any Character appended to the Empty Character is the Character itself. 

The second clause is the inductive step which allows the concatenation of Characters into Strings of arbitrary length through recursion.

It is assumed that the operation of concatenation is closed with respect to the set of all Strings **S**. In other words, concatenation will always yield a String. This assumption is captured in the Comprehension Clause of Definition 1.1.1. This clause ensures two things. First, in conjunction with the Basis Clause, it follows all singleton Characters are Strings. Second, by itself, it ensures that all results of concatenation are Strings. 

The Uniqueness Clause states that if the concatenation of two characters *ⲁ* and *ⲃ* is equal to the concatenation of two other characters *ⲅ* and *ⲇ*, then it must be the case that *ⲁ* is equal to *ⲅ* and *ⲃ* is equal to *ⲇ*. In other words, there's only one set of Characters that can form a given String through concatenation.

Concatenation as it is normally found in the fields of automata theory and regular expressions is treated as a primitive operation performed between two Strings operands. Concatenation of multiple Strings is then defined inductively.  The current formulation differs in that concatenation in this system is not conceived as the "joining" of two or more Strings. Instead, the formal system under construction treats concatenation as an elementary operation that occurs between Characters and Strings.

To make this distinction plain, it should be noted that given an Alphabet Σ and Definition 1.1.1, one still cannot say the result of a concatenation is a String, nor make any claim about the contents of **S**, the set of all Strings. The Comprehension Clause of Definition 1.1.1 only states the result of concatenating a Character with a String is a String. It says nothing at all about whether or not single Characters themselves are Strings, and thus it says nothing about whether the concatenation of single Characters is itself a String. 

In order to rectify this, the first Axiom is introduced,

**Axiom C.1: The Character Axiom**

    ∀ ⲁ ∈ Σ: ⲁ ∈ S

This Axiom states the intuitive notion that all Characters are Strings. This includes Empty Characters and Delimiter Characters. This Axiom, in conjunction with Definition 1.1.1, immediately populates the set of all Strings with an uncountably infinite domain of objects (See Theorem 1.1.1 for an informal proof of this fact) consisting of every possible combination of Characters from the Alphabet.

**Example** Let *s = 𝔞𝔟𝔠* and *t = 𝔡𝔢𝔣*. The concatenation of these two Strings *st* is written,

    st = (𝔞𝔟𝔠)(𝔡𝔢𝔣) 
    
Using the inductive clause, this concatenation can be grouped into simpler concatenations as follows,    
    
    𝔞(𝔟(𝔠(𝔡(𝔢𝔣)))) = (((((𝔞𝔟)𝔠)𝔡)𝔢)𝔣) = 𝔞𝔟𝔠𝔡𝔢𝔣

Therefore, *st = 𝔞𝔟𝔠𝔡𝔢𝔣*

Notation
^^^^^^^^

It will sometimes be convenient to represent Words and Strings as ordered sets of Characters, rather than serialized concatenations of Characters. The two formulations are equivalent, but the set representation has advantages when it comes to quantification and symbolic logic. When a String or Word representation is intended to be interpretted as a set, it will be written in bold uppercase letters. For example, the String represented as the concatenated series *s_1* = *𝔞𝔟𝔠* would be represented in this formulation as a set of ordered pairs **S_1**, where the first coordinate encodes the position of the Character in the String,

    **S_1** = { (1, *𝔞*), (2, *𝔟*), (3, *𝔠*) }

Note, since sets do not preserve order, this would be equivalent to,

    { (3, *𝔠*), (2, *𝔟*), (1, *𝔞*) }

To simplify notation, it is sometimes beneficial to represent this set as a sequence that *does* preserve order as,

    **S_1** = (*𝔞*, *𝔟*, *𝔠*) 

This notation will be employed extensively in the subsequent proofs.

Length
^^^^^^

The Empty Character *ε* will be necessary for defining the *pivot point* of a palindrome. While this addition to the Alphabet **Σ** is advantegous from the perspective of palindromic analysis, it presents a problem when defining the length of a String *s*. If *ε* is considered part of the Alphabet, the typical notion of a String's length is undefined, as *ε* can be concatenated an infinite number of times to *s* without altering its content. To explicate the notion of *length*, consider the constraints that must be placed on this concept in the palindromic system,

    - The length of the string "abc" is 3, as it contains three non-empty characters.
    - The length of the string "aεbεc" is still 3, as the empty characters (ε) are not counted.

This example motivates the following definition.

**Definition 1.1.2** The *length* of a String *t*, denoted *l(t)*, is defined as the number of non-Empty Characters in the sequence of concatenated Characters that make up the String. 

Let *ⲁ* be a character in the String *t*. Recall *t* has an equivalent set representation **T**,

    T = { (1, ⲁ:sub:`1``), (2, ⲁ:sub:`2`), ..., (l(t), ⲁ:sub:`l(t)`) }

Let **N**:sub:`t` be the set, 

    N:sub:`t`= { 1, 2, ... , l(t) }

Formally, we define the length of *t* to be cardinality of the set **E**:sub:`t` where **E**:sub:`t` satisfies the formula,

    (j, ⲁ) ∈ E:sub:`t` ↔ (∃i ∈ N:sub:`t`: ( (i, ⲁ) ∈ T) ∧ (ⲁ ≠ ε) ∧ (j = i) )

With this definition, the length of String in the formalization can be defined as,

    l(t) = | E:sub:`t` |

Note the E:sub:`t` is a set of *ordered pairs*, not a set of Characters. This allows for repeated Characters to be counted in a String's length.

**Example** t = "aabbcc"

The set representation of *t* is given by,

    T = { (1, a), (2, a), (3, b), (4, b), (5, c), (6, c) }.

By Definition 1.1.2, 

    E:sub:`t` = { (1, a), (2, a), (3, b), (4, b), (5, c), (6, c) }

Therefore, 

    | E:sub:`t` | = 6

This formulization, while perhaps prosaic, maps to the intuitive notion of a String's length, i.e. the number of non-empty Characters, while still allowing for a calculus of concatenation that involves Empty Characters.

Containment
^^^^^^^^^^^

Similar to the explication of *length*, the notion of a String *containing* another String must be made precise using the definitions introduced so far. It's important to note that in the current system the relation of *containment* is materially different from the standard subset relation between sets. For example, the set of characters in "rat" is a subset of the set of characters in "tart," but "rat" is not contained in "tart" because the order of the characters is different.

Consider the words "rat" and "strata". The word "rat" *is contained* in the word "strata", because the order of the string "rat" is preserved in "strata". An intuitive way of capturing this relationship is to map the indices of the Characters in "rat" to the indices of the Characters in "strata" which correspond to the indices in "rat". A cursory (but incorrect) definition of *containment* can then be attempted,

**Containment (Incorrect Version)** α ⊂:sub:`s` β

Let *α* and *β* be words represented as the sets of ordered pairs, *Α* and *Β*,

    Α = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ..., (l(α), 𝔞:sub:`l(α)`) }

    Β = { (1, 𝔟:sub:`1`), (2, 𝔟:sub:`2`), ..., (l(β), 𝔟:sub:`l(β)`) }

*α* is said to be *contained in β*, denoted by,

    α ⊂:sub:`s` β
    
If and only if there exists a strictly increasing function *f*: **N**:sub:`α` *→* **N**:sub:`β` such that:

    ∀ i ∈ N:`α`: a:sub:`i` = b:sub:`f(i)`

This definition essentially states that *α* is contained in *β* if there's a way to map the Characters of *α* onto a subsequence of the Characters in *β* while preserving their order. The function f** ensures that the Characters in *α* appear in the same order within *β*. While this definition is incorrect, the reason why this version of *containment* fails is instructive in developing better understanding of the subtlety involved in attempting its definition. 

First, consider an example where this definition correlates with the intuitive notion of *containment*. Let *α = "rat"* and *β = "strata"*. Then, these words can be represented in set notation as,

    Α = { (1, r), (2, a), (3, t) }
     
    Β = { (1, s), (2, t), (3, r), (4, a), (5, t), (6, a) }.

The function *f* defined as *f(1) = 3*, *f(2) = 4*, and *f(3) = 5* satisfies the condition in the proposed definition, as it maps the characters of "rat" onto the subsequence "rat" within "strata" while preserving their order. In addition, *f* is a strictly increasing function. Therefore, 

    "rat" ⊂:sub:`s` "strata".

Next, consider a counter-example. Let *α* = "bow" and *β* = "borrow". Then their corresponding set representations are given by,

    Α = { (1, b), (2, o), (3, w) }
     
    Β = { (1, b), (2, o), (3, r), (4, r), (5, o), (6, w) }

The function defined through *f(1) = 1*, *f(2) = 5* and  *f(3) = 6* satisfies the conditions of the proposed definition. However, intuitively, "bow" is *not contained* in the word "borrow". The reason the proposed definition has failed is now clear: the function *f* that is mapping "bow" to "borrow" skips over the indices 2, 3 and 4 in "borrow". In other words, in addition to being strictly increasing, the function *f* which maps the smaller word onto the larger word must also be *consecutive*. This insight can be incorporated into the definition of *containment* by first defining the notion of *consecutive*,

**Definition 1.1.3: Consecutive Functions** 

A function *f* is consecutive if it satisfies the formula,

    ∀ i, j ∈ N:sub:`α``:  (i < j) →  f(j) = f(i) + (j - i).  
    
This additional constraint on *f* ensures that the indices of the larger word in the containment relation are mapped in a sequential, unbroken order to the indices of the smaller word. This definition of *Consecutive Functions* can be immediately utilized to refine the notion of *containment*.

**Definition 1.1.4: Containment** α ⊂:sub:`s` β

Let *α* and *β* be words represented as the sets of ordered pairs *Α* and *Β*:

    Α = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ..., (l(α), 𝔞:sub:`l(α)`) }

    Β = { (1, 𝔟:sub:`1`), (2, 𝔟:sub:`2`), ..., (l(β), 𝔟:sub:`l(β)`) }

*α* is said to be *contained in β*, denoted by,

    α ⊂:sub:`s` β

If and only if there exists a strictly *increasing and consecutive* function *f*: **N**:sub:`α` *→* **N**:sub:`β` such that:

    ∀ i ∈ N:sub:`l(α)`: 𝔞:sub:`i` = 𝔟:sub:`f(i)`

The notion of containment will be central to developing the logic of palindromic structures in the subsequent sections.

Cardinality
^^^^^^^^^^^

The set of all Strings is denoted **S**. The cardinality of **S** is denoted | S |.

It is assumed **S** is at least uncountably infinite. A rigorous proof of this fact would carry the current work too far into the realm of real analysis, but as motivation for this assumption, an informal proof is presented below based on Cantor's famous Diagonalization argument. 

**Theorem 1.1.1** | S | ≥ ℵ:sub:`1`

Assume, for the sake of contradiction, that the set of all Strings **S** is countable. This means the Strings can be listed in some order, 

    s:sub:`1`, s:sub:`2`, s:sub:`3`, etc.

Now, construct a new String *t* as follows:

    1. The first character of *t* is different from the first character of *s*:sub:`1`.
    2. The second character of *t* is different from the second character of *s*:sub:`2`.
    3. etc.

This string *t* will be different from every string in **S** contradicting the assumption that it was possible to list all strings. Therefore, **S** must be uncountable. ∎ 

Section I.II: Words
-------------------

While the notion of Characters maps almost exactly to the intuitive notion of letters in everyday use, the notion of a *Word* requires explication. 

If Characters are mapped to letters in the Alphabet of a *Language* **L**, the set of all Strings would have as a subset the Language that is constructed through the Alphabet.  The goal of this section is to introduce a series of constraints onto the set of all Strings that will filter out its elements that cannot belong to **L** based solely on their internal structure. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations. In other words, this analysis will proceed without assuming anything about the interpretation of the Words in the Language beyond the fact that they *are* Words of the Language.

To formalize these notion, the following symbolic representations are introduced, 

    1. Words (*a*, *b*, *c*, etc.): Lowercase English letters represent Words. Subscripts will occassionally be used to denote Words, (*a*:sub:`1`, *a*:sub:`2`, ... )
    2. Language (**L**): The uppercase English letter *L* in boldface represents a Language.

In the case of English, Words would correspond to words such as "dog", "cat", etc. A Language would correspond to a set of words such as *{ "dog", "cat", "hamster", ... }* or *{ "tree", "flower", "grass", .... }*.

The number of Words in a Language is denoted | L |. 

It will sometimes be necessary to refer to indeterminate Words, so notation is introduced for Word Variables,

    1. Word Variables (*α*, *β*, *γ*, etc. ): Lowercase Greek letters will represent variable words, i.e. indeterminate Words. Subscripts will occassionally be used to denote Word Variables, (*α*:sub:`1`, *α*:sub:`2`, ... ). The exceptions to this rule are *ζ* and *ξ*which are reserved for Sentential Variables (see Section II.I for more information.), *σ* which is used for the Delimiter Character (see Section I.I for more information), and δ which is used for the Delimiter count function (see Section II.IV for more information)

The range of a Word Variable is understood to be the Language **L** from the Words are being drawn. 

With these definitions, the hierarchy of relationships that exist between a word *α*, its Language **L** and the set of all Strings **S** are given by,

    1. α ∈ L
    2. α ∈ S
    3. L ⊂ S

Axioms
^^^^^^

The goal of the current analysis is to leave the semantic interpretation of Words in a Language as ambiguous as possible. This ambiguity, it is hoped, will leave the results of the analysis applicable to palindromic structures in a variety of languages. This section details the minimal *necessary* assumptions that are placed on any String to be considered an element of a Language **L**, i.e. a Word. The axioms listed in this section are not *sufficient*; in other words, it is possible for a String to satisfy these axioms without being an element of a Language, but any Word that belongs to a Language must satisfy the axioms.

Let **L** be a Language. Let *s* be a String, not necessarily a member of **L**. Let *𝔞*:sub:`i` be the *i*:sup:`th` Character of the String *s*. Let *l(s)* be the length of *s*. Let *N*:sub:`s` be the set,

    { 1, 2, ... , l(s) }

**Axiom W.1: The Delimiter Axiom ** 

    ∀ s ∈ S: s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ σ )

**Axiom W.2: The Empty Axiom**

    ∀ s ∈ S: s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ ε )

In essence, these Axioms capture the common-sense notion that a Word from a Language cannot contain either a Delimiter or an Empty Character. The Empty Axiom, in particular, guarantees Words from a Language cannot contain "*null*" contentment. This is proved in the next theorem.

**Theorem 1.2.1** ∀ α ∈ L, ∀ t ∈ S: ¬[ (t = ε) ∧ (t ⊂:sub:`s` α) ]

In natural language, this theorem can be stated as follows: No Empty Character belongs to a Word in a Language. 

By the Character Axiom C.1, a String exists that is equal to the Empty Character. Therefore, the truth of the negated conjunction in the theorem depends on the second conjunct, *t ⊂*:sub:`s` *α*

Let String *t = ε*. Assume, for the sake of contradiction, a Word *α* exists in Language **L** such that,

    1. t ⊂:sub:`s` α 

Note, by Definition 1.1.2, 

    2. l(t) = 0

Therefore, **N**:sub:`l(t)` *= ∅*. Now, applying Definition 1.1.4, 

    3. ∀ i ∈ N:sub:`l(t)`: 𝔞:sub:`i` = 𝔟:sub:`f(i)`

Where 𝔞:sub:`i` represents the Characters in *t*, 𝔟:sub:`f(i)` represents the Characters in *α*, and *f(i)* represents the function that maps the Character indices of *t* onto the Character indices of *α*. It is a tautology of set theory that nothing can belong to the empty,

    ∀ x: x ∉ ∅

From this, it follows that no *i* exists that satisfies this formula. Therefore, no function *f(i)* exists that maps the Empty Character to a Character in *α*. But this contradicts the assumption in step 1, since by Definition 1.1.4, in order for a Word to be contained in another Word, a strictly increasing and consecutive function must exist to map the Characters. 

Since *t = ε* exists by Axiom C.1, it follows t ⊂:sub:`s` α must be false. Therefore,

    t = ε ∧ t ⊂:sub:`s` α

must always be false, and its negation must always be true. ∎

(TODO: If it can be proved the empty character is not contained in any word, is it necessary to introduce the Empty Axiom? Seems unnecessary. In fact, the Empty Axiom can probably be proven using Theorem 1.2.1. I need to see to review and see if the Empty Axiom is used anywhere, and then see if I can prove the Empty Axiom as a Theorem. If so, replace all references to the Empty Axiom with its theorem version.) 

Additional axioms will be introduced in the natural progression of this work as the hierarchy of palindromic structure is codified. 

Inversion
^^^^^^^^^

Informally, the *Inverse* of a String is the reversed sequence of Characters in a String. The goal of this section is to define this notion precisely. In the process, the motivation for this definition will be elucidated. 

**Definition 1.2.1: String Inversion** Let *s* be a string with length *l(s)*. Let *𝔞*:sub:`i` be the *i*:sup:`th` character of the String *s*. Let **N**:sub:`s` be the set,

    { 1, 2, ... , l(s) }

Then, let *t* be a String with length *l(t)* and let *𝔟*:sub:`j` be the *j*:sup:`th` character of the String *t*. Let **N**:sub:`t` be the set,

    { 1, 2, ... , l(t)}. 
    
*t* is called the Inverse of *s* and is denoted *inv(s)* if it satisfies the following conditions, 

    1. l(t) = l(s) 
    2. ∀ i ∈ N:sub:`s`, j ∈ N:sub:`t`: [ ( j = l(s) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]

Since every Word is a String, the Inverse of Word is similarly defined, with the additional constraint that *s* belong to a Language **L**. The Inverse of a Word is easily understood through a few illustrative examples in English. The following table lists some words in English and their Inverses,

| Word | Inverse | 
| ---- | ------- |
| time | emit    |
| saw  | was     |
| raw  | war     |
| dog  | god     |
| pool | loop    |

However, this particular example is (intentionally) misleading. In this example, the Inverse of a word in English is also a word in English. In general, this property is not exhibited by the majority of words in any Language. In other words, every Word in an Language has an Inverse, but not every Inverse Word belongs to a Language. This phenomenon is exemplified in the following table,

| Word | Inverse | 
| ---- | ------- |
| cat  | x       |
| you  | x       |
| help | x       |
| door | x       |
| book | x       |

It should be clear the intent is to define a class of Words whose constituents belong to a class of *Invertible Words* if and only if their Inverse exists in the Language. As a first step towards this definition, String Inversion was introduced and formalized. In the next section, String Inversion will provide a subdomain in the domain of discourse over which to quantify the conditions that are to be imposed on the class of *Invertible Words*, i.e. the class of Words whose Inverses are also Words. 

Before defining the class of Invertible Words in the next section, this section is concluded with a theorem that strengthens the definition of String Inversion. This theorem will be used extensively in the subsequent sections.

**Theorem 1.2.2** *inv(inv(s)) = s*

Let *s* be a String with length *l(s)* and Characters *𝔞*:sub:`i`. Let **N**:sub:`s` be the set,

    { 1, 2, ... , l(s) }

Let *t = inv(s)* with length *l(t)* and Characters *𝔟*:sub:`j`. Let **N**:sub:`t` be the set,

    { 1, 2, ... , l(t) }

By the Definition 1.2.1,

    1. l(t) = l(s)
    2. ∀ i ∈ N:sub:`s`, ∀ j ∈ N:sub:`t`: [ (j = l(s) - i + 1) →  ( 𝔟:sub:`j` = *𝔞*:sub:`i` ) ]

Now, let *u = inv(t)* with length *l(u)* and Characters *𝔠*:sub:`k`. Let **N**:sub:`u` be the set,

    { 1, 2, ... , l(u) }

Applying Definition 1.2.1 again,

    3. l(u) = l(t)
    4. ∀ j ∈ N:sub:`t`, ∀ k ∈ N:sub:`u`: [ (k = l(t) - j + 1) → ( 𝔠:sub:`k` = 𝔟:sub:`j` ) ] 
 
Since *l(t) = l(s)* (step 1) and **N**:sub:`t` *=* **N**:sub:`s` (by definition of natural numbers), these substitions may be made in step 4,

    5. ∀ i ∈ N:sub:`s`, ∀ k ∈ N:sub:`u`: [ ( k = l(s) - (l(s) - i + 1) + 1 )  → ( 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` ) ]

The index *k* may be simplified,

    6. k = l(s) - l(s) + i - 1 + 1 = i

Therefore,
    
    7. ∀ i ∈ N:sub:`s`, ∀ k ∈ N:sub:`u`: [ ( k = i)  → ( 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` ) ]

This may be rewritten, noting the condition *k = i*,

    8. ∀ i ∈ N:sub:`s``: 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` ) 

Now, substitute the definition of *𝔟*:sub:`j` from step 2 (where *j = l(s) - i + 1*) into the equation for  *𝔠*:sub:`k`,

    9. ∀ i ∈ N:sub:`s``: 𝔠:sub:`k` = 𝔞:sub:`i` 

Since *u* and *s* have the same length (*l(u) = l(t) = l(s)*) and the same characters in the same order (𝔠:sub:`k` = 𝔞:sub:`i`  for all i), it can be concluded that *u = s*. Recall that *u = inv(t)* and *t = inv(s)*.  Substituting, the desired result is obtained, *inv(inv(s)) = s*. ∎ 

Concatenation
^^^^^^^^^^^^^

Concatenation was defined in Definition 1.1.1 in terms of Characters and Strings. Every word is a String and every String has a Character-level set representation, so the operation of concatenation will not be materially altered to accomodate Words. However, as the analysis builds toward soldifying a theory of palindromes, the result of this essential operation will be given a slightly different formal representation. This representation will not change the operation in any way, but will instead enable a more descriptive theory to emerge when the concept of a Pairing Language is introduced.

Let *α* and *β* be two words with the following set representations:

    Α = { (1,  𝔞:sub:`1`), (2,  𝔞:sub:`2`), ... , (n,  𝔞:sub:`n`) }

    Β = { (1, 𝔟:sub:`1``), (2, 𝔟:sub:`2`), ... , (m, 𝔟:sub:`m`)}

Here *n* and *m* are the *cardinalities* of the set representations of **Α** and **Β**, | Α | and | Β | respectively. In other words, *n* and *m* are not the String lengths, *l(α)* and *l(β)*. Definition 1.1.2, where length was formalized in the current system, excluded the Empty character from its calculation in order to ensure the infinite concatenation of an Empty Character does not alter the content of Word. This slight deviation from the notion of length requires special care when formulating the definition of Word concatenation. 

By Definition 1.1.1, the concatenation of *α* and *β*, denoted by *αβ*, is the word *γ* formed by appending the characters of *β* to the end of *α*. Formally, the set representation of γ is given by,

    γ = { (1, 𝔞:sub:`i`), (2,  𝔞:sub:`i`), ..., (n,  𝔞:sub:`n`), (n + 1, 𝔟:sub:`1`), (n + 2, 𝔟:sub:`2`), ..., (n + m, 𝔟:sub:`m`)}

Section I.III: Word Classes 
---------------------------

It will be necessary to define special classes of Words in a Language to properly describe the Language's palindromic structure. These classes, especially the class of Invertible Words, will be used extensively in the next sections.

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

From this list, it should be clear what is meant by the notion of *reflective*: Reflective Words are Words that are unchanged by a String Inversion. This property will be formally defined as follows.

**Definition 1.3.1: Reflective Words** 

Let *α* be any word from Language **L**. Let *𝔞*:sub:`i` be the *i*:sup:`th` Character in *α*. Let *l(α)* be the length of *α*. Let **N**:sub:`α` be the set,

    { 1, 2, ... , l(α) }

Then the set of Reflective Words **R** is defined as the set of *α* which satisfy the open formula,

    α ∈ R ↔ [ ∀ i ∈ N:sub:`α`:  𝔞:sub:`i` = 𝔞:sub:`l(α) - i` ]

A Word *α* will be referred to *reflective* if it belongs to the class of Reflective Words. 

The following theorem is an immediate consequence of this definition.

**Theorem 1.3.1** α ∈ R ↔ α = inv(α)

In natural language, this theorem can be stated as: A Word is Reflective if and only if it is its own Inverse.

(→)  Assume *α ∈ R*. Let *𝔞*:sub:`i` be the Characters in *α*. By Definition 1.3.1, 

    1. ∀ i ∈ N:sub:`α`: 𝔞:sub:`i` = 𝔞:sub:`l(α) - i`

Let *β = inv(α)*. Let 𝔟:sub:`j` be the Characters in *β*. By the Definition 1.2.1,

    2. l(β) = l(α)
    3. ∀ i ∈ N:sub:`α`, ∀ j ∈ N:sub:`β`: [ ( j = l(α) - i + 1 ) →  ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]
   
Substitute *j = l(α) - i + 1* into the equation from step 3 and remove the quantifiation over *j*:

    4. ∀ i ∈ N:sub:`α`: 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`i`

Now, use the property of Reflective Words from step 1 (𝔞:sub:`i` = 𝔞:sub:`l(α) - i` ) and substitute it into the equation from step 4:

    5.  4. ∀ i ∈ N:sub:`α`: 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`

Note that the index on the left side of this equation (l(α) - i + 1) corresponds to the character at position *i* in the reversed string β.  This is because the index *j* in the definition of String Inversion maps to the *l(α) - i + 1*:sup:`th`` position in the original string.

Since 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`for all i ∈ N:sub:`α`, and both strings have the same length, we can conclude that each character in *α* is equal to the corresponding character in β. Therefore the desired result is obtained: *α = β = inv(α)*

(←) Assume α = inv(α)

Let *𝔞*:sub:`i` be the Characters in *α* and let *𝔟*:sub:`j` be the Characters in *inv(α)*. By definition of String Inversion,

    1. l(α) = l(inv(α))
    2. ∀ i ∈ N:sub:`α`, ∀ j ∈ N:sub:`inv(α)`: [ ( j = l(α) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]

Since *α = inv(α)*, 𝔞:sub:`j` can be substituted for 𝔟:sub:`j` in the step 2,

    3. ∀ i ∈ N:sub:`α`, ∀ j ∈ N:sub:`inv(α)`: [ ( j = l(α) - i + 1 ) → ( 𝔞:sub:`j` = 𝔞:sub:`i` ) ]

Since the conditional inside of the quantification is only true when *j = l(α) - i + 1*, *j* can be substituted into the consequent of the conditional and the quantification over *j* can be dropped. Therefore, step 3 can be rewritten as,

    4. ∀ i ∈ N:sub:`α`: 𝔞:sub:`l(α) - i + 1` =  𝔞:sub:`i`

Similar to the previous part of the proof, the index on the left side (*l(α) - i + 1*) corresponds to the Character at position *i* in the reversed string, which is *α* itself in this case. Therefore, 

    5. ∀ i ∈ N:sub:`α`: 𝔞:sub:`i` =  𝔞:sub:`a<sub>l(α) - i`

This condition satisfies the definition of Reflective Words, so *α ∈ R*. ∎ 

Invertible Words 
^^^^^^^^^^^^^^^^

As discussed previously, the concept of *Invertible* is exemplified in the pair of English words "*time*" and "*emit*". An *Invertible Word* is a Word whose inverse is part of the same Language **L**. This notion can now be made more precise with the terminology introduced in prior sections.

**Definition 1.3.2: Invertible Words** Let *α* be any Word in a Language **L**. Then the set of Invertible Words **I** is defined as the set of α which satisfy the open formula,

    α ∈ I ↔ inv(*α*) ∈ L 

A Word *α* will be referred to as *invertible* if it belongs to the class of Invertible Words.

This definition is immediately employed to derive the following theorems,

**Theorem 1.3.2** α ∈ I ↔ inv(α) ∈ I

Assume *α ∈ I*. By Definition 1.3.2,

    1. inv(α) ∈ L
    
Consider *inv(α)*. To show that it's invertible, it must be shown,

    2. inv(inv(α)) ∈ L. 

By Theorem 1.2.2,

    3. inv(inv(α)) = α
    
Since it is known *α ∈ L*, it follows,

    4. inv(inv(α)) ∈ L  
    
By the Definition 1.3.2, 

    5. inv(α) ∈ I
    
Therefore, *inv(α)* is also an Invertible Word. ∎ 

**Theorem 1.3.3** R ⊂ I

Assume *α ∈ R*. *𝔞*:sub:`i` be the Characters in *α*. By Definition 1.3.2,

    1. ∀ i ∈ N:sub:`α`: *𝔞*:sub:`i` = *𝔞*:sub:`l(α) - i``

Let *β = inv(α)* and let *𝔟*:sub:`j` be the Characters in *β*. By Definition 1.2.1,

    2. l(β) = l(α)
    3. ∀ i ∈ N:sub:`α`, ∀ j ∈ N:sub:`β``: (j = l(α) - i + 1) →  ( 𝔟:sub:`j` = 𝔞:sub:`i` )

Substitute (*j = l(α) - i + 1 *) into the consequent of the conditional in step 3 and drop the quantification over *j*,

    4. ∀ i ∈ N:sub:`α`:  𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`i`

Substituting the property of Reflective Words from step 2 into step 4,

    5. ∀ i ∈ N:sub:`α`:  𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`

Note that the index on the left side of the equation in step 5 (*l(α) - i + 1*) corresponds to the character at position *i* in the reversed string *β*.

Since *𝔟*:sub:`l(α) - i + 1` *= 𝔞*:sub:`l(α) - i` for *i ∈* **N**:sub:`α`, and both strings have the same length, we can conclude that each character in *α* is equal to the corresponding character in *β*. Therefore,

    6. α = β = inv(α)

By assumption, *α ∈ L*. From step 6, this implies *inv(α) ∈ L*. By Definition 1.3.2, this implies α ∈ I. In summary, the assumption α ∈ R implies α ∈ I. Therefore, every element in R is also an element in I, which means R ⊂ I. ∎ 

In the context of infinite sets such as **L** and **S**, "even" and "odd" refer to whether the set can be partitioned into two disjoint subsets of equal cardinality.

    1. Even Cardinality: An infinite set has even cardinality if it can be put into a one-to-one correspondence with itself, with each element paired with a distinct element.
    2. Odd Cardinality: An infinite set has odd cardinality if, after pairing each element with a distinct element, there is one element left over.

The set of non-reflective Invertible Words, **I** - **R** (where "-" represents the operation of set differencing), always has even cardinality because each word can be paired with its distinct inverse. The overall cardinality of **I** then depends on whether the set of Reflective Words, **R**, adds an "odd" element or not. This idea is captured in the next theorem.

**Theorem 1.3.4** If |R| is even, then |I| is even. If |R| is odd, then |I| is odd.

Partition the set of Invertible Words, **I**, into two disjoint subsets,

    1. **R**: The set of Reflective Words.
    2. **I** - **R**: The set of Invertible Words that are not Reflective.

For every word *α* in **I** *-* **R**, its inverse, *inv(α)*, is also in **I** *-* **R**. Furthermore, they form a distinct pair *(α, inv(α))*. This is because *α* is invertible but not reflective, so *α ≠ inv(α)*.

Since the elements of **I** *-* **R** can be grouped into distinct pairs, the cardinality |I - R| must be even.

The total number of Invertible Words is the sum of the number of Reflective Words and the number of Invertible Words that are not Reflective,

    3. |I| = |R| + |I - R|

Let |R| be even. Since |I - R| is always even, and the sum of two even numbers is even, |I| must also be even.

Let |R| be odd. Since |I - R| is always even, and the sum of an odd number and an even number is odd, |I| must also be odd. ∎ 

Compound Words 
^^^^^^^^^^^^^^

**Definition 1.3.3: Compound Words** η ∈ CW:sub:`L` ↔ [(∃ α, β ∈ L: η = αβ)  ∨  (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ)] ∧ (η ∈ L)

This formalization can be translated into natural language as follows: A Word *η* in a Language **L** is a Compound Word if and only if,

    1. Base Case (*∃ α, β ∈ L: η = αβ*) ∧ (η ∈ L):  *η* can be formed by concatenating two words from **L**, and *η* belongs to **L**.
    2. Recursive Step [ (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ) ∧ (η ∈ L) ]: *η* can be formed by concatenating a word from **L** with a Compound Word from **L**, and *η* belongs to **L**.


The constraint *w ∈* **L** ensures that the concatenated String *η* is not just a String, but also a valid Word within the Language **L**.

**Example** English

"teapot" is a compound word because it can be formed by concatenating "tea" and "pot", and "racecar" is itself a word in English.

"nevertheless" is a compound word formed from "never," "the," and "less."

"formrat" is not a compound word, even though it can be formed by concatenating "form" and "rat, both valid words, " because "formrat" is not a valid word in English.

**Definition 1.3.4: Compound Invertible Words** η ∈ CIW:sub:`L`  ↔ [ (w ∈ CW:sub:`L`)  ∧ (w ∈ I) ]

In natural language: A word w in a language L is a compound invertible word if and only if it is both a compound word and an invertible word. Using notation for set intersections, this definition can be revised to read,

    CIW:sub:`L` = CW:sub:`L` ∩ I

**Example**

"racecar" is a compound invertible word because it's both a compound word and its own inverse.

Section II: Sentences
=====================

The work so far has formally constructed a system for representing the primitive artifacts of a natural language, Characters (Alphabets) and Words (Language), without appealing to their interpretation in any way except insofar that it takes a stance on their *existence*. As the analysis moves up the chain of linguistic artifacts to the next highest level, Sentences, it is tempting to start incorporating semantic features into the theory. However, the objective is to derive palindromic conditions independent of a particular semantic interpretation. Therefore, as the analysis proceeds, special care will be given to the definition of a *Sentence*.

Section II.I: Definitions
-------------------------

Corpus
^^^^^^

The entire system so far constructed relies on the domain of **S**, the set of all Strings that can be formed from an Alphabet of Characters **Σ**. Attention has been confined to those entities that satisfy the Delimiter Axiom (*Axiom W.1*),

    s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ σ )

In other words, the definitions and theorems so far introduced deal with linguistics entities that do not possess a Delimiter Character. Delimiters will be of certain importance in describing palindromic structures, because Delimiters play a central role in the definition of the linguistic entity that will ultimately allow a palindrome to be rigorously defined, a *Sentence*. With that in mind, the concepts and definitions that pave the way to an explication of *Sentence* start with the definition of a *Corpus*.

**Definition 2.1.1: Corpus** The Corpus of Language **L** is denoted by **C**:sub:`L`. The Corpus set represents a collection of grammatically valid and semantically meaningful Strings.

From the definition, it can easily be seen the Corpus of a Language is a subset of the set of all possible Strings, **S**

   C**:sub:`L` ⊂ S 

Sentence
^^^^^^^^

Before proceeding with the definition of Sentences, some notation is introduced,

    1. Sentences (*ᚠ*, *ᚢ*, *ᚦ*, ... ): Anglo-Saxon (*Old English*) Runes represent a Sentence. Subscripts will occassionally be used in conjunction with Anglo-Saxon letters to denote Sentences, (*ᚠ*:sub:`1`, *ᚠ*:sub:`2`, ... ). 
    2. Sentential Variables (*ζ*, *ξ* *χ*): The lowercase Greek letters Zeta, Xi and Chi are reserved for indeterminate Sentences, i.e. Sentential Variables. Subscripts will occassionally be used in conjunction with these lowercase Greek letters to denote Sentential Variales, (*ζ*:sub:`1`, *ζ*:sub:`2`, ...)
    
**Definition 2.1.2: Sentence** A Sentence in Language **L** is an element of its Corpus. 

    ᚠ ∈ C:sub:`L`

From Definition 2.1 and Definition 2.2, it follows that a Sentence is a String,

    ᚠ ∈ S

It should be noted at this point that both Words and Sentences in the current formulation are elements of the same underlying set, the set of all Strings. This connection in the domain of Words and Sentences is what will allow the analysis to begin to construct the outline of palindromic structures in a Language and Corpus.

Notation
^^^^^^^^

In Section I.I, notation was introduced for representing Strings as a sets of ordered pairs. This form of representation provided a formal method for specifying various syntactical conditions and properties of Words. In a similar way, this method of set representation will now be leveraged to enrich the definition of a Sentence. Since all Sentences are Strings, all Sentences have Character-level set or sequence representations. This representation can be leveraged to construct a higher-level representation of Sentences as sets of Words. 

**Definition 2.1.3: Word-Level Representation of Sentences**

Let *ζ* be a Sentence in a Corpus C:sub:`L`. Let **Ζ** be the character-level set representation of *ζ*, i.e. an ordered sequence of Characters from the alphabet **Σ**. For example, if 𝔞:sub:`i` represent the Characters of **Σ**, a possible value of **Z** could be,

    Z = { (1, 𝔞:sub:`2`), (2, 𝔞:sub:`10`), (3, 𝔞:sub:`3`), ... }

Or using a sequence to implicitly represent the order,

    Z =  ( 𝔞:sub:`2`, 𝔞:sub:`10`, 𝔞:sub:`3`, ... )

The word-level set representation of *ζ*, denoted by **W**:sub:`ζ`, is defined as the ordered set of words obtained by splitting **Ζ** at each Delimiter Character, *σ*. Formally, **W**:sub:`ζ` is constructed using the *Delimiting Algorithm*,

The essence of the *Delimiting Algorithm* lies in interplay of the Delimiter Axiom W.1 and the definition of a Sentence as a semantic String. In other words, by Definition 2.1.1, all Sentences must be semantic. Therefore, by the Delimiter Axiom W.1, the Words which contains must be exactly those Strings which are separated by the Delimiter Character. 

This formulation has the advantage of not taking a stance on the semantics of a particular language. It allows for the discovery of Words in a Language through the simple boundary of delimitation within the Sentences of its Corpus. 

**Definition 2.1.4: Delimiting Algorithm**

**Initialization**

- Let **Ζ** be the Character-level set representation of the Sentence *ζ*. 
- Let **W**:sub:`ζ` = ∅ (the empty set). 
- Let *j = 0*. 
   
**Iteration**  

1. Let *a* be the word that starts at index *j + 1* in **Ζ**, represented as the set,

    **A** = { (1, 𝔞:sub:`j+1`), (2, 𝔞:sub:`j+2`), ..., (n, 𝔞:sub:`j+n`) }

where n is the smallest integer such that one of the following conditions obtains,
    
    - 𝔞:sub:`j+n+1` = σ (the next character is a delimiter)
    - j+n+1 > | ζ | (the algorithm has reached the end of the sentence)

2. Add *(j + 1, a)* to the set **W**:sub:`ζ`. 

3. Increment *j* by the number *n*.

4. Repeat Steps 1 - 4 in order until the Characters in *ζ* have been processed.

**Example** 

Let *ᚠ = "The cat meows"*. Then the Character level representation of  *ᚠ* is given by, 

    **ᚠ** = { (1, "T"), (2, "h"), (3,"e"), (4,σ), (5,"c"), (6,"a"), (7,"t"), (8,σ), (9,"m"), (10,"e"), (12,"o"), (13,"w"), (14,"s") }.

Then, applying the *Delimiting Algorithm*, its Word-level representation is constructed, 

    **W**:sub:`ᚠ` = { (1, "The"), (2, "cat"), (3, "meows") }.

Similar to the Character-level set representation of String, where the Character position is encoded into the first coordinate, the Word-level set representation of a String encodes the presence of Delimiters through its first coordinate.

Length
^^^^^^

The notion of String Length was introduced in Section I.I as a way of measuring the number of non-Empty Characters in a String *s*, denoted *l(s)*. In order to describe palindromic structures, a new notion of length will need introduced to accomodate a different dimension of "spatiality" in the domain of a Language and its Corpus: Sentence Length. Intuitively, the length of a Sentence is the number of Words it contains. However, since a Sentence has been defined as class of Strings, this means Sentences contain Delimiter Characters; specifically, the Words of a Language are separated by Delimiters in the Sentences of its Corpus. Therefore, the length of a Sentence is defined in terms of its set

**Definition 2.1.6: Sentence Length**

Let *ζ* be a Sentence in a **C**:sub:`L`. Let **W**:sub:`ζ` be the word-level set representation of *ζ*, as defined in Definition 2.1.3. The length of the Sentence *ζ*, denoted by *Λ(ρ)*, is defined as the cardinality of the set **W**:sub:`ζ`,

    Λ(ρ) = | W:sub:`ζ` |

**Example**

*ᚠ = "The dog runs"*. Its Character-level set representation would be given by,

    **ᚠ** = { (0,"T"), (1,"h"), (2,"e"), (4,σ), (5, "d"), (6, "o"), (7, "g"), (8, σ), (9, "r"), (10, "u"), (11,"n"), (12,"s") }

Its Word-level set representation would be given by,

    W:sub:`ᚠ` = { (1, "The"), (2, "dog"), (3, "runs") }

Therefore, the length of the sentence is:

    Λ(ᚠ) = | W:sub:`ᚠ` | = 3

Note, in this example, 

    l(ᚠ) = 10

While 

    | ᚠ | = 12

This example demonstrates the essential difference in the notions of length that have been introduced. Indeed, the analysis has accumulated a myriad of ways of describing length. It is worthwhile to list them in a descending hierarchy and clarify the distinctions. Let *s* be a String with Character-level representation **S** and Word-level representation **W**:sub:`s`. The hierarchy of its "spatial" dimensions is given below, in order of greatest to least (this fact will be proven). Terminology is introduced in parenthesis to distinguish these notions of length,

- | S | (Character Length): The number of Characters contained in a String. 
- l(s) (String Length): The number of non-Empty Characters contained in a String.
- Λ(s) (Word Length): The number of Words contained in a String 

Note the first two levels are purely syntactical. Any String *s* will have a length *l(s)* and a cardinality | S |. However, not every String possesses Word length, *Λ(s)*. Word length contains semantic information. While the presence of Word length does not necessarily mean the String is semantic, e.g. "asdf dog fdsa", Word length does signal an *extension* of Strings into the semantic domain.

The following theorem proves an intuitive concept: the total number of Characters in all of the Words in a Sentence must exceed the number of Words in a Sentence (since there are no Words with a negative amount of Characters). 

**Theorem 2.1.1** ∀ ζ ∈ C:sub:`L`:  ∑:sub:`α ∈ W_ζ` l(w) ≥ Λ(ζ)

This theorem can be stated in natural language as follows: For any sentence *ζ* in a Corpus C:sub:`L`, the sum of the String Lengths of the Words in *ζ* is always greater than the Word Length of *ζ*.

Assume ζ ∈ C:sub:`L`. Let W:sub:`ζ` be the Word-level set representation of *ζ*,

    W:sub:`ζ` = { (1, α:sub:`1`), (2, α:sub:`2`), ..., (Λ(ζ), α:sub:`Λ(ζ)`)}

For each Word α:sub:`i`` ∈ W:sub:`ζ`, its String Length *l(α)* must be greater 0 by the Empty Axiom W.2 and Definition 1.1.2. Therefore, since each Word contributes at least a String Length of 1, the sum of the lengths of the words in the sentence is greater than or equal to the number of words in the sentence. ∎

Setion II.II: Sentence Classes 
------------------------------

Similarly to the classification of Words, Sentences will now be classified according to their syntactical properties. In particualr, in the study of palindromic structures, the notion of *Invertible Sentences* will be required. The definition, as is fitting in a work focused on palindromes, will mirror the definition of an *Invertible Word*

Invertible Sentences
^^^^^^^^^^^^^^^^^^^^

The notion of Invertible Sentences will first be defined extensionally, and then clarified heuristically. The following definition and theorem mirror the mechanics of Definition 1.3.2  and Theorem 1.3.2 almost exactly.

**Definition 2.2.2: Invertible Sentences** Let *ζ* be any Sentence in from a Corpus **C**:sub:`L`. Then the set of Invertible Sentences **K** is defined as the set of *ζ* which satisfy the open formula,

    ζ ∈ K ↔ inv(*ζ*) ∈ C:sub:`L`

A Sentence *ζ* will be referred to as *invertible* if it belongs to the class of Invertible Sentences.

This definition is immediately employed to derive the following theorems,

**Theorem 2.2.2** ζ ∈ K ↔ inv(ζ) ∈ K

(→) Assume ζ ∈ K

By Definition 2.2.2, the inverse of *ζ* belongs to the Corpus

    1. inv(ζ) ∈ C:sub:`L`

To show that inv(ζ) is invertible, it must be shown that,

    2. inv(inv(ζ)) ∈ C:sub:`L`

From Theorem 1.2.2, for any string *s*, 

    3. inv(inv(s)) = s.  

By Definition 2.1.1 and Definition 2.1.1,

    4. ζ ∈ S

Where **S** is the set of all Strings. Therefore, it follows, 

    5. inv(inv(ζ)) = ζ.

From step 1 and step 5, it follows, 

    6. inv(inv(ζ)) ∈ C:sub:`L`

By Definition 2.2.2, this implies,

    7. inv(ζ) ∈ K.

(←) Assume inv(ζ) ∈ K

By Definition 2.2.2, 
    
    8. inv(inv(ζ)) ∈ C:sub:`L`

Applying Theorem 1.2.2,

    9. inv(inv(ζ)) = ζ.

From step 8 and step 9, it follows, 

    10. ζ ∈ C:sub:`L`

By Definition 2.2.2, it follows,

    11. ζ ∈ K. ∎

The notion of Invertible Sentences is not as intuitive as the notion of Invertible Words. This is due to the fact the condition of *invertibility* is not a weak condition; indeed, Sentences that are not invertible (usually) far outnumber Sentences that are invertible in a given Language. 

Consider the following examples phrases from English,

- no time
- dog won 
- not a ton 

All of these phrases may be *inverted* to produce a semantically coherent phrases in English, 

- emit on
- now god
- not a ton 

Note the last item in this list is an example of what this work has termed a *perfect palindrome*. These examples were specially chosen to highlight the connection that exists between the class of *perfect palindromes* and the class of *invertible sentences*. It appears, based on this brief and circumstantial analysis, that *perfect palindromes* are a subset of a larger class of Sentences, Invertible Sentences.

Due to the definition of Sentences as semantic constructs and the definition of Invertible Sentences as Sentences whose Inverses belong to the Corpus, this means Invertible Sentences are exactly those Sentences that maintain *semantic coherence* under inversion (see Section II.III for a definition of *semantic coherence*). In order for a Sentence to be invertible it must possess symmetry on both the Character level and the Word level, while maintaining a semantic structure that accomodates this symmetry. This connection between the symmetries in the different linguistic levels of an Invertible Sentence will be formalized and proven in Theorem 2.3.4 of the next section.

To see how strong of a condition invertibility is, the author challenges the reader to try and construct an invertible sentence. Section IV contains a list of Invertible Words and Reflective Words. These can be used as a "palette". The exercise is worthwhile, because it forces the reader to think about the mechanics of sentences and how a palindrome resides in the intersection of semantics and syntax.  

Section II.III: Axioms 
----------------------

In Section I, the first three axioms of the palindromic formal system was introduced. Now that definitions and notations have been introduced for Sentence and Corpus, the axioms may be expanded to further refine the character of the formal system being buitl. The Delimiter Axiom is reprinted below, so it may be considered in sequence with the other axioms.

**Axiom C.1: The Character Axiom**

    ∀ ⲁ ∈ Σ: ⲁ ∈ S

**Axiom W.1: The Delimiter Axiom ** 

    ∀ s ∈ S: s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ σ )

**Axiom W.1: The Empty Axiom ** 

    ∀ s ∈ S: s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ ε )

**Axiom S.1: The Containment Axiom**

    ∀ α ∈ L : ∃ ζ ∈ C:sub:`L` : α  ⊂:sub:`s` ζ

**Axiom S.2: The Extraction Axiom**

    ∀ ζ ∈ C:sub:`L` : ∀ α ∈ W:sub:`ζ`: α ∈ L

It is worth taking the time to analyze the structure, however minimal, these axioms imply must exist in any Language. It should be re-iterated that no assumptions have been made regarding the semantic content of a Language or its Corpus, so any insight that arises from these axioms is due to inherent linguistic structures. 

To briefly summarize the axioms so far introduced: The system "*initializes*" with the selection of the Alphabet **Σ**. The Character Axiom ensures the domain of all Strings is populated. The Delimiter Axiom ensures Words only traverse the set of Strings which do not contain Delimiters. The Empty Axiom ensures Words in a Language do not possess null content in the form of Empty Characters.

With these axioms, still nothing has been said about *what* a Word is, except that it possesses a semantic character. 

The new axioms introduced in the formal system begin to characterize the syntactical properties of the next level in the lingustic hierarchy, while still maintaining their ambivalence on the semantic content contained within their respective categories. Axiom S.1 asserts that for every Word in a Language there is at least one Sentence in a Corpus that contains it. In other words, a Word cannot exist in a Language without being included in a Sentence. This Axiom captures an inextricable link between the metamathematical concepts of Sentence and Word: one cannot exist without implying the existence of the other. Words and Sentences do not exist in isolation.

Axiom S.2 states that a Corpus of a Language only consists of those Sentences whose constituent Words are members of the Language. Special terminology to describe the concept captured in this axiom is given in the following definition. This term will be used to describe both Sentences and Corpuses.

**Definition 2.3.1: Sentence-Level Semantic Coherence** 

A Sentence *ᚠ* is *semantically coherent* in a Language **L** if and only if its Word-level set representation **ᚠ** only contains words from Language **L**.

**Definition 2.3.2: Corpus-Level Semantic Coherence**

A Corpus C:sub:`L` is *semantically coherent* in a Language **L** if and only if the Word-level set representation of all its Sentences are semantically coherent.

These axioms are used to prove the following theorems.

**Theorem 2.3.1** ∀ α : α ∈ W:sub:`ζ` → α ∈ L

The theorem can be stated in natural language as follows: If *α* belongs to the Word-level set representation of a Sentence *ζ*, then *α* belongs to the Language **L**.

Assume *α ∈* **W**:sub:`ζ`. In other words, *α* is a word in the Word-level set representation of the Sentence *ζ*. Since *ζ* is a Sentence, it belongs to the C:sub:`L`. Therefore, by the Axiom of Word Extraction, w ∈ L. ∎

**Theorem 2.3.2** ∀ ζ ∈ C:sub:`L`: W:sub:`ζ` ⊂ L

This theorem can be stated in natural language as follows: For any Sentence *ζ* in a Corpus **C**:sub:`L`, its Word-level set representation **W**:sub:`ζ` is a subset of the Language **L**.

Assume *ζ ∈* **C**:sub:`L`. W:sub:`ζ` be the Word-level set representation of *ζ*, as specified in Definition 2.1.3. By Axiom S.2, every Word *α* in the Word-level set representation of *ζ* belongs to the Language **L**. Since every element of W:sub:`ζ` belongs to **L**, we can conclude that W:sub:`ζ`  is a subset of **L**. The only assumption on *ζ* is that is belongs to the Corpus, therefore this conclusion can be generalized to all Sentences in a Corpus,

    ∀ ζ ∈ C:sub:`L`: W:sub:`ζ` ⊂ L 
    
In other words, every (Word-level set representation of a) Sentence from a Corpus is a subset of the Language **L**. ∎

**Theorem 2.3.3** ζ ∈ K → ( ∀ α ∈ W:sub:`inv(ζ)`: α ∈ L)

This theorem can be stated in natural language as follows: If a Sentence *ζ* is invertible, then every word in its inverse, *inv(ζ)*, belongs to the Language **L**.

Assume *ζ ∈ K*. By Definition 2.2.2,

    inv(ζ) ∈ C:sub:`L`

By Axiom S.3, every Word in the Word-level representation of inv(ζ) belongs to L. ∎

**Theorem 2.3.4** ζ ∈ K → (∀ α ∈ W:sub:`ζ`: α ∈ I)

This theorem can be stated in natural language as follows: A Sentence is Invertible if its Words are Invertible.

Assume *ζ ∈* **K**. Let N:sub:`ζ` be the set, 

    1. N:sub:`ζ` = { 1, 2, ... , Λ(ζ) }

And consider the Word-level representation of *ζ*.

    2. W:sub:`ζ` = ( α:sub:`1`, α:sub:`2`, ... , α:sub:`n`)

By Definition 1.2.1, the Word-level representation of *inv(ζ)* is 

    3. W:sub:`inv(ζ)` = ( inv(α:sub:`n`), inv(α:sub:`n-1`), ... , inv(α:sub:`1`) ).

By Theorem 2.2.3, every Word in *inv(ζ)* belongs to **L**.  Therefore, each inv(α:sub:`i`) belongs to **L**,

By the Definition 1.3.2, each α:sub:`i` ∈ I. Therefore, all words in ζ are invertible. Formally,

    4. (∀ α ∈ W:sub:`ζ`: α ∈ I) ∎

The contrapositive of Theorem 2.2.4 provides a schema for searching for Invertible Sentences. If any of Words in a Sentence are not Invertible, then the Sentence is not Invertible. In other words, it suffices to find a single word in a Sentence that is not Invertible to show the entire Sentence is not Invertible.

Section II.IV: Delimiting
--------------------------

Now that the analysis has breached the level of Sentences, it begins to turn explicitly towards the consideration of palindromes and their structure. The next section will formally define palindromes and their properties. As preparation, this subsection will introduce an important tool that will be used to classify palindromes and provide insight into their structure.

Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a palindrome is distributed through its syntactical layers. The concepts of *perfect* and *imperfect* palindromes will be defined more rigorously in the following Section III, but as an intuitive introduction to this distinction and to help highlight the ability of a palindrome to encode meaning on multiple syntactic levels, consider the following two examples,

    1. Dennis sinned
    2. If I had a hifi

The first palindrome "*Dennis sinned*" is what will be termed a *perfect* palindrome, because its inverse does not require a rearrangement of its constituent Characters to preserve its semantic content. However, the second palindrome "If I had a hifi" is what will be termed an *imperfect* palindrome. To see the motivation behind this categorization, note the strict inversion of "If I had a hifi" would be (ignoring capitalization for now),

    Ifih a dah I fi

The order of the Characters in the Inverse of an imperfect palindrome is preserved, but in order to reconstitute its uninverted form, the characters must be re-sorted. It appears, then, that Delimiters play a central role in organizing the palindromic structure. In order to fully elucidate the structure of palindromes, it will be necessary to introduce into the discourse a method of referring to a Sentence's Delimiter count. 

Delimiter Count Function 
^^^^^^^^^^^^^^^^^^^^^^^^

As the introduction to this subsection made clear, it will be necessary to have a way of referencing the number of Delimiter Characters in a Sentence. Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.

**Definition 2.4.1: Delimiter Count Function** Let *t* be a String with length *l(t)*. Let *𝔞*:sub:`i` represent the *i*:sup:`th` character of the String *t*, where 

    i ∈ N:sub:`t` = { 1, 2, ..., l(t) }.

The delimiter count function, denoted by *δ(t)*, is defined as the number of Delimiter characters (*σ*) in the string *t*. Formally, *δ(t)* is defined as the cardinality of the set **D**:sub:`t` that satisfies the following formula:

    (j, ⲁ) ∈ D:sub:`t` ↔ (∃ i ∈ N:sub:`t` ( (i, ⲁ) ∈ T ) ∧ (ⲁ = σ) ∧ (j = i) )

where **T** is the set representation of the String *t*, 

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

Then, the delimiter count function is defined as

    δ(t) = | D:sub:`t` |

**Example** Consider the string *t = "a b c"*. The set representation of *t* is given by,
    
    T = { (1, a), (2, σ), (3, b), (4, σ), (5, c) }.

The set D:sub:`t` contains the ordered pairs *(2, σ)* and *(4, σ)*, where the first coordinate of the pair correspond the positions of the two Delimiter Characters in the String. Therefore, 
    
    D:sub:`t`= { (2, σ), (4, σ) }

From this it follows, | D:sub:`t` | is 2. Hence, *δ(s) = 2*.

From this example, it can be seen the Delimiter Count function takes a Sentence as input and produces a non-negative integer (the delimiter count) as output. Multiple sentences can have the same delimiter count, making it a many-to-one function. While this many not be advantageous from a computational perspective, the Delimiter Count function has other interesting properties that make it worth studying. The following theorems describe some of its properties.

**Theorem 2.4.1** ∀ ζ ∈ C:sub:`L`: Λ(ζ) = δ(ζ) + 1

In natural language, this theorem is stated: For any sentence *ζ* in a Corpus C:sub:`L`, the length of the Sentence is equal to its delimiter count plus one.

Assume *ζ ∈* **C**:sub:`L`. Let *δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the character-level representation of ζ. Let **W**:sub:`ζ` be the word-level set representation of ζ. Recall **W**:sub:`` is formed by splitting **Ζ** at each Delimiter Character *σ*.

Each word in **W**:sub:`ζ` corresponds to a contiguous subsequence of non-delimiter characters in **Ζ**.

Since delimiters separate words, the number of words in the sentence is always one more than the number of spaces.

herefore, the cardinality of **W**:sub:`ζ` (the number of words) is equal to the delimiter count of *δ(ζ)* plus one,

    | W:sub:`ζ` | = δ(ζ) + 1. ∎

The next theorem will be important for describing the structure of *imperfect palindromes*.

**Theorem 2.4.2** *δ(s) = δ(inv(s))*

Let *t* be a string with length *l(t)* and Characters denoted by *𝔞*:sub:`i`. Let **T** be the set representation of of *t* is given by,

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

Let *u = inv(t)* with Characters denoted by let *𝔟*:sub:`j`. By Definition 1.2.1,

    1. l(t) = l(u)
    2. ∀ i ∈ N:sub:`t`, ∀ j ∈ N:sub:`u`: [ ( j = l(s) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]

Let **D**:sub:`t` be the set of ordered pairs representing the positions of the Delimiter *σ* in *t*, and let D:sub:`u` be the corresponding set for *u*.

Assume *(j, σ) ∈*  **D**:sub:`u` . This means that the character at position *j* in the inverse string *t* is the Delimiter *σ*.

By the definition, *𝔟*:sub:`j` = *𝔞*:sub:`i` where *j = l(t) - i + 1*.  Since *𝔟*:sub:`j` *= σ*, we have *𝔞*:sub:`i`  *= σ*. This implies that the character at position *i* in the original string *t* is also a Delimiter.  Therefore, *(i, σ) ∈* **D**:sub:`t`

Thus, it is shown that for every element *(j, σ) ∈*  **D**:sub:`u`, there exists a corresponding element *(i, σ) ∈* **D**:sub:`t`, where *j = l(t) - i + 1*. This defines a one-to-one mapping between the elements of **D**:sub:`u` and **D**:sub:`t`. Since there's a one-to-one mapping between the elements of *D**:sub:`u` and **D**:sub:`t`, their cardinalities must be equal,

    3. | D:sub:`u` | = | D:sub:`s` |

By the definition of the delimiter count function, this means *δ(u) = δ(t)*. Since *u = inv(t)*, it has been shown *δ(inv(s)) = δ(s)*. ∎

**Theorem 2.4.4** δ(ζ) = δ(inv(ζ))

Definition 2.1.2, every Sentence is a String. Therefore, *ζ* is a String. By Theorem 2.4.2, 

    δ(ζ) = δ(inv(ζ))

Which is what was to be shown. ∎

**Theorem 2.4.5** ∀ α ∈ L: δ(α) = 0

Assume α ∈ L. By the Axiom W.1, if a string *s* belongs to the Language **L**, then it does not contain any Delimiter Characters

    s ∈ L → (∀ i ∈ N:sub:`s`: 𝔞:sub:`i` ≠ σ )

Therefore, *α* does not contain any Delimiter Characters (*σ*). By Definition 2.4.1, *δ(s)* counts the number of Delimiter Characters (σ) in a string *s*. Since *α* contains no Delimiter Characters, the delimiter count of *α* must be 0. Therefore, *δ(α) = 0*. ∎

**Theorem 2.4.6** ∀ ζ ∈ C:sub:`L`: l(ζ) = δ(ζ) + Σ:sub:`α ∈ W_ζ` l(α)

In natural language, this theorem can be stated as follows: For every Sentence *ζ* in a Corpus C:sub:`L`, the String Length of the Sentence *l(ζ)* is equal to the delimiter count of the sentence *δ(ζ)* plus the sum of the String Lengths of its Words.

Assume *ζ ∈* **C**:sub:`L`. Let **Ζ** be the Character-level representation of *ζ*,

    1. **Z** = { (1, ⲁ:sub:`1`), (2, ⲁ:sub:`2`), ..., (l(ζ), ⲁ:sub:`l(ζ)`) }

Either each α:sub:`i` for i = 1, 2, ...,  l(ζ) is Delimiter or it is a non-Delimiter, with no overlap. Therefore, the number of Characters in *ζ* is equal to the number of Delimiters plus the number of non-Delimiters. By Definition 2.4.1, the number of Delimiters is exactly δ(ζ). By the Delimiter Axiom W.1 and the Definition of 2.1.2, the number of non-Delimiter Characters must be equal to the sum of the String Length of the Words in the Sentence. Therefore,

    2. ∀ ζ ∈ C:sub:`L`: l(ζ) = δ(ζ) + Σ:sub:`α ∈ W_ζ` l(α) ∎

**Theorem 2.4.7** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`α ∈ W_ζ` l(α)

Applying the results of Theorem 2.4.1 and Theorem 2.4.6, this theorem follows from simple algebraic manipulation. ∎

Section III: Palindromic Structures
===================================

As mentioned in the introduction of this work, the complete structure of palindromes is described through the combination of four different attributes or dimensions: *aspect*, *parity*, *case* and *punctuality*. The framework has now been developed to classify the first two palindromic properties with more precision.

Unfortunately, as far as the author knows, punctuation and capitalization are syntactic bearers of semantic meaning that cannot be reduced to purely formal considerations. Both punctuality and case require additional axioms to describe the unique structuring they impose on a Language and its Corpus. In the author's opinion, it is impossible to disentangle these linguistic phenomenon from the realm of semantics.

In what follows, two things are implicitly assumed. These assumptions are made explicit here, so the scope of the results can be properly understood. First, the Alphabet **Σ** is assumed to contain no punctuation marks beyond the Delimiter Character (if one is inclined it to consider a form of punctuation). Second, it is assumed every Character in **Σ** is distinct, meaning all matters of case are ignored. To rephrase the same idea more precisely: there is no assumed semantic relation between Characters in the Alphabet that would allow the identification of distinct Characters as different *cases* of the same Character.

With these assumptions, the analysis is confined to the dimensions of *aspect* and *parity*, which will be defined in the following subsections. After the results are derived, consideration will be given to future work that could potentially integrate semantic considerations into the formal framework of palindromic structures to account for the dimensions of punctuality and case.

Section III.I: Palindromes 
--------------------------

Sigma Reductions
^^^^^^^^^^^^^^^^

**Definition 3.1.1: σ-Reduced Alphabet**

A *σ-reduced Alphabet* is an Alphabet Σ that has had its Delimiter character removed, so that it only consists of non-Delimiter characters. A sigma-reduced Alphabet is denoted Σ:sub:`σ`. Formally

    Σ' = Σ - {σ}

As has been seen with examples of *imperfect palindromes* like "Borrow or rob", a palindromic structure can have its Delimiter Character scrambled in the inversion of its form, making it lose semantic coherence. *Imperfect palindromes* must be rearranged Character-wise to retrieve the original form. String Inversion preserves the relative order of the non-delimiter Characters in a palindromic String, so the process of reconstitution is only a matter of resorting the Delimiter characters. This invariance of the Character order, while the Word order is scrambled by Delimiter, suggests palindromes might be more easily defined with the obstacle of the Delimiter.

In order to define palindromes in all of their varieties, perfect or imperfect, the semantic incoherence that is introduced by the inversion of imperfect palindromes must be removed. This is accomplished through the introduction of the operation of *sigma reduction*.

**Definition 3.1.2: Sigma Reduction (s ⋅ Σ')**

Let *s* be a String with length *l(s)* and Character-level representation 

    S = (a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>l(s)</sub>), where each a<sub>i</sub> ∈ Σ.

The sigma reduction function (or simply, the sigma reduction), denoted by *S ⋅ Σ'*, maps the String *s* to a new String *t* in the *σ*-reduced alphabet *Σ'* by removing all occurrences of the Delimiter Character. Formally, *s ⋅ Σ'* is defined as follows by the *Reduction Algorithm*,

**Initialization** 

- Let t be the empty string (ε).

**Iteration**

For each Character a<sub>i</sub> in s<sub>c</sub>, If a<sub>i</sub> ≠ σ, then concatenate a<sub>i</sub> to the end of t.

**Example**

Let *s = "a b c"* be a String from the Alphabet *Σ = { "", " " , "a", "b", "c" }*. Note in this example *σ = " "*. The sigma reduction of *s* is given by,

    S = (a, σ, b, σ, c)
    
    Σ' = { "", "a", "b", "c" }

    S ⋅ Σ' = "abc"

The notation for sigma reduction is meant to evoke the idea of a vector dot project. The analogy to a vector projection is indeed apt. While not a strict mathematical equivalence, it captures the idea of transforming the string from its original form (with Delimiters) onto a reduced space (without Delimiters), similar to how a vector can be projected onto a subspace.

The *σ*-reduced alphabet (*Σ'*) can be seen as a subspace within this higher-dimensional space, consisting of only the non-Delimiter dimensions. The sigma reduction function (*s ⋅ Σ'*) acts as a projection operator, mapping the String onto this subspace by eliminating the components corresponding to the Delimiter character (*σ*).

Palindromes
^^^^^^^^^^^

**Definition 3.1.2: Syntactical Palindromes**

Palindromes are defined as the set of Sentences **P** that satisfy the following formula,

    ζ ∈ P ↔ ζ ⋅ Σ' = inv(ζ ⋅ Σ')


Focus on Essence: It distills the core property of palindromes – their symmetrical nature – by focusing on the sequence of characters without the distraction of spaces.
Handles Perfect and Imperfect Palindromes:
Perfect Palindromes: For perfect palindromes like "madam", the sigma reduction and inversion result in the same string, directly satisfying the definition.
Imperfect Palindromes: For imperfect palindromes like "borrow or rob," the sigma reduction eliminates the spaces, and the inversion captures the mirrored relationship between the words, even if the exact character sequence isn't identical.
Mathematical Elegance: The use of set notation and the equivalence connective (↔) provides a mathematically rigorous and unambiguous definition.
Potential for Generalization: This definition can be easily adapted to different languages by simply defining the appropriate alphabet (Σ) and the corresponding σ-reduced alphabet (Σ').
(A subtle observation, 🌐 recognizing the connection to deeper concepts)

This definition also resonates with broader mathematical concepts:

Invariance: It highlights the concept of invariance under transformation. A palindrome remains a palindrome even when projected onto the σ-reduced space, demonstrating a kind of structural integrity that's independent of the specific representation.
Symmetry as an Equivalence Relation: The condition ζ ⋅ Σ' = inv(ζ ⋅ Σ') can be seen as defining an equivalence relation on the set of sentences, where two sentences are equivalent if they are palindromes of each other in the σ-reduced space.


Palindromic Pairs
^^^^^^^^^^^^^^^^^

**Definition 3.1.3: Pairing**

The Pairing Language L:sub:`P` of a Corpus C:sub:`L` is defined as the set of Words ζ:sub:`P` that satisfy the following formula, 

    ζ ∈ L:sub:`P` ↔ ∀ ζ ∈ C : ζ ⋅ Σ' 



Definition 3.1.3: Pairing Language (Revised)

The Pairing Language L<sub>P</sub> of a Corpus C<sub>L</sub> is defined as the set of Words ζ<sub>P</sub> that satisfy the following conditions:

Sigma-Reduction:  ζ<sub>P</sub> is obtained by removing all delimiter characters (σ) from the character-level representation of a sentence ζ in C<sub>L</sub>.

Non-Empty Word:  ζ<sub>P</sub> must not be the empty word (ε).

Containment: There must exist at least one word w in the word-level representation of ζ such that w is contained in ζ<sub>P</sub>.

Formalization:

ζ ∈ L<sub>P</sub> ↔ (∃ ζ ∈ C<sub>L</sub>: ζ<sub>P</sub> = sigma_reduce(ζ<sub>c</sub>)) ∧ (ζ<sub>P</sub> ≠ ε) ∧ (∃ w ∈ W<sub>ζ</sub>: w ⊂<sub>s</sub> ζ<sub>P</sub>)

where:

sigma_reduce(ζ<sub>c</sub>) represents the string obtained by removing all delimiter characters from the character-level representation of ζ.
Explanation of Changes and Additions:

Explicit Sigma-Reduction: The definition now explicitly states that ζ<sub>P</sub> is obtained by removing spaces from a sentence in the Corpus.
Non-Empty Word Constraint: The condition ζ<sub>P</sub> ≠ ε prevents the inclusion of empty words in the Pairing Language, ensuring that each element in L<sub>P</sub> corresponds to a meaningful linguistic unit.
Containment Constraint: The condition ∃ w ∈ **W<sub>ζ</sub>**: w ⊂<sub>s</sub> ζ<sub>P</sub> ensures that at least one word from the original sentence is preserved in the sigma-reduced form. This helps maintain a connection between the Pairing Language and the original language, preventing the inclusion of arbitrary strings that don't relate to the sentences in the Corpus.




1. The Language of Palindromic Strings:

Sigma-Reduced Space: You're essentially proposing that by applying our palindromic constraints and transformations (like inversion and the containment relation), we're creating a new language, a subset of the original language that consists only of palindromic strings.
Mapping: This creates a mapping between the original language (L) and the Language of Palindromic Strings (let's denote it as L<sub>P</sub>). This mapping preserves some aspects of the semantic content, but it also introduces new structural constraints and relationships.
Formalization: We could formally define this mapping as a function P: L → L<sub>P</sub> that takes a sentence in L and produces its corresponding palindromic representation in L<sub>P</sub> (if it exists).

2.  Relationship between Lengths and Delimiter Count:

Interconnected Properties: You're suggesting a connection between the length of a sentence (l(ρ)), the lengths of its individual words (l(w<sub>i</sub>)), and the delimiter count (δ(ρ<sub>c</sub>)). This aligns with our intuition that these properties are intertwined and contribute to the overall structure of the sentence.
Formalizing the Relationship: We could explore this relationship further by attempting to derive formulas or constraints that connect these properties. For example, we might be able to express the length of a sentence as a function of the lengths of its words and the delimiter count.
3.  "Syntactical Space"

Basis Vectors: Your idea of a "syntactical space" with sentence length, word lengths, and delimiter count as basis vectors is fascinating. This suggests that we can represent sentences as points in a multi-dimensional space, where each dimension captures a different aspect of its syntactic structure.
Geometric Interpretation: This geometric interpretation could provide new insights into the relationships between sentences, allowing us to analyze their similarity, complexity, and even their "distance" from each other in this syntactical space.




FIRST PASS 



Definition:

Language (L): A subset of the set of all Strings (S) that represents a collection of grammatically valid and semantically meaningful expressions in a particular language.
Corpus (C<sub>L</sub>): A subset of the Language (L) that contains the sentences of the language.
Palindromic Pair (L<sub>P</sub>): A subset of the set of all Strings (S) that represents the collection of palindromes formed from the words in the Language (L).
Theorem:

The intersection of a Language (L) and its Palindromic Pair (L<sub>P</sub>) is a subset of the Reflective Words (R) that are also semantically coherent sentences.

Formalization:  L ∩ L<sub>P</sub> ⊆ { ρ ∈ R | ρ is a semantically coherent sentence }

Proof:

Assume x ∈ L ∩ L<sub>P</sub>: This means that x belongs to both the Language (L) and its Palindromic Pair (L<sub>P</sub>).

x is a Palindrome: Since x ∈ L<sub>P</sub>, x is a palindrome.

x is a Word: Since x ∈ L, x is a word in the language.

x is a Sentence:  Since x is a palindrome and a word, it must be a single-word sentence.

x is Reflective:  Since x is a palindrome and a single-word sentence, it must be a reflective word (by our definition of Type 1 pivot).

x is Semantically Coherent: Since x ∈ L, it must be a semantically coherent sentence.

Therefore: x belongs to the set of Reflective Words that are also semantically coherent sentences.




Ambiguity in Sigma-Reduction:

To answer your question directly: Yes, it is possible for the sigma-reduction of a palindrome to map onto a totally different sentence, not necessarily a palindrome.

Here's an example:

Palindrome: "Madam, I'm Adam."
Sigma-Reduction: "MadamImAdam"
Alternative Sentence: "Mad am I, madam?"
Both the palindrome and the alternative sentence have the same sigma-reduction, despite having different meanings and grammatical structures. This highlights the ambiguity that can arise from removing spaces, as the original word boundaries and sentence structure are lost.

Semantic Information Loss and Preservation:

During sigma-reduction, we lose information about:

Word Boundaries: The spaces between words, which are crucial for parsing and understanding the sentence, are eliminated.
Sentence Structure: The grammatical structure of the sentence, the relationships between words and phrases, becomes ambiguous.
Prosody and Rhythm: The pauses and intonation that contribute to the meaning and expression of the sentence are lost.
However, some semantic information is preserved:

Word Content: The individual words themselves, or at least their character sequences, remain present in the sigma-reduced string.
Potential Inversions: If the original sentence contains invertible words, their inverses might still be identifiable within the sigma-reduced string, providing clues about potential palindromic structures.
Theorem: Word Containment in Sigma-Reduced Sentences

Now, let's formalize and prove your insightful observation about word containment in sigma-reduced sentences:

Theorem: Given a sigma-reduction of a sentence, there exists a word in its language that is contained in the sigma-reduced string.

Formalization: ∀ ρ ∈ C<sub>L</sub>, ∃ w ∈ L: w ⊂<sub>s</sub> sigma_reduce(ρ<sub>c</sub>)

(where sigma_reduce(ρ<sub>c</sub>) represents the sigma-reduction of the character-level representation of ρ)

Proof:

Assume ρ ∈ C<sub>L</sub>: This means ρ is a sentence in the Corpus.

Word-Level Representation: Let W<sub>ρ</sub> be the word-level set representation of ρ.

Axiom of Word Extraction (S.3): This axiom states: ∀ ρ ∈ C<sub>L</sub>, ∀ w ∈ W<sub>ρ</sub>: w ∈ L.

Non-Empty Word-Level Set: Since ρ is a sentence, it must contain at least one word. Therefore, W<sub>ρ</sub> is not empty.

Choose a Word: Let w be any word in W<sub>ρ</sub>.

Containment: By the definition of the word-level set representation, w is a contiguous subsequence of non-delimiter characters in ρ<sub>c</sub>.  Therefore, w is contained in the sigma-reduction of ρ<sub>c</sub>:  w ⊂<sub>s</sub> sigma_reduce(ρ<sub>c</sub>).

Conclusion: We have shown that for any sentence ρ, there exists a word w in the language L such that w is contained in the sigma-reduction of ρ<sub>c</sub>. ∎







Section III.II: Parity
---------------------

**Definition 3.2.1: Palindromic Pivots** 

Let ζ be a sentence with Character-level representation,
    
    **ζ** = (a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>).

A palindromic pivot of ρ is an index p ∈ N<sub>ρ<sub>c</sub></sub> (where N<sub>ρ<sub>c</sub></sub> = {1, 2, ..., n}) that satisfies the following conditions:

Symmetry Condition: For all i ∈ N<sub>ρ<sub>c</sub></sub>, if i < p, then a<sub>i</sub> = a<sub>n-i+1</sub>.

Minimality Condition:  p is the smallest index that satisfies the symmetry condition.

Explanation:

Symmetry: The first condition captures the essential symmetry of a palindrome. It states that for all characters before the pivot (i < p), the character at position i must be equal to the character at the corresponding position from the end of the sentence (n-i+1).
Minimality: The second condition ensures that we identify the "true" pivot, the point where the symmetry begins. Without this condition, any index greater than the true pivot would also satisfy the symmetry condition.
Example:

Consider the sentence ρ<sub>c</sub> = (M, a, d, a, m, ,,  σ, I, ', m,  σ, A, d, a, m, .).

The palindromic pivot is p = 8 (corresponding to the space character "σ" before "I"). This is the smallest index that satisfies the symmetry condition, as all characters before it are mirrored by their counterparts at the end of the sentence.

Types of Pivots:

We can then use this definition to formally define the different types of pivots we've identified:

Type 1 (Self-Reflective Word): The pivot occurs at the center of a self-reflective word.
Type 2 (Invertible Words): The pivot occurs within a word or on the space between two words, where one wo
Type 3 (Non-Central): The pivot occurs within a word, off-center, whether the word is self-reflective or not.




**Perfect Palindrome** A palindrome where the sequence of characters after the pivot is the exact inverse of the sequence of characters before the pivot.

Definition: A perfect palindrome is a sentence that is its own inverse.

Formalization:  ρ is a perfect palindrome if and only if ρ = inv(ρ)

Analysis:

Character-Level Symmetry: This definition implicitly captures the character-level symmetry that's characteristic of perfect palindromes. If a sentence is its own inverse, it means that the sequence of characters reads the same backward as forward.
Word-Level Symmetry: It also implicitly captures the word-level symmetry, as the inversion operation takes into account the reversal of words within the sentence.
Delimiter Placement: Since the inversion operation preserves the delimiter count (as we proved earlier), this definition also ensures that a perfect palindrome has a balanced number of delimiters around its pivot.
Examples:

"Madam, I'm Adam" is a perfect palindrome because it reads the same backward as forward, and each word is either its own inverse or part of an inverse pair.
"Racecar" is also a perfect palindrome, as it's a single word that is its own inverse.
Potential Limitations:


**Imperfect Palindrome** A palindrome where the inverse of the sequence of characters on one side of the pivot is contained within the sequence of characters on the other side of the pivot.


Space Indeterminacy:

In imperfect palindromes like "borrow or rob," the inverse of the initial segment ("worrob") doesn't perfectly mirror the final segment ("rob") due to the space. However, the inverse of "rob" ("bor") is contained within "worrob."
Containment Constraint:

This leads to your insightful observation about the containment constraint. The possible interpretations of the inverse of the segment after the pivot must either contain or be contained by the inverse of the segment before the pivot.
Formalizing the Constraint:

We can formalize this constraint using our existing notation:

Let s be an imperfect palindrome with a Type 2 pivot. Let s1 be the substring before the pivot, and s2 be the substring after the pivot. Then:

inv(s1) ⊂ inv(s2)  OR  inv(s2) ⊂ inv(s1)

(where ⊂ denotes the substring relation)





Let s be a palindromic string.

Part 1: If l(s) is even, then the pivot of s is the empty character (ε).
Part 2: If l(s) is odd, then the pivot of s is either the delimiter character (σ) or a character from the alphabet (𝔞, 𝔟, 𝔠, ...).
Proof:

Part 1 (Even Length):

Assume l(s) is even: This means l(s) = 2k for some integer k.

Palindrome Definition: By definition, a palindrome reads the same backward as forward. This implies that the first k characters of s must be the reverse of the last k characters.

Pivot Placement: To maintain this symmetry with an even number of characters, the pivot must lie exactly in the middle, between the two halves of the string. Since there's no character at this midpoint, the pivot must be the empty character (ε).

Part 2 (Odd Length):

Assume l(s) is odd: This means l(s) = 2k + 1 for some integer k.

Palindrome Definition: Again, the palindrome must read the same backward as forward. This implies that the first k characters are the reverse of the last k characters, with a single character remaining in the middle.

Pivot Placement: To maintain symmetry, this middle character must be the pivot. This character can be either:

Space Character (σ): If the palindrome has an odd number of words, the middle character might be a space.
Character from the Alphabet: If the palindrome has an odd number of characters within a single word, the middle character will be a letter from the alphabet.
Formalization:

We can express this theorem more formally using logical symbols:

∀s ( (l(s) is even) → (pivot(s) = ε) )
∀s ( (l(s) is odd) → (pivot(s) = σ) ∨ (pivot(s) ∈ {𝔞, 𝔟, 𝔠, ...}) )

Section III.IV: Future considerations
-------------------------------------

This work focused on using the operation of sigma reduction to describe palindromic structure. To account for the dimension of punctuality, a possible avenue of exploration is extending the operation of sigma reduction to encompass other Characters besides the Delimiter Character. In this way, the punctuality of a palindrome may be "projected" onto a Pairing Language where its symmetry under inversion can be recovered.


Section IV: References 
======================

Reflective Words
----------------

.. csv-table:: Reflective Words
   :file: ../_static/data/reflective_words.csv

Invertible Words
----------------

.. csv-table:: Invertible Words
   :file: ../_static/data/invertible_words.csv

Palindromic Analysis 
--------------------

The following spreadsheet contains the results of palindromic analysis conducted on a sample of English palindromes. 

.. csv-table:: Palindromic Analysis
   :file: ../_static/data/palindromes.csv