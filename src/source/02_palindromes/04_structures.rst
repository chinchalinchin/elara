.. _section-iii:

Section III: Structures
=======================

The foundation of the formal system has now been laid. Mathematical machinery capable of describing linguistic hierarchies has been constructed. The purpose of this formal system is to analyze the structures embedded in Palindromes. While the formal system possesses flexibility and applicability (as demonstrated by its ability to generate theorems like :ref:`Theorem 2.3.9 <theorem-2-3-9>` which are empirically verifiable), it does not yet have the necessary tools for describing palindromic structures. 

Inversion, while a key component of the apparatus necessary for understanding the dynamics of Palindromes, is not the only linguistic operation involved in the formation of Palindromes. The pure involutive property of Palindromes (e.g., :math:`\zeta = \text{inv}(\zeta))` only manifests in a rare class of Sentences known as Perfect Palindrome (:ref:`Definition 4.1.2 <definition-4-1-2>`).

However, the vast majority of Palindromes in any language are not pure involutions. Instead, the operation of inversion usually degrades the semantic content of a Sentence by re-ordering the Delimiters, as seen in the following, 

.. math::

    \zeta = \text{"now sir a war is won"}

.. math::

    \text{inv}(\zeta) = \text{"now si raw a ris won"}

In order to properly understand the nature of a Palindrome, the formal system under construction must have a method of quantifying the distribution of Delimiters in a Sentence and making claims about the nature of that Distribution. Furthermore, the system requires a method of removing the *"impurities"* in semantic content that are introduced through inversion.

This section of the work is dedicated to introducing several novel concepts for analyzing Delimiters distributions: the operation of *σ-reduction* and the *Delimiter Count* function.

Section III.I: σ-Reductions 
---------------------------

The mathematical definition of Palindromes (:ref:`Definition 4.1.1 <definition-4-1-1>` in the next section) will revolve around a novel linguistic operation, termed a *σ*-reduction. This operation will allow the semantic content of a Palindrome to be projected onto an Alphabet that preserves the order of its Characters under String Inversion, allowing for a precise specification of palindromic inversion in an Alphabet where symmetry is preserved.

Definitions
^^^^^^^^^^^

Before defining a *σ*-reduction, the preliminary concept of a *σ-reduced Alphabet* must be introduced. The following definition serves as the basis for constructing the operation of *σ*-reduction.

As has been seen with examples of Imperfect Palindromes like *"borrow or rob"*, a palindromic structure can have its Delimiter Character scrambled in the inversion of its form, i.e. *"bor ro worrob"*, making it lose semantic coherence. Imperfect Palindromes must be rearranged Delimter-wise to retrieve the original form of the Sentence. However, String Inversion preserves the relative order of the non-Delimiter Characters in a palindromic String, so the process of reconstitution is only a matter of resorting the Delimiter characters. This invariance of the Character order, while the Word order is scrambled by Delimiters, suggests palindromes might be more easily defined without the obstacle of the Delimiter.

**Definition 3.1.1: σ-Reduced Alphabet**

A *σ-reduced Alphabet* is an Alphabet Σ that has had its Delimiter character removed, so that it only consists of non-Delimiter characters. A *σ*-reduced Alphabet is denoted Σ:sub:`σ`. Formally,

.. math::

    \Sigma_\sigma = \Sigma - \{ \sigma \} 
    
∎

In order to define palindromes in all of their varieties, perfect or imperfect, the semantic incoherence that is introduced by the inversion of Imperfect Palindromes must be removed. This is accomplished through the introduction of the operation of *σ-reduction*.

**Definition 3.1.2: σ-Reduction**

Let *t* be a String with length *l(t)* and Character-level representation 

.. math::

    1. T = \{ (1,\mathfrak{a}_1) , (2, \mathfrak{a}_2) , ... , (l(t), \mathfrak{a}_{l(t)}) \} 
    
.. math::

    2. \mathfrak{a}_i \in \Sigma.

The *σ*-reduction of *t*, denoted by the lowercase Greek final Sigma, *ς(t)*, maps the String *t* to a new String *u* in the *σ*-reduced alphabet **Σ**:sub:`σ` by removing all occurrences of the Delimiter Character. Formally, *ς(t)* is defined and constructed using the *Reduction Algorithm*,

**Reduction Algorithm**

**Algorithm 3: Reduction Algorithm**

The Reduction Algorithm takes in a String *t* as input. It initializes the values of several local variables and then iterates over the Character-level set representation of the String *t* until the Characters have been exhausted. It then returns the *σ-reduced* String *s* that corresponds to the String *t*. The exact details are given below.

.. topic:: Algorithm Reduce(t: String)

    # Input: A String t
    # Output: A String s that represents the σ-reduction of t

    # Initialization
    ## Character-level representation of s
    1. s ← Empty(s)
    ## Index to iterate over input String
    2. i ← 1
    ## Empty string to store σ-reduced String
    3. t ← ε            

    # Iteration
    4. While i ≤ l(s):
        
        a. If s[i] ≠ σ:
            
            i. t ← (t)(s[i])
        
        c. i ← i + 1

    # Finalization
    5. If l(t) > 0:
        
        a. Apply Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>` to t
    
    6. Return t ∎

Note the String *s* which is initialized to hold the *σ*-reduced String is set equal to the value of the Empty Character. The conditional application of the Basis Clause of Concatenation in step 1 of the Finalization Block ensures this Character is removed from the output of the Reduction Algorithm, if the input string contained at least one non-Empty Character. Otherwise, the Reduction Algorithm returns an Empty Character. From this, it is clear if a String only contains Delimiters,

.. math::

    \varepsilon = \varsigma(\sigma) = \varsigma(\sigma\sigma) = \varsigma(\sigma\sigma\sigma) = ... 

From which, it follows, by :ref:`Definition 1.1.3 <definition-1-1-3>` of String Length, the String Length of a reduced Delimiter is simply zero,

.. math::

    l(\varsigma(\sigma)) = 0

Moreover, since by :ref:`Discovery Axiom W.1 <axiom-w1>`, Words do not contain Delimiters, for any Word *α* in Language **L**,

.. math::

    \varsigma(\alpha) = \alpha

Again, from :ref:`Definition 1.1.3 <definition-1-1-3>`, the String Length of a reduced Word is simply the String Length of the Word,

.. math::

    l(\varsigma(\alpha)) = l(\alpha)

A subtlety of the Reduction Algorithm should be noted. While :ref:`\varsigma(\sigma) = \varepsilon` and `\varsigma(\alpha) = \alpha`, it does not follow the *σ*-reduction of a Word concatenated with the Delimiter is the concatenation of that Word with the Empty Character. In other words, the following holds,

.. math::

    \varsigma(\alpha\sigma) ≠ \alpha\varepsilon

Except insofar that the Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>` defines the concatenation of *αε* to equal *α*.

This is because of the condition *(j > 1)* in the Finalization Block of the Reduction ensures Empty Characters are stripped from *t* when the input String contains atleast one non-Empty Character that has been concatenated into the *σ*-reduction String. 

The more complicated properties of *σ*-reductions are proved in the theorems that follow. Before moving onto the proofs, the following example shows how to apply the Reduction Algorithm to construct the *σ*-reduction of a String.

**Example**

Let *s = "a b c"* be a String from the Alphabet 

    \Sigma = \{ \text{""}, \text{" "} , \text{"a"}, \text{"b"}, \text{"c"} \} 
    
Note in this example :math:`\sigma = \text{" "}` and :math:`l(s) = 5`. The value of the variables in the Reduction Algorithm after each iteration are given below,

.. math::

    1. i = 2, t = \varepsilon\text{"a"}

.. math::

    2. i = 3, t = \varepsilon\text{"a"}

.. math::

    3. i = 4, t = \varepsilon\text{"ab"}
    
.. math::

    4. i = 5, t = \varepsilon\text{"ab"}
    
.. math::

    5. i = 5, t = \text{"abc"}
        
The result of the σ-reduction of *s* is thus given by,

.. math::

    \varsigma(s) = \text{"abc"} 
    
∎

A *σ*-reduction can be thought of as a linguistic operation analogous to vector projection. While not a strict mathematical equivalence, this conception of *σ*-reduction captures the idea of transforming a String from its original form (with Delimiters) onto a reduced space (without Delimiters), similar to how a vector can be projected onto a subspace.

The *σ*-reduced Alphabet (**Σ**:sub:`σ`) can be seen as a subspace within this higher-dimensional space, consisting of only the non-Delimiter dimensions. The sigma reduction function (*ς(s)*) acts as a projection operator, mapping the String onto this subspace by eliminating the components corresponding to the Delimiter character (*σ*).

Note that a *σ*-reduction is not a one-to-one operation. It is possible for the *σ*-reduction of a palindrome to map onto a totally different sentence, not necessarily a palindrome.

As an example, consider the (partial, ignoring punctuality) Palindromes :math:`\rune{f} = \text{"madam im adam"}` and :math:`\rune{u} = \text{"mad am i madam"}`. The *σ*-reduction of both of these Sentences would map to the *σ-reduced* value of *madamimadam".

Both the Palindrome and the alternative Sentence (which also happens to be a Palindrome) have the same *σ*-reduction, despite having different meanings and grammatical structures. This highlights the ambiguity that can arise from removing spaces, as the original Word boundaries and Sentence structure are lost.

.. _reduction-theorems:

Theorems 
^^^^^^^^

The following theorems establish the basic properties of *σ*-reductions. 

.. _theorem-3-1-1:

**Theorem 3.1.1** :math:`\forall \zeta \in C_L: \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta))`

Let *ζ* be an arbitrary sentence in C:sub:`L`. Let *s* be the *σ*-reduction of *ζ*,

.. math::

    1. s = \varsigma(\zeta)

Let *t* be the Inverse of *s*,

.. math::

    2. t = \text{inv}(s).

Let *u* be the Inverse of *ζ*,

.. math::

    3. u = \text{inv}(ζ). 
    
Let *v* be the *σ*-reduction of *u*,

.. math::

    4. v = \varsigma(u) = \varsigma(\text{inv}(ζ)) 

Since *s* contains only the non-Delimiter characters of *ζ* in their original order, and *t* is the reversed sequence of Characters in *s*, *t* contains only the non-Delimiter characters of *ζ* in reversed order.

Similarly, since *u* is the reverse sequence of Characters in *ζ*, and *v* is obtained by removing Delimiters from *u*, *v* also contains only the non-Delimiter characters of *ζ* in the reversed order.

Therefore, by :ref:`Definition 1.1.4 <definition-1-1-4>`, *t* and *v* must be the same String, as they both contain the same Characters in the same order. Since :math:`t = v`, 

.. math::

    5. \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta))

