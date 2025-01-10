.. _section-iv:

Section IV: Palindromes
=======================

As mentioned in the introduction of this work, the structure of palindromes is described through the combination of four different attributes or dimensions: *aspect*, *parity*, *case* and *punctuality*. The framework has now been developed to classify the first two palindromic properties with more precision.

Unfortunately, as far as the author knows, punctuation and capitalization are syntactic bearers of semantic meaning that cannot be reduced to purely formal considerations. Both punctuality and case require additional axioms to describe the unique structuring they impose on a Language and its Corpus. In the author's opinion, it is impossible to disentangle these linguistic phenomenon from the realm of semantics.

In what follows, two things are implicitly assumed. These assumptions are made explicit here, so the scope of the results can be properly understood. First, the Alphabet **Σ** is assumed to contain no punctuation marks beyond the Delimiter Character (if one is inclined it to consider a form of punctuation). Second, it is assumed every Character in **Σ** is distinct, meaning all matters of case are ignored. To rephrase the same idea more precisely: there is no assumed semantic relation between Characters in the Alphabet that would allow the identification of distinct Characters as different *cases* of the same Character.

With these assumptions, the analysis is confined to the dimensions of *aspect* and *parity*, which will be defined in the following subsections. After the results are derived, consideration will be given to future work that could potentially integrate semantic considerations into the formal framework of palindromic structures to account for the dimensions of punctuality and case, in addition to symmetries above the Sentence level that might be incorporated into the conditions for Palindromes.

The current analysis now turns towards its culmination, using the notions that have been developed up to this point to define the mathematical structure of Palindromes. To motivate the next definition, consider how the operation of *σ*-reduction "*projects*" Palindromes onto an Alphabet where their symmetry is preserved.

Consider a Perfect Palindrome like :math:`ᚠ = \text{"strap on no parts"}`,

.. math::

    \varsigma(ᚠ)= \text{"straponnoparts"}

.. math::

    \text{inv}(\varsigma(ᚠ)) = \text{"straponnoparts"}

In other words, the *σ*-reduction and the inversion of its *σ*-reduction projection result in the same String.

Consider an Imperfect Palindrome like :math:`ᚢ = \text{"borrow or rob"}`,

.. math::

    \varsigma(ᚢ) = \text{"borroworrob"}

.. math::

    \text{inv}(\varsigma(ᚢ)) = \text{"borroworrob"}

Again, the *σ*-reduction eliminates the Delimiters, and the inversion of the *σ*-reduction captures the mirrored relationship between the words, even if the exact Character sequence isn't identical to the original Palindrome. Nevertheless, the *order* of the Characters is preserved. 

These examples lead directly to the next, important definition.

.. _definition-4-1-1:

**Definition 4.1.1: Palindromes**

Palindromes are defined as the set of Sentences **P** that satisfy the following formula,

.. math::

    \forall \zeta \in C_L: \zeta \in P ↔ (\varsigma(\zeta) = \text{inv}(\varsigma(\zeta))) 
    
∎

This definition distills the core property of Palindromes, their symmetrical nature, by focusing on the sequence of Characters without the ambiguity of Delimiters. The use of set notation and logical operations provides a mathematically rigorous and unambiguous definition. Moreover, this definition can be easily adapted to different languages by simply defining the appropriate Alphabet **Σ** and the corresponding *σ-reduced* alphabet **Σ**:sub:`σ`

:ref:`Definition 4.1.1 <definition-4-1-1>` highlights the core feature of Palindromes: invariance under transformation. A Palindrome remains a Palindrome even when projected onto the *σ-reduced* Alphabet, demonstrating a structural integrity that's independent of the specific Alphabet that is used to represent it.

The condition :math:`\varsigma(\zeta) = \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta))`, where the last equality follows from :ref:`Theorem 3.1.1 <theorem-3-1-1>`, can be seen as defining an equivalence relation on the set of Sentences, where Sentences are equivalent if inversion and *σ*-reduction *commute* over them.

This definition highlights that Palindromes possess a structure that is preserved even under the transformation of *σ*-reduction, demonstrating that their palindromic nature is not dependent on the presence of Delimiters. Moreover, it suggests Palindromes are an artifact of a *"hidden"* algebraic structure embedded into linguistics.

.. _section-iv-i:

Section IV.I: Aspect
--------------------

The first classification of Palindromes is now introduced.

.. _definition-4-1-2:

**Definition 4.1.2: Perfect Palindromes**

Perfect Palindromes are defined as the set of Sentences **PP** that satisfy the following formula,

.. math::

    \forall \zeta \in C_L: \zeta \in PP \leftrightarrow \zeta = \text{inv}(\zeta) 
    
∎

Note the name given to this class of Sentences is premature. While the terminology will prove to be accurate, at this point in the analysis, one must be careful not to confuse Perfect Palindromes with Palindromes. It has not yet been shown the class of Sentences which satisfy :ref:`Definition 4.1.2 <definition-4-1-2>` also satisfy :ref:`Definition 4.1.1 <definition-4-1-1>`. Before moving onto this verification, the motivation for :ref:`Definition 4.1.2 <definition-4-1-2>` will briefly be explained.

:ref:`Definition 4.1.2 <definition-4-1-2>` implicitly captures the Character-level symmetry that's characteristic of Perfect Palindromes. If a Sentence is its own inverse, it means that the sequence of Characters reads the same backward as forward. It also implicitly captures the Word-level symmetry, as the inversion operation takes into account the reversal of Words within the Sentence, by :ref:`Theorems 2.3.9 <theorem-2-3-9>` - :ref:`2.3.11 <theorem-2-3-11>`. A Perfect Palindrome is a confluence of symmetries, a *"singularity"* of reflected inversion at every level of the linguistic hierarchy.

The following theorems will be used to validate the proposed class **PP** does indeed satisfy :ref:`Definition 4.1.1 <definition-4-1-1>`, and thus Perfect Palindromes are a subset of the class of Palindromes in any Language and its Corpus.

.. _theorem-4-1-1:

**Theorem 4.1.1** :math:`PP \subset K`

In natural language, this theorem can be stated as follows: Perfect Palindromes are a subset of the Invertible Sentences in a Corpus. 

Assume *ζ* is arbitrary Sentence in **C**:sub:`L` such that,

.. math::

    1. \quad \zeta \in PP

This means *ζ* is a Perfect Palindrome, so by :ref:`Definition 4.1.2 <definition-4-1-2>`, 

.. math::

    2. \quad \zeta = \text{inv}(\zeta).

