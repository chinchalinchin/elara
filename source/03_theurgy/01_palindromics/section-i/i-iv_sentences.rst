.. _palindromics-section-i-iv:

Section I.IV: Sentences
=======================

A Sentence is a Limitation of Words over a Phrase in the Language's Lexicon for any value of :math:`n \geq 1`.

.. warning::

    This statement should not be interpretted as a schema for generating grammatical sentences. In general, Limitations are *not* grammatical. However, all grammatical sentences *are* Limitations.
    
    In other words, this statement should be interpretted as a necessary syntactic pre-condition a Sentence must satisfy before it may be assigned semantic content.

The Corpus is the aggregate of all Sentences.

.. math::

    \forall \zeta \in C: \exists n \in \mathbb{N}: \zeta = \Pi_i^{n} p(i)

.. note::

    The value of :math:`n` in the preceding equation will be further specified after several definitions and theorems. It will be shown to be directly and necessarily related to the Word structure of :math:`\zeta`.

The full semantic hierarchy has now been formalized. The hierarchy is summarized as follows,

1. Strings: :math:`\iota, \alpha, \zeta`
2. Sets: :math:`\Sigma, L, C`
3. Character Membership: :math:`\iota \in \Sigma`
4. Word Membership: :math:`\alpha \in L`
5. Sentence Membership: :math:`\zeta \in C`

These observations can be rendered into English,

1. All Characters, Words and Sentences are Strings.
2. The Alphabet, Languages and Corpus are sets of Strings.
3. All non-Empty Characters belong to an Alphabet.
4. All Words belong to the Language.
5. All Sentences belong to the Corpus.

.. _palindromics-word-length:

Word Length
-----------

.. _palindromics-definition-1-4-1:

.. topic:: Definition 1.4.1: Word Length

    Let :math:`s \in S` and :math:`n \in N` such that :math:`\zeta = \Pi_{i=1}^n p(i)`. The Word Length of :math:`\zeta`, denoted :math:`\Lambda(\zeta)`, is defined inductively through the following schema,

    - Basis: If :math:`\neg(\sigma \subset_s s)`,
        - If :math:`s = \varepsilon` or :math:`s \notin L`, :math:`\Lambda(s) = 0`
        - If :math:`s \in L`, :math:`\Lambda(s) = 1`
    - Induction: 
        - If :math:`s = {\sigma}{v}`, or if :math:`s = {u}{\sigma}{v}` and :math:`u \notin L`, then :math:`\Lambda(s) = \Lambda(v)`
        - If :math:`s = {u}{\sigma}{v}` and :math:`u \in L`, then :math:`\Lambda(s) = \Lambda(v) + 1`

.. important::

    The Induction clause of Word Length relies on the :ref:`Discovery Axiom <palindromics-axiom-v>` and the :ref:`Measureable Axiom <palindromics-axiom-iv>` to ensure for any Strings :math:`u \in L`, :math:`\neg(\sigma \subset_s u)` and :math:`u \neq \varepsilon`.

.. important::

    While Word Length will be primarily used on :math:`\zeta \in C`, it is important to note the definition is defined over all :math:`s \in S`. In other words, Word Length is a property of *Strings*, as can be seen in the example, "*blargafaful buttons*". 


**Example** Let :math:`ᚠ = \text{truth is beauty}`.

Let :math:`u_1 = \text{truth}` and :math:`v_1 = \text{is beauty}`. Then :math:`u_1 \in L_{\text{english}}` and :math:`ᚠ = (u_1)(\sigma)(v_1)`. Apply the Induction clause of :ref:`Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(ᚠ) = \Lambda(v_1) + 1

Let :math:`u_2 = \text{is}` and :math:`v_2 = \text{beauty}`. 

.. important::

    A selection of :math:`u_2 = \text{i}` or :math:`u_2 = \text{is be}` would not satisfy the condition :math:`s = {u}{\sigma}{v}` in the Induction clause, which requires :math:`u` and :math:`v` to be delimited with :math:`\sigma`.

Then :math:`u_2 \in L_{\text{english}}` and :math:`v_1 = (u_2)(\sigma)(v_2)`. Apply the Induction clause of :ref:`Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(v_1) = \Lambda(v_2) + 1

Finally, note :math:`v_2 \in L_{\text{english}}` and apply the Basis clause to :math:`v_2`,

.. math::

    \Lambda(v_2) = 1

Putting the recursion together,

.. math::

    \Lambda(ᚠ) = (1 + 1) + 1 = 3

∎

**Example** Let :math:`ᚠ = \text{palindromes vorpal semiordinlap}`