Since ζ was an arbitrary Sentence, this can be generalized over the Corpus

.. math::

    6. \forall \zeta \in C_L: \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta)) 

∎

:ref:`Theorem 3.1.1 <theorem-3-1-1>` is essential because it allows free movement between the Inverse of a *σ*-reduction and the *σ*-reduction of an Inverse. In other words, :ref:`Theorem 3.1.1 <theorem-3-1-1>` establishes the commutativity of *σ*-reduction over inversion and visa versa. 

As the theorems in this section will make clear, there exists a unique type of algebraic structure that links the operations of *σ*-reduction, inversion and concatenation. The properties of this algebraic structure will be necessary for establishing many of the results regarding palindromes.

The next theorem demonstrates how *σ*-reduction interacts with concatenation.

.. _theorem-3-1-2:

**Theorem 3.1.2** :math:`\forall \zeta, \xi \in C_L: \varsigma(\zeta\xi) = (\varsigma(\zeta)\varsigma(\xi))`

Let *ζ* and *ξ* be arbitrary sentences in **C**:sub:`L`. Let **Ζ** and **Ξ** be the character-level representations of *ζ* and *ξ*, respectively,

.. math::

    1. \Zeta = (\iota_1, \iota_2, ..., \iota_{l(\zeta)})

.. math::

    2. \Xi = (\nu_1, \nu_2, ..., \nu_{l(\xi)})

Let *ζξ* be the concatenation of *ζ* and *ξ*. The character-level representation of *ζξ* is given by,

.. math::

    3. \Zeta\Xi = (\iota_1, \iota_2, ..., \iota_{l(\zeta)}, \nu_1, \nu_2, ..., \nu_{l(\xi)})

Let *s* be the σ-reduction of *ζξ*. Let *t* be the *σ*-reduction of *ζ*. Let *u* be the *σ*-reduction of *ζξ*,

.. math::

    4. s = \varsigma(\zeta\xi)
    
.. math::

    5. t = \varsigma(\zeta)
    
.. math::

    6. u = \varsigma(\xi)

