

.. _palindromics-introduction:

Introduction
============

The goal of this work is to formalize the constraints the palindromes of *any* language and corpus must satisfy independently of the semantic interpretation of their constituent words and sentences. These formal constraints will in turn lead to the identification of the main structural elements of palindromes. After a language is assumed and a class of words identified, these structural elements can be used as a basis for further empirical and statistical analysis of the assumed language. 

At the outset, it must be stated the complexity of pursuing a complete theory of palindromes is beyond the scope of the current work Palindromes are a rich and diverse linguistic phenomenon, appearing in many different shapes and sizes. Some of these forms are more amenable to analysis than others. 

This work will introduce the notions of a palindrome's core attributes: *aspect*, *parity*, *punctuality* and *case*. The first two attributes are within the scope of formal analysis. The third and fourth attributes, however, presents certain difficulties that will be more fully appreciated after the theory to describe the first two attributes has been solidifed. Suffice to say, it is the author's opinion these second two attributes of palindromes cannot be given an account unless semantic assumptions are introduced into the formal model.

To provide a overview of the theory of palindromic structures and give a general notion of what is meant by these attributes of a palindrome, consider three well-known examples,

- no devil lived on
- not on
- don't nod

The first example is what will be termed a *perfect palindrome*. This sentence, ignoring case and punctuation, is a perfect mirror image of itself. The reversal of *"no devil lived on"* reads the same forwards as backwards. 

The second example is what will be termed an *imperfect palindrome*. This sentence, even ignoring the mitigations of case and punctuation, is not an *exact* mirror image of itself. The strict reversal of "*not on*" is "*no ton*". The spaces in the reversed sentence need un-scrambled in order to retrieve the semantic content. However, the reversed string is not precisely *devoid* of semantic content. The relative order of the characters is still preserved in the string; it is only the spaces which need re-arranged. 

This distinction between *perfect* and *imperfect* is termed a palindrome's *aspect*. The *aspect* denotes the type of delimiter (space) symmetry displayed by the palindrome. This delimiter symmetry is a measure of how much semantic content is preserved under sentence reversal. 

This insight into the *aspect* of a palindrome will lead to the introduction of a linguistic operation termed a *sigma reduction*. This operation will in turn lead to a formal definition of palindromes that describes their syntactical structure in terms of delimiters (spaces) and inversions (sentence reversal).

The *parity* of a palindrome is related to its *palindromic pivot*, or its point of symmetry.  In other words, a palindrome is type of sentence that has a "*center*". This "*center*" will be termed its *pivot*. The *parity* of a palindrome is determined by its length, which manifests as the type of pivot that describes it symmetry. For example, the sentence "*no devil lived on*" with character length 19 reflects around the pivot of " ", the sentence's central character, whereas the sentence "*not on*" with character length of 6 reflects around an empty character "" between "*t*" and " ". From this example, it can be seen that depending on the parity of the sentence length, the palindromic pivot will either be a character in the sentence, or an empty character that acts as a boundary between two actual characters in the sentence. 

As it will turn out, this example of parity is oversimplified, due to the complications introduced by the aspect of a palindrome. The pivot of a palindrome cannot be rigorously defined until the semantic content of a palindrome's *imperfection* is reconstituted somehow.

The third example of "*don't nod*" demonstrates the deepening ambiguity of introducing punctuation to palindromes. The reversal of this sentence is the opaque *"don t'nod"*. Now, in addition to the scrambling of the spaces, the reversed string must also have its punctuation re-sorted. There is no formal method known to the author for dealing with these types of ambiguities that depend entirely on the semantic interpretation of the language under consideration, such as the rules of contractions. The *punctuality* of a palindrome can only be described by introducing semantics into the theory.

Similarly, the fourth attribute of palindromes, *case*, is a semantic construct that possesses no unifying syntactical properties across languages (as far as the author knows). *Case* is a semantic relationship that identifies characters in an alphabet as different manifestations of the same underlying semantic entity, i.e. *"a"* and *"A"* are regarded as different *"modes"* of the same letter. This information is not present in the syntax of a language and is an extra assumption that must be modeled accordingly.

The aim of this analysis is to develop a theory of palindromes *independent* of semantic interpretation. In other words, formalizing a theory of palindromes that describes the logical structure of their aspect and parity is the goal of the current analysis. For this reason, all complications that arise from case and punctuality are ignored. The examples that are considered in the following sections only deal with sentences that are meaningful without the considerations of case or punctuations.

This restriction to *aspect* and *parity* may appear restrictive; Indeed, it may be argued by introducing this restriction to the formal theory that is about to developed, it has no application to actual language. To this argument, it should be countered the structures uncovered in this restricted subset of language must nevertheless preserve their structure when embedded into the whole of language.

