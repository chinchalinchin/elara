Section I: Language
===================

Some general notation adopted throughout the course of this work is given below.

1. **N**:sub:`n` will represent the set of natural numbers starting at 1 and ending at *n*, 

.. math::

    N_n = \{ 1, 2, ... , n \}

2. The cardinality of a set **A** will be denoted | A |

3. The ∎ symbol will be used to denote the ending of all Definitions, Examples and Proofs. 

4. The terms *"set"* and *"class"* are used interchangeably. 
   

Section I.I: Strings
--------------------

The domain of discourse is composed of *Strings*. A String will be represented as follows, 

    1. String (*s*:sub:`1`, *s*:sub:`2`, *s*:sub:`3`): A lowercase English *s* with a subscript denotes a String. Often the subscript will be dropped and *s* will be used. The letter *t*, *u*, *v* and *w* are also reserved for Strings.

A String is regarded as a linguistic artifact that is defined by its *length*, its *Characters* and their *ordering*. It is assumed if one knows how many Characters are in a String, which Characters are in a String and in what order they occur, then one has all the information necessary to completely determine the String. This notion is made more precise below with the introduction of several core definitions.

The set of all Strings is denoted **S**. At this point, nothing definitive can be asserted about the contents or cardinality of **S**. Once Characters are introduced and concatenation is defined, it will be possible to make claims regarding **S**.

The goal is to define all linguistics entities over the set of all Strings: Characters, Alphabets, Words, Languages, Sentences and Corpuses. As each of these entities is introduced and defined, a new level of relations will reveal itself. Palindromic symmetries will manifest on each level, in slightly different but related forms. Each type of symmetry will involve, in some form or another, the concept of *String Inversion*, to be defined shortly. The essence of a Palindrome lies in binding together the syntactical symmetries at every linguistic layer into a semantic whole. Indeed, it will be seen the symmetrical structure required by Palindromes in turn requires these linguistic layers to have specific synactical properties, regardless of their semantic interpretation.

A *Word* will be considered a *type* of String. Colloquially, a Word can be understood as a String with semantic content. The goal of this section is to describe the necessary syntactic conditions for a String to be considered a formal Word, without taking into account the semantic content that is assigned to it through everyday use. In other words, the analysis assumes Words have already been selected from the set of all possible Strings and assigned interpretations. 

Characters
^^^^^^^^^^

A *Character* is the basic unit of a String. Characters will be represented as follows,

    1. Characters (*𝔞*, *𝔟*,  *𝔠*, etc. ): Lowercase Fraktur letters represent Characters. Subscripts will occassionally be used in conjunction with Fraktur letters to denote Characters at specific positions within Strings, (*𝔞*:sub:`1`, *𝔞*:sub:`2`, ... ). 
    2. Empty (*ε*): The lowercase Greek letter epsilon, *ε*, represents the Empty Character.
    3. Delimiter (*σ*): The lowercase Greek letter sigma, *σ*, represents the Delimiter Character. 

In the case of English, Characters would correspond to letters such as "a", "b", "c", etc., the Empty Character would correspond to the null letter, "", and the Delimiter Character would correpond to the blank letter, " ". 

The exact meaning of these symbols should be attended with utmost care. *𝔞*, *𝔟*,  *𝔠*, etc., represent Characters of the Alphabet and thus are all unique, each one representing a different linguistic element. When Character symbols are used with subscripts, *𝔞*:sub:`1`, *𝔞*:sub:`2`, etc., they are being referenced in their capacity to be ordered within a String. With this notation, it is not necessarily implied 𝔞*:sub:`1` and *𝔞*:sub:`2` are unequal Character-wise, but that they are differentiated only by their relative order in a String.

The Empty Character also deserves special mention, since it represents a *null* Character. The Empty Character is to be understood as a Character with no semantic content. It can be added or subtracted from a String without altering it in any way. The domain of all Strings **S**, as will be shown in (the albeit informal) Theorem 1.1.2, is uncountably infinite. Beyond this, the Empty Character introduces further ambiguity when defining the concepts of Word and Language, since multiple Strings with the Empty Character, i.e. *𝔞ε*, *𝔞εε*, *𝔞εεε*, etc., can represent the same semantic content. In order to formally define these linguistic entities, the Empty Character must be excluded from the domain of Words and Language. 

Take note, at this point it is has not yet been shown that Characters are Strings; the preceding statements should be taken heuristically. This will be rectified in the next section with the formal definition of concatenation and the introduction of Character Axiom C.1. 

The aggregate of all Characters is called an *Alphabet* and is denoted by an uppercase Sigma, :math:`\Sigma`,

.. math::

    \Sigma = { \varepsilon, \sigma, \mathfrak{a}, \mathfrak{b}, \mathfrak{c}, ... }

It will sometimes be necessary to refer to indeterminate Characters, so notation is introduced for Character Variables,

    1. Character Variables (*ⲁ*, *ⲃ*, *ⲅ*, etc. ): Lowercase Coptic letters will represent Character Variables, i.e. indeterminate Characters. Subscripts will occassionally be used with Coptic letters to denote Word Variables, (*ⲁ*:sub:`1`, *ⲁ*:sub:`2`, ... )

Once again, it should be noted when Character Variables are used with subscripts, it is meant to refer to the capacity of a Character Variable to be indeterminate at a *determinate position* within a String. Moreover, the range of a Character Variable is understood to be the Alphabet :math:`\Sigma` from which it is being drawn.

At this early stage, the formal system needs to introduce a notion of *equality* to make any significant headway. There will be a several types of equality defined within the system, but each new layer of equality will be built on top of the primitive notion of *Character Equalty* now introduced in the first preliminary Axiom to the formal system.

**Axiom C.0: The Equality Axiom**

For any Characters :math:`ⲁ, ⲃ \in \Sigma`, the notion of equality, denoted by :math:`ⲁ = ⲃ`, is a primitive concept and assumed to be understood. It is further assumed that Character Equality is an equivalence relation, satisfying reflexivity, symmetry and transitivity,

    1. :math:`\forall ⲁ \in \Sigma: ⲁ = ⲁ`
    2. :math:`\forall ⲁ, ⲃ \in \Sigma: ⲁ = ⲃ \leftrightarrow ⲃ = ⲁ`
    3. :math:`\forall ⲁ, ⲃ, ⲅ \in \Sigma: (ⲁ = ⲃ \land ⲃ = ⲅ) \rightarrow (ⲁ = ⲅ)`
∎ 

Character Equality will be used to define *String Equality* in Definition 1.14 and Word Equality in 1.2.3.

Concatenation 
^^^^^^^^^^^^^

Concatenation is considered the sole constitutive operation for the formation of Strings. It is taken as a primitive operation, but not an elementary operation. By this it is meant the notion of concatenation that is about to be adopted does not define concatenation solely in terms of Strings. Concatenation will be defined as a hetergeneous operation that is performed between Characters in a Alphabet and Strings.

**Definition 1.1.1: Concatenation**  

The result of *concatenating* any two Characters *ⲁ* and *ⲃ** is denoted *ⲁⲃ*. To make the operands of concatenation clear, parenthesis will sometimes be used to separate the Characters being concatenated, e.g. *ⲁ(ⲃ) = (ⲁ)ⲃ = (ⲁ)(ⲃ) = ⲁⲃ*. Character concatenation is defined inductively through the following schema,

    1. Basic Clause: :math:`\forall ⲁ \in \Sigma: ⲁ \varepsilon = ⲁ`
    2. Inductive Clause: :math:`\forall ⲁ, ⲃ \in \Sigma, \forall s \in S: ⲁ(ⲃs) = (ⲁⲃ) s`
    3. Uniqueness Clause: :math:`\forall ⲁ, ⲃ, ⲅ, ⲇ \in \Sigma: (ⲁⲃ = ⲅⲇ) \rightarrow ((ⲁ = ⲅ) \land (ⲃ = ⲇ))` 
    4. Comprehension Clause: :math:`\forall ⲁ \in \Sigma, \forall s \in S: (ⲁs) \in S` ∎

Colloquially, :math:`ⲁⲃ` is the String that results from placing :math:`ⲃ` behind :math:`ⲁ`.

The first clause in Definition 1.1.1 is the basis step of induction which states any Character appended to the Empty Character is the Character itself. The second clause is the inductive step which allows the concatenation of Characters of arbitrary length into Strings through recursion.

