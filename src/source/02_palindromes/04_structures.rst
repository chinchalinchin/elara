Section III: Structures
=======================

The foundation of the formal system has now been laid. Mathematical machinery capable of describing linguistic hierarchies has been constructed. The purpose of this formal system is to analyze the structures embedded in Palindromes. While the formal system possesses flexibility and applicability (as demonstrated by its ability to generate theorems like Theorem 2.3.9 which are empirically verifiable), it does not yet have the necessary tools for describing palindromic structures. 

Inversion, while a key component of the apparatus necessary for understanding the dynamics of Palindromes, is not the only linguistic operation involved in the formation of Palindromes. The pure involutive property of Palindromes (e.g., *ζ = inv(ζ)*) only manifests in a rare class of Sentences known as Perfect Palindrome (Definition 4.1.2).

However, the vast majority of Palindromes in any language are not pure involutions. Instead, the operation of inversion usually degrades the semantic content of a Sentence by re-ordering the Delimiters, as seen in the following, 

    ζ = "now sir a war is won"

    inv(ζ) = "now si raw a ris won"

In order to properly understand the nature of a Palindrome, the formal system under construction must have a method of quantifying the distribution of Delimiters in a Sentence and making claims about the nature of that Distribution. Furthermore, the system requires a method of removing the *"impurities"* in semantic content that introduced through *inversion*.

This section of the work is dedicated to introducing several novel concepts for analyzing Delimiters distributions: the operation of *σ-reduction*, the *Delimiter Count* function and *Sentence Integrals*.

Section III.I: σ-Reductions 
----------------------------

The mathematical definition of Palindromes (Definition 4.1.1 in the next section) will revolve around a novel linguistic operation, termed a *σ*-reduction. This operation will allow the semantic content of a Palindrome to be projected onto an Alphabet that preserves the order of its Characters under String Inversion, allowing for a precise specification of palindromic inversion in an Alphabet where symmetry is preserved.

Definitions
^^^^^^^^^^^

Before defining a *σ*-reduction, the preliminary concept of a *σ-reduced Alphabet* must be introduced. The following definition serves as the basis for constructing the operation of *σ*-reduction.

As has been seen with examples of Imperfect Palindromes like *"borrow or rob"*, a palindromic structure can have its Delimiter Character scrambled in the inversion of its form, i.e. *"bor ro worrob"*, making it lose semantic coherence. Imperfect Palindromes must be rearranged Delimter-wise to retrieve the original form of the Sentence. However, String Inversion preserves the relative order of the non-Delimiter Characters in a palindromic String, so the process of reconstitution is only a matter of resorting the Delimiter characters. This invariance of the Character order, while the Word order is scrambled by Delimiter, suggests palindromes might be more easily defined without the obstacle of the Delimiter.

**Definition 3.1.1: σ-Reduced Alphabet**

A *σ-reduced Alphabet* is an Alphabet Σ that has had its Delimiter character removed, so that it only consists of non-Delimiter characters. A sigma-reduced Alphabet is denoted Σ:sub:`σ`. Formally,

    Σ:sub:`σ` = Σ - { σ } ∎

In order to define palindromes in all of their varieties, perfect or imperfect, the semantic incoherence that is introduced by the inversion of Imperfect Palindromes must be removed. This is accomplished through the introduction of the operation of *sigma reduction*.

**Definition 3.1.2: σ-Reduction**

Let *t* be a String with length *l(t)* and Character-level representation 

    1. t = { (1,𝔞:sub:`1`) , (2, 𝔞:sub:`2`) , ... , (l(t), 𝔞:sub:`l(t)`) } 
    2. 𝔞:sub:`i` ∈ Σ.

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
        
        a. Apply Basis Clause of Definition 1.1.1 to t
    
    6. Return t ∎

Note the String *s* which is initialized to hold the *σ*-reduced String is set equal to the value of the Empty Character. The conditional application of the Basis Clause of Concatenation in step 1 of the Finalization Block ensures this Character is removed from the output of the Reduction Algorithm, if the input string contained at least one non-Empty Character. Otherwise, the Reduction Algorithm returns an Empty Character. From this, it is clear if a String only contains Delimiters,

    ε = ς(σ) = ς(σσ) = ς(σσσ) = ... 

