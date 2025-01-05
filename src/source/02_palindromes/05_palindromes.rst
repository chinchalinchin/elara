
Section IV: Palindromes
=======================

As mentioned in the introduction of this work, the structure of palindromes is described through the combination of four different attributes or dimensions: *aspect*, *parity*, *case* and *punctuality*. The framework has now been developed to classify the first two palindromic properties with more precision.

Unfortunately, as far as the author knows, punctuation and capitalization are syntactic bearers of semantic meaning that cannot be reduced to purely formal considerations. Both punctuality and case require additional axioms to describe the unique structuring they impose on a Language and its Corpus. In the author's opinion, it is impossible to disentangle these linguistic phenomenon from the realm of semantics.

In what follows, two things are implicitly assumed. These assumptions are made explicit here, so the scope of the results can be properly understood. First, the Alphabet **Σ** is assumed to contain no punctuation marks beyond the Delimiter Character (if one is inclined it to consider a form of punctuation). Second, it is assumed every Character in **Σ** is distinct, meaning all matters of case are ignored. To rephrase the same idea more precisely: there is no assumed semantic relation between Characters in the Alphabet that would allow the identification of distinct Characters as different *cases* of the same Character.

With these assumptions, the analysis is confined to the dimensions of *aspect* and *parity*, which will be defined in the following subsections. After the results are derived, consideration will be given to future work that could potentially integrate semantic considerations into the formal framework of palindromic structures to account for the dimensions of punctuality and case, in addition to symmetries above the Sentence level that might be incorporated into the conditions for Palindromes.

Section IV.I: Definitions
-------------------------

The current analysis now turns towards its culmination, using the notions that have been developed up to this point to define the mathematical structure of Palindromes. To motivate the next definition, consider how the operation of *σ*-reduction "*projects*" Palindromes onto an Alphabet where their symmetry is preserved.

Consider a Perfect Palindrome like *ᚠ = "strap on no parts"*,

    ς(ᚠ)= "straponnoparts"

    inv(ς(ᚠ)) = "straponnoparts"

In other words, the *σ*-reduction and the inversion of its *σ*-reduction projection result in the same String.

Consider an Imperfect Palindrome like *ᚢ = "borrow or rob"*,

    ς(ᚢ) = "borroworrob"

    inv(ς(ᚢ)) = "borroworrob"

Again, the *σ*-reduction eliminates the Delimiters, and the inversion of the *σ*-reduction captures the mirrored relationship between the words, even if the exact Character sequence isn't identical to the original Palindrome. Nevertheless, the *order* of the Characters is preserved. 

These examples lead directly to the next, important definition.

**Definition 3.2.1: Palindromes**

Palindromes are defined as the set of Sentences **P** that satisfy the following formula,

    ∀ ζ ∈ C:sub:`L`: ζ ∈ P ↔ (ς(ζ) = inv(ς(ζ))) ∎

This definition distills the core property of Palindromes, their symmetrical nature, by focusing on the sequence of Characters without the ambiguity of Delimiters. The use of set notation and logical operations provides a mathematically rigorous and unambiguous definition. Moreover, this definition can be easily adapted to different languages by simply defining the appropriate Alphabet **Σ** and the corresponding *σ-reduced* alphabet **Σ**:sub:`σ`

Definition 3.2.1 highlights the core feature of Palindromes: invariance under transformation. A Palindrome remains a Palindrome even when projected onto the *σ-reduced* Alphabet, demonstrating a structural integrity that's independent of the specific Alphabet that is used to represent it.

The condition *ς(ζ) = inv(ς(ζ)) = ς(inv(ζ))*, where the last equality follows from Theorem 3.1.1, can be seen as defining an equivalence relation on the set of Sentences, where Sentences are equivalent if inversion and *σ*-reduction *commute* over them.

This definition highlights that Palindromes possess a structure that is preserved even under the transformation of *σ*-reduction, demonstrating that their palindromic nature is not dependent on the presence of Delimiters. Moreover, it suggests Palindromes are an artifact of a *"hidden"* algebraic structure embedded into linguistics.

Aspect
^^^^^^

The first classification of Palindromes is now introduced.

**Definition 3.2.2: Perfect Palindromes**

Perfect Palindromes are defined as the set of Sentences **PP** that satisfy the following formula,

    ∀ ζ ∈ C:sub:`L`: ζ ∈ PP ↔ ζ = inv(ζ) ∎

Note the name given to this class of Sentences is premature. While the terminology will prove to be accurate, at this point in the analysis, one must be careful not to confuse Perfect Palindromes with Palindromes. It has not yet been shown the class of Sentences which satisfy Definition 3.2.2 also satisfy 3.1.3. Before moving onto this verification, the motivation for Definition 3.2.2 will briefly be explained.

Definition 3.2.2 implicitly captures the Character-level symmetry that's characteristic of Perfect Palindromes. If a Sentence is its own inverse, it means that the sequence of Characters reads the same backward as forward. It also implicitly captures the Word-level symmetry, as the inversion operation takes into account the reversal of Words within the Sentence, by Theorems 2.3.9 - 2.3.11. A Perfect Palindrome is a confluence of symmetries, a *"singularity"* of reflected inversion at every level of the linguistic hierarchy.

The following theorems will be used to validate the proposed class **PP** does indeed satisfy Definition 3.2.1, and thus Perfect Palindromes are a subset of the class of Palindromes in any Language and its Corpus.

**Theorem 3.2.1** PP ⊂ K

In natural language, this theorem can be stated as follows: Perfect Palindromes are a subset of the Invertible Sentences in a Corpus. 

Assume *ζ* is arbitrary Sentence in **C**:sub:`L` such that,

    1. ζ ∈ PP

This means *ζ* is a Perfect Palindrome, so by Definition 3.2.2, 

    2. ζ = inv(ζ).

Since *ζ* is a Perfect Palindrome, it is also a Sentence, and therefore,

    3. ζ ∈ C:sub:`L`
    
Because *ζ = inv(ζ)* and *ζ ∈* **C**:sub:`L`, it follows,

    4. inv(ζ) ∈ C:sub:`L`.

By Definition 2.3.2 of Invertible Sentences, 

    5. inv(ζ) ∈ C:sub:`L` ↔ ζ ∈ K

Therefore, 

    6. ζ ∈ PP → ζ ∈ K. 
    
This in turn implies,

    7. PP ⊂ K ∎

The connection between Invertible Sentences and Palindromes is thus established with Theorem 3.2.1. All Perfect Palindromes are Invertible Sentences, but not all Invertible Sentences are Perfect Palindromes. This in turn leads to the next two theorems which demonstrate the connection between Palindromes and Invertible Words. 

**Theorem 3.2.2** ∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})

This theorem can be stated in natural language as follows: If a Sentence is a Perfect Palindrome, then the *i*:sup:`th` Word of its Inverse is the Inverse of the Sentence's *Λ(ζ) - i + 1*:sup:`th` Word. 

Let ζ be an arbitrary Sentence in the Corpus such that it is a Perfect Palindrome,

    1. ζ ∈ PP

By Theorem 3.2.1 

    1. PP ⊂ K

By Theorem 2.3.9,

    ∀ i ∈ N:sub:`Λ(ζ)`: inv(ζ){i} = inv(ζ{Λ(ζ) - i + 1})  ∎

**Theorem 3.2.3** ∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I

This theorem can be stated in natural language as follows: If a Sentence is a Perfect Palindrome, then all of its Words are Invertible. 

Recall the definition of a subset,

    1. A ⊂ B ↔ (∀ x: x ∈ A → x ∈ B)

Applying this definition to Theorem 3.2.1, 
    
    2. ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → ζ ∈ K

From Theorem 2.3.11, it is known the consequent of this conditional implies the following,

    3. ∀ ζ ∈ C:sub:`L`: ζ ∈ K → (∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I)

Recall the tautology of *Hypothetical Syllogisms*, for any propositions *p*, *q* and *r*,

    4. ( p → q ∧ q → r ) → (q → r)

Applying this tautological law to step 2 and step 3,

    5. ∀ ζ ∈ C:sub:`L`: ζ ∈ PP → (∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I)

This can be rewritten using the rules of quantifiers,

    6. ∀ ζ ∈ PP: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ∈ I

Which is what was to be shown. ∎ 

It is now shown using the previous theorems that Perfect Palindromes are in fact a subset of the set that implicitly satisfies Definition 3.2.1.

**Theorem 3.2.4**  PP ⊂ P

Assume *ζ* is arbitrary Sentence in **C**:sub:`L` such that,

    1. ζ ∈ PP 
    