The Uniqueness Clause states that if the concatenation of two characters :math:`ⲁ` and :math:`ⲃ`` is equal to the concatenation of two other characters *ⲅ* and :math:`ⲇ`, then it must be the case that :math:`ⲁ` is equal to :math:`ⲅ` and :math:`ⲃ` is equal to :math:`ⲇ`. In other words, there's only one set of Characters that can form a given String through concatenation.

It is assumed that the operation of concatenation is closed with respect to the set of all Strings **S**. In other words, concatenation will always yield a String. This assumption is partly captured in the Comprehension Clause of Definition 1.1.1. This clause ensures that the result of concatenating any Character with a String is a String. However, this clause in and of itself does not ensure the closure of **S** with respect to concatenation. In order to close **S** over concatenation, an additional assumption must be introduced. Before introducing this assumption in the form of an axiom, a brief explanation is required for this departure from convention.

Concatenation as it is normally found in the fields of automata theory or regular expressions is treated as a primitive operation performed between two string operands. Concatenation of multiple strings is then defined inductively, similary to Definition 1.1.1 but differing in the essential quality that it treats of only strings. The current formulation differs in that concatenation in this system is not conceived, at least in the primitive stage, as the "joining" of two or more Strings. Instead, the formal system under construction treats concatenation as an elementary operation that occurs between Characters and Strings, i.e. it is a *hetergeneous* operation.

The reason for this distinction will become clear as the formal theory begins to detail palindromic structures that display symmetry across linguistic levels. It should only be noted at this point that Definition 1.1.1 is a conscious decision to depart from convention.

To make this distinction plain, consider that given an Alphabet :math:`\Sigma` and Definition 1.1.1, one still cannot say the result of a concatenation of two Characters is a String, nor make any claim about the contents of :math:`S`, the set of all Strings. The Comprehension Clause of Definition 1.1.1 only states the result of concatenating a Character with a String is a String. It says nothing at all about whether or not single Characters themselves are Strings, and thus it says nothing about whether the result of concatenating two or more Characters is itself a String. 

In order to rectify this, the first (official) Axiom is now introduced.

**Axiom C.1: The Character Axiom**

.. math::

    \forall ⲁ \in \Sigma: ⲁ \in S

This Axiom states the intuitive notion that all Characters are Strings. This includes Empty Characters and Delimiter Characters. This Axiom, in conjunction with Definition 1.1.1, immediately populates the set of all Strings **S** with an uncountably infinite domain of objects (See Theorem 1.1.2 for an informal proof of this fact) consisting of every possible combination of Characters from the Alphabet, in every possible order. In other words, Axiom C.1 in conjunction with Definition 1.1.1 ensure the domain is non-Empty. 

**Example** Let *s = 𝔞𝔟𝔠* and *t = 𝔡𝔢𝔣*. The concatenation of these two Strings *st* is written,

.. math::

    st = (\mathfrak{abc})(\mathfrak{def}) 
    
Using the inductive clause, this concatenation can be grouped into simpler concatenations as follows,    
    
.. math::

    \mathfrak{a}(\mathfrak{b}(\mathfrak{c}(\mathfrak{d}(\mathfrak{ef})))) = (((((\mathfrak{ab})\mathfrak{c})\mathfrak{d})\mathfrak{e})\mathfrak{f}) = \mathfrak{abcdef}

Therefore, *st = 𝔞𝔟𝔠𝔡𝔢𝔣* ∎

Length
^^^^^^

It will sometimes be convenient to represent Strings as ordered sets of Characters, rather than serialized concatenations of Characters. The two formulations are equivalent, but the set representation has advantages when it comes to quantification and symbolic logic. When a String or Word representation is intended to be interpretted as a set, it will be written in bold uppercase letters. For example, the String represented as the concatenation *s*:sub:`1` *= 𝔞𝔟𝔠* would be represented in this formulation as a set of ordered pairs **S**:sub:`1`, where the first coordinate encodes the position of the Character in the String,

.. math::

    S_1 = \{ (1, \mathfrak{a}), (2, \mathfrak{b}), (3, \mathfrak{c}) \}

Note, since sets do not preserve order, this would be equivalent to,

.. math::

    { (3, \mathfrak{a}), (2, \mathfrak{b}), (1, \mathfrak{c}) }

To simplify notation, it is sometimes beneficial to represent this set as a sequence that *does* preserve order as,

.. math::

    S_1 = (\mathfrak{a}, \mathfrak{b}, \mathfrak{c}) 

However, before adopting this notation formally, a problem exists. It is the intention of this analysis to treat Empty Characters as vacuous, i.e. Characters without semantic content. However, this does not mean the Empty Character will not be treated as a legitimate entity within the confines of the formal system. Instead, the goal is to construct a formal system that excludes the Empty Character from the domain of semantics, but not the domain of syntax. 

Due to the nature of the Empty Character and its ability to be concatenated ad infinitum, and the desire to construct a theory of Words and Language that emerges from the transcendental domain of Strings, the construction of the Character-level set representation of a String requires a special algorithm to filter out any Empty Characters while preserving the relative order of the non-Empty Characters concatenated into the String. 

Before presenting the *Emptying Algorithm* that will allow the construction of the Character-level representation of an arbitrary String, motivation for the particular form of the Emptying Algorithm is given by way of analogy to assembly language in computer science. 

At the most primitive level, iteration in assembly or machine language is essentially achieved through a combination of two components,

    1. Memory Addresses: Data, including Strings (which are just sequences of Characters), is stored in memory at specific addresses.
   
    2. Registers: The CPU has special memory locations called registers. Registers are used to hold, 

        - Data: Values being currently processed.
        - Pointers: Memory addresses of data being accessed.
        - Counters: Values used to keep track of the iteration's progress.
        - Instructions: The CPU executes a sequence of instructions.

The Instruction set consists of operations for,

   - Load data: Move data from memory to registers.
   - Store data: Move data from registers to memory.
   - Arithmetic operations: Perform calculations (like adding 1).
   - Conditional jumps: Change the flow of execution based on certain conditions (e.g., checking if a counter has reached a certain value).

At the assembly level, a typical algorithm for iterating through a String is given below (the semi-colon ";" denotes a code comment),

.. code-block::

    ; Assume:
    ;   - String "abc" is stored at memory address STRING_START
    ;   - STRING_START: 'a', 'b', 'c', 0  (0 is a null terminator indicating the end)
    ;   - Register R1 will be used as a pointer (initially holds STRING_START)
    ;   - Register R2 will be used as a counter (initially holds 0)

    LOOP_START:
        LOAD R3, (R1)     ; Load the character at the address in R1 into R3
        CMP R3, 0        ; Compare R3 with the null terminator (0)
        JE LOOP_END      ; If R3 is 0 (equal), jump to LOOP_END
        ADD R1, 1        ; Increment R1 (move the pointer to the next character's address)
        ADD R2, 1        ; Increment the counter R2
        JMP LOOP_START   ; Jump back to LOOP_START
    LOOP_END:

A step-by-step breakdown of this algorithm is instructive for understanding how iterationg through String is implemented at the most basic level in the theory of computation. Each command in this assembly-like language is broken down as follows,

    1. R1 (pointer) is set to STRING_START.
    2. R2 (counter) is set to 0.
    3. LOOP_START: This is a label marking the beginning of the loop.
    4. LOAD R3, (R1): The Character at the memory address stored in R1 is loaded into register R3.
    5. CMP R3, 0: The character in R3 is compared to the null terminator (0).
    6. JE LOOP_END: If the comparison is equal (meaning we've reached the end of the string), the program jumps to the LOOP_END label.
    7. ADD R1, 1: This is the crucial step where the pointer is incremented. 1 is added to R1 because each Character occupies one memory location (in this simplified example). This moves the pointer to the next Character's address.
    8. ADD R2, 1: The counter is incremented.
    9. JMP LOOP_START: The program jumps back to the beginning of the loop.

The key idea is this algorithm is *"unaware"* of how *long* the String is that is stored in the *R1* register. The algorithm naively iterates over the data and then checks whether or not the data has been processed with the command *CMP R3, 0*, i.e. the algorithm checks whether or not the next Character in the String *exists*. 

By treating Strings as Characters stored sequentially in a data register, this algorithm is able to construct a representation of the String on a higher level, allowing for the definition of derivative concepts, like String Length. 

This insight leads directly to the definition of the Character-level set representation of a String and its construction via the Emptying Algorithm.

**Definition 1.1.2: Character-level Set Representations**

Let *t* be a String with Characters *𝔞*:sub:`i`. The Character-level set representation of *t*, denoted by bold uppercase letters **T**, is defined as the ordered set of Characters obtained by removing each Empty Character, *ε*. Formally, **T** is constructed using the *Emptying Algorithm* 

**Algorithm 1: The Emptying Algorithm**

The Emptying Algorithm takes a string *t* as input, which can be thought of as a sequence of Characters *𝔞*:sub:`1`, *𝔞*:sub:`2`, *𝔞*:sub:`3`, ... , where some characters might be *ε*. It then initializes a set to hold **X** and an index for the Characters it will add to **X**. The algorithm iterates the index and constructs the Character-level representation by ignoring *ε*. The Emptying Algorithm is formally defined below.

.. topic:: Algorithm Empty(t: String)

    # Input: A string t
    # Output: An ordered set T representing the character-level set representation of t

    # Initialization
    ## empty set to hold Character-level representation
    T ← ∅
    ## index for non-Empty Characters in T
    j ← 1 
    ## index for iterating through original String t
    i ← 1 

    # Iteration
    1. While 𝔞:sub:`i` exists:

        a. If 𝔞:sub:`i` ≠ ε:

            i. T ← { (j, 𝔞:sub:`i`) } ∪ T
            ii. j ← j + 1

        b. i ← i + 1

    1. Return T ∎

Step 1 in the Emptying Algorithm is essentially equivalent to a *try-catch* block in modern programming languages. Step 1 is materially different than comparing a Character in a String to the Empty Character. Step 1 relies on the idea that attempting to select a Character outside of the String is an undefined operation and will thus result in an error (i.e. a stack overflow). As the Characters in a String are iterated through, as long as the String is not infinite, the iteration will eventually reach the last Character, and once it tries to select the next Character, it will throw an error. 

This point is important because the Emptying Algorithm must remain *"unaware"* of String Length. The essence of the Emptying Algorithm is that it implicitly defines the length of the String as its number of non-Empty Characters, without explicitly stating that is what *String Length* is or how it is calculated. This is crucial to the formalization of Strings as ordered sequences of Characters, because it allows String Length to be defined without any circularity. In other words, this formalization avoids the vicous circle of defining the Character-level representation in terms of String Length and then defining String Length as the cardinality of the Character-level representation.

The following example illustrates a simple application of the Emptying Algorithm.

**Example**

Let *t = ("ab")(ε)("c")*.

   1. i = 1, 𝔞:sub:`1` = "a". Add (1, "a") to T. j increases to 2. i increases to 2.
   2. i = 2, 𝔞:sub:`2` = "b". Add (2, "b") to T. j increases to 3. i increases to 3.
   3. i = 3, 𝔞:sub:`3` = ε. Skip Empty Character. i increases to 4.
   4. i = 4, 𝔞:sub:`4` = "c". Add (3, "c") to T. j increases to 4. i increases to 5.
   5. i = 5, 𝔞:sub:`5` does not exist. Algorithm halts.  

The result returned by the Emptying Algorithm would then be,

.. math::

    T = \{ (1, \text{"a"}), (2, \text{"b"}), (3, \text{"c"}) \} 

Note the Emptying Algorithm results in consecutive indices while also removing the Empty Character. ∎

This method of abstraction and notation will be employed extensively in the subsequent proofs. It will be made more convenient with Character Index notation in the next section, after the preliminary notion of *String Length* is defined. However, in order to define String Length, a method of referring to a String as a set of ordered non-Empty Characters is required. The construction afforded by the Emptying Algorithm operating on any input String *t* will serve that purpose.  

As a brief aside, it may seem the formal system would be better developed by excluding the Empty Character altogether from its Alphabet. The Empty Character's presence in the Alphabet complicates matter extensively, requiring intricate and subtle definitions. 

The reasons for this are two-fold. First: the Empty Character *ε* will be necessary for defining the *Pivot* of a Palindrome, the point around which a certain class of Palindrome reflect. Second: Strings consisting of only the Empty Character are not a mere novelty of abstraction; They play a crucial role in computer science and database management. Any rigorous formal system that excludes the notion of an Empty Character will fail to describe the exact domain from which Language arises, and thus it may fail to account for pre-Language syntactical conditions that necessarily affect the formation of Language.

This approach is not without its challenges. As Definition 1.1.3 below will make clear, if *ε* is considered part of the Alphabet, the typical notion of a String's Length is undefined, as *ε* can be concatenated an infinite number of times to a String without altering its content. To explicate the notion of *length*, consider the constraints that must be placed on this concept in the palindromic system,

    - The length of the string "abc" is 3, as it contains three non-Empty Characters.
    - The length of the string "aεbεc" is still 3, as the Empty Characters (*ε*) are not counted.

This example motivates the following definition.

**Definition 1.1.3: String Length** 

Let *t* be a String. Let **T** be the Character-level set representation of *t* constructed through the Emptying Algorithm in Definition 1.1.2. The String Length of *t*, denoted *l(t)*, is the number which satisfies the following formula,

.. math::

    l(t) = | T | 
    
∎

**Example** 

Consider the String *t = ("aa")(ε)("b")(ε)("bcc")*

By Definition 1.1.3, 

.. math::

    T = \{ (1, \text{"a"}), (2, \text{"a"}), (3, \text{"b"}), (4, \text{"b"}), (5, \text{"c"}), (6, \text{"c"}) \}

Therefore, 

.. math::

    | T | = 6 
    
∎

This formalization of String Length, with the Emptying Algorithm, while perhaps prosaic, maps to the intuitive notion of a String's length, i.e. the number of non-Empty Characters, while still allowing for a calculus of concatenation that involves Empty Characters. For reasons that will become clear in Section II, *l(s)* will be called the *String Length* of a String s. 

To confirm Definitions 1.1.2 and 1.1.3 correspond to reality, a theorem confirming its expected behavior is now derived. Definition 1.1.3 ensures the String Length of concatenated Strings is equal to the sum of their individual String Lengths, as demonstrated by Theorem 1.1.1.

**Theorem 1.1.1** :math:`\forall u, t \in S : l(ut) = l(u) + l(t)`

Let *u* and *t* be arbitrary strings in **S**. Let **U** and **T** be the character-level representations of *u* and *t*, respectively,

.. math::

    U = ( \mathfrak{a}_1, \mathfrak{a}_2, ..., \mathfrak{a}_{l(s)} )

.. math::

    T = ( \mathfrak{b}_1, \mathfrak{b}_2, ..., \mathfrak{b}_{l(t)} )

Let *ut* be the concatenation of *u* and *t*. By Definition 1.1.1, the Character-level representation of *ut* is,

.. math::

    UT = ( \mathfrak{a}_1, \mathfrak{a}_2, ..., \mathfrak{a}_{l(s)}, \mathfrak{b}_1, \mathfrak{b}_2, ..., \mathfrak{b}_{l(t)})

By Definition 1.1.3, the String Length of a String is the number of indexed non-Empty Characters it contains. Thus, :math:`l(u)` is the number of non-Empty Characters in *u*, :math:`l(t)` is the number of non-Empty Characters in *t*, and :math:`l(ut)` is the number of non-Empty Characters in *ut*.

Since concatenation simply joins Characters without adding or removing Characters, with the possible exception of Empty Characters through the Basis Clause of Definition 1.1.1, the non-Empty Characters in *ut* are precisely the non-Empty Characters from *u* followed by the non-Empty Characters from *t*.

Therefore, the total number of non-Empty Characters in *ut* is the sum of the number of non-Empty characters in *u* and the number of non-Empty Characters in *t*,

.. math::

    l(ut) = l(u) + l(t)

Since *u* and *t* were arbitrary strings, this can be generalized over the set of all Strings,

.. math::

    \forall u, t \in S : l(ut) = l(u) + l(t)`