From which, it follows, by Definition 1.1.3 of String Length, the String Length of a reduced Delimiter is simply zero,

    l(ς(σ)) = 0

Moreover, since by Discovery Axiom W.1., Words do not contain Delimiters, for any Word *α* in Language **L**,

    ς(α) = α

Again, from Definition 1.1.3, the String Length of a reduced Word is simply the String Length of the Word,

    l(ς(α)) = l(α)

A subtlety of the Reduction Algorithm should be noted. While *ς(σ) = ε* and *ς(α) = α*, it does not follow the *σ*-reduction of a Word concatenated with the Delimiter is the concatenation of that Word with the Empty Character. In other words, the following holds,

    ς(ασ) ≠ αε

This is because of the condition *(j > 1)* in the Finalization Block of the Reduction ensures Empty Characters are stripped from *t* when the input String contains atleast one non-Empty Character that has been concatenated into the *σ*-reduction String. 

The more complicated properties of *σ*-reductions are proved in the theorems that follow. Before moving onto the proofs, the following example shows how to apply the Reduction Algorithm to construct the *σ*-reduction of a String.

**Example**

Let *s = "a b c"* be a String from the Alphabet *Σ = { "", " " , "a", "b", "c" }*. Note in this example *σ = " "* and *l(s) = 5*. The value of the variables in the Reduction Algorithm after each iteration are given below,

    1. i = 2, t = ε"a"
    2. i = 3, t = ε"a"
    3. i = 4, t = ε"ab"
    4. i = 5, t = ε"ab"
    5. i = 5, t = "abc"
        
The result of the σ-reduction of *s* is thus given by,

    ς(s) = "abc" ∎

A *σ*-reduction can be thought of as a linguistic operation analogous to vector projection. While not a strict mathematical equivalence, this conception of *σ*-reduction captures the idea of transforming a String from its original form (with Delimiters) onto a reduced space (without Delimiters), similar to how a vector can be projected onto a subspace.

The *σ*-reduced Alphabet (**Σ**:sub:`σ`) can be seen as a subspace within this higher-dimensional space, consisting of only the non-Delimiter dimensions. The sigma reduction function (*ς(s)*) acts as a projection operator, mapping the String onto this subspace by eliminating the components corresponding to the Delimiter character (*σ*).

Note that a *σ*-reduction is not a one-to-one operation. It is possible for the *σ*-reduction of a palindrome to map onto a totally different sentence, not necessarily a palindrome.

As an example, consider the (partial, ignoring punctuality) Palindromes *ᚠ = "madam im adam"* and *ᚢ = "mad am i madam"*. The *σ*-reduction of both of these Sentences would map to the *σ-reduced* value of *madamimadam".

Both the Palindrome and the alternative Sentence (which also happens to be a Palindrome) have the same *σ*-reduction, despite having different meanings and grammatical structures. This highlights the ambiguity that can arise from removing spaces, as the original Word boundaries and Sentence structure are lost.

Theorems 
^^^^^^^^

The following theorems establish the basic properties of *σ*-reductions. 

**Theorem 3.1.1** ∀ ζ ∈ C:sub:`L`: inv(ς(ζ)) = ς(inv(ζ))

Let *ζ* be an arbitrary sentence in C:sub:`L`. Let *s* be the *σ*-reduction of *ζ*,

    1. s = ς(ζ)

Let *t* be the Inverse of *s*,

    2. t = inv(s).

Let *u* be the Inverse of *ζ*,

    3. u = inv(ζ). 
    
Let *v* be the *σ*-reduction of *u*,

    4. v = ς(u) = ς(inv(ζ)) 

Since *s* contains only the non-Delimiter characters of *ζ* in their original order, and *t* is the reversed sequence of Characters in *s*, *t* contains only the non-Delimiter characters of *ζ* in reversed order.

