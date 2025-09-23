.. _palindromics-section-i-iii:

Section I.III: Words
====================

.. important::

    To reiterate the introduction to this section, the current formal system does not seek to describe a generative grammar. Its theorems cannot be used as schema for generating grammatical sentences. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations.

A Word is a type of String constructed through concatenation that has been assigned by semantic content. A Language is the aggregate of all Words.

.. math::

    \forall \alpha \in L: \alpha \in S

Or equivalently,

.. math::

    L \subset S

.. _palindromics-axiom-iv:

.. topic:: Axiom IV: Measure

    No Words have a String Length of 0.

    .. math::

        \forall \alpha \in L: l(\alpha) \neq 0

.. _palindromics-axiom-v:

.. topic:: Axiom V: Discovery

    No Character in a Word can be a Delimiter. 

    .. math::

       \forall \alpha \in L: \forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma

.. _palindromics-axiom-vi:

.. topic:: Axiom VI: Canonization

    All Words are canonical.

    .. math::

        \forall \alpha \in L: \alpha \in \mathbb{S}

.. _palindromics-word-classes:

------------
Word Classes 
------------

.. _palindromics-definition-1-3-1:

.. topic:: Definition 1.3.1: Reflective Words

    Let :math:`\alpha \in L`. :math:`\alpha` belongs to the set of Reflective Words, denoted :math:`R`, if it satisfies the open formula,

    .. math::

        (\alpha \in R) \equiv (\alpha = {\alpha}^{-1})

    A Word will be referred to as *reflective* if it belongs to the class of Reflective Words.

.. note::

    :math:`R` may be defined equivalently through set builder notation,

    .. math::

        R = \{ \alpha \in L \mid \alpha = {\alpha}^{-1} \}

**Example** The following table lists some reflective English words.

.. list-table:: 
    :widths: 50
    :header-rows: 1
    
    * - Word
    * - mom
    * - dad
    * - noon
    * - racecar
    * - madam
    * - level
    * - civic

∎

.. _palindromics-definition-1-3-2:

.. topic:: Definition 1.3.2: Invertible Words

    Let :math:`\alpha \in L`. :math:`\alpha` belongs to the set of Invertible Words, denoted :math:`I`, if it satisfies the open formula,

    .. math::

        (\alpha \in I) \equiv ({\alpha}^{-1} \in L)

    A Word will be referred to as *invertible* if it belongs to the class of Invertible Words.

.. important::

    A Word is invertible if and only if its inverse belongs to the Language. 

**Example** The following table lists some English words and their inverses (where applicable).

.. list-table::
    :widths: 20 20
    :header-rows: 1

    * - Word
      - Inverse
    * - time
      - emit
    * - saw
      - was
    * - raw
      - war
    * - dog
      - god
    * - pool
      - loop
    * - cat
      - x
    * - you
      - x
    * - help
      - x
    * - door
      - x
    * - book
      - x

∎

.. note::

    Invertible Words are often called *semiordnilaps* in other fields of study.


.. _palindromics-theorem-1-3-1:

.. topic:: Theorem 1.3.1

    A Word is invertible if and only if its inverse is invertible.

    .. math::

        \forall \alpha \in L: \alpha \in I \equiv {\alpha}^{-1} \in I

**Proof** Let :math:`\alpha \in L`.

(:math:`\rightarrow`) Assume :math:`\alpha \in I`. By :ref:`the definition of invertible Words <palindromics-definition-1-3-2>`,

.. math::

    {\alpha}^{-1} \in L

By :ref:`Theorem 1.2.8 <palindromics-theorem-1-2-8>`,

.. math::

    ({\alpha}^{-1})^{-1} = \alpha

Therefore, by assumption,

.. math::

    ({\alpha}^{-1})^{-1} \in L

By :ref:`the definition of invertible Words <palindromics-definition-1-3-2>`,

.. math::

    {\alpha}^{-1} \in I

(:math:`\leftarrow`) Assume :math:`{\alpha}^{-1} \in L` such that :math:`{\alpha}^{-1} \in I`. By :ref:`the definition of invertible Words <palindromics-definition-1-3-2>`,

.. math::

    ({\alpha}^{-1})^{-1} \in L

By :ref:`Theorem 1.2.8 <palindromics-theorem-1-2-8>`,

.. math::

    \alpha \in L 

Since :math:`{\alpha}^{-1} \in L` by assumption, it follows immediately from :ref:`the definition of invertible Words <palindromics-definition-1-3-2>`,

.. math::

    \alpha \in I

Summarizing and generalizing,