∎

With the concept of String Length now defined, it is also a simple matter to define String Equality in terms of Character Equality using the Equality Axiom C.0.

**Definition 1.1.4: String Equality**

Let *t* be a String. Let **T** be the Character-level set representation of *t* constructed through Definition 1.1.2,

.. math::

    T = \{ (i, \mathfrak{a}_i) | 1 \leq i \leq l(t) \}
     
Let *u* be a String. Let **U** be the Character-level set representation of *u* constructed through Definition 1.1.2,

.. math::

    U = \{ (i, \mathfrak{b}_j) | 1 \leq j \leq l(u) \}

The string *t* is said to be *equal* to String *u* if the Strings have equal length and the Characters at each corresponding index are equal. Formally, *t = u* if and only if,

    1. :math:`l(t) = l(u)` (The String Lengths of t and u are equal)
    2. :math:`\forall i \in N_{l(t)}: \mathfrak{a}_{i} = \mathfrak{b}_{i}` (The Characters at each corresponding index are equal) ∎

Finally, String Length provides the means for a quality-of-life enhancement to the formal system in the form of Character Index notation.

**Definition 1.1.5: Character Index Notation**

Let *t* be a string with Character-level representation **T**,
 
 .. math::

    T = (\mathfrak{a}_1, \mathfrak{a}_2, ..., \mathfrak{a}_{l(t)}). 
    
Then for any *i* such that :math:`1 \leq i \leq l(t)`, :math:`t[i]` is defined as *𝔞*:sub:`i`, where :math:`(i, \mathfrak{a}_i) \in T`. ∎

Character Index notation will simplify many of the subsequent proofs, so it is worth taking a moment to become familiar with its usage. Indexing starts at 1, consistent with the definition of **N**:sub:`n` made in the preamble. So, *t[1]* is the first character of *t*, *t[2]* is the second, and so on.

In terms of the Character-level set representation, *t[i]* refers to the Character at position *i* in the set **T**. In other words, the notation *t[i]* implicitly assumes the String *t* has already been stripped of its Empty Characters through the Emptying Algorithm in Definition 1.1.2. This notation can effectively replace the use of lowercase Fraktur letters with subscripts (e.g., *𝔞*:sub:`i`) when referring to specific Characters within Strings.

**Example**

If *s = "abc"*, then *s[1] = "a"*, *s[2] = "b"*, and *s[3] = "c"*. ∎

With the notion of String Length established for each element in the domain and some of its basic properties established, the size of the domain itself, **S**, will now be elaborated in greater detail.
  
It is assumed **S** is at least uncountably infinite. A rigorous proof of this fact would carry the current work too far into the realm of real analysis, but as motivation for this assumption, an informal proof is presented below based on Cantor's famous diagonalization argument. 

**Theorem 1.1.2** :math:`| S | \geq \aleph_{1}`

Assume, for the sake of contradiction, that the set of all Strings **S** is countable. This means the Strings can be listed in some order, 

.. math::
    
    s_1, s_2, s_3, ...

Now, construct a new String *t* as follows:

    1. The first character of *t* is different from the first character of *s*:sub:`1`.
    2. The second character of *t* is different from the second character of *s*:sub:`2`.
    3. etc.

This string *t* will be different from every string in **S** contradicting the assumption that it was possible to list all strings. Therefore, **S** must be uncountable. ∎ 

Containment
^^^^^^^^^^^

Similar to the explication of *length*, the notion of a String *containing* another String must be made precise using the definitions introduced so far. It's important to note that in the current system the relation of *containment* is materially different from the standard subset relation between sets. For example, the set of characters in *"rat"* is a subset of the set of characters in *"tart"*, but *"rat"* is not contained in *"tart"* because the order of the characters is different.

Consider the Strings *"rat"* and *"strata"*. The string *"rat"* *is contained* in the String strata", because the order of the String *"rat"* is preserved in *"strata"*. An intuitive way of capturing this relationship is to map the indices of the Characters in *"rat"* to the indices of the Characters in *"strata"* which correspond to the indices in *"rat"*. A cursory (but incorrect) definition of *containment* can then be attempted, using this insight as a guide.

**Containment (Incorrect Version)** :math:`t \subset_{s} u` 

Let *t* and *u* be Strings. *t* is said to be *contained in u*, denoted by,

.. math::

    t \subset_{s} u

If and only if there exists a strictly increasing function :math:`f: N_{l(t)} \rightarrow N_{l(u)}` such that:

.. math::

    \forall i \in N_{l(t)}: t[i] = u[f(i)]
    
∎
    
This definition essentially states that *t* is contained in *u* if and only if there's a way to map the Characters of *t* onto a subsequence of the Characters in *u* while preserving their order. The function *f* ensures that the Characters in *t* appear in the same order within *u*. While this definition is incorrect, the reason why this version of *containment* fails is instructive in developing a better understanding of the subtlety involved in attempting its definition. 

First, consider an example where this definition correlates with the intuitive notion of *containment*. Let *t = "rat"* and *u = "strata"*. Then, these Strings can be represented in set notation as,

.. math::

    T = \{ (1, \text{"r"}), (2, \text{"a"}), (3, \text{"t"}) \}
     
.. math::

    U = \{ (1, \text{"s"}), (2, \text{"t"}), (3, \text{"r"}), (4, \text{"a"}), (5, \text{"t"}), (6, \text{"a"}) \}.