Since *ζ* is a Perfect Palindrome, it is also a Sentence, and therefore,

.. math::

    3. \quad \zeta \in C_L
    
Because :math:`\zeta = \text{inv}(\zeta)` and :math:`\zeta \in C_L`, it follows,

.. math::

    4. \quad \text{inv}(\zeta) \in C_L.

By :ref:`Definition 2.3.2 <definition-2-3-2>` of Invertible Sentences, 

.. math::

    5. \quad \text{inv}(\zeta) \in C_L \leftrightarrow \zeta \in K

Therefore, 

.. math::

    6. \quad \zeta \in PP \to \zeta \to K. 
    
This in turn implies,

.. math::

    7. \quad PP \subset K 

∎

The connection between Invertible Sentences and Palindromes is thus established with :ref:`Theorem 4.1.1 <theorem-4-1-1>`. All Perfect Palindromes are Invertible Sentences, but not all Invertible Sentences are Perfect Palindromes. This in turn leads to the next two theorems which demonstrate the connection between Palindromes and Invertible Words. 

.. _theorem-4-1-2:

**Theorem 4.1.2** :math:`\forall \zeta \in PP: \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})` 

This theorem can be stated in natural language as follows: If a Sentence is a Perfect Palindrome, then the *i*:sup:`th` Word of its Inverse is the Inverse of the Sentence's *Λ(ζ) - i + 1*:sup:`th` Word. 

Let *ζ* be an arbitrary Sentence in the Corpus such that it is a Perfect Palindrome,

.. math::

    1. \quad \zeta \in PP

By :ref:`Theorem 4.1.1 <theorem-4-1-1>`, 

.. math::

    2. \quad PP \subset K

By :ref:`Theorem 2.3.9 <theorem-2-3-9>`,

.. math::

    3. \quad \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})  

∎

.. _theorem-4-1-3:

**Theorem 4.1.3** :math:`\forall \zeta \in PP: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I`

This theorem can be stated in natural language as follows: If a Sentence is a Perfect Palindrome, then all of its Words are Invertible. 

Recall the definition of a subset,

.. math::

    1. \quad A \subset B \leftrightarrow (\forall x: x \in A \to x \in B)

Applying this definition to :ref:`Theorem 4.1.1 <theorem-4-1-1>`, 

.. math::

    2. \quad \forall \zeta \in C_L: \zeta \in PP \to \zeta \in K

From :ref:`Theorem 2.3.11 <theorem-2-3-11>`, it is known the consequent of this conditional implies the following,

.. math::
    
    3. \quad \forall \zeta \in C_L: \zeta \in K \to (\forall i \in N_{\Lambda(\zeta}`: \zeta\{i\} \in I)

Recall the tautology of *Hypothetical Syllogisms*, for any propositions *p*, *q* and *r*,

.. math::

    4. \quad ( p \to q \land q \to r ) \to (q \to r)

Applying this tautological law to step 2 and step 3,

.. math::

    5. \quad \forall \zeta \in C_L: \zeta \in PP \to (\forall i \in N_{\Lambda(\zeta)}`: \zeta\{i\} \in I)

This can be rewritten using the rules of quantifiers,

.. math::

    6. \quad \forall \zeta \in PP: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I

Which is what was to be shown. ∎ 

It is now shown using the previous theorems that Perfect Palindromes are in fact a subset of the set that implicitly satisfies :ref:`Definition 4.1.1 <definition-4-1-1>`.

.. _theorem-4-1-4:

**Theorem 4.1.4**  :math:`PP \subset P`

Assume *ζ* is arbitrary Sentence in **C**:sub:`L` such that,

.. math::

    1. \quad \zeta \in PP 
    
This means *ζ* is a Perfect Palindrome, so by :ref:`Definition 4.1.2 <definition-4-1-2>` , 

.. math::

    2. \quad \zeta = \text{inv}(\zeta).

Applying a *σ*-reduction to both sides of the equation,

.. math::

    3. \quad \varsigma(\zeta) = \varsigma(\text{inv}(\zeta))

By :ref:`Theorem 3.1.1 <theorem-3-1-1>`, 

.. math::

    4. \quad \varsigma(\text{inv}(\zeta)) = \text{inv}(\varsigma(\zeta))

Combining steps 3 and 4, 

.. math::

    5. \quad \varsigma(\zeta) = \text{inv}(\varsigma(\zeta))

Step 4 exactly satisfies the condition for *ζ* to be a Palindrome according to :ref:`Definition 4.1.1 <definition-4-1-1>`. Therefore, 

.. math::

    6. \quad \zeta \in P

Since *ζ* was an arbitrary Perfect Palindrome, it has been shown that,

.. math::

    7. \quad \zeta \in PP \to \zeta \in P
    
This in turn implies,

.. math::

    8. \quad PP \subset P 

∎

Now that Perfect Palindromes have been shown to satisfy :ref:`Definition 4.1.1 <definition-4-1-1>`, it is a simple matter of defining Imperfect Palindromes as those Palindromes which are *not* Perfect.

.. _definition-4-1-3:

**Definition 4.1.3: Imperfect Palindromes**

Imperfect Palindromes are defined as the set of Sentences **IP** that satisfy the following open formula,

.. math::

    \zeta \in P - PP 

∎

:ref:`Definition 4.1.3 <definition-4-1-3>` is not an explicit definition. It does not say how the class of Imperfect Palindromes are constructed. It only says those Palindromes which are not their own Inverses in the Corpus (i.e. are not Perfect) can have their symmetry under inversion preserved by a reduction to the *σ*-reduced Alphabet. 

This gives a way of identifying Sentences such as :math:`ᚠ = \text{"to oscillate metallic soot"}` and :math:`ᚢ = \text{"rats live on no evil star"}` as representatives of the same class, namely Palindromes, but with different *aspects*. *ᚢ* is Perfect, while *ᚠ* requires a *σ*-reduction. 

.. _theorem-4-1-5:

**Theorem 4.1.5** :math:`PP \cup IP = P``

Follows immediately from :ref:`Theorem 4.1.4 <theorem-4-1-4>`, :ref:`Definition 4.1.3 <definition-4-1-3>`, and the fact that **PP** and **IP** are disjoint (by the definition of set difference). ∎

Since **PP** and **IP** are non-overlapping by :ref:`Definition 4.1.3 <definition-4-1-3>` and their union encompasses the entire class of Palindromes by :ref:`Theorem 4.1.5 <theorem-4-1-5>`, these two sets form a partition of the class of Palindromes. The following definition and terminology is introduced to help describe this partitioning.

**Definition 4.1.4: Aspect**

A Palindrome *ζ* is said to have a *perfect aspect* or *be perfect* if and only if,

.. math::

    \zeta \in PP 

A Palindrome *ζ* is said to have an *imperfect aspect* or *be imperfect* if and only if,

.. math::

    \zeta \in IP 
    
∎

Thus, the first partitioning of the class of Palindromes has been discovered. The next section will detail the second partitioning of Palindromes: *parity*.

.. _section-iv-ii:

Section IV.II: Parity
---------------------

One partitioning, or dimension, of Palindromes has been introduced through the concept of *aspect*. A Palindrome can either be perfect or imperfect, but not both. In this section, the definitions and theorems for uncovering the second partitioning of Palindromes, *parity*, will be developed.

In order to develop the notion of parity, a formal method of referring to the *left* and *right* halves of a Sentence must be introduced. This new notation can be seen as an extension of Character Index Notation introduced in :ref:`Definition 1.1.5 <definition-1-1-5>`.

.. _definition-4-2-1:

**Definition 4.2.1: Left Partial Sentence**

Let *ζ* be a Sentence in C:sub:`L` with Character-level representation **Z**,

.. math::

    \zeta  = (\iota_1 , \iota_2 , ... , \iota_{l(\zeta)}`).

