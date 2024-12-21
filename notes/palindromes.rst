======================
Palindromic Structures
======================

The paper contains a formal method for analyzing palindromic structures. It is a work in progress. What follows should by no means be interpretted as a complete or consistent formal theory; it should be treated more like a rough draft. Many of the notions need further clarification and elaboration.  
    
The goal of this paper is to introduce formal constraints the palindromes in *any* language must satisfy independently of the semantic interpretation of their constituent words. These formal constraints will in turn lead to the identification of the main structural elements of palindromes. After a language is assumed and a class of words identified, these structural elements can be used as a basis for further semantical and statistical analysis of the assumed language. 

Section I: Defintions 
=====================

Section I.1: Strings
--------------------

The domain of discourse is composed of *Strings*. A String will be represented as follows, 

    1. String (*s*:sub:`1`, *s*:sub:`2`, *s*:sub:`3`): A lowercase English "s" with a subscript indicates a *String*. Sometimes the subscript will be dropped and *s* will be used.

A String is regarded as a linguistic artifact that is defined by its *length*, its *Characters* and their *ordering*. It is assumed if one knows how many Characters are in a String, which Characters are in a String and in what order they occur, then one has all the information necessary to completely determine the String. This notion is made more precise in the following sections with the introduction of several definitions.

A *Word* will be considered a *type* of String. Colloquially, a word can be understood as a String with semantic content. The goal of the analysis is to describe the necessary syntactic conditions for a String to be considered a formal Word, without taking into account the semantic content that is assigned to through everyday use. In other words, the analysis assumes Words have already been selected from the set of all possible Strings and assigned interpretations. 

The set of all Strings will be denoted **S**. | **S** | is assumed to be uncountably infinite.

Characters
^^^^^^^^^^

A *Character* is the basic unit of a String. Characters will be represented as follows,

    1. Characters (*𝔞*, *𝔟*,  *𝔠*, etc. ): Lowercase Fraktur letters represent Characters. Subscripts will occassionally be used to denote Characters, (*𝔞*:sub:`1`, *𝔞*:sub:`2`, ... ). 
    2. Empty (*ε*): The lowercase Greek epsilon, *ε*, represents the Empty Character.
    3. Space (*σ*): The lowercase Greek sigma, *σ*, represents the Space Character. 

In the case of English, Characters would correspond to letters such as "a", "b", "c", etc., the Empty Character would correspond to a null letter, "", and the Space Character would correpond to a blank letter, " ".

The aggregate of all Characters is called an Alphabet and is denoted by an uppercase Sigma, Σ,

    Σ = { *ε*, *σ*, *𝔞*, *𝔟*,  *𝔠*, ... }

The number of elements in an Alphabet is denoted | Σ |.

Concatenation 
^^^^^^^^^^^^^

Concatenation is considered the sole constitutive operation for the formation of Strings. Concatenation is defined in terms of Characters as,

    1. Concatenation  *𝔞* and *𝔟* means to place *𝔟* behind *𝔞*  *𝔞𝔟*

The operation of concatenation will be expanded to a larger class of entities in the next section when the notion of a *Word* is further clarified, but its application will always be reducible to simple Character concatenation. This current definition of concatenation leads immediately to the dual *Laws of Nullity*, 

    1. *𝔞ε* = *𝔞*
    2. *ε𝔞* = *𝔞*
   
In other words, the operation of concatenating a Character with the Empty Character in either direction will leave the original Character unaltered. 

Length
^^^^^^

The *length* of a *String*, *l(s_i)*, is defined as the number of non-Empty characters in the sequence of concatenated Characters that make up the *String*.

Section I.2: Words
------------------

While the notion of Characters maps almost exactly to the intuitive notion of letters in every day use, the notion of a *Word* requires explication. 

If Characters are mapped to letters in the alphabet of a *Language* **L**, the set of all Strings would have as a subset the Language that is constructed through the alphabet. The goal of this section is to introduce a series of constraints onto the set of all Strings that will filter out its elements that cannot belong to **L** based solely on their internal structure. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations. In other words, this analysis will proceed without assuming anything about the interpretation of the Words in the Language beyond the fact that they *are* Words of the Language.

To formalize these notion, the following symbolic representations are introduced, 

    1. Words (*a*, *b*, *c*, etc.): Lowercase English letters represent Words. Subscripts will occassionally be used to denote Words, (*a*:sub:`1`, *a*:sub:`2`, ... )
    2. Language (**L**): The uppercase English letter *L* in boldface represents a Language.