This means *ζ* is a Perfect Palindrome, so by Definition 3.2.2, 

    2. ζ = inv(ζ).

Applying a *σ*-reduction to both sides of the equation,

    3. ς(ζ) = ς(inv(ζ))

By Theorem 3.1.1, 

    4. ς(inv(ζ)) = inv(ς(ζ))

Combining steps 3 and 4, 

    5. ς(ζ) = inv(ς(ζ))

Step 4 exactly satisfies the condition for *ζ* to be a Palindrome according to Definition 3.2.1. Therefore, 

    6. ζ ∈ P.

Since *ζ* was an arbitrary Perfect Palindrome, it been shown that,

    7. ζ ∈ PP → ζ ∈ P
    
This in turn implies,

    8. PP ⊂ P ∎

Now that Perfect Palindromes have been shown to satisfy Definition 3.2.1, it is a simple matter of defining Imperfect Palindromes as those Palindromes which are *not* Perfect.

**Definition 3.2.3: Imperfect Palindromes**

Imperfect Palindromes are defined as the set of Sentences **IP** that satisfy the following open formula,

    ζ ∈ P - PP ∎

Definition 3.2.3 is not an explicit definition. It does not say how the class of Imperfect Palindromes are constructed. It only says those Palindromes which are not their own Inverses in the Corpus (i.e. are not Perfect) can have their symmetry under inversion preserved by a reduction to the *σ*-reduced Alphabet. 

This gives a way of identifying Sentences such as *ᚠ = "to oscillate metallic soot"* and *ᚢ = "rats live on no evil star"* as representatives of the same class, namely Palindromes, but with different *aspects*. *ᚢ* is Perfect, while *ᚠ* requires a *σ*-reduction. 

**Theorem 3.2.5** PP ∪ IP = P

Follows immediately from Theorem 3.2.4, Definition 3.2.3, and the fact that PP and IP are disjoint (by the definition of set difference). ∎

Since PP and IP are non-overlapping by Definition 3.2.3 and their union encompasses the entire class of Palindromes by Theorem 3.2.3, these two sets form a partition of the class of Palindromes. The following definition and terminology is introduced to help describe this partitioning.

**Definition 3.2.4: Aspect**

A Palindrome ζ is said to have a *perfect aspect* or *be perfect* if and only if,

    ζ ∈ PP 

A Palindrome ζ is said to have an *imperfect aspect* or *be imperfect* if and only if,

    ζ ∈ IP ∎

Thus, the first partitioning of the class of Palindromes has been discovered. The next section will detail the second partitioning of Palindromes: *parity*.

Parity
^^^^^^

One partitioning, or dimension, of Palindromes has been introduced through the concept of *aspect*. A Palindrome can either be perfect or imperfect, but not both. In this section, the definitions and theorems for uncovering the second partitioning of Palindromes, *parity*, will be developed.

In order to develop the notion of parity, a formal method of referring to the *left* and *right* halves of a Sentence must be introduced. This new notation can be seen as an extension of Character Index Notation introduced in Definition 1.1.5.

**Definition 3.2.5: Left Partial Sentence**

Let ζ be a Sentence in C:sub:`L` with Character-level representation **Z**,

    Z  = (ⲁ:sub:`1` , ⲁ:sub:`2` , ... , ⲁ:sub:`l(ζ)`).

Let *n* be a fixed natural number such that *1 ≤ n ≤ l(ζ)*. A Left Partial Sentence of the *n*:sup:`th` Character, denoted *ζ[:n]*, is formally defined as the sequence of Characters which satisfies, 

    Z[:n] = (ⲁ:sub:`1` , ⲁ:sub:`2` , ... , ⲁ:sub:`n`)  

When *n = 0*, *ζ[:0]* is defined as the empty string, *ε*.

When *n = l(ζ)*, *ζ[:n]* is the entire sentence *ζ*. ∎

**Definition 3.2.6: Right Partial Sentence**

Let ζ be a Sentence in C:sub:`L` with Character-level representation **Z**,

    Z  = (ⲁ:sub:`1` , ⲁ:sub:`2` , ... , ⲁ:sub:`l(ζ)`).

Let *n* be a fixed natural number such that *1 ≤ n ≤ l(ζ)*. A Right Partial Sentence of the *n*:sup:`th` Character, denoted *ζ[n:]*, is formally defined as the String which satisfies, 

    ζ[n:] = (ⲁ:sub:`n`, ⲁ:sub:`n+1`, ..., ⲁ:sub:`l(ζ)`)

where n is a natural number such that 1 ≤ n ≤ l(ζ) + 1.

When n = 1, ζ[1:] is the entire sentence ζ.

When n = l(ζ) + 1, ζ[n:] is defined as the empty string, ε. ∎

**Example**

Consider the Sentence *ᚠ = "form is the possibility of structure"*. Note, *l(ᚠ) = 36* and *Λ(ᚠ) = 6*. Then, 

    1. ᚠ[:2] = "fo"
    2. ᚠ[2:] = "orm is the possibility of structure"
    3. ᚠ[:4] = "form"
    4. ᚠ[10:] = "he possibility of structure" ∎

The notation *ζ[n:]* and *Z[:n]* is analogous to array slicing notation found in many programming languages. It indicates a substring is being taken starting from a position *n* Characters from the one end of the String up to the other end of the String, the direction depending on whether the Partial Sentence is Left or Right.

Take note, Partial Sentences are not necessarily a Word or a sequence of Words. A Left Partial Sentence will only be semantically coherent if the Character at *n* is a Delimiter, if the Character at *n* is the last Character of a Word or Sentence, or if the Partial Sentence "slices" a compound Word at exactly the correct position in Word. Simarily, a Right Partial Sentence will only be semantically coherent if *n* is the first Character in a Word or Sentence, or if the index slices a compound Word. 

Note, regardless of the value of *n*,

    l(ζ[:n]) = n

    l(ζ[n:]) = l(ζ) - n + 1

This relation bears a similarity to Definition 1.2.4 of String Inversion and Definition 1.3.1 of Reflective Words, both of which require Character-level inversions,

    α[i] = α[l(α) - 1 + 1]

A Palindrome is a type of inversion. In a Palindrome, the requirement that individual Characters must maintain their symmetry across its String Length is extended up to the Sentence level through the requirement that, based on the parity of the Palindrome, the Partial Sentences on either side of the Sentence's center must be mirror images of one another. 

Note that Definition 3.2.5 and Definition 3.2.6 are given in terms of Sentences because they will be applied primarily to Sentences, but there is nothing inherently in the definitions which prevents the Partial Notation from being applied to Strings that have been stripped of their Empty Characters via the Emptying Algorithm for the construction of their Character-level representation (Definition 1.1.2). In other words, Definition 3.2.5 and Definition 3.2.6 operate on a String's Character-level representation, not the String itself. This is an important distinction to be made (one that must be made for Character Index Notation and Word Index Notation as well). Partial Sentences (and Character Index Notation and Word Index Notation) are abstractions defined on a representation of a String that has been processed through the Emptying and Delimiting Algorithm.

The next two theorems leverage this insight and establish the fundamental relationship between Left and Right Partial Sentences. In addition, they prove the existence of a natural number that acts as the mid-point of the Sentence's String Length. This in turn will allow for a definition of a Sentence's *Pivot* as the center of a Sentence.

**Theorem 3.2.6** ∀ ζ ∈ C:sub:`L`:  ∀ i ∈ N:sub:`l(ζ)`: inv(ζ)[:i] = ζ[l(ζ) - i + 1:]

Let *ζ* be an arbitrary Sentence in the Corpus,

    1. ζ ∈ C:sub:`L`

Let *i* be a natural number such that,

    2. i ∈ N:sub:`l(ζ)`

By Definition 1.2.4 of String Inversion, the Inverse of *ζ*, denoted *inv(ζ)*, is formed by reversing the order of the Characters in *ζ*.

By Definition 3.2.5, the Left Partial Sentence of *inv(ζ)* up to index i, denoted *inv(ζ)[:i]*, consists of the first *i* characters of *inv(ζ),

    3. inv(ζ)[:i] = (inv(ζ)[1], inv(ζ)[2], ..., inv(ζ)[i])

By Definition 1.2.4, for any Character index j in inv(ζ):

    4. inv(ζ)[j] = ζ[l(ζ) - j + 1]

Applying this to each Character in inv(ζ)[:i], we get:

    5. inv(ζ)[:i] = (ζ[l(ζ)], ζ[l(ζ) - 1], ..., ζ[l(ζ) - i + 1])