Let *v* be the concatenation of the Strings *t* and *u*,

.. math::

    7. v = tu = (\varsigma(\zeta))(\varsigma(\xi))

Since *σ*-reduction only removes Delimiters and doesn't change the order of non-Delimiter Characters, the non-Delimiter characters in *s* (the *σ*-reduction of *ζξ*) are the same as the non-Delimiter Characters in *ζ* followed by the non-Delimiter Characters in ξ.

The non-Delimiter characters in *v*, the concatenation of *ς(ζ)* and *ς(ξ)*, are also the non-Delimiter characters in *ζ* followed by the non-delimiter characters in *ξ*.

Therefore, by :ref:`Definition 1.1.4 <definition-1-1-4>`, *s* and *v* must be the same String, as they both contain the same Characters in the same order (the non-Delimiter Characters of *ζ* followed by the non-Delimiter characters of *ξ*). Since :math:`s = v`, 

.. math::

    8. \varsigma(\zeta\xi) = (\varsigma(\zeta))(\varsigma(\xi))

Since ζ and ξ were arbitrary Sentence, this can be generalized over the Corpus,

.. math::

    9. \forall \zeta, \xi \in C_L: \varsigma(\zeta\xi) = (\varsigma(\zeta))(\varsigma(\xi)) 

∎

:ref:`Theorem 3.1.2 <theorem-3-1-2>` further demonstrates the *algebraic* nature of *σ*-reduction and the other String operations. It shows that *σ*-reduction *distributes* over concatenation, just as inversion "distributes" (in a reversed way) over concatenation (:ref:`Theorem 1.2.5 <theorem-1-2-5>`). These properties suggest that *σ*-reduction, inversion and concatenation are not just arbitrary operations but instead are deeply connected to the underlying structure of Strings and Sentences.

As another example of this *"linguistic algebraic structure"*, the following theorem might be termed the *"Idempotency of σ-reduction"* or the *"σ-reduction Idempotence Property"*.

.. _theorem-3-1-3:

**Theorem 3.1.3** :math:`\forall \zeta \in C_L: \varsigma(\varsigma(\zeta)) = \varsigma(\zeta)`

Let *ζ* be an arbitrary Sentence in **C**:sub:`L`. Let s be the *σ*-reduction of *ζ*,

.. math::

    1. s = \varsigma(\zeta)

Let *t* be the *σ*-reduction of *s*,

.. math::

    2. t = \varsigma(s) = \varsigma(\varsigma(\zeta))

Since *s* is the result of applying a *σ*-reduction to *ζ*, it contains no Delimiter Characters (*σ*).

When *s* is *σ*-reduced (to get *t*), the Reduction Algorithm in :ref:`Definition 3.1.2 <definition-3-1-2>` iterates through the Characters of *s*. Since s has no Delimiters, the condition if :math:`s[i] \neq \sigma` in the algorithm will always be true, and every character of *s* will be concatenated to the initially empty string *t*. Therefore, by :ref:`Definition 1.1.4 <definition-1-1-4>`, *t* will be identical to *s*, as it contains the same Characters in the same order. Thus,

.. math::

    3. \varsigma(\varsigma(\zeta)) = \varsigma(\zeta)

Since ζ was an arbitrary Sentence, this can be generalized over the Corpus,

.. math::

    4. \forall \zeta \in C_L: \varsigma(\varsigma(zeta)) = \varsigma(\zeta) 

∎

.. _theorem-3-1-4:

**Theorem 3.1.4** :math:`\forall \zeta \in C_L: \Lambda(\varsigma(\zeta)) \leq 1`

Let *ζ* be an arbitrary Sentence in **C**:sub:`L`. By the :ref:`Duality Axiom S.1 <axiom-s1>`, every Sentence in **C**:sub:`L` must contain at least one word from **L**. 

.. math::

    1. \exists \alpha \in L: \alpha subset_s \zeta

By :ref:`Definition 3.1.2 <definition-3-1-2>`, *ς(ζ)* removes all Delimiters from *ζ*. Therefore, *ς(ζ)* consists of the Characters of the words in *ζ* concatenated together without any delimiters.

By the :ref:`Discovery Axiom W.1 <axiom-w1>`, Words in **L** cannot contain Delimiters.

By :ref:`Definition 2.1.4 <definition-2-1-4>`, the Word Length *Λ(s)* of a String *s* counts the number of Words in *s*, where Words are separated by Delimiters.

If *ζ* contains only one Word, then *ς(ζ)* will be that Word,

.. math::

    2. \Lambda(\varsigma(\zeta)) = 1

If *ζ* contains multiple Words, then *ς(ζ)* will be a concatenation of those words without Delimiters. This concatenated String may or may not be a valid Word in **L**.

If the concatenated String is a valid Word in **L**, then,

.. math::

    3. \Lambda(\varsigma(\zeta)) = 1

If the concatenated String is not a valid Word in **L**, then,

.. math::

    4. \Lambda(\varsigma(\zeta)) = 0

Therefore, in all possible cases,

.. math::

    5. \Lambda(\varsigma(\zeta)) \leq 1

Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,

.. math::

    6. \forall \zeta \in C_L: \Lambda(\varsigma(\zeta)) \leq 1 

∎

.. _theorem-3-1-5:

**Theorem 3.1.5** :math:`\forall u, t \in S: u \subset_s t \leftrightarrow \varsigma(u) \subset_s \varsigma(t)`

This theorem can be stated in natural language as follows: For any two Strings *u* and *t*, *u* is contained in *t* if and only if the *σ*-reduction of *u* is contained in the *σ*-reduction of *t*.

Let *u* and *t* be arbitrary strings in **S**.

(→) Assume 

.. math::

    1. u \subset_s t

By Definition 1.1.7, there exists a strictly increasing and consecutive function :math:`f: N_{l(u)} \to N_{l(t)}` such that,

.. math::

    2. \forall i \in N_{l(u)}: u[i] = t[f(i)]

Let 

.. math::

    3. s = \varsigma(u) 
    
.. math::

    4. v = \varsigma(t).

By the :ref:`Definition 3.1.2 <definition-3-1-2>` of *σ*-reduction, *s* is obtained by removing all Delimiters from *u*, and *v* is obtained by removing all Delimiters from *t*.

Since *u* is contained in *t*, the non-Delimiter Characters of *u* appear in *t* in the same order. The function *f* maps the indices of these Characters.