In the case of English, Words would correspond to words such as "dog", "cat", etc. A Language would correspond to a set of words such as { "dog", "cat", "hamster", ... } or { "tree", "flower", "grass", .... }.

The number of Words in a Language is denoted | **L** |. 

It will sometimes be necessary to refer to indeterminate Words, so notation is introduced for Word Variables,

    1. Word Variables (*α*, *β*, *γ*, etc. ): Lowercase Greek letters will represent variable words, i.e. indeterminate Words. Subscripts will occassionally be used to denote Word Variables, (*α*:sub:`1`, *α*:sub:`2`, ... )

The range of a Word Variable is understood to be the Language **L** from the Words are being drawn. 

Notation
^^^^^^^^

It will sometimes be convenient to represent Words and Strings as ordered sets of Characters, rather serial concatenations of Characters. The two formulations are equivalent, but the set representation has advantages when it comes to quantification and symbolic logic. When a String or Word representation is intended to be interpretted as a set, it will be written in bold uppercase letters. For example, the String represented as the concatenated series *s_1* = *𝔞𝔟𝔠* would be represented in this formulation as a set of ordered pairs **S_1**, where the first coordinate encodes the position of the Character in the String,

    **S_1** = { (1, *𝔞*), (2, *𝔟*), (3, *𝔠*) }

Note, since sets do not preserve order, this would be equivalent to,

    { (3, *𝔠*), (2, *𝔟*), (1, *𝔞*) }

To simplify notation, it is beneficial to represent this set as a sequence that preserves order as,

    **S_1** = (*𝔞*, *𝔟*, *𝔠*)

With this equivalent represention, the length of a String *s_1*, l(*s_1*), may be written as | **S_1** |. 

Axioms of Syntax
^^^^^^^^^^^^^^^^

The goal of the analysis is to leave the semantic interpretation of Words in a Language as ambiguous as possible. This ambiguity, it is hoped, will leave the results of the analysis applicable to palindromic structures in a variety of languages. This section details the minimal *necessary* assumptions that are placed on any String to be considered an element of a Language **L**. The axioms listed in this section are not *sufficient*; in other words, it is possible for a String to satisfy all of the axioms in this section without being an element of a Language.

For the axioms that follow, let **L** be a Language. Let *s* be a String, not necessarily a member of **L**. Let *𝔞*:sub:`i` be the i:sup:`th` Character of the String *s*. Let *l(s)* be the length of *s*. Let *N*:sub:`s` be the set,

    { 1, 2, ... , l(s) }

The following Axioms detail the syntactical conditions necessary for a String to be considered a Word,

**The Delimiter Axiom ** 

    s ∈ L → (∀ i ∈ *N*:sub:`s`: 𝔞:sub:`i` ≠ σ )

TODO: Are there any other syntactical constraints on words besides the fact that they have to be delimited?

Inversion
^^^^^^^^^

Informally, the *Inverse* of a Word is the reversed sequence of Characters in the Word. The Inverse of a Word is easily understood through examples in English. The following table lists words in English. If an Inverse of that word exists, it is listed in the second column. If an Inverse does not exist, the second column is filled with an "x",

| Word | Inverse | 
| ---- | ------- |
| time | emit    |
| saw  | was     |
| raw  | war     |
| dog  | god     |
| pool | loop    |
| rat  | tar     |
| cat  | x       |
| you  | x       |
| help | x       |
| door | x       |

While this example is illustrative, its essential semantic character should be noted. Nevertheless, it should be clear the intent is to define the Inverse of a Word only if its exists. To do this, the definition of the Inverse of a String is first required. This will provide a subdomain in the domain of discourse over which to quantify the conditions that are to be imposed on the Inverse of a Word. Informally, the Inverse of a String *s*, denoted by *inv(s)*, is the string formed by reversing the order of characters in *s*.

**String Inversion** Let *s* be a string with length *l(s)*. Let *𝔞*:sub:`i` be the i:sup:`th` character of the String s. Let *N*:sub:`s` be the set,

    { 1, 2, ... , l(s) }

Then, let *t* be a String with length *l(t)* and let *𝔟*:sub:`i` be the i:sup:`th` character of the String *t*. *t* is called the Inverse of *s* and is denoted *inv(s)* if it satisfies the following conditions, 

    1. l(t) = l(s) 
    2. ∀ i ∈ *N*:sub:`s`: 𝔟:sub:`i` = 𝔞:sub:`l(s) - i + 1`

**Theorem 1.2.1** For any String *s*, inv(inv(s)) = s