Similarly, since *u* is the reverse sequence of Characters in *ζ*, and *v* is obtained by removing Delimiters from *u*, *v* also contains only the non-Delimiter characters of *ζ* in the reversed order.

Therefore, by Definition 1.1.4, *t* and *v* must be the same String, as they both contain the same Characters in the same order. Since *t = v*, 

    1. inv(ς(ζ)) = ς(inv(ζ))

Since ζ was an arbitrary sentence in C:sub:`L`, this can be generalized,

    1. ∀ ζ ∈ C:sub:`L`: inv(ς(ζ)) = ς(inv(ζ)) ∎

This corollary is essential because it allows free movement between the Inverse of a *σ*-reduction and the *σ*-reduction of an Inverse. In other words, Theorem 3.1.1 establishes the commutativity of *σ*-reduction over inversion and visa versa. 

As the theorems in this section will make clear, there exists a unique type of algebraic structure that links the operations of *σ*-reduction, inversion and concatenation. The properties of this algebraic structure will be necessary for establishing the results in the next subsection.

The next theorem demonstrates how *σ*-reduction interacts with concatenation.

**Theorem 3.1.2** ∀ ζ, ξ ∈ C:sub:`L`: ς(ζξ) = (ς(ζ))(ς(ξ))

Let *ζ* and *ξ* be arbitrary sentences in **C**:sub:`L`. Let **Ζ** and **Ξ** be the character-level representations of *ζ* and *ξ*, respectively,

    1. Ζ = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(ζ)`)

    2. Ξ = (𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(ξ))`

Let *ζξ* be the concatenation of *ζ* and *ξ*. The character-level representation of *ζξ* is,

    3. ΖΞ = (ⲁ:sub:`1`, ⲁ:sub:`2`, ..., ⲁ:sub:`l(ζ)`, 𝔟:sub:`1`, 𝔟:sub:`2`, ..., 𝔟:sub:`l(ξ)`)

Let *s* be the σ-reduction of *ζξ*. Let *t* be the *σ*-reduction of *ζ*. Let *u* be the *σ*-reduction of *ζξ*,

    4. s = ς(ζξ)
    5. t = ς(ζ)
    6. u = ς(ξ)

Let *v* be the concatenation of the Strings *t* and *u*,

    7. v = tu = (ς(ζ))(ς(ξ))

Since *σ*-reduction only removes Delimiters and doesn't change the order of non-Delimiter Characters, the non-Delimiter characters in *s* (the *σ*-reduction of *ζξ*) are the same as the non-Delimiter Characters in *ζ* followed by the non-Delimiter Characters in ξ.

The non-Delimiter characters in *v*, the concatenation of *ς(ζ)* and *ς(ξ)*, are also the non-Delimiter characters in *ζ* followed by the non-delimiter characters in *ξ*.

Therefore, by Definition 1.1.4, *s* and *v* must be the same String, as they both contain the same Characters in the same order (the non-Delimiter Characters of *ζ* followed by the non-Delimiter characters of *ξ*). Since *s = v*, 

    8. ς(ζξ) = (ς(ζ))(ς(ξ))

Since ζ and ξ were arbitrary sentences in C:sub:L, this can be generalized,

    9. ∀ ζ, ξ ∈ C:sub:`L`: ς(ζξ) = (ς(ζ))(ς(ξ)) ∎

Theorem 3.1.2 further demonstrates the *algebraic* nature of *σ*-reduction and the other String operations. It shows that *σ*-reduction *distributes* over concatenation, just as inversion "distributes" (in a reversed way) over concatenation (Theorem 1.2.5). These properties suggest that *σ*-reduction, inversion and concatenation are not just arbitrary operations but instead are deeply connected to the underlying structure of Strings and Sentences.

As another example of this *"linguistic algebraic structure"*, the following theorem might be termed the *"Idempotency of σ-reduction"* or the *"σ-reduction Idempotence Property"*.

**Theorem 3.1.3** ∀ ζ ∈ C:sub:`L`: ς(ς(ζ)) = ς(ζ)