Define a function :math:`g: N_{l(s)} \to N_{l(v)}` that maps the indices of *s* to the indices of *v*. In other words, if *i* is an index in *s*, then *g(i)* is the index in *v* that corresponds to the same non-Delimiter character.

Since *f* is strictly increasing and consecutive, and *σ*-reduction only removes Delimiters, *g* will also be strictly increasing and consecutive. (*g* essentially compresses the mapping of *f* by skipping over the Delimiter indices and offseting).

For any index *i* in *s*, 

.. math::

    5. s[i] = u[j] 
    
for some *j*. Moreover, 

.. math::

    6. u[j] = t[f(j)]. 
    
Since *s* and *v* are *σ*-reduced, *s[i]* and *v[g(i)]* correspond to the same non-Delimiter Character, and g(i) is constructed such that 

.. math::

    7. v[g(i)] = t[f(j)]. 
    
Therefore, 

.. math::

    8. s[i] = v[g(i)].

Since *g* is a strictly increasing and consecutive function and :math:`s[i] = v[g(i)]`, by :ref:`Definition 1.1.7 <definition-1-1-7>`, 

.. math::

    9. s \subset_s v
    
From which it follows,

.. math::

    10. \varsigma(u) \subset_s \varsigma(t).

(←) Assume 

.. math::

    1. \varsigma(u) \subset_s \varsigma(t).

By :ref:`Definition 1.1.7 <definition-1-1-7>`, there exists a strictly increasing and consecutive function :math:`g: N_{l(\varsigma(u))} \to N_{l(\varsigma(t))}` such that:

.. math::

    2. \forall i \in N_{l(\varsigma(u))}: \varsigma(u)[i] = \varsigma(t)[g(i)]

Define a function :math:`f: N_{l(u)} \to N_{l(t)}` that maps the indices of *u* to the indices of *t* by essentially "re-inserting" the delimiters. For each non-Delimiter character in *u* (and corresponding index in *ς(u)*), *f* will map to the corresponding index in *t*. For Delimiter characters in *u*, *f* will map to an index in *t* that preserves the order and consecutiveness.

Since *g* is strictly increasing and consecutive, and the Delimiters are only removed, not reordered, the function *f* will also be strictly increasing and consecutive.

For each index *i* in *u*, *u[i]* will either be a non-Delimiter or a Delimiter Character.

If *u[i]* is a non-Delimiter character, it corresponds to a Character in *ς(u)*, and by the properties of *g* and *f*, the following holds for some *j*,

.. math::

    3. u[i] = \varsigma(u)[j] = \varsigma(t)[g(j)] = t[f(i)] 

If *u[i]* is a Delimiter, then by the construction of *f*, it will be mapped to a corresponding Delimiter in *t*, so 

.. math::

    4. u[i] = t[f(i)]

Since *f* is a strictly increasing and consecutive function and :math:`u[i] = t[f(i)]` for all :math:`i \in N_{l(u)}`, by :ref:`Definition 1.1.7 <definition-1-1-7>`,

.. math::

    5. u \subset_s t

Since both directions of the implication hold, it can be concluded,

.. math::

    6. \forall u, t \in S : u \subset_S t \leftrightarrow varsigma(u) \subset_s \varsigma(t) 

∎

During a *σ*-reduction, :ref:`Theorem 3.1.4 <theorem-3-1-4>` demonstrates information is lost with respect to the following semantic categories,

  - Word Boundaries: The spaces between words, which are crucial for parsing and understanding the sentence, are eliminated.
  - Sentence Structure: The grammatical structure of the sentence, the relationships between words and phrases, becomes ambiguous.
  - Prosody and Rhythm: The pauses and intonation that contribute to the meaning and expression of the sentence are lost.

However, some semantic information is preserved. The individual words themselves, or at least their character sequences, remain present in the *σ-reduced* string. The next theorem proves semantic content is retained during the *σ*-reduction of a Sentence.

.. _theorem-3-1-6:

**Theorem 3.1.6** :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\Zeta)}: \zeta\{i\} \subset_s \varsigma(\zeta)`

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus **C**:sub:`L`, and for every Word *ζ{i}* in the Word-level representation of *ζ*, *ζ{i}* is contained in *ς(ζ)*.

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. By :ref:`Theorem 2.2.4 <theorem-2-2-4>`, it is known at least one Word must exist in *ζ*. Let *ζ{i}* be one of the Words in the sequence of Words that form *ζ*. 

This means that *ζ* can be written as either, in the case of :math:`\Lambda(\zeta) > 1`, 

.. math::

    1. \text{Case} (\Lambda(\zeta) > 1): \zeta = (s_1)(\sigma)(\zeta\{i\})(\sigma)(s_2)
    
where *s*:sub:`1` and *s*:sub:`2` are (possibly Empty) Strings. 

In the case that Λ(ζ) = 1, then, this means *ζ* can be written simply as, 

.. math::

    2. \text{Case} (\Lambda(\zeta) = 1): \zeta = \zeta\{1\}

By the :ref:`Definition 3.1.2 <definition-3-1-2>`, *ς(ζ)* is obtained by removing all Delimiters from *ζ*. Furthermore, by :ref:`Theorem 3.1.2 <theorem-3-1-2>`, *σ*-reduction distributes over concatenation. Thus,

.. math::

    3. \text{Case} (\Lambda(\zeta) > 1): \varsigma(\zeta) = (\varsigma(s_1))(\varsigma(\zeta\{i\}))(\varsigma(s_2))

.. math::

    4. \text{Case} (\Lambda(\zeta) = 1): \varsigma(\zeta\{1\})

By the :ref:`Discovery Axiom W.1 <axiom-w1>`, Words in **L** do not contain Delimiters.

.. math::

    5. \text{Case} (\Lambda(\zeta) > 1): \varsigma(\zeta) = (\varsigma(s_1))(\zeta\{i\})(\varsigma(s_2))
    
.. math::

    6. \text{Case} (\Lambda(\zeta) = 1): \varsigma(\zeta\{1\}) = \zeta\{1\}

Therefore, by :ref:`Definition 1.1.7 <definition-1-1-7>` of Containment,

.. math::

    7. \text{Case} (\Lambda(\zeta) > 1): \zeta\{i\} \subset_s \varsigma(\zeta)
    
.. math::

    8. \text{Case} (\Lambda(\zeta) = 1): \zeta\{1\} \subset_s \varsigma(\zeta) 

In both cases, there is a Word in *ζ* that is contained in the *σ*-reduction of *ζ*. Since *ζ* was arbitrary, this can generalize over the Corpus,

.. math::

    9. \forall ζ \in C_L: \forall i \in N_{\Lambda(\zeta)}`: \zeta\{i\} \subset_s \varsigma(\zeta) 