The function *f* defined as :math:`f(1) = 3`, :math:`f(2) = 4`, and :math:`f(3) = 5`` satisfies the condition in the proposed definition, as it maps the characters of *"rat"* onto the subsequence *"rat"* within *"strata"* while preserving their order. In addition, *f* is a strictly increasing function. Therefore, 

.. math::

    \text{"rat"} \subset_{s} \text{"strata"}

Next, consider a counter-example. Let *t = "bow"* and *u = "borrow"*. Then their corresponding set representations are given by,

.. math::

    T = \{ (1, \text{"b"}), (2, \text{"o"}), (3, \text{"w"}) }
     
.. math::

    U = \{ (1, \text{"b"}), (2, \text{"o"}), (3, \text{"r"}), (4, \text{"r"}), (5, \text{"o"}), (6, \text{"w"}) }

The function defined through :math:`f(1) = 1`, :math:`f(2) = 5` and  :math:`f(3) = 6` satisfies the conditions of the proposed definition. However, intuitively, *"bow"* is *not contained* in the word *"borrow"*. The reason the proposed definition has failed is now clear: the function *f* that is mapping *"bow"* to *"borrow"* skips over the Character indices 2, 3 and 4 in *"borrow"*. In other words, in addition to being strictly increasing, the function *f* which maps the smaller String onto the larger String must also be *consecutive*. This insight can be incorporated into the definition of *containment* by first defining the notion of *consecutive*,

**Definition 1.1.6: Consecutive Functions** 

A function *f* is consecutive over N:sub:`s` if it satisfies the formula,

.. math::

    \forall i, j \in N_s: (i < j) \rightarrow f(j) = f(i) + (j - i)`
    
∎
    
This additional constraint on *f* ensures that the indices of the larger String in the containment relation are mapped in a sequential, unbroken order to the indices of the smaller String. This definition of *Consecutive Functions* can be immediately utilized to refine the notion of *containment*.

**Definition 1.1.7: Containment** :math:`t \subset_{s} u` 

Let *t* and *u* be Strings. *t* is said to be *contained in u*, denoted by,

.. math::

    t \subset_{s} u

If and only if there exists a strictly *increasing and consecutive* function :math:`f: N_{l(t)} \rightarrow N_{l(u)}` such that:

.. math::

    \forall i \in N_{l(t)}: t[i] = u[f(i)] 
    
∎

The notion of containment will be central to developing the logic of palindromic structures in the subsequent sections. The next theorem establishes a fundamental property regarding containment.

**Theorem 1.1.3** :math:`\forall s \in S: \varepsilon \subset_{s} s`

Let *s* be an arbitrary string in **S**. By Definition 1.1.3, *l(ε) = 0*. Thus,

.. math::

   1. N_{l(ε)} = \emptyset

The empty function :math:`f: \emptyset \rightarrow N_{l(s)}` vacuously satisfies the condition for containment (Definition 1.1.7), as there are no elements in the domain to violate the condition. Therefore, 

.. math::

    2. \varepsilon \subset_{s} s

Since *s* was arbitrary, this can be generalized over the set of all Strings,
 
.. math::

    \forall s \in S: \varepsilon \subset_{s} s
    
∎

Section I.II: Words
-------------------

While the notion of Characters maps almost exactly to the intuitive notion of letters in everyday use, the notion of a *Word* requires explication. 

If Characters are mapped to letters in the Alphabet of a Language **L**, the set of all Strings would have as a subset the Language that is constructed through the Alphabet. The goal of this section is to define the syntactical properties of Words in **L** that differentiates them from Strings in **S** based solely on their internal cohesion as a linguistic unit. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations. In other words, this analysis will proceed without assuming anything about the interpretation of the Words in the Language beyond the fact that they *are* Words of the Language. The goal is to leave the semantic interpretation of Words in a Language as ambiguous as possible. This ambiguity, it is hoped, will leave the results of the analysis applicable to palindromic structures in a variety of languages, and perhaps make the formal system applicable to areas outside the realm of Palindromes.

**Definition 1.2.1: Language** 

A Language **L** is a set of Strings constructed through concatenation on an Alphabet **Σ** that are assigned semantic content. ∎

**Definition 1.2.2: Word** 

A Word is an element of a Language **L**. ∎

The following symbolic notation is introduced for these terms, 

    1. Words (*a*, *b*, *c*, etc.): Lowercase English letters represent Words. Subscripts will occassionally be used to denote Words, (*a*:sub:`1`, *a*:sub:`2`, ... )
    2. Language (**L**): The uppercase English letter *L* in boldface represents a Language.

In the case of English, Words would correspond to words such as "dog", "cat", etc. A Language would correspond to a set of words such as *{ "dog", "cat", "hamster", ... }* or *{ "tree", "flower", "grass", .... }*. The number of Words in a Language is denoted | L |.

Again, at the risk of unwarranted repetition, Language is assumed to be a *fixed set* known a priori to the construction of the current formal system. It not the goal of the formal system to describe the semantic conditions for a Word's eligibility in Language or how a Language is constructed from elementary Characters and Strings into a class of Words through systems like grammar or pragmatics, but rather, given a Language of Words, the formal system seeks to elaborate the syntactical conditions that are imposed on Language by its nature as a set of Strings with ordered Characters. 

Note, Definition 1.2.1 and Definition 1.2.2 relies on the idea that Words are Strings and their meaning is conveyed through the ordered sequence of its concatenated Characters. This necessarily precludes from the formal system any languages which do *not* use the ordering of Characters as the primary medium for representing Words. While edge cases like sign language exist, nevertheless, the sole constitutive feature of any natural is the *ordering* of some type of Character. In the case of sign language, a Character in the formal system might be identified with *"a configuration of fingers"* and a String might be identified with *"configurations over time"*.

It will sometimes be necessary to refer to indeterminate Words, so notation is introduced for Word Variables,

    1. Word Variables (*α*, *β*, *γ*, etc. ): Lowercase Greek letters will represent variable words, i.e. indeterminate Words. Subscripts will occassionally be used to denote Word Variables, (*α*:sub:`1`, *α*:sub:`2`, ... ). 

The exceptions to this rule for Lowercase Greek letters are Zeta and Xi, *ζ* and *ξ*, which are reserved for Sentential Variables (see Section II.I for more information.), Sigma and Epsilon, *σ* and *ε*, which are reserved for the Delimiter and Empty Character (see Section I.I for more information), Omega, *ω*, which is reserved for the Palindromic Pivot (see Section III.II for more information), and the lowercase final Sigma, *ς*, which is reserved for *σ*-reductions (see Section III.I for more information)

The range of a Word Variable is understood to be the Language **L** from the Words are being drawn. 

With these definitions, the hierarchy of relationships that exist between a Word *α*, its Language **L** and the set of all Strings **S** is given by,

    1. :math:`\alpha \in L`
    2. :math:`\alpha \in S`
    3. :math:`L \subset S`

To clarify the relationship between Strings, Words and Language in plain language,

    1. All Words belong to a Language.
    2. All Words belong to the set of all Strings
    3. Language is a subset of the set of all Strings.
    4. Not all Strings are Words. 

As mentioned several times, all objects in this formal system are defined on the domain of Strings through either the set relation of "belonging" or the set relation of "subset". Words and Characters are different types of Strings, while a Language is a subset of Strings. Because Words are Strings, defining their equality is a simple matter of referring back to the definition of String Equality.

**Definition 1.2.3: Word Equality**

Let *a* and *b* be words in **L**. Then *a = b* if and only if *a* and *b* are equal as Strings (according to Definition 1.1.4). ∎ 

The next axiom represents the minimal *necessary* assumptions that are placed on any String to be considered an element of a Language **L**, i.e. a Word. The axiom listed in this section is not *sufficient*; in other words, it is possible for a String to satisfy this axiom without being an element of a Language, but any Word that belongs to a Language must satisfy the axiom.

**Axiom W.1: The Discovery Axiom** 

.. math::

    \forall \alpha \in L: [ (l(\alpha) \neq 0) \land (\forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma) ]

∎

There are two conjuncts in the Discovery Axiom and each of them captures a noteworthy assumption that is being made about Words in a Language. The first conjunct, (:math:`l(\alpha) \neq 0`), will be used to prove some fundamental properties of Words in the next section. This condition that a Word's String Length cannot be equal to zero serves a dual purpose. First, by Definition 1.1.3, it ensures the Empty Character cannot be a Character in a Word (this fact will be more rigorously proven in Theorem 1.2.4 below), preventing vacuous semantic content. 

Second, in order for two Words to be distinguished as the same Word, there must be dimensions of comparision over which to assert the equality. One must have some criteria for saying *this* linguistic entity is equal to that *that* linguistic entity. String Length serves as one of the two dimensions for a Word necessary for a word to be "embodied" in a medium (the other being the inherent ordinality of Characters in a Word). In other words, the concept of String Length is foundational to the discovery of Words from the set of all Strings **S**. One must be able to discard those Strings possessing null content before one can engage in Language. 

While the definition of String Length and the first conjunct preclude the inclusion of the Empty Character in a Word, there is no such restriction on the Delimiter, hence the second conjunct of the Discovery Axiom. This conjunct captures the common-sense notion that a Word from a Language cannot contain a Delimiter; Instead, Delimiters are what separate Words from one another in a String. 

It is these two purely syntactical properties that allow a user of Language to separate Words from the arbitrary chaos of Strings, preparing them for the assignment of semantic content. 

Theorems
^^^^^^^^

The next theorems establish some basic results about Words in a Language within this formalization. All of these theorems should conform to the common sense notion of Words. 

**Theorem 1.2.1** :math:`\forall \alpha \in L:  \alpha \varepsilon = \varepsilon \alpha = \alpha`

This theorem can be stated in natural language as follows: For every Word in a Language, concatenating the Word with the empty String *ε* on either side results in the Word itself.