Let *ζ* be an arbitrary Sentence in **C**:sub:`L`. Let s be the *σ*-reduction of *ζ*,

    1. s = ς(ζ)

Let *t* be the *σ*-reduction of *s*,

    2. t = ς(s) = ς(ς(ζ))

Since *s* is the result of applying a *σ*-reduction to *ζ*, it contains no Delimiter Characters (σ).

When *s* is *σ*-reduced (to get *t*), the Reduction Algorithm in Definition 3.1.2 iterates through the Characters of *s*. Since s has no Delimiters, the condition if *s[i] ≠ σ* in the algorithm will always be true, and every character of *s* will be concatenated to the initially empty string *t*. Therefore, by Definition 1.1.4, *t* will be identical to *s*, as it contains the same Characters in the same order. Thus,

    1. ς(ς(ζ)) = ς(ζ)

Since ζ was an arbitrary sentence in C:sub:L, this can be generalized,

    4. ∀ ζ ∈ C:sub:`L`: ς(ς(ζ)) = ς(ζ) ∎

**Theorem 3.1.4** ∀ ζ ∈ C:sub:`L`: Λ(ς(ζ)) ≤ 1

Let *ζ* be an arbitrary sentence in C:sub:`L`. By the Duality Axiom S.1, every Sentence in C:sub:`L` must contain at least one word from L. 

By Definition 3.1.2, *ς(ζ)* removes all Delimiters from *ζ*. Therefore, *ς(ζ)* consists of the Characters of the words in *ζ* concatenated together without any delimiters.

By the Discovery Axiom W.1., Words in **L** cannot contain Delimiters.

By Definition 2.1.4, the Word Length *Λ(s)* of a String *s* counts the number of Words in *s*, where Words are separated by Delimiters.

If *ζ* contains only one Word, then *ς(ζ)* will be that Word,

    1. Λ(ς(ζ)) = 1

If *ζ* contains multiple Words, then *ς(ζ)* will be a concatenation of those words without Delimiters. This concatenated String may or may not be a valid Word in **L**.

If the concatenated String is a valid Word in **L**, then,

    2. Λ(ς(ζ)) = 1

If the concatenated String is not a valid Word in **L**, then,

    3. Λ(ς(ζ)) = 0

Therefore, in all possible cases,

    Λ(ς(ζ)) ≤ 1.

Since *ζ* was an arbitrary sentence in **C**:sub:`L`, this can be generalized, 

    ∀ ζ ∈ C:sub:`L`: Λ(ς(ζ)) ≤ 1. ∎


**Theorem 3.1.5** ∀ u, t ∈ S : u ⊂:sub:`s` t ↔ ς(u) ⊂:sub:`s` ς(t) 

This theorem can be stated in natural language as follows: For any two Strings *u* and *t*, *u* is contained in *t* if and only if the *σ*-reduction of *u* is contained in the *σ*-reduction of *t*.

Let *u* and *t* be arbitrary strings in **S**.

(→) Assume 

    1. u ⊂:sub:`s` t.

By Definition 1.1.7, there exists a strictly increasing and consecutive function *f*: N:sub:`l(u)` → N:sub:`l(t)` such that,

    2. ∀ i ∈ N:sub:`l(u)`: u[i] = t[f(i)]

Let 

    3. s = ς(u) 
    4. v = ς(t).

By the Definition 3.1.2 of *σ*-reduction, *s* is obtained by removing all Delimiters from *u*, and *v* is obtained by removing all Delimiters from *t*.

Since *u* is contained in *t*, the non-Delimiter Characters of *u* appear in *t* in the same order. The function *f* maps the indices of these Characters.

Define a function *g*: **N**:sub:`l(s)` → **N**:sub:`l(v)` that maps the indices of *s* to the indices of *v*. In other words, if *i* is an index in *s*, then *g(i)* is the index in *v* that corresponds to the same non-Delimiter character.