∎

This next theorem shows how *σ*-reduction behaves over the class of Invertible Sentences, an extremely important class for understanding the mechanics of Palindromes.

.. _theorem-3-1-7:

**Theorem 3.1.7** ∀ ζ ∈ K: [ ς(ζ) = inv(inv(ς(ζ))) ]

In natural language, this theorem can be stated in natural language as follows: If a Sentence in a Corpus is Invertible, then its invertibility is invariant under *σ*-reduction.

Assume 

.. math::

    1. ζ \in K

In other words, assume that *ζ* is an Invertible Sentence. By :ref:`Theorem 2.3.11 <definition-2-3-11>`, since *ζ* is invertible, all its Words are also Invertible,
 
 .. math::

    1. \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I

The σ-reduction of *ζ*, *ς(ζ)*, is obtained by removing all Delimiters from ζ. Since no Word contains Delimiters (by :ref:`Discovery Axiom W.1 <axiom-w1>`), the *σ*-reduction concatenates the Words of *ζ*,

.. math::

    2. \varsigma(\zeta)= (\zeta\{1\})(\zeta\{2\})...(\zeta\{\Lambda(\zeta)\})

Applying :ref:`Theorem 1.2.5 <theorem-1-2-5>` repeatedly,

.. math::

    3. \text{inv}(\varsigma(\zeta)) = \text{inv}((\zeta\{1\})(\zeta\{2\})...(\zeta{\Lambda(\zeta)\}))

To get,

.. math::

    5.  \text{inv}(\varsigma(\zeta))  = (\text{inv}(\zeta\{\Lambda(ζ)\})) ... (\text{inv}(\zeta\{2\}))(\text{inv}((\ζ\{1\})))

Applying a second Inversion,

.. math::

    6. \text{inv}(\text{inv}(\varsigma(\zeta))) = \text{inv}((\text{inv}(\zeta\{\Lambda(\zeta)\})) ... (\text{inv}(\zeta\{2\}))(\text{inv}((\zeta\{1\}))))

Applying :ref:`Theorem 1.2.5 <theorem-1-2-5>` again,

    7. \text{inv}(\text{inv}(\varsigma(\zeta))) = (\text{inv}(\text{inv}((\zeta\{1\})))) (\text{inv}(\text{inv}((\zeta\{2\}))))...(\text{inv}(\text{inv}((\zeta\{\Lambda(\zeta)\}))))

Finally, applying :ref:`Theorem 1.2.4 <theorem-1-2-4>` (:math:`\text{inv}(\text{inv}(s)) = s`)

.. math::

    8. \text{inv}(\text{inv}(\varsigma(\zeta))) = (\zeta\{1\})(\zeta\{2\})...(\zeta\{\Lambda(\zeta)\})

Therefore, combining step 3 and step 8

.. math::
    
    9. \varsigma(\zeta) = \text{inv}(\text{inv}(\varsigma(\zeta)))

Since *ζ* was an arbitrary Sentence in **K**, this can be generalized over Invertible Sentences,

    10. \forall \zeta \in K: \varsigma(\zeta) = \text{inv}(\text{inv}(\varsigma(\zeta)))

∎

The contrapositive of this theorem, much like the contrapositive of :ref:`Theorem 3.1.7 <theorem-3-1-7>`, provides a schema for searching the *σ-reduced* space for Invertible Sentences. The domain of this space reduces the complexity of searching for palindromic strings. Potential palindromic candidates can be projected into the *σ-reduced* spaced, and then filtered by those whose *σ*-reduction whose Inverse does not equal itself. 

The final theorems in this section, :ref:`Theorems 3.1.8 <theorem-3-1-8>` - :ref:`3.1.9 <theorem-3-1-9>`, provide a method for constructing the *σ*-reduction of a Sentence through iterated concatenation. These theorems leverage the operations of Delimitation and Limitation introduced in :ref:`Definitions 1.2.7 <definition-1-2-7>` - :ref:`1.2.8 <definition-1-2-8>`.

.. _theorem-3-1-8:

**Theorem 3.1.8** :math:`\forall \zeta \in C_L: \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`

This theorem can be stated in natural language as follows: The *σ*-reduction of a Sentence is the Limitation of its Words.

Assume,

.. math::

    1. ζ \in C_L

By :ref:`Definition 2.1.3 <definition-2-1-3>`, 

.. math::

    2. W_{\zeta} = (\alpha_1, \alpha_2, ..., \alpha_{\Lambda(\zeta)})

Where,

.. math::

    3. \forall i \in N_{\Lambda(\zeta)}: \alpha_i \in L

By :ref:`Theorem 2.3.4 <theorem-2-3-4>`, *ζ* can be expressed as the Delimitation of its Words:

.. math::

    4. \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\} = (\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{\Lambda(\zeta)\})

By :ref:`Definition 3.1.2 <definition-3-1-2>`, *ς(ζ)* removes all Delimiters from *ζ*. Applying *σ*-reduction to the expression step 4,

.. math::

    5. \varsigma(\zeta) = \varsigma((\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{\Lambda(\zeta)\}))

By repeated application of :ref:`Theorem 3.1.2 <theorem-3-13>`, i.e. by distributing the *σ*-reduction over concatenation,

.. math::

    6. \varsigma(\zeta) = (\varsigma(\zeta\{1\}))(\varsigma(\sigma))(\varsigma(\zeta\{2\}))(\varsigma(\sigma)) ... (\varsigma(\sigma))(\varsigma(\zeta\{\Lambda(\zeta)\}))

Since 

.. math::

    7. \varsigma(\sigma) = \varepsilon