Let *α* be an arbitrary word in **L**. By Definition 1.2.2, *α* is a String of characters. By Definition 1.1.3, :math:`l(\alpha)` is the number of non-Empty Characters in *α*. 

Consider *ε*, the empty string. By Definition 1.1.3, :math:`l(\varepsilon) = 0`. By Definition 1.1.1, the concatenation of any String *s* with *ε* results in a new string with the same Characters as *s* in the same order.

Therefore, *αε* and *εα* are both Strings with the same Characters as *α* in the same order. Since *α* is a Word in **L** and concatenation with *ε* does not change its length or order of Characters. Thus, by Definition 1.2.3, 

.. math::

    \alpha\varepsilon = \varepsilon\alpha = \alpha.

Since *α* was arbitrary, this can be generalized over the Language, 

.. math::

    \forall \alpha \in L:  \alpha \varepsilon = \varepsilon \alpha = \alpha

∎

**Theorem 1.2.2** :math:`\forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \subset_{s} \alpha`

This theorem can be stated in natural language as follows: All Characters in a Word are contained in the Word.

Assume *α* is a Word from Language **L**. By the Axiom W.1, :math:`l(\alpha) \neq 0`` and thus it must have at least one non-Empty Character *α[i]* for some non-zero *i*.

Consider the String *s* with a single Character :math:`𝔟_1 = \alpha[i]`.

.. math::

    s = \alpha[i]

Clearly, by Definition 1.1.3, :math:`l(s) = 1`. To show that *s* is contained in *α*, a strictly increasing and consecutive function that maps the Characters in *s* to the Characters in *α* must be found. Since :math:`l(s) = 1`, this can be defined simply as,

.. math::

    f(1) = i

For any value of *i*. Therefore, by Definition 1.1.7,

.. math::

    \alpha[i] \subset_{s} \alpha 
    
Since *α* and *i* are arbitary, this can be generalized, 

.. math::

    \forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \subset_{s} \alpha

The next theorem, Theorem 1.2.3, is the direct result of defining String length as the number of non-Empty characters in a String and then defining containment based on String length. Careful inspection of Definition 1.1.7 will show that it depends on a precise notion of String Length. In other words, in the current formal system, containment is derivative of length. The order of definitions and axioms in any formal system of Language cannot be of an arbitary character. There is an inherent hierarchical structure in linguistics that must be captured and formalized in the correct order.

**Theorem 1.2.3**  :math:`\forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon`

Let *α* be an arbitrary word in **L**, and let *i* be a natural number such that,
 
.. math::

    1 \leq i \leq l(\alpha)
    
By the Discovery Axiom W.1, it is known that :math:`l(\alpha) \neq 0`.

By Definition 1.1.3, the length of a String is the number of non-Empty Characters it contains in its Character-level set representation **Α**. Since :math:`l(\alpha) > 0`, *α* must have at least one non-Empty character.

Since :math:`1 \leq i \leq l(\alpha)`, the Character at position *i* in *α*, denoted *α[i]*, exists and is non-Empty, :math:`α[i] \neq \varepsilon`. Since *α* and *i* are arbitrary, this can generalized over the Language,

.. math::

    \forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon

∎

Theorem 1.2.1 - 1.2.3 are the necessary logical pre-conditions for Words to arise from the domain of Strings. In essence, before Language can be distinguished from its uncountably infinite domain, a way of measuring String length must be introduced. This definition must prevent Empty Strings from entering into the Language, which would otherwise allow the annunciation of null content. Then it must be assumed for semantic content to be assigned to a series of concatenated Characters the length of that String must be non-zero. This is the meaning of the first conjunct in the Discovery Axiom W.1.

Language is materially different from its un-structured domain of Strings for this reason. Language does not possess null content. Language is measureable. Words in Language have String Length. Moreover, Words are delimited. In other words, Words are separable, distinct linguistic entities. These facts are guaranteed by the Discovery Axiom W.1 and Theorem 1.2.1 - Theorem 1.2.3. These results provide the canvas upon which the rest of the theory will be drawn.

There may appear to be a contradiction in the results of Theorem 1.1.3, which states the Empty Character is contained in every String, and Theorem 1.2.3, which states no Character in a Word can be the Empty Character. Every Word is a String, by Definition 1.2.2, so the results appear at odds. The solution to this apparent contradiction lies in how Characters and Strings have been formalized as distinct, but interrelated, terms. The contradiction is no longer a contradiction once the distinction between a String being contained in another String and a Character being a constituent element at a specific position with in a String is understood.

The containment relation :math:`\varepsilon \subset_{s} s` refers to the Empty Character as a subsequence of *s*. The relation being expressed is about the sequence of Characters, and the Empty sequence is always a subsequence of any other sequence.

Theorem 1.2.3, on the other hand, refers to individual Characters at specific positions within a Word. It is a claim about the elements of the Character-level representation (e.g., the *ⲁ* in :math:`(i, ⲁ) \in \Alpha`).

Inversion
^^^^^^^^^

Before developing the palindromic structure and symmetries in Words and Language, an operation capable of describing this symmetry much be introduced. Informally, the *Inverse* of a String is the reversed sequence of Characters in a String. The goal of this section is to define this notion precisely. In the process, the motivation for this definition as it pertains to Words will be elucidated. 

**Definition 1.2.4: String Inversion** 

Let *s* be a string with length *l(s)*. Then, let *t* be a String with length *l(t)*.
    
*t* is called the Inverse of *s* and is denoted *inv(s)* if it satisfies the following conditions, 

.. math::

    l(t) = l(s)

.. math::

    \forall i \in N_{l(s)}: t[i] = s[l(s) - i + 1]
 
∎

Note the advantage of Character Index notation in stating this definition. The quantification in the second clause of Definition 1.2.4 can be made directly over the natural numbers, rather than the intermediary of the Character level set representation of *t* and *s*.

**Example**

Let *s = "abcde"* (:math:`l(s) = 5`). Then :math:`\text{inv}(s) = t = \text{"edcba"}`

.. math::

    t[1] = s[5 - 1 + 1] = s[5] = \text{"e"}

.. math::

    t[2] = s[5 - 2 + 1] = s[4] = \text{"d"}

.. math::

    t[3] = s[5 - 3 + 1] = s[3] = \text{"c"}
    
.. math::

    t[4] = s[5 - 4 + 1] = s[2] = \text{"b"}
    
.. math::

    t[5] = s[5 - 5 + 1] = s[1] = \text{"a"} 
    
∎

Since every Word is a String, the Inverse of Word is similarly defined, with the additional constraint that *s* belong to a Language **L**, i.e. by adding a third bullet to Definition 1.2.4 with :math:`s \in L`. The Inverse of a Word is easily understood through a few illustrative examples in English. The following table lists some words in English and their Inverses,

| Word | Inverse | 
| ---- | ------- |
| time | emit    |
| saw  | was     |
| raw  | war     |
| dog  | god     |
| pool | loop    |

However, this particular example is (intentionally) misleading. In this example, the Inverse of a word in English is also a word in English. In general, this property is not exhibited by the majority of Words in any Language. In other words, every Word in an Language has an Inverse but not every Inverse Word belongs to a Language. This phenomenon is exemplified in the following table,

| Word | Inverse | 
| ---- | ------- |
| cat  | x       |
| you  | x       |
| help | x       |
| door | x       |
| book | x       |

The intent is to define a class of Words whose elements belong to it if and only if their Inverse exists in the Language. As a first step towards this definition, String Inversion was introduced and formalized. In the next section, String Inversion will provide a subdomain in the domain of discourse over which to quantify the conditions that are to be imposed on the class of *Invertible Words*, i.e. the class of Words whose Inverses are also Words. 

Note, Invertible Words are often termed *semordnilaps* in linguistics. The terminology *invertible* is adopted here to emphasis the structural inversion that is occuring on the Character-level within this class of Words. 

Before defining the class of Invertible Words in the sequel, this section is concluded with theorems that strengthen the definition of String Inversion. These theorems will be used extensively in all that follows.

**Theorem 1.2.4** :math:`\forall s \in S: \text{inv}(\text{inv}(s)) = s`

Let *s* be a String with length *l(s)* and Characters *𝔞*:sub:`i`. 

Let :math:`t = \text{inv}(s)` with length *l(t)* and Characters *𝔟*:sub:`j`.

By the Definition 1.2.4,

.. math::

    1. l(t) = l(s)

.. math::

    2. \forall i \in N_{l(s)}: t[i] = s[l(s) - i + 1]

Now, let :math:`u = inv(t)` with length *l(u)*. Applying Definition 1.2.4 again,

.. math::

    3. l(u) = l(t)
    
.. math::

    4. \forall j \in N_{l(t)}: u[j] = t[l(t) - j + 1]

Since :math:`l(t) = l(s) = l(u)` and :math:`N_l(t) = N_{l(s)} = N_{l(u)}`(from step 1, step 3 and by definition of natural numbers), these substitions may be made in step 4,

.. math::

    5. \forall j \in N_{l(s)}: u[j] = s[l(s) - (l(t) - j + 1) + 1]

Simplifying the index on the right hand side,

.. math::

    6. \forall j \in N_{l(s)}: u[j] = s[j]

Since *u* and *s* have the same length (:math:`l(u) = l(t) = l(s)`) and the same Characters in the same order (:math:`u[j] = s[j]` for all *i*), by Definition 1.1.4 of String Equality, it can be concluded that :math:`u = s`. Recall that :math:`u = inv(t)` and :math:`t = inv(s)`. Substituting, the desired result is obtained, :math:`inv(inv(s)) = s`. ∎ 

Two versions of Theorem 1.2.5 are given, the first using only the Character-level representation of a String, the second using Character Index notation. This is done to show the two formulations are equivalent, and it is a matter of personal preference which style of notation is employed. Throughout the rest of this work, the Character Index notation is primarily utilized, although there are several proofs that are better served by the Character-level representation.

**Theorem 1.2.5 (Character-level Representation)** :math:`\forall u, t \in S: \text{inv}(ut) = \text{inv}(t)\text{inv}(u)`

Let **U** be the Character level representation of *u*,

.. math::

    1. U = (\mathfrak{a}_1 , \mathfrak{a}_2 , ..., \mathfrak{a}_{l(u)})

Let **T** be the Character level representation of *t*,

.. math::

    2. T = (\mathfrak{b}_1, \mathfrak{b}_2, ... , \mathfrak{b}_{l(t)})

The Character level representation of *ut*, denoted **UT**, is then given by,

.. math::

    3. UT = (\mathfrak{a}_1 , \mathfrak{a}_2 , ..., \mathfrak{a}_{l(u)}, \mathfrak{b}_1, \mathfrak{b}_2 , ... , \mathfrak{b}_{l(t)})

By Definition 1.2.4 of String Inversion, the Character level representation of *inv(ut)* is the reversed sequence of **UT**,

.. math::

    4. \text{inv}(UT) = ( \mathfrak{b}_{l(t)}, ..., \mathfrak{b}_2 , \mathfrak{b}_1 , \mathfrak{b}_{l(u)}, ..., \mathfrak{a}_2 , \mathfrak{a}_1)

The Character level representation of *inv(U)*, denoted **inv(U)**,

.. math::

    5. \text{inv}(U) = (\mathfrak{a}_{l(u)}, ..., \mathfrak{a}_2 , \mathfrak{a}_1)

The Character-level representation of *inv(t)*, denoted **inv(T)** is 

.. math::

    6. inv(T) = ( \mathfrak{b}_{l(t)}, ..., \mathfrak{b}_2 , \mathfrak{𝔟}_1 )

The Character-level representation of *inv(t)inv(u)* is:

    7. ( \mathfrak{b}_{l(t)}, ..., \mathfrak{b}_2 , \mathfrak{b}_1, \mathfrak{a}_{l(u)}, ..., \mathfrak{a}_2 , \mathfrak{a}_1)

Comparing the results from step 4 and step 7, it can be seen the Character-level representations of *inv(ut)* and *inv(t)inv(u)* are identical.

Therefore, :math:`\text{inv}(ut) = \text{inv}(t)\text{inv}(u)`. ∎

**Theorem 1.2.5 (Character Index Notation)**: :math:`\forall u, t \in S: \text{inv}(ut) = \text{inv}(t)\text{inv}(u)`

Let *u* and *t* be arbitrary strings in **S**. Let :math:`l(u) = m` and :math:`l(t) = n`. Then, :math:`l(ut) = m + n`, by Definition 1.1.3.

Let :math:`s = ut`. Let :math:`v = \text{inv}(s) = \text{inv}(ut)`. Let :math:`w = \text{inv}(t)\text{inv}(u).

