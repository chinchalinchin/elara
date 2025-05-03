.. _section-vi:

Section VI: Postulates
----------------------

The following theorems serve as the main result of the current formal system that has been constructed to describe the syntactical structures of Palindromes in any Language. 

**Theorem 3.3.1: The Inverse Postulate** [ (inv(ζ{1}) ⊂:sub:s ζ{Λ(ζ)}) ∨ (inv(ζ{Λ(ζ)}) ⊂:sub:s ζ{1}) ] ∧ [ (ζ{1} ⊂:sub:s inv(ζ{Λ(ζ)})) ∨ (ζ{Λ(ζ)} ⊂:sub:s inv(ζ{1})) ]

Assume *ζ* is an arbitrary Sentence in the Corpus **C**:sub:`L` such that it is a Palindrome,

    1. ζ ∈ P
    
By :ref:`Definition 4.1.1 <definition-4-1-1>`,

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

By Theorem 2.2.4 (Λ(ζ) ≥ 1), step 2 and by :ref:`Definition 4.1.1 <definition-4-1-1>` , there are two possible cases to consider,

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

Using :ref:`Definition 4.1.1 <definition-4-1-1>` , Let 

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

TODO: need some way to relate the pivots of sigma-reduction to original pivots!

.. admonition:: TODO (Notes!)

    **Theorem: The Perfect Pivot Postulate**

    ζ ∈ PP ↔ [∃ α ∈ L: (ζ[ω(ζ)] ⊂ :sub:`s` α) ∧ (α ∈ R) ] ∨ (ζ[ω(ζ)] = σ)

    **First Pass Notes**

    (→)  Assume ζ ∈ PP (ζ is a Perfect Palindrome).

    Word-level representation: Let W:sub:ζ = (α₁ , α₂ , ..., αₙ) be the Word-level representation of ζ, where n = Λ(ζ).

    Pivot: Let ω :sub:`ζ` be the Pivot of ζ. There are two cases:

    Case 1: ω :sub:`ζ` = σ (Delimiter Pivot). In this case, the condition (ω :sub:`ζ` = σ) is satisfied, and the right-hand side of the biconditional is true.

    Case 2: ω :sub:`ζ` ≠ σ (Non-Delimiter Pivot).

    In this case, the Pivot is a Character within a Word. Let k be the index such that αₖ contains ω:sub:ζ.
    Since ζ is a Perfect Palindrome, by :ref:`Definition 4.1.1 <definition-4-1-1>`, ζ = inv(ζ).
    This implies that the Word αₖ is symmetrical around the Pivot Character ω:sub:ζ.
    Therefore, αₖ must be a Reflective Word (αₖ ∈ R), and ω :sub:`ζ` ⊂ :sub:`s` αₖ.
    This satisfies the condition [∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R) ].
    In both cases, the right-hand side of the biconditional is true.

    (←) Assume [∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R) ] ∨ (ω:sub:`ζ` = σ).

    Cases: There are two cases to consider:

    Case 1: ∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R).

    This means the Pivot Character is contained within a Reflective Word α.
    Since α is Reflective, it is symmetrical around its center, which includes the Pivot Character.
    This symmetry of α contributes to the overall symmetry of ζ, making it a Perfect Palindrome (ζ ∈ PP).
    Case 2: ω:sub:ζ = σ.

    This means the Pivot is the Delimiter Character, which naturally creates a symmetrical division in the Sentence.
    By the Second Inverse Postulate, the Words surrounding the Delimiter Pivot either contain each other or are equal.
    This, combined with the overall palindromic structure, ensures that ζ is a Perfect Palindrome (ζ ∈ PP).
    In both cases, ζ ∈ PP.

    Since we have proven both directions of the implication, the theorem is established:

    ζ ∈ PP ↔ [∃ α ∈ L: (ω :sub:`ζ` ⊂:sub:`s` α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ) ∎

    **Second Pass**

    Let's first slightly reformulate the theorem to make it even clearer and more precise:

    ζ ∈ PP ↔ [ (∃ α ∈ L: (ζ[ω(ζ)] ⊂ :sub:`s` α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (inv(α :sub:`ζ` :sup:`-ω`) ⊂ :sub:`s` α :sub:`ζ` :sup:`+ω`) ∨ (inv(α :sub:`ζ` :sup:`+ω`) ⊂ :sub:`s` α :sub:`ζ`:sup:`-ω`)) ]

    Translation: A sentence ζ is a perfect palindrome if and only if one of the following conditions holds:

    The character at the pivot index ω(ζ) is contained in a reflective word α that is in the language.
    The character at the pivot index ω(ζ) is a delimiter (σ), and the inverse of the left pivot word is contained in the right pivot word, or the inverse of the right pivot word is contained in the left pivot word.

    Proof:

    (↔) Direction:

    Assume ζ ∈ PP.

    Definition of Perfect Palindrome: By :ref:`Definition 4.1.2 <definition-4-1-2>`, ζ = inv(ζ).
    
    Case 1: ζ[ω(ζ)] = σ:
    
    If the character at the pivot is a delimiter, then by the Second Inverse Postulate , we know that ( inv(α:sub:ζ:sup:-ω) ⊂ :sub:`s` α :sub:`ζ` :sup:`+ω`) ∨ ( inv(α :sub:`ζ` :sup:`+ω`) ⊂ :sub:`s` α :sub:`ζ` :sup:`-ω` ).
    Case 2: ζ[ω(ζ)] ≠ σ:

    If the character at the pivot is not a delimiter, then it must belong to a word.

    By Axiom S.2, we know there's at least one word α in ζ.
    
    Since ζ is a perfect palindrome, and the pivot character is not a delimiter, the pivot must lie within a word.
    Let α be the word such that (x, α) ∈ W :sub:`ζ`, and ω(ζ) is within the indices of the characters of α in the character-level representation of ζ.
    
    Since ζ is a perfect palindrome, α must be a reflective word (α ∈ R), because any word that spans across the pivot in a perfect palindrome must be its own inverse.

    Also, since ω(ζ) is within the indices of α, we know that ζ[ω(ζ)] ⊂ :sub:`s` α.

    (←) Direction:

    Assume [(∃ α ∈ L: (ζ[ω(ζ)] ⊂ :sub:`s` α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ ( inv(α :sub:`ζ` :sup:`-ω`) ⊂ :sub:`s` α :sub:`ζ` :sup:`+ω`) ∨ ( inv(α :sub:`ζ` :sup:`+ω` ) ⊂ :sub:`s` α :sub:`ζ` :sup:`-ω` ))].

    Case 1: ∃ α ∈ L: (ζ[ω(ζ)] ⊂ :sub:`s` α) ∧ (α ∈ R)

    If there exists a reflective word α in L that contains the character at the pivot, then ζ must be a perfect palindrome. This is because the presence of a reflective word spanning the pivot implies symmetry around the pivot, which is the defining characteristic of a perfect palindrome.

    Case 2: ζ[ω(ζ)] = σ ∧ ( inv(α :sub:`ζ` :sup:`-ω` ) ⊂ :sub:`s` α :sub:`ζ` :sup:`+ω` ) ∨ ( inv(α :sub:`ζ` :sup:`+ω` ) ⊂ :sub:`s` α :sub:`ζ`:sup:`-ω` )

    If the character at the pivot is a delimiter and either the inverse of the left pivot word is contained in the right pivot word or vice versa, then ζ must be a perfect palindrome. This is because the delimiter at the pivot, combined with the containment relationship between the pivot words, ensures symmetry around the pivot.
    Conclusion:

    We have shown that if ζ is a perfect palindrome, then either the character at the pivot is contained in a reflective word in the language, or the character at the pivot is a delimiter and the pivot words exhibit the specific containment property. Conversely, if either of these conditions holds, then ζ must be a perfect palindrome.

    Therefore:

    ζ ∈ PP ↔ [ (∃ α ∈ L: (ζ[ω(ζ)] ⊂ :sub:`s` α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ ( inv(α :sub:`ζ` :sup:`-ω`) ⊂ :sub:`s` α :sub:`ζ` :sup:`+ω` ) ∨ ( inv(α :sub:`ζ` :sup:`+ω` ) ⊂ :sub:`s` α :sub:`ζ` :sup:`-ω` )) ]

    ∎

    **Third Pass**

    Theorem 3.2.4:

    ∀ ζ ∈ PP: (∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (α :sub:`ζ` :sup:`-ω` ∈ I))

    Translation: For every perfect palindrome ζ, either:

    There exists a word α in the language L such that the character at the pivot index ω(ζ) is contained in α, and α is a reflective word (α ∈ R), OR

    The character at the pivot index ω(ζ) is a delimiter (σ), and the left pivot word is invertible (α:sub:ζ:sup:-ω ∈ I).
    Proof:

    Let ζ be an arbitrary perfect palindrome in PP.

    Definition of Perfect Palindrome: By :ref:`Definition 4.1.1 <definition-4-1-1>`, ζ = inv(ζ).

    Cases based on Parity: We have two cases to consider:

    Case 1: ζ has odd length (ζ ∈ P :sup:`-` )

    By Theorem 3.2.3, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]). This means the pivot falls on a character, ζ[ω(ζ)].

    Subcase 1: ζ[ω(ζ)] ≠ σ
    
    Since ζ[ω(ζ)] is not a delimiter, it must belong to a word. By Axiom S.1, there exists a word α in L such that α is contained in ζ. Since the pivot character is not a delimiter, it must be part of a word in ζ. Let α be the word such that (x, α) ∈ W :sub:`ζ` and ω(ζ) is within the indices of the characters of α in the character-level representation of ζ.

    Since ζ is a perfect palindrome, and ω(ζ) is the pivot, this word α must be reflective (α ∈ R). Otherwise, the characters in ζ would not be symmetrical around the pivot, and ζ wouldn't be a perfect palindrome.
    
    Therefore, ∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R).
    
    Subcase 2: ζ[ω(ζ)] = σ
    
    Since the pivot character is a delimiter, by Theorem 3.2.3, we know that inv(α :sub:`ζ`:sup:`-ω`) ⊂ α :sub:`ζ` :sup:`+ω` or inv(α :sub:`ζ` :sup:`+ω` ) ⊂ α :sub:`ζ` :sup:`-ω` .

    Since ζ is a perfect palindrome, we have ζ = inv(ζ). This means the words to the left and right of the pivot must be inverses of each other.

    Therefore, α :sub:`ζ` :sup:`-ω` = inv(α :sub:`ζ` :sup:`+ω` ).
    
    Since α :sub:`ζ` :sup:`+ω` is in L, and α :sub:`ζ` :sup:`-ω` is its inverse, by definition of invertible words, α :sub:`ζ` :sup:`-ω` ∈ I.
    
    Case 2: ζ has even length (ζ ∈ P :sup:`+`)

    By Theorem 3.2.4, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ) + 1:]) + 1. This means the pivot falls between two characters.

    Since ζ is a perfect palindrome, the two characters adjacent to the pivot must be identical (because ζ = inv(ζ)).
    
    By Axiom W.1, these characters cannot be delimiters. Thus, they must belong to a word α that spans across the pivot.
    
    Similar to Case 1, this word α must be reflective (α ∈ R) for ζ to be a perfect palindrome.
    
    Since the two characters adjacent to the pivot are identical and belong to α, we can say that ζ[ω(ζ)] is "contained" in α in the sense that α spans across the pivot.
    
    Therefore, ∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R).
    
    The case where the pivot is a delimiter is covered by our definition of an even-length perfect palindrome.
    
    Conclusion: In all cases, at least one of the two conditions holds. Since ζ was an arbitrary perfect palindrome, we can generalize:

    ∀ ζ ∈ PP: (∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (α :sub:`ζ` :sup:`-ω` ∈ I))

    This completes the proof. ∎

    **Theorem: The Perfect Parity Postulate**

    **NOTE**: This is wrong as stated, but it contains the grain of something true!

    ζ ∈ PP ∧ ζ ∈ P:sup:`+` ↔ ∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R)

    Theorem (Fourth Inverse Postulate): ζ ∈ PP ∧ ζ ∈ P⁺ ↔ ∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R)

    Proof:

    (→) Assume ζ ∈ PP ∧ ζ ∈ P⁺ (ζ is a Perfect Palindrome and an Even Palindrome).

    Even Palindrome: Since ζ ∈ P⁺, by Definition 3.2.3, ω :sub:`ζ` = ε (the Pivot is the Empty Character).

    Perfect Palindrome: Since ζ ∈ PP, by the strengthened Third Inverse Postulate, we have:

    [∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R) ] ∨ (ω:sub:ζ = σ)

    Case analysis:  We have two cases from step 2:

    Case 1: ∃ α ∈ L: (ω :sub:`ζ` ⊂:sub:`s` α) ∧ (α ∈ R). This directly satisfies the right-hand side of the biconditional we're trying to prove.

    Case 2: ω :sub:`ζ` = σ. This contradicts step 1, where we established that ω :sub:`ζ` = ε. Therefore, this case cannot hold.

    Conclusion: Only Case 1 holds, which means ∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R).

    (←) Assume ∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R).

    Strengthened Third Inverse Postulate: This condition directly implies the left-hand side of the strengthened Third Inverse Postulate:

    [∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R) ] ∨ (ω :sub:`ζ` = σ)

    Perfect Palindrome: By the strengthened Third Inverse Postulate, this implies that ζ ∈ PP (ζ is a Perfect Palindrome).

    Non-Delimiter Pivot: Since ω :sub:`ζ` ⊂ :sub:`s` α and α is a Word in the Language, by Axiom W.1 (Discovery Axiom), α cannot contain the Delimiter Character. Therefore, ω :sub:`ζ` ≠ σ.

    Even Palindrome: Since ω :sub:`ζ` ≠ σ, by the strengthened Third Inverse Postulate, it must be the case that ω :sub:`ζ` = ε. By Definition 3.2.3, this means ζ ∈ P⁺ (ζ is an Even Palindrome).

    Conclusion: We have shown that ζ ∈ PP and ζ ∈ P⁺, which means ζ ∈ PP ∧ ζ ∈ P⁺.

    Since we have proven both directions of the implication, the theorem is established:

    ζ ∈ PP ∧ ζ ∈ P⁺ ↔ ∃ α ∈ L: (ω :sub:`ζ` ⊂ :sub:`s` α) ∧ (α ∈ R) ∎