Let :math:`u_1 = \text{palindromes}` and :math:`v_1 = \text{vorpal semiordinlap}`. Then :math:`u_1 \in L_{\text{english}}` and :math:`ᚠ = (u_1)(\sigma)(v_1)`. Apply the Induction clause of :ref:`Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(ᚠ) = \Lambda(v_1) + 1

Let :math:`u_2 = \text{vorpal}` and :math:`v_2 = \text{semiordinlap}`. Then :math:`u_2 \notin L_{\text{english}}` and :math:`v_1 = (u_2)(\sigma)(v_2)`. Apply the Induction clause of :ref:`Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(v_1) = \Lambda(v_2)

Finally, note :math:`v_2 \in L_{\text{english}}` and apply the Basis clause to :math:`v_2`,

.. math::

    \Lambda(v_2) = 1

Putting the recursion together,

.. math::

    \Lambda(ᚠ) = (1 + 1) = 2

∎

.. important::

    As these examples demonstrate, the Word Length of a String is always *relative* to a given a Language. A subscript will be used to denote whether a Word Length is relative to a particular language, 
    
    .. math::
        
        \Lambda_{\text{english}}(\text{closing sale}) = 2

    Whereas,

    .. math::

        \Lambda_{\text{italian}}(\text{closing sale}) = 1

.. _palindromics-definition-1-4-2:

.. topic:: Definition 1.4.2: Word Indices

    The Word at index :math:`i` in a String :math:`s \in S`, denoted :math:`s[[i]]`, is defined inductively using the following schema,

    - Basis: 
        - :math:`s[[i]] = s` if and only if :math:`i = 1` and :math:`s \in L`
        - Otherwise, :math:`s[[i]]` is undefined.
    - Induction:
        - If :math:`s = {\sigma}{v}`, or if :math:`s = {u}{\sigma}{v}` and :math:`u \notin L`, then :math:`s[[i]] = v[[i]]`
        - If :math:`s = {u}{\sigma}{v}`, :math:`u \in L` and :math:`i = 1`, then :math:`s[[i]] = u`
        - If :math:`s = {u}{\sigma}{v}`, :math:`u \in L` and :math:`i > 1`, then :math:`s[[i]] = v[[i-1]]`

**Example** Let :math:`L = L_{\text{english}}`. Let :math:`ᚠ = \text{observe how system into system runs}`. Consider :math:`ᚠ[[3]]`.

Let :math:`u_1 = \text{observe}` and :math:`v_1 = \text{how system into system runs}`. Then :math:`ᚠ = (u_1)(\sigma)(v_1)`, :math:`u_1 \in L` and :math:`3 > 1`. Therefore, by the Induction clause of :ref:`Word Indices <palindromics-definition-1-4-2>`,

.. math::

    ᚠ[[3]] = v_1[[3-1]] = v_1[[2]]

At the next step, let :math:`u_2 = \text{how}` and :math:`v_2 = \text{system into system runs}`. Then :math:`v_1 = (u_2)(\sigma)(v_2)`, :math:`u_2 \in L` and :math:`2 > 1`,

.. math::

    v_1[[2]] = v_2[[1]]

At the next step, let :math:`u_3 = \text{system}` and :math:`v_3 = \text{into system runs}`. Then :math:`v_2 = (u_3)(\sigma)(v_3)`, :math:`u_3 \in L` but :math:`1 = 1`, therefore,

.. math::

    ᚠ[[3]] = v_1[[2]] = v_2[[1]] = u_3 = \text{system}

∎

**Example** Let :math:`ᚠ = \text{the gobberwarts with my blurglecruncheon}`. Consider :math:`ᚠ[2]`.

Let :math:`u_1 = \text{"the"}` and :math:`v_1 = \text{gobberwarts with my blurglecruncheon}`. Then :math:`ᚠ = (u_1)(\sigma)(v_1)`, :math:`u_1 \in L` and :math:`2 > 1`. Therefore, by the Induction clause of :ref:`Word Indices <palindromics-definition-1-4-2>`,

.. math::

    ᚠ[[2]] = v_1[[2-1]] = v_1[[1]]

At the next step, let :math:`u_2 = \text{gobberwarts}` and :math:`v_2 = \text{with my blurglecruncheon}`. Then :math:`v_1 = (u_2)(\sigma)(v_2)` but :math:`u_2 \notin L` and :math:`1 = 1`, so by the first condition of the Induction clause,

.. math::

    v_1[[1]] = v_2[[1]]

At the next step, let :math:`u_3 = \text{with}` and :math:`v_3 = \text{my blurglecruncheon}`. Then :math:`v_2 = (u_3)(\sigma)(v_3)`, :math:`u_3 \in L` and :math:`1 = 1`. So, the second condition of the Induction clause,

.. math::

    ᚠ[[2]] = v_1[[1]] = v_2[[1]] = u_3 = \text{with}