Since *f* is strictly increasing and consecutive, and *σ*-reduction only removes Delimiters, *g* will also be strictly increasing and consecutive. (*g* essentially compresses the mapping of *f* by skipping over the Delimiter indices and offseting).

For any index *i* in *s*, 

    5. s[i] = u[j] 
    
for some j. Moreover, 

    6. u[j] = t[f(j)]. 
    
Since *s* and *v* are *σ*-reduced, *s[i]* and *v[g(i)]* correspond to the same non-Delimiter Character, and g(i) is constructed such that 

    7. v[g(i)] = t[f(j)]. 
    
Therefore, 

    8. s[i] = v[g(i)].

Since g is a strictly increasing and consecutive function and s[i] = v[g(i)], by Definition 1.1.7, 

    9. s ⊂:sub:`s` v
    
From which it follows,

    10. ς(u) ⊂:sub:`s` ς(t).

(←) Assume 

    1. ς(u) ⊂:sub:`s` ς(t).

By Definition 1.1.7, there exists a strictly increasing and consecutive function *g*: **N**:sub:`l(ς(u))` → **N**:sub:`l(ς(t))` such that:

    2. ∀ i ∈ N:sub:`l(ς(u))`: ς(u)[i] = ς(t)[g(i)]

Define a function *f*: N:sub:`l(u)` → N:sub:`l(t)` that maps the indices of *u* to the indices of *t* by essentially "re-inserting" the delimiters. For each non-Delimiter character in *u* (and corresponding index in *ς(u)*), *f* will map to the corresponding index in *t*. For Delimiter characters in *u*, *f* will map to an index in *t* that preserves the order and consecutiveness.

Since *g* is strictly increasing and consecutive, and the Delimiters are only removed, not reordered, the function *f* will also be strictly increasing and consecutive.

For each index *i* in *u*, *u[i]* will either be a non-Delimiter or a Delimiter Character.

If *u[i]* is a non-Delimiter character, it corresponds to a Character in *ς(u)*, and by the properties of *g* and *f*, the following holds for some *j*,

    3. u[i] = ς(u)[j] = ς(t)[g(j)] = t[f(i)] 

If *u[i]* is a Delimiter, then by the construction of *f*, it will be mapped to a corresponding Delimiter in *t*, so 

    4. u[i] = t[f(i)]

Since *f* is a strictly increasing and consecutive function and *u[i] = t[f(i)]* for all *i* *∈* **N**:sub:`l(u)`, by Definition 1.1.7,

    5. u ⊂:sub:`s` t.

Since both directions of the implication hold, it can be concluded,

    6. ∀ u, t ∈ S : u ⊂:sub:`s` t ↔ ς(u) ⊂:sub:`s` ς(t) ∎

During a *σ*-reduction, Theorem 3.1.4 demonstrates information is lost with respect to the following semantic categories,

  - Word Boundaries: The spaces between words, which are crucial for parsing and understanding the sentence, are eliminated.
  - Sentence Structure: The grammatical structure of the sentence, the relationships between words and phrases, becomes ambiguous.
  - Prosody and Rhythm: The pauses and intonation that contribute to the meaning and expression of the sentence are lost.

However, some semantic information is preserved. The individual words themselves, or at least their character sequences, remain present in the *σ-reduced* string. The next theorem proves semantic content is retained during the *σ*-reduction of a Sentence.