A note on the terminology introduced in this work is in order. When a semantic term is capitalized, e.g. Word or Sentence, this will mean it is referred to in its capacity as a formal entity. While the formal system was designed to model the actual syntax of Characters, Words and Sentences, this should not be taken to mean the formal entities that emerge from this system are necessarily representative of actual linguistic entities. While the formal entities in this system may not map *one-to-one* with their empirical counterparts, it will be seen their characteristics nevertheless provide insight into the nature of their empirical counterparts.

.. _palindromics-table-of-contents:

Table Of Contents
-----------------

- Introduction
    - Table of Contents
    - Glossary
- :ref:`Section I: Languages & Corpora <palindromics-section-i>`
    - :ref:`I.I: Formalization <palindromics-section-i-i>`
    - :ref:`I.II: Strings <palindromics-section-i-ii>`
    - :ref:`I.III: Words <palindromics-section-i-iii>`
    - :ref:`I.IV: Sentences <palindromics-section-i-iv>`
    - :ref:`I.V: Summary <palindromics-section-i-v>`
- :ref:`Section II: Structures <palindromics-section-ii>`
    - :ref:`II.I: Delimiter Count <palindromics-section-ii-i>`
    - :ref:`II.II: Reductions <palindromics-section-ii-ii>`
    - :ref:`II.III: Palindromes <palindromics-section-ii-iii>`
    - :ref:`II.IV: Summary <palindromics-section-ii-iv>`
- :ref:`Section III: Postulates <palindromics-section-iii>`
    - :ref:`III.I: Prior Results <palindromics-section-iii-i>`
    - :ref:`III.II: Inverse Postulates <palindromics-section-iii-ii>`
    - :ref:`III.III: Summary <palindromics-section-iii-iii>`
- :ref:`Section IV: Analysis <palindromics-section-iv>`
    - :ref:`IV.I: Sentence Integrals <palindromics-section-iv-i>`
    - :ref:`IV.II: Probability <palindromics-section-iv-ii>`
    - :ref:`IV.III: Summary <palindromics-section-iv-iii>`
- :ref:`Appendix I: Addendums <palindromics-appendix-i>`
    - :ref:`AI.I: Omitted Axioms <palindromics-appendix-i-i>`
    - :ref:`AI.II: Omitted Proofs <palindromics-appendix-i-ii>`
- :ref:`Appendix II: Data <palindromics-appendix-ii>`
    - :ref:`AII.I: English Data <palindromics-appendix-ii-i>`
    - :ref:`AII.II: Latin Data <palindromics-appendix-ii-ii>`
- :ref:`Appendix III: Code <palindromics-appendix-iii>`

.. _palindromices-glossary:

Glossary
--------

.. NOTE: Glossary isn't done yet.

.. _palindromics-definitions:

-----------
Definitions
-----------

- :ref:`Definition 1.2.1: Concatenation <palindromics-definition-1-2-1>`: :math:`st`
- :ref:`Definition 1.2.2: String Length <palindromics-definition-1-2-2>`: :math:`l(s)`
- :ref:`Definition 1.2.3: Character Index Notation <palindromics-definition-1-2-3>`: :math:`s[i]`
- :ref:`Definition 1.2.4: String Equality <palindromics-definition-1-2-4>`: :math:`s = t`
- :ref:`Definition 1.2.5: Containment <palindromics-definition-1-2-5>`: :math:`t \subset_s s`
- :ref:`Definition 1.2.6: String Inversion <palindromics-definition-1-2-6>`: :math:`s^{-1}`
- :ref:`Definition 1.3.1: Reflective Words <palindromics-definition-1-3-1>`: :math:`\alpha in R \equiv \alpha = {\alpha}^{-1}`
- :ref:`Definition 1.3.2: Invertible Words <palindromics-definition-1-3-2>` :math:`\alpha in I \equiv {\alpha}^{-1} \in L`
- :ref:`Definition 1.3.3: Phrases <palindromics-definition-1-3-3>`: :math:`P_n = (p(1), ..., p(n))`
- :ref:`Definition 1.3.4: Lexicons <palindromics-definition-1-3-4>`: :math:`L_n = \{ p \mid \forall p: p = P_n \}`
- :ref:`Definition 1.3.5: Limitation <palindromics-definition-1-3-5>`: :math:`\Pi_{i=1}^{n} p(i)`
- :ref:`Definition 1.3.6: Canonization <palindromics-definition-1-3-6>`: :math:`\pi(s)`
- :ref:`Definition 1.3.7: Canon <palindromics-definition-1-3-7>`: :math:`\mathbb{S} = \{ \pi(s) \mid \forall s \in S \}` 
- :ref:`Definition 1.3.8: Dialect <palindromics-definition-1-3-6>`: :math:`D = \bigcup_{i=1}^{\infty} \{ s \in S \mid \exists p \in L_i: s = \Pi_{j=1}^{i} p(j) \}`
- :ref:`Definition 1.4.1: Word Length <palindromics-definition-1-4-1>`: :math:`\Lambda(\zeta)`
- :ref:`Definition 1.4.2: Word Indices <palindromics-definition-1-4-2>`: :math:`\zeta[[i]]`
- :ref:`Definition 1.4.3: Invertible Sentences <palindromics-definition-1-4-3>`: :math:`\zeta \in K \equiv {\zeta}^{-1} \in C`
- :ref:`Definition 2.1.1: Delimiter Count <palindromics-definition-2-1-1>`: :math:`\Delta(s)`
- :ref:`Definition 2.2.1: σ-Reduction <palindromics-definition-2-2-1>`: :math:`\varsigma(s)`