∎


.. note::

    The next theorems will not be required for the final postulates, but they are given to indicate the type of results that may be established regarding the concept of Word Length. For the curious reader, the details can be found in :ref:`Appendix I.II, Omitted Proofs <palindromics-appendix-i-ii>`.

.. _palindromics-theorem-1-4-1:

.. topic:: Theorem 1.4.1

    The sum of the String Lengths of the Words in a Sentence is atleast as great as the Word Length of the Sentence.

    .. math::

        \forall \zeta \in C: \sum_{j=1}^{\Lambda(\zeta)} l(\zeta[[j]]) \geq \Lambda(\zeta)

.. _palindromics-theorem-1-4-2:

.. topic:: Theorem 1.4.2

    The Word Length of the concatenation of two Sentences is no more than the sum of their individual Word Lengths.

    .. math::

        \forall \zeta, \xi \in C: \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)

.. note::

    :ref:`Theorem 1.4.1 <palindromics-theorem-1-4-1>` and :ref:`Theorem 1.4.2 <palindromics-theorem-1-4-2>` demonstrate Word Length is fundamentally different than String Length with respect to the operation of concatenation. In :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>`, it was shown String Length sums over concatenation. :ref:`Theorem 1.4.1 <palindromics-theorem-1-4-1>` shows the corresponding property is not necessarily true for Word Length. This is an artifact of the potential destruction of semantic content that may occur upon concatenation. (The edge case of compound Words (e.g. *daylight*) makes the proof :ref:`Theorem 1.4.2 <palindromics-theorem-1-4-2>` particularly interesting.)

    Indeed, most algebraic properties of *String Length* do not extend up the semantic hierarchy. For example, it is easily seen, in general, 

    .. math::

        \Lambda(\zeta^{-1}) \neq \Lambda(\zeta)

    However, there is a special class of sentences where this property does hold, as will be seen in :ref:`Theorem 1.4.12 <palindromics-theorem-1-4-12>`.

.. _palindromics-sentence-theorems:

Theorems
--------

The first theorem demonstrates the relationship between a Limitation and Word Length that was pointed out in the introduction of this subsection.

.. _palindromics-theorem-1-4-3:

.. topic:: Theorem 1.4.3

    .. math::

        \forall \zeta \in C: \zeta = \Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]]

**Proof** Let :math:`\zeta \in C`. By definition of a Sentence, there exists :math:`n \in \mathbb{N}` and :math:`p \in L_n` such that

.. math::

    p = (\alpha_1, \alpha_2, ... , \alpha_n)

.. math::

    \zeta = \Pi_{i=1}^{n} p(i)

So that, applying the :ref:`definition of Limitations <palindromics-definition-1-3-5>`,

.. math::

    \zeta = (\alpha_1)(\sigma)(\alpha_2)(\sigma)...(\sigma)(\alpha_n) \quad \text{ (1) }
    
By the :ref:`definition of Word Length <palindromics-definition-1-4-1>`, with :math:`u = \alpha_1` and :math:`v = \Pi_{i=1}^{n-1} \alpha_{i+1}`

.. math::

    \Lambda(\zeta) = \Lambda(\Pi_{i=1}^{n-1} \alpha_{i+1}) + 1

Since there are :math:`n` words in :math:`p`, it follows the :ref:`definition of Word Length <palindromics-definition-1-4-1>` will be applied :math:`n` times, resulting in,

.. math::

    \Lambda(\zeta) = n

Now, apply the :ref:`definition of Word Indices <palindromics-definition-1-4-2>` to (1). The Basis clause yields,

.. math::

    \zeta[[1]] = \alpha_1

Using the Induction clause with :math:`u = \alpha_1` and :math:`v = \Pi_{i=1}^{n-1} \alpha_{i+1}`,

.. math::

    \zeta[[2]] = v[[1]] = \alpha_2

Where the last equality follows from the Basis clause applied to :math:`v`. Continuing this process, it is found,

.. math::

    \forall i \in N_n: \zeta[[i]] = \alpha_i

Therefore, since the Words in the Sentence correspond index by index to the Words in the Phrase, and the Word Length of the Sentence is equal to the Word Length of the Phrase, it follows, 

.. math::

    \forall \zeta \in C: \zeta = \Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]]

∎

.. note::

    The next theorem can be seen as a specialiation of :ref:`Theorem 1.2.5 <palindromics-theorem-1-2-5>` for the subdomain of the Corpus.

.. _palindromics-theorem-1-4-4:

.. topic:: Theorem 1.4.4

    The inverse of a Limitation is the Limitation of inverses.

    .. math::

        \forall \zeta \in C: (\Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]])^{-1} = \Pi_{i=1}^{\Lambda(\zeta)} (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}


**Proof** Let :math:`\zeta \in C`. Let :math:`n = \Lambda(\zeta)`. Let :math:`s`,

.. math::

    s = \Pi_{i=1}^{n} \zeta[[i]] \quad \text{ (1) }

.. math::

    = (\zeta[[1]])(\sigma)(\zeta[[2]]) ... (\sigma)(\zeta[[n]])

Consider :math:`s^{-1}`,

.. math::

    s^{-1} = ((\zeta[[1]])(\sigma)(\zeta[[2]]) ... (\sigma)(\zeta[[n]]))^{-1}

From :ref:`String Inversion <palindromics-definition-1-2-8>` and the fact :math:`l(\sigma) = 1`, it follows :math:`\sigma^{-1} = \sigma`. Using this fact, the application of :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-10>` :math:`n` times yields,