Let *s* be a String with length *l(s)* and Characters denoted by *𝔞*:sub:`i` for *i = 1, 2 , ... , l(s)*. Let *t = inv(s)* with Characters *𝔟*:sub:`i`. By the definition of String Inversion:

    1. l(t) = l(s) 
    2. ∀ i ∈ *N*:sub:`s`: 𝔟:sub:`i` = 𝔞:sub:`l(s) - i + 1`

Now, let *u = inv(t)* with Characters *𝔠*:sub:`i`. Applying the definition of String Inversion again:

    3. l(u) = l(t)
    4. ∀ i ∈ N:sub:`t`: 𝔠:sub:`i` = 𝔟:sub:`l(t) - i + 1`

Since l(t) = l(s) and *N*:sub:`t` = *N*:sub:`s`, we can substitute l(s) for l(t) and *N*:sub:`s`,for *N*:sub:`t`, in the definition of u:

    5. ∀ i ∈ *N*:sub:`s`: 𝔠:sub:`i` = 𝔟:sub:`l(s) - i + 1`

ow, substitute the definition of 𝔟:sub:`i` from step 2 into the equation for 𝔠:sub:`i`:

    6. ∀ i ∈ *N*:sub:`s`: 𝔠:sub:`i` = 𝔞:sub:`l(s) - (l(s) - i + 1) + 1`
   
Simplifying,

    7. ∀ i ∈ *N*:sub:`s`: 𝔠:sub:`i` = 𝔞:sub:`i`

Eince *u* and *s* have the same length (*l(u) = l(t) = l(s)*) and the same characters in the same order (*𝔠*:sub:`i` = *𝔞*:sub:`i` for all *i*), it can be concluded, *u = s*. Recall that *u = inv(t)* and *t = inv(s)*.  Substituting, the desired result is then deduced: *inv(inv(s)) = s*.

Section I.3: Word Classes 
-------------------------

It will be necessary to define special classes of Words in a Language. These classes will assist in the description of palindromic structures. 

Reflective Words 
^^^^^^^^^^^^^^^^

Let *𝔞*:sub:`i` be the i:sup:`th` Character in the Word *α*. Let *l(α)* be the length of *α*. Let *N*:sub:`α` be the set,

    { 1, 2, ... , l(α) }

Then the set of Reflective Words **R** is defined as the set of α which satisfy the open formula,

    α ∈ R ↔ [ ∀ i ∈ *N*:sub:`α`:  *𝔞*:sub:`i` = *𝔞*:sub:`l(α) - i` ]

**Theoreom 1.3.1** α ∈ R ↔ α = inv(α)

Corollary:  If a word  w is self-reflective (belongs to the set R), then w = inv(w).

Proof:

Assume α ∈ R: This means w is a self-reflective word.

Definition of Reflective Words: By our definition, this implies:

∀ i ∈ N<sub>w</sub>: w<sub>i</sub> = w<sub>l(w) - i</sub>
Let v = inv(w): By the definition of string inversion:

l(v) = l(w)
∀ i ∈ N<sub>w</sub>: v<sub>i</sub> = w<sub>l(w) - i + 1</sub>
Character Equality:  From step 2, we know that w<sub>i</sub> = w<sub>l(w) - i</sub>.  Substituting this into the equation from step 3, we get:

∀ i ∈ N<sub>w</sub>: v<sub>i</sub> = w<sub>l(w) - i</sub> = w<sub>i</sub>
Equality of Strings: Since v and w have the same length (l(v) = l(w)) and the same characters in the same order (v<sub>i</sub> = w<sub>i</sub> for all i), we can conclude that v = w.

Final Step: Recall that v = inv(w). Substituting, we get inv(w) = w. ∎

Theorem: For any word α,  α ∈ R ↔ α = inv(α)

Proof:

We need to prove both directions of the equivalence:

1. Forward Direction (α ∈ R → α = inv(α))

This is essentially the proof we already constructed for the corollary.  Here's a recap:

Assume α ∈ R.
By the definition of reflective words: ∀ i ∈ N<sub>α</sub>: a<sub>i</sub> = a<sub>l(α) - i</sub>
This implies α = inv(α) (as shown in the previous proof).
2. Reverse Direction (α = inv(α) → α ∈ R)

Assume α = inv(α): This means the word α is identical to its inverse.

Definition of String Inversion: By the definition of string inversion, this implies:

