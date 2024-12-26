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
  
A note on the terminology introduced in this work is in order. When a semantic term is capitalized, e.g. Word or Sentence, this will mean it is referred to in its capacity as a formal entity. While the formal system was designed to model the actual syntax of Characters, Words and Sentences, this should not be taken to mean the formal entities that emerge from this system are necessarily representative of actual linguistic entities. While the formal entities in this system may not map *one-to-one* with their empirical counterparts, it will be seen these formal characteristics nevertheless provide insight into the empirical nature of their counterparts.

The main results of this work are given in the following list,

- Theorem 2.3.4: This theorem states if a Sentence is invertible, then its Words are invertible.  
- Theorem 3.3.1: This theorem states either the ending word of a Palindrome must be contained in its starting word, or the starting word of a Palindrome must be contained in its ending word.
- Theorem 3.3.2: This theorem states if a Palindrome has a Delimiter Pivot, then the Word on one side of the Pivot must contain the Word on the other side of the pivot
- Theorem 3.3.3: This theorem states if a Palindrome is perfect, then either its Pivot occurs at the center of a Reflective Word, or its Pivot is flanked by Invertible Words where one Word must contain the other Word.
- Theorem 3.3.4: This theorem states if a Palindrome is perfect and has even parity, then its Pivot must occur at the center of a Reflective Word. If a Palindrome is perfect and has odd parity, then either its Pivot occurs at the center of a reflective word, or its Pivot is a Delimiter flanked by Invertible Words where one Word contains the other Word.

Section I: Defintions 
=====================

Some general notation adopted throughout the course of this work is given below.

1. **N**:sub:`n` will represent the set of natural numbers starting at 1 and ending at *n*, 

    N:sub:`n`= { 1, 2, ... , n }

2. The cardinality of a set **A** will be denoted | A |

3. The ∎ symbol will be used to denote the ending of all Definitions, Examples and Proofs. 

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

It will sometimes be necessary to refer to indeterminate Characters, so notation is introduced for Character Variables,

    1. Character Variables (*ⲁ*, *ⲃ*, *ⲅ*, etc. ): Lowercase Coptic letters will represent Character Variables, i.e. indeterminate Characters. Subscripts will occassionally be used with Coptic letters to denote Word Variables, (*ⲁ*:sub:`1`, *ⲁ*:sub:`2`, ... )

Concatenation 
^^^^^^^^^^^^^

Concatenation is considered the sole constitutive operation for the formation of Strings. It is taken as a primitive operation, but not an elementary operation. By this it is meant the notion of concatenation that is about to be adopted does not define concatenation solely in terms of Strings. Concatenation will be defined as a hetergeneous operation that is performed between Characters in Alphabet and Strings.

**Definition 1.1.1: Concatenation**  The result of *concatenating* any two Characters *ⲁ* and *ⲃ** is denoted *ⲁⲃ*. To make the operands of concatenation clear, parentheis will sometimes be used to separate the Characters being concatenated, *ⲁ(ⲃ) = (ⲁ)ⲃ = ⲁⲃ*.

Colloquially, *ⲁ* is the String that results from placing *ⲃ* behind *ⲁ*. More formally, Character concatenation is defined inductively through the following schema,

    1. Basis Clause: ∀ ⲁ ∈ Σ: ⲁε = ⲁ
    2. Inductive Clause: ∀ ⲁ, ⲃ, ⲅ ∈ Σ: ⲁ(ⲃⲅ) = (ⲁⲃ)ⲅ
    3. Comprehension Clause: ∀ ⲁ ∈ Σ, ∀ s ∈ S: ⲁs ∈ S
    4. Uniqueness Clause: ∀ ⲁ, ⲃ, ⲅ, ⲇ ∈ Σ: (ⲁⲃ = ⲅⲇ) → ((ⲁ = ⲅ) ∧ (ⲃ = ⲇ)) ∎

The first clause is the basis step of induction which states any Character appended to the Empty Character is the Character itself. The second clause is the inductive step which allows the concatenation of Characters into Strings of arbitrary length through recursion.

It is assumed that the operation of concatenation is closed with respect to the set of all Strings **S**. In other words, concatenation will always yield a String. This assumption is captured in the Comprehension Clause of Definition 1.1.1. This clause ensures ensures that all results of concatenation are Strings. 

The Uniqueness Clause states that if the concatenation of two characters *ⲁ* and *ⲃ* is equal to the concatenation of two other characters *ⲅ* and *ⲇ*, then it must be the case that *ⲁ* is equal to *ⲅ* and *ⲃ* is equal to *ⲇ*. In other words, there's only one set of Characters that can form a given String through concatenation.

Concatenation as it is normally found in the fields of automata theory and regular expressions is treated as a primitive operation performed between two Strings operands. Concatenation of multiple Strings is then defined inductively. The current formulation differs in that concatenation in this system is not conceived as the "joining" of two or more Strings. Instead, the formal system under construction treats concatenation as an elementary operation that occurs between Characters and Strings, i.e. it is a *hetergeneous* operation.

To make this distinction plain, it should be noted that given an Alphabet Σ and Definition 1.1.1, one still cannot say the result of a concatenation is a String, nor make any claim about the contents of **S**, the set of all Strings. The Comprehension Clause of Definition 1.1.1 only states the result of concatenating a Character with a String is a String. It says nothing at all about whether or not single Characters themselves are Strings, and thus it says nothing about whether the result of concatenating single Characters is itself a String. 

In order to rectify this, the first Axiom is introduced,

**Axiom C.1: The Character Axiom**

    ∀ ⲁ ∈ Σ: ⲁ ∈ S

This Axiom states the intuitive notion that all Characters are Strings. This includes Empty Characters and Delimiter Characters. This Axiom, in conjunction with Definition 1.1.1, immediately populates the set of all Strings **S** with an uncountably infinite domain of objects (See Theorem 1.1.1 for an informal proof of this fact) consisting of every possible combination of Characters from the Alphabet. In other words, Axiom C.1 in conjunction with Definition 1.1.1 ensure the domain is non-Empty. 

**Example** Let *s = 𝔞𝔟𝔠* and *t = 𝔡𝔢𝔣*. The concatenation of these two Strings *st* is written,

    st = (𝔞𝔟𝔠)(𝔡𝔢𝔣) 
    
Using the inductive clause, this concatenation can be grouped into simpler concatenations as follows,    
    
    𝔞(𝔟(𝔠(𝔡(𝔢𝔣)))) = (((((𝔞𝔟)𝔠)𝔡)𝔢)𝔣) = 𝔞𝔟𝔠𝔡𝔢𝔣

Therefore, *st = 𝔞𝔟𝔠𝔡𝔢𝔣* ∎

Notation
^^^^^^^^

It will sometimes be convenient to represent Words and Strings as ordered sets of Characters, rather than serialized concatenations of Characters. The two formulations are equivalent, but the set representation has advantages when it comes to quantification and symbolic logic. When a String or Word representation is intended to be interpretted as a set, it will be written in bold uppercase letters. For example, the String represented as the concatenated series *s*:sub:`1` *= 𝔞𝔟𝔠* would be represented in this formulation as a set of ordered pairs **S**:sub:`1`, where the first coordinate encodes the position of the Character in the String,

    S:sub:`1` = { (1, *𝔞*), (2, *𝔟*), (3, *𝔠*) }

Note, since sets do not preserve order, this would be equivalent to,

    { (3, *𝔠*), (2, *𝔟*), (1, *𝔞*) }

To simplify notation, it is sometimes beneficial to represent this set as a sequence that *does* preserve order as,

    S:sub:`1` = (*𝔞*, *𝔟*, *𝔠*) 

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

Formally, we define the length of *t* to be cardinality of the set **E**:sub:`t` that satisfies the open formula,

    (j, ⲁ) ∈ E:sub:`t` ↔ (∃i ∈ N:sub:`l(t)`: ((i, ⲁ) ∈ T) ∧ (ⲁ ≠ ε) ∧ (j = i) )

The length of String in the formalization can be written,

    l(t) = | E:sub:`t` | ∎

Note the E:sub:`t` is a set of *ordered pairs*, not a set of Characters. This allows for repeated Characters to be counted in a String's length.

**Example** t = "aabbcc"

The set representation of *t* is given by,

    T = { (1, "a"), (2, "a"), (3, "b"), (4, "b"), (5, "c"), (6, "c") }.

By Definition 1.1.2, 

    E:sub:`t` = { (1, "a"), (2, "a"), (3, "b"), (4, "b"), (5, "c"), (6, "c") }

Therefore, 

    | E:sub:`t` | = 6 ∎

This formulization, while perhaps prosaic, maps to the intuitive notion of a String's length, i.e. the number of non-Empty Characters, while still allowing for a calculus of concatenation that involves Empty Characters.

Containment
^^^^^^^^^^^

Similar to the explication of *length*, the notion of a String *containing* another String must be made precise using the definitions introduced so far. It's important to note that in the current system the relation of *containment* is materially different from the standard subset relation between sets. For example, the set of characters in "rat" is a subset of the set of characters in "tart," but "rat" is not contained in "tart" because the order of the characters is different.

Consider the strings "rat" and "strata". The string "rat" *is contained* in the string strata", because the order of the string "rat" is preserved in "strata". An intuitive way of capturing this relationship is to map the indices of the characters in "rat" to the indices of the characters in "strata" which correspond to the indices in "rat". A cursory (but incorrect) definition of *containment* can then be attempted, using this insight as a guide.

**Containment (Incorrect Version)** t ⊂:sub:`s` u

Let *t* and *u* be Strings represented as the sets of ordered pairs, **T** and **U**,

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ..., (l(t), 𝔞:sub:`l(t)`) }

    U = { (1, 𝔟:sub:`1`), (2, 𝔟:sub:`2`), ..., (l(u), 𝔟:sub:`l(u)`) }

*t* is said to be *contained in u*, denoted by,

    t ⊂:sub:`s` u
    
If and only if there exists a strictly increasing function *f*: **N**:sub:`u` *→* **N**:sub:`t` such that:

    ∀ i ∈ N:sub:`u`: 𝔞:sub:`i` = 𝔟:sub:`f(i)` ∎

This definition essentially states that *t* is contained in *u* if there's a way to map the Characters of *t* onto a subsequence of the Characters in *u* while preserving their order. The function *f* ensures that the Characters in *t* appear in the same order within *u*. While this definition is incorrect, the reason why this version of *containment* fails is instructive in developing better understanding of the subtlety involved in attempting its definition. 