.. math::

    s^{-1} = ({\zeta}^{-1}[[n]])(\sigma)({\zeta}^{-1}[[n-1]]) ... (\sigma)({\zeta}^{-1}[[1]])

Reindex the terms on the RHS to match :ref:`Limitation <palindromics-definition-1-3-5>` with :math:`j = n - i + 1`. Then, as :math:`i` goes from :math:`1 \to n`, :math:`j` goes :math:`n \to 1` and visa versa,

.. math::

    = \Pi_{i=1}^{n} {\zeta[[n - i + 1]]}^{-1} \quad \text{ (2) }

Combining (1) and (2) and generalizing,

.. math::

    \forall \zeta in C: (\Pi_{i=1}^{n} \zeta[[i]])^{-1} = \Pi_{i=1}^{n} (\zeta[[n - i + 1]]^{-1})

∎

.. _palindromics-theorem-1-4-5:

.. topic:: Theorem 1.4.5

    For any two Strings in the Dialect, the Word Length of their Limitation is the sum of their individual Word Lengths.

    .. math::

        \forall s,t \in D: \Lambda((s)(\sigma)(t)) = \Lambda(s) + \Lambda(t)

**Proof** Let :math:`s, t \in D`. That is, assume, for some :math:`n, m \in \mathbb{N}`,

.. math::

    s = \Pi_{i=1}^{n} p(i)

.. math::

    t = \Pi_{i=1}^{m} q(i)

where :math:`n = \Lambda(s)` and :math:`m = \Lambda(t)`.

The proof proceeds by induction on :math:`n`.

:underline:`Basis`: Assume :math:`n = 1`. 

Then, by the Basis clause of :ref:`Limitations <palindromics-definition-1-3-5>`, :math:`s = \alpha` for some :math:`\alpha \in L`. By the :ref:`Discovery Axiom <palindromics-axiom-v>`, :math:`\neg(\sigma \subset_s \alpha)`. 

Consider :math:`u = (\alpha)(\sigma)(t)`. By the Basis clause of :ref:`Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(u) = \Lambda(\alpha) + \Lambda(t)

.. math::

    \Lambda((s)(\sigma)(t)) = \Lambda(s) + \Lambda(t)

:underline:`Induction` Assume for any :math:`u \in D` with :math:`\Lambda(u) = n`,

.. math::

    \Lambda((u)(\sigma)(t)) = \Lambda(u) + \Lambda(t)

Let :math:`s \in D` such that :math:`\Lambda(s) = n + 1`. By the Induction clause of the :ref:`Dialects <palindromics-definition-1-3-6>` and :ref:`Limitations <palindromics-definition-1-3-5>`,

.. math::

    s = (\alpha)(\sigma)(v)

By the Induction clause of :ref:`Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(s) = \Lambda(\alpha) + \Lambda(v)

.. math::

    \Lambda(s) = 1 + \Lambda(v) \quad \text{ (1) }

From this and :math:`\Lambda(s) = n + 1`, it is concluded :math:`\Lambda(v) = n` and therefore satisfies the inductive hypothesis.

Consider :math:`\Lambda((s)(\sigma)(t))`.

.. math::

    \Lambda((s)(\sigma)(t)) = \Lambda((\alpha)(\sigma)(v)(\sigma)(t))

.. math::

    = \Lambda(\alpha) + \Lambda((v)(\sigma)(t))

.. math::

    = 1 + \Lambda(v) + \Lambda(t)

But from (1), this reduces to,

.. math::

    = \Lambda(s) + \Lambda(t)

Therefore, putting everything together, the Induction is complete,

.. math::

    \Lambda((s)(\sigma)(t)) =  \Lambda(s) + \Lambda(t)

Summarizing and generalizing,

.. math::

    \forall s,t \in D: \Lambda((s)(\sigma)(t)) = \Lambda(s) + \Lambda(t)