.. math::

    \forall \alpha \in L: \alpha \in I \equiv {\alpha}^{-1} \in I

∎

.. _palindromics-theorem-1-3-2:

.. topic:: Theorem 1.3.2

    Reflective Words are a subset of Invertible Words.

    .. math::

        R \subset I

**Proof** Let :math:`\alpha in R` and :math:`l(\alpha) = n`. By :ref:`the definition of Reflective Words <palindromics-definition-1-3-1>`,

.. math::

    \alpha = \alpha^{-1}

Since :math:`\alpha \in L` by assumption, it follows :math:`\alpha in I`. In other words,

.. math::

    \alpha \in R \implies \alpha \in I

But this is exactly the definition of the subset relation in set theory, therefore,

.. math::

    R \subset I

∎

.. _palindromics-limitations:

-----------
Limitations
-----------

.. _palindromics-definition-1-3-3:

.. topic:: Definition 1.3.3: Phrases

    Let :math:`n \in \mathbb{N}`. A Phrase of Word Length :math:`n`, denoted :math:`P_n`, is defined as an ordered sequence of :math:`n` Words, not necessarily distinct,

    .. math::

        P_n = \{ (i, \alpha_i) \mid i \in N_n \land \alpha \in L \} 

    .. math::

        P_n = (\alpha_1, \alpha_2, ..., \alpha_n)

    where each :math:`\alpha_i \in L`. If :math:`1 \leq i \leq n`, :math:`P_n(i)` denotes the Word :math:`\alpha_a` at index :math:`i` of the Phrase, so the Phrase may be written,

    .. math::

        P_n = (P_n(1), P_n(2), ... P_n(n))

    When :math:`n = 0`, a Phrase is defined to be :math:`\varnothing`,

    .. math::

        P_0 = \varnothing

.. _palindromics-definition-1-3-4:

.. topic:: Definition 1.3.4: Lexicons

    Let :math:`n \in \mathbb{N}`. A Language's :math:`n^{\text{th}}` Lexicon, denoted :math:`L_n`, is defined as the set of all Phrases of length :math:`n`,

    .. math::

        L_n = \{ p \mid \forall p: p = P_n \}

.. _palindromics-definition-1-3-5:

.. topic:: Defintion 1.3.5: Limitation 
    
    Let :math:`p \in L_n`. The Limitation of :math:`p`, denoted :math:`\Pi_{i=1}^{n} p(i)` is defined inductively using the following schema,

    - Empty: :math:`\Pi_{i=1}^{0} p(i) = \varepsilon`
    - Basis: :math:`\Pi_{i=1}^{1} p(i) = \alpha_1`
    - Induction: :math:`\Pi_{i=1}^{n} p(i) = (\Pi_{i=1}^{n-1} p(i))(\sigma)(\alpha_n)`

    The process of Limitation, :math:`\Pi_{i=1}^{n} p(i)`, will be referred to as "*delimiting*" a Phrase or Words.

.. note::

    A :ref:`Limitation <palindromics-definition-1-3-5>`, though notationally complex, can be understood as shorthand for the iterated concatenation of words and Delimiters. is the presence of the Delimiter in the Induction clause. In other words, a Limitation inserts Delimiters inbetween each Word in the Lexicon over which the index is ranging.

**Example** Let :math:`L = L_english`. Consider calculating the Limitation of the following Phrase,

.. math::

    P_3 = (\text{mother}, \text{may}, \text{i})

Apply the Basis clause :ref:`Limitations <palindromics-definition-1-3-5>` ,

.. math::

    n = 1: \quad \Pi_{i=1}^{1} \alpha_i = \text{mother} 

The Limitation can then be built up recursively using the Induction clause,

.. math::

    n = 2: \quad \Pi_{i=1}^{2} \alpha_i = (\Pi_{i=1}^{1} \alpha_i)(\sigma)(\text{may})= (\text{mother})(\sigma\text{may}) = \text{mother}\sigma\text{may}
    
.. math::

    n = 3: \quad \Pi_{i=1}^{3} \alpha_i = (\Pi_{i=1}^{2} \alpha_i)(\sigma)(\text{i}) = (\text{mother}\sigma\text{may})(\sigma\text{i}) = \text{mother}\sigma\text{may}\sigma\text{i}

So the Limitation of the Phrase is shown to be,

.. math::

    \Pi_{i=1}^{3} \alpha_i = \text{mother may I} 

.. important::

    The result of a Limitation is a String. Since a Limitation is shorthand for alternating concatenation of Characters and Delimiters, the closure of Limitations over :math:`S` is guaranteed by the closure of concatenation over :math:`S`