**Theorem 3.1.6** ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` ς(ζ)

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus **C**:sub:`L`, and for every Word *ζ{i}* in the Word-level representation of *ζ*, *ζ{i}* is contained in *ς(ζ)*.

Let *ζ* be an arbitrary sentence in **C**:sub:`L`. By Theorem 2.2.4, it is known at least one Word must exist in *ζ*. Let *ζ{i}* be one of the Words in the sequence of Words that form *ζ*. 

This means that *ζ* can be written as either, in the case of *Λ(ζ) > 1*, 

    1. Case (Λ(ζ) > 1): ζ = (s:sub:`1`)(σ)(ζ{i})(σ)(s:sub:`2`)
    
where *s*:sub:`1` and *s*:sub:`2` are (possibly Empty) Strings. 

In the case that Λ(ζ) = 1, then, this means *ζ* can be written simply as, 

    1. Case (Λ(ζ) = 1): ζ = ζ{1}

By the Definition 3.1.2, *ς(ζ)* is obtained by removing all Delimiters from *ζ*. Furthermore, by Theorem 3.1.2, *σ*-reduction distributes over concatenation. Thus,

    1. Case (Λ(ζ) > 1): ς(ζ) = (ς(s:sub:`1`))(ς(ζ{i}))(ς(s:sub:`1`))
    2. Case (Λ(ζ) = 1): ς(ζ{1})

By the Discovery Axiom W.1, Words in **L** do not contain Delimiters.

    1. Case (Λ(ζ) > 1): ς(ζ) = (ς(s:sub:`1`))(ζ{i})(ς(s:sub:`1`))
    2. Case (Λ(ζ) = 1): ς(ζ{1}) = ζ{1}

Therefore, by the definition of Containment (Definition 1.1.4):

    1. Case (Λ(ζ) > 1): ζ{i} ⊂:sub:`s` ς(ζ)
    2. Case (Λ(ζ) = 1): ζ{1} ⊂:sub:`s` ς(ζ) 

In both cases, there is a Word in *ζ* that is contained in the *σ*-reduction of *ζ*. Since *ζ* was arbitrary, this can generalize as,

    ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` ς(ζ) ∎

As one of the final precursors to a formal explication of palindromic structures, this next theorem shows how *σ*-reduction behaves over the class of Invertible Sentences, an extremely important class for understanding the mechanics of Palindromes.

**Theorem 3.1.7** ∀ ζ ∈ K: [ ς(ζ) = inv(inv(ς(ζ))) ]

In natural language, this theorem can be stated in natural language as follows: If a Sentence in a Corpus is invertible, then its invertibility is invariant under *σ*-reduction.

Assume 

    1. ζ ∈ K

In other words, assume that *ζ* is an Invertible Sentence. By Theorem 2.3.7, since *ζ* is invertible, all its Words are also Invertible,
 
    2. ∀ ζ ∈ C:sub:`L`: inv(ζ) ∈ K → inv(ζ){i} ∈ L

The σ-reduction of *ζ*, *ς(ζ)*, is obtained by removing all Delimiters from ζ. Since no Word contains Delimiters (by Discovery Axiom W.1), the *σ*-reduction concatenates the Words of *ζ*,

    3. ς(ζ)= (ζ{1})(ζ{2})...(ζ{Λ(ζ)})

Applying Theorem 1.2.5 repeatedly,

    4. inv(ς(ζ)) = inv((ζ{1})(ζ{2})...(ζ{Λ(ζ)}))

To get,

    5.  inv(ς(ζ))  = (inv(ζ{Λ(ζ)})) ... (inv(ζ{2}))(inv((ζ{1})))

Applying a second Inversion,

    6. inv(inv(ς(ζ))) = inv((inv(ζ{Λ(ζ)})) ... (inv(ζ{2}))(inv((ζ{1}))))

Applying Theorem 1.2.5 again,

    7. inv(inv(ς(ζ))) = (inv(inv((ζ{1})))) (inv(inv((ζ{2}))))...(inv(inv((ζ{Λ(ζ)}))))

Finally, applying Theorem 1.2.4 (*inv(inv(s)) = s*)

    8. inv(inv(ς(ζ))) = (ζ{1})(ζ{2})...(ζ{Λ(ζ)})

Therefore, combining step 3 and step 8

    9. ς(ζ) = inv(inv(ς(ζ))). ∎

The contrapositive of this theorem, much like the contrapositive of Theorem 2.3.6, provides a schema for searching the *σ-reduced* space for Invertible Sentences. The domain of this space reduces the complexity of searching for palindromic strings. Potential palindromic candidates can be projected into the *σ-reduced* spaced, and then filtered by those whose *σ*-reduction whose Inverse does not equal itself. 