First, consider an example where this definition correlates with the intuitive notion of *containment*. Let *t = "rat"* and *u = "strata"*. Then, these Strings can be represented in set notation as,

    T = { (1, "r"), (2, "a"), (3, "t") }
     
    U = { (1, "s'), (2, "t"), (3, "r"), (4, "a"), (5, "t"), (6, "a") }.

The function *f* defined as *f(1) = 3*, *f(2) = 4*, and *f(3) = 5* satisfies the condition in the proposed definition, as it maps the characters of "rat" onto the subsequence "rat" within "strata" while preserving their order. In addition, *f* is a strictly increasing function. Therefore, 

    "rat" ⊂:sub:`s` "strata".

Next, consider a counter-example. Let *t* = "bow" and *u* = "borrow". Then their corresponding set representations are given by,

    T = { (1, "b"), (2, "o"), (3, "w") }
     
    U = { (1, "b'), (2, "o"), (3, "r"), (4, "r"), (5, "o"), (6, "w") }

The function defined through *f(1) = 1*, *f(2) = 5* and  *f(3) = 6* satisfies the conditions of the proposed definition. However, intuitively, "bow" is *not contained* in the word "borrow". The reason the proposed definition has failed is now clear: the function *f* that is mapping "bow" to "borrow" skips over the indices 2, 3 and 4 in "borrow". In other words, in addition to being strictly increasing, the function *f* which maps the smaller word onto the larger word must also be *consecutive*. This insight can be incorporated into the definition of *containment* by first defining the notion of *consecutive*,

**Definition 1.1.3: Consecutive Functions** 

A function *f* is consecutive over N:sub:`s` if it satisfies the formula,

    ∀ i, j ∈ N:sub:`s`:  (i < j) →  f(j) = f(i) + (j - i) ∎
    
This additional constraint on *f* ensures that the indices of the larger word in the containment relation are mapped in a sequential, unbroken order to the indices of the smaller word. This definition of *Consecutive Functions* can be immediately utilized to refine the notion of *containment*.

**Definition 1.1.4: Containment** t ⊂:sub:`s` u

Let *t* and *u* be Strings represented as the sets of ordered pairs, **T** and **U**,

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ..., (l(t), 𝔞:sub:`l(t)`) }

    U = { (1, 𝔟:sub:`1`), (2, 𝔟:sub:`2`), ..., (l(u), 𝔟:sub:`l(u)`) }

*t* is said to be *contained in u*, denoted by,

    t ⊂:sub:`s` u

If and only if there exists a strictly *increasing and consecutive* function *f*: **N**:sub:`t` *→* **N**:sub:`u` such that:

    ∀ i ∈ N:sub:`t`: 𝔞:sub:`i` = 𝔟:sub:`f(i)` ∎

The notion of containment will be central to developing the logic of palindromic structures in the subsequent sections.

Cardinality
^^^^^^^^^^^

The set of all Strings is denoted **S**. The cardinality of **S** is denoted | S |.

It is assumed **S** is at least uncountably infinite. A rigorous proof of this fact would carry the current work too far into the realm of real analysis, but as motivation for this assumption, an informal proof is presented below based on Cantor's famous diagonalization argument. 

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

If Characters are mapped to letters in the Alphabet of a *Language* **L**, the set of all Strings would have as a subset the Language that is constructed through the Alphabet. The goal of this section is to define the syntactical properties of Words in **L** that differentiates them from Strings in **S** based solely on their internal structure. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations. In other words, this analysis will proceed without assuming anything about the interpretation of the Words in the Language beyond the fact that they *are* Words of the Language.

To formalize these notion, the following symbolic notation is introduced, 

    1. Words (*a*, *b*, *c*, etc.): Lowercase English letters represent Words. Subscripts will occassionally be used to denote Words, (*a*:sub:`1`, *a*:sub:`2`, ... )
    2. Language (**L**): The uppercase English letter *L* in boldface represents a Language.

In the case of English, Words would correspond to words such as "dog", "cat", etc. A Language would correspond to a set of words such as *{ "dog", "cat", "hamster", ... }* or *{ "tree", "flower", "grass", .... }*.

The number of Words in a Language is denoted | L |. 

It will sometimes be necessary to refer to indeterminate Words, so notation is introduced for Word Variables,

    1. Word Variables (*α*, *β*, *γ*, etc. ): Lowercase Greek letters will represent variable words, i.e. indeterminate Words. Subscripts will occassionally be used to denote Word Variables, (*α*:sub:`1`, *α*:sub:`2`, ... ). 

The exceptions to this rule for Lowercase Greek letters are *ζ* which is reserved for Sentential Variables (see Section II.I for more information.), *σ* and *ε* which are reserved for the Delimiter and Empty Character (see Section I.I for more information), and *ω* which is reserved for the Palindromic Pivot (see Section III.II for more information).

The range of a Word Variable is understood to be the Language **L** from the Words are being drawn. 

With these definitions, the hierarchy of relationships that exist between a word *α*, its Language **L** and the set of all Strings **S** are given by,

    1. α ∈ L
    2. α ∈ S
    3. L ⊂ S

To clarify the relationship between Strings, Words and Language,

    1. All Words belong to a Language.
    2. All Words belong to the set of all Strings
    3. Language is a subset of the set of all Strings.
    4. Not all Strings are Words. 

The next theorems establish some basic results about Words in a Language within this formalization. All of these theorems should conform to the common sense notion of Words. The first theorem provides a rigorous formalization of the inituitive notion that every Character in a Word is contained in the Word. 

**Theorem 1.2.1** ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: ( (i, ⲁ:sub:`i`) ∈  Α ) → ( ⲁ:sub:`i` ⊂ α)

Assume *α ∈* **L**. Let (*i*, *ⲁ*:sub:`i`) be the *i*:sup:`th` ordered pair in its Character level representation **Α**. Consider the String *s* with a single Character *𝔟*:sub:`1` = *ⲁ*:sub:`i`.

    s = ⲁ:sub:`i`.

Clearly, l(s) = 1. To show that *s* is contained in *α*, a strictly increasing and consecutive function that maps the Characters in *s* to the Characters in *α* must be found. Since *l(s) = 1*, this can be defined simply as,

    f(1) = i

For any value of *i*. Therefore, by Definition 1.1.4,

    ⲁ:sub:`i` ⊂ α ∎

Theorem 1.2.2 and Theorem 1.2.3 are the direct result of defining String length as the number of non-Empty characters in a String and then defining containment based on String length. Careful inspection of Definition 1.1.4 will show that it depends on a precise notion of length. In other words, in the current formal system, containment is a derivative concept of length. 

**Theorem 1.2.2** ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: [ (i, ⲁ:sub:`i`) ∈  Α ] → ¬[ (ⲁ:sub:`i` = ε) ∧ (ⲁ:sub:`i` ⊂:sub:`s` α) ]

This theorem can be stated in natural language as follows: The Empty Character does not belong to a Word in a Language. 

Assume *α ∈* **L**. Let (*i*, *ⲁ*:sub:`i`) be the *i*:sup:`th` ordered pair in its Character level representation **Α**.

Let String *t = ε*. Assume, for the sake of contradiction, a Word *α* exists in Language **L** such that,

    1. t ⊂:sub:`s` α 

Note, by Definition 1.1.2, 

    2. l(t) = 0

Therefore, **N**:sub:`l(t)` *= ∅*. Now, applying Definition 1.1.4, 

    3. ∀ i ∈ N:sub:`l(t)`: 𝔞:sub:`i` = 𝔟:sub:`f(i)`

Where 𝔞:sub:`i` represents the Characters in *t*, 𝔟:sub:`f(i)` represents the Characters in *α*, and *f(i)* represents the function that maps the Character indices of *t* onto the Character indices of *α*. It is a tautology of set theory that nothing can belong to the empty set,

    4. ∀ x: x ∉ ∅

From this, it follows that no *i* exists that satisfies this formula. Therefore, no function *f(i)* exists that maps the Empty Character to a Character in *α*. But this contradicts the assumption in step 1, since by Definition 1.1.4, in order for a String to be contained in another String, a strictly increasing and consecutive function must exist to map the Characters. 

Since *t = ε* exists by Axiom C.1, it follows,

    1. t = ε ∧ t ⊂:sub:`s` α

must always be false, and its negation must always be true. ∎

**Theorem 1.2.3**  ∀ α ∈ L : ∀ i ∈ N:sub:`l(α)`: 𝔞:sub:`i` ≠ ε 

This theorem can be stated in natural language as follows: If a Word belongs to a Language, then none of its Characters are empty.

Assume *α ∈* **L**. Let (*i*, *ⲁ*:sub:`i`) be the *i*:sup:`th` ordered pair in its Character level representation **Α**.

From Theorem 1.2.1, it follows, 

    1. ( ⲁ:sub:`i` ⊂ α)

From Theorem 1.2.2, it follows, 

    2. ¬[ (ⲁ:sub:`i` = ε) ∧ (ⲁ:sub:`i` ⊂:sub:`s` α) ]

Recall for any propositions *p* and *q*,

    3. ¬ ( p ∧ q ) = ¬ p ∨ ¬ q

Applying step 3 to step 2,

    4. (ⲁ:sub:`i` ≠ ε) ∨  ¬(ⲁ:sub:`i` ⊂:sub:`s` α) 

The only way for step 1 to be consistent with step 4 is if the first conjunct of the expression obtains, 

    ⲁ:sub:`i` ≠ ε 

But *i* was assumed to be an arbitrary Character index in the set representation of *α*. Therefore, generalizing, none of the Characters in a Word can be empty. ∎

Theorem 1.2.2 and 1.2.3 are the necessary logical pre-conditions for Words to arise from Strings. In essence, before Language can be distinguished from its uncountably infinite domain, a way of measure String length must be introduced. This definition prevents Empty Strings from entering into the Language, which would otherwise allow the annunciation of null content.

Language is materially different from its un-structured domain, but this is not guaranteed by Theorem 1.2.1 - Theorem 1.2.3. Rather, Theorem 1.2.1 - Theorem 1.2.3 provide the foundation. To build on this foundation, an additional Axiom governing Word discovery is introduced in the next section.

Axioms
^^^^^^

The goal of the current analysis is to leave the semantic interpretation of Words in a Language as ambiguous as possible. This ambiguity, it is hoped, will leave the results of the analysis applicable to palindromic structures in a variety of languages. This section details the minimal *necessary* assumptions that are placed on any String to be considered an element of a Language **L**, i.e. a Word. The axioms listed in this section are not *sufficient*; in other words, it is possible for a String to satisfy these axioms without being an element of a Language, but any Word that belongs to a Language must satisfy the axioms.

Let **L** be a Language. Let *s* be a String, not necessarily a member of **L**. Let *𝔞*:sub:`i` be the *i*:sup:`th` Character of the String *s*.

**Axiom W.1: The Delimiter Axiom ** 

    ∀ s ∈ S: s ∈ L → (∀ i ∈ *N*:sub:`l(s)`: 𝔞:sub:`i` ≠ σ ) ∎

While the definition of String length precludes the inclusion of the Empty Character in a Word, there is no such restriction on the Delimiter. In essence, this Axiom capture the common-sense notion that a Word from a Language cannot contain a Delimiter; Instead, Delimiters are what separate Words from one another in a String. 

Inversion
^^^^^^^^^

Informally, the *Inverse* of a String is the reversed sequence of Characters in a String. The goal of this section is to define this notion precisely. In the process, the motivation for this definition will be elucidated. 

**Definition 1.2.1: String Inversion** 

Let *s* be a string with length *l(s)*. Let *𝔞*:sub:`i` be the *i*:sup:`th` character of the String *s*. 

Then, let *t* be a String with length *l(t)* and let *𝔟*:sub:`j` be the *j*:sup:`th` character of the String *t*. 
    
*t* is called the Inverse of *s* and is denoted *inv(s)* if it satisfies the following conditions, 

    1. l(t) = l(s) 
    2. ∀ i ∈ N:sub:`l(s)`, j ∈ N:sub:`l(t)`: [ ( j = l(s) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ] ∎

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

The intent is to define a class of Words whose elements belong to it if and only if their Inverse exists in the Language. As a first step towards this definition, String Inversion was introduced and formalized. In the next section, String Inversion will provide a subdomain in the domain of discourse over which to quantify the conditions that are to be imposed on the class of *Invertible Words*, i.e. the class of Words whose Inverses are also Words. 

Before defining the class of Invertible Words in the next section, this section is concluded with a theorem that strengthens the definition of String Inversion. This theorem will be used extensively in the subsequent sections.

**Theorem 1.2.4** *inv(inv(s)) = s*

Let *s* be a String with length *l(s)* and Characters *𝔞*:sub:`i`. 

Let *t = inv(s)* with length *l(t)* and Characters *𝔟*:sub:`j`.

By the Definition 1.2.1,

    1. l(t) = l(s)
    2. ∀ i ∈ N:sub:`l(s)`, ∀ j ∈ N:sub:`l(t)`: [ (j = l(s) - i + 1) →  ( 𝔟:sub:`j` = *𝔞*:sub:`i` ) ]

Now, let *u = inv(t)* with length *l(u)* and Characters *𝔠*:sub:`k`. Applying Definition 1.2.1 again,

    1. l(u) = l(t)
    2. ∀ j ∈ N:sub:`l(t)`, ∀ k ∈ N:sub:`l(u)`: [ (k = l(t) - j + 1) → ( 𝔠:sub:`k` = 𝔟:sub:`j` ) ] 
 
Since *l(t) = l(s)* (step 1) and **N**:sub:`l(t)` *=* **N**:sub:`l(s)` (by definition of natural numbers), these substitions may be made in step 4,

    5. ∀ i ∈ N:sub:`l(s)`, ∀ k ∈ N:sub:`l(u)`: [ ( k = l(s) - (l(s) - i + 1) + 1 )  → ( 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` ) ]

The index *k* may be simplified,

    6. k = l(s) - l(s) + i - 1 + 1 = i

Therefore,
    
    7. ∀ i ∈ N:sub:`l(s)`, ∀ k ∈ N:sub:`l(u)`: [ ( k = i)  → ( 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` ) ]

This may be rewritten, noting the condition *k = i*,

    8. ∀ i ∈ N:sub:`l(s)`: 𝔠:sub:`k` = 𝔟:sub:`l(s) - i + 1` 

Now, substitute the definition of *𝔟*:sub:`j` from step 2 (where *j = l(s) - i + 1*) into the equation for  *𝔠*:sub:`k`,

    9. ∀ i ∈ N:sub:`l(s)`: 𝔠:sub:`i` = 𝔞:sub:`i` 

Since *u* and *s* have the same length (*l(u) = l(t) = l(s)*) and the same Characters in the same order (𝔠:sub:`i` = 𝔞:sub:`i`  for all *i*), it can be concluded that *u = s*. Recall that *u = inv(t)* and *t = inv(s)*.  Substituting, the desired result is obtained, *inv(inv(s)) = s*. ∎ 

Concatenation
^^^^^^^^^^^^^

Concatenation was defined in Definition 1.1.1 in terms of Characters and Strings. Every Word is a String and every String has a Character-level set representation, so the operation of concatenation will not be materially altered to accomodate Words. However, as the analysis builds toward soldifying a theory of palindromes, the result of this essential operation will be given a slightly different formal representation. This representation will not change the operation in any way, but will instead enable a more descriptive theory to emerge when the concept of a Pairing Language is introduced.

Let *α* and *β* be two words with the following Character level set representations:

    Α = { (1,  𝔞:sub:`1`), (2,  𝔞:sub:`2`), ... , (l(α),  𝔞:sub:`l(α)`) }

    Β = { (1, 𝔟:sub:`1``), (2, 𝔟:sub:`2`), ... , (l(β), 𝔟:sub:`l(β)`)}

By Definition 1.1.1, the concatenation of *α* and *β*, denoted by *αβ*, is the String *t* formed by appending the characters of *β* to the end of *α*. Formally, the set representation of *t* is given by,

    T = { (1, 𝔞:sub:`i`), (2,  𝔞:sub:`2`), ..., (l(α),  𝔞:sub:`l(α)`), (l(α) + 1, 𝔟:sub:`1`), (l(α) + 2, 𝔟:sub:`2`), ..., (l(α) + l(β), 𝔟:sub:`l(β)`)}

Note *t* is not necessarily a Word in the Language. 

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

From this list, it should be clear what is meant by the notion of *reflective*. Reflective Words are those Words whose meaning is unchanged by a String Inversion. However, the semantic content that is preserved under inversion is not the primitive property that primarily explains this invariance. The invariance of the semantic content under inversion is the result of Character level symmetries. 

Rather than attempt to define Reflective Words as the class of Words that are their own Inverses, a different approach will be taken that highlights the Character level symmetries that exist in these class of Words. It will then be proven the class of Words which satisfy this definition are exactly those Words that are their own Inverses.

**Definition 1.3.1: Reflective Words** 

Let *α* be any word from Language **L**. Let *𝔞*:sub:`i` be the *i*:sup:`th` Character in *α*. Then the set of Reflective Words **R** is defined as the set of *α* which satisfy the open formula,

    α ∈ R ↔ [ ∀ i ∈ N:sub:`l(α)`:  𝔞:sub:`i` = 𝔞:sub:`l(α) - i` ] ∎

A Word *α* will be referred to *reflective* if it belongs to the class of Reflective Words. 

The following theorem is an immediate consequence of this definition.

**Theorem 1.3.1** α ∈ R ↔ α = inv(α)

In natural language, this theorem can be stated as: A Word is Reflective if and only if it is its own Inverse.

(→)  Assume *α ∈ R*. Let *𝔞*:sub:`i` be the Characters in *α*. By Definition 1.3.1, 

    1. ∀ i ∈ N:sub:`l(α)`: 𝔞:sub:`i` = 𝔞:sub:`l(α) - i`

Let *β = inv(α)*. Let 𝔟:sub:`j` be the Characters in *β*. By the Definition 1.2.1,

    2. l(β) = l(α)
    3. ∀ i ∈ N:sub:`l(α)`, ∀ j ∈ N:sub:`β`: [ ( j = l(α) - i + 1 ) →  ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]
   
Substitute *j = l(α) - i + 1* into the equation from step 3 and remove the quantifiation over *j*:

    4. ∀ i ∈ N:sub:`l(α)`: 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`i`

Now, use the property of Reflective Words from step 1 (𝔞:sub:`i` = 𝔞:sub:`l(α) - i` ) and substitute it into the equation from step 4:

    5.  4. ∀ i ∈ N:sub:`l(α)`: 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`

Note that the index on the left side of this equation (l(α) - i + 1) corresponds to the character at position *i* in the reversed string β.  This is because the index *j* in the definition of String Inversion maps to the *l(α) - i + 1*:sup:`th`` position in the original string.

Since 𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`for all i ∈ N:sub:`α`, and both strings have the same length, we can conclude that each character in *α* is equal to the corresponding character in β. Therefore the desired result is obtained: *α = β = inv(α)*

(←) Assume α = inv(α)

Let *𝔞*:sub:`i` be the Characters in *α* and let *𝔟*:sub:`j` be the Characters in *inv(α)*. By definition of String Inversion,

    1. l(α) = l(inv(α))
    2. ∀ i ∈ N:sub:`l(α)`, ∀ j ∈ N:sub:`l(inv(α))`: [ ( j = l(α) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]

Since *α = inv(α)*, 𝔞:sub:`j` can be substituted for 𝔟:sub:`j` in the step 2,

    3. ∀ i ∈ N:sub:`l(α)`, ∀ j ∈ N:sub:`l(inv(α))`: [ ( j = l(α) - i + 1 ) → ( 𝔞:sub:`j` = 𝔞:sub:`i` ) ]

Since the conditional inside of the quantification is only true when *j = l(α) - i + 1*, *j* can be substituted into the consequent of the conditional and the quantification over *j* can be dropped. Therefore, step 3 can be rewritten as,

    4. ∀ i ∈ N:sub:`l(α)`: 𝔞:sub:`l(α) - i + 1` =  𝔞:sub:`i`

Similar to the previous part of the proof, the index on the left side (*l(α) - i + 1*) corresponds to the Character at position *i* in the reversed string, which is *α* itself in this case. Therefore, 

    5. ∀ i ∈ N:sub:`l(α)`: 𝔞:sub:`i` =  𝔞:sub:`l(α) - i`

This condition satisfies the definition of Reflective Words, so *α ∈ R*. ∎ 

Invertible Words 
^^^^^^^^^^^^^^^^

As discussed previously, the concept of *Invertible* is exemplified in the pair of English words "*time*" and "*emit*". An *Invertible Word* is a Word whose inverse is part of the same Language **L**. This notion can now be made more precise with the terminology introduced in prior sections.

**Definition 1.3.2: Invertible Words** 

Let *α* be any Word in a Language **L**. Then the set of Invertible Words **I** is defined as the set of α which satisfy the open formula,

    α ∈ I ↔ inv(α) ∈ L ∎

A Word *α* will be referred to as *invertible* if it belongs to the class of Invertible Words.

This definition is immediately employed to derive the following theorems,

**Theorem 1.3.2** α ∈ I ↔ inv(α) ∈ I

Assume *α ∈ I*. By Definition 1.3.2,

    1. inv(α) ∈ L
    
Consider *inv(α)*. To show that it's invertible, it must be shown,

    2. inv(inv(α)) ∈ L. 

By Theorem 1.2.4,

    3. inv(inv(α)) = α
    
Since it is known *α ∈ L*, it follows,

    4. inv(inv(α)) ∈ L  
    
By the Definition 1.3.2, 

    5. inv(α) ∈ I
    
Therefore, *inv(α)* is also an Invertible Word. ∎ 

**Theorem 1.3.3** R ⊂ I

Assume *α ∈ R*. *𝔞*:sub:`i` be the Characters in *α*. By Definition 1.3.2,

    1. ∀ i ∈ N:sub:`l(α)`: *𝔞*:sub:`i` = *𝔞*:sub:`l(α) - i``

Let *β = inv(α)* and let *𝔟*:sub:`j` be the Characters in *β*. By Definition 1.2.1,

    2. l(β) = l(α)
    3. ∀ i ∈ N:sub:`l(α)`, ∀ j ∈ N:sub:`l(β)``: (j = l(α) - i + 1) →  ( 𝔟:sub:`j` = 𝔞:sub:`i` )

Substitute (*j = l(α) - i + 1 *) into the consequent of the conditional in step 3 and drop the quantification over *j*,

    4. ∀ i ∈ N:sub:`l(α)`:  𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`i`

Substituting the property of Reflective Words from step 2 into step 4,

    5. ∀ i ∈ N:sub:`l(α)`:  𝔟:sub:`l(α) - i + 1` = 𝔞:sub:`l(α) - i`

Note that the index on the left side of the equation in step 5 (*l(α) - i + 1*) corresponds to the character at position *i* in the reversed string *β*.

Since *𝔟*:sub:`l(α) - i + 1` *= 𝔞*:sub:`l(α) - i` for *i ∈* **N**:sub:`l(α)`, and both strings have the same length, we can conclude that each character in *α* is equal to the corresponding character in *β*. Therefore,

    6. α = β = inv(α)

By assumption, *α ∈ L*. From step 6, this implies *inv(α) ∈ L*. By Definition 1.3.2, this implies α ∈ I. In summary, the assumption α ∈ R implies α ∈ I. Therefore, every element in R is also an element in I, which means R ⊂ I. ∎ 

In the context of (potentially) infinite sets such as **L** and **S**, "even" and "odd" refer to whether the set can be partitioned into two disjoint subsets of equal cardinality.

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

**Examples**

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

The work so far has formally constructed a system for representing the first two levels of artifacts from a natural language, Characters (Alphabets) and Words (Language), without appealing to their interpretation in any way except insofar that it takes a stance on their *existence*. As the analysis moves up the chain of linguistic artifacts to the next highest level, Sentences (Corpuses), it is tempting to start incorporating semantic features into the theory. However, the objective is to derive palindromic conditions independent of a particular semantic interpretation. Therefore, as the analysis proceeds, special care will be given to the definition of a *Sentence* and its *Corpus*.

Section II.I: Definitions
-------------------------

In this section, the final level of the semantic hierarchy will be defined. 

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
    2. Sentential Variables (*ζ*): The lowercase Greek letter Zeta is reserved for indeterminate Sentences, i.e. Sentential Variables. Subscripts will occassionally be used in conjunction with Zeta to denote Sentential Variales, (*ζ*:sub:`1`, *ζ*:sub:`2`, ...)
    
**Definition 2.1.2: Sentence** A Sentence in Language **L** is an element of its Corpus. 

    ᚠ ∈ C:sub:`L`

From Definition 2.1 and Definition 2.2, it follows that a Sentence is a String,

    ᚠ ∈ S

It should be noted at this point that Characters, Words and Sentences in the current formulation are elements of the same underlying set, the set of all Strings. This connection in the domain of Characters, Words and Sentences is what will allow the analysis to begin to construct the outline of palindromic structures in a Language and Corpus.

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

**Definition 2.1.5: Sentence Length**

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

This example demonstrates the essential difference in the notions of length that have been introduced. Indeed, the analysis has accumulated a myriad of ways of describing length. It is worthwhile to list them in a descending hierarchy and clarify the distinctions. Let *s* be a String with Character-level representation **S** and Word-level representation **W**:sub:`s`. The hierarchy of its "spatial" dimensions is given below, in order of greatest to least (this fact will be proven in Theorem 2.4.8, after the introduction of the Delimiter Count Function). Terminology is introduced in parenthesis to distinguish these notions of length,

   - | S | (Character Length): The number of Characters contained in a String. 
   - l(s) (String Length): The number of non-Empty Characters contained in a String.
   - Λ(s) (Word Length): The number of Words contained in a String 

Note the first two levels are purely syntactical. Any String *s* will have a length *l(s)* and a cardinality | S |. However, not every String possesses Word length, *Λ(s)*. Word length contains semantic information. While the presence of Word length does not necessarily mean the String is semantic, e.g. "asdf dog fdsa", Word length does signal an *extension* of Strings into the semantic domain.

The following theorem proves an intuitive concept: the total number of Characters in all of the Words in a Sentence must exceed the number of Words in a Sentence (since there are no Words with a negative amount of Characters). 

**Theorem 2.1.1** ∀ ζ ∈ C:sub:`L`:  ∑:sub:`(i, α) ∈ W_ζ` l(α) ≥ Λ(ζ)

This theorem can be stated in natural language as follows: For any sentence *ζ* in a Corpus C:sub:`L`, the sum of the String Lengths of the Words in *ζ* is always greater than the Word Length of *ζ*.

Assume ζ ∈ C:sub:`L`. Let W:sub:`ζ` be the Word-level set representation of *ζ*,

    W:sub:`ζ` = { (1, α:sub:`1`), (2, α:sub:`2`), ..., (Λ(ζ), α:sub:`Λ(ζ)`)}

For each ordered Word (*i*, *α*:sub:`i`) ∈ W:sub:`ζ`, its String Length *l(*α*:sub:`i`)* must be greater 0 by the Empty Axiom W.2 and Definition 1.1.2. Therefore, since each Word contributes at least a String Length of 1, the sum of the lengths of the words in the sentence is greater than or equal to the number of words in the sentence. ∎

**Theorem 2.1.2** ∀ ζ ∈ C:sub:`L`: Λ(ζ) ≥ 1

Proof:

Sentence as a String: By Definition 2.1.2, every Sentence (ζ) is an element of the Corpus (C:sub:L). By Definition 2.1.1, the Corpus is a subset of the set of all Strings (S). Therefore, every Sentence is a String.

Non-empty String: By Definition 1.1.2, the length of a String (l(s)) is the number of non-Empty Characters in the String. Since a Sentence is a meaningful construct in a Language, it must contain at least one non-Empty Character. Therefore, for any Sentence ζ, l(ζ) ≥ 1.

Word Length: By Definition 2.1.6, the Word Length of a Sentence (Λ(ζ)) is defined as the cardinality of its Word-level set representation (W:sub:ζ).

Relationship between Lengths: We have previously proven (using Theorem 2.1.1) that for any Sentence ζ,  |Z| ≥ l(ζ) ≥ Λ(ζ), where |Z| is the Character Length of ζ.

Combining Inequalities: Since l(ζ) ≥ 1 (from step 2) and l(ζ) ≥ Λ(ζ) (from step 4), it follows that Λ(ζ) ≥ 1.

Therefore, every Sentence in a Corpus must have a Word Length of at least 1, meaning it contains at least one Word. ∎

Setion II.II: Sentence Classes 
------------------------------

Similarly to the classification of Words, Sentences will now be classified according to their syntactical properties. In particular, in the study of palindromic structures, the notion of *Invertible Sentences* will be required. The definition, as is fitting in a work focused on palindromes, will mirror the definition of an *Invertible Word*

Invertible Sentences
^^^^^^^^^^^^^^^^^^^^

The notion of Invertible Sentences will first be defined extensionally, and then clarified heuristically. The following definition and theorem mirror the mechanics of Definition 1.3.2 and Theorem 1.3.2 almost exactly.

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

From Theorem 1.2.4, for any string *s*, 

    3. inv(inv(s)) = s.  

By Definition 2.1.1,

    1. ζ ∈ S

Where **S** is the set of all Strings. Therefore, it follows, 

    5. inv(inv(ζ)) = ζ.

From step 1 and step 5, it follows, 

    6. inv(inv(ζ)) ∈ C:sub:`L`

By Definition 2.2.2, this implies,

    7. inv(ζ) ∈ K.

(←) Assume inv(ζ) ∈ K

By Definition 2.2.2, 
    
    8. inv(inv(ζ)) ∈ C:sub:`L`

Applying Theorem 1.2.4,

    9. inv(inv(ζ)) = ζ.

From step 8 and step 9, it follows, 

    10. ζ ∈ C:sub:`L`

By Definition 2.2.2, it follows,

    11. ζ ∈ K. ∎

The notion of Invertible Sentences is not as intuitive as the notion of Invertible Words. This is due to the fact the condition of *invertibility* is not a weak condition; indeed, Sentences that are not invertible far outnumber Sentences that are invertible in a given Language (for all known natural languages, at any rate; it is conceivable purely formal system with no semantic content or general applicability could be constructed with invertibility in mind). 

Consider the following examples phrases from English,

- no time
- dog won 
- not a ton 

All of these phrases may be *inverted* to produce a semantically coherent phrases in English, 

- emit on
- now god
- not a ton 

Note the last item in this list is an example of what this work has termed a *perfect palindrome*. These examples were specially chosen to highlight the connection that exists between the class of *perfect palindromes* and the class of *invertible sentences*. It appears, based on this brief and circumstantial analysis, that *perfect palindromes* are a subset of a larger class of Sentences, Invertible Sentences.

Due to the definition of Sentences as semantic constructs and the definition of Invertible Sentences as Sentences whose Inverses belong to the Corpus, this means Invertible Sentences are exactly those Sentences that maintain *semantic coherence* under inversion (see Section II.III for a definition of *semantic coherence*). In order for a Sentence to be invertible it must possess symmetry on both the Character level and the Word level, while maintaining a semantic structure at the Sentence level that accomodates this symmetry. This connection between the symmetries in the different linguistic levels of an Invertible Sentence will be formalized and proven in Theorem 2.3.4 of the next section.

To see how strong of a condition invertibility is, the author challenges the reader to try and construct an invertible sentence. Section IV contains a list of Invertible Words and Reflective Words. These can be used as a "palette" for the exercise. The exercise is worthwhile, because it forces the reader to think about the mechanics of sentences and how a palindrome resides in the intersection of semantics and syntax.  

Section II.III: Axioms 
----------------------

In Section I, the first three axioms of the palindromic formal system were introduced. Now that definitions and notations have been introduced for Sentence and Corpus, the axioms may be expanded to further refine the character of the formal system being built. The Character, Delimiter and Empty Axiom are reprinted below, so they may be considered in sequence with the other axioms.

**Axiom C.1: The Character Axiom**

    ∀ ⲁ ∈ Σ: ⲁ ∈ S

**Axiom W.1: The Delimiter Axiom ** 

    ∀ α ∈ L: ∀ i ∈ *N*:sub:`l(s)`: 𝔞:sub:`i` ≠ σ 

**Axiom S.1: The Containment Axiom**

    ∀ α ∈ L : ∃ ζ ∈ C:sub:`L`: α  ⊂:sub:`s` ζ

**Axiom S.2: The Extraction Axiom**

    ∀ ζ ∈ C:sub:`L` : ∀ i ∈ N:sub:`Λ(ζ)`: (i, α:sub:`i`) ∈ W:sub:`ζ` → α:sub:`i` ∈ L

Note the Delimiter Axiom has been revised to quantify over a Language, rather than quantifying over **S** while making the quantified expression conditional on the String belonging to a Language. 

It is worth taking the time to analyze the structure, however minimal, these axioms imply must exist in any Language. It should be re-iterated that no assumptions have been made regarding the semantic content of a Language or its Corpus, so any insight that arises from these axioms is due to inherent linguistic structures. 

To briefly summarize the axioms so far introduced: The system "*initializes*" with the selection of the Alphabet **Σ**. The Character Axiom ensures the domain of all Strings is populated. The Delimiter Axiom ensures Words only traverse the set of Strings which do not contain Delimiters. With these axioms, still nothing has been said about *what* a Word is, except that it possesses a semantic character. 

The new axioms introduced in the formal system begin to characterize the syntactical properties of the next level in the lingustic hierarchy, while still maintaining their ambivalence on the semantic content contained within their respective categories. Axiom S.1 asserts that for every Word in a Language there is at least one Sentence in a Corpus that contains it. In other words, a Word cannot exist in a Language without being included in a Sentence. This Axiom captures an inextricable link between the metamathematical concepts of Sentence and Word: one cannot exist without implying the existence of the other. Words and Sentences do not exist in isolation.

Axiom S.2 states that a Corpus of a Language only consists of those Sentences whose constituent Words are members of the Language. Special terminology to describe the concept captured in this axiom is given in the following definition. This term will be used to describe both Sentences and Corpuses.

**Definition 2.3.1: Sentence-Level Semantic Coherence** 

A Sentence *ᚠ* is *semantically coherent* in a Language **L** if and only if its Word-level set representation **ᚠ** only contains words from Language **L**.

**Definition 2.3.2: Corpus-Level Semantic Coherence**

A Corpus C:sub:`L` is *semantically coherent* in a Language **L** if and only if the Word-level set representation of all its Sentences are semantically coherent.

**Definition 2.3.3: Sentence Language**

A Sentence Language is defined as the set of unique Words which are contained in a Sentence *ζ*. **L**:sub:`ζ` denotes a Sentence Language.  

   α ∈ L:sub:`ζ` ↔ ∃ i ∈ N:sub:`Λ(ζ)`: (i, α) ∈ W:sub:`ζ`

These axioms are used to prove the following theorems.

**Theorem 2.3.1** ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L

This theorem can be stated in natural language as follows: For any Sentence *ζ* in a Corpus **C**:sub:`L`, its Sentence Language is a subset of the Language **L**.

Assume *ζ ∈* **C**:sub:`L`. W:sub:`ζ` be the Word-level set representation of *ζ*, as specified in Definition 2.1.3. By Axiom S.2, every Word *α* in the Word-level set representation of *ζ* belongs to the Language **L**. Since every ordered element of W:sub:`ζ` that belongs to **L** also belongs to L:sub:`ζ` by Definition 2.3.3, it can concluded that L:sub:`ζ`  is a subset of **L**. The only assumption on *ζ* is that is belongs to the Corpus, therefore this conclusion can be generalized to all Sentences in a Corpus,

    ∀ ζ ∈ C:sub:`L`: L:sub:`ζ` ⊂ L 
    
In other words, every (Word-level set representation of a) Sentence from a Corpus is a subset of the Language **L**. ∎

**Theorem 2.3.2** ∀ ζ ∈ C:sub:`L`, ∀ t ∈ S: ¬[ (t = ε) ∧ (t ⊂:sub:`s` ζ) ]

Proof:

Let ζ be an arbitrary Sentence in C:sub:L and let t be an arbitrary String in S.

Assume, for the sake of contradiction, that (t = ε) ∧ (t ⊂:sub:s ζ).

Since t ⊂:sub:s ζ, by Definition 1.1.4 of Containment, there exists a strictly increasing and consecutive function f: N:sub:l(t) → N:sub:l(ζ) such that ∀ i ∈ N:sub:l(t): 𝔞:sub:i = 𝔟:sub:f(i), where 𝔞:sub:i represents the Characters in t and 𝔟:sub:f(i) represents the Characters in ζ.

However, since t = ε, by Definition 1.1.2 of String Length, l(t) = 0. This implies that N:sub:l(t) = ∅ (the empty set).

Since N:sub:l(t) = ∅, the function f in step 2 cannot exist, as there are no elements in the domain to map to the codomain.

This contradicts our assumption in step 2 that such a function f exists.

Therefore, our initial assumption in step 1 that (t = ε) ∧ (t ⊂:sub:s ζ) must be false.

Hence, ¬[ (t = ε) ∧ (t ⊂:sub:s ζ) ] is true.

Since ζ and t were arbitrary, we can generalize this result:

∀ ζ ∈ C:sub:L, ∀ t ∈ S: ¬[ (t = ε) ∧ (t ⊂:sub:s ζ) ] ∎

(TODO: trim)




**Theorem 2.3.3** ζ ∈ K → ( ∀ α ∈ W:sub:`inv(ζ)`: α ∈ L)

This theorem can be stated in natural language as follows: If a Sentence *ζ* is invertible, then every word in its inverse, *inv(ζ)*, belongs to the Language **L**.

Assume *ζ ∈ K*. By Definition 2.2.2,

    inv(ζ) ∈ C:sub:`L`

By Axiom S.3, every Word in the Word-level representation of inv(ζ) belongs to L. ∎




Example:

Consider the Sentence ζ = "This is a test."

Its Character-level representation is:

Z = (T, h, i, s, σ, i, s, σ, a, σ, t, e, s, t, .)

Now, let's reverse Z to get the Character-level representation of inv(ζ):

Reverse(Z) = (., t, s, e, t, σ, a, σ, s, i, σ, s, i, h, T)

Notice that the Delimiters (σ) still appear at the same indices in both Z and Reverse(Z), just in reversed order.

In Z, the Delimiters are at indices 4, 7, and 9.
In Reverse(Z), the Delimiters are at indices 9, 7, and 4 (counting from the beginning of the reversed string).
Why this happens:

When we reverse a String at the Character level, we're essentially flipping the order of all Characters. This includes the Delimiters.  So, while the sequence of Delimiters is reversed, their positions relative to the beginning and end of the String remain the same.

Implications for the Delimiting Algorithm:

Since the Delimiting Algorithm identifies Words based on Delimiter positions, this means that when we apply the algorithm to the reversed Character-level representation, we'll still get the same Words, but in reversed order and inverted.

This is why the Word-level representation of inv(ζ) in Corollary 2.3.4.1 is the reordered inverses of the Words in ζ.

In our example:

Applying the Delimiting Algorithm to Z gives us:

W:sub:ζ = ("This", "is", "a", "test")

Applying the Delimiting Algorithm to Reverse(Z) gives us:

W:sub:inv(ζ) = ("tset", "a", "si", "siht")




Corollary 2.3.4.1:

Let ζ be a Sentence in C:sub:L with Word-level representation:

W:sub:ζ = (α:sub:1, α:sub:2, ..., α:sub:Λ(ζ))

Then, the Word-level representation of inv(ζ) is:

W:sub:inv(ζ) = (inv(α:sub:Λ(ζ)), inv(α:sub:Λ(ζ)-1), ..., inv(α:sub:1))

Proof:

Character-level representation: Let Z be the Character-level representation of ζ. By Definition 1.2.1 (String Inversion), the Character-level representation of inv(ζ) is the reverse of Z.

Delimiter positions: The Delimiters in Z and the reverse of Z appear at the same indices, just in reversed order.

Word boundaries:  Since the Delimiting Algorithm (Definition 2.1.4) identifies Words based on Delimiter positions, the Words in inv(ζ) will be the inverses of the Words in ζ, but in reversed order.

Word-level representation: This implies that the Word-level representation of inv(ζ) is indeed the reordered inverses of the Words in ζ, as stated in the corollary. ∎



**Theorem 2.3.4** ζ ∈ K → (∀ α ∈ W:sub:`ζ`: α ∈ I)

This theorem can be stated in natural language as follows: A Sentence is Invertible if its Words are Invertible.

Assume *ζ ∈* **K**. Consider the Word-level representation of *ζ*.

    1. W:sub:`ζ` = ( α:sub:`1`, α:sub:`2`, ... , α:sub:`Λ(ζ)`)

By Definition 1.2.1 AND THE THEOREM PROVED ABOVE, the Word-level representation of *inv(ζ)* is 

    3. W:sub:`inv(ζ)` = ( inv(α:sub:`Λ(ζ)`), inv(α:sub:`Λ(ζ)-1`), ... , inv(α:sub:`1`) )

By Theorem 2.2.3, every Word in *inv(ζ)* belongs to **L**.  Therefore, each inv(α:sub:`i`) belongs to **L**,

By the Definition 1.3.2, each α:sub:`i` ∈ I. Therefore, all words in ζ are invertible. Formally,

    4. (∀ α ∈ L:sub:`ζ`: α ∈ I) ∎

The contrapositive of Theorem 2.2.4 provides a schema for searching for Invertible Sentences. If any of Words in a Sentence are not Invertible, then the Sentence is not Invertible. In other words, it suffices to find a single word in a Sentence that is not Invertible to show the entire Sentence is not Invertible.

Section II.IV: Delimiting
--------------------------

Now that the analysis has breached the level of Sentences, it begins to turn explicitly towards the consideration of palindromes and their structure. The next section will formally define palindromes and their properties. As preparation, this subsection will introduce an important tool that will be used to build the theorems which in turn will be used to classify palindromes and provide insight into their structure.

Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a palindrome is distributed through its syntactical layers. The concepts of *perfect* and *imperfect* palindromes will be defined more rigorously in the following Section III, but as an intuitive introduction to this distinction and to help highlight the ability of a palindrome to encode meaning on multiple syntactic levels, consider the following two examples,

    1. Dennis sinned
    2. If I had a hifi

The first palindrome "*Dennis sinned*" is what will be termed a *perfect* palindrome, because its inverse does not require a rearrangement of its constituent Characters to preserve its semantic content. However, the second palindrome "If I had a hifi" is what will be termed an *imperfect* palindrome. To see the motivation behind this categorization, note the strict inversion of "If I had a hifi" would be (ignoring capitalization for now),

    Ifih a dah I fi

The order of the Characters in the Inverse of an imperfect palindrome is preserved, but in order to reconstitute its uninverted form, the Delimter Characters must be re-sorted. It appears, then, that Delimiters play a central role in organizing the palindromic structure. In order to fully elucidate the structure of palindromes, it will be necessary to introduce into the discourse a method of referring to a Sentence's Delimiter count. 

Delimiter Count Function 
^^^^^^^^^^^^^^^^^^^^^^^^

As the introduction to this subsection made clear, it will be necessary to have a way of referencing the number of Delimiter Characters in a Sentence. Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.

**Definition 2.4.1: Delimiter Count Function** Let *t* be a String with length *l(t)*. Let *𝔞*:sub:`i` represent the *i*:sup:`th` character of the String *t*, where 

    i ∈ N:sub:`l(t)` = { 1, 2, ..., l(t) }.

The delimiter count function, denoted by *Δ(t)*, is defined as the number of Delimiter characters (*σ*) in the string *t*. Formally, *Δ(t)* is defined as the cardinality of the set **D**:sub:`t` that satisfies the following formula:

    (j, ⲁ) ∈ D:sub:`t` ↔ (∃ i ∈ N:sub:`l(t)` ( (i, ⲁ) ∈ T ) ∧ (ⲁ = σ) ∧ (j = i) )

where **T** is the set representation of the String *t*, 

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

Then, the delimiter count function is defined as

    Δ(t) = | D:sub:`t` |

**Example** Consider the string *t = "a b c"*. The set representation of *t* is given by,
    
    T = { (1, a), (2, σ), (3, b), (4, σ), (5, c) }.

The set D:sub:`t` contains the ordered pairs *(2, σ)* and *(4, σ)*, where the first coordinate of the pair correspond the positions of the two Delimiter Characters in the String. Therefore, 
    
    D:sub:`t`= { (2, σ), (4, σ) }

From this it follows, | D:sub:`t` | is 2. Hence, *Δ(s) = 2*.

From this example, it can be seen the Delimiter Count function takes a Sentence as input and produces a non-negative integer (the delimiter count) as output. Multiple sentences can have the same delimiter count, making it a many-to-one function. While this many not be advantageous from a computational perspective, the Delimiter Count function has other interesting properties that make it worth studying. The following theorems describe some of its properties.

**Theorem 2.4.1** ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1

In natural language, this theorem is stated: For any sentence *ζ* in a Corpus C:sub:`L`, the length of the Sentence is equal to its delimiter count plus one.

Assume *ζ ∈* **C**:sub:`L`. Let *Δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the character-level representation of ζ. Let **W**:sub:`ζ` be the word-level set representation of ζ. Recall **W**:sub:`ζ` is formed by splitting **Ζ** at each Delimiter Character *σ*.

Each word in **W**:sub:`ζ` corresponds to a contiguous subsequence of non-delimiter characters in **Ζ**.

Since delimiters separate words, the number of words in the sentence is always one more than the number of spaces.

herefore, the cardinality of **W**:sub:`ζ` (the number of words) is equal to the delimiter count of *Δ(ζ)* plus one,

    | W:sub:`ζ` | = Δ(ζ) + 1. ∎

A more explicit version of Theorem 2.4.1 is given below using the Delimit Algorithm.

**Theorem 2.4.1 (Explicit Version)** ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1

Assume *ζ ∈* **C**:sub:`L`. Let *Δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the character-level representation of ζ. Let **W**:sub:`ζ` be the word-level set representation of ζ. By Definition 2.1.3, **W**:sub:`ζ` is constructed using the Delimiting Algorithm. 

The algorithm starts with an empty set **W**:sub:`ζ` and  *j = 0*.

In each iteration, the algorithm identifies a Word *a* in **Ζ** that starts at index j + 1 and ends either at a Delimiter or the end of the Sentence.

The pair (j + 1, *a*) is added to **W**:sub:`ζ`

The index *j* is incremented by the length of the Word *a*, *l(a)*.

Every time a Word is added to **W**:sub:`ζ`, the algorithm encounters exactly one delimiter (except for the last word, where it encounters the end of the sentence).

The algorithm terminates when all characters in Ζ have been processed.

Therefore, the number of words added to **W**:sub:`ζ` is exactly one more than the number of delimiters encountered.

By Definition 2.4.1, Δ(ζ) counts the number of delimiter characters in *ζ*. By Definition 2.1.6,  Λ(ζ) = | W:sub:`ζ` | (the number of words in *ζ*).

Hence, Λ(ζ) = Δ(ζ) + 1. ∎

The next theorem will be important for describing the structure of *imperfect palindromes*.

**Theorem 2.4.2** *Δ(s) = Δ(inv(s))*

Let *t* be a string with length *l(t)* and Characters denoted by *𝔞*:sub:`i`. Let **T** be the set representation of of *t* is given by,

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

Let *u = inv(t)* with Characters denoted by let *𝔟*:sub:`j`. By Definition 1.2.1,

    1. l(t) = l(u)
    2. ∀ i ∈ N:sub:`l(t)`, ∀ j ∈ N:sub:`l(u)`: [ ( j = l(s) - i + 1 ) → ( 𝔟:sub:`j` = 𝔞:sub:`i` ) ]

Let **D**:sub:`t` be the set of ordered pairs representing the positions of the Delimiter *σ* in *t*, and let D:sub:`u` be the corresponding set for *u*.

Assume *(j, σ) ∈*  **D**:sub:`u` . This means that the character at position *j* in the inverse string *t* is the Delimiter *σ*.

By the definition, *𝔟*:sub:`j` = *𝔞*:sub:`i` where *j = l(t) - i + 1*.  Since *𝔟*:sub:`j` *= σ*, we have *𝔞*:sub:`i`  *= σ*. This implies that the character at position *i* in the original string *t* is also a Delimiter.  Therefore, *(i, σ) ∈* **D**:sub:`t`

Thus, it is shown that for every element *(j, σ) ∈*  **D**:sub:`u`, there exists a corresponding element *(i, σ) ∈* **D**:sub:`t`, where *j = l(t) - i + 1*. This defines a one-to-one mapping between the elements of **D**:sub:`u` and **D**:sub:`t`. Since there's a one-to-one mapping between the elements of *D**:sub:`u` and **D**:sub:`t`, their cardinalities must be equal,

    3. | D:sub:`u` | = | D:sub:`s` |

By the definition of the delimiter count function, this means *Δ(u) = Δ(t)*. Since *u = inv(t)*, it has been shown *Δ(inv(s)) = Δ(s)*. ∎

**Theorem 2.4.3** Δ(ζ) = Δ(inv(ζ))

Definition 2.1.2, every Sentence is a String. Therefore, *ζ* is a String. By Theorem 2.4.2, 

    Δ(ζ) = Δ(inv(ζ))

Which is what was to be shown. ∎

**Theorem 2.4.4** ∀ α ∈ L: Δ(α) = 0

Assume α ∈ L. By the Axiom W.1, if a string *s* belongs to the Language **L**, then it does not contain any Delimiter Characters

    s ∈ L → (∀ i ∈ N:sub:`l(s)`: 𝔞:sub:`i` ≠ σ )

Therefore, *α* does not contain any Delimiter Characters (*σ*). By Definition 2.4.1, *Δ(s)* counts the number of Delimiter Characters (*σ*) in a String *s*. Since *α* contains no Delimiter Characters, the delimiter count of *α* must be 0. Therefore, *Δ(α) = 0*. ∎

**Theorem 2.4.5** ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`(i, α) ∈ W_ζ` l(α)

In natural language, this theorem can be stated as follows: For every Sentence *ζ* in a Corpus C:sub:`L`, the String Length of the Sentence *l(ζ)* is equal to the delimiter count of the sentence *Δ(ζ)* plus the sum of the String Lengths of its Words.

Assume *ζ ∈* **C**:sub:`L`. Let **Ζ** be the Character-level representation of *ζ*,

    1. **Z** = { (1, ⲁ:sub:`1`), (2, ⲁ:sub:`2`), ..., (l(ζ), ⲁ:sub:`l(ζ)`) }

Either each α:sub:`i` for i = 1, 2, ...,  l(ζ) is Delimiter or it is a non-Delimiter, with no overlap.

By Definition 2.4.1, the number of Delimiter Characters in *ζ* is Δ(*ζ*). 

By Axiom W.1 (Delimiter Axiom), words in **L** do not contain Delimiters. By Definition 2.1.3, the words in **W**:sub:`ζ` are obtained by splitting *ζ*  at the Delimiters. Therefore, the total number of non-Delimiter characters in *ζ* is the sum of the lengths of the words in *W**:sub:`ζ`, which is *Σ*:sub:`(i, α) ∈ W_ζ` l(α).

Since every Character in *ζ* is either a Delimiter or a non-Delimiter (and not both), the total number of Characters in *ζ*is the sum of the number of delimiters and the number of non-delimiters. Therefore, the number of Characters in *ζ* is equal to the number of Delimiters plus the sum of the lengths of the words in *W**:sub:`ζ`.  

    1. ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`(i, α) ∈ W_ζ` l(α) ∎

**Theorem 2.4.6** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`α ∈ W_ζ` l(α)

Applying the results of Theorem 2.4.1 and Theorem 2.4.5, this theorem follows from simple algebraic manipulation. ∎

**Theorem 2.4.7** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Σ:sub:`(i, α) ∈ W_ζ` l(α)

Assume *ζ ∈* **C**:sub:`L`. By Theorem 2.1.2,
    
    1. Λ(ζ) ≥ 1

From Theorem 2.4.6,

    2. l(ζ) + 1 - Σ:sub:`α ∈ W_ζ` l(α) = Λ(ζ)

Combining step 1 and step 2, the theorem is obtained through simple algebraic manipulation,

    l(ζ) ≥ Σ:sub:`(i, α) ∈ W_ζ` l(α) ∎

**Theorem 2.4.8** ∀ ζ ∈ C:sub:`L`: | Z | ≥ l(ζ) ≥ Λ(ζ)

Let ζ be an arbitrary Sentence in C:sub:`L`.

1. To show | Z | *≥ l(ζ)*: 

| Z | represents the total number of Characters in the Sentence (Character Length), including Delimiters and Empty Characters (if any). *l(ζ)* represents the number of non-Empty Characters in the Sentence. Since | Z | counts all Characters, while *l(ζ)* only counts a subset of those Characters, it follows that |Z| *≥ l(ζ)*.

2. To show *l(ζ) ≥ Λ(ζ)*: 

Let **W**:sub:`ζ`` be the Word-level representation of *ζ*. By Definition 2.1.6, *Λ(ζ) = *| W:sub:`ζ` |, which is the number of Words in *ζ* (Word Length). By Theorem 1.2.3, each Word in **W**:sub:`ζ` consists of one or more non-Empty Characters.

Therefore, the total number of non-Empty Characters in *ζ*, *l(ζ)* (String Length), must be greater than or equal to the number of Words in *ζ*, *Λ(ζ)*. This can be more formally expressed using Theorem 2.1.1: 

    ∑:sub:`(i, α) ∈ W_ζ` l(α) ≥ Λ(ζ)

By Theorem 2.4.7, the result is obtained,

    l(ζ) ≥ Λ(ζ).

Combining (1) and (2): 

    | Z | ≥ l(ζ) ≥ Λ(ζ).

Therefore, for any Sentence ζ ∈ C:sub:`L`, the Character Length is greater than or equal to the String Length, which is greater than or equal to the Word Length. ∎

Section III: Palindromic Structures
===================================

As mentioned in the introduction of this work, the complete structure of palindromes is described through the combination of four different attributes or dimensions: *aspect*, *parity*, *case* and *punctuality*. The framework has now been developed to classify the first two palindromic properties with more precision.

Unfortunately, as far as the author knows, punctuation and capitalization are syntactic bearers of semantic meaning that cannot be reduced to purely formal considerations. Both punctuality and case require additional axioms to describe the unique structuring they impose on a Language and its Corpus. In the author's opinion, it is impossible to disentangle these linguistic phenomenon from the realm of semantics.

In what follows, two things are implicitly assumed. These assumptions are made explicit here, so the scope of the results can be properly understood. First, the Alphabet **Σ** is assumed to contain no punctuation marks beyond the Delimiter Character (if one is inclined it to consider a form of punctuation). Second, it is assumed every Character in **Σ** is distinct, meaning all matters of case are ignored. To rephrase the same idea more precisely: there is no assumed semantic relation between Characters in the Alphabet that would allow the identification of distinct Characters as different *cases* of the same Character.

With these assumptions, the analysis is confined to the dimensions of *aspect* and *parity*, which will be defined in the following subsections. After the results are derived, consideration will be given to future work that could potentially integrate semantic considerations into the formal framework of palindromic structures to account for the dimensions of punctuality and case.

Section III.I: Palindromes 
--------------------------

The study of palindromes will revolve around a novel linguistic operation, termed a *σ-reduction*. This operation will allow the semantic content of a palindrome to be projected onto an Alphabet that preserves the order of its Characters under String Inversion, allowing for a precise definition of a palindrome within purely formal language.

σ-Reductions
^^^^^^^^^^^^

Before defining a *σ-reduction*, the preliminary concept of a *σ-reduced Alphabet* must be introduced. The following definition serves as the basis for constructing the operation of *σ-reduction*.

As has been seen with examples of *imperfect palindromes* like "Borrow or rob", a palindromic structure can have its Delimiter Character scrambled in the inversion of its form, making it lose semantic coherence. *Imperfect palindromes* must be rearranged Delimter-wise to retrieve the original form. However, String Inversion preserves the relative order of the non-Delimiter Characters in a palindromic String, so the process of reconstitution is only a matter of resorting the Delimiter characters. This invariance of the Character order, while the Word order is scrambled by Delimiter, suggests palindromes might be more easily defined without the obstacle of the Delimiter.

**Definition 3.1.1: σ-Reduced Alphabet**

A *σ-reduced Alphabet* is an Alphabet Σ that has had its Delimiter character removed, so that it only consists of non-Delimiter characters. A sigma-reduced Alphabet is denoted Σ:sub:`σ`. Formally

    Σ:sub:`σ` = Σ - {σ}

In order to define palindromes in all of their varieties, perfect or imperfect, the semantic incoherence that is introduced by the inversion of imperfect palindromes must be removed. This is accomplished through the introduction of the operation of *sigma reduction*.

**Definition 3.1.2: σ-Reduction**

Let *s* be a String with length *l(s)* and Character-level representation 

    1. S = { (1,𝔞:sub:`1`) , (2, 𝔞:sub:`2`) , ... , (l(s), 𝔞:sub:`l(s)`) } 
    2. 𝔞:sub:`i` ∈ Σ.

The *σ-reduction* function (or simply, the *σ-reduction*), denoted by *S ⋅ Σ*:sub:`σ`, maps the String *s* to a new String *t* in the *σ*-reduced alphabet **Σ**:sub:`σ` by removing all occurrences of the Delimiter Character. Formally, *S ⋅ Σ*:sub:`σ` is defined and constructed using the *σ-Reduction Algorithm*,

**σ-Reduction Algorithm**

**Initialization** 

- Let t be the empty string, *t = ε*.

**Iteration**

- For each Character *𝔞*:sub:`i` in **S**, if *𝔞*:sub:`i` ≠ σ, then concatenate *𝔞*:sub:`i` to the end of *t*.

**Example**

Let *s = "a b c"* be a String from the Alphabet *Σ = { "", " " , "a", "b", "c" }*. Note in this example *σ = " "*. The sigma reduction of *s* is given by,

    S = (a, σ, b, σ, c)
    
    Σ' = { "", "a", "b", "c" }

    S ⋅ Σ' = "abc"

The notation for sigma reduction is meant to evoke the idea of a vector dot project. The analogy to a vector projection is indeed apt. While not a strict mathematical equivalence, it captures the idea of transforming the string from its original form (with Delimiters) onto a reduced space (without Delimiters), similar to how a vector can be projected onto a subspace.

The *σ*-reduced alphabet (**Σ**:sub:`σ`) can be seen as a subspace within this higher-dimensional space, consisting of only the non-Delimiter dimensions. The sigma reduction function (**S ⋅ Σ**:sub:`σ`) acts as a projection operator, mapping the String onto this subspace by eliminating the components corresponding to the Delimiter character (*σ*).

Note that a *σ-reduction* is not a one-to-one operation. It is possible for the *σ-reduction* of a palindrome to map onto a totally different sentence, not necessarily a palindrome.

As an example, consider the (partial, ignoring punctuality) Palindromes *ᚠ = "madam im adam"* and *ᚢ = "mad am i madam"*. The *σ-reduction* of both of these Sentences would map to the *σ-reduced* value of *madamiadam".

Both the Palindrome and the alternative Sentence have the same *σ-reduction*, despite having different meanings and grammatical structures. This highlights the ambiguity that can arise from removing spaces, as the original word boundaries and sentence structure are lost.

During a *σ-reduction*, information in lost with respect to the following semantic categories,

  - Word Boundaries: The spaces between words, which are crucial for parsing and understanding the sentence, are eliminated.
  - Sentence Structure: The grammatical structure of the sentence, the relationships between words and phrases, becomes ambiguous.
  - Prosody and Rhythm: The pauses and intonation that contribute to the meaning and expression of the sentence are lost.

However, some semantic information is preserved. The individual words themselves, or at least their character sequences, remain present in the *σ-reduced* string. The next theorem proves semantic content is retained during the *σ-reduction* of a Sentence.

**Theorem 3.1.1** ∀ ζ ∈ C:sub:`L`, ∃ α ∈ L: α ⊂:sub:`s` ( Ζ ⋅ Σ:sub:`σ` )

This theorem can be stated in natural language as follows: Given the *σ-reduction* of a Sentence, there exists a Word in its Language that is contained in the *σ-reduced* string.

Assume *ζ ∈ C*:sub:`L`. Let **Ζ** be the Character-level set representation of *ζ*.

By the Axiom of Word Extraction (S.3),

    1. ∀ ζ ∈ C*:sub:`L`, ∀ α ∈ W:sub:`ζ`: α ∈ L.

Since *ζ* is a sentence, by Theorem 2.1.3,it must contain at least one word. Therefore, W:sub:`ζ` is not empty. Let *α* be any word in **W**:sub:`ζ`:.

By Definition 2.1.3 of the Word-level set representation, *α* is a contiguous subsequence of non-Delimiter Characters in **Ζ**.  

Now, let's formally show that α is contained in Ζ ⋅ Σ:sub:σ:

Representations: Let A = (𝔞:sub:1, 𝔞:sub:2, ..., 𝔞:sub:l(α)) be the Character-level representation of α. Let Z' = (𝔟:sub:1, 𝔟:sub:2, ..., 𝔟:sub:l(Ζ ⋅ Σ:sub:σ)) be the Character-level representation of Ζ ⋅ Σ:sub:σ.

Constructing the function: Since α is a contiguous subsequence of non-Delimiter Characters in Ζ, there exists an index k such that:

𝔞:sub:1 = 𝔟:sub:k
𝔞:sub:2 = 𝔟:sub:k+1
...
𝔞:sub:l(α) = 𝔟:sub:k+l(α)-1
Define the function f: N:sub:l(α) → N:sub:l(Ζ ⋅ Σ:sub:σ`) as f(i) = k + i - 1.

Strictly increasing and consecutive: The function f is clearly strictly increasing and consecutive, as it maps consecutive indices in α to consecutive indices in Ζ ⋅ Σ:sub:σ.

Satisfying containment:  By construction, f satisfies the condition ∀ i ∈ N:sub:l(α): 𝔞:sub:i = 𝔟:sub:f(i).

Therefore, by Definition 1.1.4 of Containment, α ⊂:sub:s (Ζ ⋅ Σ:sub:σ). ∎

(TODO: trim)

Corollary 3.1.2.1: Let s and t be Strings. Then, inv(st) = inv(t)inv(s).

Proof:

Character-level representations:

Let S = (𝔞₁ , 𝔞₂ , ..., 𝔞ₗ₍ₛ₎) be the Character-level representation of s.
Let T = (𝔟₁ , 𝔟₂ , ..., 𝔟ₗ₍ₜ₎) be the Character-level representation of t.
Concatenation: The Character-level representation of st is:

ST = (𝔞₁ , 𝔞₂ , ..., 𝔞ₗ₍ₛ₎, 𝔟₁ , 𝔟₂ , ..., 𝔟ₗ₍ₜ₎)

Inversion of concatenated string: By Definition 1.2.1 (String Inversion), the Character-level representation of inv(st) is the reverse of ST:

inv(ST) = (𝔟ₗ₍ₜ₎, ..., 𝔟₂ , 𝔟₁ , 𝔞ₗ₍ₛ₎, ..., 𝔞₂ , 𝔞₁)

Inversion of individual strings:

The Character-level representation of inv(s) is (𝔞ₗ₍ₛ₎, ..., 𝔞₂ , 𝔞₁).
The Character-level representation of inv(t) is (𝔟ₗ₍ₜ₎, ..., 𝔟₂ , 𝔟₁).
Concatenation of inverted strings:  The Character-level representation of inv(t)inv(s) is:

(𝔟ₗ₍ₜ₎, ..., 𝔟₂ , 𝔟₁ , 𝔞ₗ₍ₛ₎, ..., 𝔞₂ , 𝔞₁)

Equality: Comparing the results from step 3 and step 5, we see that the Character-level representations of inv(st) and inv(t)inv(s) are identical.

Therefore, inv(st) = inv(t)inv(s). ∎



**Theorem 3.1.2** ∀ ζ ∈ C:sub:`L` : ζ ∈ K → [ inv(Ζ ⋅ Σ:sub:`σ`) = inv(inv(Ζ ⋅ Σ:sub:`σ`)) ]

In natural language, this theorem can be stated in natural language as follows: If a Sentence in a Corpus is invertible, then its invertibility is invariant under *σ-reduction*.

Theorem 3.1.2: ∀ ζ ∈ C:sub:L : ζ ∈ K → [ inv(Ζ ⋅ Σ:sub:σ) = inv(inv(Ζ ⋅ Σ:sub:σ)) ]

Proof:

Assume ζ ∈ C:sub:L and ζ ∈ K (ζ is an invertible Sentence).

Word-level representation: Let the Word-level representation of ζ be:

W:sub:ζ = (α₁ , α₂ , ..., αₙ)  where n = Λ(ζ)

Invertible words: By Theorem 2.3.4, since ζ is invertible, all its Words are also invertible: ∀ i ∈ N:sub:n: αᵢ ∈ I.

σ-reduction:

The σ-reduction of ζ, (Ζ ⋅ Σ:sub:σ), is obtained by removing all Delimiters from ζ.

Since no Word contains Delimiters (Axiom W.1), the σ-reduction essentially concatenates the Words in W:sub:ζ:

Ζ ⋅ Σ:sub:σ = α₁α₂...αₙ

Inversion of σ-reduced string: Applying Corollary 3.1.2.1 repeatedly, we get:

inv(Ζ ⋅ Σ:sub:σ) = inv(α₁α₂...αₙ)
= inv(αₙ)...inv(α₂) inv(α₁)

Double inversion: Now, let's invert the result from step 4:

inv(inv(Ζ ⋅ Σ:sub:σ)) = inv(inv(αₙ)...inv(α₂) inv(α₁))
= inv(inv(α₁))inv(inv(α₂))...inv(inv(αₙ))  (by Corollary 3.1.2.1)
= α₁α₂...αₙ  (by Theorem 1.2.4, inv(inv(s)) = s)

Equality:  We see that inv(inv(Ζ ⋅ Σ:sub:σ)) = α₁α₂...αₙ, which is the same as Ζ ⋅ Σ:sub:σ from step 3.

Therefore, inv(Ζ ⋅ Σ:sub:σ) = inv(inv(Ζ ⋅ Σ:sub:σ)). ∎



The contrapositive of this theorem, much like the contrapositive of Theorem 2.3.4, provides a schema for searching the *σ-reduced* space. The domain of this space, what will be termed the σ-Pairing Language in the next section, reduces the complexity of searching for palindromic strings. Potential palindromic candidates can be projected into the *σ-reduce* spaced, and then filtered by those whose Palindromic Pair Inverse in the Pairing Language does not equal itself. 

These ideas will be expounded until in Section III.III, when the theorems and results of this work are used to implement a Palindrome search algorithm.

Aspect
^^^^^^

The current analysis now turns towards its apex, using the notions that have been developed up to this point to define the mathematical structure of Palindromes. To motive the next definition, consider how the operation of *σ-reduction* "*projects*" Palindromes onto an Alphabet where their symmetry is preserved.

Consider a perfect palindromes like *ᚠ = "strap on no parts"*,

    **ᚠ** ⋅ Σ:sub:`σ`= "straponnoparts"

    inv( **ᚠ** ⋅ Σ:sub:`σ` ) = "straponnoparts"

In other words, the *σ-reduction* and the inversion of its *σ-reduction* space result in the same String.

Consider an imperfect palindrome like *ᚢ = "borrow or rob"*,

    **ᚢ** ⋅ Σ:sub:`σ`= "borroworrob"

    inv( **ᚢ** ⋅ Σ:sub:`σ` ) = "borroworrob"

Again, the *σ-reduction* eliminates the Delimiters, and the inversion of the *σ-reduction* captures the mirrored relationship between the words, even if the exact Character sequence isn't identical.

These examples lead directly to the next, important definition.

**Definition 3.1.2: Palindromes**

Palindromes are defined as the set of Sentences **P** that satisfy the following formula,

    ζ ∈ P ↔ [ (Ζ ⋅ Σ:sub:`σ`) = inv(Ζ ⋅ Σ:sub:`σ`) ]

This definition distills the core property of Palindromes, their symmetrical nature, by focusing on the sequence of Characters without the ambiguity of Delimiters. The use of set notation and logical operations provides a mathematically rigorous and unambiguous definition.

Moreover, this definition can be easily adapted to different languages by simply defining the appropriate Alphabet **Σ** and the corresponding *σ-reduced* alphabet **Σ**:sub:`σ`

It highlights the concept of invariance under transformation. A Palindrome remains a Palindrome even when projected onto the *σ-reduced* Alphabet, demonstrating a kind of structural integrity that's independent of the specific representation.

The condition (ζ ⋅ Σ:sub:`σ`) = inv(ζ ⋅ Σ:sub:`σ`) can be seen as defining an equivalence relation on the set of Sentences, where two Sentences are equivalent if they are Palindromes of each other in the *σ-reduced* space.

**Definition 3.1.3: Perfect Palindromes**

Perfect Palindromes are defined as the set of Sentences **PP** that satisfy the following formula,

    ζ ∈ PP ↔ ζ = inv(ζ)

Note the name given to this class of Sentences is premature. While the terminology will prove to be accurate, at this poitn in the analysis, one must not be careful to confuse Perfect Palindromes with Palindromes. It has not yet been shown the class of Sentences which satisfy Definition 3.1.3 also satisfy 3.1.2. 

Before verifying the class of Sentences which satisfy Definition 3.1.3 are indeed palindromes, the motivation for Definition 3.1.3 will briefly be explained.

This Definition implicitly captures the cCaracter-level symmetry that's characteristic of perfect Palindromes. If a Sentence is its own inverse, it means that the sequence of Characters reads the same backward as forward.

It also implicitly captures the Word-level symmetry, as the inversion operation takes into account the reversal of words within the sentence, by Theorem 2.3.4. 

The following theorems will be used to validate the proposed class **PP** does indeed satisfy Definition 3.1.3, and thus Perfect Palindromes are a subset of the class Palindromes in any Language and its Corpus.

**Theorem 3.1.3** PP ⊂ K

In natural language, this theorem can be stated as follows: Perfect Palindromes are a subset of the Invertible Sentences in a Corpus. 

Proof:

Assume ζ ∈ PP.  This means ζ is a Perfect Palindrome, so by Definition 3.1.3, ζ = inv(ζ).

Sentence in Corpus: Since ζ is a Perfect Palindrome, it is also a Sentence, and therefore belongs to the Corpus C:sub:L (by Definition 2.1.2).

Inverse in Corpus:  Because ζ = inv(ζ) and ζ ∈ C:sub:L, it follows that inv(ζ) ∈ C:sub:L.

Invertible Sentence: By Definition 2.2.2 (Invertible Sentences), since inv(ζ) ∈ C:sub:L, this means ζ ∈ K.

Therefore, if ζ ∈ PP, then ζ ∈ K. This implies PP ⊂ K. ∎

Explanation:

The proof demonstrates that if a Sentence is a Perfect Palindrome (meaning it's its own inverse), then it must also be an Invertible Sentence (meaning its inverse is in the Corpus). This is because the Sentence being equal to its inverse directly satisfies the condition for being an Invertible Sentence.

(TODO: Need to prove this with the definition of invertible sentences, since perfect palindromes are defined as the class of sentences which are their own inverses.)

**Theorem 3.1.4** ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → (∀ α ∈ W:sub:`ζ`: α ∈ I)

In natural language, this theorem can be states as Follows: If a Sentence is Perfect Palindrome, then all of its Words are invertible. 

Recall the definition of a subset,

    1. A ⊂ B ↔ (∀ x: x ∈ A → x ∈ B)

Applying this definition to Theorem 3.1.3, 
    
    2. ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → ζ ∈ K

From Theorem 2.3.4, it is known the consequent of this conditional implies the following,

    3. ∀ ζ ∈ C:sub:`L`: ζ ∈ K → (∀ α ∈ W:sub:`ζ`: α ∈ I)

Recall the tautology of *Hypothetical Syllogisms*, for any propositions *p*, *q* and *r*,

    4. ( p → q ∧ q → r ) → (q → r)

Applying this tautological law to step 2 and step 3,

    5. ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → (∀ α ∈ W:sub:`ζ`: α ∈ I)

Which is what was to be shown. ∎ 

**Theorem 3.1.5**  PP ⊂ P

Theorem 3.1.5: PP ⊂ P

Proof:

Assume ζ ∈ PP. This means ζ is a Perfect Palindrome, so by Definition 3.1.3, ζ = inv(ζ).

σ-reduction: Let's apply σ-reduction to both sides of the equation in step 1:

(Ζ ⋅ Σ:sub:σ) = (inv(Ζ) ⋅ Σ:sub:σ)

Applying Corollary 3.1.2.1:  Since every Sentence is a String (Definition 2.1.2), we can apply Corollary 3.1.2.1 to the right-hand side of the equation in step 2:

(Ζ ⋅ Σ:sub:σ) = inv(Ζ ⋅ Σ:sub:σ)

Palindrome Definition: The equation in step 3 satisfies the condition for ζ to be a Palindrome according to Definition 3.1.2. Therefore, ζ ∈ P.

Since ζ was an arbitrary Perfect Palindrome, we have shown that if ζ ∈ PP, then ζ ∈ P. This implies PP ⊂ P. ∎

Explanation:

This proof demonstrates that all Perfect Palindromes are also Palindromes. We achieved this by showing that if a Sentence is its own inverse, then its σ-reduction is also its own inverse, which satisfies the definition of a Palindrome.

**Definition 3.1.4: Imperfect Palindromes**

Imperfect Palindromes are defined as the set of Sentences **IP** that satisfy the following formula,

    ζ ∈ P - PP 

**Theorem 3.1.6** PP ∪ IP = P

Follows immediately from Theorem 3.1.3 and Definition 3.1.4. ∎

Since PP and IP are non-overlapping by Definition 3.1.4 and their union encompasses the entire class of Palindromes by Theorem 3.1.6, these two sets form a partition of the class of Palindromes. The following definition and terminology is introduced to help describe this partitioning.

**Definition 3.1.5: Aspect**

A Palindrome P is said to have a *perfect aspect* if and only if *P ∈ PP*. A Palindrome is said to have an *imperfect aspect* if and only if *P ∈ IP*.

Parity
^^^^^^

One partitioning, or dimension, of Palindromes has been introduced through the concept of *aspect*. A Palindrome can either be perfect or imperfect, but not both. In this section, the definitions and theorems for uncovering the second partitioning of Palindromes, *parity*, will be developed.

**Definition 3.1.6: Partial Sentence**

A Partial Sentence of Length *n* is denoted *ζ*:sub:`n`. Given a sentence *ζ* from a Corpus C:sub:`L` and a fixed *n*, the Partial Sentence of Length *n* is formally defined as the Sentence *ζ*:sub:`n`

Definition 3.2.1: Partial Sentence (Revised)

Let ζ be a Sentence in C:sub:L with Character-level representation Z = (ⲁ₁ , ⲁ₂ , ..., ⲁₗ₍ζ₎).

The Partial Sentence of length n, denoted ζ:sub:n, is defined as:

ζ:sub:n = (ⲁ₁ , ⲁ₂ , ..., ⲁₙ)  where 1 ≤ n ≤ l(ζ)

**Theorem 3.1.7** ∀ ζ ∈ C:sub:`L`: [ ∃ ⲁ ∈ Σ: ( 2 *  l(ζ:sub:`ⲁ`) = l(ζ) ) ∨ (ⲁ = ε)]

This theorem can be stated in natural language as follows: For every Sentence in a Corpus, there is a Character in the Sentence that perfectly the divides of String length of the Palindrome in half, or there is no Character in the Sentence which divides it in half.

Theorem 3.2.2: ∀ ζ ∈ C:sub:L: [ ∃ ⲁ ∈ Σ: ( 2 * l(ζ:sub:ⲁ) = l(ζ) ) ∨ (ⲁ = ε)]

Proof:

Let ζ be an arbitrary Sentence in C:sub:L with Character-level representation Z = (ⲁ₁ , ⲁ₂ , ..., ⲁₗ₍ζ₎).

Consider the String Length of ζ, l(ζ).  There are two cases:

Case 1: l(ζ) is odd.  In this case, there is a unique middle Character in Z. Let ⲁ be this middle Character. Then, the Partial Sentence ζ:sub:ⲁ includes all Characters up to and including ⲁ. Since ⲁ is the middle Character, l(ζ:sub:ⲁ) = (l(ζ) + 1) / 2.  Thus, 2*l(ζ:sub:ⲁ) = l(ζ).

Case 2: l(ζ) is even. In this case, there is no single middle Character. Instead, there is a "gap" between the two middle Characters. Let ⲁ = ε (the Empty Character). Since there is no Character that splits the Sentence exactly in half, the condition 2*l(ζ:sub:ⲁ) = l(ζ) cannot be satisfied by any Character in Σ. Therefore, ⲁ = ε satisfies the theorem.

In both cases, we have either found a Character ⲁ ∈ Σ that satisfies l(ζ:sub:ⲁ) = 2 * l(ζ), or we have set ⲁ = ε.

Therefore, ∀ ζ ∈ C:sub:L: [ ∃ ⲁ ∈ Σ: ( 2 * l(ζ:sub:ⲁ) = l(ζ) ) ∨ (ⲁ = ε)] ∎

Explanation:

This proof demonstrates that for any Sentence, there exists a Character that acts as a "midpoint" or "pivot" in terms of String Length. If the Sentence has an odd String Length, this midpoint is the middle Character. If the Sentence has an even String Length, we use the Empty Character as a symbolic midpoint.

Theorem 3.2.2 ensures the existence of a Character that can be reliably called a Palindromic Pivot. With this theorem, every Sentence in a Corpus it must have a Pivot.

**Definition 3.1.7: Pivots** 

The Pivot of a Sentence *ζ*, denoted *ω*:sub:`ζ`, is defined as the Character in the Palindrome such that the following formula is tue,

   ( l(ζ:sub:`ω_ζ`) = 2 * l(ζ) ) ∨ (ω:sub:`ζ` = ε)

Given a Palindromic Sentence *ζ ∈ P*, Theorem 3.2.2 ensures the existence of this Pivot Character.

**Definition 3.1.8: Even Palindromes**

The class of Even Palindromes, denoted P:sup:`+`, is defined as the set of Sentences ζ which satisfy the following formula,

    ζ ∈ P:sup:`+` ↔ [ (ζ ∈ P) ∧ ( ω:sub:`ζ` = ε )]

**Definition 3.1.9: Odd Palindromes**

The class of Even Palindromes, denoted P:sup:`-`, is defined as the set of Sentences ζ which satisfy the following formula,

    ζ ∈ P:sup:`-` ↔ [ (ζ ∈ P) ∧ ( ω:sub:`ζ` ≠ ε )]

**Theorem 3.1.8** ζ ∈ P:sup:`+` ↔ l(ζ) = 2 * l(ζ:sub:`ω_ζ`) 

Proof:

(→) Assume ζ ∈ P⁺.

Even Palindrome: By Definition 3.2.3, this means ζ ∈ P (ζ is a Palindrome) and ω:sub:ζ = ε (the Pivot is the Empty Character).

Pivot Property: Since ω:sub:ζ = ε, by Definition 3.2.2 (Pivots), it follows that l(ζ:sub:ω_ζ) = 2 * l(ζ) does NOT hold. This is because there is no Character in ζ that divides its String Length exactly in half.

Even String Length: Since ζ is a Palindrome with an Empty Character as its Pivot, it must have an even String Length (l(ζ) is even).

Partial Sentence:  By Definition 3.2.1 (Partial Sentence), ζ:sub:ω_ζ is the Partial Sentence up to the Pivot ω:sub:ζ. Since ω:sub:ζ = ε, ζ:sub:ω_ζ includes all Characters up to the "gap" between the two middle Characters of ζ.

String Length of Partial Sentence: Therefore, the String Length of ζ:sub:ω_ζ is exactly half the String Length of ζ: l(ζ:sub:ω_ζ) = l(ζ) / 2.

Rearranging: This can be rewritten as l(ζ) = 2 * l(ζ:sub:ω_ζ).

(←) Assume l(ζ) = 2 * l(ζ:sub:ω_ζ).

Even String Length: This equation implies that l(ζ) is even.

No Middle Character: Since l(ζ) is even, there is no single Character in ζ that divides its String Length exactly in half.

Empty Pivot: By Definition 3.2.2 (Pivots), this means the Pivot of ζ must be the Empty Character: ω:sub:ζ = ε.

Even Palindrome: Since ζ is a Palindrome (as assumed in the theorem statement) and ω:sub:ζ = ε, by Definition 3.2.3, it follows that ζ ∈ P⁺.

Since we have proven both directions of the implication, the theorem is established:

ζ ∈ P⁺ ↔ l(ζ) = 2 * l(ζ:sub:ω_ζ) ∎

Explanation:

This theorem provides a useful characterization of Even Palindromes in terms of their String Length and the String Length of their Partial Sentence up to the Pivot. It essentially states that a Palindrome is even if and only if its total String Length is twice the String Length of its first half.

**Theorem 3.1.9** ζ ∈ P:sup:`-` ↔ l(ζ) = 2 * l(ζ:sub:`ω_ζ`) + 1

TODO

Theorem 3.2.4: ζ ∈ P⁻ ↔ l(ζ) = 2 * l(ζ:sub:ω_ζ) + 1

Proof:

(→) Assume ζ ∈ P⁻.

Odd Palindrome: By Definition 3.2.4 (with the corrected symbol), this means ζ ∈ P (ζ is a Palindrome) and ω:sub:ζ ≠ ε (the Pivot is not the Empty Character).

Pivot Property: Since ω:sub:ζ ≠ ε, by Definition 3.2.2 (Pivots), it follows that l(ζ:sub:ω_ζ) = 2 * l(ζ) does NOT hold. This is because there IS a Character in ζ that divides its String Length in a specific way, but not exactly in half.

Odd String Length: Since ζ is a Palindrome with a non-Empty Character as its Pivot, it must have an odd String Length (l(ζ) is odd).

Partial Sentence: By Definition 3.2.1 (Partial Sentence), ζ:sub:ω_ζ is the Partial Sentence up to the Pivot ω:sub:ζ. Since ω:sub:ζ is the middle Character of ζ, ζ:sub:ω_ζ includes all Characters up to and including ω:sub:ζ.

String Length of Partial Sentence: Therefore, the String Length of ζ:sub:ω_ζ is exactly half the String Length of ζ, minus 1/2 (to account for the middle character): l(ζ:sub:ω_ζ) = (l(ζ) - 1) / 2.

Rearranging: This can be rewritten as l(ζ) = 2 * l(ζ:sub:ω_ζ) + 1.

(←) Assume l(ζ) = 2 * l(ζ:sub:ω_ζ) + 1.

Odd String Length: This equation implies that l(ζ) is odd.

Middle Character: Since l(ζ) is odd, there is a single Character in ζ that acts as the midpoint.

Non-Empty Pivot: By Definition 3.2.2 (Pivots), this means the Pivot of ζ must be a non-Empty Character: ω:sub:ζ ≠ ε.

Odd Palindrome: Since ζ is a Palindrome (as assumed in the theorem statement) and ω:sub:ζ ≠ ε, by Definition 3.2.4, it follows that ζ ∈ P⁻.

Since we have proven both directions of the implication, the theorem is established:

ζ ∈ P⁻ ↔ l(ζ) = 2 * l(ζ:sub:ω_ζ) + 1 ∎

Explanation:

This theorem provides a characterization of Odd Palindromes in terms of their String Length and the String Length of their Partial Sentence up to the Pivot. It essentially states that a Palindrome is odd if and only if its total String Length is twice the String Length of its first half (not including the middle Character) plus 1 (to account for the middle Character).

**Theorem 3.1.10** P:sup:`-` ∩ P:sup:`+` = ∅ 

Theorem 3.2.5: P⁻ ∩ P⁺ = ∅

Proof:

Assume, for the sake of contradiction, that ζ ∈ P⁻ ∩ P⁺. This means ζ belongs to both the set of Odd Palindromes and the set of Even Palindromes.

Applying Theorems 3.2.3 and 3.2.4:

Since ζ ∈ P⁻, by Theorem 3.2.4, we have: l(ζ) = 2 * l(ζ:sub:ω_ζ) + 1
Since ζ ∈ P⁺, by Theorem 3.2.3, we have: l(ζ) = 2 * l(ζ:sub:ω_ζ)
Contradiction: These two equations contradict each other. The first equation implies that l(ζ) is odd, while the second equation implies that l(ζ) is even. A number cannot be both odd and even.

Therefore, our initial assumption that ζ ∈ P⁻ ∩ P⁺ must be false.

Hence, P⁻ ∩ P⁺ = ∅.

TODO

**Theorem 3.1.11** P:sup:`-` ∪ P:sup:`+` = P

TODO

Theorem 3.2.6: P⁻ ∪ P⁺ = P

Proof:

Every Palindrome is either Odd or Even: By Definitions 3.2.3 and 3.2.4, a Palindrome must either have an Empty Character as its Pivot (making it even) or a non-Empty Character as its Pivot (making it odd). There are no other possibilities.

No Palindrome can be both Odd and Even: Theorem 3.2.5 establishes that no Palindrome can belong to both P⁻ and P⁺.

Therefore, the sets P⁻ and P⁺ form a partition of P. This means every Palindrome belongs to either P⁻ or P⁺, and no Palindrome belongs to both.

Hence, P⁻ ∪ P⁺ = P. ∎

Explanation:

These two theorems demonstrate that the sets of Odd Palindromes and Even Palindromes form a partition of the set of all Palindromes. This means that every Palindrome is either odd or even, and no Palindrome can be both.

This partitioning is based on the parity of the Palindrome's String Length, as reflected in the position of its Pivot.

**Definition 3.1.1O: Parity** 

A Palindrome P is said to have a *even parity* if and only if *P ∈ P*:sup:`+`. A Palindrome is said to have an *odd parity* if and only if *P ∈ *P:sup:`-`*.

(TODO: there is a probably a relationship between pivots in unreduced space versus pivots in reduced space that can be proved in a theorem. Observation: pivots that are empty in reduced space map to pivots that empty or delimters in unreduced space)



Section III.II: Structures
---------------------------

The following theorems serve as the main result of the current formal system that has been constructed to describe the syntactical structures of Palindromes in any Language. 

**Definition 3.1.11: Boundary Words**

For any Sentence in a Corpus, the Boundary Words, denoted *α*:sub:`start` and *α*:sub:`end`, the Words which satisfy the following opening formulas, 

    1. ∀ ζ ∈ C:sub:`L`: ((1, β) ∈ W:sub:`ζ`) ↔ β = α:sub:`start`
    2. ∀ ζ ∈ C:sub:`L`: ((Λ(ζ), β) ∈ W:sub:`ζ`) ↔ β = α:sub:`end` 

**Definition 3.2.2: Pivot Words** 

For any Sentence in a Corpus, the Pivot Words, denoted α:sub:`-`(ω) and *α*:sub:`+`(ω), are defined as follows.

Let ζ be a Sentence in C:sub:L with Word-level representation W:sub:ζ = (α₁ , α₂ , ..., αₙ), where n = Λ(ζ), and Pivot ω:sub:ζ.

If ω:sub:ζ ≠ ε (Odd Palindrome):

Let k be the index such that (k, αₖ) ∈ W:sub:ζ and αₖ contains the Pivot Character ω:sub:ζ.
Then, the Pivot Words are defined as:
α:sub:-(ω:sub:ζ) = αₖ₋₁ (if k > 1) or ε (if k = 1)
α:sub:+(ω:sub:ζ) = αₖ₊₁ (if k < n) or ε (if k = n)
If ω:sub:ζ = ε (Even Palindrome):

Let k = n / 2.
Then, the Pivot Words are defined as:
α:sub:-(ω:sub:ζ) = αₖ
α:sub:+(ω:sub:ζ) = αₖ₊₁

The Inverse Postulates
^^^^^^^^^^^^^^^^^^^^^^

**Theorem 3.2.1: The Boundary Postulate** ∀ ζ ∈ P : ( α:sub:`start` ⊂:sub:`s` α:sub:`end` ) ∨ ( α:sub:`end` ⊂:sub:`s` α:sub:`start` )

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

Applying Corollary 3.1.2.1: Using Corollary 3.1.2.1 repeatedly on inv(Ζ ⋅ Σ:sub:σ) , we get:

inv(Ζ ⋅ Σ:sub:σ) = inv(α₁α₂...αₙ)
= inv(αₙ)...inv(α₂) inv(α₁)

Combining equations: Combining equations from steps 3 and 5, we have:

α₁α₂...αₙ = inv(αₙ)...inv(α₂) inv(α₁)

Analyzing cases: Now, let's consider the lengths of the Boundary Words, α₁ (α:sub:start) and αₙ (α:sub:end). There are three cases:

Case 1: l(α₁) = l(αₙ)

In this case, the equation in step 6 implies that α₁ = inv(αₙ) and αₙ = inv(α₁).
Since α₁ and αₙ are Invertible Words (by Theorem 2.3.4), this means α₁ = αₙ.
Therefore, both α:sub:start ⊂:sub:s α:sub:end and α:sub:end ⊂:sub:s α:sub:start hold.
Case 2: l(α₁) < l(αₙ)

In this case, the equation in step 6 implies that α₁ is a contiguous subsequence of inv(αₙ).
Since αₙ is an Invertible Word, inv(αₙ) is also a Word in the Language.
By Definition 1.1.4 (Containment), this means α₁ ⊂:sub:s inv(αₙ).
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

∀ ζ ∈ P: (ω:sub:`ζ` = σ) → ( α:sub:`-` (ω:sub:`ζ`) ⊂ α:sub:`+` (ω:sub:`ζ`) ) v ( α:sub:`+` (ω:sub:`ζ`) ⊂ α:sub:`-` (ω:sub:`ζ`) )

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

Applying Corollary 3.1.2.1: Using Corollary 3.1.2.1 repeatedly on inv(Ζ ⋅ Σ:sub:σ) , we get:

inv(Ζ ⋅ Σ:sub:σ) = inv(α₁α₂...αₙ)
= inv(αₙ)...inv(α₂) inv(α₁)

Combining equations: Combining equations from steps 4 and 6, we have:

α₁α₂...αₙ = inv(αₙ)...inv(α₂) inv(α₁)

Analyzing Pivot Words: Since the Pivot is between αₖ and αₖ₊₁, the equation in step 7 implies:

αₖ αₖ₊₁ = inv(αₖ₊₁) inv(αₖ)

Cases based on length:  Similar to the proof of the first Inverse Postulate, we consider the lengths of αₖ and αₖ₊₁:

Case 1: l(αₖ) = l(αₖ₊₁):

In this case, αₖ = inv(αₖ₊₁) and αₖ₊₁ = inv(αₖ).
Since αₖ and αₖ₊₁ are Invertible Words (by Theorem 2.3.4), this means αₖ = αₖ₊₁.
Therefore, both α:sub:- (ω:sub:ζ) ⊂ α:sub:+ (ω:sub:ζ) and α:sub:+ (ω:sub:ζ) ⊂ α:sub:- (ω:sub:ζ) hold.
Case 2: l(αₖ) < l(αₖ₊₁):

In this case, αₖ is a contiguous subsequence of inv(αₖ₊₁).
Since αₖ₊₁ is an Invertible Word, inv(αₖ₊₁) is also a Word in the Language.
By Definition 1.1.4 (Containment), this means αₖ ⊂:sub:s inv(αₖ₊₁).
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

ζ ∈ PP ↔ [∃ α ∈ L: (ω:sub:`ζ` ⊂:sub:`s` α) ∧ (α ∈ R) ] ∨ (ω:sub:`ζ` = σ)

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

Non-Delimiter Pivot: Since ω:sub:ζ ⊂:sub:s α and α is a Word in the Language, by Axiom W.1 (Delimiter Axiom), α cannot contain the Delimiter Character. Therefore, ω:sub:ζ ≠ σ.

Even Palindrome: Since ω:sub:ζ ≠ σ, by the strengthened Third Inverse Postulate, it must be the case that ω:sub:ζ = ε. By Definition 3.2.3, this means ζ ∈ P⁺ (ζ is an Even Palindrome).

Conclusion: We have shown that ζ ∈ PP and ζ ∈ P⁺, which means ζ ∈ PP ∧ ζ ∈ P⁺.

Since we have proven both directions of the implication, the theorem is established:

ζ ∈ PP ∧ ζ ∈ P⁺ ↔ ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ∎

Explanation:

This proof demonstrates the biconditional relationship between a Sentence being both a Perfect Palindrome and an Even Palindrome, and the existence of a Reflective Word containing the Sentence's Pivot.

The proof utilizes the definitions of Perfect Palindromes, Even Palindromes, and Reflective Words, along with the strengthened Third Inverse Postulate and the Delimiter Axiom, to analyze the different cases and demonstrate the implications in both directions.

Section III.III: Palindromic Algorithms
---------------------------------------

The results derived in this work can be used to construct algorithms for searching for various classes of Palindromes. The general outline for one such algorithm is given in this section, and then an example implemention in Python is presented.

A naive algorithm for filtering out Strings that cannot possibly be Palindromes might consist of inverting the strings and comparing them for equality. However, this would miss Palindromes with an imperfect aspect, as their symmetry does not manifest in the unreduced Alphabet. Without a *σ-reduction*, any algorithm that searchs for Palindromic String must be aware of the semantics of the Language in which it is searching. However, *σ-reduction* and the theorems proved over the course of this work allow algorithms to be constructed that are independent of the host Language.

Moreover, as mentioned after the body Theorem 3.1.2, the *σ*-Pairing Language reduces the complexity of searching for Palindromic strings. An Alphabet with less Characters can be traversed quicker. 

To implement this, a String can be projected onto its *σ-reduced* Alphabet, and then those Pairs in the σ-Pairing Language whose inverse does not equal itself can be removed from the list of potential Palindromes. To find a String whose inverse does not equal itself, it suffices to find a single Character whose inverted position is not occupied by that Character. 

Therefore, as a first step to generating a list of Palindromes, the Strings which do not satisfy these conditions can be discarded.

Theorem 3.3.1 and Theorem 3.3.2 provide further conditions that any Palindrome must satisfy, reducing the set of potential Palindromes in this hypothetical search algorithm even more. 

With respect to Perfect Palindromes, the search algorithm can be refined even further by incorporating the conditions given in Theorem 3.3.3 and Theorem 3.3.4. Based on the String Length of a Perfect Palindrome, its point of symmetry must possess certain measurable properties, such as the presence of a Reflective Word or an Invertible Word contained by the word opposite the pivot. 

Python Implementation 
^^^^^^^^^^^^^^^^^^^^^

(TODO: code this!)

Section III.IV: Future considerations
-------------------------------------

This work focused on using the operation of sigma reduction to describe palindromic structure in terms of its *aspect* and its *parity*. As mentioned at several points, there are two other dimensions of palindromes this work has not sought to incorporate into formal system. While the considerations in the introduction seem to preclude the possibility of a purely syntactical account of palindromes, the author does not believe this means the structure of palindromes cannot be formalized by taking into account certain universal semantic assumptions. 

To account for the dimension of *punctuality*, a possible avenue of exploration could be extending the operation of sigma reduction to encompass other Characters besides the Delimiter Character. In this way, the punctuality of a palindrome may be "projected" onto a Pairing Language where its symmetry under inversion can be recovered.

To account for the dimension of *case*, the link between uppercase and lowercase letters in natural languages may be viewed as inducing a symmetry in the Alphabet that in turn may be exploitable for describing palindromic symmetry. In such a formalization, a possible method of attack would be introduce a many-to-one relationship between in a sigma-reduction where uppercase and lowercase letters are mapped to their "primitive" Character in an appropriate Pairing Language.

(TODO: comment on possibility of interesting recursions, i.e. what happens when the Alphabet of this formal system is assigned the symbols of the formal system itself?)

(TODO: comment on completeness, i.e. what does this formal model of language say about the completeness of language, or its lack thereof?)

Section IV: References 
======================

Reflective Words
----------------

The following spreadsheet contains a sample of reflective words in English.

.. csv-table:: Reflective Words
   :file: ../_static/data/reflective_words.csv

Invertible Words
----------------

The following spreadsheet contains a sampe of invertible words (minus reflective words) in English.

.. csv-table:: Invertible Words
   :file: ../_static/data/invertible_words.csv

Palindromic Analysis 
--------------------

The following spreadsheet contains the results of palindromic analysis conducted on a sample of English palindromes. 

.. csv-table:: Palindromic Analysis
   :file: ../_static/data/palindromes.csv