This can be rewritten with the Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>`,

.. math::

    8. \varsigma(\zeta) = (\varsigma(\zeta\{1\}))(\varsigma(\zeta\{2\}))...(\varsigma(\zeta\{\Lambda(\zeta)\}))

By :ref:`Definition 3.1.2 <definition-3-1-2>` and the :ref:`Discovery Axiom W.1 <axiom-w1>`,

.. math::

    9. \forall i \in N_{\Lambda(\zeta)}: \varsigma(\zeta\{i\}) = \zeta\{i\}

Therefore,
   
.. math::

    10. \varsigma(\zeta) = (\zeta\{1\})(\zeta\{2\})...(\zeta\{\Lambda(\zeta)\})

By :ref:`Definition 1.2.8 <definition-1-2-8>`, the right-hand side is the Limitation of the words in **W**:sub:`ζ`,

.. math::

    11. \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}

Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,

.. math::

    12.  \forall \zeta \in C_L: \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\} 

∎

:ref:`Theorem 3.1.8 <theorem-3-1-8>` establishes an important formula for the construction of *σ*-reductions. The Reduction Algorithm targets Strings as input, i.e. it processes sequential Characters in a String. If an ordered sequence of Words is already at hand, without :ref:`Theorem 3.1.8 <theorem-3-1-8>`, it would be required to reconstruct the String which corresponds to the sequence and process it through the Reduction Algorithm. Rather than applying the Reduction Algorithm everytime a *σ*-reduction is required, :ref:`Theorem 3.1.8 <theorem-3-1-8>` provides a schema for the construction of *σ*-reductions through the process of Limitation.

Compare :ref:`Theorem 3.1.8 <theorem-3-1-8>` to :ref:`Theorem 2.2.5 <theorem-2-2-5>`, reprinted below for reference,

.. math::

    \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}

In other words, taking the *σ*-reduction of a Sentence converts the Delimitation of its Words into a Limitation. This follows directly from :ref:`Definitions 1.2.7 <definition-1-2-7>` and :ref:`1.2.8 <definition-1-2-8>` of Limitation and Delimitation. The next theorem proves this relationship for the more general case of *any* ordered sequence of Words, not necessarily a semantically coherent and admissible Sentence.

.. _theorem-3-1-9:

**Theorem 3.1.9**  :math:`\forall n \in \mathbb{N}: \forall p \in X_L(n): \varsigma(D\Pi_{i=1}^{n} p(i)) = L\Pi_{i=1}^{n} p(i)`

This theorem can be stated in natural language as follows: the *σ*-reduction of the Delimitation of a Phrase is equal to the Limitation of the same Phrase.

Let *n* be an arbitrary natural number, and let *p* be an arbitrary Phrase from a Language's *n*:sup:`th` Lexicon, 

.. math::

    1. p \in Χ_L(n)
    
.. math::

    2. p = (\alpha_1, \alpha_2, ..., \alpha_n).

By :ref:`Definition 1.2.7 <definition-1-2-7>`, 

.. math::

    3. D\Pi_{i=1}^{n} p(i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_n)

Applying :ref:`Definition 3.1.2 <definition-3-1-2>` of *σ*-reduction to the Delimitation and applying the Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>`,

.. math::

    4. \varsigma(D\Pi_{i=1}^{n} p(i)) = (\alpha_1)(\alpha_2) ... (\alpha_n)

By :ref:`Definition 1.2.8 <definition-1-2-8>`,

.. math::

    5. L\Pi_{i=1}^{n} p(i) = (\alpha_1)(\alpha_2) ... (\alpha_n)

By repeated application of :ref:`Theorem 1.1.1 <theorem-1-1-1>` to step 4,

.. math::

    6. l(ς(D\Pi_{i=1}^{n} p(i))) = \sum_{i=1}^{n} l(\alpha_i)

By repeated application of :ref:`Theorem 1.1.1 <theorem-1-1-1>` to step 5,

.. math::

    7. l((\alpha_1)(\alpha_2)... (\alpha_n)) = \sum_{i=1}^{n} l(\alpha_i)

Comparing step 6 to step 7 and noting the *α*:sub:`i` is in the same position the same for all :math:`1 \leq i \leq n`, it follows by :ref:`Definition 1.1.4 <definition-1-1-4>` of String Equality, 

.. math::

    8. \varsigma(D\Pi_{i=1}^{n} p(i)) = L\Pi_{i=1}^{n} p(i)

Since n and p were arbitrary, this can be generalized over the Lexicon,

.. math::

    9. \forall n \in \mathbb{N}: \forall p \in Χ_L(n): \varsigma(D\Pi_{i=1}^{n} p(i)) = L\Pi_{i=1}^{n} p(i) 

∎

The relationship between *σ*-reductions, Limitations and Delimitations provides an easy method for establishing the relationship between the String Length of a Sentence and the String Length of its σ-reduced form. 

.. _theorem-3-1-10:

**Theorem 3.1.10** :math:`\forall \zeta \in C_L: l(\zeta) \geq l(\varsigma(\zeta))`

Let ζ be an arbitrary Sentence in the Corpus. By :ref:`Theorem 3.1.8 <theorem-3-1-8>`,

.. math::

    1. \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}

By :ref:`Theorem 2.2.5 <theorem-2-2-5>`,

.. math::

    2. \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}

Since the only different between :ref:`Definition 1.2.7 <definition-1-2-7>` and :ref:`1.2.8 <definition-1-2-8>` is that Delimitations insert a Delimiter while Limitations simply concatenate, it must follow,

.. math::

    3. l(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) \geq L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}

From this, step 1 and step 2, it follows, 

.. math::

    4. l(\zeta) \geq l(\varsigma(\zeta))

Since *ζ* was arbitary, this can be generalized over the Corpus,

.. math::

    5. \forall \zeta \in C_L: l(\zeta) \geq l(\varsigma(\zeta)) 

∎

.. _section-iii-ii:

Section III.II: Delimiter Count Function 
----------------------------------------

Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a Palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a Palindrome is distributed through its syntactical layers. The concepts of *Perfect* and *Imperfect* Palindromes are be defined more rigorously in Section III, but as an intuitive introduction to the ability of a Palindrome to encode meaning on multiple syntactic levels and as a justification for the introduction of the Delimiter Count Function, consider the following two examples,

    1. dennis sinned
    2. if i had a hifi

The first palindrome "*dennis sinned*" is what will be termed a Perfect Palindrome in :ref:`Definition 4.1.2 <definition-4-1-2>`, because its inverse does not require a rearrangement of its constituent Characters to preserve its semantic content. However, the second Palindrome *"if i had a hifi"* is what is termed an Imperfect Palindrome in :ref:`Definition 4.1.3 <definition 4.1.3>`. To see the motivation behind this categorization, note the strict inversion of "If I had a hifi" would be (ignoring capitalization for now),

    ifih a dah i fi

The order of the Characters in the Inverse of an Imperfect Palindrome is preserved, but in order to reconstitute its uninverted form, the Delimter Characters must be re-sorted. It appears, then, that Delimiters play a central role in organizing the palindromic structure. 