The final theorems in this section, Theorems 3.1.8 - 3.1.9, provide a method for constructing the *σ*-reduction of a Sentence through iterated concatenation. These theorem leverage the operations of Delimitation and Limitation introduced in Definitions 1.2.7 - 1.2.8.

**Theorem 3.1.8** ∀ ζ ∈ C:sub:`L`: ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

This theorem can be stated in natural language as follows: The *σ*-reduction of a Sentence is the Limitation of its Words.

Assume,

    1. ζ ∈ C:sub:`L`

By Definition 2.1.3, 

    2. W:sub:`ζ` = (α:sub:`1`, α:sub:`2`, ..., α:sub:`Λ(ζ)`)

Where,

    3. ∀ i ∈ N:sub:`Λ(ζ)`: α:sub:`i` ∈ L.

By Theorem 2.3.4, ζ can be expressed as the Delimitation of its words:

    4. ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i} = (ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{Λ(ζ)})

By Definition 3.1.2, *ς(ζ)* removes all Delimiters from *ζ*. Applying *σ*-reduction to the expression step 4,

    5. ς(ζ) = ς((ζ{1})(σ)(ζ{2})(σ) ... (σ)(ζ{Λ(ζ)}))

By repeated application of Theorem 3.1.2, i.e. by distributing the *σ*-reduction,

    6. ς(ζ) = (ς(ζ{1}))(ς(σ))(ς(ζ{2}))(ς(σ)) ... (ς(σ))(ς(ζ{Λ(ζ)}))

Since 

    7. ς(σ) = ε

This can be rewritten with the Basis Clause of Concatenation,

    8. ς(ζ) = (ς(ζ{1}))(ς(ζ{2}))...(ς(ζ{Λ(ζ)}))

By Definition 3.1.2 and the Discovery Axiom W.1.,

    9. ∀ i ∈ N:sub:`Λ(ζ)`: ς(ζ{i}) = ζ{i}

Therefore,
   
    10. ς(ζ) = (ζ{1})(ζ{2})...(ζ{Λ(ζ)})

By Definition 1.2.8, the right-hand side is the Limitation of the words in **W**:sub:`ζ`,

    11. ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

Since *ζ* was an arbitrary Sentence in this Corpus, this can be generalized,

    12. ∀ ζ ∈ C:sub:`L`: ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i} ∎

Theorem 3.1.8 establishes an important formula for the construction of *σ*-reductions. The Reduction Algorithm targets Strings as input, i.e. it processes sequential Characters in a String. If an ordered sequence of Words is already at hand, without Theorem 3.1.8, it would be required to reconstruct the String which corresponds to the sequence and process it through the Reduction Algorithm. Rather than applying the Reduction Algorithm everytime a *σ*-reduction is required, Theorem 3.1.8 provides a schema for the construction of *σ*-reductions through the process of Limitation.

Compare Theorem 3.1.8 to Theorem 2.2.5, reprinted below for reference,

    ζ = DΠ:sub:`i=1`:sup:`n` ζ{i}

In other words, taking the *σ*-reduction of a Sentence converts the Delimitation of its Words into a Limitation. This follows directly from the Definitions of Limitation and Delimitation. The next theorem proves this relationship for the more general case of *any* ordered sequence of Words, not necessarily a semantically coherent and admissible Sentence.

**Theorem 3.1.9** ∀ n ∈ ℕ: ∀ p ∈ Χ:sub:`L(n)`: ς(DΠ:sub:`i=1`:sup:`n` p(i)) = LΠ:sub:`i=1`:sup:`n` p(i)

This theorem can be stated in natural language as follows: the *σ*-reduction of a Delimitation of a Phrase is equal to a Limitation of the same Phrase.

Let *n* be an arbitrary natural number, and let *p* be an arbitrary Phrase from a Language's *n*:sup:`th` Lexicon, 

    1. p ∈ Χ:sub:L(n)
    2. p = (α:sub:`1`, α:sub:`2`, ..., α:sub:`n`).