To prove show the theorem, it must be shown that *v = w*, which means, by Definition 1.1.4, it must be shown that 

.. math::

    1. l(v) = l(w)
    
.. math::

    2. \forall i ∈ N_{l(v)}: v[i] = w[i] 

By repeated applications of Definition 1.2.4, 

.. math::

    3. l(v) = l(s) = l(ut) = m + n
    
.. math::

    4. l(\text{inv}(t)) = l(t) = n
    
.. math::

    5. l(\text{inv}(u)) = l(u) = m. 

From step 3 and step 4, it follows,
 
.. math::

    5. l(w) = l(\text{inv}(t)\text{inv}(u)) = l(\text{inv}(t)) + l(\text{inv}(u)) = n + m = m + n.

From steps 4 and 5, it follows, 

    6. l(v) = l(w) = m + n.

Now it is to be shown that :math:`v[i] = w[i]`` for all :math:`i \in N_{l(v)}`. Let *i* be an arbitrary index such that :math:`1 \leq i \leq m + n`.

**Case 1**: :math:`1 \leq i \leq m + n`

By Definition 1.2.4,

.. math::

    a. v[i] = s[l(s) - i + 1]

Since *l(s) = m + n*, it follows,

.. math::

    b. v[i] = s[m + n - i + 1]
    
Since *m + n - i + 1* corresponds to an index in *t*, it follows,

.. math::

    c. v[i] = t[n - i + 1]
    
By Definition 1.2.4,

.. math::

    d. v[i] = \text{inv}(t)[i]

Since :math:`w = \text{inv}(t)\text{inv}(u)`,

.. math::

    e. v[i] = w[i]

**Case 2**: :math:`n + 1 \leq i \leq m + n`:

By Definition 1.2.4,

.. math::

    a. v[i] = s[l(s) - i + 1]

Since :math:`l(s) = m + n`,

    b. v[i] = s[m + n - i + 1]

Since *m + n - i + 1* corresponds to an index in *u*,

.. math::

    c. v[i] = u[m - (i - n) + 1] 

Simplifying,

    d. v[i] = u[m + n - i + 1]

By Definition 1.2.4,

    e. v[i] = \text{inv}(u)[i - n]

Since :math:`w = \text{inv}(t)\text{inv}(u)`,

    f. v[i] = w[i] (since w = inv(t)inv(u))

In both cases, :math:`v[i] = w[i]` for all :math:`i \in N_{l(v)}`. Since :math:`l(v) = l(w)`, by Definition 1.1.4 it follows :math:`v = w`. Therefore, 

.. math::

    7. \text{inv}(ut) = \text{inv}(t)\text{inv}(u).

Since *u* and *t* were arbitrary Strings, this can generalize over the set of all Strings,

.. math::

    8. \forall u, t \in S: \text{inv}(ut) = \text{inv}(t)\text{inv}(u) ∎

The next theorem establishes the *"distributivity"* of String inversion over the relation of containment. 

**Theorem 1.2.6** :math:`\forall u, t \in S : u \subset_{s} t \leftrightarrow \text{inv}(u) \subset_{s} \text{inv}(t)`

This theorem can be stated in natural language as follows: For any two Strings *u* and *t*, *u* is contained in *t* if and only if the Inverse of *u* is contained in the Inverse of *t*.

Let *u* and *t* be arbitrary Strings in **S**.

(→) Assume,

.. math::

    1. u \subset_s t

By Definition 1.1.7, there exists a strictly increasing and consecutive function :math:`f: N_{l(u)} \rightarrow N_{l(t)}` such that,

.. math::

    1. \forall i \in N_{l(u)}: u[i] = t[f(i)]

Let,

.. math::

    3. v = \text{inv}(t)

.. math::

    4. w = inv(u).

By Definition 1.2.4

.. math::

    5. \forall i \in N_{l(u)}: w[i] = \text{inv}(u)[i] = u[l(u) - i + 1]

.. math::
    
    6. \forall i \in N_{l(t)}: v[i] = \text{inv}(t)[i] = t[l(t) - i + 1]
   
Define a function :math:`g: N_{l(w)} \rightarrow N_{l(v)}`  as follows,

    1. g(i) = l(t) - f(l(u) - i + 1) + 1

This function maps the Character indices of *w* (the inverse of *u*) to the indices of *v* (the inverse of *t*).

**Increasing** To show *g* is strictly increasing, let

    8. i, j ∈ N:sub:`l(w)`

Such that *i < j*. Since *l(w) = l(u)*,

    9. i, j ∈ N:sub:`l(u)`

Because *f* is strictly increasing, and

    10. l(u) - j + 1 < l(u) - i + 1,

It follows,

    11. f(l(u) - j + 1) < f(l(u) - i + 1)
Therefore,

    12. l(t) - f(l(u) - i + 1) + 1 < l(t) - f(l(u) - j + 1) + 1

which means

    13. g(i) < g(j).

Thus, g is strictly increasing.

**Consecutive** To show *g* is consecutive, let

    14. i ∈ N:sub:`l(w)`

Such that *i < l(w)*. Then,

    15. g(i+1) = l(t) - f(l(u) - (i + 1) + 1) + 1
    16. g(i+1) = l(t) - f(l(u) - i - 1 + 1) + 1

Since f is consecutive, we have:

    17. f(l(u) - i - 1 + 1) = f(l(u) - i) + 1

Then,

    18. g(i+1) = l(t) - (f(l(u) - i) + 1) + 1
    19. g(i+1) = l(t) - f(l(u) - i)
    20. g(i+1) = l(t) - f(l(u) - i + 1) + 1 + 1 - 1
    21. g(i+1) = l(t) - f(l(u) - i + 1) + 1
    22. g(i+1) = g(i) + 1

Thus *g* is consecutive.

**Containment** Now, it must shown be that, 

    23.  ∀ i ∈ N:sub:`l(w)`: w[i] = v[g(i)]

By Definition 1.2.4,

    24. w[i] = u[l(u) - i + 1]

From step 2, it follows,

    25. w[i] = t[f(l(u) - i + 1)]

By definition of *g*,

    26. g(i) = l(t) - f(l(u) - i + 1) + 1

Rearranging,

    27. f(l(u) - i + 1) = l(t) - g(i) + 1

Substituting into step 25,

    28. w[i] = t[l(t) - g(i) + 1]

By Definition 1.2.4 and the definition of v,

    29. v[g(i)] = t[l(t) - g(i) + 1]

Therefore,

    30. w[i] = v[g(i)]

Since this holds for all *i* *∈* **N**:sub:`l(w)`, and g is a strictly increasing and consecutive function, by Definition 1.1.7, it follows,

    31. w ⊂:sub:`s` v

Therefore,

    32. inv(u) ⊂:sub:`s` inv(t)

(←) Assume

    1. inv(u) ⊂:sub:`s` inv(t)

By Theorem 1.2.4,

    2. inv(inv(u)) = u
    3. inv(inv(t)) = t

Therefore, using the result just proved in the (→) direction, it can be said since

    4. inv(u) ⊂:sub:`s` inv(t)

This implies,

    5. inv(inv(t)) ⊂:sub:`s` inv(inv(u))

Substituting in steps 2 and 3,

    6. t ⊂:sub:`s` u

Since both directions of the implication hold, it follows,

    7. ∀ u, t ∈ S: u ⊂:sub:`s` t ↔ inv(u) ⊂:sub:`s` inv(t) ∎

The next theorem establishes the *transivity* of containment over Strings. 

**Theorem 1.2.7** ∀ t, u, v ∈ S : (t ⊂:sub:`s` u) ∧ (u ⊂:sub:`s` v) → (t ⊂:sub:`s` v) 

This theorem can be stated in natural language as follows: For any Strings *t*, *u*, and *v* in **S**, if *t* is contained in *u* and *u* is contained in *v*, then *t* is contained in *v*.

Let *t*, *u*, and *v* be arbitrary Strings in **S** such that both of the following expressions are true,

    1. t ⊂:sub:`s` u
    2. u ⊂:sub:`s` v

By Definition 1.1.7 and step 1, there exists a strictly increasing and consecutive function *f*: **N**:sub:`l(t)` → **N**:sub:`l(u)` such that,

    3. ∀ i ∈ N:sub:`l(t)`: t[i] = u[f(i)]

Similarly, by Definition 1.1.7 and step 2, there exists a strictly increasing and consecutive function *g*: **N**:sub:`l(u)` → N:sub:`l(v)` such that:

    4. ∀ j ∈ N:sub:`l(u)`: u[j] = v[g(j)]

Define a new function *h*: **N**:sub:`l(t)` *→* **N**:sub:`l(v)` as the composition of *f* and *g*,

    5. ∀ j ∈ N:sub:`l(t)`: h(i) = g(f(i))

**Increasing** Let 

    6. i, j ∈ N:sub:`l(t)` 
    
Such that *i < j*. Since *f* is strictly increasing, 

    7. f(i) < f(j) 

Since *g* is strictly increasing, 

    8. g(f(i)) < g(f(j))
    
Therefore, 

    9. h(i) < h(j)
    
And *h* is strictly increasing.

**Consecutive** Let 

    10. i ∈ N:sub:`l(t)` 
    
Such that *i < l(t)*. Since *f* is consecutive, 

    11. f(i+1) = f(i) + 1 
    
Since *g* is consecutive, following from step 11,

    12. g(f(i+1)) = g(f(i) + 1) = g(f(i)) + 1
    
Therefore, 

    13. h(i+1) = h(i) + 1, and h is consecutive.

**Containment** Let 

    14. i ∈ N:sub:`l(t)` 
    
Then, by step 3

    15. t[i] = u[f(i)]

Since *f*: **N**:sub:`l(t)` *→* **N**:sub:`l(u)`, it follows that for all 

    16. ∀ i ∈ N:sub:`l(t)`: f(i) ∈ N:sub:`l(u)`

By step 16 and step 4,

    17. u[f(i)] = v[g(f(i))]

By definition of *h*,

    18. v[g(f(i))] = v[h(i)]

Therefore, 

    19. ∀ i ∈ N:sub:`l(t)`: t[i] = v[h(i)]

Since *h* is a strictly increasing and consecutive function from **N**:sub:`l(t)` to **N**:sub:`l(v)`, and *t[i] = v[h(i)]* for all *1≤ i ≤ l(t)*, by Definition 1.1.7,

    20. t ⊂:sub:`s` v.

Since *t*, *u*, and *v* were arbitrary Strings, this can be generalized as,

    21. ∀ t, u, v ∈ S : (t ⊂:sub:`s` u) ∧ (u ⊂:sub:`s` v) → (t ⊂:sub:`s` v) ∎

Phrases
^^^^^^^

While the analyis has not yet introduced the notion of Sentences into the formal system (see Section II), an operation will now be introduced that allows Words to be ordered into Phrases and then concatenated into Strings. This new operation will be important when String Inversion is applied to the sentential level of the formal system, allowing the conditions for a Sentence Inversion to be precisely specified.

The placement of Definition 1.2.5 and Definition 1.2.6 is somewhat arbitary. There are valid arguments to be made for placing these definitions after the concepts of Sentence and Word Index notation have been introduced in Section II. However, since the operation of *Delimitation* and *Limitations* to be expounded immediately are essentially an operation defined on the domain of Strings which yields as a result another String, i.e. Delimitation and Limitation are closed with respect to Strings, the definitions are made here, to highlight the derivative notions (Inversion, Delimitation and Limitations) which can be built on top of the primitive notion of concatenation.

**Definition 1.2.5: Phrase**

Let *n* be a fixed, non-zero natural number, *n ≥ 1*. A Phrase of Word Length *n* from Language **L**, denoted **P**:sub:`n`, is defined as an ordered sequence of *n* (not necessarily distinct) Words,

    P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

where each *α*:sub:`i` *∈* **L**. If *i* is *1 ≤ i ≤ n*, P:sub:`n`(i) denotes the Word *α*:sub:`i` at index *i*, so that **P**:sub:`n` may be rewritten, 

    P:sub:`n` = (P:sub:`n`(1), P:sub:`n`(2), ... , P:sub:`n`(n))

When *n = 0*, **P**:sub:`0` is defined as the empty sequence (). ∎

In order to establish some properties of Phrases, Delimitations and Limitations , a symbol for representing the range of a Phrase **P**:sub:`n` over a Language **L** is now defined.

**Definition 1.2.6: Lexicon**

Let *n* be a fixed natural number. We define a Language's *n*:sup:`th` Lexicon, denoted **X**:sub:`L`(*n*), as the set of all Phrases of length *n* formed from Words in **L**,

    Χ:sub:`L`(n) = { P:sub:`n` | P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`) ∧ ∀ i ∈ N:sub:`n`: α:sub:`i` ∈ L } ∎