The study of Delimiter Characters in a Sentence bears study beyond its application to palindromic structures, though. The following section of the Appendix introduces this function for quantifying the number of Delimiters in a sentence. Various properties about this function are then proved, in particular how the function interacts with other linguistic operations and functions that have been defined in the main body of the work. 

Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.

.. _definition-3-2-1:

**Definition 3.2.1: Delimiter Count Function** Let *t* be a String with length *l(t)*. Let **T** be the Character-level representation of *t* with the Characters *𝔞*:sub:`i` denoting the *i*:sup:`th` character of the String *t*, where *1 ≤ i ≤ l(t)*,

    T = { (1, 𝔞:sub:`1`), (2, 𝔞:sub:`2`), ... , (l(t), 𝔞:sub:`l(t)`) }

The Delimiter Count Function, denoted by *Δ(t)*, is defined as the number of Delimiter Characters (*σ*) in the string *t*. Formally, *Δ(t)* is defined as the cardinality of the set that satisfies the following formula:

    D:sub:`t` ↔ { (i, ⲁ) ∈ T | ⲁ = σ, 1 ≤ i ≤ l(t) } 

Then, the delimiter count function is defined as

    Δ(t) = | D:sub:`t` | ∎

**Example** 

Consider the string *t = "a b c"*. The Character-level set representation of *t* is given by,
    
    T = { (1, "a"), (2, σ), (3, "b"), (4, σ), (5, "c") }.

By Definition 3.2.1, The set **D**:sub:`t` contains the ordered pairs *(2, σ)* and *(4, σ)*, where the first coordinate of each pair correspond the positions of the two Delimiter Characters in the String. Therefore, 
    
    D:sub:`t`= { (2, σ), (4, σ) }

From this it follows, 

    | D:sub:`t` | = 2 
    
Hence, 
    
    Δ(t) = 2 ∎

From the previous example, it can be seen the Delimiter Count function takes a Sentence as input and produces a non-negative integer (the Delimiter count) as output. Multiple sentences can have the same Delimiter count, making it a many-to-one function. While this many not be advantageous from a computational perspective, the Delimiter Count function has other interesting properties that make it worth studying. The following theorems describe some of its properties.

**Theorem 3.2.1** ∀ ζ ∈ C:sub:`L`: Λ(ζ) = Δ(ζ) + 1

.. note::

    I think this needs revised to be *Λ(ζ) ≥ Δ(ζ) + 1* to account for edge cases where the sentence has multiple Delimiters in sequence, or has a Delimiter at the end or beginning of the String. 
    
    Alternatively, this inconsistency might be resolvable by introducing an assumption about the structure of a Sentence. Perhaps all Delimiters between two consecutive Words should be treated as a single Delimiter? Or an Axiom to constrain the placement of Delimiters in Sentences?

In natural language, this theorem is stated: For any sentence *ζ* in a Corpus C:sub:`L`, the length of the Sentence is equal to its Delimiter count plus one.

Assume *ζ ∈* **C**:sub:`L`. Let *Δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the Character-level representation of ζ. Let **W**:sub:`ζ` be the word-level set representation of ζ. Recall **W**:sub:`ζ` is formed by splitting **Ζ** at each Delimiter Character *σ* with the Delimiting Algorithm in Definition 2.1.3.

Each word in **W**:sub:`ζ` corresponds to a contiguous subsequence of non-Empty, non-Delimiter Characters in **Ζ**.

Since Delimiters separate Words, and each Delimiter corresponds to one Word boundary, the number of Words in the Sentence is always one more than the number of delimiters. Therefore, the cardinality of **W**:sub:`ζ` (the number of words) is equal to the Delimiter count of *Δ(ζ)* plus one,

    | W:sub:`ζ` | = Λ(ζ) = Δ(ζ) + 1. ∎

The next two theorems establish the invariance of the Delimiter count under String Inversion for any String, and by extension, any Sentence.

**Theorem 3.2.2** ∀ s ∈ S: Δ(s) = Δ(inv(s))

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

**Theorem 3.2.3** ∀ ζ ∈ C:sub:`L`: Δ(ζ) = Δ(inv(ζ))

Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L`,

    1. ζ ∈ C:sub:`L`

By Definition 2.1.2, every Sentence is a String. Therefore, *ζ* is a String. By Theorem A.3.2, 

    1. Δ(ζ) = Δ(inv(ζ))

Which is what was to be shown. ∎

**Theorem 3.2.4** ∀ α ∈ L: Δ(α) = 0

This theorem can be stated in natural language as follows: The Delimtier Count of any Word in a Language is zero.

Assume *α* is a Word in Language **L**,

    1. α ∈ L
    
By the Discovery Axiom W.1, all Words in Language do not have Delimiters,

    2. ∀ i ∈ N:sub:`l(s)`: α[i] ≠ σ

Therefore, *α* does not have any Delimiter Characters (*σ*). By Definition 2.4.1, *Δ(s)* counts the number of Delimiter Characters (*σ*) in a String *s*. Since *α* hasno Delimiter Characters, the Delimiter Count of *α* must be 0. Therefore,

    3. Δ(α) = 0 ∎

**Theorem 3.2.5** ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

In natural language, this theorem can be stated as follows: For every Sentence in a Corpus, the String Length of the Sentence is equal to the Delimiter Count of the sentence plus the sum of the String Lengths of its Words.

Assume 

    1. ζ ∈ C:sub:`L`. 

Either each *ζ{i}* for *1 ≤ i ≤ l(ζ)* is Delimiter or it is a non-Delimiter, with no overlap. By Definition 3.2.1, the number of Delimiter Characters in *ζ* is *Δ(ζ)*. 

By the Discovery Axiom W.1, words in **L** do not contain Delimiters. By Definition 2.1.3, the Words in **W**:sub:`ζ` are obtained by splitting *ζ*  at the Delimiters. Therefore, the total number of non-Delimiter characters in *ζ* is the sum of the Word Lengths l(ζ{i}) which is 

    2. Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Since every Character in *ζ* is either a Delimiter or part of a Word (and not both), the total number of Characters in *ζ* is the sum of the number of Delimiters and the number of Characters in Words. By Definition 1.1.3 of String Length, the total number of non-Empty characters in ζ is *l(ζ)*. Therefore, the number of non-Empty Characters in *ζ* is equal to the number of Delimiters plus the sum of its Word Lengths,

    3. ∀ ζ ∈ C:sub:`L`: l(ζ) = Δ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I}) ∎

**Theorem 3.2.6** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = Λ(ζ) + Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{I})

Applying the results of Theorem 3.2.1 and Theorem 3.2.5, this theorem follows from simple algebraic manipulation. ∎

**Theorem 3.2.7** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥  Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i})

This theorem can be stated in natural language as follows: For any Sentence in the Corpus, its String Length is greater than or equal to the sum of the String Length of its Words. 

Assume *ζ ∈* **C**:sub:`L`. By Theorem 3.2.4,
    
    1. Λ(ζ) ≥ 1

From Theorem 3.2.6,

    2. l(ζ) + 1 - Σ:sub:`i = 1`:sup:`Λ(ζ)` l(ζ{i}) = Λ(ζ)

Combining step 1 and step 2, the theorem is obtained through algebraic manipulation,

    l(ζ) ≥ Σ:sub:`i = 1`:sup:`Λ(ζ)` l(α) ∎

.. _theorem_3-2-8:

**Theorem 3.2.8** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ Λ(ζ)

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

**Theorem 3.2.9 (Informal)** ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

Let *u* and *t* be arbitrary strings in S. Let **U** and **T** be the Character-level representations of *u* and *t*, respectively:

    1. U = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(u)`)

    2. T = (𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)`)

The Character-level representation of *ut* is:

    3. UT = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(u)`, 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(t)``)