Let *n* be a fixed natural number such that :math:`1 \leq n \leq l(\zeta)`. A Left Partial Sentence of the *n*:sup:`th` Character, denoted :math:`\zeta[:n]`, is formally defined as the sequence of Characters which satisfies, 

.. math::

    \zeta[:n] = (\iota_1 , \iota_2 , ... , \iota_n`)  

When :math:`n = 0`, *ζ[:0]* is defined as the empty string, *ε*.

When :math:`n = l(ζ)`, *ζ[:n]* is the entire sentence *ζ*. ∎

.. _definition-4-2-2:

**Definition 4.2.2: Right Partial Sentence**

Let *ζ* be a Sentence in C:sub:`L` with Character-level representation **Z**,

.. math::

    \zeta  = (\iota_1 , \iota_2 , ... , \iota_{l(\zeta)}).

Let *n* be a fixed natural number such that :math:`1 \leq n \leq l(\zeta)*. A Right Partial Sentence of the *n*:sup:`th` Character, denoted *ζ[n:]*, is formally defined as the String which satisfies, 

.. math::

    \zeta[n:] = (\iota_n, \iota_{n+1}, ..., \iota_{l(\zeta)})

where *n* is a natural number such that 1 ≤ n ≤ l(ζ) + 1.

When :math:`n = 1`, *ζ[1:]* is the entire sentence *ζ*.

When :math:`n = l(ζ) + 1`, *ζ[n:]* is defined as the empty string, *ε*. ∎

**Example**

Consider the Sentence *ᚠ = "form is the possibility of structure"*. Note, *l(ᚠ) = 36* and *Λ(ᚠ) = 6*. Then, 

    1. ᚠ[:2] = "fo"
    2. ᚠ[2:] = "orm is the possibility of structure"
    3. ᚠ[:4] = "form"
    4. ᚠ[10:] = "he possibility of structure" ∎

The notation *ζ[n:]* and *Z[:n]* is analogous to array slicing notation found in many programming languages. It indicates a substring is being taken starting from a position *n* Characters from the one end of the String up to the other end of the String, the direction depending on whether the Partial Sentence is Left or Right.

Take note, Partial Sentences are not necessarily a Word or a sequence of Words. A Left Partial Sentence will only be semantically coherent if the Character at *n* is a Delimiter, if the Character at *n* is the last Character of a Word or Sentence, or if the Partial Sentence "slices" a compound Word at exactly the correct position in Word. Simarily, a Right Partial Sentence will only be semantically coherent if *n* is the first Character in a Word or Sentence, or if the index slices a compound Word. 

Note, regardless of the value of *n*,

.. math::

    l(\zeta[:n]) = n

.. math::

    l(\zeta[n:]) = l(\zeta) - n + 1

This relation bears a similarity to :ref:`Definition 1.2.4 <definition-1-2-4>` of String Inversion and :ref:`Definition 1.3.1 <definition-1-3-1>` of Reflective Words, both of which require Character-level inversions,

.. math::

    \alpha[i] = \alpha[l(\alpha) - 1 + 1]

A Palindrome is a type of inversion. In a Palindrome, the requirement that individual Characters must maintain their symmetry across its String Length is extended up to the Sentence level through the requirement that, based on the parity of the Palindrome, the Partial Sentences on either side of the Sentence's center must be mirror images of one another. 

Note that :ref:`Definition 4.2.1 <definition-4-2-1>` and :ref:`Definition 4.2.2 <definition-4-2-2>` are given in terms of Sentences because they will be applied primarily to Sentences, but there is nothing inherently in the definitions which prevents the Partial Notation from being applied to Strings that have been stripped of their Empty Characters via the :ref:`Emptying Algorithm <algorithm-1>` for the construction of their Character-level representation (:ref:`Definition 1.1.2 <definition-1-1-2>` ). In other words, :ref:`Definition 4.2.1 <definition-4-2-1>` and :ref:`Definition 4.2.2 <definition-4-2-2>` operate on a String's Character-level representation, not the String itself. This is an important distinction to be made (one that must be made for Character Index Notation and Word Index Notation as well). Partial Sentences (and Character Index Notation and Word Index Notation) are abstractions defined on a representation of a String that has been processed through the :ref:`Emptying <algorithm-1>` and :ref:`Delimiting Algorithm <algorithm-2>`.

The next two theorems leverage this insight and establish the fundamental relationship between Left and Right Partial Sentences. In addition, they prove the existence of a natural number that acts as the mid-point of the Sentence's String Length. This in turn will allow for a definition of a Sentence's *Pivot* as the center of a Sentence.

.. _theorem-4-2-1:

**Theorem 4.2.1** :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \text{inv}(\zeta)[:i] = \zeta[l(\zeta)-i+1]`

Let *ζ* be an arbitrary Sentence in the Corpus,

.. math::

    1. \quad \zeta \in C_L

Let *i* be a natural number such that,

.. math::

    2. \quad i \in N_{l(\zeta)}

By :ref:`Definition 1.2.4 <definition-1-2-4>` of String Inversion, the Inverse of *ζ*, denoted *inv(ζ)*, is formed by reversing the order of the Characters in *ζ*.

By :ref:`Definition 4.2.1 <definition-4-2-1>`, the Left Partial Sentence of *inv(ζ)* up to index i, denoted *inv(ζ)[:i]*, consists of the first *i* characters of *inv(ζ)*,

.. math::

    3. \quad \text{inv}(\zeta)[:i] = (\text{inv}(\zeta)[1], \text{inv}(\zeta)[2], ..., \text{inv}(\zeta)[i])

By :ref:`Definition 1.2.4 <definition-1-2-4>`, for any Character index *j* in *inv(ζ)*:

.. math::

    4. \quad \text{inv}(\zeta)[j] = \zeta[l(\zeta) - j + 1]

Applying this to each Character in *inv(ζ)[:i]*, we get:

.. math::

    5. \quad \text{inv}(\zeta)[:i] = (\zeta[l(\zeta)], \zeta[l(\zeta) - 1], ..., \zeta[l(\zeta) - i + 1])

Now, consider the Right Partial Sentence of *ζ* starting at index *l(ζ) - i + 1*, denoted *ζ[l(ζ) - i + 1:]*. By :ref:`Definition 4.2.2 <definition-4-2-2>`, this consists of the characters from index *l(ζ) - i + 1* to the end of *ζ*,

.. math::

    6. \quad \zeta[l(\zeta) - i + 1:] = (\zeta[l(\zeta) - i + 1], \zeta[l(\zeta) - i + 2], ..., \zeta[l(\zeta)])

Notice that the sequence of Characters in *inv(ζ)[:i]* (from step 4) is the reverse of the sequence of Characters in *ζ[l(ζ) - i + 1:]* (from step 5).

Since *inv(ζ)* is the Inverse of *ζ*, the Characters in these two sequences are identical, just in reverse order.

Therefore, *inv(ζ)[:i]* and *ζ[l(ζ) - i + 1:]* have the same Characters in the same order. Furthermore, 

.. math::

    7. \quad l(\text{inv}(\zeta)[:i]) = i
    
.. math::

    8. \quad l(\zeta[l(\zeta) - i + 1:]) = l(\zeta) - (l(\zeta) - i + 1) + 1 = i

Therefore, by :ref:`Definition 1.1.4 <definition-1-1-4>` means they are equivalent as Strings,

.. math::

    9. \quad \text{inv}(\zeta)[:i] = \zeta[l(\zeta) - i + 1:]

Since *ζ* and *i* were arbitrary, this can generalize over the Corpus, 

.. math::

    10.  \quad \forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \text{inv}(\zeta)[:i] = \zeta[l(\zeta) - i + 1:] 

∎

.. _theorem-4-2-2:

**Theorem 4.2.2** :math:`\forall \zeta \in C_L: \exists i \in \mathbb{N}: (l(\zeta) = 2i + 1) \land (l(\zeta[:i+1]) = l(\zeta[i+1:]))`

This theorem can be stated in natural language as follows: For any Sentence in the Corpus, its String Length is odd if and only if the String Length of the Left Partial Sentence of Length *i+1* is equal to the String Length of the Right Partial Sentence starting at index *i+1*.

(→) Let ζ be an arbitrary sentence in C:sub:`L` with odd length,

.. math::

    1. \quad \exists i \in \mathbb{N}: l(\zeta) = 2i + 1

Let

.. math::

    2. \quad n = i + 1. 

Since *i* is a natural number, *n* is also a natural number (by the property of integer succession). From step 1 and step 2, it follows

.. math::

    3. \quad 1 \leq n \leq l(\zeta)

Thus, 

.. math::

    4. \quad n \in N_{l(\zeta)}`.

The Left Partial Sentence of String Length *n* is then given by,

.. math::

    5. \quad \zeta[:n] = \zeta[:i+1]
    
By :ref:`Definition 4.2.1 <definition-4-2-1>` of Left Partial Sentences, 

.. math::

    6. \quad l(\zeta[:i+1]) = i + 1.

The Right Partial Sentence is given by,

.. math::

    7. \quad \zeta[n:] = \zeta[i+1:]
    
By the definition of Right Partial Sentences, 

.. math::

    8. \quad l(ζ[i+1:]) = l(\zeta) - n + 1 = (2i + 1) - (i + 1) + 1 = i + 1

Therefore, 

.. math::

    9. \quad l(\zeta[:i+1]) = l(\zeta[i+1:]) = i + 1.

From this it follows, 

    10. \quad \exists i \in N_{l(\zeta)}: (l(\zeta[:i+1]) = l(\zeta[i+1:])).

(←) Let *ζ* be an arbitrary sentence in **C**:sub:`L` such that,

.. math::

    1. \quad \exists i \in N_{l(\zeta)}: (l(\zeta[:i+1]) = l(\zeta[i+1:])).

By the :ref:`Definitions 4.2.1 <definition-4-2-1>` and :ref:`4.2.2 <definition-4-2-2>`,

.. math::

    2. \quad l(\zeta[:i+1]) = i+1

.. math::

    3. \quad l(\zeta[i+1:]) = l(\zeta) - (i+1) + 1

Putting step 1, step 2 and step 3 together, 

.. math::

    4. \quad i+1 = l(\zeta) - (i+1) + 1

From which it follows algebraically, 

.. math::

    5. \quad l(\zeta) = 2n + 1.

Therefore *l(ζ)* is odd. Putting both directions of the proof together and generalizing over all Sentences in the Corpus,

.. math::

    6. \quad \forall \zeta \in C_L: \exists i \in \mathbb{N}: (l(\zeta) = 2i + 1 ) \land (l(\zeta[:i+1]) = l(\zeta[i+1:]))  

∎

.. _theorem-4-2-3:

**Theorem 4.2.3** :math:`\forall \zeta \in C_L: \exists i \in \mathbb{N}: (l(\zeta) = 2i) \land (l(\zeta[:i]) + 1 = l(\zeta[i:]))`

This theorem can be stated in natural language as follows: For any Sentence in the Corpus, its String Length is even if and only if the String Length of the Left Partial Sentence of Length *i* plus 1 is equal to the String Length of the Right Partial Sentence starting at index *i*.

(→) Let *ζ* be an arbitrary sentence in **C**:sub:`L` such that there exists a natural number *i* with the following condition,
 
.. math::

    1. \quad l(\zeta) = 2i

Since *i* is a natural number, it follows,

.. math::

    2. \quad 1 \leq n \leq l(\zeta)

From which it follows, 

.. math::

    3. \quad i \in N_{l(\zeta)}

By :ref:`Definition 4.2.1 <definition-4-2-1>`, the String Length of the Left Partial Sentence is given by,

.. math::

    4. \quad l(\zeta[:i]) = i

By :ref:`Definition 4.2.2 <definition-4-2-2>`, the String Length of the Right Partial Sentence is given by,

.. math::

    5. \quad l(\zeta[i:]) = l(\zeta) - i + 1 = 2i - i + 1 = i + 1

Therefore, 

.. math::

    6. \quad l(\zeta[:i]) + 1 = l(\zeta[i:]) = i + 1

This shows an *i* exists such that 

.. math::

    7.  \quad l(\zeta[:i]) + 1 = l(\zeta[i:])

Therefore, 

.. math::

    8. \quad \exists i \in N_{l(\zeta)}: (l(\zeta[:i]) + 1 = l(\zeta[i:]))

(←) Let *ζ* be an arbitrary sentence in C:sub:`L` such that, 

.. math::

    1. \quad \exists i \in N_{l(\zeta)}: (l(\zeta[:i]) + 1 = l(\zeta[i:]))

By :ref:`Definition 4.2.1 <definition-4-2-1>` and :ref:`Definition 4.2.2 <definition-4-2-2>`,

.. math::

    2. \quad l(\zeta[:i]) = i

.. math::

    3. \quad l(\zeta[i:]) = l(\zeta) - i + 1

Combining step 1, step 2 and step 3, 

.. math::

    4. \quad i + 1 = l(\zeta) - i + 1

Solving for *l(ζ)*,

.. math::

    5. \quad l(\zeta) = 2i

Thus, *l(ζ)* is even. Since both directions of the implication hold and *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,

.. math::

    6. \quad \forall \zeta \in C_L: (\exists i \in \mathbb{N}: l(\zeta) = 2i) ↔ (\exists i \in N_{l(\zeta)}: (l(\zeta[:i]) + 1 = l(\zeta[i:]))) 

∎

.. _theorem-4-2-4:

**Theorem 4.2.4** :math:`\forall \zeta \in C_L: \exists n in N_{l(\zeta)}: (l(\zeta[:n]) = l(\zeta[n:])) \lor (l(\zeta[:n]) + 1 = l(\zeta[n:]))` 

This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus, there exists a natural number *n* (between *1* and the length of *ζ*, inclusive) such that either the String Length of its Left Partial Sentence is equal to the String Length of its Right Partial Sentence, or the String Length of the Left Partial Sentence is one more than the String Length of the Right Partial Sentence.

Let *ζ* be an arbitrary sentence in C:sub:`L`. Let,

.. math::

    1. \quad l(\zeta) = k

If *k* is even, let 

.. math::

    2. \quad n = k/2

Then 

.. math::

    3. \quad l(\zeta[:n]) = n = k/2

And 

.. math::

    4. \quad l(\zeta[n:]) = k - n + 1 = k - k/2 = (k + 1)/2

Therefore, 

.. math::

    5. \quad l(\zeta[:n]) + 1 = l(ζ[n:])

If *k* is odd, let 

.. math::

    6. \quad n = (k + 1)/2

Then 

.. math::

    7. \quad l(\zeta[:n]) = n = (k + 1)/2

And 

.. math::

    8. \quad l(\zeta[n:]) = k - n  + 1 = k - (k + 1)/2  + 1= (k - 1)/2 + 1 = (k + 1)/2

Therefore, 

.. math::

    9. \quad l(\zeta[:n]) = l(\zeta[n:])

In both cases, an *n* has been found that satisfies the condition in the theorem. Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,

.. math::

    10. \quad \forall \zeta \in C:sub:`L`: \exists n \in N_{l(\zeta)}: ( l(\zeta[:n]) = l(\zeta[n:]) ) \lor ( l(\zeta[:n]) + 1 = l(\zeta[n:]) ) 

∎

:ref:`Theorems 4.2.2 <definition-4-2-2>` - :ref:`4.2.4 <definition-4-2-4>` conjunctively establish the existence of a natural number that can reliably be called the center, or *Pivot*, of any Sentence in a Corpus. This leads to the following definition. 

.. _definition-4-2-3:

**Definition 4.2.3: Pivots** 

The Pivot of a Sentence *ζ*, denoted *ω(ζ)*, is defined as the natural number such that the following formula is true,

.. math::

   (l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) ) ∨ (l(ζ[:ω(ζ)]) + 1 = l(ζ[ω(ζ):])) 
   