∎


.. important::

    Theorem 1.4.5 *only* applies to Strings quantified over the Dialect. If the theorem were quantified over the Corpus, i.e. semantic Sentences, then the inductive hypothesis would fail at the step where the induced String is decomposed,

    .. math::

        s = (\alpha)(\sigma)(u)
    
    To see this, note that when a Sentence has it's first Word partitioned from it, there is no guarantee the resultant will also be a semantic Sentence, e.g. "*we are the stuffed men*" is a Sentence, but "*are the stuffed men*" is not a Sentence. Therefore, the theorem must be induced over the Dialect. 

    This may seem a strong restriction, but as the next two theorems establish, this result still applies to the Corpus.


.. _palindromics-theorem-1-4-6:

.. topic:: Theorem 1.4.6

    The Corpus is a subset of the Dialect.

    .. math::

        C \subseteq D

**Proof** Let :math:`\zeta \in C`. By definition of a Sentence,

.. math::

    \zeta = \Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]]

By the :ref:`definition of a Dialect <palindromics-definition-1-3-6>`, :math:`\zeta \in D`.

Therefore, :math:`\zeta \in C \implies \zeta \in D`. This is exactly the definition of a subset,

.. math::

    C \subseteq D

∎

.. _palindromics-theorem-1-4-7:

.. topic:: Theorem 1.4.7

    For any two Sentences in the Corpus, the Word Length of their Limitation is the sum of their individual Word Lengths.

    .. math::

        \forall \zeta,\xi \in C: \Lambda((\zeta)(\sigma)(\xi)) = \Lambda(\zeta) + \Lambda(\xi)
    

**Proof** Let :math:`\zeta, \xi \in C`. 

By :ref:`Theorem 1.4.6 <palindromics-theorem-1-4-6>`, :math:`C \subseteq D`. By definition of subsets, 

.. math::

    \zeta, \xi \in C \implies \zeta, \xi \in D 

Therefore, by :ref:`Theorem 1.4.5 <palindromics-theorem-1-4-5>`,

.. math::

    \forall \zeta, \xi \in C: \Lambda((\zeta)(\sigma)(\xi)) = \Lambda(\zeta) + \Lambda(\xi)

∎

.. _palindromics-theorem-1-4-8:

.. topic:: Theorem 1.4.8

    The Corpus is a subset of the Canon.

    .. math::

        C \subseteq \mathbb{S}

**Proof** Let :math:`\zeta \in C`. By :ref:`Theorem 1.4.3 <palindromics-theorem-1-4-3>`,

.. math::

    \zeta = \Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]]

By the definition of Sentences and :ref:`Canonization Axiom <palindromics-axiom-vi>`,

.. math::

    \zeta[[i]] \in \mathbb{S}

By the :ref:`definition of Canonization <palindromics-definition-1-3-6>`,

.. math::

    \pi(\sigma) = \sigma

By the :ref:`definition of Limitation <palindromics-definition-1-3-5>`, :math:`\Pi` produces Strings through Concatenation. By :ref:`Theorem 1.2.6 <palindromics-theorem-1-2-6>`, the Canon is closed over Concatenation. From this, it must be the case :math:`\zeta \in \mathbb{S}`. Therefore,

.. math::

    \zeta \in C \implies \zeta \in \mathbb{S}

This is exactly the definition of subsets,

.. math::

    C \subseteq \mathbb{S}

∎

.. _palindromics-sentence-classes:

Classes
-------

.. _palindromics-definition-1-4-3:

.. topic:: Definition 1.4.3: Invertible Sentences

    Let :math:`\zeta \in C`. Then the set of Invertible Sentences, denoted :math:`J`, is defined as the set of Sentences which satisfy the following open formula,

    .. math::

        \zeta \in J \equiv {\zeta}^{-1} \in C

    A Sentence that belongs to :math:`J` will be referred to as "*invertible*".

.. note::

    Invertible Words are sometimes called *semiordinalps* in other fields of study. However, the term "*semiordinalip*" will be given a more precise and formal explication with the introducion and :ref:`definition of Subvertible Sentences <palindromics-definition-2-2-3>` in the next section.

.. _palindromics-theorem-1-4-9:

.. topic:: Theorem 1.4.9

    A Sentence is invertible if and only if its inverse is invertible.

    .. math::

        \forall \zeta \in C: \zeta \in J \equiv {\zeta}^{-1} \in J

**Proof** Let :math:`\zeta \in C`.

(:math:`\rightarrow`) Assume :math:`\zeta \in J`. By the :ref:`definition of Invertible Sentences <palindromics-definition-1-4-3>`,

.. math::

    {\zeta}^{-1} \in C