By Definition 3.2.1, *Δ(u)* is the number of Delimiters in *u*, *Δ(t)* is the number of Delimiters in *t*, and *Δ(ut)* is the number of Delimiters in *ut*.

Since concatenation simply joins two Strings without adding or removing Characters, with the possible exception of Empty Characters through the Basis Clause of Definition 1.1.1, the number of Delimiters in *ut* is the sum of the number of Delimiters in *u* and the number of Delimiters in *t*. ∎

**Theorem 3.2.9 (Formal)** ∀ u, t ∈ S: Δ(ut) = Δ(u) + Δ(t)

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

**Theorem 3.2.10** ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t)

Let *u* and *t* be arbitrary strings in S.

By Theorem A.4.2,

    1. Δ(s) = Δ(inv(s)).

Therefore, 

    2. Δ(ut) = Δ(inv(ut)).

By Theorem 3.2.9,
 
    3. Δ(ut) = Δ(u) + Δ(t).

Combining steps 2 and 3, it follows, 

    4. Δ(inv(ut)) = Δ(ut) = Δ(u) + Δ(t)

Since *u* and *t* were arbitrary strings, this can be generalized,

    5. ∀ u, t ∈ S: Δ(inv(ut)) = Δ(u) + Δ(t) ∎

**Theorem 3.2.11** ∀ t ∈ S: Δ(ς(t)) = 0

This theorem can be stated in natural language as follows: For any String, the Delimiter Count of its *σ*-Reduction is 0.

Let t be an arbitrary string in **S**,

    1. t ∈ S

By Definition 3.1.2, *ς(t)* is the String obtained by removing all occurrences of the Delimiter character *σ* from *t*. By Definition 3.2.1, Δ(t) is the number of Delimiter Characters *σ* in a String *t*. Since *ς(t)* has all its Delimiters removed, it contains no occurrences of the Character *σ*. Therefore, 

    2. Δ(ς(t)) = 0

Since *t* was an arbitrary string in **S**, this can be generalized over **S**,

    3. ∀ t ∈ S: Δ(ς(t)) = 0 ∎

**Theorem 3.2.12** ∀ t ∈ S: l(ς(t)) + Δ(t) = l(t)

Translation: For any String, its String Length is equal to the String Length of its σ-reduction plus its Delimiter Count.

Let *t* be an arbitrary String in **S**,

   1. t ∈ S

By Definition 3.1.2, *ς(t)* is the String obtained by removing all occurrences of the Delimiter character *σ* from *t*.

By Definition 3.2.1, *Δ(t)* is the number of Delimiter characters in *t*.

By Definition 1.1.3, *l(t)* is the total number of non-Empty Characters in *t*, including Delimiters.

Similarly, *l(ς(t))* is the number of non-DelimiterCcharacters in *t*.

Every Character in *t* is either a Delimiter or a non-Delimiter character. Therefore, the total number of characters in *t* is the sum of the number of non-delimiter characters and the number of delimiter characters.

Therefore,

    2. ∀ t ∈ S: l(ς(t)) + Δ(t) = l(t)

Since *t* was an arbitrary String, this can be generalized over **S**,

    1. ∀ s ∈ S: l(s) = l(ς(t)) + Δ(s)  ∎

Theorem 3.2.12 expresses a fundamental relationship between the String Length of a String, the String Length of its σ-reduction, and its Delimiter Count. It essentially states that the original String Length can be decomposed into the String Length of the String without Delimiters (the *σ*-reduction) and the number of Delimiters that were removed (the Delimiter Count).

**Example**

Let *t = (𝔞)(σ)(𝔟)(σ)(𝔠)*. Then, by Definition 3.1.2,

    ς(t) = 𝔞𝔟𝔠

The following quantities can then be calculated,

    l(t) = 5    
    Δ(t) = 2
    l(ς(t))= 3

And indeed, 

    l(t) = l(ς(t)) + Δ(t) ∎

**Theorem 3.2.13** ∀ ζ ∈ C:sub:`L`: l(ς(t)) + Λ(ζ) = l(ζ) + 1

Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L`,

    1. ζ ∈ C:sub:`L`

By Definition 2.1.2, every Sentence is a String. Therefore, Theorem 3.2.12 may be applied to *ζ*

    2. l(ζ) = l(ς(ζ)) + Δ(ζ)

By Theorem 3.2.1,

    3. Λ(ζ) = Δ(ζ) + 1

Rearranging,

    4. Δ(ζ) = Λ(ζ) - 1

Substituting the expression for *Δ(ζ)* from step 4 into the equation from step 2,

    5. l(ζ) = l(ς(ζ)) + (Λ(ζ) - 1)

Rearranging the terms, 

    6. l(ς(ζ)) + Λ(ζ) = l(ζ) + 1

Since ζ** was an arbitrary Sentence in **C**:sub:`L`, this can be generalized over the Corpus as,

    7. ∀ ζ ∈ C:sub:`L`: l(ς(ζ)) + Λ(ζ) = l(ζ) + 1 ∎