Using :ref:`Theorem 4.2.2 <theorem-4-2-2>` and :ref:`Theorem 4.2.3 <theorem-4-2-3>`, the explicit formula for a Sentence Pivot are given below,

    - If l(ζ) is odd, then :math:`\omega(\zeta) = i + 1`, where i is the natural number satisfying :math:`l(\zeta) = 2i + 1`.
    - If l(ζ) is even, then :math:`\omega(\zeta) = i`, where i is the natural number satisfying :math:`l(ζ) = 2i`. 
  
∎

The following example shows the relationship between Partial Sentences and Pivots.

**Example**

Consider these simple examples from a hypothetical Language **L** with Alphabet,

.. math::

    \Sigma = \{ \text{"a"}, \text{"b"}, \text{"c"}, \text{" "}, \text{""} \}

Various "sentences" of this Language are given below, along with their Partial Sentences and Pivots,

.. list-table::
   :header-rows: 1

   * - ζ
     - l(ζ)
     - ω(ζ)
     - ζ[:ω(ζ)]
     - l(ζ[:ω(ζ)])
     - ζ[ω(ζ):]
     - l(ζ[ω(ζ):])
   * - "a"
     - 1
     - 1
     - "a"
     - 1
     - "a"
     - 1
   * - "aa"
     - 2
     - 1
     - "a"
     - 1
     - "aa"
     - 2
   * - "aba"
     - 3
     - 2
     - "ab"
     - 2
     - "ba"
     - 2
   * - "abba"
     - 4
     - 2
     - "ab"
     - 2
     - "bba"
     - 3
   * - "abcba"
     - 5
     - 3
     - "abc"
     - 3
     - "cba"
     - 3
   * - "abccba"
     - 6
     - 3
     - "abc"
     - 3
     - "ccba"
     - 4
   * - "abbcbba"
     - 7
     - 4
     - "abbc"
     - 4
     - "cbba"
     - 4
   * - "abbccbba"
     - 8
     - 4
     - "abbc"
     - 4
     - "ccbba"
     - 5
   * - "abbbcbbba"
     - 9
     - 5
     - "abbbc"
     - 5
     - "cbbba"
     - 5
   * - "abbbccbbba"
     - 10
     - 5
     - "abbbc"
     - 5
     - "ccbbba"
     - 6
   * - "a a"
     - 3
     - 2
     - "a "
     - 2
     - " a"
     - 2
   * - "a ba"
     - 4
     - 2
     - "a "
     - 2
     - " ba"
     - 3
   * - "ab cb"
     - 5
     - 3
     - "ab "
     - 3
     - " cb"
     - 3
   * - "a bca"
     - 5
     - 3
     - "a b"
     - 3
     - "bca"
     - 3
   * - "a bbc  a"
     - 8
     - 4
     - "a bb"
     - 3
     - "bc  a"
     - 5