Some of the later theorems in this work will require quantifying over Phrases in a Language's *n*:sub:`th` Lexicon, so notation is introduced for Phrase Variables,

    1. Phrase Variables (*p*, *q*, *r*): The lowercase English letters *p*, *q*, *r* are reserved for representing indeterminate Phrases of a Language's *n*:sup:`th` Lexicon.
   
Because Phrases are ordered sequences of Words, the Phrase Variable *p(i)* will denote, exactly like the Definition of a Phrase, the Word at index *i* for *1 ≤ i ≤ n*.

Using these pair of definitions for Phrases and Lexicons and their associated terminology, the operation of *Delimitation* is now defined over Phrases of fixed Word Length *n* in Definition 1.2.7.

**Definition 1.2.7: Delimitation**

Let *p* be a Phrase from a Language **L**'s *n*:sup:`th` Lexicon,

    p = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

The *Delimitation* of *p*, denoted *DΠ*:sub:`i=1`:sup:`n` *p(i)*, is defined recursively as:

    1. Empty Clause: DΠ:sub:`i=1`:sup:`0` p(i) = ε
    2. Basis Clause (n = 1): DΠ:sub:`i=1`:sup:`1` p(i) = α:sub:`1`
    3. Recursive Clause (n > 1): DΠ:sub:`i=1`:sup:`n` p(i) = (DΠ:sub:`i=1`:sup:`n-1` p(i))(σ)(α:sub:`n`) ∎

**Definition 1.2.8: Limitation**

Let *p* be a Phrase from a Language **L**'s *n*:sup:`th` Lexicon,

    p = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

The *Limitation* of *p*, denoted *LΠ*:sub:`i=1`:sup:`n` *p(i)*, is defined recursively as:

    1. Empty Clause: LΠ:sub:`i=1`:sup:`0` p(i) = ε
    2. Basis Clause (n = 1): LΠ:sub:`i=1`:sup:`1` p(i) = α:sub:`1`
    3. Recursive Clause (n > 1): LΠ:sub:`i=1`:sup:`n` p(i) = (LΠ:sub:`i=1`:sup:`n-1` p(i))(α:sub:`n`) ∎

The key difference between Definition 1.2.7 and Definition 1.2.8 is the presence of the Delimiter in the Recursive Clause. In other words, a Delimitation inserts a Delimiter between the Words it is concatenating, while a Limitation is simply a shorthand simply for concatenating a sequence of Words.

Before proving the existence of Delimitations and Limitations, an example of how they are constructed recursively is given below.

**Example**

Let 

    P:sub:`3` = ("mother", "may", "I")

Apply Definition 1.2.7 to construct the Delimitation of **P**:sub:`3`. The Basis Step yields,

    1. n = 1: DΠ:sub:`i=1`:sup:`1` α:sub:`i` = "mother" 

And then the Delimitation can be built up recursively using the Recursive Step repeatedly,

    2.  n = 2: DΠ:sub:`i=1`:sup:`2` α:sub:`i` = (DΠ:sub:`i=1`:sup:`1` α:sub:`i`)(σ)("may")= ("mother")(σ"may") = "mother"σ"may"
    3.  n = 3: DΠ:sub:`i=1`:sup:`3` α:sub:`i` = (DΠ:sub:`i=1`:sup:`2` α:sub:`i`)(σ)("I") = ("mother"σ"may")(σ"I") = "mother"σ"may"σ"I"

So the Delimitation of the Phrase is given by,

    4. Π:sub:`i=1`:sup:`3` α:sub:`i` = "mother may I" 

Similarly, the Limitation can be constructed recursive from the same Basis Step using Definition 1.2.8,

   5. n = 2: LΠ:sub:`i=1`:sup:`2` α:sub:`i` = (LΠ:sub:`i=1`:sup:`1` α:sub:`i`)("may")= ("mother")("may") = "mothermay"
   6. n = 3: LΠ:sub:`i=1`:sup:`3` α:sub:`i` = (LΠ:sub:`i=1`:sup:`2` α:sub:`i`)("I") = ("mothermay")("I") = "mothermayI" ∎

From this example, it should be clear what the Delimitation and Limitation operations represent within the formal system. Delimitation is a method of constructing a Sentence-like (see Section II.III for the formal difference between a Delimitation and Sentence) String from a sequence of words, while a Limitation is shorthand for iterated concatenation over a sequence of Words.