By :ref:`Theorem 1.2.9 <palindromics-theorem-1-2-9>`,

.. math::

    ({\zeta}^{-1})^{-1} = \zeta

By assumption, :math:`\zeta \in C`, therefore, by the :ref:`definition of Invertible Sentences <palindromics-definition-1-4-3>`,

.. math::

    {\zeta}^{-1} \in J

(:math:`\leftarrow`) Assume :math:`{\zeta}^{-1} \in J`, which implies :math:`{\zeta}^{-1} \in C`. By assumption :math:`\zeta \in C`. Therefore, :ref:`definition of Invertible Sentences <palindromics-definition-1-4-3>`,

.. math::

    \zeta \in J

Summarizing and generalizing,

.. math::

    \forall \zeta \in C: \zeta \in J \equiv {\zeta}^{-1} \in J

∎

.. _palindromics-theorem-1-4-10:

.. topic:: Theorem 1.4.10

    If a Sentence in the Corpus is invertible, then all of the Words are also invertible.

    .. math::

        \forall \zeta \in J: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \in I

**Proof** Let :math:`\zeta \in J`. By the :ref:`definition of Invertible Sentences <palindromics-definition-1-4-3>`,

.. math::

    {\zeta}^{-1} \in C

By :ref:`Theorem 1.4.4 <palindromics-theorem-1-4-4>`, this can be written,

.. math::

    {\zeta}^{-1} = \Pi_{i=1}^{n} p(i)

where, 

.. math::

    p = ( {\zeta[[n]]}^{-1}, {\zeta[[n-1]]}^{-1}, ... , {\zeta[[1]]}^{-1} )

By definition of a Sentence and :math:`{\zeta}^{-1} \in C`,

.. math::

    \forall i \in N_{\Lambda(\zeta)}: {{\zeta}^{-1}}[[i]] \in L

From this, it can be concluded every :math:`{\zeta[[i]]}^{-1}` in :math:`p` must belong to :math:`L`, and each of those Words has an inverse that is also in :math:`L`.

By :ref:`the definition of Invertible Words <palindromics-definition-1-3-2>`, the inverse of a Word can only belong to a Language if and only if the Word is invertible.

.. math::

    \forall i \in N_{\Lambda(\zeta)}: {{\zeta}^{-1}}[[i]] \in I

Therefore,

.. math::

    \forall i \in N_{\Lambda(\zeta)}: {\zeta[[i]]}^{-1} \in I

By :ref:`Theorem 1.3.1 <palindromics-theorem-1-3-1>`, 

.. math::

    \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \in I

Generalizing,

.. math::

    \forall \zeta \in J: \forall i \in N_{\Lambda(\zeta)}: \zeta[[i]] \in I

∎

.. _palindromics-theorem-1-4-11:

.. topic:: Theorem 1.4.11

    If a Sentence is invertible, then the :math:`i^{\text{th}}` Word in its inverse Sentence is equal to the inverse of the :math:`i^{\text{th}}`-to-last Word in the Sentence.

    .. math::

        \forall \zeta \in J: \forall i \in N_{\Lambda(\zeta)}: {\zeta}^{-1}[[i]] = (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}

**Proof** Let :math:`\zeta \in J`, let :math:`n = \Lambda(\zeta)` and let :math:`i \in N_n`.

By :ref:`Theorem 1.4.6 <palindromics-theorem-1-4-8>` and assumption,

.. math::

    \forall i \in N_n: \zeta[[i]] \in I

By :ref:`Theorem 1.3.1 <palindromics-definition-1-3-3>`,

.. math::

    \forall i \in N_n: (\zeta[[i]])^{-1} \in I

Consider,

.. math::

   \Pi_{i=1}^{n} (\zeta[[n - i + 1]])^{-1}

By :ref:`Theorem 1.4.4 <palindromics-theorem-1-4-4>`,

.. math::

    (\Pi_{i=1}^{n} \zeta[[i]])^{-1}

And by definition of Sentences and :ref:`Limitations <palindromics-definition-1-3-5>`,

.. math::

    \zeta = \Pi_{i=1}^{n} \zeta[[i]]

Therefore,

.. math::

    (\zeta)^{-1} = \Pi_{i=1}^{n} (\zeta[[n - i + 1]])^{-1}

By the :ref:`Theoreom 1.4.8 <palindromics-theorem-1-4-8>`, :math:`C \subset \mathbb{S}`. By :ref:`Theorem 1.3.3 <palindromics-definition-1-3-3>`, Limitations are unique over the Canon, thus the only way two Limitations that belong to the Corpus can be equal to :math:`\zeta^{-1}` is when,

.. math::

    {{\zeta}^{-1}}[[i]] = (\zeta[[n - i + 1]])^{-1}