∎

In the previous example, take note when the Sentence String Length is even, the Right Partial Sentence accumulates an extra Character relative to the Left Partial Sentence, in accordance with :ref:`Theorem 4.2.3 <theorem-4-2-3>`. Similarly, when the Sentence String Length is odd, the Left Partial Sentence is equal in String Length to the Right Partial, in accordance with :ref:`Theorem 4.2.2 <theorem-4-2-2>`. 

With the notion of a Palindromic Pivot established, the class of Even and Odd Palindromes is now defined. 

.. _definition-4-2-4:

**Definition 4.2.4: Even Palindromes**

The class of Even Palindromes, denoted **P**:sup:`+`, is defined as the set of Sentences ζ which satisfy the following open formula,

.. math::

    \zeta \in P_{+} \leftrightarrow [ (\zeta \in P) \land (\exists k \in \mathbb{N} : l(\zeta) = 2k )] 

∎

.. _definition-4-2-5:

**Definition 4.2.5: Odd Palindromes**

The class of Even Palindromes, denoted **P**:sup:`-`, is defined as the set of Sentences ζ which satisfy the following open formula,

.. math::

    \zeta \in P_{-} \leftrightarrow [ (\zeta \in P) \land (\exists k \in \mathbb{N} : l(\zeta) = 2k + 1) ]