∀ i ∈ N<sub>α</sub>: a<sub>i</sub> = a<sub>l(α) - i + 1</sub>
Character Equality: Since l(α) - i + 1 is simply the index of the character corresponding to a<sub>i</sub> when the word is reversed, this equation shows that each character in α is equal to its corresponding character in the reversed word.

Definition of Reflective Words: This satisfies the definition of a reflective word, so α ∈ R.

Invertible Words 
^^^^^^^^^^^^^^^^

Let *α* be any Word in a Language **L**. Then the set of Invertible Words **I** is defined as the set of α which satisfy the open formula,

    α ∈ I ↔ inv(*α*) ∈ L

A Word *α* will be referred to as *invertible* if it belongs to the class of Invertible Words. Similarly, a Word *α* will be referred to *reflective* if it belongs to the class of Reflective Words. 

These definitions are employed to derive the following theoremes,

**Theorem 1.3.2** If *α* is an invertible word in Language **L**, then *inv(α)* is also an invertible word in **L**.

Assume α is invertible. This means,
    
    α ∈ I, 

where **I** is the set of invertible words in **L**. By definition, this implies,

    inv(α) ∈ L
    
Consider *inv(α)*. To show that it's invertible, it must be shown,


    inv(inv(α)) ∈ L. 

By Theorem 1.2.1,

    inv(inv(α)) = α
    
Since it is known *α ∈ L*, it follows,

    inv(inv(α)) ∈ L  
    
Therefore, by the definition of invertibility, 

    inv(α) ∈ I
    
Meaning *inv(α)* is also an invertible word. 

**Theorem 1.3.3** R ⊂ I

Proof:

Assume α ∈ R: This means α is a Reflective word.

Definition of Reflective Words: By your definition, this implies:

∀ i ∈ N<sub>α</sub>: a<sub>i</sub> = a<sub>l(α) - i</sub>
Applying String Inversion:  This condition precisely matches our definition of string inversion! It means that the i-th character of α is equal to the (l(α) - i + 1)-th character of α.  Therefore:

α = inv(α)
α ∈ L: Since α is a word in the language L, we have α ∈ L.

Substitution: Combining steps 3 and 4, we get: inv(α) ∈ L

Definition of Invertible Words:  Since inv(α) ∈ L, by your definition of Invertible words, this implies α ∈ I.

Conclusion: We started with the assumption that α ∈ R and showed that this implies α ∈ I. Therefore, every element in R is also an element in I, which means R ⊂ I.  ∎


**Theorem 1.3.3** If | **L** | is finite, then | **I** | is even. 

Assume that a Language **L** has a finite number of words. Consider the set I of invertible words in L. By Theorem 1.3.2, for every word α in I, its inverse, inv(α), must also be in I. 

Furthermore, α and inv(α) must be distinct words, unless α is reflective (in which case α = inv(α)).  If they were not distinct, and α was not a palindrome, it would imply that a word is its own inverse without being a palindrome, which contradicts the definition of a palindrome.

Even Cardinality:  Therefore, the elements of I can be grouped into distinct pairs (α, inv(α)). Since each pair contains two elements, and the number of words in L (and therefore in I) is finite, the total number of elements in I must be even.

Formalization:

We can express this proof more formally using set notation and logical symbols:

Let |L| denote the cardinality (number of elements) of the set L.
Let |I| denote the cardinality of the set I.
Let P be the set of palindromes in L.
Then, we can state the theorem as:

If |L| is finite, then |I| is even.

Proof:

|L| is finite. (Premise)
I = {α ∈ L | inv(α) ∈ L} (Definition of I)
∀α ∈ I, inv(α) ∈ I (Symmetry of invertibility)
∀α ∈ I, (α ≠ inv(α)) ∨ (α ∈ P) (Distinctness of inverses or palindromes)
I can be partitioned into disjoint pairs (α, inv(α)) and the set P.
|I| = 2 * number of pairs + |P|
Since |L| is finite, |I| and |P| are also finite.
Therefore, |I| is even. ∎
Conclusion:


Section II: Palindromic Structures
==================================

Section II.1: Pivots
--------------------

Let s be a palindromic string.

Part 1: If l(s) is even, then the pivot of s is the empty character (ε).
Part 2: If l(s) is odd, then the pivot of s is either the space character (σ) or a character from the alphabet (𝔞, 𝔟, 𝔠, ...).
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


Section II.2: Palindromic Pivots
--------------------------------

TODO

Section II.3: Palindromic Classification 
----------------------------------------

**Perfect Palindrome** A palindrome where the sequence of characters after the pivot is the exact inverse of the sequence of characters before the pivot.


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