Summarizing and generalizing,

.. math::

    \forall \zeta \in J: \forall i \in N_{\Lambda(\zeta)}: {\zeta}^{-1}[[i]] = (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}

∎

.. _palindromics-theorem-1-4-12:

.. topic:: Theorem 1.4.12:

    The Word Length of every Invertible Sentence is equal to the Word Length of its Inverse.

    .. math::

        \forall \zeta \in J: \Lambda(\zeta) = \Lambda(\zeta^{-1})

**Proof** Let :math:`\zeta \in J` with :math:`n = \Lambda(\zeta)`

By :ref:`Theorem 1.4.10 <palindromics-theorem-1-4-10>`,

.. math::

    \forall i \in N_n: \zeta[[i]] \in I

By :ref:`definition of Invertible Words <palindromics-definition-1-3-2>`,

.. math::

    \forall i \in N_n: (\zeta[[i]])^{-1} \in L

By :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>`,

.. math::

    \forall i \in N_n: {{\zeta}^{-1}}[[n - i + 1]] \in L

Note for :math:`1 \leq i \leq n`, :math:`n - i + 1` is a decreasing, consecutive function that goes :math:`n \to 1`. Therefore, every Word of the Inverse belongs to the Language and by :ref:`by definition of Word Length <palindromics-definition-1-4-1>`,

.. math::

    \Lambda(\zeta) = \Lambda(\zeta^{-1})

Summarizing and generalizing, 

.. math::

    \forall \zeta \in J: \Lambda(\zeta) = \Lambda(\zeta^{-1})

∎

.. _palindromics-partial-sentences:

Partial Sentences
-----------------

.. _palindromics-definition-1-4-4:

.. topic:: Definition 1.4.4: Partial String

    Let :math:`s \in S` with :math:`n = l(s)`. Let :math:`i \in N_n`.

    **Right Partial String** :math:`s[i:]`

    - Basis: :math:`s[n:] = s[n]`
    - Induction: :math:`s[i:] = (s[i])s[i+1:]`

    **Left Partial String** :math:`s[:i]`

    - Basis: :math:`s[:1] = s[1]`
    - Induction: :math:`s[:i] = (s[:i-1])s[i]`

    When :math:`s \in C`, :math:`s[i:]` and :math:`s[:i]` are called Partial Sentences.

**Example** Let :math:`ᚠ = \text{form is the possibility of structure}`. Then :math:`l(ᚠ) = 36`.

Consider :math:`ᚠ[:4]`. Applying the :ref:`definition of Partial String <palindromics-definition-1-4-4>`, the Left Partial Sentence is given by, 

.. math::

    ᚠ[:4] = (ᚠ[:3])ᚠ[4] = ((ᚠ[:2])ᚠ[3])ᚠ[4]=((ᚠ[:1](ᚠ[2]))ᚠ[3])ᚠ[4] = ((ᚠ[1](ᚠ[2]))ᚠ[3])ᚠ[4]

Thus :math:`ᚠ[:4] = \text{form}`.

Consider :math:`ᚠ[10:]`. The Right Partial Sentence is given by,

.. math::

    ᚠ[10:] = ᚠ[10]ᚠ[11:] = ᚠ[10]ᚠ[11]ᚠ[12:] = ... = ᚠ[10]ᚠ[11]...ᚠ[36]

Thus :math:`ᚠ[10:] = \text{he possibility of structure}` 

∎

.. important::

    Note Partial Sentences are **not** part of the Corpus.

.. _palindromics-theorem-1-4-13:

.. topic:: Theorem 1.4.13 

    The String Length of a Left Partial Right :math:`s[:i]` is :math:`i`.

    .. math::

        \forall s \in S: \forall i \in N_{l(s)}: l(s[:i]) = i

**Proof** Let :math:`s \in S`. Let :math:`n = l(s)`. Let :math:`i \in N_n`. The proof proceeds by induction on :math:`i`.

.. BASIS 

:underline:`Basis`: :math:`i = 1`

By :ref:`definition of Left Partial Strings <palindromics-definition-1-4-4>`,

.. math::

    s[:1] = s[i]

Since :math:`s[i]` is a single Character, it follows from the :ref:`definition of String Length <palindromics-definition-1-2-2>`,

.. math::

    l(s[1]) = 1

.. INDUCTION

:underline:`Induction`: Assume for a fixed :math:`1 < i \leq n - 1`, :math:`l(s[:i]) = i`.

Since :math:`i` is at most :math:`n - 1`, :math:`i + 1` is at most :math:`n`. Therefore, :math:`s[:i+1]` is defined. By the Induction clause :ref:`Left Partial Strings <palindromics-definition-1-4-4>`,

.. math::

    s[:i+1] = s[:i]s[i+1]

By :ref:`Thoerem 1.2.1 <palindromics-theorem-2-2-1>`,

.. math::

    l(s[:i+1]) = l(s[:i]) + l(s[i+1])

The first term on the RHS is :math:`i` by inductive hypothesis and the second term is :math:`1` by :ref:`definition of String Length <palindromics-definition-1-2-2>`,

.. math::

    l(s[:i+1]) = i + 1

The Induction is thus established for :math:`i \in N_n`. Summarizing and generalizing,

.. math::

    \forall S: \forall i \in N_n: l(s[:i]) = i

∎

.. _palindromics-theorem-1-4-14:

.. topic:: Theorem 1.4.14

    The String Length of a Right Partial String :math:`s[i:]` is equal :math:`l(s) - i + 1`
    
    .. math::

        \forall s \in S: l(s[i:]) = l(s) - i + 1

**Proof** Let :math:`s \in S`. Let :math:`n = l(s)`. Consider :math:`s[i:]` with :math:`i \in N_n`. Let 

.. math::
    
    j = n - i + 1
    
Then :math:`j \in N_n`, since :math:`i = 1 \implies j = n` and :math:`i = n \implies j = 1`. The proof proceeds by induction on :math:`j`.
 
.. BASIS

:underline:`Basis`: :math:`j = 1`. Then :math:`i = n`. 

.. math::

    s[n:] = s[n]

.. math::

    l(s[n:]) = 1 = n - n + 1

.. INDUCTION

:underline:`Induction`: Assume for a fixed :math:`1 < j \leq n - 1`, :math:`l(s[i:]) = l(s) - i + 1`.

Now, 

.. math::


    1 < j \leq n - 1 \equiv 1 < n - i + 1 \leq n - 1 

From which follows,

.. math::

    2 < i \leq n

Therefore, :math:`s[i-1:]` is defined. By the Induction clause of :ref:`Right Partial Strings <palindromics-definition-1-4-4>`,

.. math::

    s[i-1:] = s[i-1]s[i:]

Therefore, 

.. math::

    l(s[i-1:]) = l(s[i-1]) + l(s[i:]) = l(s[i:]) + 1

The first term on the RHS is :math:`l(s) - i + 1` by inductive hypothesis,

.. math::

    l(s[i-1:]) = l(s) - i + 1 + 1 
    
Rewriting to make the induction obvious,

.. math::

    l(s[i-1:]) = l(s) -  (i - 1) + 1

The induction is established. Summarizing and generalizing,

.. math::

    \forall s \in S: l(s[i:]) = l(s) - i + 1

∎

.. note::

    The proofs of :ref:`Theorem 1.4.15 <palindromics-theorem-1-4-15>` and :ref:`Theorem 1.4.16 <palindromics-theorem-1-4-16>` are similar to the proofs of :ref:`Theorem 1.4.13 <palindromics-theorem-1-4-13>` and :ref:`Theorem 1.4.14`. The proofs are omitted and can be found in :ref:`Appendix I.II, Omitted Proofs<palindromics-omitted-proofs-i-iv>`.

.. _palindromics-theorem-1-4-15:

.. topic:: Theorem 1.4.15

    .. math::

        \forall s \in S: s[:l(s)] = s 

∎

.. _palindromics-theorem-1-4-16:

.. topic:: Theorem 1.4.16

    .. math::

        \forall s \in S: s[1:] = s

∎

.. _palindromics-theorem-1-4-17:

.. topic:: Theorem 1.4.17

    The Concatenation of a Left Partial String with its Right Partial String is the String. 

    .. math::

        \forall s \in S: \forall i \in N_{l(s) - 1}: s = (s[:i])(s[i+1:])

**Proof** Let :math:`s \in S` with :math:`n = l(s)`. 

If :math:`n = 1`, then :math:`s[i+1:]` is undefined, so the proof proceeds by induction on String Length, starting at :math:`l(s) = 2`.

:underline:`Basis`: :math:`n = 2`. Then, by :ref:`definition of Character Indices <palindromics-definition-1-2-3>`, 

.. math::
    
    s = (s[1])(s[2])
    
By :ref:`definition of Partial Strings <palindromics-definition-1-4-4>`,

.. math::

    s[:1] = s[1]

.. math::

    s[2:] = s[2]

Thus, 

.. math::

    s = (s[:1])(s[2:])

:underline:`Induction`: Assume for all :math:`i` and all :math:`s \in S`, :math:`s = (s[:i])(s[i+1:])` for some fixed :math:`l(s) = m`,

Let :math:`t \in S` such that :math:`l(t) = m + 1`. 

.. TODO: ........................................................................

∎