By Definition 1.2.7, 

    3. DΠ:sub:`i=1`:sup:`n` p(i) = (α:sub:`1`)(σ)(α:sub:`2`)(σ) ... (σ)(α:sub:`n`)

Applying Definition 3.1.2 of *σ*-reduction to the Delimitation and applying the Basis Clause of Definition 1.1.1,

    4. ς(DΠ:sub:`i=1`:sup:`n` p(i)) = (α:sub:`1`)(α:sub:`2`)... (α:sub:`n`)

By Definition 1.2.8,

    5. LΠ:sub:`i=1`:sup:`n` p(i) = (α:sub:`1`)(α:sub:`2`) ... (α:sub:`n`)

By repeated application of Theorem 1.1.1 to step 4,

    6. ς(DΠ:sub:`i=1`:sup:`n` p(i)) = Σ:sub:`i=1`:sup:`n` α:sub:`i`

By repeated application of Theorem 1.1.1 to step 5,

    7. l((α:sub:`1`)(α:sub:`2`)... (α:sub:`n`)) = Σ:sub:`i=1`:sup:`n` α:sub:`i`

Comparing step 6 to step 7 and noting the *α*:sub:`i` is in the same position the same for all *1 ≤ i ≤ n*, it follows by Definition 1.1.4 of String Equality, 

    8. ς(DΠ:sub:`i=1`:sup:`n` p(i)) = LΠ:sub:`i=1`:sup:`n` p(i)

Since n and p were arbitrary, this can be generalized,

    9. ∀ n ∈ ℕ: ∀ p ∈ Χ:sub:`L(n)`: ς(DΠ:sub:`i=1`:sup:`n` p(i)) = LΠ:sub:`i=1`:sup:`n` p(i) ∎

The relationship between σ-reductions, Limitations and Delimitations provides an easy method for establishing the relationship between the String Length of a Sentence and the String Length of its σ-reduced form. 

**Theorem 3.1.10** ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ l(ς(ζ))

Let ζ be an arbitrary Sentence in the Corpus. By Theorem 3.1.8,

    1. ς(ζ) = LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

By Theorem 2.2.5,

    2. ζ = DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

Since the only different between Definition 1.2.7 and 1.2.8 is that Delimitations insert a Delimiter while Limitations simply concatenate, it must follow,

    3. l(DΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}) ≥ LΠ:sub:`i=1`:sup:`Λ(ζ)` ζ{i}

From this, step 1 and step 2, it follows, 

    4. l(ζ) ≥ l(ς(ζ))

Since ζ was arbitary, this can be generalized, 

    5. ∀ ζ ∈ C:sub:`L`: l(ζ) ≥ l(ς(ζ)) ∎

Section III.II: Delimiter Count Function 
--------------------------------------

Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a Palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a Palindrome is distributed through its syntactical layers. The concepts of *Perfect* and *Imperfect* Palindromes are be defined more rigorously in Section III, but as an intuitive introduction to the ability of a Palindrome to encode meaning on multiple syntactic levels and as a justification for the introduction of the Delimiter Count Function, consider the following two examples,

    1. dennis sinned
    2. if i had a hifi

The first palindrome "*dennis sinned*" is what will be termed a *Perfect* Palindrome, because its inverse does not require a rearrangement of its constituent Characters to preserve its semantic content. However, the second Palindrome *"if i had a hifi"* is what is termed an *Imperfect* Palindrome. To see the motivation behind this categorization, note the strict inversion of "If I had a hifi" would be (ignoring capitalization for now),

    ifih a dah i fi

The order of the Characters in the Inverse of an Imperfect Palindrome is preserved, but in order to reconstitute its uninverted form, the Delimter Characters must be re-sorted. It appears, then, that Delimiters play a central role in organizing the palindromic structure. 

The study of Delimiter Characters in a Sentence bears study beyond its application to palindromic structures, though. The following section of the Appendix introduces this function for quantifying the number of Delimiters in a sentence. Various properties about this function are then proved, in particular how the function interacts with other linguistic operations and functions that have been defined in the main body of the work. 

Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.

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