Note the previous example may be misleading in one important respect. A Delimitation is not necessarily "grammatical" or "meaningful". It may be a String of semantic Words without an accompanying interpretation on the Sentence level of the linguistic hierarchy. 

However, as the next theorems shows, the result of a Delimitation or Limitation is unique.

**Theorem 1.2.8** ∀ n ∈ ℕ, ∀ p ∈ Χ:sub:`L(n)` ∃! s ∈ S: s = DΠ:sub:`i=1`:sup:`n` p(i)

This theorem can be stated in natural language as follows: For every natural number n, and for every Phrase **P**:sub:`n` in the *n*:sup:`th` Lexicon of **L**, there exists a unique string *s* in **S** such that *s* is the Delimitation of **P**:sub:`n`.

Let *n* be an arbitrary natural number, and let **P**:sub:`n` be a Phrase of Word Length *n* in Language **L** from the Language's *n*:sup:`th` Lexicon, **X**:sub:`L`*(n)*,

    q. P:sub:`n` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`)

The theorem will be proved using induction.

**Base Case (n = 1)**

By Definition 1.2.7,
    
    1. DΠ:sub:`i=1`:sup:`1` P:sub:`n(i)` = α:sub:`1`

Since *α*:sub:`1` is a word in **L** (by Definition 1.2.6 of Lexicon), it is also a String in S (by Definition 1.2.2). Thus, there exists a String *s = α*:sub:`1` such that 

    3. s = DΠ:sub:`i=1``:sup:`1` P:sub:`n(i)`.

Since the base case of Delimitation is defined as simple equality, the string s must be unique.

**Inductive Hypothesis**

Assume that for some *k ≥ 1*, there exists a unique string *s*:sub:`k` such that 

    4. s:sub:`k` = DΠ:sub:`i=1`:sup:`k` P:sub:`n(i)`

To complete the induction, it must be shown that there exists a unique string *s*:sub:`k+1` such that,
 
    5. s:sub:`k+1` = DΠ:sub:`i=1`:sup:`k+1` P:sub:`n(i)`

By Definition 1.2.7, 

    6. DΠ:sub:`i=1`:sup:`k+1` P:sub:`n(i)` = (DΠ:sub:`i=1`:sup:`k` P:sub:`n(i)`)(σ)(α:sub:`k+1`)

By inductive hypothesis,
    
    7. DΠ:sub:`i=1`:sup:`k` P:sub:`n(i)` = s:sub:`k`
    
Thus, *s*:sub:`k` is unique. Since *α*:sub:`k+1` is a Word in **L** (by the definition of **Χ**:sub:`L`*(n+1)*), it is also a unique String in S.

The concatenation of *s*:sub:`k`, *σ*, and *α*:sub:`k+1` is a unique string (by the Definition 1.1.1 of Concatenation and Definition 1.1.4 of String Equality).

Therefore, *s*:sub:`k+1` = (*s*:sub:`k`)(σ)(*α*:sub:`k+1`) is a unique string.

By induction, for every natural number *n*, and for every phrase **P**:sub:`n` in **Χ**:sub:`L(n)`, there exists a unique string *s* in **S** such that *s = DΠ*:sub:`i=1`:sup:`n` P:sub:`n(i)`. ∎

**Theorem 1.2.9** ∀ n ∈ ℕ, ∀ p ∈ Χ:sub:`L(n)` ∃! s ∈ S: s = LΠ:sub:`i=1`:sup:`n` p(i)

The proof of this theorem is almost exactly identical to Theorem 1.2.8, with the exception there is no Delimiter in step 6. ∎

Section I.III: Word Classes 
---------------------------

It will be necessary to define special classes of Words in a Language to properly describe the Language's palindromic structure. These classes, especially the class of Invertible Words, will be used extensively in the next sections. Reflective Words, however, will play a crucial role in this work's climatic theorem. 

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

The set of Reflective Words **R** is defined as the set of *α* which satisfy the open formula,

    α ∈ R ↔ ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1] ∎

A Word *α* will be referred to as *reflective* if it belongs to the class of Reflective Words. 

The following theorem is an immediate consequence of Definition 1.3.1 and Definition 1.2.4.

**Theorem 1.3.1** ∀ α ∈ L: α ∈ R ↔ α = inv(α)

In natural language, this theorem can be stated as: A Word in a Language is Reflective if and only if it is its own Inverse.

(→)  Assume *α ∈ R*. By Definition 1.3.1, 

    1. ∀ i ∈ N:sub:`l(α)`:  α[i] = α[l(α) - i + 1] 

Let *β = inv(α)*. By the Definition 1.2.4,

    2. l(β) = l(α)
    3. ∀ i ∈ N:sub:`l(α)`: ( β[i] = α[l(α) - i + 1] )

Substituting the property of Reflective Words from step 1 into step 3,

    4.  4. ∀ i ∈ N:sub:`l(α)`: β[i] = α[i]

Since *β[i] = α[i]* for all *i ∈* **N**:sub:`l(α)`, and both strings have the same length, by Definition 1.1.4, it can be concluded that *α = β*. Therefore the desired result is obtained, *α = β = inv(α)*.

(←) Assume *α = inv(α)*.  By Definition 1.2.4 of String Inversion,

    1. l(α) = l(inv(α))
    2. ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1]

But step 2 is exactly the definition of Reflective Words, so by Definition 1.3.1, *α ∈* **R** ∎ 

Invertible Words 
^^^^^^^^^^^^^^^^

As discussed previously, the concept of *invertible* is exemplified in pairs of English words, such as *"parts"* and *"strap"*, or *"repaid"* and *"diaper"*. If a Word can be inverted, this is not simply a syntactic operation, but a semantic one as well. An *Invertible Word* is a Word whose inverse is part of the same Language **L** as the original Word. This notion can now be made more precise with the terminology introduced in prior sections.

**Definition 1.3.2: Invertible Words** 

Let *α* be any Word in a Language **L**. Then the set of Invertible Words **I** is defined as the set of *α* which satisfy the open formula,

    α ∈ I ↔ inv(α) ∈ L ∎

A Word *α* will be referred to as *invertible* if it belongs to the class of Invertible Words.

Definition 1.3.2 is immediately employed to derive the following theorems.

**Theorem 1.3.2** ∀ α ∈ L: α ∈ I ↔ inv(α) ∈ I

(→) Assume *α ∈* **I**. By Definition 1.3.2,

    1. inv(α) ∈ L
    
Consider *inv(α)*. To show that it's invertible, it must be shown,

    2. inv(inv(α)) ∈ L. 

By Theorem 1.2.4,

    3. inv(inv(α)) = α
    
Since it is known *α ∈ L*, it follows,

    4. inv(inv(α)) ∈ L  
    
By the Definition 1.3.2, 

    5. inv(α) ∈ I
    
Therefore, *inv(α)* is also an Invertible Word. 

(←) Assume *inv(α)* is a Word in Language L and *inv(α) ∈* **I**. Then by Definition 1.3.2,

    1. inv(inv(α)) ∈ L

By Theorem 1.2.4,

    2. α ∈ L

To show *α* is invertible, it must be shown *inv(α) ∈* **L**, but this is exactly what has been assumed, so it follows immediately. 

Therefore, putting both directions of the equivalence together and generalizing over all Words in a Language, 

    ∀ α ∈ L: α ∈ I ↔ inv(α) ∈ I ∎ 

**Theorem 1.3.3** R ⊆ I

Assume *α ∈* **R**. By Definition 1.3.2,

    1. ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1]

Let *β = inv(α)*. By Definition 1.2.4,

    2. l(β) = l(α)
    3. ∀ j ∈ N:sub:`l(α)`: β[j] = α[l(α) - j + 1]

Substituting step 1 into step 3,

    4. ∀ i ∈ N:sub:`l(α)`:  β[j] = α[j]

Since both strings have the same length and the same Characters in the same order, by Definition 1.1.4, 

    5. α = β = inv(α)

By assumption, *α* is a Word from Language **L** that belongs to **R**. From step 5, this implies *inv(α)* is also part of the Language **L**. By Definition 1.3.2, this implies,

    6. α ∈ I 

In other words, 

    ∀ α ∈ L : α ∈ R → α ∈ I 

But this is exactly the definition of the subset relation in set theory. Therefore,

    R ⊆ I ∎ 

In the context of (potentially) infinite sets such as **L** and **S**, *"even"* and *"odd"* refer to whether the set can be partitioned into two disjoint subsets of equal cardinality.

    1. Even Cardinality: An infinite set has even cardinality if it can be put into a one-to-one correspondence with itself, with each element paired with a distinct element.
    2. Odd Cardinality: An infinite set has odd cardinality if, after pairing each element with a distinct element, there is one element left over.

The set of non-reflective Invertible Words, **I** - **R** (where "-" represents the operation of set differencing), always has even cardinality because each word can be paired with its distinct inverse. The overall cardinality of **I** then depends on whether the set of Reflective Words, **R**, adds an "odd" element or not. This idea is captured in the next theorem.

**Theorem 1.3.4** If | R | is even, then | I | is even. If | R | is odd, then | I | is odd.

Partition the set of Invertible Words, **I**, into two disjoint subsets,

    1. **R**: The set of Reflective Words.
    2. **I** - **R**: The set of Invertible Words that are not Reflective.

For every word *α* in **I** *-* **R**, its inverse, *inv(α)*, is also in **I** *-* **R**. Furthermore, they form a distinct pair *(α, inv(α))*. This is because *α* is invertible but not reflective, so *α ≠ inv(α)*.

Since the elements of **I** *-* **R** can be grouped into distinct pairs, the cardinality | I - R | must be even.

The total number of Invertible Words is the sum of the number of Reflective Words and the number of Invertible Words that are not Reflective,

    3. | I | = | R | + | I - R |

Let | R | be even. Since | I - R | is always even, and the sum of two even numbers is even, | I | must also be even.

Let | R | be odd. Since | I - R | is always even, and the sum of an odd number and an even number is odd, | I | must also be odd. ∎ 