Now, consider the Right Partial Sentence of *ζ* starting at index *l(ζ) - i + 1*, denoted *ζ[l(ζ) - i + 1:]*. By Definition 3.2.6, this consists of the characters from index *l(ζ) - i + 1* to the end of *ζ*,

    6. ζ[l(ζ) - i + 1:] = (ζ[l(ζ) - i + 1], ζ[l(ζ) - i + 2], ..., ζ[l(ζ)])

Notice that the sequence of Characters in *inv(ζ)[:i]* (from step 4) is the reverse of the sequence of Characters in *ζ[l(ζ) - i + 1:]* (from step 5).

Since *inv(ζ)* is the Inverse of *ζ*, the Characters in these two sequences are identical, just in reverse order.

Therefore, *inv(ζ)[:i]* and *ζ[l(ζ) - i + 1:]* have the same Characters in the same order. Furthermore, 

    7. l(inv(ζ)[:i]) = i
    8. l(ζ[l(ζ) - i + 1:]) = l(ζ) - (l(ζ) - i + 1) + 1 = i

Therefore, by definition 1.1.4 means they are equivalent as Strings,

    9. inv(ζ)[:i] = ζ[l(ζ) - i + 1:]

Since ζ and i were arbitrary, this can generalize over the Corpus, 

    10.  ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`l(ζ)`: inv(ζ)[:i] = ζ[l(ζ) - i + 1:] ∎

**Theorem 3.2.7** ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i + 1) ∧ (l(ζ[:i+1]) = l(ζ[i+1:]))

This theorem can be stated in natural language as follows: For any Sentence in the Corpus, its String Length is odd if and only if the String Length of the Left Partial Sentence of Length *i+1* is equal to the String Length of the Right Partial Sentence starting at index *i+1*.

(→) Let ζ be an arbitrary sentence in C:sub:`L` with odd length,

    1. ∃ i ∈ ℕ: l(ζ) = 2i + 1

Let

    2. n = i + 1. 

Since *i* is a natural number, *n* is also a natural number (by the property of integer succession). From step 1 and step 2, it follows

    3. 1 ≤ n ≤ l(ζ)

Thus, 

    4. n ∈ N:sub:`l(ζ)`.

The Left Partial Sentence of String Length *n* is then given by,

    5. ζ[:n] = ζ[:i+1]
    
By Definition 3.2.5 of Left Partial Sentences, 

    6. l(ζ[:i+1]) = i + 1.

The Right Partial Sentence is given by,

    7. ζ[n:] = ζ[i+1:]
    
By the definition of Right Partial Sentences, 

    8. l(ζ[i+1:]) = l(ζ) - n + 1 = (2i + 1) - (i + 1) + 1 = i + 1

Therefore, 

    9. l(ζ[:i+1]) = l(ζ[i+1:]) = i + 1.

From this it follows, 

    10. ∃ i ∈ N:sub:`l(ζ)`: (l(ζ[:i+1]) = l(ζ[i+1:])).

(←) Let *ζ* be an arbitrary sentence in **C**:sub:`L` such that,

    1. ∃ 1 ∈ N:sub:`l(ζ)`: (l(ζ[:i+1]) = l(ζ[i+1:])).

By the Definitions 3.1.7 and 3.1.8,

    2. l(ζ[:i+1]) = i+1

    3. l(ζ[i+1:]) = l(ζ) - (i+1) + 1

Putting step 1, step 2 and step 3 together, 

    4. i+1 = l(ζ) - (i+1) + 1

From which it follows algebraically, 

    5. l(ζ) = 2n + 1.

Therefore l(ζ) is odd. Putting both directions of the proof together and generalizing over all Sentences in the Corpus,

    6. ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i + 1 ) ∧ (l(ζ[:i+1]) = l(ζ[i+1:]))  ∎

**Theorem 3.2.8** ∀ ζ ∈ C:sub:`L`: ∃ i ∈ ℕ: (l(ζ) = 2i) ∧ (l(ζ[:i]) + 1 = l(ζ[i:]))

This theorem can be stated in natural language as follows: For any Sentence in the corpus, its String Length is even if and only if the String Length of the Left Partial Sentence of Length *i* plus 1 is equal to the String Length of the Right Partial Sentence starting at index *i*.

(→) Let *ζ* be an arbitrary sentence in **C**:sub:`L` such that there exists a natural number *i* with the following condition,
 
    1. l(ζ) = 2i.

Then let,

    2. n = i. 

Since *i* is a natural number, it follows from step 2 that,

    3. 1 ≤ n ≤ l(ζ)

From which it follows, 

    4. n ∈ N:sub:`l(ζ)`

The Left Partial Sentence of String Length *n* is then given by,

    5. ζ[:n] = ζ[:i]

By Definition 3.2.5, 

    6. l(ζ[:i]) = i

The Right Partial Sentence is given by,

    7. ζ[n:] = ζ[i:].

By Definition 3.2.6, 

    8. l(ζ[i:]) = l(ζ) - i + 1 = 2i - i + 1 = i + 1

Therefore, 

    9. l(ζ[:n]) + 1 = l(ζ[n:]) = i + 1

This shows found an *n* (specifically, *n = i*) exists such that 

    10. l(ζ[:n]) + 1 = l(ζ[n:])

Therefore, 

    11. ∃ n ∈ N:sub:`l(ζ)`: (l(ζ[:n]) + 1 = l(ζ[n:]))

(←) Let *ζ* be an arbitrary sentence in C:sub:`L` such that, 

    1. ∃ n ∈ N:sub:`l(ζ)`: (l(ζ[:n]) + 1 = l(ζ[n:]))

By Definition 3.2.5 and Definition 3.2.6,

    2. l(ζ[:n]) = n
    3. l(ζ[n:]) = l(ζ) - n + 1

Combining step 1, step 2 and step 3, 

    4. n + 1 = l(ζ) - n + 1

Solving for l(ζ),

    5. l(ζ) = 2n

Thus, l(ζ) is even. Since both directions of the implication hold, it can be concluded,

    ∀ ζ ∈ C:sub:`L`: (∃ i ∈ ℕ: l(ζ) = 2i) ↔ (∃ n ∈ N:sub:`l(ζ)`: (l(ζ[:n]) + 1 = l(ζ[n:]))) ∎

**Theorem 3.2.9** ∀ ζ ∈ C:sub:`L`: ∃ n ∈ N:sub:`l(ζ)`: (l(ζ[:n]) = l(ζ[n:])) ∨ (l(ζ[:n]) + 1 = l(ζ[n:]))

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus, there exists a natural number *n* (between *1* and the length of *ζ*, inclusive) such that either the String Length of its Left Partial Sentence is equal to the String Length of its Right Partial Sentence, or the String Length of the Left Partial Sentence is one more than the String Length of the Right Partial Sentence.

Let ζ be an arbitrary sentence in C:sub:`L`. Let,

    1. l(ζ) = k

If k is even, let 

    2. n = k/2

Then 

    3. l(ζ[:n]) = n = k/2

And 

    4. l(ζ[n:]) = k - n + 1 = k - k/2 = (k + 1)/2

Therefore, 

    5. l(ζ[:n]) + 1 = l(ζ[n:])

If k is odd, let 

    6. n = (k + 1)/2

Then 

    7. l(ζ[:n]) = n = (k + 1)/2

And 

    8. l(ζ[n:]) = k - n  + 1 = k - (k + 1)/2  + 1= (k - 1)/2 + 1 = (k + 1)/2

Therefore, 

    9. l(ζ[:n]) = l(ζ[n:])

In both cases, an *n* has been found that satisfies the condition in the theorem. Since *ζ* was an arbitrary Sentence, this can generalize over the Corpus,

    10. ∀ ζ ∈ C:sub:`L`: ∃ n ∈ N:sub:`l(ζ)`: ( l(ζ[:n]) = l(ζ[n:]) ) ∨ ( l(ζ[:n]) + 1 = l(ζ[n:]) ) ∎

Theorems 3.2.7 - 3.2.9 conjunctively establish the existence of a natural number that can reliably be called the center, or *Pivot*, of any Sentence in a Corpus. This leads to the following definition. 

**Definition 3.2.7: Pivots** 

The Pivot of a Sentence *ζ*, denoted *ω(ζ)*, is defined as the natural number such that the following formula is true,

   (l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) ) ∨ (l(ζ[:ω(ζ)]) + 1 = l(ζ[ω(ζ):])) 
   
Using Theorem 3.2.7 and Theorem 3.2.8, the explicit formula for a Sentence Pivot are given below,

    - If l(ζ) is odd, then ω(ζ) = i + 1, where i is the natural number satisfying l(ζ) = 2i + 1.
    - If l(ζ) is even, then ω(ζ) = i, where i is the natural number satisfying l(ζ) = 2i. ∎