∎

The *parity* (to be defined shortly, after it is proven Even and Odd Palindromes partition the class of Palindromes) manifests in a Palindrome's behavior around it's Pivot. This behavior around the Pivot will be important for establishing the various cases of the theorems proved in the next section. The key insight is recognizing, as the previous example shows, the String Length of the Right Partial Sentence for Sentences of odd String Length is always one more than the String Length of the Left Partial Sentence, while the Left and Right Partial are of equal String Length when the String Length of the Sentence is even.

.. _theorem-4-2-5:

**Theorem 4.2.5** :math:`\forall \zeta \in C_L: (\exists k \in \mathbb{N}: l(\zeta) = 2k + 1) \leftrightarrow \omega(\zeta) = \frac{l(\zeta) + 1}{2}`

( → ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

.. math::

    1. \quad \exists k \in \mathbb{N} : l(\zeta) = 2k + 1

From :ref:`Theorem 4.2.2 <theorem-4-2-2>` and step 1, it follows 

.. math::

    2. \quad n = k + 1 
    
Where *n* satisfies,

.. math::

    3. \quad l(\zeta[:n]) = l(\zeta[n:])

Therefore, 

.. math::

    4. \quad  = k + 1 = (2k + 1 + 1)/2 = \frac{l(\zeta) + 1}{2}

By :ref:`Definition 4.2.3 <definition-4-2-3>`, the pivot *ω(ζ)* is the smallest natural number satisfying the condition. Since *n* satisfies the condition and is the only solution, it must be the smallest. Therefore, 

.. math::

    5. \quad \omega(\zeta) = \frac{l(\zeta) + 1}{2}

( ← ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

.. math::

    1. \quad \omega(\zeta) = \frac{l(\zeta) + 1}{2}

This can be re-arranged to yield,

.. math::

    2. \quad l(\zeta)  = 2\omega(\zeta) - 1

Since *ω(ζ)* is defined to be a natural number, let *k* be,

.. math::

    3. \quad k = \omega(\zeta) + 1

Then, 

.. math::

    4. \quad l(\zeta)  = 2k + 1

Therefore,

.. math::

    5. \quad \exists k \in \mathbb{N} : l(\zeta) = 2k + 1

Since both directions of the equivalence are shown, the theorem is proven by generalizing over the Corpus,

.. math::

    6. \quad \forall \zeta \in C_L: (\exists k \in \mathbb{N} : l(\zeta) = 2k + 1) \leftrightarrow \omega(\zeta) = \frac{l(\zeta) + 1}{2} 

∎

.. _theorem-4-2-6:

**Theorem 4.2.6** :math:`\forall \zeta \in P^{-}: \omega = \frac{l(\zeta) + 1}{2}`

Assume *ζ* is an arbitrary Sentence such that,

.. math::

    1. \quad \zeta \in P^{-}

From :ref:`Definition 4.2.4 <definition-4-2-4>`, it follows, 

.. math::

    2. \quad \exists k \in \mathbb{B} : l(\zeta) = 2k + 1

From :ref:`Theorem 4.2.5 <theorem-4-2-5>`, it follows, 

.. math::

    3. \quad \omega(\zeta) = \frac{l(\zeta) + 1}{2} 

∎

.. _theorem-4-2-7:

**Theorem 4.2.7** :math:`\forall \zeta \in C_L: (\exists i \in \mathbb{N}: l(\zeta) = 2i) \leftrightarrow \omega = \frac{l(\zeta)}{2}`

( → ) Let ζ be an arbitrary in **C**:sub:`L` such that,

.. math::

    1. \quad \exists i \in \mathbb{N} : l(\zeta) = 2i

By :ref:`Theorem 4.2.3 <definition-4-2-3>`, 

.. math::

    2. \quad l(\zeta[:i]) + 1 = l(\zeta[i:])

From :ref:`Definition 4.2.1 <definition-4-2-1>` and :ref:`Definition 4.2.2 <definition-4-2-2>`, this is equivalent to,

.. math::

    3. \quad i + 1 = l(\zeta) - i + 1

Therefore,

.. math::

    4. \quad i = \frac{l(\zeta)}{2}

By :ref:`Definition 4.2.3 <definition-4-2-3>`, the Pivot *ω(ζ)* is the smallest natural number satisfying the condition. Since *i* satisfies the condition and is the only solution when *l(ζ)* is even, it must be the smallest. Therefore, 

.. math::

    5. \quad \omega(\zeta) = \frac{l(\zeta)}{2}

( ← ) Let *ζ* be an arbitrary Sentence from **C**:sub:`L` such that

.. math::

    1. \quad \omega(\zeta) = \frac{l(\zeta)}{2} 

Since by :ref:`Definition 4.2.3 <definition-4-2-3>`, a Pivot is a natural number, let *i* be a natural number such that,

.. math::

    2. \quad i = \omega(\zeta)

It follows immediately,

.. math::

    3. \quad l(\zeta) = 2i

Therefore *ζ* is even,

.. math::

    4. \quad \exists i \in \mathbb{N}: l(\zeta) = 2i

Since both directions of the equivalence have been shown, it follows,

.. math::

    5. \quad \forall \zeta \in C_L: \omega(\zeta) = \frac{l(\zeta)}{2} 

∎

.. _theorem-4-2-8:

**Theorem 4.2.8** :math:`\forall \zeta \in P^{+}: \omega = \frac{l(\zeta)}{2}`

Assume *ζ* is arbitrary Sentence such that,

.. math::

    1. \quad \zeta \in P^{+}

From :ref:`Definition 4.2.5 <definition-4-2-5>`, it follows, 

.. math::

    2. \quad \exists k \in \mathbb{N} : l(\zeta) = 2k

From :ref:`Theorem 4.2.8 <theorem-4-2-8>`, it follows, 

.. math::

    3. \quad \omega(\zeta) = \frac{l(\zeta)}{2} 

∎

.. _theorem-4-2-9:

**Theorem 4.2.9** :math:`\forall \zeta \in C_L: l(\zeta) + 1 = l(\zeta[:\omega(\zeta)]) + l(\zeta[\omega(\zeta):])`

Assume *ζ* is an arbtirary Sentence from the Corpus,

.. math::

    1. \quad \zeta \in C_L

Let *ω(ζ)* be the Pivot of ζ. From :ref:`Definition 4.2.1 <definition-4-2-1>` of Left Partial Sentence,

.. math::

    2. \quad l(\zeta[:\omega(\zeta)]) = \omega(\zeta)

From :ref:`Definition 4.2.2 <definition-4-2-2>` of Right Partial Sentence, 

.. math::

    3. \quad l(\zeta[\omega(\zeta):]) =  l(\zeta) - \omega(\zeta) + 1

Therefore, 

.. math::

    4. \quad l(\zeta[:\omega(\zeta)]) + l(\zeta[\omega(\zeta):]) = l(\zeta) + 1 
    
Since *ζ* was arbitrary, this can be generalized over the Corpus,

.. math::

    5. \quad \forall \zeta \in C_L: l(\zeta) + 1 = l(\zeta[:\omega(\zeta)]) + l(\zeta[\omega(\zeta):]) 

∎

.. _theorem-4-2-10:

**Theorem 4.2.10** :math:`\forall \zeta \in C_L: \omega(\varsigma(\zeta)) \leq \omega(\zeta)`

Let *ζ* be an arbitrary Sentence in the Corpus. By :ref:`Theorem 3.1.10 <theorem-3-1-10>`,

.. math::

    1. \quad l(\zeta) \geq l(\varsigma(\zeta))

Through algebraic manipulation, this is equivalent to the following,

.. math::

    2. \quad \frac{l(\zeta) + 1}{2} \geq \frac{l(\varsigma(\zeta)) + 1}{2}

It is also equivalent to,

.. math::

    3. \quad \frac{l(\zeta)}{2} \geq \frac{l(\varsigma(\zeta))}{2}

Moreover,

.. math::

    4. \quad \frac{l(\varsigma(\zeta)) + 1}{2} ≥ \frac{l(\varsigma(\zeta))}{2}

By :ref:`Theorems 4.2.6 <theorem-4-2-6>` and :ref:`4.2.8 <theorem-4-2-8>`, one of the following must be true,

.. math::

    5. \quad \omega(\zeta) = \frac{l(\zeta) + 1}{2}
    
.. math::

    6. \quad \omega(\zeta) = \frac{l(\zeta)}{2}

Similarly, it must be the case, one of the following is true,

.. math::

    7. \quad \omega(\varsigma(\zeta)) = \frac{l(\varsigma(\zeta)) + 1}{2}
    
.. math::

    8. \quad \omega(\varsigma(\zeta)) = \frac{l(\varsigma(\zeta))}{2}

If :math:`\omega(\zeta) = \frac{l(\zeta) + 1}{2}`, then *l(ζ)* is odd by :ref:`Theorem 4.2.5 <theorem-4-2-5>`. It follows from step 2 and step 4, that no matter the value of *ω(ς(ζ))*,

.. math::

    9. \quad \omega(\varsigma(\zeta)) \leq \omega(\zeta)  

If :math:`\omega(\zeta) = \frac{l(\zeta)}{2}`, then *l(ζ)* is even by Theorem 3.2.12. From step 3, if :math:`(\varsigma(\zeta)) = \frac{l(\varsigma(\zeta))}{2}`, it follows, 

.. math::

    10. \quad \omega(\varsigma(\zeta)) \leq \omega(\zeta) 

If :math:`\omega(\varsigma(\zeta)) = \frac{l(\varsigma(\zeta)) + 1}{2}`, then *l(ς(ζ))* is odd by Theorem 3.2.10. 

Since *l(ς(ζ))* is odd and *l(ζ)* is even, atleast one Delimiter was removed from *ζ* during *σ*-reduction, 

.. math::

    11. \quad l(\varsigma(\zeta)) + 1 leq l(\zeta)

Therefore, 
    
.. math::

    12. \quad \frac{l(\varsigma(\zeta)) + 1}{2} \leq \frac{l(\zeta)}{2}.

It follows,

.. math::

    13. \quad \omega(\varsigma(\zeta)) = \frac{l(\varsigma(\zeta)) + 1}{2} \leq \frac{l(\zeta)}{2} = \omega(\zeta)

Thus, in all possible cases,

.. math::

    14. \quad \omega(\varsigma(\zeta)) \leq \omega(\zeta)

Since *ζ* was arbitrary, this can be generalized over the Corpus,

.. math::

    15. \quad \forall \zeta \in C_L: \omega(\varsigma(\zeta)) \leq \omega(\zeta) 

∎

These properties of Pivots and Partial Sentences will be necessary to state and prove the main results of the work in the next section. In addition, it will be necessary to know the class of Odd Palindromes and the class of Even Palindromes form a partition of the class of all Palindromes. This result is definitively established in :ref:`Theorems 4.2.11 <theorem-4-2-11>` - :ref:`4.2.12 <theorem-4-2-11>`.

.. _theorem-4-2-11:

**Theorem 4.2.11** :math:`P_{+} \cap P_{-} = \emptyset`

This theorem can be stated in natural language as follows: A Palindrome cannot be both even and odd.

For the sake of contradiction, assume there exists a sentence *ζ* such that 

.. math::

    1. \quad \zeta \in P_{+} \cap P_{-}

This means each of the individual expressions is true,

.. math::

    2. \quad \zeta \in P_{+}
    
.. math::

    3. \quad \zeta \in P_{-}

By :ref:`Definition 4.2.4 <definition-4-2-4>`, it follows from step 2,

.. math::

    4. \quad \exists k \in \mathbb{N} : l(\zeta) = 2k

By :ref:`Definition 4.2.5 <definition-4-2-5>`, it follows from step 3,

.. math::

    5. \quad \exists k \in \mathbb{N} : l(\zeta) = 2k + 1

This leads to the contradiction, 

.. math::

    6. \quad 0 = 1

Therefore, the assumption that *ζ* is both an Even and Odd Palindrome must be false. From this it follows,

.. math::

    7. \quad P_{-} \cap P_{+} = \emptyset 

∎

.. _theorem-4-2-12:

**Theorem 4.2.12** :math:`P_{-} \cup P_{+} = P`

This theorem can be translated into natural language as follows: All Palindromes are either Even Palindromes or Odd Palindromes. 

(⊆) Let *ζ* be an arbitrary Sentence of the Corpus such that, 

.. math::

    1. \quad \forall \zeta \in P_{-} \cup P_{+}

Which means either of this two cases must obtain, 

.. math::

    2. \quad \zeta \in P_{-}
    
.. math::

    3. \quad \zeta \in P_{+}

By :ref:`Definition 4.2.4 <definition-4-2-4>`, if step 2 obtains, then 

.. math::

    4. \quad \zeta \in P

By :ref:`Definition 4.2.5 <definition-4-2-5>`, if step 3 obtains, then 

.. math::
    
    5. \quad \zeta \in P
   
Therefore, in either case, 

.. math::

    6. \quad \zeta \in P

Since *ζ* was an arbitrary Sentence in :math:`P_{-} \cup P_{+}`, this can generalize as,

.. math::

    7. \quad \forall \zeta \in (P_{-} \cup P_{+}) \to \zeta \in P
   
This in turn implies,

.. math::

    8. \quad P_{-} \cup P_{+} \subset P

(⊇) Let *ζ* be an arbitrary Sentence of the Corpus such that, 

.. math::

    1. \quad \zeta \in P 

By the properties of natural numbers, it must be the case that one of the following obtains,

.. math::

    2. \quad \exists k \in \mathbb{N} : l(ζ) = 2k

.. math::

    3. \quad \exists k \in \mathbb{N} : l(ζ) = 2k + 1
   
If *l(ζ)* is even, then by :ref:`Definition 4.2.4 <definition-4-2-4>`, 
    
.. math::

    3. \quad \zeta \in P_{+}

If *l(ζ)* is odd, then by :ref:`Definition 4.2.5 <definition-4-2-5>`, 

.. math::

    4. \quad \zeta \in P_{-}

Therefore, in either case, 

.. math::

    5. \quad \zeta \in P_{+} \cup P_{-}
   
Since *ζ* was an arbitrary Palindrome, this can generalize as,

.. math::

    6. \quad \forall \zeta \in P \to \zeta \in (P_{+} \cup P_{-})

This implies,

.. math::

    7. \quad P \subset P_{+} \cup P_{-}
   
Step 8 from the (⊆) direction and taken with step 7 from the (⊇) together imply,

.. math::

    8. \quad P_{+} \cup P_{-} = P 

∎

With the partitioning of the class **P** of Sentences in a Corpus, i.e. Palindromes, the notion of *parity* can now be stated precisely in the following definition.

.. _definition-4-2-6:

**Definition 4.2.6: Parity** 

A Palindrome ζ is said to have a *even parity* or *be even* if and only if,

.. math::

    P \in P_{+} 
    
A Palindrome ζ is said to have an *odd parity* or *be odd* if and only if,

.. math::

    P \in P_{-} 

∎

Now that the two partitioning of Palindromes, aspect and parity, have been precisely defined, the final two sections (:ref:`Section V <section-v>` and :ref:`Section VI <section-vi>`) of this work requires one more definition to correctly formulate its main results. This definition will allow the structure around a Palindrome's Pivot to be described with precise notation.

.. _definition-4-2-7:

**Definition 4.2.7: Pivot Words**

Let *ζ* be a sentence in C:sub:`L` with length *Λ(ζ)*, word-level representation W:sub:`ζ`, and pivot *ω(ζ)*. The left Pivot Word, denoted *ζ{ω-}*, and the right Pivot Word, denoted *ζ{ω+}*, are defined as follows:

**Case 1**: :math:`\Lambda(\zeta) = 1`

.. math::

    \zeta\{\omega-\} = \zeta\{\omega+\} = \zeta\{1\} = \zeta\{\Lambda(\zeta)\}

**Case 2**: :math:`\Lambda(\zeta) > 1 \land \zeta[\omega(\zeta)] = \sigma`

    - :math:`\zeta\{\omega-\} = \alpha_j`, such that :math:`(j, \alpha_j) \in W_{\zeta}` and :math:`\alpha_j` is immediately to the left of the Delimiter at ω(ζ).
    - :math:`\zeta\{\omega+\} = \alpha_k`, such that :math:`(k, \alpha_k) \in W_{\zeta}` and :math:`k = j + 1`.

**Case 3**: :math:`\Lambda(\zeta) > 1 \land \zeta[\omega(\zeta)] \neq \sigma`

    - :math:`\zeta\{\omega-\} = \zeta\{\omega+\} = \alpha_j` such that :math:`(j, \alpha_j) \in W_{\zeta}` and :math:`\alpha_j` contains the character at position ω(ζ). 
  
  ∎

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
    - ζ{ω-} = "abc" <definition-4-1-1>`0
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
    - ζ{ω+} = "fg"

∎

From these simplified examples, it should be clear that a Pivot Word is either the Word which contains the Pivot Character, or it is the pair of Words which surround the Pivot Character (i.e. exactly when the Pivot Character is a Delimiter).