.. _palindromics-axioms:

------
Axioms
------

- :ref:`Axiom C.1: Delimiter Axiom <palindromics-axiom-c-1>`: :math:`\sigma \in \Sigma`
- :ref:`Axiom C.2: Character Comprehension Axiom <palindromics-axiom-c-2>`: :math:`\iota \in S`
- :ref:`Axiom W.1: Measure Axiom <palindromics-axiom-s-1>`: :math:`l(\alpha) \neq 0`
- :ref:`Axiom W.2: Discovery Axiom <palindromics-axiom-w-2>`: :math:`\alpha[i] \neq \sigma`
- :ref:`Axiom S.1: Word Comprehension Axiom <palindromics-axiom-s-1>`: :math:`\zeta[[i]] \in L`
- :ref:`Axiom S.2: Duality Axiom <palindromics-axiom-s-2>`: :math:`\exists \alpha: \alpha \subset_s \zeta`

.. _palindromices-theorems:

--------
Theorems
--------

- :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>`: :math:`l(st) = l(s) + l(t)`
- :ref:`Theorem 1.2.2 <palindromics-theorem-1-2-2>`: :math:`\varepsilon \subset_s s`
- :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`: :math:`{s^{-1}}^{-1} = s`
- :ref:`Theorem 1.2.4 <palindromics-theorem-1-2-4>`: :math:`(st)^{-1} = (t^{-1})(s^{-1})`
- :ref:`Theorem 1.2.5 <palindromics-theorem-1-2-5>`: :math:`u \subset_s v \equiv u^{-1} subset_s v^{-1}`
- :ref:`Theorem 1.3.1 <palindromics-theorem-1-3-1>`: :math:`\alpha \in I \equiv {\alpha}^{-1} \in I`
- :ref:`Theorem 1.3.2 <palindromics-theorem-1-3-2>`: :math:`R \subset I`
- :ref:`Theorem 1.3.3 <palindromics-theorem-1-3-1>`: :math:`s = \Pi_{i=1}^{n} p(i)` 
- :ref:`Theorem 1.4.1 <palindromics-theorem-1-4-1>`: :math:`\sum_{j=1}^{\Lambda(\zeta)} l(\zeta[[j]]) \geq \Lambda(\zeta)`
- :ref:`Theorem 1.4.2 <palindromics-theorem-1-4-2>`: :math:`\Lamdba(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)` 
- :ref:`Theorem 1.4.3 <palindromics-theorem-1-4-3>`: :math:`\zeta = \Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]]`
- :ref:`Theorem 1.4.4 <palindromics-theorem-1-4-4>`: :math:`(\Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]])^{-1} = \Pi_{i=1}^{\Lambda(\zeta)} (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}`
- :ref:`Theorem 1.4.5 <palindromics-theorem-1-4-5>`: :math:`\Lambda((s)(\varsigma)(t)) = \Lambda(s) + \Lambda(t)`
- :ref:`Theorem 1.4.6 <palindromics-theorem-1-4-6>`: :math:`C \subseteq D`
- :ref:`Theorem 1.4.7 <palindromics-theorem-1-4-7>`: :math:`Lambda((\zeta)(\varsigma)(\xi)) = \Lambda(\zeta) + \Lambda(\xi)`
- :ref:`Theorem 1.4.8 <palindromics-theorem-1-4-8>`: :math:`\zeta \in K \equiv {\zeta}^{-1} \in K`
- :ref:`Theorem 1.4.9 <palindromics-theorem-1-4-9>`: :math:`\zeta \in K \implies \zeta[[i]] \in I`
- :ref:`Theorem 1.4.7 <palindromics-theorem-1-4-7>`: :math:`\zeta \in K \implies {\zeta}^{-1}[[i]] = (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}`
- :ref:`Theorem 2.1.1 <palindromics-theorem-2-1-1>`: :math:`\Lambda(\zeta) = \Delta(\zeta) + 1`