The following example shows the relationship between Partial Sentences and Pivots.

**Example**

Consider these simple examples from a hypothetical Language **L** with Alphabet *Σ = { "a", "b", "c", " ", "" }*,

|    ζ          | l(ζ) | ω(ζ) | ζ[:ω(ζ)]   | l(ζ[:ω(ζ)]) | ζ[ω(ζ):]    | l(ζ[ω(ζ):]) |
| ------------- | ---- | ---- | ---------- | ----------- | ----------- | ----------- |
| "a"           | 1    | 1    | "a"        | 1           | "a"         | 1           |
| "aa"          | 2    | 1    | "a"        | 1           | "aa"        | 2           |
| "aba"         | 3    | 2    | "ab"       | 2           | "ba"        | 2           |
| "abba"        | 4    | 2    | "ab"       | 2           | "bba"       | 3           |
| "abcba"       | 5    | 3    | "abc"      | 3           | "cba"       | 3           |
| "abccba"      | 6    | 3    | "abc"      | 3           | "ccba"      | 4           |
| "abbcbba"     | 7    | 4    | "abbc"     | 4           | "cbba"      | 4           |
| "abbccbba"    | 8    | 4    | "abbc"     | 4           | "ccbba"     | 5           |
| "abbbcbbba"   | 9    | 5    | "abbbc"    | 5           | "cbbba"     | 5           |
| "abbbccbbba"  | 10   | 5    | "abbbc"    | 5           | "ccbbba"    | 6           |
| "a a"         | 3    | 2    | "a "       | 2           | " a"        | 2           |
| "a ba"        | 4    | 2    | "a "       | 2           | " ba"       | 3           |
| "ab cb"       | 5    | 3    | "ab "      | 3           | " cb"       | 3           |
| "a bca"       | 5    | 3    | "a b"      | 3           | "bca"       | 3           |
| "a bbc  a"    | 8    | 4    | "a bb"     | 3           | "bc  a"     | 5           | ∎

In the previous example, take note when the Sentence String Length is even, the Right Partial Sentence accumulates an extra Character relative to the Left Partial Sentence, in accordance with Theorem 3.2.9. Similarly, when the Sentence String Length is odd, the Left Partial Sentence is equal in String Length to the Right Partial, in accordance with Theorem 3.2.8. 

With the notion of a Palindromic Pivot established, the class of Even and Odd Palindromes is now defined. 

**Definition 3.2.8: Even Palindromes**

The class of Even Palindromes, denoted **P**:sup:`+`, is defined as the set of Sentences ζ which satisfy the following open formula,

    ζ ∈ P:sup:`+` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k )] ∎

**Definition 3.2.9: Odd Palindromes**

The class of Even Palindromes, denoted **P**:sup:`-`, is defined as the set of Sentences ζ which satisfy the following open formula,

    ζ ∈ P:sup:`-` ↔ [ (ζ ∈ P) ∧ (∃ k ∈ ℕ : l(ζ) = 2k + 1) ] ∎

The *parity* (to be defined shortly, after it is proved Even and Odd Palindromes partition the class of Palindromes) manifests in a Palindrome's behavior around it's Pivot. This behavior around the Pivot will be important for establishing the various cases of the theorems proved in the next section. The key insight is recognizing, as the previous example shows, the String Length of the Right Partial Sentence for Sentences of odd String Length is always one more than the String Length of the Left Partial Sentence, while the Left and Right Partial are of equal String Length when the String Length of the Sentence is even.

**Theorem 3.2.10** ∀ ζ ∈ C:sub:`L`: (∃ k ∈ ℕ : l(ζ) = 2k + 1) ↔ ω(ζ) = (l(ζ) + 1)/2

( → ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

    1. ∃ k ∈ ℕ : l(ζ) = 2k + 1

From Theorem 3.2.7 and step 1, it follows 

    2. n = i + 1 
    
Where *n* satisfies,

    3. l(ζ[:n]) = l(ζ[n:]).

Therefore, 

    4. n = i + 1 = (2i + 1 + 1)/2 = (l(ζ) + 1)/2.

By Definition 3.2.7, the pivot *ω(ζ)* is the smallest natural number satisfying the condition. Since *n* satisfies the condition and is the only solution, it must be the smallest. Therefore, 

    5. ω(ζ) = (l(ζ) + 1)/2.

( ← ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

    1. ω(ζ) = (l(ζ) + 1)/2.

This can be re-arranged to yield,

    2. l(ζ)  = 2 * ω(ζ) - 1

Since *ω(ζ)* is defined to be a natural number, let *k* be,

    3. k = ω(ζ) + 1

Then, 

    4. l(ζ)  = 2k + 1

Therefore,

    5. ∃ k ∈ ℕ : l(ζ) = 2k + 1

Since both direction of the equivalence are shown, the theorem is proved, 

    6. ∀ ζ ∈ C:sub:`L`: (∃ k ∈ ℕ : l(ζ) = 2k + 1) ↔ ω(ζ) = (l(ζ) + 1)/2 ∎

**Theorem 3.2.11** ∀ ζ ∈ P:sup:`-`: ω(ζ) = (l(ζ) + 1)/2

Assume 

    1. ζ ∈ P:sup:`-`

From Definition 3.2.9, it follows, 

    2. ∃ k ∈ ℕ : l(ζ) = 2k + 1

From Theorem 3.2.10, it follows, 

    3. ω(ζ) = (l(ζ) + 1)/2 ∎

**Theorem 3.2.12** ∀ ζ ∈ C:sub:`L`: (∃ i ∈ ℕ : l(ζ) = 2i) ↔ ω(ζ) = l(ζ)/2

( → ) Let ζ be an arbitrary in **C**:sub:`L` such that,

    1. ∃ i ∈ ℕ : l(ζ) = 2i

By Theorem 3.2.8, 

    2. l(ζ[:i]) + 1 = l(ζ[i:])

From Definition 3.2.5 and Definition 3.2.6, this is equivalent to,


    3. i + 1 = l(ζ) - i + 1

Therefore, 

    4. i = l(ζ)/2.

By Definition 3.2.7, the Pivot *ω(ζ)* is the smallest natural number satisfying the condition. Since *i* satisfies the condition and is the only solution when *l(ζ)* is even, it must be the smallest. Therefore, 

    5. ω(ζ) = l(ζ)/2.

( ← ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

    1. ω(ζ) = l(ζ)/2 

Since by Definition 3.2.7, a Pivot is a natural number, let *i* be a natural number such that,

    i = ω(ζ)

It follows immediately,

    l(ζ) = 2i

Therefore *ζ* is even,

    ∃ i ∈ ℕ : l(ζ) = 2i

Since both directions of the equivalence have been shown, it follows,

    ∀ ζ ∈ C:sub:`L`: ω(ζ) = l(ζ)/2 ∎

**Theorem 3.2.13** ∀ ζ ∈ P:sup:`+`: ω(ζ) = l(ζ)/2

Assume 

    1. ζ ∈ P:sup:`+`

From Definition 3.2.8, it follows, 

    2. ∃ k ∈ ℕ : l(ζ) = 2k

From Theorem 3.2.12, it follows, 

    3. ω(ζ) = l(ζ)/2 ∎

**Theorem 3.2.14** ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = l(ζ[:ω(ζ)]) + l(ζ[ω(ζ):])

Assume *ζ* is an arbtirary Sentence from the Corpus,

    1. ζ ∈ C:sub:`L`

Let *ω(ζ)* be the Pivot of ζ. From Definition 3.2.5 of Left Partial Sentence,

    2. l(ζ[:ω(ζ)]) = ω(ζ)

From Definition 3.2.6 of Right Partial Sentence, 

    3. l(ζ[ω(ζ):]) =  l(ζ) - ω(ζ) + 1

Therefore, 

    4. l(ζ[:ω(ζ)]) + l(ζ[ω(ζ):]) = l(ζ) + 1 
    
Since *ζ* was arbitrary, this can generalize,

    5. ∀ ζ ∈ C:sub:`L`: l(ζ) + 1 = l(ζ[:ω(ζ)]) + l(ζ[ω(ζ):]) ∎

**Theorem 3.2.15** ∀ ζ ∈ C:sub:`L`: ω(ς(ζ)) ≤ ω(ζ) 

Let *ζ* be an arbitrary Sentence in the Corpus. By Theorem 3.1.11,

    1. l(ζ) ≥ l(ς(ζ))

Through algebraic manipulation, this is equivalent to the following,

    2. (l(ζ) + 1)/2 ≥ (l(ς(ζ)) + 1)/2

It is also equivalent to,

    3. l(ζ)/2 ≥ l(ς(ζ))/2

Moreover,

    4. (l(ς(ζ)) + 1)/2 ≥ l(ς(ζ))/2

By Theorems 3.2.11 and 3.2.13, one of the following must be true,

    5. ω(ζ) = (l(ζ) + 1)/2
    6. ω(ζ) = l(ζ)/2

Similarly, it must be the case, one of the following is true,

    7. ω(ς(ζ)) = (l(c(ζ)) + 1)/2
    8. ω(ς(ζ)) = l(ς(ζ))/2

If *ω(ζ) = (l(ζ) + 1)/2*, then *l(ζ)* is odd by Theorem 3.2.10. It follows from step 2 and step 4, that no matter the value of *ω(ς(ζ))*,

    9. ω(ς(ζ)) ≤ ω(ζ)  

If ω(ζ) = l(ζ)/2, then *l(ζ)* is even by Theorem 3.2.12. From step 3, if *ω(ς(ζ)) = l(ς(ζ))/2*, it follows, 

    10.  ω(ς(ζ)) ≤ ω(ζ) 

If *ω(ς(ζ)) = (l(c(ζ)) + 1)/2*, then *l(ς(ζ))* is odd by Theorem 3.2.10. 

Since *l(ς(ζ))* is odd and *l(ζ)* is even, atleast one Delimiter was removed from *ζ* during *σ*-reduction, 

    11. l(ς(ζ)) + 1 ≤ l(ζ).

Therefore, 
    
    12. (l(ς(ζ)) + 1)/2 ≤ l(ζ)/2.

It follows,

    13. ω(ς(ζ)) = (l(ς(ζ)) + 1)/2 ≤ l(ζ)/2 = ω(ζ)

Thus, in all possible cases,

    14. ω(ς(ζ)) ≤ ω(ζ)

Since *ζ* was arbitrary, this can be generalized over the Corpus as,

    15. ∀ ζ ∈ C:sub:`L`: ω(ς(ζ)) ≤ ω(ζ) ∎

These properties of Pivots and Partial Sentences will be necessary to state and prove the main results of the work in the next section. In addition, it will be necessary to know the class of Odd Palindromes and the class of Even Palindromes form a partition of the class of all Palindromes. This result is definitively established in Theorems 3.1.14 - 3.1.15.

**Theorem 3.2.15** P:sup:`+` ∩ P:sup:`-` = ∅

This theorem can be stated in natural language as follows: A Palindrome cannot be both even and odd.

For the sake of contradiction, assume there exists a sentence *ζ* such that 

    1. ζ ∈ P:sup:`+` ∩ P:sup:`-`

This means each of the individual expressions is true,

    2. ζ ∈ P:sup:`+``
    3. ζ ∈ P:sup:`-`

By Definition 3.2.8, it follows from step 2,

    4. ∃ k ∈ ℕ : l(ζ) = 2k

By Definition 3.2.9, it follows from step 3,

    5. ∃ k ∈ ℕ : l(ζ) = 2k + 1

This leads to the contradiction, 

    6. 0 = 1

Therefore, the assumption that ζ is both an Even and Odd Palindrome must be false. From this it follows,

    7. P:sup:`-` ∩ P:sup:`+` = ∅ ∎

**Theorem 3.2.16** P:sup:`-` ∪ P:sup:`+` = P

This theorem can be translated into natural language as follows: All Palindromes are either Even Palindromes or Odd Palindromes. 

(⊆) Let *ζ* be an arbitrary Sentence of the Corpus such that, 

    1. ζ ∈ P:sup:`-` ∪ P:sup:`+`

Which means either of this two cases must obtain, 

    2. ζ ∈ P:sup:`-`
    3. ζ ∈ P:sup:`+`

By Definition 3.2.8, if step 2 obtains, then 

    4. ζ ∈ P

By Definition 3.2.9, if step 3 obtains, then 

    5. ζ ∈ P
   
Therefore, in either case, 

    6. ζ ∈ P

Since ζ was arbitrary, this can generalize as,

    1. ∀ ζ ∈ (P:sup:`-` ∪ P:sup:`+`) → ζ ∈ P
   
This in turn implies,

    8. P:sup:`-` ∪ P:sup:`+` ⊆ P

(⊇) Let ζ be an arbitrary Sentence of the Corpus such that, 

    1. ζ ∈ P 

By the properties of natural numbers, it must be the case that one of the following obtains,

    1. ∃ k ∈ ℕ : l(ζ) = 2k
    2. ∃ k ∈ ℕ : l(ζ) = 2k + 1
   
If step 1 obtains, then by Definition 3.2.8, 
    
    3. ζ ∈ P:sup:`+`

If l(ζ) is odd, then by Definition 3.2.9, 

    4. ζ ∈ P:sup:`-`

Therefore, in either case, 

    5. ζ ∈ P:sup:`+` ∪ P:sup:`-`
   
Since ζ was arbitrary, this generalizes as,

    6. ∀ ζ ∈ P → ζ ∈ (P:sup:`+` ∪ P:sup:`-`)

This implies,

    7. P ⊆ P:sup:`-` ∪ P:sup:`+`
   
Step 8 from the (⊆) direction and taken with step 7 from the (⊇) together imply,

    P:sup:`-` ∪ P:sup:`+` = P ∎

With the partitioning of the class **P** of Sentences in a Corpus, i.e. Palindromes, the notion of *parity* can now be stated precisely in the following definition.

**Definition 3.2.10: Parity** 

A Palindrome ζ is said to have a *even parity* or *be even* if and only if,

    P ∈ P:sup:`+` 
    
A Palindrome ζ is said to have an *odd parity* or *be odd* if and only if,

    P ∈ P:sup:`-` ∎

Now that the two partitioning of Palindromes, aspect and parity, have been precisely defined, the final section of this work requires one more definition to correctly formulate its main results. This definition will allow the structure around a Palindrome's Pivot to be described with precise notation.

**Definition 3.2.11: Pivot Words**

Let *ζ* be a sentence in C:sub:`L` with length *Λ(ζ)*, word-level representation W:sub:`ζ`, and pivot *ω(ζ)*. The left Pivot Word, denoted *ζ{ω-}*, and the right Pivot Word, denoted *ζ{ω+}*, are defined as follows:

**Case 1**: Λ(ζ) = 1

    - ζ{ω-} = ζ{ω+} = ζ{1} = ζ{Λ(ζ)}

**Case 2**: Λ(ζ) > 1 and ζ[ω(ζ)] = σ

    - ζ{ω-} = α:sub:`j`, such that (j, α:sub:`j`) ∈ W:sub:`ζ` and α:sub:`j` is immediately to the left of the Delimiter at ω(ζ).
    - ζ{ω+} = α:sub:`k`, such that (k, α:sub:`k``) ∈ W:sub:`ζ` and k = j + 1.

**Case 3**: Λ(ζ) > 1 and ζ[ω(ζ)] ≠ σ

    - ζ{ω-} = ζ{ω+} = α:sub:`j` such that (j, α:sub:`j`) ∈ W:sub:`ζ` and α:sub:`j` contains the character at position ω(ζ). ∎

The meaning of Pivot Words can be clarified with a few examples. 

**Example**

1. Let *ᚠ = "a b c"*
   
    - l(ᚠ) = 5, ω(ᚠ) = 3, ᚠ[3] = b
    - W:sub:`ᚠ` = {(1, "a"), (2, "b"), (3, "c")}
    - ᚠ{ω-} = "b"
    - ᚠ{ω+} = "B"

2. Let *ᚠ = "abc def"*

    - l(ζ) = 7, ω(ζ) = 4, ζ[4] = σ
    - W:sub:`ζ` = {(1, "abc"), (2, "def")}
    - ζ{ω-} = "abc"
    - ζ{ω+} = "def"

3. Let *ᚠ = "a bc de fg h"*

    - l(ζ) = 12, ω(ζ) = 6, ζ[6] = d
    - W:sub:ζ = {(1, "a"), (2, "bc"), (3, "de"), (4,"fg"), (5, "h")}
    - ζ{ω-} = "de"
    - ζ{ω+} = "de" 

4. Let *ᚠ = "ab cde fg hij"*

    - l(ζ) = 13, ω(ζ) = 7, ζ[6] = σ
    - W:sub:ζ = {(1, "ab"), (2, "cde"), (3, "fg"), (4,"hij")}
    - ζ{ω-} = "dce"
    - ζ{ω+} = "fg"∎

From these simplified examples, it should be clear that a Pivot Word is either the Word which contains the Pivot Character, or it is the pair of Words which surround the Pivot Character (i.e. exactly when the Pivot Character is a Delimiter).

Section III.III: Structures
---------------------------

The following theorems serve as the main result of the current formal system that has been constructed to describe the syntactical structures of Palindromes in any Language. 

**Theorem 3.3.1: The Inverse Postulate** [ (inv(ζ{1}) ⊂:sub:s ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:s ζ{1}) ] ∧ [ (ζ{1} ⊂:sub:s inv(ζ{Λ(ζ)})) ∨ (ζ{Λ(ζ)} ⊂:sub:s inv(ζ{1})) ]

Assume *ζ* is an arbitrary Sentence in the Corpus **C**:sub:`L` such that it is a Palindrome,

    1. ζ ∈ P
    
By Definition 3.2.1,

    2. ς(ζ) = inv(ς(ζ))

By Definition 1.1.4,

    3. l(ς(ζ)) = l(inv(ς(ζ)))

Let,
    
    4. α = ζ{1}
    5. β = ζ{Λ(ζ)} 

By Discovery Axiom W.1, Words do not contain Delimiters, so the *σ*-Reduction of *ζ*, *ς(ζ)*, can be represented as a concatenation of the *σ*-reduced words of *ζ*, with Theorem 3.1.8 and Definition 1.2.8 of Limitations,

    6. ς(ζ) = (ς(α)) (ς(ζ{2})) ... (ς(ζ{Λ(ζ)-1})) (ς(β))

Taking the Inverse of both sides,

    7. inv(ς(ζ)) = inv((ς(α)) (ς(ζ{2})) ... (ς(ζ{Λ(ζ)-1})) (ς(β)))

Applying Theorem 1.2.5 repeatedly,

    8. inv(ς(ζ)) = (inv(ς(β))) (inv(ς(ζ{Λ(ζ)-1}))) ... (inv(ς(ζ{2}))) (inv(ς(α)))

By the Definition of *σ*-reduction, and because *α* and *β* are Words, it follows from the Discovery Axiom W.1,

    9. ς(α) = α
    10. ς(β) = β

Substituting step 9 and step 10 into step 6,

    11. ς(ζ) = (α) (ς(ζ{2})) ... (ς(ζ{Λ(ζ)-1})) (β)

Substituting step 9 and step 10 into step 8,

    12. inv(ς(ζ)) = (inv(β)) (inv(ς(ζ{Λ(ζ)-1}))) ... (inv(ς(ζ{2}))) (inv(α))
   
By step 2, step 11 and step 12 are equal (by definition of Palindromes). Now, since String Length is a natural number, it is either the case, by the trichotomy principle,

    13. l(α) = l(β)
    14. l(α) > l(β)
    15. l(α) < l(β)

If l(α) = l(β), then because inversion preserves String Length,

    16. l(α) = l(inv(β))

And by Definition 1.1.7 of Containment, since *α* and *inv(β)* are the first Words that appear in step 11 and step 12, it follows, 

    17. (α ⊂:sub:`s` inv(β)) ∧ (inv(β) ⊂:sub:`s` α)

And by Definition 1.1.7 of Containment, since *inv(α)* and *β* are the last Words that appear in step 11 and step 12, it follows, 

    18. (inv(α) ⊂:sub:`s` β) ∧ (β ⊂:sub:`s` inv(α))
   
If l(α) > l(β), then 

    19.  l(inv(α)) = l(α) > l(inv(β)) = l(β)

And by Definition 1.1.7 of Containment, since *α* and *inv(β)* are the first Words that appear in step 11 and step 12, it follows, 

    20.   inv(β) ⊂:sub:`s` α

And by Definition 1.1.7 of Containment, since *inv(α)* and *β* are the last Words that appear in step 11 and step 12, it follows,

    21.  β ⊂:sub:`s` inv(α) 

If l(α) < l(β), then 

    22.  l(inv(α)) = l(α) < l(inv(β)) = l(β)

And by Definition 1.1.7 of Containment, since *α* and *inv(β)* are the first Words that appear in step 11 and step 12, it follows, 

    23.  α ⊂:sub:`s` inv(β)

And by Definition 1.1.7 of Containment, since *inv(α)* and *β* are the last Words that appear in step 11 and step 12, it follows,

    24. inv(α)  ⊂:sub:`s` β
   
In all cases, the follow propositions obtain,

    25. (inv(α)  ⊂:sub:`s` β) ∨ (inv(β) ⊂:sub:`s` α)
    26. (α  ⊂:sub:`s` inv(β)) ∨ (β ⊂:sub:`s` inv(α))

Since *ζ* was an arbitrary Palindrome, this can be generalized using the definitions of *α* and *β* from step 4 and step 5.

    27. ∀ ζ ∈ P: [ (inv(ζ{1}) ⊂:sub:s ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:s ζ{1}) ] ∧ [ (ζ{1} ⊂:sub:s inv(ζ{Λ(ζ)})) ∨ (ζ{Λ(ζ)} ⊂:sub:s inv(ζ{1})) ] ∎

**Theorem 3.2.2: The Pivot Postulate** ∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( (inv(ζ{ω-}) ⊂:sub:`s` ζ{ω+}) ∨ (inv(ζ{ω+}) ⊂:sub:`s` ζ{ω-}))

This theorem can be stated in natural language as follows: For every Palindrome, if the Character at the Pivot is a Delimiter, then either the inverse of the left Pivot Word contained in the Right Pivot Word, or the inverse of the Right Pivot Word is contained in the left Pivot Word.

Let ζ be an arbitrary Sentence in the Corpus such that the followign is true,

    1. ζ ∈ P
    2. ζ[ω(ζ)] = σ

By Definitino 3.2.1,

    3. ς(ζ) = inv(ς(ζ))
   
Let 

    4. α = ζ{ω-}
    5. β = ζ{ω+} 

By Theorem 2.2.4 (Λ(ζ) ≥ 1), step 2 and by Definition 3.2.11, there are two possible cases to consider,

**Case 1**: Λ(ζ) = 1

    6. ζ{ω-} = ζ{ω+} = ζ{1} = ζ{Λ(ζ)}

Note,

    7. l(ζ{1}) = l(ζ{Λ(ζ)})

In this case, using the Discovery Axiom W.1,

    8. ς(ζ{1}) = ζ{1}

And 

    9. ς(ζ{Λ(ζ)}) = ζ{Λ(ζ)}

Take the Inverse of step 8,

    10. inv(ς(ζ{1})) = inv(ζ{1})

By step 3, step 10 is equal to step 8, so it follows, 

    11. ζ{1} = inv(ζ{1})

From step 6, it follows, 

    12. ζ{Λ(ζ)} = inv(ζ{Λ(ζ)})

By Definition 1.1.7 of Containment, a String is contained in itself (i.e. let *f(i) = i* in Definition 1.1.7), so it follows, plugging in step 6,

    13. (inv(ζ{ω-}) ⊂:sub:`s` ζ{ω+}) ∧ (inv(ζ{ω+}) ⊂:sub:`s` ζ{ω-})

**Case 2**: Λ(ζ) > 1 and ζ[ω(ζ)] = σ

Using Definition 3.2.11, Let 

    14. ζ{ω-} = α:sub:`j`
    
Such that 

    15. (j, α:sub:`j`) ∈ W:sub:`ζ` 
    
and α:sub:`j` is immediately to the left of the Delimiter at ω(ζ).

Let 
    
    16. ζ{ω+} = α:sub:`k`
    
Such that 

    17. (k, α:sub:`k``) ∈ W:sub:`ζ` 
    
and k = j + 1, where

    18.  W:sub:`ζ` = (α:sub:`1` , ..., ζ{ω-}, ζ{ω+}, ..., α:sub:`n`)

    (Note: it may be the case α:sub:`1` = ζ{ω-} and ζ{ω+} = α:sub:`n` )

Note, by the Reduction Algorithm in Definition 3.1.2

    19. ς(σ) = ε

And by the Discovery Axiom W1 and Definition 3.1.3

    20. ς(ζ{ω+}) = ζ{ω+}
    21. ς(ζ{ω-}) = ζ{ω-}
   
And furthermore, since *ζ[ω(ζ)] = σ*, the Delimiter at the pivot will be removed during σ-reduction. This means that in ς(ζ), the words *ζ{ω-}* and *ζ{ω+}* will be adjacent,

By Theorem 3.1.8,

    22. ς(ζ) = (ς(α:sub:`1`)) ... (ζ{ω-})(ζ{ω+}) ... (ς(α:sub:`n`))

Take the inverse of both sides of step 22 and apply Theorem 1.2.5 repeatedly, 

    23. inv(ς(ζ)) = (ς(α:sub:`n`)) ... (ζ{ω+})(ζ{ω-}) ... (ς(α:sub:`1`))








(inv(α) ⊂:sub:s β) ∨ (inv(β) ⊂:sub:s α)
Substituting Back: Substituting α = ζ{ω-} and β = ζ{ω+}, we get:

(inv(ζ{ω-}) ⊂:sub:s ζ{ω+}) ∨ (inv(ζ{ω+}) ⊂:sub:s ζ{ω-})
Conclusion: Since ζ was an arbitrary palindrome satisfying the premise, we can generalize:

∀ ζ ∈ P: (ζ[ω(ζ)] = σ) → ( (inv(ζ{ω-}) ⊂:sub:s ζ{ω+}) ∨ (inv(ζ{ω+}) ⊂:sub:s ζ{ω-}) )
This completes the proof. ∎













**Theorem: The Perfect Pivot Postulate**

ζ ∈ PP ↔ [∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:`s` α) ∧ (α ∈ R) ] ∨ (ζ[ω(ζ)] = σ)

Theorem (Third Inverse Postulate - Strengthened): ζ ∈ PP ↔ [∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ)

Proof:

(→)  Assume ζ ∈ PP (ζ is a Perfect Palindrome).

Word-level representation: Let W:sub:ζ = (α₁ , α₂ , ..., αₙ) be the Word-level representation of ζ, where n = Λ(ζ).

Pivot: Let ω:sub:ζ be the Pivot of ζ. There are two cases:

Case 1: ω:sub:ζ = σ (Delimiter Pivot). In this case, the condition (ω:sub:ζ = σ) is satisfied, and the right-hand side of the biconditional is true.

Case 2: ω:sub:ζ ≠ σ (Non-Delimiter Pivot).

In this case, the Pivot is a Character within a Word. Let k be the index such that αₖ contains ω:sub:ζ.
Since ζ is a Perfect Palindrome, by Definition 3.2.1, ζ = inv(ζ).
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




Reformulation of the Theorem:

Let's first slightly reformulate the theorem to make it even clearer and more precise:

Theorem 3.2.4:

ζ ∈ PP ↔ [ (∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ (inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω)) ]

Translation: A sentence ζ is a perfect palindrome if and only if one of the following conditions holds:

The character at the pivot index ω(ζ) is contained in a reflective word α that is in the language.
The character at the pivot index ω(ζ) is a delimiter (σ), and the inverse of the left pivot word is contained in the right pivot word, or the inverse of the right pivot word is contained in the left pivot word.
Do I think it's true?

Yes, I believe this reformulated theorem is true and captures a fundamental property of perfect palindromes.

Proof:

(↔) Direction:

Assume ζ ∈ PP.

Definition of Perfect Palindrome: By Definition 3.2.1, ζ = inv(ζ).
Case 1: ζ[ω(ζ)] = σ:
If the character at the pivot is a delimiter, then by the Second Inverse Postulate , we know that ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω ).
Case 2: ζ[ω(ζ)] ≠ σ:
If the character at the pivot is not a delimiter, then it must belong to a word.
By Axiom S.2, we know there's at least one word α in ζ.
Since ζ is a perfect palindrome, and the pivot character is not a delimiter, the pivot must lie within a word.
Let α be the word such that (x, α) ∈ W:sub:ζ, and ω(ζ) is within the indices of the characters of α in the character-level representation of ζ.
Since ζ is a perfect palindrome, α must be a reflective word (α ∈ R), because any word that spans across the pivot in a perfect palindrome must be its own inverse.
Also, since ω(ζ) is within the indices of α, we know that ζ[ω(ζ)] ⊂:sub:s α.
(←) Direction:

Assume [(∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω ))].

Case 1: ∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)
If there exists a reflective word α in L that contains the character at the pivot, then ζ must be a perfect palindrome. This is because the presence of a reflective word spanning the pivot implies symmetry around the pivot, which is the defining characteristic of a perfect palindrome.
Case 2: ζ[ω(ζ)] = σ ∧ ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω )
If the character at the pivot is a delimiter and either the inverse of the left pivot word is contained in the right pivot word or vice versa, then ζ must be a perfect palindrome. This is because the delimiter at the pivot, combined with the containment relationship between the pivot words, ensures symmetry around the pivot.
Conclusion:

We have shown that if ζ is a perfect palindrome, then either the character at the pivot is contained in a reflective word in the language, or the character at the pivot is a delimiter and the pivot words exhibit the specific containment property. Conversely, if either of these conditions holds, then ζ must be a perfect palindrome.

Therefore:

ζ ∈ PP ↔ [ (∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ ( inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ ( inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω )) ]

∎

Explanation:

(→) Direction: This direction shows that if a sentence is a perfect palindrome, then it must satisfy one of the two conditions related to the pivot character and reflective words or the pivot character and the containment of pivot words.
(←) Direction: This direction shows that if either of the two conditions is met, then the sentence must be a perfect palindrome.
Key Insights:

Reflective Words at the Pivot: This theorem beautifully connects the concept of perfect palindromes to the presence of reflective words at the pivot. It highlights that perfect palindromes can be constructed by having a reflective word at the center or by having the pivot be a delimiter with a specific relationship between the pivot words.
Delimiter as a Pivot: The theorem also incorporates the case where the pivot is a delimiter, which is essential for handling imperfect palindromes that become perfect when delimiters are removed.
Characterization of Perfect Palindromes: This theorem provides a powerful way to characterize and potentially identify perfect palindromes based on their internal structure.





Theorem 3.2.4:

∀ ζ ∈ PP: (∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (α:sub:ζ:sup:-ω ∈ I))

Translation: For every perfect palindrome ζ, either:

There exists a word α in the language L such that the character at the pivot index ω(ζ) is contained in α, and α is a reflective word (α ∈ R), OR
The character at the pivot index ω(ζ) is a delimiter (σ), and the left pivot word is invertible (α:sub:ζ:sup:-ω ∈ I).
Proof:

Let ζ be an arbitrary perfect palindrome in PP.

Definition of Perfect Palindrome: By Definition 3.2.1, ζ = inv(ζ).

Cases based on Parity: We have two cases to consider:

Case 1: ζ has odd length (ζ ∈ P:sup:-)
By Theorem 3.2.3, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]). This means the pivot falls on a character, ζ[ω(ζ)].
Subcase 1: ζ[ω(ζ)] ≠ σ
Since ζ[ω(ζ)] is not a delimiter, it must belong to a word. By Axiom S.1, there exists a word α in L such that α is contained in ζ. Since the pivot character is not a delimiter, it must be part of a word in ζ. Let α be the word such that (x, α) ∈ W:sub:ζ and ω(ζ) is within the indices of the characters of α in the character-level representation of ζ.
Since ζ is a perfect palindrome, and ω(ζ) is the pivot, this word α must be reflective (α ∈ R). Otherwise, the characters in ζ would not be symmetrical around the pivot, and ζ wouldn't be a perfect palindrome.
Therefore, ∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R).
Subcase 2: ζ[ω(ζ)] = σ
Since the pivot character is a delimiter, by Theorem 3.2.3, we know that inv(α:sub:ζ:sup:-ω) ⊂ α:sub:ζ:sup:+ω or inv(α:sub:ζ:sup:+ω) ⊂ α:sub:ζ:sup:-ω.
Since ζ is a perfect palindrome, we have ζ = inv(ζ). This means the words to the left and right of the pivot must be inverses of each other.
Therefore, α:sub:ζ:sup:-ω = inv(α:sub:ζ:sup:+ω).
Since α:sub:ζ:sup:+ω is in L, and α:sub:ζ:sup:-ω is its inverse, by definition of invertible words, α:sub:ζ:sup:-ω ∈ I.
Case 2: ζ has even length (ζ ∈ P:sup:+)
By Theorem 3.2.4, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ) + 1:]) + 1. This means the pivot falls between two characters.
Since ζ is a perfect palindrome, the two characters adjacent to the pivot must be identical (because ζ = inv(ζ)).
By Axiom W.1, these characters cannot be delimiters. Thus, they must belong to a word α that spans across the pivot.
Similar to Case 1, this word α must be reflective (α ∈ R) for ζ to be a perfect palindrome.
Since the two characters adjacent to the pivot are identical and belong to α, we can say that ζ[ω(ζ)] is "contained" in α in the sense that α spans across the pivot.
Therefore, ∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R).
The case where the pivot is a delimiter is covered by our definition of an even-length perfect palindrome.
Conclusion: In all cases, at least one of the two conditions holds. Since ζ was an arbitrary perfect palindrome, we can generalize:

∀ ζ ∈ PP: (∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (α:sub:ζ:sup:-ω ∈ I))
This completes the proof. ∎



**Theorem 3.2.5: The Perfect Parity Postulate**

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

Non-Delimiter Pivot: Since ω:sub:ζ ⊂:sub:s α and α is a Word in the Language, by Axiom W.1 (Discovery Axiom), α cannot contain the Delimiter Character. Therefore, ω:sub:ζ ≠ σ.

Even Palindrome: Since ω:sub:ζ ≠ σ, by the strengthened Third Inverse Postulate, it must be the case that ω:sub:ζ = ε. By Definition 3.2.3, this means ζ ∈ P⁺ (ζ is an Even Palindrome).

Conclusion: We have shown that ζ ∈ PP and ζ ∈ P⁺, which means ζ ∈ PP ∧ ζ ∈ P⁺.

Since we have proven both directions of the implication, the theorem is established:

ζ ∈ PP ∧ ζ ∈ P⁺ ↔ ∃ α ∈ L: (ω:sub:ζ ⊂:sub:s α) ∧ (α ∈ R) ∎

Explanation:

This proof demonstrates the biconditional relationship between a Sentence being both a Perfect Palindrome and an Even Palindrome, and the existence of a Reflective Word containing the Sentence's Pivot.

The proof utilizes the definitions of Perfect Palindromes, Even Palindromes, and Reflective Words, along with the strengthened Third Inverse Postulate and the Discovery Axiom, to analyze the different cases and demonstrate the implications in both directions.






Analysis:

Even Parity: An even-parity palindrome has an even number of words (Λ(ζ) is even).
Imperfect Palindrome: An imperfect palindrome is a palindrome but not a perfect palindrome. This means it cannot be its own inverse (ζ ≠ inv(ζ)), but its σ-reduction is a palindrome (σ_reduce(ζ) = inv(σ_reduce(ζ))).
Delimiter Count: By Theorem 2.4.1, the number of delimiters in a sentence ζ is one less than the number of words: Δ(ζ) = Λ(ζ) - 1. Since Λ(ζ) is even for an even-parity palindrome, Δ(ζ) must be odd.
σ-reduction: σ-reduction removes all delimiters.
Length of σ-reduced Form: The length of the σ-reduced form, l(σ_reduce(ζ)), is the original length of the sentence minus the number of delimiters: l(σ_reduce(ζ)) = l(ζ) - Δ(ζ).
Theorem
∀ ζ ∈ IP ∩ P:sup:+: (l(σ_reduce(ζ)) is odd)

Proof
Let ζ be an imperfect palindrome with even parity, ζ ∈ IP ∩ P:sup:+.
Let n = Λ(ζ) be the number of words in ζ. Since ζ has even parity, n must be even.
By Theorem 2.4.1, Δ(ζ) = n - 1. Since n is even, n - 1 must be odd.
Since ζ is an imperfect palindrome, by the definition of the imperfection, we know:
ζ ≠ inv(ζ)
σ_reduce(ζ) = inv(σ_reduce(ζ))
Since σ_reduce(ζ) = inv(σ_reduce(ζ)), and by Theorem 3.2.3 we know parity is preserved if the length of the left partial at the pivot point is exactly one longer than the right partial, we know the sentence pivot must either fall on a character or a delimiter.
If the pivot falls on a delimiter, then n must be odd by the Second Inverse Postulate. Since n is even, this is impossible.
If the pivot falls on a character, then that character must be a non-delimiter, non-empty character by our definition of a pivot. Since ζ is an imperfect palindrome, this pivot character cannot be part of a reflective word by Theorem 3.2.4. This means it must be part of an invertible word pair by Theorem 3.2.1. The inverse of the pivot character must appear in the inverse word, since it cannot be a reflective word.
By our definition of σ-reduction, σ_reduce(ζ) removes all delimiters, and by Theorem 1.2.4, inversion inverts words. So, for a palindrome, σ_reduce(ζ) = inv(σ_reduce(ζ)) preserves the order of non-delimiter characters under inversion.
Therefore, l(σ_reduce(ζ)) must be odd, as it preserves the non-delimiter pivot character under inversion, and there are an even number of non-delimiter characters around it, (Δ(ζ)).

Conclusion:

Yes, we can conclude that an imperfect palindrome with even parity must have a σ-reduced form with an odd length.

Reasoning:

An even-parity imperfect palindrome has an even number of words.
This implies an odd number of delimiters.
The σ-reduced form has a length equal to the original length minus the number of delimiters: l(σ_reduce(ζ)) = l(ζ) - Δ(ζ).
Since l(ζ) is even (because the number of delimiters is odd, the number of characters must be odd to be a palindrome) and Δ(ζ) is odd, their difference l(σ_reduce(ζ)) must be odd.
Implications:

Constraints on σ-reduced Forms: This result further constrains the possible σ-reduced forms of imperfect palindromes.
Relationship between Parity and Length: It establishes a direct link between the parity of a palindrome (at the word level) and the length of its σ-reduced form (at the character level).
Potential for Simplification: This might help simplify some of our formulas or proofs related to σ-induction, as we now know that even-parity imperfect palindromes will always have odd-length σ-reduced forms.
Further Considerations:

Odd-Parity Imperfect Palindromes: We could investigate the corresponding relationship for odd-parity imperfect palindromes.
Perfect Palindromes: It's worth noting that perfect palindromes don't have this same constraint. A perfect palindrome with even parity can have an even or odd length σ-reduced form.








Section III.III: Palindromic Algorithms
---------------------------------------

The results derived in this work can be used to construct algorithms for searching for various classes of Palindromes. The general outline for one such algorithm is given in this section, and then an example implemention in Python is presented.

A naive algorithm for filtering out Strings that cannot possibly be Palindromes might consist of inverting the strings and comparing them for equality. However, this would miss Palindromes with an imperfect aspect, as their symmetry does not manifest in the unreduced Alphabet. Without a *σ*-reduction, any algorithm that searchs for Palindromic String must be aware of the semantics of the Language in which it is searching. However, *σ*-reduction and the theorems proved over the course of this work allow algorithms to be constructed that are independent of the host Language.

Moreover, as mentioned after the body Theorem 3.1.2, the *σ-reductions* reduce the complexity of searching for Palindromic strings. An Alphabet with less Characters can be traversed quicker. 

To implement this, a String can be projected onto its *σ-reduced* Alphabet, and then those reductiosn whose inverse does not equal itself can be removed from the list of potential Palindromes. To find a String whose inverse does not equal itself, it suffices to find a single Character whose inverted position is not occupied by that Character. 

Therefore, as a first step to generating a list of Palindromes, the Strings which do not satisfy these conditions can be discarded.

Theorem 3.3.1 and Theorem 3.3.2 provide further conditions that any Palindrome must satisfy, reducing the set of potential Palindromes in this hypothetical search algorithm even more. 

With respect to Perfect Palindromes, the search algorithm can be refined even further by incorporating the conditions given in Theorem 3.3.3 and Theorem 3.3.4. Based on the String Length of a Perfect Palindrome, its point of symmetry must possess certain measurable properties, such as the presence of a Reflective Word or an Invertible Word contained by the word opposite the pivot. 

Python Implementation 
^^^^^^^^^^^^^^^^^^^^^

(TODO: code this!)

Section III.IV: Future considerations
-------------------------------------

This work focused on using the operation of sigma reduction to describe palindromic structure in terms of its *aspect* and its *parity*. As mentioned at several points, there are two other dimensions of palindromes this work has not sought to incorporate into formal system. While the considerations in the introduction seem to preclude the possibility of a purely syntactical account of palindromes, the author does not believe this means the structure of palindromes cannot be formalized by taking into account certain universal semantic assumptions. 

To account for the dimension of *punctuality*, a possible avenue of exploration could be extending the operation of sigma reduction to encompass other Characters besides the Delimiter Character. In this way, the punctuality of a palindrome may be "projected" onto a reduced Alphabet where its symmetry under inversion can be recovered.

To account for the dimension of *case*, the link between uppercase and lowercase letters in natural languages may be viewed as inducing a symmetry in the Alphabet that in turn may be exploitable for describing palindromic symmetry. In such a formalization, a possible method of attack would be introduce a many-to-one relationship between in a sigma-reduction where uppercase and lowercase letters are mapped to their "primitive" Character in their reduced space.

(TODO: comment on possibility of interesting recursions, i.e. what happens when the Alphabet of this formal system is assigned the symbols of the formal system itself?)

(TODO: comment on completeness, i.e. what does this formal model of language say about the completeness of language, or its lack thereof?)