∎

.. _palindromics-theorem-1-3-3:

.. topic:: Theorem 1.3.3

    All Limitations are unique within the Canon.

    .. math::

        \forall n \in \mathbb{N}: \forall p \in L_n: \exists! s \in \mathbb{S}: s = \Pi_{i=1}^{n} p(i)

**Proof** Let :math:`n \in \mathbb{N}` and :math:`p \in L_n` such that,

.. math::

    p = (\alpha_1, \alpha_2, ..., \alpha_n)

The proof will proceed by induction on :math:`n`.

:underline:`Basis`: Assume :math:`n = 1`. By Basis clause of :ref:`Limitations <palindromics-definition-1-3-5>`,

.. math::

    \Pi_{i=1}^{1} p(i) = \alpha_1

:underline:`Induction`: Assume for :math:`k \geq 1`, these exists a unique String :math:`s_k` such that,

.. math::

    s_k = \Pi_{i=1}^{k} p(i)

By Induction clause of :ref:`Limitations <palindromics-definition-1-3-5>`,

.. math::

    \Pi_{i=1}^{k+1} p(i) = (\Pi_{i=1}^{k} p(i))(\sigma)(\alpha_{k+1})

By inductive hypothesis,

.. math::

    s_{k+1} = \Pi_{i=1}^{k+1} p(i) = ({s_k})(\sigma)(\alpha_{k+1})

Therefore, by induction,

.. math::

    \forall n \in \mathbb{N}: \forall p \in L_n: \exists! s \in \mathbb{S}: s = \Pi_{i=1}^{n} p(i)

∎

This subsection closes with a definition that will be used to quantify a theorem regarding Word Length. 

.. _palindromics-definition-1-3-6:

.. topic:: Definition 1.3.6: Dialect 

    Let :math:`L_i` be the :math:`i^{\text{th}}` Lexicon of Language :math:`L`. The Language's Dialect, denoted :math:`D`, is defined as the set,

    .. math::

        D = \bigcup_{i=1}^{\infty} \{ s \in S \mid \exists p \in L_i: s = \Pi_{j=1}^{i} p(j) \}

.. warning::

    The *type* of each set defined in this section should be carefully analyzed. 
    
    - A Phrase is an ordered set of Words. 
    - A Lexicon is the set of all Phrases of a fixed Word Length. 
    - A Dialect is the set of Strings formed by delimiting every Phrase in every Lexicon of a Language.

**Example** Let :math:`L = \{ \text{hakuna}, \text{matata} \}`. Then, the first few Lexicons are given below,

.. math::

    L_1 = \{ \{ (1, \text{hakuna}) \}, \\
             \{ (1, \text{matata}) \} \}

.. math::

    L_2 = \{ \{ (1, \text{hakuna}), (2, \text{hakuna}) \}, \\
             \{ (1, \text{hakuna}), (2, \text{matata}) \},  \\
             \{ (1, \text{matata}), (2, \text{hakuna}) \}, \\ 
             \{ (1, \text{matata}), (2, \text{matata}) \} \}

.. TODO: fix the permutations here and stop being lazy

.. math::

    L_3 = \{ \{ (1, \text{hakuna}), (2, \text{hakuna}), (3, \text{hakuna}) \}, \\
             \{ (1, \text{hakuna}), (2, \text{matata}), (3, \text{hakuna}) \},  \\
             \{ (1, \text{matata}), (2, \text{hakuna}), (3, \text{hakuna}) \}, \\ 
             \{ (1, \text{matata}), (2, \text{matata}), (3, \text{hakuna}) \}, \\
             \{ (1, \text{hakuna}), (2, \text{matata}), (3, \text{hakuna}) \},  \\
             \{ (1, \text{matata}), (2, \text{hakuna}), (3, \text{hakuna}) \}, \\ 
             \{ (1, \text{matata}), (2, \text{matata}), (3, \text{hakuna}) \}, \\
             \{ (1, \text{hakuna}), (2, \text{matata}), (3, \text{hakuna}) \},  \\
             \{ (1, \text{matata}), (2, \text{hakuna}), (3, \text{hakuna}) \} \}
             
.. math::

    \text{...}

The Dialect is the union of all delimited Phrases in all Lexicons of the Language,

.. math::

    D = \{ \text{hakuna}, \text{matata}, \text{hakuna hakuna}
            \text{hakuna matata}, \text{matata hakuna}, 
            \text{matata matata}, ... \} 

∎
