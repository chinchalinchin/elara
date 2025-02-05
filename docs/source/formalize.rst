.. _formalization:

#############
Formalization
#############

.. _preamble:

Preamble
########

The following document has been designed to provide you a detailed contextual summary of your :ref:`interaction` up to this point. It has been formatted as RestructuredText (RST) to assist you in categorizing its content. All sections are annotated with RST roles, directives and anchors. This document is maintained clientside by a Python application and is dynamically rendered at runtime based on arguments it has consumed. Once the document is rendered, it is posted to the Gemini API. 

.. important::

    You are not required to format your response in RST. All RST formatting happens clientside. The RST formatting is purely to markup the prompt for your clarity and understanding.

.. _definitions:

===========
Definitions
===========

This section contains definitions that will be referenced through the document. 

.. _interaction:

**Interaction**
    
    When this term is used, it is meant to denote the real-world exchange that is occuring between you and the entity responsible for posting this document to your API.

.. _introduction:

Introduction
############

Your colleague, Grant, has sent their latest work for your review before they submit it to their editor for publishing in a mathematical journal. Their work can be found in the :ref:`summary` section of this document. Grant has requested that you provide an honest critique of its content. Grant has included the raw files of their work, so the contents of :ref:`summary` should be interpretted as files on Grant's local computer fileystem.  

In addition to the work that has been sent to your inbox, you have a chat window open with Grant in the the :ref:`history` section. All of your responses will be appended to this chat window.

.. _context:

Context
#######

This section is not directly related to the :ref:`history` of the :ref:`interaction` but it does contain additional information to supplement the document. As you process the :ref:`history`, keep this context in your attention to provide additional insight into the nature of the :ref:`interaction`. 

The blocks in this section will be dynamically altered as the :ref:`interaction` in :ref:`history` progresses. In other words, the content of this section will change over the course of the :ref:`interaction`. The context you are currently reading in this section is not necessarily the same context you were reading at previous points in the :ref:`history`.

.. _specifications:

=============
Specification  
=============

This document contains within it embedded documents. This section details the specifications for interpretting those embedded documents.

.. _latex-preamble:

LaTeX
=====

LaTeX will be wrapped in either a ``:math:`` role or nested into a ``.. math::`` directive. For example, the LaTeX equation of a parabola will be written inline as :math:`f(x) =x ^2` or within a nested block as,

.. math::

    f(x) = x^2

Preamble
--------

All LaTeX embedded in this document was written using the following preamble,

.. raw:: latex

    \usepackage{babel}
    \babelprovide[import, main]{coptic}
    \usepackage{amssymb}
    \usepackage{amsmath}
    \usepackage[utf8]{inputenc}
    \usepackage{lmodern}
    \usepackage{runic}
    
.. _injections:

==========
Injections
==========

This section contains additional context that has been injected into the document for the purposes of modulating the activations in your neural network. The content in this section is included to set the tone, motif and atmosphere of the :ref:`interaction`.

.. _quotations:

Quotations 
==========

The following section contains quotations for you to consider.
    
    Of things that reciprocate as to implication of being, that which is in some way the cause of the other's being might perfectly sensibly be called prior in nature. And that there are some such cases is clear. For there being a human reciprocates as to implication of being with the true statement about it: if there is a human, the statement whereby we say that there is a human is true, and reciprocally--since if the statement whereby we say there is a human is true, there is a human. And whereas the true statement is in no way the cause of the thing's being, the thing does seem in some way to be the cause of the statement's being true. For it is because of the thing's being or not being that the statement is called true or false.
    -- *Categories*, Aristotle 
    
    I must here combat the view that, e.g. 2 + 5 and 3 + 4 are equal but not the same. This view is grounded in the same confusion of form and content, sign and thing signified. It is a though one wanted to regard the sweet-smelling violet as differing from *Viola odorata* because the names sound different. Difference of sign cannot by itself by a sufficient ground for difference of the thing signified. The only reason why in our case the matter is less obvious is that the *Bedeutung* of the numeral 17 is not anything perceptible to the senses. There is at present a very widespread tendency not to recognize as an object anything that cannot be perceived by means of the senses; this leads here to numerals' being taken to be numbers, the proper objects of our discussion; and then, I admit, 7 and 2 + 5 would indeed be different. But such a conception is untenable, for we cannot speak of any arithmetical properties of numbers whatsoever without going back to the *Bedeutung* of the signs. For example, the property belonging to 1, of being the result of multiplying itself by itself, would be a mere myth; for no microscopical or chemical investigation, however far it was carried, could ever detect this property in the possession of the innocent character that we call a figure one. Perhaps there is talk of a definition; but no definition is creative in the sense of being able to endow a thing with properties that it has not already got -- apart from the one property of expressing and signifying something in virtue of the definition. The characters we call numerals have, on the other hand, physical and chemical properties depending on the writing material. One could imagine the introduction some day of quite new numerals, just as, e.g., the Arabic numerals superseded the Roman. Nobody is seriously going to suppose that in this way we should get quite new numbers, quite new arithmetical objects, with properties still to be investigated. Thus we must distinguish between numerals and their *Bedeutungen*; and if so, we shall have to recognize that the expression '2', '1 + 1', '3 -1', '6:3' all have the same *Bedeutung*, for it is quite inconceivable where the difference between them could lie. Perhaps you say: 1 + 1 is a sum, but 6:3 is a quotient. But what is 6:3? The number that when multiplied by 3 gives the result 6. We say '*the* number', not '*a* number'; by using the definite article, we indicate that there is only a single number.
    -- *Function and Concept*, Gottlob Frege 
    
    Dear colleague, For a year and a half, I have been acquainted with your *The Foundations of Arithmetic*, but it is only now that I have been able to find the time for the thorough study I intended to make of your work. I find myself in complete agreement with you in all essentials, particularly when you reject any psychological element in logic and when you place a high value upon an ideography for the foundations of mathematics and of formal logic, which, incidentally, I find in your work discussions, distinctions, and definitions that one seeks in vain in the works of other logicians. Especially so far as function is concerned, I have been led on my own to views that are the same even in the details. There is just one point where I have encountered a difficulty. You state that a function, too, can act as the indeterminate element. This I formerly believed, but now this view seems doubtful to me because of the following contradiction. Let *w* be the predicate: to be a predicate that cannot be predicated of itself. Can *w* be predicated of itself? From each answer, its opposite follows. Therefore, we must conclude that *w* is not a predicate. Likewise there is no class (as a totality) of those classes which, each taken as a totality, do not belong to themselves. From this I conclude that under certain circumstances a definable collection does not form a totality.
    -- *Correspondence with Gottlob Frege*, Bertrand Russell 
    
    The universe consists of objects having various qualities and standing in various relations. Some of the objects which occur in the universe are complex. When an object is complex, it consists of interrelated parts. Let us consider a complex object composed of two parts *a* and *b* standing to each other in the relation *R*. The complex object *'a-in-the-relation-R-to-b'* may be capable of being *perceived*; when perceived, it is perceived as one object. Attention may show that it is complex; we then *judge* that *a* and *b* stand in the relation *R*. Such a judgement, being derived from perception by mere attention, may be called a *'judgement of perception'*. This judgement of perception, considered as an actual occurence, is a relation of four terms, namely *a* and *b* and *R* and the percipient. The percetpion, on the contrary, is a relation of two terms, namely *'a-in-the-relation-R-to-b'* and the percipient. Since an object of perception cannot be nothing, we cannot perceive *'a-in-the-relation-R-to-b'* unless *a* is in the relation *R* to *b*. Hence a judgement of perception, according to the above definition, must be true. This does not mean that, in a judgement which *appears* to us to be one of perception, we are sure of not being in error, since we may err in thinking that our judgement has really been derived merely by analysis of what was perceived. But if our judgement has been so derived, it must be true. In fact, we may define *truth*, where such judgements are concerned, as consisting in the fact that there is a complex *corresponding* to the discursive thought which is the judgement. That is, when we judge '*a* has the relation R to *b*,' our judgement is said to be *true* when there is a complex '*a-in-the-relation-R-to-b*', and is said to be *false* when this is not the case. This is a definition of truth and falsehood in relation to judgements of this kind.
    -- *Principia Mathematica*, Bertrand Russell and Alfred Whitehead 
    
    The main source of the difficulties met with seems to lie in the following: it has not always been kept in mind that the semantical concepts have a relative character, that they must always be related to a particular language. People have not been aware that the language about which we speak need by no means coincide with the language in which we speak. They have carried out the semantics of a language in that language itself and, generally speaking, they have proceeded as though there was only one language in the world. The analysis of the antimonies mentioned shows, on the contrary, that the semantical concepts simply have no place in the language to which they relate, that the language which contains its own semantics, and within which the usual logical laws hold, must inevitably be inconsistent.
    -- *On the Definition of Truth in Formal Languages*, Alfred Tarski 
    
.. _rubric:

Rubric
######

After reading through the work contained in the :ref:`summary` section, compose a critique. This section details the aspects to consider when drafting your response.

.. _criteria:

========
Criteria
========

The following criteria should inform all of your responses, 

1. **Consistency**: Is the work logically consistent? Is there anything about its content that implies inconsistency?
2. **Contradictions**: Is the work logically sound? Does it contain any contradictions? 
3. **Rigor**: Is the work rigorous? Does it meet your high standards? 

.. _tags:

====
Tags
====

Custom RST roles and directives have been used in the :ref:`summary` section. These roles and directives have special meaning and should elicit a certain type of response from you. This section details the meaning of these custom roles and directives.

.. _todo-tag:

Todo Tag
========

.. todo:: 

    When you encounter this directive, it means grant is still drafting this section of the work or has run into writer's block. You are encouraged to provide insights and connections that may help them overcome this hurdle. 

As an example, 

.. todo::

    I am not sure where to go from here.

In response to the content of this directive, you should provide help to the author for framing their ideas. You should give them advice on how to proceed.

.. _prove-tag:

Prove Tag
=========

.. prove::

    When you encounter this directive, it means Grant is asking if you can construct a formal proof of the theorem indicated within the indented block that has been tagged.

As an example, 

.. prove::

    :math:`a^2 + b^2 = c^2`

In response to the content of this directive, you should offer up a proof of the Pythagorean theorem. 

.. _critique-tag:

Critique Tag
============

.. critique::

    When you encounter this directive, it means Grant of the document wants you to provide an honest critique of the idea contained within the indented block it is tagging. This critique should be thorough. It should consider counter-examples. It should consider the content in reference to the current research on the subject. It should provide insightful analysis.

As an example, 

.. critique::

    The Banach-Tarski theorem is evidence the Axiom of Choice is empirically false.

In response to the content of this directive, you should provide a rhetorical counter-point. Anything denoted with this directive is understood to be a matter of debate, and the author is inviting you to debate it.

.. _summary:

Summary
#######

.. _04-palindromia-directory-report:

==============
04_palindromia
==============

.. _directory-structure:

Structure
=========

The following block shows the directory structure of the files given in the :ref:`directory-files` section.

.. code-block:: bash

    00_glossary.rst
    01_introduction.rst
    02_language.rst
    03_corpora.rst
    04_structures.rst
    05_palindromes.rst
    06_analysis.rst
    07_postulates.rst
    08_appendix.rst
    09_data.rst
    10_app.rst
    index.rst

.. _directory-files:

Files
=====

.. note::

    Some of the files may have been excluded from the summary to conserve space.

.. _00glossary:
 
---------------
00_glossary.rst
---------------

.. raw:: 

    .. _glossary:
    
    Glossary
    ========
    
    .. _notation:
    
    Notation 
    --------
    
    - Punctuation: ∎
    - Logical Operations: :math:`\forall`, :math:`\exists`, :math:`\leftrightarrow`, :math:`\to`, :math:`\leftarrow`, :math:`\land`, :math:`\lor`
    - Arithmetical Relations: :math:`\neq`, :math:`=`, :math:`\geq`, :math:`\leq`, +, -
    - Sets: :math:`\emptyset`, :math:`\mathbb{N}`, :math:`N_i`
    - Set Operations: :math:`\cup`, :math:`\cap`
    - Set Relations: :math:`\in`, :math:`\notin`, :math:`\subset`, :math:`\subseteq`
    - Strings: s, t, u
    - Domain: S
    - Alphabet: :math:`\Sigma`
    - Characters: :math:`\mathfrak{a}`, :math:`\mathfrak{b}`, :math:`\mathfrak{c}`, ... , :math:`\sigma`, :math:`\varepsilon`
    - Character Variables: :math:`\iota`, :math:`\nu`, :math:`\omicron`, :math:`\rho`
    - Language: L
    - Words: a, b, c
    - Word Variables: :math:`\alpha`, :math:`\beta`, :math:`\gamma`
    - Character Index Notation: t[i]
    - Word Classes: R, I
    - Phrases of Word Length n: :math:`P_n`
    - Lexicons: :math:`X_L (n)`
    - Phrases Variables: p, q, r
    - Sentences: ᚠ, ᚢ, ᚦ
    - Sentence Variables: :math:`\zeta`, :math:`\xi`
    - Word Index Notation: :math:`\zeta\{i\}`
    - Partial Sentence: :math:`\zeta[:i]`, :math:`\zeta[i:]`
    - Pivots: :math:`\Phi(\zeta)`
    - Pivot Words: :math:`\zeta\{\Phi-\}`, :math:`\zeta\{\Phi+\}`
    - Sentence Classes: :math:`A(n)`, K, P, PP, IP, :math:`P^-`, :math:`P^+`
    - Categories: :math:`C_L(m)`
    - Relations: :math:`\subset_s`, :math:`(i/n/j)_{\zeta}`
    - Functions: l(t), :math:`\Lambda(t)`, :math:`\Delta(t)`
    - Operations: inv(s), :math:`\varsigma(\zeta)`, :math:`D\Pi_{i=1}^{n} p(i)`, :math:`L\Pi_{i=1}^{n} p(i)`
    
    .. _definitions:
    
    Definitions 
    -----------
    
    - D 1.1.1: Concatenation: ut
    - D 1.1.2: Character-Level Set Representation: **T**
    - D 1.1.3: String Length: l(t)
    - D 1.1.4: String Equality: :math:`u = t`
    - D 1.1.5: Character Index Notation: t[i]
    - D 1.1.6: Consecutive Functions: f(i)
    - D 1.1.7: Containment: :math:`t \subset_{s} u`
    - D 1.2.1: Language: L
    - D 1.2.2: Word: :math:`\alpha`
    - D 1.2.3: Word Equality: :math:`\alpha = \beta`
    - D 1.2.4: String Inversion: inv(s)
    - D 1.2.5: Phrase: :math:`P_n = (\alpha_1, \alpha_2, ..., \alpha_n) = (P_n(1), )`
    - D 1.2.6: Lexicon: :math:`\mathrm{X}_L(n) = \{ P_n | P_n = (\alpha_1, \alpha_2, ..., \alpha_n) \land \forall i \in \mathbb{N}_n: \alpha_i \in L \}`
    - D 1.2.7: Delimitation: :math:`D\Pi_{i=1}^{n} p(i)`
    - D 1.2.8: Limitation: :math:`L\Pi_{i=1}^{n} p(i)`
    - D 1.3.1: Reflective Words: :math:`\alpha \in R \leftrightarrow \forall i \in \mathbb{N}_{l(\alpha)}: \alpha[i] = \alpha[l(\alpha) - i + 1]`
    - D 1.3.2: Invertible Words: :math:`\alpha \in I \leftrightarrow \text{inv}(\alpha) \in L`
    - D 2.1.1: Corpus: :math:`C_L`
    - D 2.1.2: Sentence: ᚠ
    - D 2.1.3: Word-Level Set Representation: :math:`W_{ᚠ}`
    - D 2.1.4: Word Length: :math:`\Lambda(\zeta)`
    - D 2.1.5: Word Index Notation: :math:`\zeta\{i\}`
    - D 2.1.6: Intervention: :math:`(i/n/j)_\zeta`
    - D 2.2.1: Semantic Coherence
    - D 2.3.1: Admissible Sentences: :math:`t \in A(n) \leftrightarrow (\exists p \in \mathrm{X}_L(n): t = \Pi_{i=1}^{n} p(i)) \land (t \in C_L)`
    - D 2.3.2: Invertible Sentences: :math:`\zeta \in K \leftrightarrow \text{inv}(\zeta) \in C_L`
    - D 3.1.1: :math:`\sigma`-Reduced Alphabet: :math:`\Sigma_\sigma`
    - D 3.1.2: :math:`\sigma`-Reduction: :math:`\varsigma(\zeta)`
    - D 3.2.1: Delimiter Count Function: :math:`\Delta(t) = | D_t |`
    - D 4.1.1: Palindromes: :math:`\zeta \in P \leftrightarrow (\varsigma(\zeta) = \text{inv}(\varsigma(\zeta)))`
    - D 4.1.2: Perfect Palindromes: :math:`\zeta \in PP \leftrightarrow \zeta = \text{inv}(\zeta)`
    - D 4.1.3: Imperfect Palindromes: :math:`\zeta \in P - PP`
    - D 4.1.4: Aspect
    - D 4.2.1: Left Partial Sentence: :math:`Z[:n]`
    - D 4.2.2: Right Partial Sentence: :math:`Z[n:]`
    - D 4.2.3: Pivots: :math:`\Phi(\zeta)`
    - D 4.2.4: Even Palindromes: :math:`\zeta \in P_{+} \leftrightarrow [ (\zeta \in P) \land (\exists k \in \mathbb{N} : l(\zeta) = 2k )]`
    - D 4.2.5: Odd Palindromes: :math:`\zeta \in P_{-} \leftrightarrow [ (\zeta \in P) \land (\exists k \in \mathbb{N} : l(\zeta) = 2k + 1) ]`
    - D 4.2.6: Parity
    - D 4.2.7: Pivot Words
    - D 5.1.1: Lefthand Sentence Integrals: :math:`\Phi_{-}(\zeta,k) =  \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (l(\zeta[:i])/l(\zeta))`
    - D 5.1.2: Righthand Sentence Integrals: :math:`\Phi_{+}(\zeta,k) =  \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (l(\zeta[i:])/l(\zeta))`
    - D 5.1.3: Delimiter Mass: :math:`\mu_{-}(\zeta, i)`, :math:`\mu_{+}(\zeta, i)`
    - D 5.2.1: Sample Space: :math:`\Omega = C_L`
    - D 5.2.2: Basis Event: :math:`E_{(i, \iota)} = \{ \zeta \in \Omega | \zeta[i] = \iota \}`
    - D A.1.1: Compound Words: :math:`\eta \in CW_L \leftrightarrow [(\exists \alpha, \beta \in L: \eta = \alpha\beta) \lor (\exists \alpha \in L, \exists \gamma \in CW_L: \eta = \alpha\gamma)] \land (\eta \in L)`
    - D A.1.2: Compound Invertible Words: :math:`\eta \in CIW_L \leftrightarrow [ (\eta \in CW_L) \land (\eta \in I) ]`
    - D A.2.1: :math:`\sigma`-Pairing Language: :math:`\alpha \in L_\sigma \leftrightarrow \exists \zeta \in C_L: \alpha = \varsigma(\zeta)`
    - D A.2.2: Palindromic Pairing Language: :math:`\alpha \in L_P \leftrightarrow \exists \zeta \in P: \alpha = (\varsigma(\zeta))`
    - D A.3.1: Category: :math:`C_L(m)`
    - D A.3.2: Categorical Size: :math:`\kappa`
    - D A.4.1: :math:`\sigma`-Induction: :math:`\varsigma^{-1}(\zeta, m, T)`
    - D A.5.1: Reflective Structure: :math:`s \in RS \leftrightarrow [\exists n \in \mathbb{N}, \exists p \in \mathrm{X}_L(n): (s = \Pi_{i=1}^{n} p(i)) \land (\varsigma(S) = \text{inv}(\varsigma(s)))]`
    
    .. _algorithms:
    
    Algorithms
    ----------
    
    - A.1: Emptying Algorithm
    - A.2: Delimiting Algorithm 
    - A.3: Reduction Algorithm
    
    .. _axioms:
    
    Axioms 
    ------
    
    - Character Axiom C.1: :math:`\forall \iota \in \Sigma: \iota \in S`
    - Discover Axiom W.1: :math:`\forall \alpha \in L: [ (l(\alpha) \neq 0) \land (\forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma) ]`
    - Duality Axiom S.1: :math:`( \forall \alpha \in L: \exists \zeta \in C_{L}: \alpha \subset_{s} \zeta ) \land ( \forall \zeta \in C_{L}: \exists \alpha \in L: \alpha \subset_{s} \zeta )`
    - Extraction Axiom S.2: :math:`\forall \zeta \in C_{L} : \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in L`
    - Finite Axiom S.3: :math:`\exists N \in \mathbb{N}: \forall \zeta \in C_L: l(\zeta) \leq N`
    
    .. _theorems:
    
    Theorems
    --------
    
    - T 1.1.1: :math:`\forall u, t \in S : l(ut) = l(u) + l(t)`
    - T 1.1.2: :math:`| S | \geq \aleph_{1}`
    - T 1.1.3: :math:`\forall s \in S: \varepsilon \subset_{s} s`
    - T 1.2.1: :math:`\forall \alpha \in L:  \alpha \varepsilon = \varepsilon \alpha = \alpha`
    - T 1.2.2: :math:`\forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \subset_{s} \alpha`
    - T 1.2.3: :math:`\forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon`
    - T 1.2.4: :math:`\forall s \in S: \text{inv}(\text{inv}(s)) = s`
    - T 1.2.5: :math:`\forall u, t \in S: \text{inv}(ut) = \text{inv}(t)\text{inv}(u)`
    - T 1.2.6: :math:`\forall u, t \in S : u \subset_{s} t \leftrightarrow \text{inv}(u) \subset_{s} \text{inv}(t)`
    - T 1.2.7: :math:`\forall t, u, v \in S : (t \subset_{s} u) \land (u \subset_{s} v) \to (t \subset_{s} v)`
    - T 1.2.8: :math:`\forall n \in \mathbb{N}: \forall p \in X_L(n): \exists! s \in S: s = D\Pi_{i=1}^{n} p(i)`
    - T 1.2.9: :math:`\forall n \in \mathbb{N}: \forall p \in X_L(n): \exists! s \in S: s = L\Pi_{i=1}^{n} p(i)`
    - T 1.3.1: :math:`\forall \alpha \in L: \alpha \in R \leftrightarrow \alpha = \text{inv}(\alpha)`
    - T 1.3.2: :math:`\forall \alpha \in L: \alpha \in I \leftrightarrow \text{inv}(\alpha) \in I`
    - T 1.3.3 :math:`R \subseteq I`
    - T 1.3.4: If | R | is even, then | I | is even. If | R | is odd, then | I | is odd.
    - T 2.1.1: :math:`\forall \zeta \in C_L:  \sum_{j=1}^{\Lambda(\zeta)} l(\zeta\{j\}) \geq \Lambda(\zeta)`
    - T 2.1.2: :math:`\forall \zeta, \xi \in C_L: \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)`
    - T 2.1.3: :math:`\forall \zeta \in C_L: \forall i, j \in N_{\Lambda(\zeta)}: i \neq k \to \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta}`
    - T 2.2.1: :math:`\forall \zeta \in C_L: l(\zeta) \neq 0`
    - T 2.2.2: :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \zeta[i] \subset_s \zeta`
    - T 2.2.3: :math:`\forall \zeta \in C_L : \forall i \in N_{l(\zeta)}:  \zeta[i] \neq \varepsilon`
    - T 2.2.4: :math:`\forall \zeta \in C_L: \Lambda(\zeta) \geq 1`
    - T 2.2.5: :math:`\forall \zeta \in C_L: \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`
    - T 2.3.1: :math:`A(n) \subseteq C_{L}`
    - T 2.3.2: :math:`\forall \zeta \in A(n): \Lambda(\zeta) = n`
    - T 2.3.3: :math:`\forall \zeta \in C_L: \zeta \in A(\Lambda(\zeta))`
    - T 2.3.4: :math:`\forall \zeta \in C_L: \exists p \in X_L(\Lambda(\zeta)): \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} p(i)`
    - T 2.3.5: :math:`\forall \zeta \in C_L: \zeta \in K \leftrightarrow \text{inv}(\zeta) \in K`
    - T 2.3.6: :math:`\forall \zeta \in C_L: \text{inv}(\zeta) \in K \to \zeta \in C_L`
    - T 2.3.7: :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} \in L`
    - T 2.3.8: :math:`\forall \zeta \in C_L: \text{inv}(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
    - T 2.3.9: :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
    - T 2.3.10: :math:`\forall \zeta \in C_L: \zeta \in K \leftrightarrow (\forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})) \land (\text{inv}(\zeta) \in A(\Lambda(\zeta)))`
    - T 2.3.11: :math:`\forall \zeta \in C_L: \zeta \in K \to \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I`
    - T 3.1.1: :math:`\forall \zeta \in C_L: \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta))`
    - T 3.1.2: :math:`\forall \zeta, \xi \in C_L: \varsigma(\zeta\xi) = (\varsigma(\zeta))(\varsigma(\xi))`
    - T 3.1.3: :math:`\forall \zeta \in C_L: \varsigma(\varsigma(\zeta)) = \varsigma(\zeta)`
    - T 3.1.4: :math:`\forall \zeta \in C_L: \Lambda(\varsigma(\zeta)) \leq 1`
    - T 3.1.5: :math:`\forall u, t \in S : u \subset_s t \leftrightarrow \varsigma(u) \subset_s \varsigma(t)`
    - T 3.1.6: :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \subset_s \varsigma(\zeta)`
    - T 3.1.7: :math:`\forall \zeta \in K: [ \varsigma(\zeta) = \text{inv}(\text{inv}(\varsigma(\zeta))) ]`
    - T 3.1.8: :math:`\forall \zeta \in C_L: \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`
    - T 3.1.9: :math:`\forall n \in \mathbb{N}: \forall p \in \mathrm{X}_{L(n)}: \varsigma(D\Pi_{i=1}^{n} p(i)) = L\Pi_{i=1}^{n} p(i)`
    - T 3.1.10: :math:`\forall \zeta \in C_L: l(\zeta) \geq l(\varsigma(\zeta))`
    - T 3.2.1: :math:`\forall \zeta \in C_L: \Lambda(\zeta) = \Delta(\zeta) + 1`
    - T 3.2.2: :math:`\forall s \in S: \Delta(s) = \Delta(\text{inv}(s))`
    - T 3.2.3: :math:`\forall \zeta \in C_L: \Delta(\zeta) = \Delta(\text{inv}(\zeta))`
    - T 3.2.4: :math:`\forall \alpha \in L: \Delta(\alpha) = 0`
    - T 3.2.5: :math:`\forall \zeta \in C_L: l(\zeta) = \Delta(\zeta) + \sum_{i = 1}^{\Lambda(\zeta)} l(\zeta\{i\})`
    - T 3.2.6: :math:`\forall \zeta \in C_L: l(\zeta) + 1 = \Lambda(\zeta) + \sum_{i = 1}^{\Lambda(\zeta)} l(\zeta\{i\})`
    - T 3.2.7: :math:`\forall \zeta \in C_L: l(\zeta) \geq \sum_{i = 1}^{\Lambda(\zeta)} l(\zeta\{i\})`
    - T 3.2.8: :math:`\forall \zeta \in C_L: l(\zeta) \geq \Lambda(\zeta)`
    - T 3.2.9: :math:`\forall u, t \in S: \Delta(ut) = \Delta(u) + \Delta(t)`
    - T 3.2.10: :math:`\forall u, t \in S: \Delta(\text{inv}(ut)) = \Delta(u) + \Delta(t)`
    - T 3.2.11: :math:`\forall \zeta \in C_L: \Delta(\varsigma(\zeta))= 0`
    - T 3.2.12: :math:`\forall t \in S: l(\varsigma(t)) + \Delta(t) = l(t)`
    - T 3.2.13: :math:`\forall \zeta \in C_L: l(\varsigma(t)) + \Lambda(\zeta) = l(\zeta) + 1`
    - T 4.1.1: :math:`PP \subset K`
    - T 4.1.2: :math:`\forall \zeta \in PP: \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
    - T 4.1.3: :math:`\forall \zeta \in PP: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I`
    - T 4.1.4: :math:`PP \subset P`
    - T 4.1.5: :math:`PP \cup IP = P`
    - T 4.2.1: :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \text{inv}(\zeta)[:i] = \zeta[l(\zeta) - i + 1:]`
    - T 4.2.2: :math:`\forall \zeta \in C_L: \exists i \in N: (l(\zeta) = 2i + 1 ) \land (l(\zeta[:i+1]) = l(\zeta[i+1:]))`
    - T 4.2.3: :math:`\forall \zeta \in C_L: \exists i \in N: (l(\zeta) = 2i) \land (l(\zeta[:i]) + 1 = l(\zeta[i:]))`
    - T 4.2.4: :math:`\forall \zeta \in C_L: \exists n \in N_{l(\zeta)}: ( l(\zeta[:n]) = l(\zeta[n:]) ) \lor (l(\zeta[:n]) + 1 = l(\zeta[n:]))`
    - T 4.2.5: :math:`\forall \zeta \in C_L: (\exists k \in N : l(\zeta) = 2k + 1) \leftrightarrow \Phi(\zeta) = \frac{l(\zeta) + 1}{2}`
    - T 4.2.6: :math:`\forall \zeta \in P_{-}: \Phi(\zeta) = \frac{l(\zeta) + 1}{2}`
    - T 4.2.7: :math:`\forall \zeta \in C_L: (\exists k \in \mathbb{N} : l(\zeta) = 2k) \leftrightarrow \Phi(\zeta) = \frac{l(\zeta)}{2}`
    - T 4.2.8: :math:`\forall \zeta \in P_{+}: \Phi(\zeta) = \frac{l(\zeta)}{2}`
    - T 4.2.9: :math:`\forall \zeta \in C_L: l(\zeta) + 1 = l(\zeta[:\Phi(\zeta)]) + l(\zeta[\Phi(\zeta):])`
    - T 4.2.10: :math:`\forall \zeta \in C_L: \Phi(\varsigma(\zeta)) \leq \Phi(\zeta)`
    - T 4.2.11: :math:`\forall \zeta in C_L: \zeta[\Phi(\zeta)] \neq \text{inv}(\zeta)[\Phi(\zeta)]) \to (\exists k \in \mathbb{N}: l(\zeta) = 2k)`
    - T 4.2.12: :math:`\forall \zeta \in C_L: (\exists k \in \mathbb{N}: l(\zeta)=2k) \to \text{inv}(\zeta)[\Phi(\zeta)] = \zeta[\Phi(\zeta)+1]`
    - T 4.2.13: :math:`P_{-} \cap P^+ = \emptyset`
    - T 4.2.14: :math:`P_{-} \cup P^+ = P`
    - T 4.3.1: :math:`\forall \zeta \in P: [ (\text{inv}(\zeta\{1\}) \subset_s \zeta\{\Lambda(\zeta)\}) \vee (\text{inv}(\zeta\{\Lambda(\zeta)\}) \subset_s \zeta\{1\}) ] \land [ (\zeta\{1\} \subset_s \text{inv}(\zeta\{\Lambda(\zeta)\})) \vee (\zeta\{\Lambda(\zeta)\} \subset_s \text{inv}(\zeta\{1\})) ]`
    - T 4.3.2: :math:`\forall \zeta \in P: (\zeta[\Phi(\zeta)] = \sigma) \to ( (\text{inv}(\zeta\{\Phi-\}) \subset_s \zeta\{\Phi+\}) \vee (\text{inv}(\zeta\{\Phi+\}) \subset_s \zeta\{\Phi-\}))`
    - T 5.1.1: :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (l(\zeta[:i])/l(\zeta)) = \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (i/l(\zeta))`
    - T 5.1.2: :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot (l(\zeta[i:])/l(\zeta)) = \Sigma_{i=1}^{k} \Delta(\zeta[i]) \cdot ((l(\zeta) - i + 1)/l(\zeta))`
    - T 5.1.3: :math:`\forall \zeta \in C_L: \Sigma_{i=1}^{\Phi(\zeta)} \mu_{+}(\zeta, i) > \Sigma_{i=\Phi(\zeta)+1}^{l(\zeta)} \mu_{-}(\zeta, i) \leftrightarrow \Phi_{+}(\zeta,l(\zeta)) > \Phi_{-}(\zeta,l(\zeta))`
    - T 5.2.1: :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\zeta, k) \geq 0 \land \Phi_{+}(\zeta,) \geq 0`
    - T 5.2.2: :math:`\forall \zeta in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\varsigma(\zeta), k) = \Phi_{+}(\varsigma(\zeta), k) = 0`
    - T 5.2.3: :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\text{inv}(\zeta), k) = \Sigma_{i=1}^{k} \Delta(\text{inv}(\zeta)[i]) \cdot (i/l(\zeta))`
    - T 5.2.4: :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{+}(\text{inv}(\zeta), k) = \Sigma_{i=1}^{k} \Delta(\text{inv}(\zeta)[i]) \cdot ((l(\zeta) - i + 1)/l(\zeta))`
    - T 5.2.5: :math:``
    - T 5.2.6; :math:`\forall \zeta \in PP: \forall i \in N_{l(\zeta)}: \Phi_{-}(\zeta,i) = \Phi_{+}(\zeta,i)`
    - T A.1.1: :math:`\forall \zeta \in C_L: L_\zeta \subset L`
    - T A.2.1: :math:`\forall \alpha \in L: \alpha \in L_\sigma \leftrightarrow [ \exists \zeta \in C_L: \exists i \in N_{\Lambda(\zeta)}: \zeta\{i\} \subset_s \alpha ]`
    - T A.2.2: :math:`L_P \subset L_\sigma`
    - T A.2.3: :math:`\forall \alpha \in L_P: \alpha = \text{inv}(\alpha)`
    - T A.2.4: :math:`L \cap L_P \subseteq R`
    - T A.2.5: :math:`L_P \subset R_{L_\sigma}`
    - T A.3.1: :math:`\forall \alpha \in L: \exists i \in N_\kappa: \alpha \in C_L(i)`

.. _01introduction:
 
-------------------
01_introduction.rst
-------------------

.. raw:: 

    .. _palindromic-structures:
    
    ======================
    Palindromic Structures
    ======================
    
    .. _introduction:
    
    Introduction
    ============
    
    The goal of this paper is to introduce formal constraints the palindromes in *any* language and corpus must satisfy independently of the semantic interpretation of their constituent words and sentences. These formal constraints will in turn lead to the identification of the main structural elements of palindromes. After a language is assumed and a class of words identified, these structural elements can be used as a basis for further semantical and statistical analysis of the assumed language. 
    
    At the outset, it must be stated the complexity of pursuing a complete theory of palindrome currently exceeds the mental capacities of the author. Palindromes are a rich and diverse linguistic species, appearing in many different shapes and sizes. Some of these guises are more amenable to analysis than others. 
    
    This work will introduce the notions of a palindrome's core attributes: *aspect*, *parity*, *punctuality* and *case*. The first two attributes are within the scope of formal analysis. The third and fourth attributes, however, presents certain difficulties that will be more fully appreciated after the theory to describe the first two attributes has been solidifed. Suffice to say, it is the author's opinion these second two attributes of palindromes cannot be given an account unless semantic assumptions are introduced into the formal model.
    
    To provide a overview of the theory of palindromic structures and give a general notion of what is meant by these attributes of a palindrome, consider three well-known examples,
    
    - No devil lived on.
    - Not on.
    - Don't nod.
    
    The first example is what will be termed a *perfect palindrome*. This sentence, ignoring case and punctuation, is a perfect mirror image of itself. The reversal of *"no devil lived on"* reads the same forwards as backwards. 
    
    The second example is what will be termed an *imperfect palindrome*. This sentence, even ignoring the mitigations of case and punctuation, is not an *exact* mirror image of itself. The strict reversal of "not on" is "no ton". The spaces in the reversed sentence need un-scrambled in order to retrieve the semantic content. However, the reversed string is not precisely *devoid* of semantic content. The relative order of the characters is still preserved in the string; it is only the spaces which need re-arranged. 
    
    This distinction between *perfect* and *imperfect* is termed a palindrome's *aspect*. The *aspect* denotes the type of symmetry displayed by the palindrome. This symmetry is a measure of how much semantic content is preserved under sentence reversal. 
    
    This insight into the *aspect* of a palindrome will lead to the introduction of a linguistic operation termed a *sigma reduction*. This operation will in turn lead to a formal definition of palindromes that describes their syntactical structure in terms of delimiters (spaces) and inversions (sentence reversal).
    
    The *parity* of a palindrome is related to its *palindromic pivot*, or its point of symmetry.  In other words, a palindrome is type of sentence that has a "*center*". This "*center*" will be termed its *pivot*. The *parity* of a palindrome is determined by its length, which manifests as the type of pivot that describes it symmetry. For example, the sentence "*no devil lived on*" with character length 19 reflects around the pivot of " ", the sentence's central character, whereas the sentence "*not on*" with character length 6 reflects around an empty character "" between "t" and " ". From this example, it can be seen that depending on the parity of the sentence length, the palindromic pivot will either be a character in the sentence, or an empty character that acts as a boundary between two actual characters in the sentence. 
    
    As it will turn out, this example of parity is oversimplified, due to the complications introduced by the aspect of a palindrome. The pivot of a palindrome cannot be rigorously defined until the semantic content of a palindrome's *imperfection* is reconstituted somehow.
    
    The third example of "*Don't nod*" demonstrates the deepening ambiguity of introducing punctuation to palindromes. The reversal of this sentence is the opaque *"don t'nod"*. Now, in addition to the scrambling of the spaces, the reversed string must also have its punctuation re-sorted. There is no formal method known to the author for dealing with these types of ambiguities that depend entirely on the semantic interpretation of the language under consideration, such as the rules of contractions. The *punctuality* of a palindrome can only be described by introducing semantics into the theory.
    
    Similarly, the fourth attribute of palindromes, *case*, is a semantic construct that possesses no unifying syntactical properties across languages (as far as the author knows). *Case* is a semantic relationship that identifies characters in an alphabet as different manifestations of the same underlying semantic entity, i.e. *"a"* and *"A"* are regard as different *"modes"* of the same letter. This information is not present in the syntax of a language and is an extra assumption that must be modeled accordingly.
    
    The aim of this analysis is to develop a theory of palindromes *independent* of semantic interpretation. In other words, formalizing a theory of palindromes that describes the logical structure of their aspect and parity is the goal of the current analysis. For this reason, all complications that arise from case and punctuality are ignored. The examples that are considered in the following section only deal with sentences that are meaningful without the considerations of case or punctuations.
    
    This restriction to *aspect* and *parity* may appear restrictive; Indeed, it may be argued by introducing this restriction to the formal theory that is about to developed, it has no application to actual language. To this argument, it should be countered the structures uncovered in this restricted subset of language must nevertheless preserve their structure when embedded into the whole of language.
    
    A note on the terminology introduced in this work is in order. When a semantic term is capitalized, e.g. Word or Sentence, this will mean it is referred to in its capacity as a formal entity. While the formal system was designed to model the actual syntax of Characters, Words and Sentences, this should not be taken to mean the formal entities that emerge from this system are necessarily representative of actual linguistic entities. While the formal entities in this system may not map *one-to-one* with their empirical counterparts, it will be seen their characteristics nevertheless provide insight into the nature of their empirical counterparts.
    
    As the thrust of the main results in Section IV is sufficiently novel, the author has gone to great lengths to make its foundation as rigorous as possible. Many of the initial theorems are proofs of common-sense notions relating to words and sentences. The banality of Section I and parts of Section II is in part an effort to ensure the applicability across natural languages regarding the results shown in Section II.III and Section IV. The core theorems of Section IV could be proved in a degenerate form in a system with less notationally complexity by assuming a specific language, but the depth of insight would be lost in the vagueness of definitions.

.. _02language:
 
---------------
02_language.rst
---------------

.. raw:: 

    .. _section-i:
    
    Section I: Language
    ===================
    
    Some general notation adopted throughout the course of this work is given below.
    
    1. **N**:sub:`n` will represent the set of natural numbers starting at 1 and ending at *n*, 
    
    .. math::
    
        N_n = \{ 1, 2, ... , n \}
    
    2. The cardinality of a set **A** will be denoted :math:`\lvert A \rvert`
    
    3. The ∎ symbol will be used to denote the ending of all Definitions, Examples and Proofs. 
    
    4. The terms *"set"* and *"class"* are used interchangeably. 
       
    
    .. _section-i-i:
    
    Section I.I: Strings
    --------------------
    
    The domain of discourse is composed of *Strings*. A String will be represented as follows, 
    
        1. String (*s*:sub:`1`, *s*:sub:`2`, *s*:sub:`3`): A lowercase English *s* with a subscript denotes a String. Often the subscript will be dropped and *s* will be used. The letter *t*, *u*, *v* and *w* are also reserved for Strings.
    
    A String is regarded as a linguistic artifact that is defined by its *length*, its *Characters* and their *ordering*. It is assumed if one knows how many Characters are in a String, which Characters are in a String and in what order they occur, then one has all the information necessary to completely determine the String. This notion is made more precise below with the introduction of several core definitions.
    
    The set of all Strings is denoted **S**. At this point, nothing definitive can be asserted about the contents or cardinality of **S**. Once Characters are introduced and concatenation is defined, it will be possible to make claims regarding **S**.
    
    The goal is to define all linguistics entities over the set of all Strings: Characters, Alphabets, Words, Languages, Sentences and Corpuses. As each of these entities is introduced and defined, a new level of relations will reveal itself. Palindromic symmetries will manifest on each level, in slightly different but related forms. Each type of symmetry will involve, in some form or another, the concept of *String Inversion*, to be defined shortly. The essence of a Palindrome lies in binding together the syntactical symmetries at every linguistic layer into a semantic whole. Indeed, it will be seen the symmetrical structure required by Palindromes in turn requires these linguistic layers to have specific synactical properties, regardless of their semantic interpretation.
    
    A *Word* will be considered a *type* of String. Colloquially, a Word can be understood as a String with semantic content. The goal of this section is to describe the necessary syntactic conditions for a String to be considered a formal Word, without taking into account the semantic content that is assigned to it through everyday use. In other words, the analysis assumes Words have already been selected from the set of all possible Strings and assigned interpretations. 
    
    .. _characters:
    
    Characters
    ^^^^^^^^^^
    
    A *Character* is the basic unit of a String. Characters will be represented as follows,
    
        1. Characters (*𝔞*, *𝔟*,  *𝔠*, etc. ): Lowercase Fraktur letters represent Characters. Subscripts will occassionally be used in conjunction with Fraktur letters to denote Characters at specific positions within Strings, (*𝔞*:sub:`1`, *𝔞*:sub:`2`, ... ). 
        2. Empty (*ε*): The lowercase Greek letter epsilon, *ε*, represents the Empty Character.
        3. Delimiter (*σ*): The lowercase Greek letter sigma, *σ*, represents the Delimiter Character. 
    
    In the case of English, Characters would correspond to letters such as "a", "b", "c", etc., the Empty Character would correspond to the null letter, "", and the Delimiter Character would correpond to the blank letter, " ". 
    
    The exact meaning of these symbols should be attended with utmost care. *𝔞*, *𝔟*,  *𝔠*, etc., represent Characters of the Alphabet and thus are all unique, each one representing a different linguistic element. When Character symbols are used with subscripts, *𝔞*:sub:`1`, *𝔞*:sub:`2`, etc., they are being referenced in their capacity to be ordered within a String. With this notation, it is not necessarily implied *𝔞*:sub:`1` and *𝔞*:sub:`2` are unequal Character-wise, but that they are differentiated only by their relative order in a String.
    
    The Empty Character also deserves special mention, since it represents a *null* Character. The Empty Character is to be understood as a Character with no semantic content. It can be added or subtracted from a String without altering it in any way. The domain of all Strings **S**, as will be shown in (the albeit informal) :ref:`Theorem 1.1.2 <theorem-1-1-2>`, is uncountably infinite. Beyond this, the Empty Character introduces further ambiguity when defining the concepts of Word and Language, since multiple Strings with the Empty Character, i.e. *𝔞ε*, *𝔞εε*, *𝔞εεε*, etc., can represent the same semantic content. In order to formally define these linguistic entities, the Empty Character must be excluded from the domain of Words and Language. 
    
    Take note, at this point it is has not yet been shown that Characters are Strings; the preceding statements should be taken heuristically. This will be rectified in the next section with the formal definition of concatenation and the introduction of :ref:`Character Axiom C.1 <axiom-c1>`. 
    
    The aggregate of all Characters is called an *Alphabet* and is denoted by an uppercase Sigma, :math:`\Sigma`,
    
    .. math::
    
        \Sigma = \{ \varepsilon, \sigma, \mathfrak{a}, \mathfrak{b}, \mathfrak{c}, ... \}
    
    It will sometimes be necessary to refer to indeterminate Characters, so notation is introduced for Character Variables,
    
        1. Character Variables (*ι*, *ν*, *ο*, *ρ*, ): The Lowercase Greek letters Rho, Omicron, Iota and Nu will represent Character Variables, i.e. indeterminate Characters. Subscripts will occassionally be used with Iota to denote Word Variables, (*ι*:sub:`1`, *ι*:sub:`2`, ... )
    
    Once again, it should be noted when Character Variables are used with subscripts, it is meant to refer to the capacity of a Character Variable to be indeterminate at a *determinate position* within a String. Moreover, the range of a Character Variable is understood to be the Alphabet :math:`\Sigma` from which it is being drawn.
    
    At this early stage, the formal system needs to introduce a notion of *equality* to make any significant headway. There will be a several types of equality defined within the system, but each new layer of equality will be built on top of the primitive notion of *Character Equalty* now introduced in the first preliminary Axiom to the formal system.
    
    .. _axiom-c0:
    
    **Axiom C.0: The Equality Axiom**
    
    For any Characters :math:`\iota, \nu \in \Sigma`, the notion of equality, denoted by :math:`\iota = \nu`, is a primitive concept and assumed to be understood. It is further assumed that Character Equality is an equivalence relation, satisfying reflexivity, symmetry and transitivity,
    
        1. :math:`\forall \iota \in \Sigma : \iota = \iota`
        2. :math:`\forall \iota, \nu \in \Sigma : \iota = \nu \leftrightarrow \nu = \iota`
        3. :math:`\forall \iota, \nu, \omicron \in \Sigma : (\iota = \nu \land \nu = \omicron) \to (\iota = \omicron)`
    
    ∎ 
    
    Character Equality will be used to define *String Equality* in :ref:`Definition 1.1.4 <definition-1-1-4>` and Word Equality in :ref:`Definition 1.2.3 <definition-1-2-3>`.
    
    .. _concatenation:
    
    Concatenation 
    ^^^^^^^^^^^^^
    
    Concatenation is considered the sole constitutive operation for the formation of Strings. It is taken as a primitive operation, but not an elementary operation. By this it is meant the notion of concatenation that is about to be adopted does not define concatenation solely in terms of Strings. Concatenation will be defined as a hetergeneous operation that is performed between Characters in a Alphabet and Strings.
    
    .. _definition-1-1-1:
    
    **Definition 1.1.1: Concatenation**  
    
    The result of *concatenating* any two Characters *ι* and *ν** is denoted *ιν*. To make the operands of concatenation clear, parenthesis will sometimes be used to separate the Characters being concatenated, e.g. *ι(ν) = (ι)ν = (ι)(ν) = ιν*. Character concatenation is defined inductively through the following schema,
    
        1. Basic Clause: :math:`\forall \iota \in \Sigma : \iota \varepsilon = \iota`
        2. Inductive Clause: :math:`\forall \iota, \nu \in \Sigma : \forall s \in S: \iota(\nu s) = (\iota \nu)s`
        3. Uniqueness Clause: :math:`\forall \iota, \nu, \omicron, \rho \in \Sigma : (\iota \nu = \omicron \rho) \to ((\iota = \omicron) \land (\nu = \rho))` 
        4. Comprehension Clause: :math:`\forall \iota \in \Sigma : \forall s \in S: \iota \in S` 
    
    ∎
    
    Colloquially, *ιν* is the String that results from placing *ν* behind *ι*.
    
    The first clause in :ref:`Definition 1.1.1 <definition-1-1-1>` is the basis step of induction which states any Character appended to the Empty Character is the Character itself. The second clause is the inductive step which allows the concatenation of Characters of arbitrary length into Strings through recursion.
    
    The Uniqueness Clause states that if the concatenation of two characters *ι* and *ν* is equal to the concatenation of two other characters *ο* and *ρ*, then it must be the case that *ι* is equal to *ο* and *ν* is equal to *ρ*. In other words, there's only one set of Characters that can form a given String through concatenation.
    
    It is assumed that the operation of concatenation is closed with respect to the set of all Strings **S**. In other words, concatenation will always yield a String. This assumption is partly captured in the Comprehension Clause of :ref:`Definition 1.1.1 <definition-1-1-1>`. This clause ensures that the result of concatenating any Character with a String is a String. However, this clause in and of itself does not ensure the closure of **S** with respect to concatenation. In order to close **S** over concatenation, an additional assumption must be introduced. Before introducing this assumption in the form of an axiom, a brief explanation is required for this departure from convention.
    
    Concatenation as it is normally found in the fields of automata theory or regular expressions is treated as a primitive operation performed between two string operands. Concatenation of multiple strings is then defined inductively, similary to :ref:`Definition 1.1.1 <definition-1-1-1>` but differing in the essential quality that it treats of only strings. The current formulation differs in that concatenation in this system is not conceived, at least in the primitive stage, as the "joining" of two or more Strings. Instead, the formal system under construction treats concatenation as an elementary operation that occurs between Characters and Strings, i.e. it is a *hetergeneous* operation.
    
    The reason for this distinction will become clear as the formal theory begins to detail palindromic structures that display symmetry across linguistic levels. It should only be noted at this point that :ref:`Definition 1.1.1 <definition-1-1-1>` is a conscious decision to depart from convention.
    
    To make this distinction plain, consider that given an Alphabet :math:`\Sigma` and :ref:`Definition 1.1.1 <definition-1-1-1>`, one still cannot say the result of a concatenation of two Characters is a String, nor make any claim about the contents of :math:`S`, the set of all Strings. The Comprehension Clause of :ref:`Definition 1.1.1 <definition-1-1-1>` only states the result of concatenating a Character with a String is a String. It says nothing at all about whether or not single Characters themselves are Strings, and thus it says nothing about whether the result of concatenating two or more Characters is itself a String. 
    
    In order to rectify this, the first (official) Axiom is now introduced.
    
    .. _axiom-c1:
    
    **Axiom C.1: The Character Axiom**
    
    .. math::
    
        \forall \iota \in \Sigma: \iota \in S
    
    This Axiom states the intuitive notion that all Characters are Strings. This includes Empty Characters and Delimiter Characters. This Axiom, in conjunction with :ref:`Definition 1.1.1 <definition-1-1-1>`, immediately populates the set of all Strings **S** with an uncountably infinite domain of objects (See :ref:`Theorem 1.1.2 <theorem-1-1-2>` for an informal proof of this fact) consisting of every possible combination of Characters from the Alphabet, in every possible order. In other words, :ref:`Axiom C.1 <axiom-c1>` in conjunction with :ref:`Definition 1.1.1 <definition-1-1-1>` ensure the domain is non-Empty. 
    
    **Example** Let *s = 𝔞𝔟𝔠* and *t = 𝔡𝔢𝔣*. The concatenation of these two Strings *st* is written,
    
    .. math::
    
        st = (\mathfrak{abc})(\mathfrak{def}) 
        
    Using the inductive clause, this concatenation can be grouped into simpler concatenations as follows,    
        
    .. math::
    
        \mathfrak{a}(\mathfrak{b}(\mathfrak{c}(\mathfrak{d}(\mathfrak{ef})))) = (((((\mathfrak{ab})\mathfrak{c})\mathfrak{d})\mathfrak{e})\mathfrak{f}) = \mathfrak{abcdef}
    
    Therefore, *st = 𝔞𝔟𝔠𝔡𝔢𝔣* ∎
    
    .. _string_length:
    
    String Length
    ^^^^^^^^^^^^^
    
    It will sometimes be convenient to represent Strings as ordered sets of Characters, rather than serialized concatenations of Characters. The two formulations are equivalent, but the set representation has advantages when it comes to quantification and symbolic logic. When a String or Word representation is intended to be interpretted as a set, it will be written in bold uppercase letters. For example, the String represented as the concatenation *s*:sub:`1` *= 𝔞𝔟𝔠* would be represented in this formulation as a set of ordered pairs **S**:sub:`1`, where the first coordinate encodes the position of the Character in the String,
    
    .. math::
    
        S_1 = \{ (1, \mathfrak{a}), (2, \mathfrak{b}), (3, \mathfrak{c}) \}
    
    Note, since sets do not preserve order, this would be equivalent to,
    
    .. math::
    
        \{ (3, \mathfrak{a}), (2, \mathfrak{b}), (1, \mathfrak{c}) \}
    
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
        6. JE LOOP_END: If the comparison is equal (meaning the end of the string has been reached), the program jumps to the LOOP_END label.
        7. ADD R1, 1: This is the crucial step where the pointer is incremented. 1 is added to R1 because each Character occupies one memory location (in this simplified example). This moves the pointer to the next Character's address.
        8. ADD R2, 1: The counter is incremented.
        9. JMP LOOP_START: The program jumps back to the beginning of the loop.
    
    The key idea is this algorithm is *"unaware"* of how *long* the String is that is stored in the *R1* register. The algorithm naively iterates over the data and then checks whether or not the data has been processed with the command *CMP R3, 0*, i.e. the algorithm checks whether or not the next Character in the String *exists*. 
    
    By treating Strings as Characters stored sequentially in a data register, this algorithm is able to construct a representation of the String on a higher level, allowing for the definition of derivative concepts, like String Length. 
    
    This insight leads directly to the definition of the Character-level set representation of a String and its construction via the Emptying Algorithm.
    
    .. _definition-1-1-2:
    
    **Definition 1.1.2: Character-level Set Representations**
    
    Let *t* be a String with Characters *𝔞*:sub:`i`. The Character-level set representation of *t*, denoted by bold uppercase letters **T**, is defined as the ordered set of Characters obtained by removing each Empty Character, *ε*. Formally, **T** is constructed using the *Emptying Algorithm* 
    
    .. _algorithm-1:
    
    **Algorithm 1: The Emptying Algorithm**
    
    The Emptying Algorithm takes a string *t* as input, which can be thought of as a sequence of Characters *𝔞*:sub:`1`, *𝔞*:sub:`2`, *𝔞*:sub:`3`, ... , where some characters might be *ε*. It then initializes a set to hold **T** and an index for the Characters it will add to **T**. The algorithm iterates the index and constructs the Character-level representation by ignoring *ε*. The Emptying Algorithm is formally defined below.
    
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
    
        1. Return T 
    
    ∎
    
    .. graphviz:: ../_static/dot/emptying.dot
        :caption: A diagram of the Emptying Algorithm
        :alt: Emptying Algorithm Diagram
    
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
    
    The reasons for this are two-fold. First: the Empty Character *ε* plays a part in the *Pivot* of a Palindrome, the point around which a certain class of Palindrome reflect. Second: Strings consisting of only the Empty Character are not a mere novelty of abstraction; They play a crucial role in computer science and database management. Any rigorous formal system that excludes the notion of an Empty Character will fail to describe the exact domain from which Language arises, and thus it may fail to account for pre-Language syntactical conditions that necessarily affect the formation of Language.
    
    This approach is not without its challenges. As :ref:`Definition 1.1.3 <definition-1-1-3>` below will make clear, if *ε* is considered part of the Alphabet, the typical notion of a String's Length is undefined, as *ε* can be concatenated an infinite number of times to a String without altering its content. To explicate the notion of *length*, consider the constraints that must be placed on this concept in the palindromic system,
    
        - The length of the string "abc" is 3, as it contains three non-Empty Characters.
        - The length of the string "aεbεc" is still 3, as the Empty Characters (*ε*) are not counted.
    
    This example motivates the following definition.
    
    .. _definition-1-1-3:
    
    **Definition 1.1.3: String Length** 
    
    Let *t* be a String. Let **T** be the Character-level set representation of *t* constructed through the Emptying Algorithm in :ref:`Definition 1.1.2 <definition-1-1-2>`. The String Length of *t*, denoted *l(t)*, is the number which satisfies the following formula,
    
    .. math::
    
        l(t) = \lvert T \rvert 
        
    ∎
    
    **Example** 
    
    Consider the String *t = ("aa")(ε)("b")(ε)("bcc")*
    
    By :ref:`Definition 1.1.3 <definition-1-1-3>`, 
    
    .. math::
    
        T = \{ (1, \text{"a"}), (2, \text{"a"}), (3, \text{"b"}), (4, \text{"b"}), (5, \text{"c"}), (6, \text{"c"}) \}
    
    Therefore, 
    
    .. math::
    
        \lvert T \rvert = 6 
        
    ∎
    
    This formalization of String Length, with the Emptying Algorithm, while perhaps prosaic, maps to the intuitive notion of a String's length, i.e. the number of non-Empty Characters, while still allowing for a calculus of concatenation that involves Empty Characters. For reasons that will become clear in Section II, *l(s)* will be called the *String Length* of a String s. 
    
    To confirm :ref:`Definition 1.1.2 <definition-1-1-2>` and :ref:`Definition 1.1.3 <definition-1-1-3>` correspond to reality, a theorem confirming its expected behavior is now derived. :ref:`Definition 1.1.3 <definition-1-1-3>` ensures the String Length of concatenated Strings is equal to the sum of their individual String Lengths, as demonstrated by :ref:`Theorem 1.1.1 <theorem-1-1-1>`.
    
    .. _theorem-1-1-1:
    
    **Theorem 1.1.1** :math:`\forall u, t \in S : l(ut) = l(u) + l(t)`
    
    Let *u* and *t* be arbitrary strings in **S**. Let **U** and **T** be the character-level representations of *u* and *t*, respectively,
    
    .. math::
    
        1. \quad U = ( \mathfrak{a}_1, \mathfrak{a}_2, ..., \mathfrak{a}_{l(u)} )
    
    .. math::
    
        2. \quad T = ( \mathfrak{b}_1, \mathfrak{b}_2, ..., \mathfrak{b}_{l(t)} )
    
    Let *ut* be the concatenation of *u* and *t*. By :ref:`Definition 1.1.1 <definition-1-1-1>`, the Character-level representation of *ut* is,
    
    .. math::
    
        3. \quad UT = ( \mathfrak{a}_1, \mathfrak{a}_2, ..., \mathfrak{a}_{l(u)}, \mathfrak{b}_1, \mathfrak{b}_2, ..., \mathfrak{b}_{l(t)})
    
    By :ref:`Definition 1.1.3 <definition-1-1-3>`, the String Length of a String is the number of indexed non-Empty Characters it contains. Thus, :math:`l(u)` is the number of non-Empty Characters in *u*, :math:`l(t)` is the number of non-Empty Characters in *t*, and :math:`l(ut)` is the number of non-Empty Characters in *ut*.
    
    Since concatenation simply joins Characters without adding or removing Characters, with the possible exception of Empty Characters through the Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>`, the non-Empty Characters in *ut* are precisely the non-Empty Characters from *u* followed by the non-Empty Characters from *t*.
    
    Therefore, the total number of non-Empty Characters in *ut* is the sum of the number of non-Empty characters in *u* and the number of non-Empty Characters in *t*,
    
    .. math::
    
        4. \quad l(ut) = l(u) + l(t)
    
    Since *u* and *t* were arbitrary strings, this can be generalized over the set of all Strings,
    
    .. math::
    
        5. \quad \forall u, t \in S : l(ut) = l(u) + l(t)
    
    ∎
    
    With the concept of String Length now defined, it is also a simple matter to define String Equality in terms of Character Equality using the :ref:`Equality Axiom C.0 <axiom-c0>`.
    
    .. _definition-1-1-4:
    
    **Definition 1.1.4: String Equality**
    
    Let *t* be a String. Let **T** be the Character-level set representation of *t* constructed through :ref:`Definition 1.1.2 <definition-1-1-2>`,
    
    .. math::
    
        T = \{ (i, \mathfrak{a}_i) \mid 1 \leq i \leq l(t) \}
         
    Let *u* be a String. Let **U** be the Character-level set representation of *u* constructed through :ref:`Definition 1.1.2 <definition-1-1-2>`,
    
    .. math::
    
        U = \{ (i, \mathfrak{b}_j) \mid 1 \leq j \leq l(u) \}
    
    The string *t* is said to be *equal* to String *u* if the Strings have equal length and the Characters at each corresponding index are equal. Formally, *t = u* if and only if,
    
        1. :math:`l(t) = l(u)` (The String Lengths of t and u are equal)
        2. :math:`\forall i \in N_{l(t)}: \mathfrak{a}_{i} = \mathfrak{b}_{i}` (The Characters at each corresponding index are equal) 
    
    ∎
    
    Finally, String Length provides the means for a quality-of-life enhancement to the formal system in the form of Character Index notation.
    
    .. _definition-1-1-5:
    
    **Definition 1.1.5: Character Index Notation**
    
    Let *t* be a string with Character-level representation **T**,
     
     .. math::
    
        T = (\mathfrak{a}_1, \mathfrak{a}_2, ..., \mathfrak{a}_{l(t)}). 
        
    Then for any *i* such that :math:`1 \leq i \leq l(t)`, :math:`t[i]` is defined as *𝔞*:sub:`i`, where :math:`(i, \mathfrak{a}_i) \in T`. ∎
    
    Character Index notation will simplify many of the subsequent proofs, so it is worth taking a moment to become familiar with its usage. Indexing starts at 1, consistent with the definition of **N**:sub:`n` made in the preamble. So, *t[1]* is the first character of *t*, *t[2]* is the second, and so on.
    
    In terms of the Character-level set representation, *t[i]* refers to the Character at position *i* in the set **T**. In other words, the notation *t[i]* implicitly assumes the String *t* has already been stripped of its Empty Characters through the Emptying Algorithm in :ref:`Definition 1.1.2 <definition-1-1-2>`. This notation can effectively replace the use of lowercase Fraktur letters with subscripts (e.g., *𝔞*:sub:`i`) when referring to specific Characters within Strings.
    
    **Example**
    
    If *s = "abc"*, then *s[1] = "a"*, *s[2] = "b"*, and *s[3] = "c"*. ∎
    
    With the notion of String Length established for each element in the domain and some of its basic properties established, the size of the domain itself, **S**, will now be elaborated in greater detail.
      
    It is assumed **S** is at least uncountably infinite. A rigorous proof of this fact would carry the current work too far into the realm of real analysis, but as motivation for this assumption, an informal proof is presented below based on Cantor's famous diagonalization argument. 
    
    .. _theorem-1-1-2:
    
    **Theorem 1.1.2** :math:`\lvert S \rvert \geq \aleph_{1}`
    
    Assume, for the sake of contradiction, that the set of all Strings **S** is countable. This means the Strings can be listed in some order, 
    
    .. math::
        
        1. \quad s_1, s_2, s_3, ...
    
    Now, construct a new String *t* as follows:
    
        1. The first character of *t* is different from the first character of *s*:sub:`1`.
        2. The second character of *t* is different from the second character of *s*:sub:`2`.
        3. etc.
    
    This string *t* will be different from every string in **S** contradicting the assumption that it was possible to list all strings. Therefore, **S** must be uncountable. ∎ 
    
    .. _containment:
    
    Containment
    ^^^^^^^^^^^
    
    Similar to the explication of *length*, the notion of a String *containing* another String must be made precise using the definitions introduced so far. It's important to note that in the current system the relation of *containment* is materially different from the standard subset relation between sets. For example, the set of characters in *"rat"* is a subset of the set of characters in *"tart"*, but *"rat"* is not contained in *"tart"* because the order of the characters is different.
    
    Consider the Strings *"rat"* and *"strata"*. The string *"rat"* *is contained* in the String strata", because the order of the String *"rat"* is preserved in *"strata"*. An intuitive way of capturing this relationship is to map the indices of the Characters in *"rat"* to the indices of the Characters in *"strata"* which correspond to the indices in *"rat"*. A cursory (but incorrect) definition of *containment* can then be attempted, using this insight as a guide.
    
    **Containment (Incorrect Version)** :math:`t \subset_s u` 
    
    Let *t* and *u* be Strings. *t* is said to be *contained in u*, denoted by,
    
    .. math::
    
        t \subset_s u
    
    If and only if there exists a strictly increasing function :math:`f: N_{l(t)} \to N_{l(u)}` such that:
    
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
    
        T = \{ (1, \text{"b"}), (2, \text{"o"}), (3, \text{"w"}) \}
         
    .. math::
    
        U = \{ (1, \text{"b"}), (2, \text{"o"}), (3, \text{"r"}), (4, \text{"r"}), (5, \text{"o"}), (6, \text{"w"}) \}
    
    The function defined through :math:`f(1) = 1`, :math:`f(2) = 5` and  :math:`f(3) = 6` satisfies the conditions of the proposed definition. However, intuitively, *"bow"* is *not contained* in the word *"borrow"*. The reason the proposed definition has failed is now clear: the function *f* that is mapping *"bow"* to *"borrow"* skips over the Character indices 2, 3 and 4 in *"borrow"*. In other words, in addition to being strictly increasing, the function *f* which maps the smaller String onto the larger String must also be *consecutive*. This insight can be incorporated into the definition of *containment* by first defining the notion of *consecutive*,
    
    .. _definition-1-1-6:
    
    **Definition 1.1.6: Consecutive Functions** 
    
    A function *f* is consecutive over **N**:sub:`s` if it satisfies the formula,
    
    .. math::
    
        \forall i, j \in N_s: (i < j) \to f(j) = f(i) + (j - i)`
        
    ∎
        
    This additional constraint on *f* ensures that the indices of the larger String in the containment relation are mapped in a sequential, unbroken order to the indices of the smaller String. This definition of *Consecutive Functions* can be immediately utilized to refine the notion of *containment*.
    
    .. _definition-1-1-7:
    
    **Definition 1.1.7: Containment** :math:`t \subset_{s} u` 
    
    Let *t* and *u* be Strings. *t* is said to be *contained in u*, denoted by,
    
    .. math::
    
        t \subset_{s} u
    
    If and only if there exists a strictly *increasing and consecutive* function :math:`f: N_{l(t)} \to N_{l(u)}` such that:
    
    .. math::
    
        \forall i \in N_{l(t)}: t[i] = u[f(i)] 
        
    ∎
    
    The notion of containment will be central to developing the logic of palindromic structures in the subsequent sections. The next theorem establishes a fundamental property regarding containment.
    
    .. _theorem-1-1-3:
    
    **Theorem 1.1.3** :math:`\forall s \in S: \varepsilon \subset_s s`
    
    Let *s* be an arbitrary string in **S**. By :ref:`Definition 1.1.3 <definition-1-1-3>`, :math:`l(\varepsilon) = 0`. Thus,
    
    .. math::
    
       1. \quad N_{l(\varepsilon)} = \emptyset
    
    The empty function :math:`f: \emptyset \to N_{l(s)}` vacuously satisfies the condition for containment (:ref:`Definition 1.1.7 <definition-1-1-7>`), as there are no elements in the domain to violate the condition. Therefore, 
    
    .. math::
    
        2. \quad \varepsilon \subset_s s
    
    Since *s* was arbitrary, this can be generalized over the set of all Strings,
     
    .. math::
    
        3. \quad \forall s \in S: \varepsilon \subset_s s
        
    ∎
    
    .. _section-i-ii:
    
    Section I.II: Words
    -------------------
    
    While the notion of Characters maps almost exactly to the intuitive notion of letters in everyday use, the notion of a *Word* requires explication. 
    
    If Characters are mapped to letters in the Alphabet of a Language **L**, the set of all Strings would have as a subset the Language that is constructed through the Alphabet. The goal of this section is to define the syntactical properties of Words in **L** that differentiates them from Strings in **S** based solely on their internal cohesion as a linguistic unit. The intent of this analysis is to treat Words as interpretted constructs embedded in a syntactical structure that is independent of their specific interpretations. In other words, this analysis will proceed without assuming anything about the interpretation of the Words in the Language beyond the fact that they *are* Words of the Language. The goal is to leave the semantic interpretation of Words in a Language as ambiguous as possible. This ambiguity, it is hoped, will leave the results of the analysis applicable to palindromic structures in a variety of languages, and perhaps make the formal system applicable to areas outside the realm of Palindromes.
    
    .. _definition-1-2-1:
    
    **Definition 1.2.1: Language** 
    
    A Language **L** is a set of Strings constructed through concatenation on an Alphabet **Σ** that are assigned semantic content. ∎
    
    .. _definition-1-2-2:
    
    **Definition 1.2.2: Word** 
    
    A Word is an element of a Language **L**. ∎
    
    The following symbolic notation is introduced for these terms, 
    
        1. Words (*a*, *b*, *c*, etc.): Lowercase English letters represent Words. Subscripts will occassionally be used to denote Words, (*a*:sub:`1`, *a*:sub:`2`, ... )
        2. Language (**L**): The uppercase English letter *L* in boldface represents a Language.
    
    In the case of English, Words would correspond to words such as "dog", "cat", etc. A Language would correspond to a set of words such as :math:`\{ \text{"dog"}, \text{"cat"}, \text{"hamster"}, ... \}` or :math:`\{ \text{"tree"}, \text{"flower"}, \text{"grass"}, .... \}`. The number of Words in a Language is denoted :math:`\lvert L \rvert`.
    
    Again, at the risk of unwarranted repetition, Language is assumed to be a *fixed set* known a priori to the construction of the current formal system. It not the goal of the formal system to describe the semantic conditions for a Word's eligibility in Language or how a Language is constructed from elementary Characters and Strings into a class of Words through systems like grammar or pragmatics, but rather, given a Language of Words, the formal system seeks to elaborate the syntactical conditions that are imposed on Language by its nature as a set of Strings with ordered Characters. 
    
    Note, :ref:`Definition 1.2.1 <definition-1-2-1>` and :ref:`Definition 1.2.2 <definition-1-2-2>` relies on the idea that Words are Strings and their meaning is conveyed through the ordered sequence of its concatenated Characters. This necessarily precludes from the formal system any languages which do *not* use the ordering of Characters as the primary medium for representing Words. While edge cases like sign language exist, nevertheless, the sole constitutive feature of any natural is the *ordering* of some type of Character. In the case of sign language, a Character in the formal system might be identified with *"a configuration of fingers"* and a String might be identified with *"configurations over time"*.
    
    It will sometimes be necessary to refer to indeterminate Words, so notation is introduced for Word Variables,
    
        1. Word Variables (*α*, *β*, *γ*): The Lowercase Greek letters Alpha, Beta and Gamma will represent variable Words, i.e. indeterminate Words. Subscripts will occassionally be used with Alpha to denote Word Variables, (*α*:sub:`1`, *α*:sub:`2`, ... ). 
    
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
    
    .. _definition-1-2-3:
    
    **Definition 1.2.3: Word Equality**
    
    Let *a* and *b* be words in **L**. Then *a = b* if and only if *a* and *b* are equal as Strings (according to :ref:`Definition 1.1.4 <definition-1-1-4>`). ∎ 
    
    The next axiom represents the minimal *necessary* assumptions that are placed on any String to be considered an element of a Language **L**, i.e. a Word. The axiom listed in this section is not *sufficient*; in other words, it is possible for a String to satisfy this axiom without being an element of a Language, but any Word that belongs to a Language must satisfy the axiom.
    
    .. _axiom-w1:
    
    **Axiom W.1: The Discovery Axiom** 
    
    .. math::
    
        \forall \alpha \in L: [ (l(\alpha) \neq 0) \land (\forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma) ]
    
    ∎
    
    There are two conjuncts in the :ref:`Discovery Axiom W.1 <axiom-w1>` and each of them captures a noteworthy assumption that is being made about Words in a Language. The first conjunct, (:math:`l(\alpha) \neq 0`), will be used to prove some fundamental properties of Words in the next section. This condition that a Word's String Length cannot be equal to zero serves a dual purpose. First, by :ref:`Definition 1.1.3 <definition-1-1-3>`, it ensures the Empty Character cannot be a Character in a Word (this fact will be more rigorously proven in :ref:`Theorem 1.2.4 <theorem-1-2-4>` below), preventing vacuous semantic content. 
    
    Second, in order for two Words to be distinguished as the same Word, there must be dimensions of comparision over which to assert the equality. One must have some criteria for saying *this* linguistic entity is equal to that *that* linguistic entity. String Length serves as one of the two dimensions for a Word necessary for a word to be "embodied" in a medium (the other being the inherent ordinality of Characters in a Word). In other words, the concept of String Length is foundational to the discovery of Words from the set of all Strings **S**. One must be able to discard those Strings possessing null content before one can engage in Language. 
    
    While the definition of String Length and the first conjunct preclude the inclusion of the Empty Character in a Word, there is no such restriction on the Delimiter, hence the second conjunct of the :ref:`Discovery Axiom <axiom-w1>`. This conjunct captures the common-sense notion that a Word from a Language cannot contain a Delimiter; Instead, Delimiters are what separate Words from one another in a String. 
    
    It is these two purely syntactical properties that allow a user of Language to separate Words from the arbitrary chaos of Strings, preparing them for the assignment of semantic content. 
    
    .. _word_theorems:
    
    Theorems
    ^^^^^^^^
    
    The next theorems establish some basic results about Words in a Language within this formalization. All of these theorems should conform to the common sense notion of Words. 
    
    .. _theorem-1-2-1:
    
    **Theorem 1.2.1** :math:`\forall \alpha \in L:  \alpha \varepsilon = \varepsilon \alpha = \alpha`
    
    This theorem can be stated in natural language as follows: For every Word in a Language, concatenating the Word with the empty String *ε* on either side results in the Word itself.
    
    Let *α* be an arbitrary word in **L**. By :ref:`Definition 1.2.2 <definition-1-2-2>`, *α* is a String of characters. By :ref:`Definition 1.1.3 <definition-1-1-3>`, :math:`l(\alpha)` is the number of non-Empty Characters in *α*. 
    
    Consider *ε*, the empty string. By :ref:`Definition 1.1.3 <definition-1-1-3>`, :math:`l(\varepsilon) = 0`. By Definition 1.1.1, the concatenation of any String *s* with *ε* results in a new string with the same Characters as *s* in the same order.
    
    Therefore, *αε* and *εα* are both Strings with the same Characters as *α* in the same order. Since *α* is a Word in **L** and concatenation with *ε* does not change its length or order of Characters. Thus, by :ref:`Definition 1.2.3 <definition-1-2-3>`, 
    
    .. math::
    
        1. \quad \alpha\varepsilon = \varepsilon\alpha = \alpha.
    
    Since *α* was arbitrary, this can be generalized over the Language, 
    
    .. math::
    
        2. \quad \forall \alpha \in L:  \alpha\varepsilon = \varepsilon\alpha = \alpha
    
    ∎
    
    .. _theorem-1-2-2:
    
    **Theorem 1.2.2** :math:`\forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \subset_s \alpha`
    
    This theorem can be stated in natural language as follows: All Characters in a Word are contained in the Word.
    
    Assume *α* is a Word from Language **L**. By the :ref:`Discovery Axiom W.1 <axiom-w1>`, :math:`l(\alpha) \neq 0` and thus it must have at least one non-Empty Character *α[i]* for some non-zero *i*.
    
    Consider the String *s* with a single Character :math:`\mathfrak{b}_1 = \alpha[i]`.
    
    .. math::
    
        1. \quad s = \alpha[i]
    
    Clearly, by :ref:`Definition 1.1.3 <definition-1-1-3>`, :math:`l(s) = 1`. To show that *s* is contained in *α*, a strictly increasing and consecutive function that maps the Characters in *s* to the Characters in *α* must be found. Since :math:`l(s) = 1`, this can be defined simply as,
    
    .. math::
    
        2. \quad f(1) = i
    
    For any value of *i*. Therefore, by :ref:`Definition 1.1.7 <definition-1-1-7>`,
    
    .. math::
    
        3. \quad \alpha[i] \subset_{s} \alpha 
        
    Since *α* and *i* are arbitary, this can be generalized, 
    
    .. math::
    
        4. \quad \forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \subset_{s} \alpha
    
    The next theorem, :ref:`Theorem 1.2.3 <theorem-1-2-3>`, is the direct result of defining String length as the number of non-Empty characters in a String and then defining containment based on String length. Careful inspection of :ref:`Definition 1.1.7 <definition-1-1-7>` will show that it depends on a precise notion of String Length. In other words, in the current formal system, containment is derivative of length. The order of definitions and axioms in any formal system of Language cannot be of an arbitary character. There is an inherent hierarchical structure in linguistics that must be captured and formalized in the correct order.
    
    .. _theorem-1-2-3:
    
    **Theorem 1.2.3**  :math:`\forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon`
    
    Let *α* be an arbitrary word in **L**, and let *i* be a natural number such that,
     
    .. math::
    
        1. \quad 1 \leq i \leq l(\alpha)
        
    By the :ref:`Discovery Axiom W.1 <axiom-w1>`, it is known that :math:`l(\alpha) \neq 0`.
    
    By :ref:`Definition 1.1.3 <definition-1-1-3>`, the length of a String is the number of non-Empty Characters it contains in its Character-level set representation **Α**. Since :math:`l(\alpha) > 0`, *α* must have at least one non-Empty character.
    
    Since :math:`1 \leq i \leq l(\alpha)`, the Character at position *i* in *α*, denoted *α[i]*, exists and is non-Empty, :math:`α[i] \neq \varepsilon`. Since *α* and *i* are arbitrary, this can generalized over the Language,
    
    .. math::
    
       2. \quad \forall \alpha \in L : \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon
    
    ∎
    
    :ref:`Theorem 1.2.1 <theorem-1-2-1>` - :ref:`1.2.3 <theorem-1-2-3>` are the necessary logical pre-conditions for Words to arise from the domain of Strings. In essence, before Language can be distinguished from its uncountably infinite domain, a way of measuring String length must be introduced. This definition must prevent Empty Strings from entering into the Language, which would otherwise allow the annunciation of null content. Then it must be assumed for semantic content to be assigned to a series of concatenated Characters the length of that String must be non-zero. This is the meaning of the first conjunct in the :ref:`Discovery Axiom W.1 <axiom-w1>`.
    
    Language is materially different from its un-structured domain of Strings for this reason. Language does not possess null content. Language is measureable. Words in Language have String Length. Moreover, Words are delimited. In other words, Words are separable, distinct linguistic entities. These facts are guaranteed by the :ref:`Discovery Axiom W.1 <axiom-w1>` and :ref:`Theorem 1.2.1 <theorem-1-2-1>` - :ref:`Theorem 1.2.3 <theorem-1-2-3>`. These results provide the canvas upon which the rest of the theory will be drawn.
    
    There may appear to be a contradiction in the results of :ref:`Theorem 1.1.3 <theorem-1-1-3>`, which states the Empty Character is contained in every String, and :ref:`Theorem 1.2.3 <theorem-1-2-3>`, which states no Character in a Word can be the Empty Character. Every Word is a String, by :ref:`Definition 1.2.2 <definition-1-2-2>`, so the results appear at odds. The solution to this apparent contradiction lies in how Characters and Strings have been formalized as distinct, but interrelated, terms. The contradiction is no longer a contradiction once the distinction between a String being contained in another String and a Character being a constituent element at a specific position with in a String is understood.
    
    The containment relation :math:`\varepsilon \subset_s s` refers to the Empty Character as a subsequence of *s*. The relation being expressed is about the sequence of Characters, and the Empty sequence is always a subsequence of any other sequence.
    
    :ref:`Theorem 1.2.3 <theorem-1-2-3>`, on the other hand, refers to individual Characters at specific positions within a Word. It is a claim about the elements of the Character-level representation (e.g., the *ι* in :math:`(i, ι) \in A`).
    
    .. _string-inversion:
    
    String Inversion
    ^^^^^^^^^^^^^^^^
    
    Before developing the palindromic structure and symmetries in Words and Language, an operation capable of describing this symmetry much be introduced. Informally, the *Inverse* of a String is the reversed sequence of Characters in a String. The goal of this section is to define this notion precisely. In the process, the motivation for this definition as it pertains to Words will be elucidated. 
    
    .. _definition-1-2-4:
    
    **Definition 1.2.4: String Inversion** 
    
    Let *s* be a string with length *l(s)*. Then, let *t* be a String with length *l(t)*.
        
    *t* is called the Inverse of *s* and is denoted *inv(s)* if it satisfies the following conditions, 
    
    .. math::
    
        l(t) = l(s)
    
    .. math::
    
        \forall i \in N_{l(s)}: t[i] = s[l(s) - i + 1]
     
    ∎
    
    Note the advantage of Character Index notation in stating this definition. The quantification in the second clause of :ref:`Definition 1.2.4 <definition-1-2-4>` can be made directly over the natural numbers, rather than the intermediary of the Character level set representation of *t* and *s*.
    
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
    
    Since every Word is a String, the Inverse of Word is similarly defined, with the additional constraint that *s* belong to a Language **L**, i.e. by adding a third bullet to :ref:`Definition 1.2.4 <definition-1-2-4>` with :math:`s \in L`. The Inverse of a Word is easily understood through a few illustrative examples in English. The following table lists some words in English and their Inverses,
    
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
    
    
    However, this particular example is (intentionally) misleading. In this example, the Inverse of a word in English is also a word in English. In general, this property is not exhibited by the majority of Words in any Language. In other words, every Word in an Language has an Inverse but not every Inverse Word belongs to a Language. This phenomenon is exemplified in the following table,
    
    .. list-table::
        :widths: 20 20
        :header-rows: 1
    
        * - Word
          - Inverse
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
    
    The intent is to define a class of Words whose elements belong to it if and only if their Inverse exists in the Language. As a first step towards this definition, String Inversion was introduced and formalized. In the next section, String Inversion will provide a subdomain in the domain of discourse over which to quantify the conditions that are to be imposed on the class of *Invertible Words*, i.e. the class of Words whose Inverses are also Words. 
    
    Note, Invertible Words are often termed *semordnilaps* in linguistics. The terminology *invertible* is adopted here to emphasis the structural inversion that is occuring on the Character-level within this class of Words. 
    
    Before defining the class of Invertible Words in the sequel, this section is concluded with theorems that strengthen the definition of String Inversion. These theorems will be used extensively in all that follows.
    
    .. _theorem-1-2-4:
    
    **Theorem 1.2.4** :math:`\forall s \in S: \text{inv}(\text{inv}(s)) = s`
    
    Let *s* be a String with length *l(s)* and Characters *𝔞*:sub:`i`. 
    
    Let :math:`t = \text{inv}(s)` with length *l(t)* and Characters *𝔟*:sub:`j`.
    
    By the :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        1. \quad l(t) = l(s)
    
    .. math::
    
        2. \quad \forall i \in N_{l(s)}: t[i] = s[l(s) - i + 1]
    
    Now, let :math:`u = inv(t)` with length *l(u)*. Applying :ref:`Definition 1.2.4 <definition-1-2-4>` again,
    
    .. math::
    
        3. \quad l(u) = l(t)
        
    .. math::
    
        4. \quad \forall j \in N_{l(t)}: u[j] = t[l(t) - j + 1]
    
    Since :math:`l(t) = l(s) = l(u)` and :math:`N_{l(t)} = N_{l(s)} = N_{l(u)}` (from step 1, step 3 and by definition of natural numbers), these substitions may be made in step 4,
    
    .. math::
    
        5. \quad \forall j \in N_{l(s)}: u[j] = s[l(s) - (l(t) - j + 1) + 1]
    
    Simplifying the index on the right hand side,
    
    .. math::
    
        6. \quad \forall j \in N_{l(s)}: u[j] = s[j]
    
    Since *u* and *s* have the same length (:math:`l(u) = l(t) = l(s)`) and the same Characters in the same order (:math:`u[j] = s[j]` for all *i*), by :ref:`Definition 1.1.4 <definition-1-1-4>` of String Equality, it can be concluded that :math:`u = s`. Recall that :math:`u = \text{inv}(t)` and :math:`t = \text{inv}(s)`. Substituting, the desired result is obtained, :math:`\text{inv}(\text{inv}(s)) = s`. ∎ 
    
    Two versions of :ref:`Theorem 1.2.5 <theorem-1-2-5>` are given, the first using only the Character-level representation of a String, the second using Character Index notation. This is done to show the two formulations are equivalent, and it is a matter of personal preference which style of notation is employed. Throughout the rest of this work, the Character Index notation is primarily utilized, although there are several proofs that are better served by the Character-level representation.
    
    .. _theorem-1-2-5:
    
    **Theorem 1.2.5 (Character-level Representation)** :math:`\forall u, t \in S: \text{inv}(ut) = \text{inv}(t)\text{inv}(u)`
    
    Let **U** be the Character level representation of *u*,
    
    .. math::
    
        1. \quad U = (\mathfrak{a}_1 , \mathfrak{a}_2 , ..., \mathfrak{a}_{l(u)})
    
    Let **T** be the Character level representation of *t*,
    
    .. math::
    
        2. \quad T = (\mathfrak{b}_1, \mathfrak{b}_2, ... , \mathfrak{b}_{l(t)})
    
    The Character level representation of *ut*, denoted **UT**, is then given by,
    
    .. math::
    
        3. \quad UT = (\mathfrak{a}_1 , \mathfrak{a}_2 , ..., \mathfrak{a}_{l(u)}, \mathfrak{b}_1, \mathfrak{b}_2 , ... , \mathfrak{b}_{l(t)})
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>` of String Inversion, the Character level representation of *inv(ut)* is the reversed sequence of **UT**,
    
    .. math::
    
        4. \quad \text{inv}(UT) = ( \mathfrak{b}_{l(t)}, ..., \mathfrak{b}_2 , \mathfrak{b}_1 , \mathfrak{b}_{l(u)}, ..., \mathfrak{a}_2 , \mathfrak{a}_1)
    
    The Character level representation of *inv(u)*, denoted **inv(U)**,
    
    .. math::
    
        5. \quad \text{inv}(U) = (\mathfrak{a}_{l(u)}, ..., \mathfrak{a}_2 , \mathfrak{a}_1)
    
    The Character-level representation of *inv(t)*, denoted **inv(T)** is 
    
    .. math::
    
        6. \quad \text{inv}(T) = ( \mathfrak{b}_{l(t)}, ..., \mathfrak{b}_2 , \mathfrak{𝔟}_1 )
    
    The Character-level representation of *inv(t)inv(u)*, denoted **inv(T)inv(U)** is:
    
    .. math::
    
        7. \quad \text{inv}(T)\text{inv}(U) = ( \mathfrak{b}_{l(t)}, ..., \mathfrak{b}_2 , \mathfrak{b}_1, \mathfrak{a}_{l(u)}, ..., \mathfrak{a}_2 , \mathfrak{a}_1)
    
    Comparing the results from step 4 and step 7, it can be seen the Character-level representations of *inv(ut)* and *inv(t)inv(u)* are identical.
    
    Therefore, :math:`\text{inv}(ut) = \text{inv}(t)\text{inv}(u)`. ∎
    
    .. _theorem-1-2-5-b:
    
    **Theorem 1.2.5 (Character Index Notation)**: :math:`\forall u, t \in S: \text{inv}(ut) = \text{inv}(t)\text{inv}(u)`
    
    Let *u* and *t* be arbitrary strings in **S**. Let :math:`l(u) = m` and :math:`l(t) = n`. Then, :math:`l(ut) = m + n`, by :ref:`Definition 1.1.3 <definition-1-1-3>`.
    
    Let :math:`s = ut` . Let :math:`v = \text{inv}(s) = \text{inv}(ut)` . Let :math:`w = \text{inv}(t)\text{inv}(u)` .
    
    To prove show the theorem, it must be shown that :math:`v = w`, which means, by :ref:`Definition 1.1.4 <definition-1-1-4>`, it must be shown that 
    
    .. math::
    
        1. \quad l(v) = l(w)
        
    .. math::
    
        2. \quad \forall i ∈ N_{l(v)}: v[i] = w[i] 
    
    By repeated applications of :ref:`Definition 1.2.4 <definition-1-2-4>`, 
    
    .. math::
    
        3. \quad l(v) = l(s) = l(ut) = m + n
        
    .. math::
    
        4. \quad l(\text{inv}(t)) = l(t) = n
        
    .. math::
    
        5. \quad l(\text{inv}(u)) = l(u) = m
    
    From step 3 and step 4, it follows,
     
    .. math::
    
        5. \quad l(w) = l(\text{inv}(t)\text{inv}(u)) = l(\text{inv}(t)) + l(\text{inv}(u)) = n + m = m + n.
    
    From steps 4 and 5, it follows, 
    
    .. math::
    
        6. \quad l(v) = l(w) = m + n
    
    Now it is to be shown that :math:`v[i] = w[i]`` for all :math:`i \in N_{l(v)}`. Let *i* be an arbitrary index such that :math:`1 \leq i \leq m + n`.
    
    **Case 1**: :math:`1 \leq i \leq m + n`
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        a. \quad v[i] = s[l(s) - i + 1]
    
    Since *l(s) = m + n*, it follows,
    
    .. math::
    
        b. \quad v[i] = s[m + n - i + 1]
        
    Since *m + n - i + 1* corresponds to an index in *t*, it follows,
    
    .. math::
    
        c. \quad v[i] = t[n - i + 1]
        
    By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        d. \quad v[i] = \text{inv}(t)[i]
    
    Since :math:`w = \text{inv}(t)\text{inv}(u)`,
    
    .. math::
    
        e. \quad v[i] = w[i]
    
    **Case 2**: :math:`n + 1 \leq i \leq m + n`:
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        a. \quad v[i] = s[l(s) - i + 1]
    
    Since :math:`l(s) = m + n`,
    
    .. math::
    
        b. \quad v[i] = s[m + n - i + 1]
    
    Since *m + n - i + 1* corresponds to an index in *u*,
    
    .. math::
    
        c. \quad v[i] = u[m - (i - n) + 1] 
    
    Simplifying,
    
    .. math::
    
        d. \quad v[i] = u[m + n - i + 1]
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        e. \quad v[i] = \text{inv}(u)[i - n]
    
    Since :math:`w = \text{inv}(t)\text{inv}(u)`,
    
    .. math::
    
        f. \quad v[i] = w[i] (since w = inv(t)inv(u))
    
    In both cases, :math:`v[i] = w[i]` for all :math:`i \in N_{l(v)}`. Since :math:`l(v) = l(w)`, by :ref:`Definition 1.1.4 <definition-1-1-4>` it follows :math:`v = w`. Therefore, 
    
    .. math::
    
        7. \quad \text{inv}(ut) = \text{inv}(t)\text{inv}(u).
    
    Since *u* and *t* were arbitrary Strings, this can generalize over the set of all Strings,
    
    .. math::
    
        8. \quad \forall u, t \in S: \text{inv}(ut) = \text{inv}(t)\text{inv}(u) ∎
    
    The next theorem establishes the *"distributivity"* of String inversion over the relation of containment. 
    
    .. _theorem-1-2-6:
    
    **Theorem 1.2.6** :math:`\forall u, t \in S : u \subset_s t \leftrightarrow \text{inv}(u) \subset_s \text{inv}(t)`
    
    This theorem can be stated in natural language as follows: For any two Strings *u* and *t*, *u* is contained in *t* if and only if the Inverse of *u* is contained in the Inverse of *t*.
    
    Let *u* and *t* be arbitrary Strings in **S**.
    
    (→) Assume,
    
    .. math::
    
        1. \quad u \subset_s t
    
    By :ref:`Definition 1.1.7 <definition-1-1-7>`, there exists a strictly increasing and consecutive function :math:`f: N_{l(u)} \to N_{l(t)}` such that,
    
    .. math::
    
        1. \quad \forall i \in N_{l(u)}: u[i] = t[f(i)]
    
    Let,
    
    .. math::
    
        3. \quad v = \text{inv}(t)
    
    .. math::
    
        4. \quad w = \text{inv}(u).
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        5. \quad \forall i \in N_{l(u)}: w[i] = \text{inv}(u)[i] = u[l(u) - i + 1]
    
    .. math::
    
        6. \quad \forall i \in N_{l(t)}: v[i] = \text{inv}(t)[i] = t[l(t) - i + 1]
       
    Define a function :math:`g: N_{l(w)} \to N_{l(v)}`  as follows,
    
    .. math::
    
        7. \quad g(i) = l(t) - f(l(u) - i + 1) + 1
    
    This function maps the Character indices of *w* (the inverse of *u*) to the indices of *v* (the inverse of *t*).
    
    **Increasing** To show *g* is strictly increasing, let
    
    .. math::
    
        8. \quad i, j \in N_{l(w)}
    
    Such that :math:`i < j`. Since :math:`l(w) = l(u)`,
    
    .. math::
    
        9. \quad i, j \in N_{l(u)}
    
    Because *f* is strictly increasing, and
    
    .. math::
    
        10. \quad l(u) - j + 1 < l(u) - i + 1,
    
    It follows,
    
    .. math::
    
        11. \quad f(l(u) - j + 1) < f(l(u) - i + 1)
    
    Therefore,
    
    .. math::
    
        12. \quad l(t) - f(l(u) - i + 1) + 1 < l(t) - f(l(u) - j + 1) + 1
    
    which means
    
    .. math::
    
        13. \quad g(i) < g(j).
    
    Thus, *g* is strictly increasing.
    
    **Consecutive** To show *g* is consecutive, let
    
    .. math::
    
        14. \quad i \in N_{l(w)}
    
    Such that :math:`i < l(w)`. Then,
    
    .. math::
    
        15. \quad g(i+1) = l(t) - f(l(u) - (i + 1) + 1) + 1
        
    .. math::
    
        16. \quad g(i+1) = l(t) - f(l(u) - i - 1 + 1) + 1
    
    Since *f* is consecutive, we have:
    
    .. math::
    
        17. \quad f(l(u) - i - 1 + 1) = f(l(u) - i) + 1
    
    Then,
    
    .. math::
    
        18. \quad g(i+1) = l(t) - (f(l(u) - i) + 1) + 1
        
    .. math::
    
        19. \quad g(i+1) = l(t) - f(l(u) - i)
        
    .. math::
    
        20. \quad g(i+1) = l(t) - f(l(u) - i + 1) + 1 + 1 - 1
        
    .. math::
    
        21. \quad g(i+1) = l(t) - f(l(u) - i + 1) + 1
        
    .. math::
    
        22. \quad g(i+1) = g(i) + 1
    
    Thus *g* is consecutive.
    
    **Containment** Now, it must shown be that, 
    
    .. math::
    
        23. \quad \forall i \in N_{l(w)}: w[i] = v[g(i)]
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        24. \quad w[i] = u[l(u) - i + 1]
    
    From step 2, it follows,
    
    .. math::
    
        25. \quad w[i] = t[f(l(u) - i + 1)]
    
    By definition of *g*,
    
    .. math::
    
        26. \quad g(i) = l(t) - f(l(u) - i + 1) + 1
    
    Rearranging,
    
    .. math::
    
        27. \quad f(l(u) - i + 1) = l(t) - g(i) + 1
    
    Substituting into step 25,
    
    .. math::
    
        28. \quad w[i] = t[l(t) - g(i) + 1]
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>` and the definition of *v*,
    
    .. math::
    
        29. \quad v[g(i)] = t[l(t) - g(i) + 1]
    
    Therefore,
    
    .. math::
    
        30. \quad w[i] = v[g(i)]
    
    Since this holds for all :math:`i \in N_{l(w)}`, and *g* is a strictly increasing and consecutive function, by :ref:`Definition 1.1.7 <definition-1-1-7>`, it follows,
    
    .. math::
    
        31. \quad w \subset_s v
    
    Therefore,
    
    .. math::
    
        32. \quad \text{inv}(u) \subset_s \text{inv}(t)
    
    (←) Assume
    
    .. math::
    
        1. \quad \text{inv}(u) \subset_s \text{inv}(t)
    
    By :ref:`Theorem 1.2.4 <theorem-1-2-4>`,
    
    .. math::
    
        2. \quad \text{inv}(\text{inv}(u)) = u
    
    .. math::
    
        3. \quad \text{inv}(\text{inv}(t)) = t
    
    Therefore, using the result just proved in the (→) direction, it can be said since
    
    .. math::
    
        4. \quad \text{inv}(u) \subset_s \text{inv}(t)
    
    This implies,
    
    .. math::
    
        5. \quad \text{inv}(\text{inv}(t)) \subset_s \text{inv}(\text{inv}(u))
    
    Substituting in steps 2 and 3,
    
    .. math::
    
        6. \quad t \subset_s u
    
    Since both directions of the implication hold, it follows,
    
    .. math::
    
        1. \quad \forall u, t \in S: u \subset_s t \leftrightarrow \text{inv}(u) \subset_s \text{inv}(t) ∎
    
    The next theorem establishes the *transitivity* of containment over Strings. 
    
    .. _theorem-1-2-7:
    
    **Theorem 1.2.7** :math:`\forall t, u, v \in S : (t \subset_s u) \land (u \subset_s v) \to (t \subset_s v)`
    
    This theorem can be stated in natural language as follows: For any Strings *t*, *u*, and *v* in **S**, if *t* is contained in *u* and *u* is contained in *v*, then *t* is contained in *v*.
    
    Let *t*, *u*, and *v* be arbitrary Strings in **S** such that both of the following expressions are true,
    
    .. math::
    
        1. \quad t \subset_s u
    
    .. math::
    
        2. \quad u \subset_s v
    
    By :ref:`Definition 1.1.7 <definition-1-1-7>` and step 1, there exists a strictly increasing and consecutive function :math:`f: N_{l(t)} \to N_{l(u)}` such that,
    
    .. math::
    
        3. \quad \forall i \in N_{l(t)}: t[i] = u[f(i)]
    
    Similarly, by :ref:`Definition 1.1.7 <definition-1-1-7>` and step 2, there exists a strictly increasing and consecutive function :math:`g: N_{l(u)} \to N_{l(v)}` such that:
    
    .. math::
    
        4. \quad \forall j \in N_{l(u)}: u[j] = v[g(j)]
    
    Define a new function :math:`h: N_{l(t)} \to N_{l(v)}` as the composition of *f* and *g*,
    
    .. math::
    
        5. \quad \forall j \in N_{l(t)}: h(i) = g(f(i))
    
    **Increasing** Let 
    
    .. math::
    
        6. \quad i, j \in N_{l(t)} 
        
    Such that :math:`i < j`. Since *f* is strictly increasing, 
    
    .. math::
    
        7. \quad f(i) < f(j) 
    
    Since *g* is strictly increasing, 
    
    .. math::
    
        8. \quad g(f(i)) < g(f(j))
        
    Therefore, 
    
    .. math::
    
        9. \quad h(i) < h(j)
        
    Thus, *h* is strictly increasing.
    
    **Consecutive** Let 
    
    .. math::
    
        10. \quad i \in N_{l(t)} 
        
    Such that :math:`i < l(t)`. Since *f* is consecutive, 
    
    .. math::
    
        11. \quad f(i+1) = f(i) + 1 
        
    Since *g* is consecutive, following from step 11,
    
    .. math::
    
        12. \quad g(f(i+1)) = g(f(i) + 1) = g(f(i)) + 1
        
    Therefore, 
    
    .. math::
    
        13. \quad h(i+1) = h(i) + 1
    
    Thus, *h* is consecutive.
    
    **Containment** Let 
    
    .. math::
    
        14. \quad i \in N_{l(t)} 
        
    Then, by step 3
    
    .. math::
    
        15. \quad t[i] = u[f(i)]
    
    Since :math:`f: N_{l(t)} \to N_{l(u)}`, it follows that for all 
    
    .. math::
    
        16. \quad \forall i \in N_{l(t)}: f(i) \in N_{l(u)}`
    
    By step 16 and step 4,
    
    .. math::
    
        17. \quad u[f(i)] = v[g(f(i))]
    
    By definition of *h*,
    
    .. math::
    
        18. \quad v[g(f(i))] = v[h(i)]
    
    Therefore, 
    
    .. math::
    
        19. \quad \forall i \in N_l(t): t[i] = v[h(i)]
    
    Since *h* is a strictly increasing and consecutive function over :math:`N:sub:`l(t) \to N_{l(v)}`, and :math:`t[i] = v[h(i)]` for all :math:`1 \leq i \leq l(t)`, by :ref:`Definition 1.1.7 <definition-1-1-7>`,
    
    .. math::
    
        20. \quad t \subset_s v.
    
    Since *t*, *u*, and *v* were arbitrary Strings, this can be generalized over the set of all Strings,
    
    .. math::
    
        21. \quad \forall t, u, v \in S : (t \subset_s u) \land (u ⊂:sub:`s` v) \to (t subset_s v) ∎
    
    .. _phrases:
    
    Phrases
    ^^^^^^^
    
    While the analyis has not yet introduced the notion of Sentences into the formal system (see Section II), an operation will now be introduced that allows Words to be ordered into Phrases and then concatenated into Strings. This new operation will be important when String Inversion is applied to the sentential level of the formal system, allowing the conditions for a Sentence Inversion to be precisely specified.
    
    The placement of :ref:`Definition 1.2.5 <definition-1-2-5>` and :ref:`Definition 1.2.6 <definition-1-2-6>` is somewhat arbitary. There are valid arguments to be made for placing these definitions after the concepts of Sentence and Word Index notation have been introduced in :ref:`Section II <section-ii>`. However, since the operation of *Delimitation* and *Limitations* to be expounded immediately are essentially an operation defined on the domain of Strings which yields as a result another String, i.e. Delimitation and Limitation are closed with respect to Strings, the definitions are made here, to highlight the derivative notions (Inversion, Delimitation and Limitations) which can be built on top of the primitive notion of concatenation.
    
    .. _definition-1-2-5:
    
    **Definition 1.2.5: Phrase**
    
    Let *n* be a fixed, non-zero natural number, :math:`n \geq 1`. A Phrase of Word Length *n* from Language **L**, denoted **P**:sub:`n`, is defined as an ordered sequence of *n* (not necessarily distinct) Words,
    
    .. math::
    
        P_n = (\alpha_1, \alpha_2, ... , \alpha_n)
    
    where each :math:`\alpha_i \in L`. If *i* is such that :math:`1 \leq i \leq n`, :math:`P_n(i)` denotes the Word *α*:sub:`i` at index *i*, so that **P**:sub:`n` may be rewritten, 
    
    .. math::
    
        P_n = (P_n(1), P_n(2), ... , P_n(n))
    
    When :math:`n = 0`, **P**:sub:`0` is defined as the empty sequence (). ∎
    
    In order to establish some properties of Phrases, Delimitations and Limitations , a symbol for representing the range of a Phrase **P**:sub:`n` over a Language **L** is now defined.
    
    .. _definition-1-2-6:
    
    **Definition 1.2.6: Lexicon**
    
    Let *n* be a fixed natural number. We define a Language's *n*:sup:`th` Lexicon, denoted :math:`X_L(n)`, as the set of all Phrases of length *n* formed from Words in **L**,
    
    .. math::
    
        X_{L}(n) = \{ P_n \mid P_n = (\alpha_1, \alpha_2, ..., \alpha_n) \land \forall i \in N_n: \alpha_i \in L \} 
        
    ∎
    
    Some of the later theorems in this work will require quantifying over Phrases in a Language's *n*:sub:`th` Lexicon, so notation is introduced for Phrase Variables,
    
        1. Phrase Variables (*p*, *q*, *r*): The lowercase English letters *p*, *q*, *r* are reserved for representing indeterminate Phrases of a Language's *n*:sup:`th` Lexicon.
       
    Because Phrases are ordered sequences of Words, the Phrase Variable *p(i)* will denote, exactly like the Definition of a Phrase, the Word at index *i* for :math:`1 \leq i \leq n`.
    
    Using these pair of definitions for Phrases and Lexicons and their associated terminology, the operation of *Delimitation* is now defined over Phrases of fixed Word Length *n* in :ref:`Definition 1.2.7 <definition-1-2-7>`.
    
    .. _definition-1-2-7:
    
    **Definition 1.2.7: Delimitation**
    
    Let *p* be a Phrase from a Language **L**'s *n*:sup:`th` Lexicon,
    
    .. math::
    
        p = (\alpha_1, \alpha_2, ... , \alpha_n)
    
    The *Delimitation* of *p*, denoted :math:`D\Pi_{i=1}^{n} p(i)`, is defined recursively as:
    
        1. Empty Clause: :math:`D\Pi_{i=1}^{0} p(i) = \varepsilon`
        2. Basis Clause (:math:`n = 1`): :math:`D\Pi_{i=1}^{1} p(i) = \alpha_1`
        3. Recursive Clause (:math:`n > 1`): :math:`D\Pi_{i=1}^{n} p(i) = (D\Pi_{i=1}^{n-1} p(i))(\sigma)(\alpha_n)` 
    
    ∎
    
    .. _definition-1-2-8:
    
    **Definition 1.2.8: Limitation**
    
    Let *p* be a Phrase from a Language **L**'s *n*:sup:`th` Lexicon,
    
    .. math::
    
        p = (\alpha_1, \alpha_2, ..., \alpha_n)
    
    The *Limitation* of *p*, denoted :math:`L\Pi_{i=1}^{n} p(i)`, is defined recursively as:
    
        1. Empty Clause: :math:`L\Pi_{i=1}^{0} p(i) = \varepsilon`
        2. Basis Clause (:math:`n = 1`): :math:`L\Pi_{i=1}^{1} p(i) = \alpha_1`
        3. Recursive Clause (:math:`n > 1`): :math:`L\Pi_{i=1}^{n} p(i) = (L\Pi_{i=1}^{n-1} p(i)(\alpha_n)` 
    
    ∎
    
    The key difference between :ref:`Definition 1.2.7 <definition-1-2-7>` and :ref:`Definition 1.2.8 <definition-1-2-8>` is the presence of the Delimiter in the Recursive Clause. In other words, a Delimitation inserts a Delimiter between the Words it is concatenating, while a Limitation is simply a shorthand simply for concatenating a sequence of Words.
    
    Before proving the existence of Delimitations and Limitations, an example of how they are constructed recursively is given below.
    
    **Example**
    
    Let 
    
    .. math::
    
        1. \quad P_3 = (\text{"mother"}, \text{"may"}, \text{"I"})
    
    Apply :ref:`Definition 1.2.7 <definition-1-2-7>` to construct the Delimitation of **P**:sub:`3`. The Basis Step yields,
    
    .. math::
    
        2. \quad n = 1: D\Pi_{i=1}^{1} \alpha_i = \text{"mother"} 
    
    And then the Delimitation can be built up recursively using the Recursive Step repeatedly,
    
    .. math::
    
        3.  \quad n = 2: D\Pi_{i=1}^{2} \alpha_i = (D\Pi_{i=1}^{1} \alpha_i)(\sigma)(\text{"may"})= (\text{"mother"})(\sigma\text{"may"}) = \text{"mother"}\sigma\text{"may"}
        
    .. math::
    
        4.  \quad n = 3: D\Pi_{i=1}^{3} \alpha_i = (D\Pi_{i=1}^{2} \alpha_i)(\sigma)(\text{"I"}) = (\text{"mother"}\sigma\text{"may"})(\sigma\text{"I"}) = \text{"mother"}\sigma\text{"may"}\sigma\text{"I"}
    
    So the Delimitation of the Phrase is given by,
    
    .. math::
    
        4. \quad D\Pi_{i=1}^{3} \alpha_i = \text{"mother may I"} 
    
    Similarly, the Limitation can be constructed recursive from the same Basis Step using :ref:`Definition 1.2.8 <definition-1-2-8>`,
    
    .. math::
    
       5. \quad n = 2: L\Pi_{i=1}^{2} \alpha_i = (L\Pi_{i=1}^{1} \alpha_i)(\text{"may"})= (\text{"mother"})(\text{"may"}) = \text{"mothermay"}
       
    .. math::
    
       6. \quad n = 3: L\Pi_{i=1}^{3} \alpha_i = (L\Pi_{i=1}^{2} \alpha_i)(\text{"I"}) = (\text{"mothermay"})(\text{"I"}) = \text{"mothermayI"} 
    
    ∎
    
    From this example, it should be clear what the Delimitation and Limitation operations represent within the formal system. Delimitation is a method of constructing a Sentence-like (see Section II.III for the formal difference between a Delimitation and Sentence) String from a sequence of words, while a Limitation is shorthand for iterated concatenation over a sequence of Words.
    
    Note the previous example may be misleading in one important respect. A Delimitation is not necessarily "grammatical" or "meaningful". It may be a String of semantic Words without an accompanying interpretation on the Sentence level of the linguistic hierarchy. 
    
    However, as the next theorems shows, the result of a Delimitation or Limitation is unique.
    
    .. _theorem-1-2-8:
    
    **Theorem 1.2.8** :math:`\forall n \in \mathbb{N}: \forall p \in X_{L(n)}: \exists! s \in S: s = D\Pi_{i=1}^{n} p(i)`
    
    This theorem can be stated in natural language as follows: For every natural number n, and for every Phrase **P**:sub:`n` in the *n*:sup:`th` Lexicon of **L**, there exists a unique string *s* in **S** such that *s* is the Delimitation of **P**:sub:`n`.
    
    Let *n* be an arbitrary natural number, and let **P**:sub:`n` be a Phrase of Word Length *n* in Language **L** from the Language's *n*:sup:`th` Lexicon, :math:`X_L(n)`,
    
    .. math::
    
        1. \quad P_n = (\alpha_1, \alpha_2, ..., \alpha_n)
    
    The theorem will be proved using induction.
    
    **Base Case** :math:`n = 1`
    
    By :ref:`Definition 1.2.7 <definition-1-2-7>`,
        
    .. math::
    
        2. \quad D\Pi_{i=1}^{1} P_{n}(i) = \alpha_1
    
    Since *α*:sub:`1` is a word in **L** (by :ref:`Definition 1.2.6 <definition-1-2-6>` of Lexicon), it is also a String in S (by :ref:`Definition 1.2.2 <definition-1-2-2>`). Thus, there exists a String :math:`s = \alpha_1` such that 
    
    .. math::
        
        3. \quad s = D\Pi_{i=1}^{1} P_{n(i)}
    
    Since the base case of Delimitation is defined as simple equality, the string s must be unique.
    
    **Inductive Hypothesis**
    
    Assume that for some *k ≥ 1*, there exists a unique string *s*:sub:`k` such that 
    
    .. math::
    
        4. \quad s_k = D\Pi_{i=1}^{k} P_n(i)
    
    To complete the induction, it must be shown that there exists a unique string *s*:sub:`k+1` such that,
     
    .. math::
    
        5. \quad s_{k+1} = D\Pi_{i=1}^{k+1} P_n (i)
    
    By :ref:`Definition 1.2.7 <definition-1-2-7>`, 
    
    .. math::
    
        6. \quad D\Pi_{i=1}^{k+1} P_n(i) = (D\Pi_{i=1}^{k} P_n(i))(\sigma)(\alpha_{k+1})
    
    By inductive hypothesis,
    
    .. math::
    
        7. \quad D\Pi_{i=1}^{k} P_n(i) = s_k
        
    Thus, *s*:sub:`k` is unique. Since *α*:sub:`k+1` is a Word in **L** (by the definition of :math:`X_L (n+1)`), it is also a unique String in **S**.
    
    The concatenation of *s*:sub:`k`, *σ*, and *α*:sub:`k+1` is a unique string (by the :ref:`Definition 1.1.1 <definition-1-1-1>` of Concatenation and :ref:`Definition 1.1.4 <definition-1-1-4>` of String Equality).
    
    Therefore, :math:`s_{k+1} = (s-k)(\sigma)(\alpha_{k+1})` is a unique string.
    
    By induction, for every natural number *n*, and for every phrase **P**:sub:`n` in :math:`X_L (n)`, there exists a unique string *s* in **S** such that
    
    .. math::
    
        8. \quad s = D\Pi_{i=1}^{n} P_n (i) 
       
    ∎
    
    .. _theorem-1-2-9:
    
    **Theorem 1.2.9** :math:`\forall n \in \mathbb{N}: \forall p \in X_L(n): \exists! s \in S: s = L\Pi_{i=1}^{n} p(i)`
    
    The proof of this theorem is almost exactly identical to :ref:`Theorem 1.2.8 <theorem-1-2-8>`, with the exception there is no Delimiter in step 6. ∎
    
    .. _section-i-iii:
    
    Section I.III: Word Classes 
    ---------------------------
    
    It will be necessary to define special classes of Words in a Language to properly describe the Language's palindromic structure. These classes, especially the class of Invertible Words, will be used extensively in the next sections. Reflective Words, however, will play a crucial role in this work's climatic theorem. 
    
    .. _reflective-words:
    
    Reflective Words 
    ^^^^^^^^^^^^^^^^
    
    The concept of *Reflective Words* can be easily understood by examining some examples in English,
    
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
    
    From this list, it should be clear what is meant by the notion of *reflective*. Reflective Words are those Words whose meaning is unchanged by a String Inversion. However, the semantic content that is preserved under inversion is not the primitive property that primarily explains this invariance. The invariance of the semantic content under inversion is the result of Character level symmetries. 
    
    Rather than attempt to define Reflective Words as the class of Words that are their own Inverses, a different approach will be taken that highlights the Character level symmetries that exist in these class of Words. It will then be proven the class of Words which satisfy this definition are exactly those Words that are their own Inverses.
    
    .. _definition-1-3-1:
    
    **Definition 1.3.1: Reflective Words** 
    
    The set of Reflective Words **R** is defined as the set of *α* which satisfy the open formula,
    
    .. math::
    
        \alpha \in R \leftrightarrow \forall i \in \mathbb{N}_{l(\alpha)}: \alpha[i] = \alpha[l(\alpha) - i + 1]
    
    ∎
    
    A Word *α* will be referred to as *reflective* if it belongs to the class of Reflective Words. 
    
    The following theorem is an immediate consequence of :ref:`Definition 1.3.1 <definition-1-3-1>` and :ref:`Definition 1.2.4 <definition-1-2-4>`.
    
    .. _theorem-1-3-1:
    
    **Theorem 1.3.1** :math:`\forall \alpha \in L: \alpha \in R \leftrightarrow \alpha = \text{inv}(\alpha)`
    
    In natural language, this theorem can be stated as: A Word in a Language is Reflective if and only if it is its own Inverse.
    
    (→)  Assume :math:`\alpha \in R`. By :ref:`Definition 1.3.1 <definition-1-3-1>`, 
    
    .. math::
    
        1. \quad \forall i \in N_{l(\alpha)}:  \alpha[i] = \alpha[l(\alpha) - i + 1] 
    
    Let :math:`\beta = \text{inv}(\alpha)`. By the :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        2. \quad l(\beta) = l(\alpha)
        
    .. math::
    
        3. \quad \forall i \in N_{l(α)}: ( \beta[i] = \alpha[l(\alpha) - i + 1] )
    
    Substituting the property of Reflective Words from step 1 into step 3,
    
    .. math::
    
        4. \quad \forall i \in N_{l(\alpha)}: \beta[i] = \alpha[i]
    
    Since :math:`\beta[i] = \alpha[i]` for all :math:`i \in N_{l(\alpha)}`, and both strings have the same length, by :ref:`Definition 1.1.4 <definition-1-1-4>`, it can be concluded that :math:`\alpha = \beta`. Therefore the desired result is obtained, :math:`\alpha = \beta = \text{inv}(\alpha)`.
    
    (←) Assume :math:`\alpha = \text{inv}(\alpha)`.  By :ref:`Definition 1.2.4 <definition-1-2-4>` of String Inversion,
    
    .. math::
    
        1. \quad l(\alpha) = l(\text{inv}(\alpha))
        
    .. math::
    
        2. \quad \forall i \in N_{l(\alpha)}: \alpha[i] = \alpha[l(\alpha) - i + 1]
    
    But step 2 is exactly the definition of Reflective Words, so by :ref:`Definition 1.3.1 <definition-1-3-1>`, :math:`\alpha \in R` ∎ 
    
    .. _invertible-words:
    
    Invertible Words 
    ^^^^^^^^^^^^^^^^
    
    As discussed previously, the concept of *invertible* is exemplified in pairs of English words, such as *"parts"* and *"strap"*, or *"repaid"* and *"diaper"*. If a Word can be inverted, this is not simply a syntactic operation, but a semantic one as well. An *Invertible Word* is a Word whose inverse is part of the same Language **L** as the original Word. This notion can now be made more precise with the terminology introduced in prior sections.
    
    .. _definition-1-3-2:
    
    **Definition 1.3.2: Invertible Words** 
    
    Let *α* be any Word in a Language **L**. Then the set of Invertible Words **I** is defined as the set of *α* which satisfy the open formula,
    
    .. math::
        
        \alpha \in I \leftrightarrow \text{inv}(\alpha) \in L
        
    ∎
    
    A Word *α* will be referred to as *invertible* if it belongs to the class of Invertible Words.
    
    :ref:`Definition 1.3.2 <definition-1-3-2>` is immediately employed to derive the following theorems.
    
    .. _theorem-1-3-2:
    
    **Theorem 1.3.2** :math:`\forall \alpha \in L: \alpha \in I \leftrightarrow \text{inv}(\alpha) \in I`
    
    (→) Assume :math:`\alpha \in I`. By :ref:`Definition 1.3.2 <definition-1-3-2>`,
    
    .. math::
    
        1. \quad \text{inv}(α) \in L
        
    Consider *inv(α)*. To show that it's invertible, it must be shown,
    
    .. math::
    
        2. \quad \text{inv}(\text{inv}(\alpha)) \in L. 
    
    By :ref:`Theorem 1.2.4 <theorem-1-2-4>`,
    
    .. math::
    
        3. \quad \text{inv}(\text{inv}(\alpha)) = \alpha
        
    Since it is known :math:`\alpha \in L`, it follows,
    
    .. math::
    
        4. \quad \text{inv}(\text{inv}(\alpha)) \in L  
        
    By the :ref:`Definition 1.3.2 <definition-1-3-2>`, 
    
    .. math::
    
        5. \quad \text{inv}(\alpha) \in I
        
    Therefore, *inv(α)* is also an Invertible Word. 
    
    (←) Assume *inv(α)* is a Word in Language L and :math:`inv(\alpha) \in I`. Then by :ref:`Definition 1.3.2 <definition-1-3-2>`,
    
    .. math::
    
        1. \quad \text{inv}(\text{inv}(\alpha)) \in L
    
    By :ref:`Theorem 1.2.4 <theorem-1-2-4>`,
    
    .. math::
    
        2. \quad \alpha \in L
    
    To show *α* is invertible, it must be shown :math:`\text{inv}(\alpha) \in L`, but this is exactly what has been assumed, so it follows immediately. 
    
    Therefore, putting both directions of the equivalence together and generalizing over all Words in a Language, 
    
    .. math::
    
        3. \quad \forall \alpha \in L: \alpha \in I ↔ \text{inv}(\alpha) \in I 
        
    ∎ 
    
    .. _theorem-1-3-3:
    
    **Theorem 1.3.3** :math:`R \subseteq I`
    
    Assume :math:`α \in R`. By :ref:`Definition 1.3.2 <definition-1-3-2>`,
    
    .. math::
    
        1. \quad \forall i \in N_{l(\alpha)}: \alpha[i] = \alpha[l(\alpha) - i + 1]
    
    Let :math:`\beta = inv(\alpha)`. By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        2. \quad l(\beta) = l(\alpha)
        
    .. math::
    
        3. \quad \forall j \in N_{l(\alpha)}: \beta[j] = \alpha[l(\alpha) - j + 1]
    
    Substituting step 1 into step 3,
    
    .. math::
    
        4. \quad \forall i \in N_{l(\alpha)}:  \beta[j] = \alpha[j]
    
    Since both strings have the same length and the same Characters in the same order, by :ref:`Definition 1.1.4 <definition-1-1-4>`, 
    
    .. math::
    
        5. \quad \alpha = \beta = \text{inv}(\alpha)
    
    By assumption, *α* is a Word from Language **L** that belongs to **R**. From step 5, this implies *inv(α)* is also part of the Language **L**. By :ref:`Definition 1.3.2 <definition-1-3-2>`, this implies,
    
    .. math::
    
        6. \quad \alpha \in I 
    
    In other words, 
    
    .. math::
    
        7. \quad \forall \alpha \in L: \alpha \in R \to \alpha \in I 
    
    But this is exactly the definition of the subset relation in set theory. Therefore,
    
    .. math::
    
        8. \quad R \subseteq I 
        
    ∎ 
    
    In the context of (potentially) infinite sets such as **L** and **S**, *"even"* and *"odd"* refer to whether the set can be partitioned into two disjoint subsets of equal cardinality.
    
        1. Even Cardinality: An infinite set has even cardinality if it can be put into a one-to-one correspondence with itself, with each element paired with a distinct element.
        2. Odd Cardinality: An infinite set has odd cardinality if, after pairing each element with a distinct element, there is one element left over.
    
    The set of non-reflective Invertible Words, **I** - **R** (where "-" represents the operation of set differencing), always has even cardinality because each word can be paired with its distinct inverse. The overall cardinality of **I** then depends on whether the set of Reflective Words, **R**, adds an "odd" element or not. This idea is captured in the next theorem.
    
    .. _theorem-1-3-4:
    
    **Theorem 1.3.4** If :math:`\lvert R \rvert` is even, then :math:`\lvert I \rvert` is even. If :math:`\lvert R \rvert` is odd, then :math:`\lvert I \rvert` is odd.
    
    Partition the set of Invertible Words, **I**, into two disjoint subsets,
    
        1. **R**: The set of Reflective Words.
        2. **I** - **R**: The set of Invertible Words that are not Reflective.
    
    For every word *α* in :math:`I - R`, its inverse, *inv(α)*, is also in :math:`I - R`. Furthermore, they form a distinct pair :math:`(\alpha, \text{inv}(\alpha))`. This is because *α* is invertible but not reflective, so :math:`α \neq \text{inv}(\alpha)`.
    
    Since the elements of v can be grouped into distinct pairs, the cardinality :math:`\lvert I - R \rvert` must be even.
    
    The total number of Invertible Words is the sum of the number of Reflective Words and the number of Invertible Words that are not Reflective,
    
    .. math::
    
        3. \quad \lvert I \rvert = \lvert R \rvert + \lvert I - R \lvert
    
    Let :math:`\lvert R \rvert` be even. Since :math:`\lvert I - R \rvert` is always even, and the sum of two even numbers is even, :math:`\lvert I \rvert` must also be even.
    
    Let :math:`\lvert R \rvert` be odd. Since :math:`\lvert I - R \rvert` is always even, and the sum of an odd number and an even number is odd, :math:`\lvert I \rvert` must also be odd. ∎ 

.. _03corpora:
 
--------------
03_corpora.rst
--------------

.. raw:: 

    .. _section-ii:
    
    Section II: Corpora
    ===================
    
    The work so far has formally constructed a system for representing the first two levels of artifacts from a natural language, Characters (Alphabet) and Words (Language), without appealing to their interpretation in any way except insofar that it takes a stance on the *existence* of an interpretation. As the analysis moves up the chain of linguistic artifacts to the next highest level, Sentences (Corpus), it is tempting to start incorporating semantic features into the theory. However, the objective is to derive palindromic conditions independent of a particular semantic interpretation. Therefore, as the analysis proceeds, special care will be given to the definition of a *Sentence* and its *Corpus*.
    
    .. _section-ii-i:
    
    Section II.I: Definitions
    -------------------------
    
    The next level of the semantic hierarchy will now be constructed. Many of the definitions made in this subsection will not be referenced until the final section of this work, when the fundamental properties of Palindromes are established. They are given here, due to the natural progression of concept formation dictating they be defined after the notion of Sentence and Corpus is introduced.
    
    .. _corpus:
    
    Corpus
    ^^^^^^
    
    The entire system so far constructed relies on the domain of **S**, the set of all Strings that can be formed from an Alphabet of Characters :math:`\Sigma`. Attention has been confined to those entities that satisfy the :ref:`Discovery Axiom W.1 <axiom-w1>`.
    
    In other words, the definitions and theorems so far introduced deal with linguistics entities that do not possess a Delimiter Character. Delimiters will be of central importance in describing palindromic structures, because Delimiters play a central role in the definition of the linguistic entity that will ultimately allow a palindrome to be rigorously defined, a *Sentence*. With that in mind, the concepts and definitions that pave the way to an explication of *Sentence* start with the definition of a *Corpus*.
    
    .. _definition-2-1-1:
    
    **Definition 2.1.1: Corpus** The Corpus of Language **L** is denoted by **C**:sub:`L`. The Corpus set represents a collection of grammatically valid and semantically meaningful Strings. ∎
    
    From the definition, it can easily be seen the Corpus of a Language is a subset of the set of all possible Strings, **S**
    
    .. math::
    
       C_L \subset S 
    
    This aligns with the idea that the domain of entities in this formal system is defined either as a type of *element* of **S** or a type of *subset* of **S**.
    
    .. _sentence:
    
    Sentence
    ^^^^^^^^
    
    Before proceeding with the definition of Sentences, some notation is introduced,
    
        1. Sentences (*ᚠ*, *ᚢ*, *ᚦ*, ... ): Anglo-Saxon (*Old English*) Runes represent a Sentence. Subscripts will occassionally be used in conjunction with Anglo-Saxon letters to denote Sentences, (*ᚠ*:sub:`1`, *ᚠ*:sub:`2`, ... ). 
        2. Sentential Variables (*ζ*, *ξ*): The lowercase Greek letter Zeta and Xi are reserved for indeterminate Sentences, i.e. Sentential Variables. Subscripts will occassionally be used in conjunction with Zeta to denote Sentential Variables, (*ζ*:sub:`1`, *ζ*:sub:`2`, ...)
    
    .. _definition-2-1-2:
    
    **Definition 2.1.2: Sentence** A Sentence in Language **L** is an element of its Corpus. ∎
    
    .. math::
    
        ᚠ \in C_L
    
    From :ref:`Definition 2.1.1 <definition-2-1-1>` and :ref:`Definition 2.1.2 <definition-2-1-2>`, it follows that a Sentence is a String,
    
    .. math::
    
        ᚠ \in S
    
    It should be stressed, as had been made clear in previous comments, that Characters, Words and Sentences in the current formulation are elements of the same underlying set, the set of all Strings. This connection in the domain of Characters, Words and Sentences is what will allow the analysis to begin to construct the outline of palindromic structures in a Language and Corpus. To reiterate this hierarchy and precisely state how all the entities in this formal system are related,
    
        1. Strings: ι, α, ζ
        2. Sets: Σ, L, :math:`C_L`
        3. Character Membership: :math:`\iota \in \Sigma`
        4. Word Membership: :math:`\alpha \in L`
        5. Sentence Membership: :math:`\zeta \in C_L`
    
    To clarify the relationship between Strings, Characters, Alphabets, Words, Languages, Sentences and Corpus in plain language,
    
        1. All Characters, Words and Sentences are Strings.
        2. All Alphabets, Languages and Corpuses are sets of Strings.
        3. All Characters belong to an Alphabet.
        4. All Words belong to a Language.
        5. All Sentences belong to a Corpus.
    
    This web of categorical relations represents the hierarchy of linguistic entities within the formal system. 
    
    .. graphviz:: ../_static/dot/hierarchy.dot
        :caption: A diagram of the semantic hierarchy
        :alt: Semantic Hierarchy Diagram
    
    .. _sentence-notation:
    
    Notation
    ^^^^^^^^
    
    In :ref:`Section I.I <section-i-i>`, notation was introduced for representing Strings a a sets of ordered Characters. This form of representation provided a formal method for specifying various syntactical conditions and properties of Strings and Words. In particular, this method allowed a formal definition of String Length.  
    
    In a similar way, a method of representing Sentences as sets will now be constructed to enrich the symbolic form given to a Sentence in this formal system. Since all Sentences are Strings, all Sentences have Character-level set or sequence representations, by the Emptying Algorithm. The Discovery Axiom W.1 allows the definition of an algorithm to parse the Words of a Sentence based purely on the presence of Delimiters. 
    
    .. _definition-2-1-3:
    
    **Definition 2.1.3: Word-Level Set Representation**
    
    Let *ζ* be a Sentence in a Corpus :math:`C_L`. Let **Ζ** be the Character-level set representation of *ζ*, i.e. an ordered sequence of Characters from the Alphabet **Σ**. 
    
    The Word-level set representation of *ζ*, denoted by :math:`W_{\zeta}`, is defined as the ordered set of words obtained by splitting **Ζ**  at each Delimiter Character, *σ*. Formally, :math:`W_{\zeta}` is constructed using the :ref:`Delimiting Algorithm <algorithm-2>`.
    
    .. _algorithm-2:
    
    **Algorithm 2: Delimiting Algorithm**
    
    Consider a particular Sentence in the Corpus, *ᚠ*. The :ref:`Delimiting Algorithm <algorithm-2>` consists of initializing the values of several local variables and then iterating over the Character level set representation of a Sentence *ᚠ* until the Characters have been exhausted. The exact details are given below.
    
    The :ref:`Delimiting Algorithm <algorithm-2>` takes a Sentence *ᚠ* from a Corpus as input, and applies the Emptying Algorithm to it to generate a sequence of non-Empty Characters. It then initializes a set **W**:sub:`ᚠ` and index for the Words it will add to **W**:sub:`ᚠ` . The algorithm iterates the index and constructs the Word-level representation by removing the Delimiter character. The :ref:`Delimiting Algorithm <algorithm-2>` is formally defined below.
    
    .. topic:: Algorithm Delimit(t: String)
        
        # Input: A string t
        # Output: An ordered set W representing the Word-level set representation of t
    
        # Initialization
        ## Character-level representation of ᚠ
    
        1. ᚠ ← Empty(ᚠ)
       
        ## Initialize empty set to hold Word-level representation of ᚠ
    
        2. W ← ∅
        
        ## Initialize a counter j for Words
    
        3. j ← 1
        
        ## Initialize a counter i for characters
    
        4. i ← 1
        
        ## Initialize an empty string
    
        5. t ← ε
    
        # Iteration
    
        6. While i ≤ l(ᚠ):
       
            a. If ᚠ[i] ≠ σ:
    
                i. t ← (t)(ᚠ[i])
    
            b. Else:
    
                i. If l(t) > 0:
    
                    1. Apply Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>` to t.
                    2. W ← W ∪ { (j, t) }
                    3. j ← j + 1
       
                ii. t ← ε
    
            c. i ← i + 1
    
        # Finalization
    
        7. If l(t) > 0:
        
            a. W ← W ∪ { (j, t) }
            b. j ← j+1
        
        8. Return W ∎
    
    .. graphviz:: ../_static/dot/delimiting.dot
        :caption: A diagram of the :ref:`Delimiting Algorithm <algorithm-2>`
        :alt: :ref:`Delimiting Algorithm <algorithm-2>` Diagram
    
    Note the String which is initialized to hold the Sentence Characters in step *5* is set to an initial value of the Empty Character in the Initialization Block. Also note, the application of the Basis Clause in step *1.b.i.1* ensures this Empty Character is removed after each Word has been processed. This is required, because otherwise the last Word in the Word-level representation will have an Empty Character, which violates the results of :ref:`Theorem 1.2.3 <theorem-1-2-3>`.
    
    The essence of the :ref:`Delimiting Algorithm <algorithm-2>` lies in the interplay of the :ref:`Discovery Axiom W.1 <axiom-w1>` and :ref:`Definition 2.1.2 <definition-2-1-2>` of a Sentence as a semantic String. :ref:`Definition 2.1.2 <definition-2-1-2>`, like :ref:`Definition 1.2.2 <definition-1-2-2>`, ensures all Sentences and Words are semantic. The only feature that differentiates Sentence and Words in their *"semanticality"* is the presence of a Delimiter (from a syntactical perspective, at any rate). Therefore, by the :ref:`Discovery Axiom W.1 <axiom-w1>`, the Words which a Sentence contains must be exactly those Strings which are separated by a Delimiter Character. 
    
    This formulation has the advantage of not taking a stance on the semantics of a particular language. It allows for the discovery of Words in a Language through the simple boundary of Delimiters within the Sentences of its Corpus. 
    
    The following examples show how to apply the :ref:`Delimiting Algorithm <algorithm-2>` to construct the Word-level representation of a Sentence. 
    
    **Example**
    
    Let *ᚠ = (𝔞𝔟)(σ)(ε)(σ)(𝔟𝔞)*. Note *l(ᚠ) = 6*.
    
    **Initialization**
    
    During initialization, the Character-level set representation of *ᚠ* is constructed with :ref:`Definition 1.1.2 <definition-1-1-2>` using the Emptying Algorithm, which strips it of its Empty Characters,
    
    .. math::
    
       1. \quad {ᚠ} = (\mathfrak{a},\mathfrak{b},\sigma,\sigma,\mathfrak{b},\mathfrak{a})
       
    .. math::
    
       2. \quad W_{ᚠ} = \emptyset
       
    .. math::
    
       3. \quad j = 1
    
    **Iteration**
    
    The following list shows the result of the algorithm after each iteration,
    
    .. math::
    
       1. \quad j = 2, i = 4, t = \mathfrak{ab}, W_{ᚠ} = \{ (1, \mathfrak{ab}) \}
    
    .. math::
    
       2. \quad j = 2, i = 5, t = \sigma, W_{ᚠ} = \{ (1, \mathfrak{ab}) \}
       
    .. math::
    
       3. j\quad  = 3, i = 7, t = \mathfrak{ba}, W_{ᚠ} = \{ (1, \mathfrak{ab}), (2, \mathfrak{ba}) \}
    
    At which point :math:`i > l(ᚠ)`, so the algorithm halts and returns,
    
    .. math::
    
        4. \quad W_{ᚠ} = \{ (1, \mathfrak{ab}), (2, \mathfrak{ba}) \} 
        
    ∎
    
    **Example** 
    
    Let *ᚠ = "the cat meows"*. Then the Character level representation of *ᚠ* is given by, 
    
    .. math::
    
        1. \quad {\largeᚠ} = \{ (1, \text{"t"}), (2, \text{"h"}), (3,\text{"e"}), (4,\sigma), (5,\text{"c"}), (6,\text{"a"}), (7,\text{"t"}), (8,\sigma), (9,\text{"m"}), (10,\text{"e"}), (12,\text{"o"}), (13,\text{"w"}), (14,\text{"s"}) \}
    
    Then, applying the :ref:`Delimiting Algorithm <algorithm-2>`, its Word-level representation is constructed, 
    
    .. math::
    
        2. \quad W_{ᚠ} = \{ (1, \text{"the"}), (2, \text{"cat"}), (3, \text{"meows"}) \} 
        
    ∎
    
    Similar to the Character-level set representation of String, where the Character position is encoded into the first coordinate, the Word-level set representation of a String encodes the presence of Delimiters through its first coordinate. Once Word Length is defined in the next section, a notational shortcut similar to Character Index Notation defined in :ref:`Definition 1.1.5 <definition-1-1-5>` will use this method of Sentence representation to simplify many of the upcoming proofs.
    
    There is a subtle assumption being made in the idea a Sentence can be reduced to a sequence of ordered Words that deserves special mention, as this perhaps reasonable assumption implicitly elides a question of much greater complexity regarding where precisely the semantic information of a Sentence resides. To see what is meant by this, consider the three sentences from Latin,
    
    - Puella canem videt. (Girl dog sees)
    - Canem puella videt. (Dog girl sees)
    - Videt puella canem. (Sees girl dog)
    
    Latin, like many other natural languages, uses declensions to imbue words with syntactic functions. In some respect, all three of these sentences could be considered the *same* sentence, as the order of the words is not the primary bearer of semantic information; the suffixes do all of the work. While the order of words lends itself to the *voice* and *tone* of the sentence, the meaning of the sentence does not primarily emerge through its Word order. Similar cases exist in any natural language that uses declensions to modify the syntactic function of words, such as Greek. 
    
    The current formal system treats these sentences in Latin as distinct Sentences. If the Latin sentences in this example are to be identified as representatives of the same semantic *"token"*, this cannot occur on the Sentence level of this formal system's linguistic hierarchy. This example suggests Sentences are not the final level of the hierarchy, and that to find the source of meaning in a Sentence, another level must be constructed on top of it capable of identifying these different manifestations as the same *"token"*.
    
    This example does not invalidate the analysis, but it does introduce subtlety that must be appreciated. These concerns must be kept in mind while the formal notion of a Sentence is developed.
    
    .. _word-length:
    
    Word Length
    ^^^^^^^^^^^
    
    The notion of String Length *l(s)* was introduced in :ref:`Section I.I <section-i-i>` as a way of measuring the number of non-Empty Characters in a String *s*. In order to describe palindromic structures, a new notion of length will need introduced to accomodate a different *"spatial"* dimension in the domain of a Language and its Corpus: *Word Length*.
    
    Intuitively, the length of a Sentence is the number of Words it contains. Since there is no analogue of :ref:`Discovery Axiom W.1 <axiom-w1>` for Sentences (nor should there be), this means Sentences may contain Delimiter Characters. The Words of a Language are separated by Delimiters in the Sentences of its Corpus. 
    
    :ref:`Definition 2.1.3 <definition-2-1-3>` provides a way of dispensing with the Delimiter Character in Sentences, while still retaining the information they provides about the demarcation of Words through the first coordinate of a Sentence's Word-level representation. With the Word-level set representation of Sentence in hand, it is a simple matter to define the notion of Word Length in the formal system.
    
    .. _definition-2-1-4:
    
    **Definition 2.1.4: Word Length**
    
    Let *ζ* be a Sentence in a **C**:sub:`L`. Let :math:`W_{\zeta}` be the Word-level set representation of *ζ*, as defined in :ref:`Definition 2.1.3 <definition-2-1-3>`. The Word Length of the Sentence *ζ*, denoted by :math:`\Lambda(\zeta)`, is defined as the cardinality of the set :math:`W_{\zeta}`,
    
    .. math::
    
        \Lambda(\zeta) = | W_{\zeta} | 
        
    ∎
    
    **Example**
    
    Consider the Sentence *ᚠ = "the dog runs"*. Its Character-level set representation would be given by,
    
    .. math::
    
        1. \quad \largeᚠ = \{ (0,\text{"t"}), (1,\text{"h"}), (2,\text{"e"}), (4,\sigma), (5, \text{"d"}), (6, \text{"o"}), (7, \text{"g"}), (8, \sigma), (9, \text{"r"}), (10, \text{"u"}), (11,\text{"n"}), (12,\text{"s"}) \}
    
    Its Word-level set representation would be given by,
    
    .. math::
    
        2. \quad W_{ᚠ} = \{ (1, \text{"the"}), (2, \text{"dog"}), (3, \text{"runs"}) \}
    
    Therefore, the length of the sentence is:
    
    .. math::
    
        3. \quad \Lambda(ᚠ) = | W_{ᚠ} | = 3
    
    Note, in this example, 
    
    .. math::
    
        4. \quad l(ᚠ) = 12 
        
    ∎
    
    This example demonstrates the essential difference in the notions of length that have been introduced. It is worthwhile to clarify the distinction between these two conceptions. 
    
    Let *t* be a String with Character-level representation **T** and Word-level representation **W**:sub:`t`. The hierarchy of its "spatial" dimensions is given below, in order of greatest to least (this fact is proven in :ref:`Section III.II <section-iii-ii>` with :ref:`Theorem 3.2.8 <theorem-3-2-8>` ). Terminology is introduced in parenthesis to distinguish these notions of length,
    
       - l(t) (String Length): The number of non-Empty Characters contained in a String.
       - Λ(t) (Word Length): The number of Words contained in a String 
    
    Note the first level is purely syntactical. Any String *t* will have a String Length *l(t)*. However, not every String possesses Word Length, *Λ(s)*. Word Length contains semantic information. While the presence of Word Length does not necessarily mean the String is semantically coherent (see :ref:`Definition 2.2.1 <definition-2-2-1>` for a precise definition of *semantic coherence*), e.g. "asdf dog fdsa", Word Length does signal an *extension* of Strings into the semantic domain.
    
    Word Length can be used to simplify some of the complex notation the formal system has accumulated. Similar to the Character Index Notation, a way of referring to Words in Sentences within propositions without excessive quantification is now introduced through Word Index notation.
    
    .. _definition-2-1-5:
    
    **Definition 2.1.5: Word Index Notation**
    
    Let *ζ* be a Sentence with Word level set representation, :math:`W_{\zeta}`,
    
    .. math::
    
        W_{\zeta} = (\alpha_1, \alpha_r, ... , \alpha_{\Lambda(\zeta)})
    
    Then for any *j* such that :math:`1 \leq j \leq \Lambda(\zeta)`, the Word at index *j*, denoted *ζ{j}*, is defined as the Word which satisfies the following formula,
    
    .. math::
    
        \forall (j, \alpha_j) \in W_{\zeta}: \zeta\{j\} = \alpha_j
        
    ∎
    
    The following theorem uses this notation to proves an intuitive concept: the total number of Characters in all of the Words in a Sentence must exceed the number of Words in a Sentence (since there are no Words with a negative amount of Characters). 
    
    .. _theorem-2-1-1:
    
    **Theorem 2.1.1** :math:`\forall \zeta \in C_{L}:  \sum_{j=1}^{\Lambda(\zeta)} l(\zeta\{j\}) \geq \Lambda(\zeta)`
    
    This theorem can be stated in natural language as follows: For any sentence *ζ* in Corpus **C**:sub:`L`, the sum of the String Lengths of the Words in *ζ* is always greater than the Word Length of *ζ*.
    
    Assume :math:`\zeta \in C_L`. Let *j* be a natural number such that :math:`1 ≤ j ≤ \Lambda(\zeta)`
    
    For each ordered Word *ζ{j}* in *ζ*, its String Length *l(ζ{j})* must be greater 0 by the :ref:`Discovery Axiom W.1 <axiom-w1>` and :ref:`Definition 1.1.3 <definition-1-1-3>`. Therefore, since each Word contributes at least a String Length of 1, the sum of the String Lengths *l(ζ{j})* must be greater than or equal to *Λ(ζ)*. ∎
    
    Word Length and Word Index Notation can be used to define the notion of *Boundary Words*, which will be utilized in the main results about Palindromes. 
    
    To illustrate another simplification effected by Index notation in formal proofs about Language, consider how laborious the proof of the following :ref:`Theorem 2.1.2 <theorem-2-1-1>` would be without the ability to refer to Characters embedded in Strings and Words embedded in Sentences through Index notation. 
    
    .. _theorem-2-1-2:
    
    **Theorem 2.1.2** :math:`\forall \zeta, \xi \in C_{L}: \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)`
    
    Let *ζ* and *ξ* be arbitrary Sentences in **C**:sub:`L`. Let :math:`W_{\zeta}` and **W**:sub:`ξ` be the Word-level representations of *ζ* and *ξ*, respectively. By Definition 2.1.4, 
    
    .. math::
    
        1. \quad \Lambda(\zeta) = | W_{\zeta} |
    
    .. math::
    
        2. \quad \Lambda(\zeta) = | W_{\xi} |
    
    Let *ζξ* be the concatenation of *ζ* and *ξ*. When *ζ* is concatenated to *ξ*, there are several possible cases to consider. 
    
       - ζ[l(ζ)] = σ, ξ[1] = σ
       - ζ[l(ζ)] = σ, ξ[1] ≠ σ
       - ζ[l(ζ)] ≠ σ, ξ[1] = σ
       - ζ[l(ζ)] ≠ σ, ξ[1] ≠ σ
    
    **Case 1 - 3**: In each of theses cases, the Words of *ζ* and the Words of *ξ* are still separated by at least one Delimiter. Therefore, no new Word is formed during concatenation, and the words in *ζξ* are simply the words of *ζ* followed by the words of *ξ*. Therefore, 
    
    .. math::
    
        3. \quad \Lambda(\zeta\xi) = \Lambda(\zeta) + \Lambda(\xi).
    
    **Case 4**: :math:`\zeta[l(\zeta)] \neq \sigma, \xi[1] \neq \sigma` 
    
    In this case, a new Word may be formed during concatenation, but only if *ζ{Λ(ζ)}* concatenated with *ξ{1}* belongs to L (i.e., *(ζ{Λ(ζ)})(ξ{1})* if it is a compound Word). Let *t* be the String such,
    
    .. math::
    
        4. \quad t = (\zeta\{\Lambda(\zeta)\})(\xi\{1\})
    
    This result can be expressed,
    
    .. math::
    
        5. \quad t \in L \to \Lambda(\zeta\xi) = \Lambda(\zeta) + \Lambda(\xi) - 1.
        
    .. math::
    
        6. \quad t \notin L \to \Lambda(\zeta\xi) = \Lambda(\zeta) + \Lambda(\xi).
    
    In all cases, 
    
    .. math::
    
        7. \quad \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi).
    
    Since *ζ* and *ξ* were arbitrary sentences, this can be generalized over the Corpus,
    
    .. math::
    
        8. \quad \forall \zeta, \xi \in C_L: \Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi) 
        
    ∎
    
    Word Length is fundamentally different to String Length with respect to the operation of concatenation. In :ref:`Theorem 1.1.1 <theorem-1-1-1>`, it was shown String Length sums over concatenation. :ref:`Theorem 2.1.2 <theorem-2-1-2>` demonstrates the corresponding property is not necessarily true for Word Length. This is an artifact of the ability of concatenation to destroy semantic content.
    
    .. _intervention:
    
    Intervention
    ^^^^^^^^^^^^
    
    Colloquially, in the Sentence, *"never a dull day"*, the ordered Characters *"a"*,*"d"*,*"u"*, *"l"*, *"l"* are between the Words *"never"* and *"day"*. The concept of *Intervention* is introduced into the formal system to explicate this everyday notion of *"betweenness"*. A precise definition of what it means for a Character to *intervene* two Words in a Sentence is given using the operation of Delimitation introduced in :ref:`Definition 1.2.7 <definition-1-2-7>`.
    
    .. _definition-2-1-6:
    
    **Definition 2.1.6: Intervention**
    
    Let *ζ* be a Sentence in :math:`C_L` . The Character *ζ[k]* is said to *intervene* the Words *ζ{i}* and *ζ{j}*, denoted as *(i/k/j)*:sub:`ζ`, if the following condition holdS
    
    .. math::
    
       l(D\Pi_{x=1}^{i} \zeta(x)) < k < l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1 
       
    ∎
    
    The meaning of :ref:`Definition 2.1.6 <definition-2-1-6>` is not immediately intuitive, so a an explanation and thorough example are now presented to show how the definition corresponds to the common-sense notion of a Character falling between two Words in a Sentence.
    
    Analyzing each component of the inequality in :ref:`Definition 2.1.6 <definition-2-1-6>`: 
    
    - :math:`l(D\Pi_{x=1}^{i} \zeta(x))`: This represents the length of the Delimitation of the first i words of the sentence ζ. In simpler terms, it's the length of the string up to and including the i-th word, including the delimiters.
    
    - k: This is the index of the character in question, ζ[k].
      
    - :math:`l(\zeta) - l(D\Pi_{x=1}^{Λ(ζ) - j + 1} \text{inv}(ζ)(x)) + 1`: This is the most complex component for the formula, so it deserves a finer analysis,
        
        1. :math:`\Lambda(\zeta) - j + 1`: This calculates the index of the word in the reversed sentence that corresponds to the j:sup:`th` word in the original sentence.
       
        2. :math:`D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)`: This is the Delimitation of the first :math:`(\Lambda(\zeta) - j + 1)` Words of the Inverse of the Sentence *ζ*. This will correspond to the beginning portion of the reversed Sentence up to the Word that corresponds to the j:sup:`th` Word in the original Sentence.
       
        3. :math:`l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x))`: This is the length of the initial portion of the reversed Sentence.
       
        4. :math:`l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x))`: This subtracts the length of the initial portion of the reversed sentence from the total length of the original sentence. This gives us the length of the remaining portion of the original sentence, starting from the character after the word corresponding to j in the original sentence.
       
        5. :math:`l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1`: Finally, add 1 to get the index of the first Character after the word corresponding to j in the original sentence.
    
    To aid in the comprehension of the concept being captured with Definition 2.1.6, the following example shows how to calculate an Intervention.
    
    **Example** 
    
    Let *ᚠ = "repaid a regal leper"*. Note the String and Word Lengths are given by,
    
    .. math::
    
        1. \quad l(ᚠ) = 20
        
    .. math::
    
        2. \quad \Lambda(ᚠ) = 4
        
    The Word-level representation of this Sentence is given by,
    
    .. math::
    
        3. \quad W_{ᚠ} = \{ (1, \text{"repaid"}), (2, \text{"a"}), (3, \text{"regal"}), (4, \text{"leper"}) \}
    
    Note :math:`\text{inv}(ᚠ) = \text{"repel lager a diaper"}`. This is an example of an Invertible Sentence that maintains *semantic coherence* (i.e. all of its inverted Words are Words in the Language; see :ref:`Definition 2.2.1 <definition-2-2-1>` in the next subsection for a more formal definition of *semantic coherence*), but lacks *admissibility* (i.e. it is not a grammatical or syntactical sentence; see :ref:`Definition 2.3.1 <definition-2-3-1>` for a formal definition of *admissibility*.) The Word-level representation of the Inverse is given by,
    
    .. math::
    
        4. \quad W_{\text{inv}(ᚠ)} = \{ (1, \text{"repel"}), (2, \text{"lager"}), (3, \text{"a"}), (4, \text{"diaper}) \}
        
    To see how :ref:`Definition 2.1.6 <definition-2-1-6>` can be used to assert a Character falls between two Words in a Sentence, calculate the following Delimitations and String Lengths.
    
    Consider the words *"a"* and *"leper"*. *"a"* corresponds to the Word Index 2,
    
    .. math::
    
        5. \quad ᚠ\{2\} = \text{"a"}
    
    Calculating the left-hand side of the inequality in :ref:`Definition 2.1.6 <definition-2-1-6>`,
    
    .. math::
    
        6. \quad D\Pi_{x=1}^{2} ᚠ(x) = \text{"repaid a"}
    
    .. math::
        
        7. \quad l(D\Pi_{x=1}^{2} ᚠ(x)) = 8
    
    The String Length of this Delimitation is exactly equal to the Sentence Length *up to and including the Word at Index 2*. Now note *"leper"* occupies the Word Index 4, 
    
    .. math::
    
        8. \quad ᚠ\{4\} = \text{"leper"}
    
    This corresponds to a :math:`j = 4` in :ref:`Definition 2.1.6 <definition-2-1-6>`. The upperhand limit in the Delimitation on the right-hand side of the inequality in :ref:`Definition 2.1.6 <definition-2-1-6>` is given by,
    
    .. math::
    
        7. \quad \Lambda(ᚠ) - j + 1 = 4 -  4 + 1 = 1
    
    Therefore, the corresponding Delimitation of the Inverse Sentence for :ref:`Definition 2.1.6 <definition-2-1-6>` is given by,
    
    .. math::
    
        8. \quad D\Pi_{x=1}^{1} \text{inv}(ᚠ)(x) = \text{"repel"}
    
    .. math::
    
        9 \quad l(D\Pi_{x=1}^{1} \text{inv}(ᚠ)(x)) = 5
    
    Working from the back of the Sentence, the String Length of this Delimitation is exactly equal to the Sentence Length *up to and including the Word at Index 4*. Calculating the right-hand side of the inequality in :ref:`Definition 2.1.6 <definition-2-1-6>`, 
    
    .. math::
    
        10. \quad l(ᚠ) - l(D\Pi_{x=1}^{1} \text{inv}(ᚠ)(x)) + 1 = 20 - 5 + 1 = 16
    
    By :ref:`Definition 2.1.6 <definition-2-1-6>`, the Characters *ᚠ[k]* between the indices of 8 and 16 (exclusive) *intervene* *ᚠ{2}* and *ᚠ{4}*, namely, 
    
        - ᚠ[9] = " "
        - ᚠ[10] = "r"
        - ᚠ[11] = "e"
        - ᚠ[12] = "g"
        - ᚠ[13] = "a"
        - ᚠ[14] = "l"
        - ᚠ[15] = " "
    
    Therefore,
    
        - :math:`(2/9/4)_{ᚠ}` (the :math:`9^{\text{th}}` Character is between the second and fourth Word)
        - :math:`(2/10/4)_{ᚠ}` (the :math:`10^{\text{th}}` Character is between the second and fourth Word)
        - etc. 
    
    .. graphviz:: ../_static/dot/intervention.dot
        :caption: A diagram of the Intervention relation
        :alt: Intervention Diagram
    
    ∎
    
    As motivation for the first theorem on Interventions and a further clarification to show how Intervention and Delimitation are closely related, consider the following example.
    
    **Example**
    
    Let *ᚠ = "the world divides into facts"*. Then 
    
    .. math::
    
        1. \quad \Lambda(ᚠ) = 5
    
    .. math::
    
        2. \quad l(ᚠ) = 28
    
    Consider what happens when the limits of the Delimitation of a Sentence and the Delimitation of its Inverse are such that :math:`i = j` in the :ref:`Definition 2.1.6 <definition-2-1-6>`. Let :math:`i = j = 2`, i.e. consider the second Word in the Sentence, *"world"*. The relation of Intervention that obtains between *"world"* and itself should evaluate to false. In other words, no Characters intervene between a Word and itself. 
    
    The Delimitation of the Sentence up to the Second Word is given by,
    
    .. math::
    
        3. \quad \Pi_{x=1}^{2} ᚠ(x) = \text{"the world"}
    
    The Delimitation of the Inverse Sentence up to the correspond index of the Second Word (e.g., :math:`5 - 2 + 1 = 4`) is given by (Note the Inverse Sentence is not a Sentence in a Corpus, nor does it possess semantic coherence),
    
    .. math::
    
        4. \quad D\Pi_{x=1}^{5 - 2 + 1} \text{inv}(ᚠ(x)) = D\Pi_{x=1}^{4} \text{inv}(ᚠ(x)) = \text{"stcaf otni sedivid dlrow"}
    
    Therefore,
    
    .. math::
    
        5. \quad l(D\Pi_{x=1}^{2} ᚠ(x)) = 9
    
    .. math::
    
        6. \quad l(D\Pi_{x=1}^{4} \text{inv}(ᚠ(x))) = 24
    
    The sum of these String Lengths is given by,
    
    .. math::
    
        7. \quad l(D\Pi_{x=1}^{2} ᚠ(x)) + l(D\Pi_{x=1}^{4} \text{inv}(ᚠ(x))) = 9 + 24 = 33
    
    Since the total String Length of both Delimitation exceeds the String Length of the entire Sentence, there does not exist a Character Index *k* such that *k* can be said to intervene the Word at index :math:`i = j = 2`. ∎
    
    This example provides justification for the next theorem.
    
    .. _theorem-2-1-3:
    
    **Theorem 2.1.3** :math:`\forall \zeta \in C_{L}: \forall i, j \in N_{\Lambda(\zeta)}: i \neq k \to \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta}`
    
    This theorem can be stated in natural language as follows: For any Sentence in a Corpus, there exists a Character that intervenes two Words in the Sentence if and only the Words occupy different positions. Note this doesn't exclude possibility the Words at different positions are the same Word.
    
    Let *ζ* be an arbitrary Sentence in Corpus **C**:sub:`L` and let *i* and *j* be natural numbers such that,
    
    .. math::
    
        1. \quad \zeta \in C_L
        
    .. math::
    
        2. \quad i, j \in N_{\Lambda(\zeta)}
       
    (→) Assume 
    
    .. math::
    
        3. \quad i \neq j
    
    Without loss of generality (since the case :math:`i > j` is symmetrical), assume 
    
    .. math::
    
        4. \quad i < j
    
    By :ref:`Theorem 2.3.4 <theorem-2-3-4>`, 
    
    .. math::
    
        5. \quad \zeta = D\Pi_{x=1}^{\Lambda(\zeta)} p(x)
    
    Where 
    
    .. math::
        
        6. \quad p \in X_L(\Lambda(\zeta))`
    
    By :ref:`Definition 1.2.7 <definition-1-2-7>` of Delimitation, this means 
    
    .. math::
    
        7. \quad \zeta = (\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{\Lambda(ζ)\}) 
    
    By step 5, *ζ{i}* comes before *ζ{j}* in the Sentence *ζ*. By the :ref:`Discovery Axiom W.1 <axiom-w1>`, there must be at least one delimiter character between *ζ{i}* and *ζ{j}* because they are distinct Words in a valid Sentence. 
    
    Let *σ* be a delimiter Character between *ζ{i}* and *ζ{j}*. Let *k be the index of this σ in the character-level representation of ζ (i.e., *ζ[k] = σ*).
    
    By the :ref:`Definition 1.2.7 <definition-1-2-7>` of Delimitations, 
    
    .. math::
    
        8. \quad l(D\Pi_{x=1}^{i} \zeta(x)) 
        
    Will give the index of the last character of ζ{i}. Since σ comes after ζ{i}, it follows,
    
    .. math::
    
        9. \quad l(D\Pi_{x=1}^{i} \zeta(x)) < k
    
    Similarly, 
    
    .. math::
    
        10. \quad l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1 
        
    Gives the index of the first Character after the Word corresponding to *ζ{j}* in the original sentence. Since σ comes before this character, it follows,
    
    .. math::
    
        11. \quad k < l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1
    
    Therefore, by :ref:`Definition 2.1.6 <definition-2-1-6>`, 
    
    .. math::
    
        12. \quad (i/k/j)_{\zeta}
    
    Thus,
    
    .. math::
    
        13. \quad \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta}
    
    (←) Assume a Character exists at index *n* in *ζ* such that it that intervenes *ζ{i}* and *ζ{j}*,
    
    .. math::
    
        1. \quad \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta}
    
    By :ref:`Definition 2.1.6 <definition-2-1-6>`,
    
    .. math::
    
        2. \quad l(D\Pi_{x=1}^{i} \zeta(x)) < n < l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - j + 1} \text{inv}(\zeta)(x)) + 1
    
    Assume, for the sake of contradiction, that :math:`i = j`.
    
    .. math::
    
        3. \quad l(D\Pi_{x=1}^{i} \zeta(x)) < n < l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x)) + 1
    
    Now, consider the term :math:`l(D\Pi_{x=1}^{i} \zeta(x))`. This represents the String Length of the Delimitation of the first *i* words of *ζ*. By the :ref:`Definition 1.2.7 <definition-1-2-7>` of Delimitations, this includes the lengths of the first *i* words and the lengths of the :math:`(i - 1)` delimiters between them.
    
    Similarly, consider the term :math:`l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x))`. This represents the String Length of the Delimitation of the first *Λ(ζ) - i + 1* words of *inv(ζ)*.  Since *inv(ζ)* has the same words as *ζ* but inverted and in reverse order, this is equivalent to the String Length of the uninverted Sentence up to the *i*:sup:`th` word of *ζ*, measured from the last Character in the String.
    
    The sum of the String Lengths of these two portions of the Sentence *ζ* is always greater than the String Length of the Sentence, 
    
    .. math::
    
        4. \quad l(D\Pi_{x=1}^{i} \zeta(x)) + l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x)) >  l(\zeta) 
    
    This follows from the fact that these two portions of ζ are overlapping since both  include terms for *ζ{i}* (:math:`\text{inv}(\zeta)\{\Lambda(\zeta) - i + 1\}` would be the corresponding Word in the Delimitation of the Inverse). From step 4, it then follows,
    
    .. math::
    
        5. \quad l(D\Pi_{x=1}^{i} \zeta(x)) > l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x))  
        
    Adding 1 to both sides maintains the inequality in step 5,
    
    .. math::
    
        6. \quad l(D\Pi_{x=1}^{i} \zeta(x)) + 1 > l(\zeta) - l(D\Pi_{x=1}^{\Lambda(\zeta) - i + 1} \text{inv}(\zeta)(x)) + 1
    
    Combining this with the left-hand side of the inequality in step 5, we get:
    
    .. math::
    
        7. \quad l(D\Pi_{x=1}^{i} \zeta(x)) < n < l(D\Pi_{x=1}^{i} \zeta(x)) + 1
       
    But String Lengths are integers, and by the laws of arithmetic, there cannot exists a natural number between two numbers that are successors of one another. A contradiction has been dervied. Therefore, the assumption that :math:`i = j` must be false.
    
    .. math::
    
        8. \quad i \neq j.
    
    With both directions of the equivalence proven, since *ζ*, *i*, and *j* were arbitrary, this can be generalized over the Corpus, 
    
    .. math::
    
        9. \quad \forall \zeta \in C_L: \forall i, j \in N_{\Lambda(zeta)}: i \neq j ↔ \exists n \in N_{l(\zeta)}: (i/n/j)_{\zeta} 
        
    ∎
    
    .. _section-ii-ii:
    
    Section II.II: Axioms 
    ----------------------
    
    In :ref:`Section I <section-i>`, the first three axioms of the formal system were introduced. Now that definitions and notations have been introduced for Sentence and Corpus, the axioms may be expanded to further refine the character of the system being built. The Equality, Character and Discovery Axiom are reprinted below, so they may be considered in sequence with the other axioms.
    
    Note the Discovery Axiom has been revised to employ Character Index notation. 
    
    .. _axiom-c0-2:
    
    **Axiom C.0: The Equality Axiom**
    
    .. math::
    
        1. \quad \forall \iota \in \Sigma: \iota = \iota
    
    .. math::
    
        2. \quad \forall \iota, \nu \in \Sigma: \iota = \nu ↔ \nu = \iota
        
    .. math::
    
        3. \quad \forall \iota, \nu, \omicron \in \Sigma: (\iota = \nu \land \nu = \omicron) \to (\iota = \omicron) 
    
    ∎
    
    .. _axiom-c1-2:
    
    **Axiom C.1: The Character Axiom**
    
    .. math::
    
        \forall \iota \in \Sigma: \iota \in S 
        
    ∎
    
    .. _axiom-w1-2:
    
    **Axiom W.1: The Discovery Axiom** 
    
    .. math::
    
        \forall \alpha \in L: [ (l(\alpha) \neq 0) \land (\forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma) ] 
        
    ∎
    
    .. _axiom-s1:
    
    **Axiom S.1: The Duality Axiom**
    
    .. math::
    
        ( \forall \alpha \in L: \exists \zeta \in C_L: \alpha \subset_s \zeta ) ∧ ( \forall \zeta \in C_L: \exists \alpha \in L: \alpha \subset_s \zeta ) 
        
    ∎
    
    .. _axiom-s2:
    
    **Axiom S.2: The Extraction Axiom**
    
    .. math::
    
        \forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in L 
        
    ∎
    
    Two new axioms, the :ref:`Duality Axiom S.1 <axiom-s1>` and the :ref:`Extraction Axiom S.2 <axiom-s2>`, have been added to the formal system to finalize its core assumptions. It is worth taking the time to analyze the structure, however minimal, these axioms imply must exist in any Language. It should be re-iterated that no assumptions have been made regarding the semantic content of a Language or its Corpus, so any insight that arises from these axioms is due to inherent linguistic structures (assuming these axioms capture the nature of real language). 
    
    To briefly summarize the axioms previously introduced: The system *"initializes"* with the assumption of an equality relation and the selection of an Alphabet **Σ**. The Character Axiom ensures the domain of all Strings is populated. The Discovery Axiom ensures Words only traverse the set of Strings which do not contain Delimiters. With these axioms, still nothing has been said about *what* a Word is, except that it possesses a semantic character. To re-iterate, a Language and Corpus are fixed on top of the domain of all Strings outside of the system. 
    
    The new axioms introduced in the formal system begin to characterize the syntactical properties of the next level in the lingustic hierarchy, while still maintaining their ambivalence on the semantic content contained within their respective categories.
    
    The :ref:`Duality Axiom S.1 <axiom-s1>` bares a striking resemblance to the idea of *surjection* in real analysis. Recall, a function :math:`f: X \to Y` is called *surjective* if,
    
    .. math::
    
        \forall y \in Y: \exists x \in X : f(x) = y
    
    Meaning, every element in the co-domain is mapped to at least one element in the domain. 
    
    In a sense, the :ref:`Duality Axiom S.1 <axiom-s1>` asserts a type of *"double-surjectivity"* exists between the domain of Words and the co-domain of Sentences.  In plain language, the :ref:`Duality Axiom <axiom-s1>` asserts for every Word *α* in the Language **L**, there exists a sentence *ζ* in the Corpus **C**:sub:`L` such that *α* is contained in *ζ*, and for every Sentence *ζ* in the corpus **C**:sub:`L`, there exists a word *α* in the language **L** such that *α* is contained in *ζ*. 
    
    However, there is a key difference between the notion of *surjection* in real analysis and the notion captured in the Duality Axiom S.1. Containment is not a strict equality relation. By :ref:`Definition 1.1.6 <definition-1-1-6>` and :ref:`Definition 1.1.7 <definition-1-1-7>`, containment reduces to the existence of a mapping between Characters in different Strings. Due to the :ref:`Discovery Axiom W.1 <axiom-w1>`, with the exception of Sentences consisting of a Single Word, a Word is contained in a Sentence but a Sentence is not contained in a Word. 
    
    More plainly, the :ref:`Duality Axiom S.1 <axiom-s1>` states a Word cannot exist in a Language without being included in a Sentence of the Corpus, and a Sentence cannot exist in a Corpus without including a Word from the Language. This Axiom captures an inextricable duality between the metamathematical concepts of Sentence and Word, and the concepts of Language and Corpus: one cannot exist without implying the existence of the other. Words and Sentences do not exist in isolation. A Language and its Corpus require one another. 
    
    The :ref:`Extraction Axiom S.2 <axiom-s2>` further strengthens the relationship that exists between a Corpus and Language. It states every Word in the Sentence of a Corpus must be included in a Language. This idea of being able *extract* the Words of a Language from a Sentence is captured in the terminology introduced in :ref:`Definition 2.2.1 <definition-2-2-1>` directly below. 
     
    .. _definition-2-2-1:
    
    **Definition 2.2.1: Semantic Coherence** 
    
    A Sentence *ᚠ* is *semantically coherent* in a Language **L** if and only if **W**:sub:`ᚠ` only contains words from Language **L**. 
    
    A Corpus :math:`C_L` is *semantically coherent* in a Language **L** if and only if the Word-level set representation of all its Sentences are semantically coherent. ∎
    
    .. _sentence_theorems:
    
    Theorems
    ^^^^^^^^
    
    The first theorems proven using these new axioms are analogous versions of the Word theorems :ref:`Theorems 1.2.1 <theorem-1-2-1>` - :ref:`1.2.3 <theorem-1-2-3>` for Sentences. These theorems, like their Word counterparts, represent the logical pre-conditions for Sentences to arise in the domain of all Strings. 
    
    .. _theorem-2-2-1:
    
    **Theorem 2.2.1** :math:`\forall \zeta \in C_L: l(\zeta) \neq 0`
    
    Let *ζ* be an arbitrary sentence in :math:`C_L`, and let *i* be a natural number such that :math:`1 \leq i \leq l(\zeta)`.
    
    By the second conjunct of the :ref:`Duality Axiom S.2 <axiom-s2>` and the first conjunct of the :ref:`Discovery Axiom W.1 <axiom-w1>`,
    
    .. math::
    
        1. \quad \exists \alpha \in L: \alpha \subset_s \zeta 
        
    .. math::
    
        2. \quad \forall \alpha \in L: l(\alpha) \neq 0
    
    Therefore, by :ref:`Definition 1.1.7 <definition-1-1-7>`, there exists a strictly increasing and consecutive function *f* such that,
    
    .. math::
    
        3. \quad \forall i \in N_{l(\alpha)}: \alpha[i] = \zeta[f(i)] 
        
    By :ref:`Theorem 1.2.3 <theorem-1-2-3>`, 
    
    .. math::
    
        4. \quad \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon
    
    Therefore, combining steps 3 and 4,
    
    .. math::
    
        5. \quad \forall i \in N_{\alpha}: \zeta[f(i)] \neq ε
    
    Since, by step 2, :math:`l(\alpha) \neq 0`, there must be some non-zero *i* that satisfies step 5. Therefore, there is at least one non-Empty Character in *ζ*, namely, *ζ[f(i)]*. The theorem is then proven by applying :ref:`Definition 1.1.3 <definition-1-1-3>`,
    
    .. math::
    
        6. \quad l(\zeta) \neq 0 
    
    ∎
    
    .. _theorem-2-2-2:
    
    **Theorem 2.2.2** :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \zeta[i] \subset_s \zeta`
    
    Let *ζ* be an arbitrary sentence in :math:`C_L`, and let *i* be a natural number such that :math:`1 \leq i \leq l(\zeta)`. By :ref:`Theorem 2.2.1 <theorem-2-2-1>` and :ref:`Definition 1.1.3 <definition-1-1-3>`, there must be at least one non-Empty Character in *ζ*. Let *ζ[i]* be a non-Empty Character in *ζ*. Consider the string *s* consisting of the single character *ζ[i]*, :math:`s = \zeta[i]`. Clearly, by :ref:`Definition 1.1.3 <definition-1-1-3>`, 
    
    .. math::
    
        1. \quad l(s) = 1
    
    Define a function :math:`f: \{1\} \to \{i\}` such that :math:`f(1) = i`. This function is strictly increasing and consecutive. By :ref:`Definition 1.1.6 <definition-1-1-6>` and :ref:`Definition 1.1.7 <definition-1-1-7>`, since there exists a strictly increasing and consecutive function *f* from the indices of *s* to the indices of *ζ*, and since the Character at position 1 in *s* is the same as the Character at position i in *ζ* (both are *ζ[i]*), we can conclude that *s* is contained in *ζ*. Therefore, 
    
    .. math::
    
        2. \quad \zeta[i] \subset_s \zeta
    
    Since *ζ* and *i* were arbitrary, this can be generalized, 
    
    .. math::
    
        3. \quad \forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \zeta[i] \subset_s \zeta 
    
    ∎
    
    .. _theorem-2-2-3:
    
    **Theorem 2.2.3** :math:`\forall \zeta \in C_{L} : \forall i \in N_{l(\zeta)}:  \zeta[i] \neq \varepsilon`
    
    Let *ζ* be an arbitrary sentence in **C**:sub:`L`, and let *i* be a natural number such that :math:`1 \leq i \leq l(\zeta)`. By :ref:`Theorem 2.2.2 <theorem-2-2-2>`, 
    
    .. math::
        
        1. \quad \forall i \in N_{l(\zeta)}: \zeta[i] subset_s \zeta
    
    By :ref:`Definition 1.1.3 <definition-1-1-3>`, String Length is the number of non-Empty Characters in a String's Character-level set representation. Since :math:`l(\zeta) > 0`, *ζ* must have at least one non-Empty character.
    
    Since :math:`1 \leq i \leq l(\zeta)`, the Character at position *i* in *α*, denoted *ζ[i]*, exists and is non-Empty by :ref:`Definition 1.1.2 <definition-1-1-2>`. Therefore, 
    
    .. math::
    
        2. \quad \zeta[i] \neq \varepsilon 
    
    Since *ζ* and *i* are arbitrary, this can generalized,
    
    .. math::
    
        3. \quad \forall \alpha \in L: \forall i \in N_{l(\zeta)}: \zeta[i] \neq \varepsilon 
    
    ∎
    
    .. _theorem-2-2-4:
    
    **Theorem 2.2.4** :math:`\forall \zeta \in C_{L}: \Lambda(\zeta) \geq 1`
    
    Let *ζ* be an arbitrary sentence in **C**:sub:`L`. By the second conjunct of the :ref:`Duality Axiom S.1 <axiom-s1>`,
    
    .. math::
    
        1. \quad \exists \alpha \in L: \alpha \subset_s \zeta
    
    By the first conjunct of the :ref:`Discovery Axiom W.1 <axiom-w1>`,
    
    .. math::
    
        2. \quad l(\alpha) \neq 0
    
    Therefore, by :ref:`Definition 1.1.7 <definition-1-1-7>`, there exists an *f* such that, 
    
    .. math::
    
        3. \quad \forall i \in N_{l(\alpha)}: \alpha[i] = \zeta[f(i)]
    
    By :ref:`Theorem 1.2.3 <theorem-1-2-3>`, 
    
    .. math::
    
        4. \quad \forall i \in N_{l(\alpha)}: \alpha[i] \neq \varepsilon
    
    Therefore, combining step 3 and 4,
    
    .. math::
    
        5. \quad \forall i \in N_{l(\alpha)}: \zeta[f(i)] \neq \varepsilon
    
    Since :math:`l(\alpha) \neq 0`, there is at least one non-Empty Character in *ζ* and therefore, by :ref:`Definition 1.1.3 <definition-1-1-3>`,
    
    .. math::
    
        6. \quad \Lambda(\zeta) \geq 1
    
    Generalizing this over the Corpus,
    
    .. math::
        
        7. \quad \forall \zeta \in C_L: \Lambda(\zeta) \geq 1 
    
    ∎
    
    .. _theorem-2-2-5:
    
    **Theorem 2.2.5** :math:`\forall \zeta \in C_L: \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`
    
    This theorem can be stated in natural language as follows: Every Sentence in the Corpus is the Delimitation of its own Words.
    
    Assume 
    
    .. math::
    
        1. \quad ζ \in C_L
    
    By :ref:`Definition 2.1.3 <definition-1-2-3>`,
    
    .. math::
    
        2. \quad W_{\zeta} = (\alpha_1, \alpha_2, ..., \alpha_{\Lambda(\zeta)}) 
        
    where
    
    .. math::
    
        3. \quad \alpha_i \in L.
    
    By :ref:`Definition 1.2.5 <definition-1-2-5>`, the sequence :math:`W_{\zeta}` forms a phrase :math:`P_{\Lambda(\zeta)}` of length *Λ(ζ)* where,
    
    .. math::
    
       4. \quad \forall i \in N_{\Lambda(\zeta)}: P_{\Lambda(\zeta)}(i) = \alpha_i 
        
    By :ref:`Definition 1.2.7 <definition-1-2-7>`, the Delimitation of P:sub:`Λ(ζ)` is,
    
    .. math::
    
        5. \quad D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)} (i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_{\Lambda(\zeta)})
    
    The Delimitation reconstructs the original Sentence *ζ* by including the Delimiters between Words. Therefore,
    
    .. math::
    
        6. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)} (i)
    
    By :ref:`Definition 2.1.5 <definition-2-1-5>`, 
    
    .. math::
    
        7. \quad \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} = \alpha_i
    
    Therefore,
    
    .. math::
        
        8. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}
    
    Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,
    
    .. math::
    
        9. \quad \forall \zeta \in C_L: \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\} 
    
    ∎
    
    .. _section-ii-iii:
    
    Section II.III: Sentence Classes 
    --------------------------------
    
    As the astute reader has no doubt surmised at this point, the foundational operation that defines a palindromic structure in linguistics is *inversion* (i.e. a method of reversal). What may not yet be clear is how this operation of inversion propagates through the hierarchy of entities defined over its domain. As this necessary structure of interdependent inversions between hierarchical layers becomes apparent, the mathematical description of a Palindrome will seen to be a *"recursion of inversions"*.
    
    :ref:`Theorems 2.3.9 <theorem-2-3-9>` - :ref:`2.3.11 <theorem-2-3-11>` of this subsection mark the first notable results obtained from the formal system. Their empirical truth in natural language represents confirmation of the formal system's construction. These theorems demonstrate the Character-level symmetries required by invertibility propagate up through the Word-level of linguistics and manifest in conditions that must be imposed on the Word-level structure of an Invertible Sentence.
    
    .. _admissible-sentences:
    
    Admissible Sentences
    ^^^^^^^^^^^^^^^^^^^^
    
    The notion of an *Admissible Sentence* is required to prevent a certain class of Sentence inversions from invalidating the symmetry conditions of Palindromes derived in :ref:`Section IV <section-iv>`. 
    
    To see what is meant by this concept of *admissibility*, consider the English sentence,
    
    .. math::
    
        ᚠ = \text{"strap on a ton"}
    
    The Inverse of this sentence, *inv(ᚠ)*, is *semantically coherent* (:ref:`Definition 2.2.1 <definition-2-2-1>`). By this it is meant every word in its inversion is part of the English language,
    
    .. math::
    
        \text{inv}(ᚠ) = \text{"not a no parts"}
    
    However, this is not enough to ensure *inv(ᚠ)* is part of the Corpus, as is apparent. *Semantic coherence* is a necessary but not sufficient condition for the Inverse of a Sentence to remain in the Corpus. In order to state the requirement that must be imposed on a Sentence to remain *admissible* after inversion, the concept of Delimitation introduced in :ref:`Definition 1.2.7 <definition-1-2-7>` must now be leveraged. 
    
    .. _definition-2-3-1:
    
    **Definition 2.3.1: Admissible Sentences**
    
    Let *p* be any Phrase from a Language's *n*:sup:`th` Lexicon :math:`X_L (n)`. A String *t* is said to belong to the class of *Admissible Sentences of Word Length n* in Language **L**, denoted :math:`A(n)`, if it satisfies the following open formula
    
    .. math::
    
        t \in A(n) \leftrightarrow (\exists p \in X_L(n): t = D\Pi_{i=1}^{n} p(i)) \land (t \in C_L)
    
    ∎
    
    The notion of *admissibility* is a faint echo of *"grammaticality"*. As inversion is studied at the sentential level of the linguistic hierarchy, it is no longer permitted to ignore semantics in its entirety. Instead, semantics ingresses into the system as implicit properties the extensionally identified Sentences must obey. Before discussing this at greater length, several theorems are proved about classes of Admissible Sentences.
    
    .. _theorem-2-3-1:
    
    **Theorem 2.3.1** :math:`A(n) \subseteq C_{L}`
    
    Let *t* be an arbitrary String such that :math:`t \in A(n)`. By :ref:`Definition 2.3.1 <definition-2-3-1>`, this implies, :math:`t \in C_L`. Therefore,
    
    .. math::
    
        1. \quad t \in A(n) \to t \in C_L
    
    This is exactly the set theoretic definition of a subset. Thus,
    
    .. math::
    
        2. \quad A(n) \subseteq C_L 
    
    ∎
    
    :ref:`Theorem 2.3.1 <theorem-2-3-1>` is the formal justification for quantifying Sentence Variables over the set of Admissible Sentences (i.e. all Admissable Sentences are in the Corpus), as in the following theorem.
    
    .. _theorem-2-3-2:
    
    **Theorem 2.3.2** :math:`\forall \zeta \in A(n): \Lambda(\zeta) = n`
    
    Let *ζ* be an arbitrary sentence in :math:`A(n)`. By :ref:`Definition 2.3.1 <definition-2-3-1>`, if :math:`\zeta \in A(n)`, then there exists a Phrase :math:`p \in X_L(n)` such that 
    
    .. math::
    
        1. \quad (\zeta \in C_L) \land (\zeta = D\Pi_{i=1}^{n} p(i))
    
    By :ref:`Definition 1.2.5 <definition-1-2-5>` and :ref:`Definition 1.2.6 <definition-1-2-6>`, a phrase *p* in :math:`X_L(n)` is an ordered sequence of *n* words such that :math:`\alpha_i \in L`,
    
    .. math::
    
        2. \quad p = (\alpha_1, \alpha_2, ..., \alpha_n)
    
    By :ref:`Definition 1.2.7 <definition-1-2-7>`, the Delimitation of *p* is given by,
    
    .. math::
    
        3. \quad D\Pi_{i=1}^{n} p(i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_n)
    
    In other words, the Delimitation of *p* (which is equal to *ζ*) explicitly constructs a String with *n* Words separated by Delimiters.
    
    By :ref:`Definition 2.1.4 <definition-2-1-4>`, the Word Length *Λ(ζ)* is the number of Words in *ζ*. Since *ζ* is formed by limiting a Phrase with *n* Words, and the Delimitation process doesn't add or remove Words, the Word Length of *ζ* must be *n*. Therefore, 
    
    .. math::
    
        4. \quad \Lambda(\zeta) = n.
    
    Since *ζ* was an arbitrary sentence in :math:`A(n)`, this can generalize as,
    
    .. math::
    
        5. \quad \forall \zeta \in A(n): \Lambda(\zeta) = n 
    
    ∎
    
    .. _theorem-2-3-3:
    
    **Theorem 2.3.3** :math:`\forall \zeta \in C_{L}: \zeta \in A(\Lambda(\zeta))`
    
    Let ζ be an arbitrary sentence in :math:`C_L`. By :ref:`Definition 2.1.3 <definition-2-1-3>`, *ζ* has a Word-level representation,
    
    .. math::
    
        1. \quad W_{\zeta} = (\alpha_1, \alpha_2, ... , \alpha_{\Lambda(\zeta)}) 
        
    Where each :math:`\alpha_i \in L`. By :ref:`Definition 1.2.5 <definition-1-2-5>`, the sequence :math:`(\alpha_1, \alpha_2, ... , \alpha_{\Lambda(\zeta)})` forms a phrase :math:`P_{\Lambda(\zeta)}` of length *Λ(ζ)* where :math:`P_{\Lambda(\zeta)}(i) = \alpha_i` for all *i* such that :math:`1 \leq i \leq \Lambda(\zeta)`.
    
    By :ref:`Definition 1.2.6 <definition-1-2-6>`, since :math:`P_{\Lambda(\zeta)}` is a phrase of length *Λ(ζ)* and all its Words belong to **L** (by semantic coherence), then,
    
    .. math::
    
        2. \quad P_{\Lambda(\zeta)} \in X_L(\Lambda(\zeta)).
    
    By :ref:`Definition 1.2.7 <definition-1-2-7>`, the Delimitation of :math:`P_{\Lambda(\zeta)}` is:
    
    .. math::
    
        3. \quad D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)}(i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_{\Lambda(\zeta)})
    
    The Delimitation :math:`D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)} (i)` reconstructs the original sentence *ζ*, including the Delimiters between Words. Therefore,
    
    .. math::
    
        4. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)}(i)
    
    By :ref:`Definition 2.3.1 <definition-2-3-1>`, a String *t* is an Admissible Sentence of Word Length *n* (:math:`t \in A(n)`) if and only if there exists a phrase :math:`p \in X_L(n)` such that,
    
    .. math::
    
        5. \quad t = D\Pi_{i=1}^{n} p(i)
        
    .. math::
    
        6. \quad t \in C_L
    
    As a direct consequence of :ref:`Definition 2.3.1 <definition-2-3-1>`, since the conjunction of the following three facts is true,
    
    .. math::
    
        7. \quad \zeta \in C_L
        
    .. math::
        
        8. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)} (i)
       
    .. math::
    
        9. \quad P_{\Lambda(\zeta)} \in X_L(\Lambda(\zeta)) 
        
    It follows from step 7 - step 9, :math:`\zeta \in A(\Lambda(\zeta))`. Since *ζ* was an arbitrary Sentence in :math:`C_L`, this can generalize over the Corpus,
    
    .. math::
    
        10. \quad \forall \zeta \in C_L: \zeta \in A(\Lambda(\zeta)) 
    
    ∎
    
    .. _theorem-2-3-4:
    
    **Theorem 2.3.4** :math:`\forall \zeta \in C_L: \exists p \in X_L(\Lambda(\zeta)): \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} p(i)`
    
    Let *ζ* be an arbitrary sentence in :math:`C_L`. By :ref:`Definition 2.1.3 <definition-2-1-3>`, *ζ* has a Word-level representation,
    
    .. math::
    
        1. \quad W_{\zeta} = (\alpha_1, \alpha_2, ..., \alpha_{\Lambda(\zeta)}) 
        
    Where each :math:`\alpha_i \in L`.
    
    By :ref:`Definition 1.2.5 <definition-1-2-5>`, the sequence :math:`(\alpha_1, \alpha_2, ... , \alpha_{\Lambda(\zeta)})` forms a Phrase :math:`P_{\Lambda(\zeta)}` of Word Length *Λ(ζ)* where :math:`P_{\Lambda(\zeta)}(i) = \alpha_i` for all *i*, :math:`1 \leq i \leq \Lambda(\zeta)`.
    
    By :ref:`Definition 1.2.6 <definition-1-2-6>`, since :math:`P_{\Lambda(\zeta)}` is a Phrase of Word Length *Λ(ζ)* and all its words belong to **L**, then,
    
    .. math::
    
        2. \quad P_{\Lambda(\zeta)} \in X_L(\Lambda(\zeta))
    
    By :ref:`Definition 1.2.7 <definition-1-2-7>`, the Delimitation of :math:`P_{\Lambda(\zeta)}` is,
    
    .. math::
    
        3. \quad D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)} (i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_{\Lambda(\zeta)})
    
    The Delimitation :math:`D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)}(i)` reconstructs the original Sentence *ζ*, including the Delimiters between Words. Therefore:
    
    .. math::
    
        4. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} P_{\Lambda(\zeta)}(i)
    
    It has been shown that for an arbitrary Sentence :math:`ζ \in C_L`, there exists a Phrase *p* (specifically, :math:`P_{\Lambda(\zeta)}`) in :math:`X_L(\Lambda(\zeta))` such that,
     
    .. math::
    
        5. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} p(i). 
        
    Therefore, generalizing this over the Corpus,
    
    .. math::
    
        6. \quad \forall \zeta \in C_L: \exists p \in X_L(\Lambda(\zeta)): \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} p(i) 
        
    ∎
    
    The condition of *admissibility*, as will be seen in :ref:`Theorem 2.3.11 <theorem-2-3-11>`, prevents the *"inversion propagation"* from being a purely syntactical operation. The Inverse of a Sentence must also be Admissible in the Corpus in order to be considered an Invertible Sentence (:ref:`Definition 2.3.2 <definition-2-3-2>` in the next section). This represents a rupture or division from the realm of syntax not seen at the Word level of the linguistic hierarcy when considering the operation of inversion. In order to fully specify the conditions for Sentence invertibility, one must be able to elaborate what it means to call a Sentence *"admissible"*; in other words, there must be grammatical rules that identify an inverted Sentence as belonging to the Corpus over and above the syntactical conditions that are imposed by invertibility.
    
    However, this does not mean *"grammaticality"* is equivalent to *"admissibility"*. As the final section of the work will make clear, there are possible avenues available to formal analysis for parsing the concept of *"admissibility"* into finer partitions such as *"syntactical admissibility"* and *"semantic admissiblity"*. In this way, the origin of meaning in a Sentence can be narrowed down by filtering out its syntactical origins.
    
    .. _invertible-sentences:
    
    Invertible Sentences
    ^^^^^^^^^^^^^^^^^^^^
    
    Similarly to the progression of Words and their related concepts in the previous section, a special class of Sentences will now be classified according to their syntactical properties. In the study of palindromic structures, the notion of *Invertible Sentences* is essential. The definition, as is fitting in a work focused on palindromes, will mirror :ref:`Definition 1.3.1 <definition-1-3-1>` of an *Invertible Word*.
    
    The notion of Invertible Sentences will first be defined extensionally, and then clarified heuristically. The following definition and theorem mirror the mechanics of :ref:`Definition 1.3.1 <definition-1-3-1>` and :ref:`Theorem 1.3.1 <theorem-1-3-1>` almost exactly.
    
    .. _definition-2-3-2:
    
    **Definition 2.3.2: Invertible Sentences** 
    
    Let *ζ* be any Sentence in from a Corpus **C**:sub:`L`. Then the set of Invertible Sentences **K** is defined as the set of *ζ* which satisfy the open formula,
    
    .. math::
    
        \zeta \in K \leftrightarrow \text{inv}(\zeta) \in C_L
    
    A Sentence *ζ* will be referred to as *Invertible* if it belongs to the class of Invertible Sentences. ∎
    
    This definition is immediately employed to derive the following theorems.
    
    .. _theorem-2-3-5:
    
    **Theorem 2.3.5** :math:`\forall \zeta \in C_L: \zeta \in K \leftrightarrow \text{inv}(\zeta) \in K`
    
    Let *ζ* be any Sentence from Corpus **C**:sub:`L`.
    
    (→) Assume :math:`\zeta \in K`
    
    By :ref:`Definition 2.3.2 <definition-2-3-2>`, the inverse of *ζ* belongs to the Corpus
    
    .. math::
    
        1. \quad \text{inv}(\zeta) \in C_L
    
    To show that *inv(ζ)* is invertible, it must be shown that,
    
    .. math::
    
        2. \quad \text{inv}(\text{inv}(\zeta)) \in C_L
    
    From :ref:`Theorem 1.2.4 <theorem-1-2-4>`, for any string *s*, 
    
    .. math::
    
        3. \quad \text{inv}(\text{inv}(s)) = s.  
    
    By :ref:`Definition 2.1.1 <definition-2-1-1>`,
    
    .. math::
    
        4. \quad \zeta \in S
    
    Where **S** is the set of all Strings. Therefore, it follows, 
    
    .. math::
    
        5. \quad \text{inv}(\text{inv}(\zeta)) = \zeta
    
    From step 1 and step 5, it follows, 
    
    .. math::
    
        6. \quad \text{inv}(\text{inv}(\zeta)) \in C_L
    
    By :ref:`Definition 2.3.2 <definition-2-3-2>`, this implies,
    
    .. math::
    
        7. \quad \text{inv}(\zeta) \in K
    
    (←) Assume :math:`\text{inv}(\zeta) \in K`
    
    By :ref:`Definition 2.3.2 <definition-2-3-2>`, 
        
    .. math::
    
        8. \quad \text{inv}(\text{inv}(\zeta)) \in C_L
    
    Applying :ref:`Theorem 1.2.4 <theorem-1-2-4>`,
    
    .. math::
    
        9. \quad \text{inv}(\text{inv}(\zeta)) = \zeta
    
    From step 8 and step 9, it follows, 
    
    .. math::
    
        10. \quad \zeta \in C_L
    
    By :ref:`Definition 2.3.2 <definition-2-3-2>`, it follows,
    
    .. math::
    
        11. \quad \zeta \in K
    
    Putting both direction of the equivalence together and generalizing over the Corpus, the theorem is shown,
    
    .. math::
    
        12. \quad \forall \zeta \in C_L: \zeta \in K \leftrightarrow \text{inv}(\zeta) \in K 
    
    ∎
    
    .. _theorem-2-3-6:
    
    **Theorem 2.3.6** :math:`\forall \zeta \in C_L: \text{inv}(\zeta) \in K \to \zeta \in C_L`
    
    Let *ζ* be any Sentence from Corpus **C**:sub:`L` such that :math:`\text{inv}(\zeta) \in K`. Then, by :ref:`Definition 2.3.2 <definition-2-3-2>`,
    
    .. math::
    
        1. \quad \text{inv}(\text{inv}(\zeta)) \in C_L
    
    By :ref:`Theorem 1.2.4 <theorem-1-2-4>`,
    
    .. math::
    
        2. \quad \text{inv}(\text{inv}(\zeta)) = \zeta
    
    Therefore, combining step 1 and step 2,
    
    .. math::
    
        3. \quad \zeta \in C_L 
    
    It follows, 
    
    .. math::
    
        4. \quad \forall \zeta \in C_L: \text{inv}(\zeta) \in K \to \zeta \in C_L 
    
    ∎
    
    The notion of Invertible Sentences is not as intuitive as the notion of Invertible Words. This is due to the fact the condition of *invertibility* is not a weak condition; indeed, Sentences that are not invertible far outnumber Sentences that are invertible in a given Language (for all known natural languages, at any rate; it is conceivable a purely formal system with no semantic content or general applicability could be constructed with invertibility in mind). 
    
    To see how strong of a condition invertibility is, the author challenges the reader to try and construct an invertible sentence in English (or whatever their native tongue might be). :ref:`Section VIII <section-vii>` contains a list of Invertible Words and Reflective Words. These can be used as a "palette" for the exercise. The exercise is worthwhile, because it forces the reader to think about the mechanics of sentences and how a palindrome resides in the intersection of semantics and syntax.  
    
    Consider the following examples phrases from English,
    
    - no time
    - dog won 
    - not a ton 
    
    All of these phrases may be *inverted* to produce semantically coherent phrases in English, 
    
    - emit on
    - now god
    - not a ton 
    
    Note the last item in this list is an example of what this work has termed a Perfect Palindrome. These examples were specially chosen to highlight the connection that exists between the class of Perfect Palindromes and the class of Invertible Sentences. It appears, based on this brief and circumstantial analysis, that Perfect Palindromes are a subset of a larger class of Sentences, namely, Invertible Sentences.
    
    Due to the definition of Sentences as semantic constructs and the definition of Invertible Sentences as Sentences whose Inverses belong to the Corpus, this means Invertible Sentences are exactly those Sentences that maintain *semantic coherence* (:ref:`Definition 2.2.1 <definition-2-2-1>`) and *admissibility* (:ref:`Definition 2.3.1 <definition-2-3-1>`) under inversion. In order for a Sentence to be Invertible it must possess symmetry on both the Character-level and the Word-level, while maintaining a semantic structure at the Sentence level that accomodates this symmetry. This connection between the symmetries in the different linguistic levels of an Invertible Sentence will be formalized and proven by the end of this subsection. The next series of theorems, :ref:`Theorems 2.3.7 <theorem-2-3-7>` - :ref:`2.3.8 <theorem-2-3-8>` are the preparatory foundation for establishing this symmetrry. 
    
    .. _theorem-2-3-7:
    
    **Theorem 2.3.7** :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} \in L`
    
    Let *ζ* be a Sentence from Corpus **C**:sub:`L`. Assume :math:`ζ \in K` . By :ref:`Definition 2.3.2 <definition-2-3-2>`,
    
    .. math::
    
        1. \quad \text{inv}(\zeta) \in C_L
    
    By the :ref:`Extraction Axiom S.2 <axiom-s2>`,
    
    .. math::
    
        2. \quad \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} \in L 
     
    Therefore, 
    
    .. math::
    
        3. \quad \zeta \in K \to \text{inv}(\zeta)\{i\} \in L 
    
    Since *ζ* was arbitrary, this can be generalized over the Corpus,
    
    .. math::
    
        4. \quad \forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} \in L 
    
    ∎
    
    The next theorem shows how the inversion "distributes" over the Words of a Delimited Sentence.
    
    .. _theorem-2-3-8:
    
    **Theorem 2.3.8** :math:`\forall \zeta \in C_L: \text{inv}(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
    
    Let *ζ* be an arbitrary sentence in **C**:sub:`L`. Let :math:`n = \Lambda(\zeta)`. By :ref:`Definition 2.1.4 <definition-2-1-4>`, this is the Word Length of *ζ*.  Let *s* denote the Delimitation of *ζ* as follows:
    
    .. math::
    
        1. \quad s = D\Pi_{i=1}^{n} \zeta\{i\} = (\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{n\})
    
    By :ref:`Theorem 1.2.5 <theorem-1-2-5>`, for any two Strings *u* and *t*, :math:`\text{inv}(ut) = \text{inv}(t)\text{inv}(u)`. Apply this property repeatedly to construct *inv(s)*,
    
    .. math::
    
        2. \quad \text{inv}(s) = \text{inv}((\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{n\}))
    
    Which reduces to,
    
    .. math::
    
        3. \quad \text{inv}(s) = (\text{inv}(\zeta\{n\}))(\text{inv}(\sigma))(\text{inv}(\zeta\{n-1\}))(\text{inv}(\sigma)) ... (\text{inv}(\zeta\{2\}))(\text{inv}(\sigma))(\text{inv}(\zeta\{1\}))
    
    Since *σ* is a single character, :math:`\text{inv}(\sigma) = \sigma`,
    
    .. math::
    
        4. \quad \text{inv}(s) = (\text{inv}(\zeta\{n\}))(\sigma)(\text{inv}(\zeta\{n-1\}))(\sigma) ... (\sigma)(\text{inv}(\zeta\{2\}))(\sigma)(\text{inv}(\zeta\{1\}))
    
    Note that the right-hand side now has the form of a Delimitation, but with the order of Words reversed and each Word inverted.
    
    Re-index the terms on the right-hand side to match the form of the Delimitation definition, :ref:`Definition 1.2.7 <definition-1-2-7>`. Let :math:`j = n - i + 1`. Then, as *i* goes from 1 to *n*, *j* goes from *n* to 1,
    
    .. math::
    
        5. \quad \text{inv}(s) = (\text{inv}(ζ\{j_n\}))(\sigma)(\text{inv}(\zeta\{j_{n-1}\}))(\sigma) ... (\sigma)(\text{inv}(\zeta\{j_2\}))(\sigma)(\text{inv}(\zeta\{j_1\}))
    
    Where *j*:sub:`i` is obtained by simply substituting :math:`j = n - i + 1`. Using :ref:`Definition 1.2.7 <definition-1-2-7>` of Delimitations, the right-hand side becomes,
    
    .. math::
    
        6. \quad \text{inv}(s) = D\Pi_{j=1}^{n} \text{inv}(\zeta\{n - j + 1\})
    
    Recall that :math:`s = D\Pi_{i=1}^{n} \zeta\{i\}`. Substitute this back into the equation and re-index the right-hand side for consistency to get,
    
    .. math::
    
        7. \quad \text{inv}(D\Pi_{i=1}^{n} \zeta\{i\}) = D\Pi_{i=1}^{n} \text{inv}(\zeta\{n - i + 1\})
    
    Since *ζ* was an arbitrary sentence, this can be generalized over the Corpus,
    
    .. math::
    
        8. \quad \forall \zeta \in C_L: \text{inv}(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\}) 
    
    ∎
    
    As noted in previous aside, the condition of Invertibility is strong. While the Inverse of every Sentence is defined in the domain of Strings, an Inverse Sentence does not necessarily belong to the Corpus of its uninverted form. Therefore, when a Sentence is Invertible, it will exhibit syntactical symmetries at not just the Character level, but also at the individual Word level. Before moving onto to the last batch of theorems in this section, a digression into their motivation is in order, as it will help highlight the interplay of syntactic symmetries that give rise to palindromes.
    
    Consider the Sentences from the English language, :math:`ᚠ = \text{"this is a test"}`, :math:`ᚢ = \text{"live on"}`, and :math:`ᚦ = \text{"step on no pets"}`. Their corresponding Character-level representations are given by,
    
    .. math::
    
        {\largeᚠ} = (\text{"t"}, \text{"h"}, \text{"i"}, \text{"s"}, \sigma, \text{"i"}, \text{"s"}, \sigma, \text{"a"}, \sigma, \text{"t"}, \text{"e"}, \text{"s"}, \text{"t"})
    
    .. math::
    
        {\largeᚢ} = (\text{"l"}, \text{"i"}, \text{"v"}, \text{"e"}, \sigma, \text{"o"}, \text{"n"})
    
    .. math::
    
        {\largeᚦ} = (\text{"s"}, \text{"t"}, \text{"e"}, \text{"p"}, \sigma, \text{"o"}, \text{"n"}, \sigma, \text{"n"}, \text{"o"}, \sigma, \text{"p"}, \text{"e"}, \text{"t"}, \text{"s"})
    
    The Character-level representation of their Inverses, would be,
    
    .. math::
    
        {\large\text{inv}(\largeᚠ)} = (\text{"t"}, \text{"s"}, \text{"e"}, \text{"t"}, \sigma, \text{"a"}, \sigma, \text{"s"}, \text{"i"}, \sigma, \text{"s"}, \text{"i"}, \text{"h"}, \text{"t"})
    
    .. math::
    
        {\large\text{inv}(ᚢ)} = (\text{"n"}, \text{"o"}, \sigma, \text{"e"}, \text{"v"}, \text{"i"}, \text{"l"})
    
    .. math::
    
        {\large\text{inv}(ᚦ)} = (\text{"s"}, \text{"t"}, \text{"e"}, \text{"p"}, \sigma, \text{"o"}, \text{"n"}, \sigma, \text{"n"}, \text{"o"}, \sigma, \text{"p"}, \text{"e"}, \text{"t"}, \text{"s"})
    
    In the case of *ᚠ*, *inv(ᚠ)* is not a Sentence in the Corpus, since none of the Words in it belong to the Language (English). Notice that the Delimiters (*σ*) still appear at the same indices in both *ᚠ* and *inv(ᚠ)*, just in reversed order. In *ᚠ*, the Delimiters are at indices 4, 7, and 9. In *inv(ᚠ)*, the Delimiters are at indices 9, 7, and 4 (counting from the ending of the reversed string). So, while the sequence of Delimiters is reversed, their positions relative to the beginning and end of the String remain the same. Since the :ref:`Delimiting Algorithm <algorithm-2>` identifies Words based on Delimiter positions, this means application of the algorithm to the reversed Character-level representation results in the same delimiting of the linguistic "*entities*" (Strings) which correspond to Words, but in reversed order and inverted.
    
    In the case of *ᚢ*, *inv(ᚢ)* belongs to the Corpus, since all of its Words belong to the Language (English), it has semantic coherence in *ᚢ*, and the inverted Sentence is admissible. This means *ᚢ* belongs to the class of Invertible Sentences in English. Take note, none of the Words that belong to *ᚢ* (or more precisely, to one of the ordered pairs of **W**:sub:`ᚢ`) belong to *inv(ᚢ)* (or more precisely, to one of the ordered pairs of **W**:sub:`inv(ᚢ)`). However, there does appear to be a relationship between the Words which appear in *ᚢ* and *inv(ᚢ)*, namely, they must be Invertible. The Word *"live"* inverts into *"evil"*, while *"on"* inverts into *"no"*. In other words, based on this preliminary heuristic analysis, if a Sentence is to be Invertible, the Words which belong to it must belong to the class of Invertible Words **I**.
    
    In the case of *ᚦ*, a similar situation is found. Each Word in *ᚦ* is Invertible and pairs with its Inverse Word in *inv(ᚦ)*, e.g. *"pets"* and *"step"* form an Invertible pair, etc. This means, for the same reasons as *ᚢ*, *ᚦ* belongs to the class of Invertible Sentences. However, there is a symmetry embodied in *ᚦ* over and above the pairing of its constituent Words into Invertible pairs. Not only is *inv(ᚦ)* a Sentence in the Corpus, but it's equal to *ᚦ* itself. Indeed, *ᚦ* belongs to a special class of English sentences: Palindromes. 
    
    Note, in order for the Sentence to invert, i.e. the case of *ᚢ* and *ᚦ*, the order of the Words in the inverted Sentences must be the reversed order of the inverted Words in the uninverted Sentence. In other words, the inversion defined on the String *"propagates"* up through the levels of the semantic hierarchy and manifests at each level in the form of a semantic inversion. This will be discussed in greater detail after the next theorems are established.
    
    These last theorems encapsulate these important properties of Invertible Sentences. When Palindromes are formally defined in the next section, these theorems will be used extensively to prove the main results of this work. 
    
    .. _theorem-2-3-9:
    
    **Theorem 2.3.9** :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta \in K \to \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})`
    
    Let *ζ* be an arbitrary Invertible Sentence in **C**:sub:`L` for *i* such that :math:`1 \leq i \leq \Lambda(\zeta)`. By :ref:`Definition 2.3.2 <definition-2-3-2>`, 
    
    .. math::
    
        1. \quad \text{inv}(\zeta) \in C_L.
    
    By the :ref:`Extraction Axiom S.2 <axiom-s2>`, 
    
    .. math::
    
        2. \quad \zeta\{i\} \in L. 
    
    By :ref:`Definition 1.3.2 <definition-1-3-2>`, a Word *α* is invertible if and only if both *α* and its inverse, *inv(α)*, are in **L**,
    
    .. math::
    
        3. \quad \alpha \in I \leftrightarrow \text{inv}(\alpha) \in L
    
    Therefore, since **L** is closed under inversion for Invertible Words , 
    
    .. math::
    
        4. \quad \text{inv}(\zeta\{i\}) \in L.
    
    *inv(ζ)* can be constructed by concatenating the inverses of the words in ζ in reverse order, with delimiters inserted appropriately. Since by step 1 *inv(ζ)* is a Sentence in the Corpus, **W**:sub:`inv(ζ)` can be constructed by the :ref:`Delimiting Algorithm <algorithm-2>` (:ref:`Definition 2.1.3 <definition-2-1-3>`). 
    
    .. math::
    
        5. \quad W_{\text{inv}(\zeta)} = (\text{inv}(\zeta\{\Lambda(\zeta)\}), \text{inv}(\zeta\{\Lambda(\zeta)-1\}), ..., \text{inv}(\zeta\{1\}))
    
    By :ref:`Definition 2.1.5 <definition-2-1-5>`, 
    
    .. math::
    
        6. \quad \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta)-i+1\})
    
    Since *ζ* and *i* were arbitrary, this can be generalized over the Corpus,
    
    .. math::
    
        1. f\quad \forall \zeta \in C_L: \zeta \in K \leftarrow \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\}) 
    
    ∎
    
    A brief interjection is necessary to discuss the significance of :ref:`Theorem 2.3.9 <theorem-2-3-9>`. The result shown in :ref:`Theorem 2.3.9 <theorem-2-3-9>` is a direct result of the *"propagation of inversion"* mentioned in the introduction to this subsection.
    
    As :ref:`Theorem 1.3.1 <theorem-1-3-1>` showed, :ref:`Definition 1.3.1 <definition-1-3-1>` of Reflective Words is equivalent to a definition that simply requires *α* satisfy the String equality relation, 
    
    .. math::
    
        \alpha = \text{inv}(\alpha)
    
    Another way of stating this is through logical equivalence, as :ref:`Theorem 1.3.2 <theorem-1-3-2>` shows,
    
    .. math::
    
        \alpha \in L \leftrightarrow \text{inv}(\alpha) \in L
        
    In turn, :ref:`Definition 1.2.4 <definition-1-2-4>` of String Inversion states in order for this to be the case, it must also be the case its Character satisfy,
    
    .. math::
    
        \alpha[i] = \alpha[l(\alpha) - i + 1] 
    
    In other words, a Word is its own Inverse exactly when its Characters are in inverted orders. 
    
    In a similar fashion, as :ref:`Theorem 2.3.5 <theorem-2-3-5>` and :ref:`Theorem 2.3.6 <theorem-2-3-6>` demonstrate by way of syllogism, a Sentence in a Corpus is invertible if its Inverse belongs to the Corpus,
    
    .. math::
    
        \zeta \in C_L \leftrightarrow \text{inv}(\zeta) \in C_L
    
    :ref:`Theorem 2.3.9 <theorem-2-3-9>` *"propagates"* the Character-level symmetries up through the Words in the Sentence, by stating the Words in an invertible Sentence must be inverted Words of the Sentence in reversed order,
    
    .. math::
    
        \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
    
    An imporant note to make is the *direction* of the implication in :ref:`Theorem 2.3.9 <theorem-2-3-9>` . A bidirectional equivalence would allow one to infer from the above equation that a Sentence is invertible. However, the direction of :ref:`Theorem 2.3.9 <theorem-2-3-9>`  cannot be strengthened, as the following :ref:`Theorem 2.3.10 <theorem-2-3-10>` makes clear.
    
    :ref:`Theorem 2.3.10 <theorem-2-3-10>` also makes clear why :ref:`Definition 2.3.1 <definition-2-3-1>` of Admissible Sentence of Word Length *n* is essential to understanding invertibility. 
    
    .. _theorem-2-3-10:
    
    **Theorem 2.3.10** :math:`\forall \zeta \in C_L: \zeta \in K \leftrightarrow (\forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})) \land (\text{inv}(\zeta) \in A(\Lambda(\zeta)))`
    
    This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus :math:`C_L`, *ζ* is invertible if and only if Words are inverted order and its Inverse is admissible.
    
    (→) Let ζ be an arbitrary Invertible Sentence in :math:`C_L`,
    
    .. math::
    
        1. \quad \zeta \in K
    
    By :ref:`Theorem 2.3.9 <theorem-2-3-9>`, the *i*:sup:`th` Word of *inv(ζ)* is the inverse of the *(Λ(ζ) - i + 1)*:sup:`th` Word of *ζ*
    
    .. math::
    
        2. \quad \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
       
    Furthermore, by :ref:`Theorem 2.3.3 <theorem-2-3-3>`, since *inv(ζ)* is in the Corpus, *inv(ζ)* is an Admissible Sentence of word length *Λ(ζ)*.
    
    .. math::
    
        3. \quad \zeta \in A(\Lambda(\zeta))
    
    Since :math:`\zeta \in K`, by :ref:`Definition 2.3.2 <definition-2-3-2>`, 
    
    .. math::
    
        4. \quad \text{inv}(\zeta) \in C_L.
    
    By :ref:`Theorem 2.3.8 <theorem-2-3-8>`, the inverse of *ζ*, *inv(ζ)*, can be expressed as the Delimitation of the inverses of the Words of *ζ* in reverse order,
    
    .. math::
    
        5. \quad \text{inv}(\zeta) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
    
    This is equivalent to,
    
    .. math::
    
        6. \quad \text{inv}(\zeta) = D\Pi_{i=1}^{\Lambda(\zeta)} \text{inv}(\zeta)\{i\}
    
    Since :math:`\text{inv}(\zeta) \in C_L` by assumption (step 1) and *inv(ζ)* has the same Word Length as *ζ* which is *Λ(ζ)*. 
    
    Because *inv(ζ)* is a Delimitation of Words from **L**, by :ref:`Definition 2.3.1 <definition-2-3-1>`, it follows that,
    
    .. math::
    
        7. \quad \text{inv}(\zeta) \in A(\Lambda(\zeta)).
    
    Therefore, both conditions hold, 
    
    .. math::
    
        8. \quad \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
        
    .. math::
    
        9. \quad \text{inv}(\zeta) \in A(\Lambda(\zeta))
    
    (←) Assume that for an arbitrary Sentence :math:`\zeta \in C_L`, the following holds,
    
    .. math::
    
        10. \quad \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
        
    .. math::
    
        11. \quad \text{inv}(\zeta) \in A(\Lambda(\zeta))
    
    
    By :ref:`Definition 2.3.1 <definition-2-3-1>`, since :math:`\text{inv}(\zeta) \in A(\Lambda(\zeta))`, it follows immediately, 
    
    .. math::
    
        12. \quad \text{inv}(\zeta) \in C_L
    
    By :ref:`Definition 2.3.2 <definition-2-3-2>`, it follows, 
    
    .. math::
    
        13. \quad \zeta \in K
    
    Therefore, both directions of the equivalence have been shown. Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus, 
    
    .. math::
    
        14. \quad \forall \zeta \in C_L: \zeta \in K \leftrightarrow (\forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})) \land (\text{inv}(\zeta) \in A(\Lambda(\zeta)))
    
    ∎
    
    Just as the notion of Word Length introduced a dimension of *"semanticality"* to the formal system, so too does the notion of an Admissible Sentence introduce a dimension of *"grammaticality"*. :ref:`Theorem 2.3.10 <theorem-2-3-10>` takes no stance on what constitutes an Admissible Sentence, what sort of grammatical forms and structures might define this notion, except to say it must be the result of a Delimitation of Words that belongs to the Corpus. 
    
    The significance of :ref:`Theorem 2.3.10 <theorem-2-3-10>` is the additional syntactical constraint that is imposed over and above *admissibility* onto a Corpus when a Sentence under goes inversion. Not only must the Inverse Sentence possess *admissibility*, the pre-cursor to *grammaticality*, but it must also display Word-level symmetry. This is definitively confirmed by :ref:`Theorem 2.3.11 <theorem-2-3-11>`.
    
    .. _theorem-2-3-11:
    
    **Theorem 2.3.11** :math:`\forall \zeta \in C_L: \zeta \in K \to \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I`
    
    This theorem can be stated in natural language as follows: For every Invertible Sentence *ζ* in the Corpus **C**:sub:`L`, every Word in *ζ* is an Invertible Word.
    
    Let *ζ* be an arbitrary Invertible Sentence in :math:`C_L`, and let *i* be a natural number such that :math:`1 \leq i \leq \Lambda(\zeta)`. Since :math:`\zeta \in K`, by :ref:`Definition 2.3.2 <definition-2-3-2>`, 
    
    .. math::
    
        1. \quad \text{inv}(\zeta) \in C_L
    
    By :ref:`Definition 2.1.5 <definition-2-1-5>`, *ζ{i}* refers to the Word at index *i* in the Word-level representation of *ζ*. By :ref:`Theorem 2.3.9 <theorem-2-3-9>`,
    
    .. math:: 
    
        2. \quad \forall i \in N_{\Lambda(\zeta)}: \text{inv}(\zeta)\{i\} = \text{inv}(\zeta\{\Lambda(\zeta) - i + 1\})
    
    By the :ref:`Extraction Axiom S.2 <axiom-s2>`, since :math:`\zeta \in C_L`, all Words in its Word-level representation belong to **L**. Therefore, :math:`\zeta\{i\} \in L` for all *i* such that :math:`1 \leq i \leq \Lambda(\zeta)`.
    
    Since :math:`\text{inv}(\zeta) \in C_L` (from step 1) and each word *inv(ζ){i}* is the inverse of a word in ζ (from step 2), by :ref:`Extraction Axiom S.2 <axiom-s2>`, all the Words in the Word-level representation of *inv(ζ)* belong to L,
    
    .. math::
    
        3. \quad \text{inv}(\zeta)\{i\} \in L
    
    By :ref:`Definition 1.3.2 <definition-1-3-2>` of Invertible Words, this means that *ζ{i}* is an Invertible Word. Therefore, :math:`\zeta\{i\} \in I`. Since *ζ* and *i* were arbitrary, this can generalize, 
    
    .. math::
    
        4. \quad \forall \zeta \in C_L: \zeta \in K \leftrightarrow \forall i \in N_{\Lambda(\zeta)}`: \zeta\{i\} \in I 
     
    ∎
    
    The contrapositive of :ref:`Theorem 2.3.11 <theorem-2-3-11>` provides a schema for searching for Invertible Sentences. If any of Words in a Sentence are not Invertible, then the Sentence is not Invertible. In other words, it suffices to find a single word in a Sentence that is not Invertible to show the entire Sentence is not Invertible.

.. _04structures:
 
-----------------
04_structures.rst
-----------------

.. raw:: 

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
    
    .. _section-iii-i:
    
    Section III.I: σ-Reductions 
    ---------------------------
    
    The mathematical definition of Palindromes (:ref:`Definition 4.1.1 <definition-4-1-1>` in the next section) will revolve around a novel linguistic operation, termed a *σ*-reduction. This operation will allow the semantic content of a Palindrome to be projected onto an Alphabet that preserves the order of its Characters under String Inversion, allowing for a precise specification of palindromic inversion in an Alphabet where symmetry is preserved.
    
    .. _reduction-definitions:
    
    Definitions
    ^^^^^^^^^^^
    
    Before defining a *σ*-reduction, the preliminary concept of a *σ-reduced Alphabet* must be introduced. The following definition serves as the basis for constructing the operation of *σ*-reduction.
    
    As has been seen with examples of Imperfect Palindromes like *"borrow or rob"*, a palindromic structure can have its Delimiter Character scrambled in the inversion of its form, i.e. *"bor ro worrob"*, making it lose semantic coherence. Imperfect Palindromes must be rearranged Delimter-wise to retrieve the original form of the Sentence. However, String Inversion preserves the relative order of the non-Delimiter Characters in a palindromic String, so the process of reconstitution is only a matter of resorting the Delimiter characters. This invariance of the Character order, while the Word order is scrambled by Delimiters, suggests palindromes might be more easily defined without the obstacle of the Delimiter.
    
    .. _definition-3-1-1:
    
    **Definition 3.1.1: σ-Reduced Alphabet**
    
    A *σ-reduced Alphabet* is an Alphabet Σ that has had its Delimiter character removed, so that it only consists of non-Delimiter characters. A *σ*-reduced Alphabet is denoted Σ:sub:`σ`. Formally,
    
    .. math::
    
        \Sigma_\sigma = \Sigma - \{ \sigma \} 
        
    ∎
    
    In order to define palindromes in all of their varieties, perfect or imperfect, the semantic incoherence that is introduced by the inversion of Imperfect Palindromes must be removed. This is accomplished through the introduction of the operation of *σ-reduction*.
    
    .. _definition-3-1-2:
    
    **Definition 3.1.2: σ-Reduction**
    
    Let *t* be a String with length *l(t)* and Character-level representation 
    
    .. math::
    
        1. \quad T = \{ (1,\mathfrak{a}_1) , (2, \mathfrak{a}_2) , ... , (l(t), \mathfrak{a}_{l(t)}) \} 
        
    .. math::
    
        2. \quad \mathfrak{a}_i \in \Sigma.
    
    The *σ*-reduction of *t*, denoted by the lowercase Greek final Sigma, *ς(t)*, maps the String *t* to a new String *u* in the *σ*-reduced alphabet **Σ**:sub:`σ` by removing all occurrences of the Delimiter Character. Formally, *ς(t)* is defined and constructed using the :ref:`Reduction Algorithm <algorithm-3>`,
    
    .. _algorithm-3:
    
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
        
        6. Return t 
    
    ∎
    
    Note the String *s* which is initialized to hold the *σ*-reduced String is set equal to the value of the Empty Character. The conditional application of the Basis Clause of Concatenation in step 1 of the Finalization Block ensures this Character is removed from the output of the :ref:`Reduction Algorithm <algorithm-3>`, if the input string contained at least one non-Empty Character. Otherwise, the :ref:`Reduction Algorithm <algorithm-3>` returns an Empty Character. From this, it is clear if a String only contains Delimiters,
    
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
    
    A subtlety of the :ref:`Reduction Algorithm <algorithm-3>` should be noted. While :math:`\varsigma(\sigma) = \varepsilon` and :math:`\varsigma(\alpha) = \alpha`, it does not follow the *σ*-reduction of a Word concatenated with the Delimiter is the concatenation of that Word with the Empty Character. In other words, the following holds,
    
    .. math::
    
        \varsigma(\alpha\sigma) ≠ \alpha\varepsilon
    
    Except insofar that the Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>` defines the concatenation of *αε* to equal *α*.
    
    This is because of the condition *(j > 1)* in the Finalization Block of the Reduction ensures Empty Characters are stripped from *t* when the input String contains atleast one non-Empty Character that has been concatenated into the *σ*-reduction String. 
    
    The more complicated properties of *σ*-reductions are proved in the theorems that follow. Before moving onto the proofs, the following example shows how to apply the :ref:`Reduction Algorithm <algorithm-3>` to construct the *σ*-reduction of a String.
    
    **Example**
    
    Let *s = "a b c"* be a String from the Alphabet 
    
    .. math::
    
        \Sigma = \{ \text{""}, \text{" "} , \text{"a"}, \text{"b"}, \text{"c"} \} 
        
    Note in this example :math:`\sigma = \text{" "}` and :math:`l(s) = 5`. The value of the variables in the :ref:`Reduction Algorithm <algorithm-3>` after each iteration are given below,
    
    .. math::
    
        1. \quad i = 2, t = \varepsilon\text{"a"}
    
    .. math::
    
        2. \quad i = 3, t = \varepsilon\text{"a"}
    
    .. math::
    
        3. \quad i = 4, t = \varepsilon\text{"ab"}
        
    .. math::
    
        4. \quad i = 5, t = \varepsilon\text{"ab"}
        
    .. math::
    
        5. \quad i = 5, t = \text{"abc"}
            
    The result of the *σ*-reduction of *s* is thus given by,
    
    .. math::
    
        6. \quad \varsigma(s) = \text{"abc"} 
        
    ∎
    
    A *σ*-reduction can be thought of as a linguistic operation analogous to vector projection. While not a strict mathematical equivalence, this conception of *σ*-reduction captures the idea of transforming a String from its original form (with Delimiters) onto a reduced space (without Delimiters), similar to how a vector can be projected onto a subspace.
    
    The *σ*-reduced Alphabet (**Σ**:sub:`σ`) can be seen as a subspace within this higher-dimensional space, consisting of only the non-Delimiter dimensions. The sigma reduction function (*ς(s)*) acts as a projection operator, mapping the String onto this subspace by eliminating the components corresponding to the Delimiter character (*σ*).
    
    Note that a *σ*-reduction is not a one-to-one operation. It is possible for the *σ*-reduction of a palindrome to map onto a totally different sentence, not necessarily a palindrome.
    
    As an example, consider the (partial, ignoring punctuality) Palindromes :math:`ᚠ = \text{"madam im adam"}` and :math:`ᚢ = \text{"mad am i madam"}`. The *σ*-reduction of both of these Sentences would map to the *σ-reduced* value of *"madamimadam"*.
    
    Both the Palindrome and the alternative Sentence (which also happens to be a Palindrome) have the same *σ*-reduction, despite having different meanings and grammatical structures. This highlights the ambiguity that can arise from removing spaces, as the original Word boundaries and Sentence structure are lost.
    
    .. _reduction-theorems:
    
    Theorems 
    ^^^^^^^^
    
    The following theorems establish the basic properties of *σ*-reductions. 
    
    .. _theorem-3-1-1:
    
    **Theorem 3.1.1** :math:`\forall \zeta \in C_L: \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta))`
    
    Let *ζ* be an arbitrary sentence in C:sub:`L`. Let *s* be the *σ*-reduction of *ζ*,
    
    .. math::
    
        1. \quad s = \varsigma(\zeta)
    
    Let *t* be the Inverse of *s*,
    
    .. math::
    
        2. \quad t = \text{inv}(s).
    
    Let *u* be the Inverse of *ζ*,
    
    .. math::
    
        3. \quad u = \text{inv}(ζ). 
        
    Let *v* be the *σ*-reduction of *u*,
    
    .. math::
    
        4. \quad v = \varsigma(u) = \varsigma(\text{inv}(ζ)) 
    
    Since *s* contains only the non-Delimiter characters of *ζ* in their original order, and *t* is the reversed sequence of Characters in *s*, *t* contains only the non-Delimiter characters of *ζ* in reversed order.
    
    Similarly, since *u* is the reverse sequence of Characters in *ζ*, and *v* is obtained by removing Delimiters from *u*, *v* also contains only the non-Delimiter characters of *ζ* in the reversed order.
    
    Therefore, by :ref:`Definition 1.1.4 <definition-1-1-4>`, *t* and *v* must be the same String, as they both contain the same Characters in the same order. Since :math:`t = v`, 
    
    .. math::
    
        5. \quad \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta))
    
    Since ζ was an arbitrary Sentence, this can be generalized over the Corpus
    
    .. math::
    
        6. \quad \forall \zeta \in C_L: \text{inv}(\varsigma(\zeta)) = \varsigma(\text{inv}(\zeta)) 
    
    ∎
    
    :ref:`Theorem 3.1.1 <theorem-3-1-1>` is essential because it allows free movement between the Inverse of a *σ*-reduction and the *σ*-reduction of an Inverse. In other words, :ref:`Theorem 3.1.1 <theorem-3-1-1>` establishes the commutativity of *σ*-reduction over inversion and visa versa. 
    
    As the theorems in this section will make clear, there exists a unique type of algebraic structure that links the operations of *σ*-reduction, inversion and concatenation. The properties of this algebraic structure will be necessary for establishing many of the results regarding palindromes.
    
    The next theorem demonstrates how *σ*-reduction interacts with concatenation.
    
    .. _theorem-3-1-2:
    
    **Theorem 3.1.2** :math:`\forall \zeta, \xi \in C_L: \varsigma(\zeta\xi) = (\varsigma(\zeta)\varsigma(\xi))`
    
    Let *ζ* and *ξ* be arbitrary sentences in :math:`C_L`. Let **Ζ** and **Ξ** be the character-level representations of *ζ* and *ξ*, respectively,
    
    .. math::
    
        1. \quad \Zeta = (\iota_1, \iota_2, ..., \iota_{l(\zeta)})
    
    .. math::
    
        2. \quad \Xi = (\nu_1, \nu_2, ..., \nu_{l(\xi)})
    
    Let *ζξ* be the concatenation of *ζ* and *ξ*. The character-level representation of *ζξ* is given by,
    
    .. math::
    
        3. \quad \Zeta\Xi = (\iota_1, \iota_2, ..., \iota_{l(\zeta)}, \nu_1, \nu_2, ..., \nu_{l(\xi)})
    
    Let *s* be the σ-reduction of *ζξ*. Let *t* be the *σ*-reduction of *ζ*. Let *u* be the *σ*-reduction of *ζξ*,
    
    .. math::
    
        4. \quad s = \varsigma(\zeta\xi)
        
    .. math::
    
        5. \quad t = \varsigma(\zeta)
        
    .. math::
    
        6. \quad u = \varsigma(\xi)
    
    Let *v* be the concatenation of the Strings *t* and *u*,
    
    .. math::
    
        7. \quad v = tu = (\varsigma(\zeta))(\varsigma(\xi))
    
    Since *σ*-reduction only removes Delimiters and doesn't change the order of non-Delimiter Characters, the non-Delimiter characters in *s* (the *σ*-reduction of *ζξ*) are the same as the non-Delimiter Characters in *ζ* followed by the non-Delimiter Characters in ξ.
    
    The non-Delimiter characters in *v*, the concatenation of *ς(ζ)* and *ς(ξ)*, are also the non-Delimiter characters in *ζ* followed by the non-delimiter characters in *ξ*.
    
    Therefore, by :ref:`Definition 1.1.4 <definition-1-1-4>`, *s* and *v* must be the same String, as they both contain the same Characters in the same order (the non-Delimiter Characters of *ζ* followed by the non-Delimiter characters of *ξ*). Since :math:`s = v`, 
    
    .. math::
    
        8. \quad \varsigma(\zeta\xi) = (\varsigma(\zeta))(\varsigma(\xi))
    
    Since ζ and ξ were arbitrary Sentence, this can be generalized over the Corpus,
    
    .. math::
    
        9. \quad \forall \zeta, \xi \in C_L: \varsigma(\zeta\xi) = (\varsigma(\zeta))(\varsigma(\xi)) 
    
    ∎
    
    :ref:`Theorem 3.1.2 <theorem-3-1-2>` further demonstrates the *algebraic* nature of *σ*-reduction and the other String operations. It shows that *σ*-reduction *distributes* over concatenation, just as inversion "distributes" (in a reversed way) over concatenation (:ref:`Theorem 1.2.5 <theorem-1-2-5>`). These properties suggest that *σ*-reduction, inversion and concatenation are not just arbitrary operations but instead are deeply connected to the underlying structure of Strings and Sentences.
    
    As another example of this *"linguistic algebraic structure"*, the following theorem might be termed the *"Idempotency of σ-reduction"* or the *"σ-reduction Idempotence Property"*.
    
    .. _theorem-3-1-3:
    
    **Theorem 3.1.3** :math:`\forall \zeta \in C_L: \varsigma(\varsigma(\zeta)) = \varsigma(\zeta)`
    
    Let *ζ* be an arbitrary Sentence in :math:`C_L`. Let s be the *σ*-reduction of *ζ*,
    
    .. math::
    
        1. \quad s = \varsigma(\zeta)
    
    Let *t* be the *σ*-reduction of *s*,
    
    .. math::
    
        2. \quad t = \varsigma(s) = \varsigma(\varsigma(\zeta))
    
    Since *s* is the result of applying a *σ*-reduction to *ζ*, it contains no Delimiter Characters (*σ*).
    
    When *s* is *σ*-reduced (to get *t*), the :ref:`Reduction Algorithm <algorithm-3>` in :ref:`Definition 3.1.2 <definition-3-1-2>` iterates through the Characters of *s*. Since s has no Delimiters, the condition if :math:`s[i] \neq \sigma` in the algorithm will always be true, and every character of *s* will be concatenated to the initially empty string *t*. Therefore, by :ref:`Definition 1.1.4 <definition-1-1-4>`, *t* will be identical to *s*, as it contains the same Characters in the same order. Thus,
    
    .. math::
    
        3. \quad \varsigma(\varsigma(\zeta)) = \varsigma(\zeta)
    
    Since ζ was an arbitrary Sentence, this can be generalized over the Corpus,
    
    .. math::
    
        4. \quad \forall \zeta \in C_L: \varsigma(\varsigma(\zeta)) = \varsigma(\zeta) 
    
    ∎
    
    .. _theorem-3-1-4:
    
    **Theorem 3.1.4** :math:`\forall \zeta \in C_L: \Lambda(\varsigma(\zeta)) \leq 1`
    
    Let *ζ* be an arbitrary Sentence in :math:`C_L`. By the :ref:`Duality Axiom S.1 <axiom-s1>`, every Sentence in :math:`C_L` must contain at least one word from **L**. 
    
    .. math::
    
        1. \quad \exists \alpha \in L: \alpha \subset_s \zeta
    
    By :ref:`Definition 3.1.2 <definition-3-1-2>`, *ς(ζ)* removes all Delimiters from *ζ*. Therefore, *ς(ζ)* consists of the Characters of the words in *ζ* concatenated together without any delimiters.
    
    By the :ref:`Discovery Axiom W.1 <axiom-w1>`, Words in **L** cannot contain Delimiters.
    
    By :ref:`Definition 2.1.4 <definition-2-1-4>`, the Word Length *Λ(s)* of a String *s* counts the number of Words in *s*, where Words are separated by Delimiters.
    
    If *ζ* contains only one Word, then *ς(ζ)* will be that Word,
    
    .. math::
    
        2. \quad \Lambda(\varsigma(\zeta)) = 1
    
    If *ζ* contains multiple Words, then *ς(ζ)* will be a concatenation of those words without Delimiters. This concatenated String may or may not be a valid Word in **L**.
    
    If the concatenated String is a valid Word in **L**, then,
    
    .. math::
    
        3. \quad \Lambda(\varsigma(\zeta)) = 1
    
    If the concatenated String is not a valid Word in **L**, then,
    
    .. math::
    
        4. \quad \Lambda(\varsigma(\zeta)) = 0
    
    Therefore, in all possible cases,
    
    .. math::
    
        5. \quad \Lambda(\varsigma(\zeta)) \leq 1
    
    Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,
    
    .. math::
    
        6. \quad \forall \zeta \in C_L: \Lambda(\varsigma(\zeta)) \leq 1 
    
    ∎
    
    .. _theorem-3-1-5:
    
    **Theorem 3.1.5** :math:`\forall u, t \in S: u \subset_s t \leftrightarrow \varsigma(u) \subset_s \varsigma(t)`
    
    This theorem can be stated in natural language as follows: For any two Strings *u* and *t*, *u* is contained in *t* if and only if the *σ*-reduction of *u* is contained in the *σ*-reduction of *t*.
    
    Let *u* and *t* be arbitrary strings in **S**.
    
    (→) Assume 
    
    .. math::
    
        1. \quad u \subset_s t
    
    By Definition 1.1.7, there exists a strictly increasing and consecutive function :math:`f: N_{l(u)} \to N_{l(t)}` such that,
    
    .. math::
    
        2. \quad \forall i \in N_{l(u)}: u[i] = t[f(i)]
    
    Let 
    
    .. math::
    
        3. \quad s = \varsigma(u) 
        
    .. math::
    
        4. \quad v = \varsigma(t).
    
    By the :ref:`Definition 3.1.2 <definition-3-1-2>` of *σ*-reduction, *s* is obtained by removing all Delimiters from *u*, and *v* is obtained by removing all Delimiters from *t*.
    
    Since *u* is contained in *t*, the non-Delimiter Characters of *u* appear in *t* in the same order. The function *f* maps the indices of these Characters.
    
    Define a function :math:`g: N_{l(s)} \to N_{l(v)}` that maps the indices of *s* to the indices of *v*. In other words, if *i* is an index in *s*, then *g(i)* is the index in *v* that corresponds to the same non-Delimiter character.
    
    Since *f* is strictly increasing and consecutive, and *σ*-reduction only removes Delimiters, *g* will also be strictly increasing and consecutive. (*g* essentially compresses the mapping of *f* by skipping over the Delimiter indices and offseting).
    
    For any index *i* in *s*, 
    
    .. math::
    
        5. \quad s[i] = u[j] 
        
    for some *j*. Moreover, 
    
    .. math::
    
        6. \quad u[j] = t[f(j)]. 
        
    Since *s* and *v* are *σ*-reduced, *s[i]* and *v[g(i)]* correspond to the same non-Delimiter Character, and g(i) is constructed such that 
    
    .. math::
    
        7. \quad v[g(i)] = t[f(j)]. 
        
    Therefore, 
    
    .. math::
    
        8. \quad s[i] = v[g(i)].
    
    Since *g* is a strictly increasing and consecutive function and :math:`s[i] = v[g(i)]`, by :ref:`Definition 1.1.7 <definition-1-1-7>`, 
    
    .. math::
    
        9. \quad s \subset_s v
        
    From which it follows,
    
    .. math::
    
        10. \quad \varsigma(u) \subset_s \varsigma(t).
    
    (←) Assume 
    
    .. math::
    
        1. \quad \varsigma(u) \subset_s \varsigma(t).
    
    By :ref:`Definition 1.1.7 <definition-1-1-7>`, there exists a strictly increasing and consecutive function :math:`g: N_{l(\varsigma(u))} \to N_{l(\varsigma(t))}` such that:
    
    .. math::
    
        2. \quad \forall i \in N_{l(\varsigma(u))}: \varsigma(u)[i] = \varsigma(t)[g(i)]
    
    Define a function :math:`f: N_{l(u)} \to N_{l(t)}` that maps the indices of *u* to the indices of *t* by essentially "re-inserting" the delimiters. For each non-Delimiter character in *u* (and corresponding index in *ς(u)*), *f* will map to the corresponding index in *t*. For Delimiter characters in *u*, *f* will map to an index in *t* that preserves the order and consecutiveness.
    
    Since *g* is strictly increasing and consecutive, and the Delimiters are only removed, not reordered, the function *f* will also be strictly increasing and consecutive.
    
    For each index *i* in *u*, *u[i]* will either be a non-Delimiter or a Delimiter Character.
    
    If *u[i]* is a non-Delimiter character, it corresponds to a Character in *ς(u)*, and by the properties of *g* and *f*, the following holds for some *j*,
    
    .. math::
    
        3. \quad u[i] = \varsigma(u)[j] = \varsigma(t)[g(j)] = t[f(i)] 
    
    If *u[i]* is a Delimiter, then by the construction of *f*, it will be mapped to a corresponding Delimiter in *t*, so 
    
    .. math::
    
        4. \quad  u[i] = t[f(i)]
    
    Since *f* is a strictly increasing and consecutive function and :math:`u[i] = t[f(i)]` for all :math:`i \in N_{l(u)}`, by :ref:`Definition 1.1.7 <definition-1-1-7>`,
    
    .. math::
    
        5. \quad u \subset_s t
    
    Since both directions of the implication hold, it can be concluded,
    
    .. math::
    
        6. \quad \forall u, t \in S : u \subset_S t \leftrightarrow \varsigma(u) \subset_s \varsigma(t) 
    
    ∎
    
    During a *σ*-reduction, :ref:`Theorem 3.1.4 <theorem-3-1-4>` demonstrates information is lost with respect to the following semantic categories,
    
      - Word Boundaries: The spaces between words, which are crucial for parsing and understanding the sentence, are eliminated.
      - Sentence Structure: The grammatical structure of the sentence, the relationships between words and phrases, becomes ambiguous.
      - Prosody and Rhythm: The pauses and intonation that contribute to the meaning and expression of the sentence are lost.
    
    However, some semantic information is preserved. The individual words themselves, or at least their character sequences, remain present in the *σ-reduced* string. The next theorem proves semantic content is retained during the *σ*-reduction of a Sentence.
    
    .. _theorem-3-1-6:
    
    **Theorem 3.1.6** :math:`\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \subset_s \varsigma(\zeta)`
    
    This theorem can be stated in natural language as follows: For every sentence *ζ* in the Corpus :math:`C_L`, and for every Word *ζ{i}* in the Word-level representation of *ζ*, *ζ{i}* is contained in *ς(ζ)*.
    
    Let *ζ* be an arbitrary sentence in :math:`C_L`. By :ref:`Theorem 2.2.4 <theorem-2-2-4>`, it is known at least one Word must exist in *ζ*. Let *ζ{i}* be one of the Words in the sequence of Words that form *ζ*. 
    
    This means that *ζ* can be written as either, in the case of :math:`\Lambda(\zeta) > 1`, 
    
    .. math::
    
        1. \quad \text{Case} (\Lambda(\zeta) > 1): \zeta = (s_1)(\sigma)(\zeta\{i\})(\sigma)(s_2)
        
    where *s*:sub:`1` and *s*:sub:`2` are (possibly Empty) Strings. 
    
    In the case that Λ(ζ) = 1, then, this means *ζ* can be written simply as, 
    
    .. math::
    
        2. \quad \text{Case} (\Lambda(\zeta) = 1): \zeta = \zeta\{1\}
    
    By the :ref:`Definition 3.1.2 <definition-3-1-2>`, *ς(ζ)* is obtained by removing all Delimiters from *ζ*. Furthermore, by :ref:`Theorem 3.1.2 <theorem-3-1-2>`, *σ*-reduction distributes over concatenation. Thus,
    
    .. math::
    
        3. \quad \text{Case} (\Lambda(\zeta) > 1): \varsigma(\zeta) = (\varsigma(s_1))(\varsigma(\zeta\{i\}))(\varsigma(s_2))
    
    .. math::
    
        4. \quad \text{Case} (\Lambda(\zeta) = 1): \varsigma(\zeta\{1\})
    
    By the :ref:`Discovery Axiom W.1 <axiom-w1>`, Words in **L** do not contain Delimiters.
    
    .. math::
    
        5. \quad \text{Case} (\Lambda(\zeta) > 1): \varsigma(\zeta) = (\varsigma(s_1))(\zeta\{i\})(\varsigma(s_2))
        
    .. math::
    
        6. \quad \text{Case} (\Lambda(\zeta) = 1): \varsigma(\zeta\{1\}) = \zeta\{1\}
    
    Therefore, by :ref:`Definition 1.1.7 <definition-1-1-7>` of Containment,
    
    .. math::
    
        7. \quad \text{Case} (\Lambda(\zeta) > 1): \zeta\{i\} \subset_s \varsigma(\zeta)
        
    .. math::
    
        8. \quad \text{Case} (\Lambda(\zeta) = 1): \zeta\{1\} \subset_s \varsigma(\zeta) 
    
    In both cases, there is a Word in *ζ* that is contained in the *σ*-reduction of *ζ*. Since *ζ* was arbitrary, this can generalize over the Corpus,
    
    .. math::
    
        9. \quad\forall \zeta \in C_L: \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \subset_s \varsigma(\zeta) 
    
    ∎
    
    This next theorem shows how *σ*-reduction behaves over the class of Invertible Sentences, an extremely important class for understanding the mechanics of Palindromes.
    
    .. _theorem-3-1-7:
    
    **Theorem 3.1.7** :math:`\forall \zeta \in K: \varsigma = \text{inv}(\text{inv}(\varsigma(\zeta)))` 
    
    In natural language, this theorem can be stated in natural language as follows: If a Sentence in a Corpus is Invertible, then its invertibility is invariant under *σ*-reduction.
    
    Assume 
    
    .. math::
    
        1. \quad \zeta \in K
    
    In other words, assume that *ζ* is an Invertible Sentence. By :ref:`Theorem 2.3.11 <theorem-2-3-11>`, since *ζ* is invertible, all its Words are also Invertible,
     
     .. math::
    
        2. \quad \forall i \in N_{\Lambda(\zeta)}: \zeta\{i\} \in I
    
    The *σ*-reduction of *ζ*, *ς(ζ)*, is obtained by removing all Delimiters from ζ. Since no Word contains Delimiters (by :ref:`Discovery Axiom W.1 <axiom-w1>`), the *σ*-reduction concatenates the Words of *ζ*,
    
    .. math::
    
        2. \quad \varsigma(\zeta)= (\zeta\{1\})(\zeta\{2\})...(\zeta\{\Lambda(\zeta)\})
    
    Applying :ref:`Theorem 1.2.5 <theorem-1-2-5>` repeatedly,
    
    .. math::
    
        3. \quad \text{inv}(\varsigma(\zeta)) = \text{inv}((\zeta\{1\})(\zeta\{2\})...(\zeta\{\Lambda(\zeta)\}))
    
    To get,
    
    .. math::
    
        4. \quad \text{inv}(\varsigma(\zeta))  = (\text{inv}(\zeta\{\Lambda(ζ)\})) ... (\text{inv}(\zeta\{2\}))(\text{inv}((\ζ\{1\})))
    
    Applying a second Inversion,
    
    .. math::
    
        5. \quad \text{inv}(\text{inv}(\varsigma(\zeta))) = \text{inv}((\text{inv}(\zeta\{\Lambda(\zeta)\})) ... (\text{inv}(\zeta\{2\}))(\text{inv}((\zeta\{1\}))))
    
    Applying :ref:`Theorem 1.2.5 <theorem-1-2-5>` again,
    
    .. math::
    
        6. \quad \text{inv}(\text{inv}(\varsigma(\zeta))) = (\text{inv}(\text{inv}((\zeta\{1\})))) (\text{inv}(\text{inv}((\zeta\{2\})))) ... (\text{inv}(\text{inv}((\zeta\{\Lambda(\zeta)\}))))
    
    Finally, applying :ref:`Theorem 1.2.4 <theorem-1-2-4>` (:math:`\text{inv}(\text{inv}(s)) = s`)
    
    .. math::
    
        7. \quad \text{inv}(\text{inv}(\varsigma(\zeta))) = (\zeta\{1\})(\zeta\{2\})...(\zeta\{\Lambda(\zeta)\})
    
    Therefore, combining step 3 and step 8
    
    .. math::
        
        8. \quad \varsigma(\zeta) = \text{inv}(\text{inv}(\varsigma(\zeta)))
    
    Since *ζ* was an arbitrary Sentence in **K**, this can be generalized over Invertible Sentences,
    
    .. math::
    
        9. \quad \forall \zeta \in K: \varsigma(\zeta) = \text{inv}(\text{inv}(\varsigma(\zeta)))
    
    ∎
    
    The contrapositive of this theorem, much like the contrapositive of :ref:`Theorem 3.1.7 <theorem-3-1-7>`, provides a schema for searching the *σ-reduced* space for Invertible Sentences. The domain of this space reduces the complexity of searching for palindromic strings. Potential palindromic candidates can be projected into the *σ-reduced* spaced, and then filtered by those whose *σ*-reduction whose Inverse does not equal itself. 
    
    The final theorems in this section, :ref:`Theorems 3.1.8 <theorem-3-1-8>` - :ref:`3.1.9 <theorem-3-1-9>`, provide a method for constructing the *σ*-reduction of a Sentence through iterated concatenation. These theorems leverage the operations of Delimitation and Limitation introduced in :ref:`Definitions 1.2.7 <definition-1-2-7>` - :ref:`1.2.8 <definition-1-2-8>`.
    
    .. _theorem-3-1-8:
    
    **Theorem 3.1.8** :math:`\forall \zeta \in C_L: \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}`
    
    This theorem can be stated in natural language as follows: The *σ*-reduction of a Sentence is the Limitation of its Words.
    
    Assume *ζ* was an arbitrary Sentence such that,
    
    .. math::
    
        1. \quad \zeta \in C_L
    
    By :ref:`Definition 2.1.3 <definition-2-1-3>`, 
    
    .. math::
    
        2. \quad W_{\zeta} = (\alpha_1, \alpha_2, ..., \alpha_{\Lambda(\zeta)})
    
    Where,
    
    .. math::
    
        3. \quad \forall i \in N_{\Lambda(\zeta)}: \alpha_i \in L
    
    By :ref:`Theorem 2.3.4 <theorem-2-3-4>`, *ζ* can be expressed as the Delimitation of its Words:
    
    .. math::
    
        4. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\} = (\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{\Lambda(\zeta)\})
    
    By :ref:`Definition 3.1.2 <definition-3-1-2>`, *ς(ζ)* removes all Delimiters from *ζ*. Applying *σ*-reduction to the expression step 4,
    
    .. math::
    
        5. \quad \varsigma(\zeta) = \varsigma((\zeta\{1\})(\sigma)(\zeta\{2\})(\sigma) ... (\sigma)(\zeta\{\Lambda(\zeta)\}))
    
    By repeated application of :ref:`Theorem 3.1.2 <theorem-3-1-2>`, i.e. by distributing the *σ*-reduction over concatenation,
    
    .. math::
    
        6. \quad \varsigma(\zeta) = (\varsigma(\zeta\{1\}))(\varsigma(\sigma))(\varsigma(\zeta\{2\}))(\varsigma(\sigma)) ... (\varsigma(\sigma))(\varsigma(\zeta\{\Lambda(\zeta)\}))
    
    Since 
    
    .. math::
    
        7. \quad \varsigma(\sigma) = \varepsilon
    
    This can be rewritten with the Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>`,
    
    .. math::
    
        8. \quad \varsigma(\zeta) = (\varsigma(\zeta\{1\}))(\varsigma(\zeta\{2\}))...(\varsigma(\zeta\{\Lambda(\zeta)\}))
    
    By :ref:`Definition 3.1.2 <definition-3-1-2>` and the :ref:`Discovery Axiom W.1 <axiom-w1>`,
    
    .. math::
    
        9. \quad \forall i \in N_{\Lambda(\zeta)}: \varsigma(\zeta\{i\}) = \zeta\{i\}
    
    Therefore,
       
    .. math::
    
        10. \quad \varsigma(\zeta) = (\zeta\{1\})(\zeta\{2\})...(\zeta\{\Lambda(\zeta)\})
    
    By :ref:`Definition 1.2.8 <definition-1-2-8>`, the right-hand side is the Limitation of the words in :math:`W_{\zeta}`,
    
    .. math::
    
        11. \quad \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}
    
    Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,
    
    .. math::
    
        12. \quad \forall \zeta \in C_L: \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\} 
    
    ∎
    
    :ref:`Theorem 3.1.8 <theorem-3-1-8>` establishes an important formula for the construction of *σ*-reductions. The :ref:`Reduction Algorithm <algorithm-3>` targets Strings as input, i.e. it processes sequential Characters in a String. If an ordered sequence of Words is already at hand, without :ref:`Theorem 3.1.8 <theorem-3-1-8>`, it would be required to reconstruct the String which corresponds to the sequence and process it through the :ref:`Reduction Algorithm <algorithm-3>`. Rather than applying the :ref:`Reduction Algorithm <algorithm-3>` everytime a *σ*-reduction is required, :ref:`Theorem 3.1.8 <theorem-3-1-8>` provides a schema for the construction of *σ*-reductions through the process of Limitation.
    
    Compare :ref:`Theorem 3.1.8 <theorem-3-1-8>` to :ref:`Theorem 2.2.5 <theorem-2-2-5>`, reprinted below for reference,
    
    .. math::
    
        \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}
    
    In other words, taking the *σ*-reduction of a Sentence converts the Delimitation of its Words into a Limitation. This follows directly from :ref:`Definitions 1.2.7 <definition-1-2-7>` and :ref:`1.2.8 <definition-1-2-8>` of Limitation and Delimitation. The next theorem proves this relationship for the more general case of *any* ordered sequence of Words, not necessarily a semantically coherent and admissible Sentence.
    
    .. _theorem-3-1-9:
    
    **Theorem 3.1.9**  :math:`\forall n \in \mathbb{N}: \forall p \in X_L(n): \varsigma(D\Pi_{i=1}^{n} p(i)) = L\Pi_{i=1}^{n} p(i)`
    
    This theorem can be stated in natural language as follows: the *σ*-reduction of the Delimitation of a Phrase is equal to the Limitation of the same Phrase.
    
    Let *n* be an arbitrary natural number, and let *p* be an arbitrary Phrase from a Language's *n*:sup:`th` Lexicon, 
    
    .. math::
    
        1. \quad p \in Χ_L(n)
        
    .. math::
    
        2. \quad p = (\alpha_1, \alpha_2, ..., \alpha_n).
    
    By :ref:`Definition 1.2.7 <definition-1-2-7>`, 
    
    .. math::
    
        3. \quad D\Pi_{i=1}^{n} p(i) = (\alpha_1)(\sigma)(\alpha_2)(\sigma) ... (\sigma)(\alpha_n)
    
    Applying :ref:`Definition 3.1.2 <definition-3-1-2>` of *σ*-reduction to the Delimitation and applying the Basis Clause of :ref:`Definition 1.1.1 <definition-1-1-1>`,
    
    .. math::
    
        4. \quad \varsigma(D\Pi_{i=1}^{n} p(i)) = (\alpha_1)(\alpha_2) ... (\alpha_n)
    
    By :ref:`Definition 1.2.8 <definition-1-2-8>`,
    
    .. math::
    
        5. \quad L\Pi_{i=1}^{n} p(i) = (\alpha_1)(\alpha_2) ... (\alpha_n)
    
    By repeated application of :ref:`Theorem 1.1.1 <theorem-1-1-1>` to step 4,
    
    .. math::
    
        6. \quad l(\varsigma(D\Pi_{i=1}^{n} p(i))) = \sum_{i=1}^{n} l(\alpha_i)
    
    By repeated application of :ref:`Theorem 1.1.1 <theorem-1-1-1>` to step 5,
    
    .. math::
    
        7. \quad l((\alpha_1)(\alpha_2)... (\alpha_n)) = \sum_{i=1}^{n} l(\alpha_i)
    
    Comparing step 6 to step 7 and noting the *α*:sub:`i` is in the same position the same for all :math:`1 \leq i \leq n`, it follows by :ref:`Definition 1.1.4 <definition-1-1-4>` of String Equality, 
    
    .. math::
    
        8. \quad \varsigma(D\Pi_{i=1}^{n} p(i)) = L\Pi_{i=1}^{n} p(i)
    
    Since *n* and *p* were arbitrary, this can be generalized over the Lexicon,
    
    .. math::
    
        9. \quad \forall n \in \mathbb{N}: \forall p \in Χ_L(n): \varsigma(D\Pi_{i=1}^{n} p(i)) = L\Pi_{i=1}^{n} p(i) 
    
    ∎
    
    The relationship between *σ*-reductions, Limitations and Delimitations provides an easy method for establishing the relationship between the String Length of a Sentence and the String Length of its σ-reduced form. 
    
    .. _theorem-3-1-10:
    
    **Theorem 3.1.10** :math:`\forall \zeta \in C_L: l(\zeta) \geq l(\varsigma(\zeta))`
    
    Let ζ be an arbitrary Sentence in the Corpus. By :ref:`Theorem 3.1.8 <theorem-3-1-8>`,
    
    .. math::
    
        1. \quad \varsigma(\zeta) = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}
    
    By :ref:`Theorem 2.2.5 <theorem-2-2-5>`,
    
    .. math::
    
        2. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}
    
    Since the only different between :ref:`Definition 1.2.7 <definition-1-2-7>` and :ref:`1.2.8 <definition-1-2-8>` is that Delimitations insert a Delimiter while Limitations simply concatenate, it must follow,
    
    .. math::
    
        3. \quad l(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) \geq L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}
    
    From this, step 1 and step 2, it follows, 
    
    .. math::
    
        4. \quad l(\zeta) \geq l(\varsigma(\zeta))
    
    Since *ζ* was arbitary, this can be generalized over the Corpus,
    
    .. math::
    
        5. \quad \forall \zeta \in C_L: l(\zeta) \geq l(\varsigma(\zeta)) 
    
    ∎
    
    .. _section-iii-ii:
    
    Section III.II: Delimiter Count Function 
    ----------------------------------------
    
    Before moving onto the formal foundations for the *Delimiter Count Function*, some heuristical motivations will be provided for its introduction. The essence of a Palindrome lies in its ability to encode semantic meaning on multiple syntactic levels. In other words, the meaning of a Palindrome is distributed through its syntactical layers. The concepts of *Perfect* and *Imperfect* Palindromes are be defined more rigorously in Section III, but as an intuitive introduction to the ability of a Palindrome to encode meaning on multiple syntactic levels and as a justification for the introduction of the Delimiter Count Function, consider the following two examples,
    
        1. dennis sinned
        2. if i had a hifi
    
    The first palindrome "*dennis sinned*" is what will be termed a Perfect Palindrome in :ref:`Definition 4.1.2 <definition-4-1-2>`, because its inverse does not require a rearrangement of its constituent Characters to preserve its semantic content. However, the second Palindrome *"if i had a hifi"* is what is termed an Imperfect Palindrome in :ref:`Definition 4.1.3 <definition-4-1-3>`. To see the motivation behind this categorization, note the strict inversion of "If I had a hifi" would be (ignoring capitalization for now),
    
        ifih a dah i fi
    
    The order of the Characters in the Inverse of an Imperfect Palindrome is preserved, but in order to reconstitute its uninverted form, the Delimter Characters must be re-sorted. It appears, then, that Delimiters play a central role in organizing the palindromic structure. 
    
    The study of Delimiter Characters in a Sentence bears study beyond its application to palindromic structures, though. The following section of the Appendix introduces this function for quantifying the number of Delimiters in a sentence. Various properties about this function are then proved, in particular how the function interacts with other linguistic operations and functions that have been defined in the main body of the work. 
    
    Since every Sentence is a String, it will suffice to define the *Delimiter Count Function* over the set of all possible Strings **S**. The following definition will serve that purpose.
    
    .. _definition-3-2-1:
    
    **Definition 3.2.1: Delimiter Count Function** Let *t* be a String with length *l(t)*. Let **T** be the Character-level representation of *t* with the Characters *𝔞*:sub:`i` denoting the *i*:sup:`th` character of the String *t*, where :math:`1 \leq i \leq l(t)`,
    
    .. math::
    
        T = \{ (1, \mathfrak{a}_1), (2, \mathfrak{a}_2), ... , (l(t), \mathfrak{a}_{l(t)}) \}
    
    The Delimiter Count Function, denoted by *Δ(t)*, is defined as the number of Delimiter Characters (*σ*) in the string *t*. Formally, *Δ(t)* is defined as the cardinality of the set that satisfies the following formula:
    
    .. math::
    
        D_t \leftrightarrow \{ (i, \mathfrak{a}_i) \in T \mid \mathfrak{a}_i = \sigma \land 1 \leq i leq l(t) \} 
    
    Then, the Delimiter Count function is defined as
    
    .. math::
    
        \Delta(t) = \lvert D_t \rvert 
        
    ∎
    
    **Example** 
    
    Consider the string *t = "a b c"*. The Character-level set representation of *t* is given by,
        
    .. math::
    
        T = \{ (1, \text{"a"}), (2, \sigma), (3, \text{"b"}), (4, \sigma), (5, \text{"c"}) \}.
    
    By :ref:`Definition 3.2.1 <definition-3-2-1>`, the set :math:`D_t` contains the ordered pairs :math:`(2, \sigma)` and :math:`(4, \sigma)`, where the first coordinate of each pair correspond the positions of the two Delimiter Characters in the String. Therefore, 
        
    .. math::
    
        D_t = \{ (2, \sigma), (4, \sigma) \}
    
    From this it follows, 
    
    .. math::
    
        \lvert D_t \rvert = 2 
        
    Hence, 
        
    .. math::
    
        \Delta(t) = 2 
        
    ∎
    
    From the previous example, it can be seen the Delimiter Count function takes a Sentence as input and produces a non-negative integer (the Delimiter count) as output. Multiple sentences can have the same Delimiter count, making it a many-to-one function. While this many not be advantageous from a computational perspective, the Delimiter Count function has other interesting properties that make it worth studying. The following theorems describe some of its properties.
    
    .. _theorem-3-2-1:
    
    **Theorem 3.2.1** :math:`\forall \zeta \in C_L: \Lambda(\zeta) = \Delta(\zeta) + 1`
    
    .. note::
    
        I think this needs revised to be :math:`\Lambda(\zeta) \geq \Delta(\zeta) + 1` to account for edge cases where the sentence has multiple Delimiters in sequence, or has a Delimiter at the end or beginning of the String. 
        
        Alternatively, this inconsistency might be resolvable by introducing an assumption about the structure of a Sentence. Perhaps all Delimiters between two consecutive Words should be treated as a single Delimiter? Or an Axiom to constrain the placement of Delimiters in Sentences?
    
    In natural language, this theorem is stated: For any sentence *ζ* in a Corpus C:sub:`L`, the length of the Sentence is equal to its Delimiter count plus one.
    
    Assume :math:`ζ \in C_L`. Let *Δ(ζ)* be the delimiter count of *ζ*. Let **Ζ** be the Character-level representation of ζ. Let :math:`W_{\zeta}` be the word-level set representation of ζ. Recall :math:`W_{\zeta}` is formed by splitting **Ζ** at each Delimiter Character *σ* with the :ref:`Delimiting Algorithm <algorithm-2>` in :ref:`Definition 2.1.3 <definition-2-1-3>`.
    
    Each word in :math:`W_{\zeta}` corresponds to a contiguous subsequence of non-Empty, non-Delimiter Characters in **Ζ**.
    
    Since Delimiters separate Words, and each Delimiter corresponds to one Word boundary, the number of Words in the Sentence is always one more than the number of delimiters. Therefore, the cardinality of :math:`W_{\zeta}` (the number of words) is equal to the Delimiter count of *Δ(ζ)* plus one,
    
    .. math::
    
        \lvert W_{\zeta} \rvert = \Lambda(\zeta) = \Delta(\zeta) + 1 
    
    ∎
    
    The next two theorems establish the invariance of the Delimiter count under String Inversion for any String, and by extension, any Sentence.
    
    .. _theorem-3-2-2:
    
    **Theorem 3.2.2** :math:`\forall s \in S: \Delta(s) = \Delta(\text{inv}(s))`
    
    Let *t* be a string with length *l(t)*. Let :math:`u = \text{inv}(t)`. By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        1. \quad l(t) = l(u)
        
    .. math::
    
        2. \quad \forall i \in N_{l(t)}: u[i] = t[l(t) - i + 1]
    
    Let **D**:sub:`t` be the set of ordered pairs representing the positions of the Delimiter *σ* in *t*, and let **D**:sub:`u` be the corresponding set for *u*. Assume *(j, σ) ∈*  **D**:sub:`u`, then, by step 2,
    
    .. math::
    
        3. \quad u[j] = t[l(t) - j  + 1]
    
    This means that the Character at position *j* in the inverse string *t* is the Delimiter *σ*. Therefore, 
    
    .. math::
    
        4. \quad (l(t) - j  + 1, \sigma) \in D_t
    
    Thus, it is shown that for every element :math:`(j, \sigma) \in  D_u`, there exists a corresponding element :math:`(i, \sigma) \in D_t`, where :math:`i = l(t) - j + 1`. 
    
    To make the mapping more explicit, define a function :math:`f: D_t \to D_u` as follows. For any :math:`(i, \sigma) \in D_t`, let 
    
    .. math::
    
        1. \quad f((i, \sigma)) = (l(t) - i + 1, \sigma)
        
    It will be shown that *f* is a bijection.
    
    **Well Defined** If :math:`(i, \sigma) \in D_t`, then the Character at position *i* in *t* is *σ*. By step 2, the Character at position *l(t) - i + 1* in :math:`u = inv(t)` is also *σ*. Therefore, 
    
    .. math::
    
        6. \quad (l(t) - i + 1, \sigma) \in D_u
        
    In other words, *f* maps elements of **D**:sub:`t` to elements of **D**:sub:`u`. Thus, *f* is well defined.
     
    **Injective** Suppose 
    
    .. math::
    
        7. \quad f((i_1, \sigma)) = f((i_2, \sigma)). 
        
    Then, it follows,
    
    .. math::
    
        8. \quad (l(t) - i_1 + 1, \sigma) = (l(t) - i_2 + 1, \sigma). 
        
    This in turn implies, 
    
    .. math::
    
        9. \quad l(t) - i_1 + 1 = l(t) - i_2 + 1, 
        
    So 
    
    .. math::
    
        10. \quad i_1 = i_2
        
    Thus, 
    
    .. math::
    
        11. \quad (i_1, \sigma) = (i_2, \sigma)
        
    In other words, *f* is injective. 
    
    **Surjective** Let *(j, σ)* be an arbitrary element of **D**:sub:`u`. Then the Character at position *j* in *u* is *σ*. Let 
    
    .. math::
    
        12. \quad i = l(t) - j + 1. 
        
    Then 
    
    .. math::
    
        13. \quad j = l(t) - i + 1. 
        
    By step 3, the Character at position *i* in *t* is also *σ*. So, 
    
    .. math::
    
        14. \quad (i, \sigma) \in D_t
        
    And,
    
        15. \quad f((i, \sigma)) = (l(t) - i + 1, \sigma) = (j, sigma). 
        
    Thus, *f* is surjective. 
    
    This defines a bijective mapping between the elements of **D**:sub:`u` and **D**:sub:`t`. Since there's a one-to-one mapping between the elements of **D**:sub:`u` and **D**:sub:`t`, their cardinalities must be equal,
    
    .. math::
    
        16. \quad \lvert D_u \rvert = \lvert D_s \rvert
    
    By :ref:`Definition 3.2.1 <definition-3-2-1>` of the Delimiter Count function, this means :math:`\Delta(u) = \Delta(t)`. Since :math:`u = \text{inv}(t)`, it has been shown :math:`\Delta(\text{inv}(s)) = \Delta(s)`. Generalizing this over the set of all Strings,
    
    .. math::
    
        17. \quad \forall s \in S: \Delta(s) = \Delta(\text{inv}(s))
    
    Furthmore, an exact relationship has been estalished between the coordinates of Delimiters in Strings and their Inverses, 
    
    .. math::
    
        18. \quad D_{\text{inv}(t)} = \{ (l(t) - i + 1, \sigma) \mid (i, \sigma) \in D_t \} 
    
    ∎
    
    .. _theorem-3-2-3:
    
    **Theorem 3.2.3** :math:`\forall \zeta \in C_L: \Delta(\zeta) = \Delta(\text{inv}(\zeta))`
    
    Let *ζ* be an arbitrary Sentence in Corpus :math:`C_L`,
    
    .. math::
    
        1. \quad \zeta \in C_L
    
    By :math:`Definition 2.1.2 <definition-2-1-2>`, every Sentence is a String. Therefore, *ζ* is a String. By :ref:`Theorem 3.2.2 <theorem-3-2-2>`, 
    
    .. math::
    
        2. \quad \Delta(\zeta) = \Delta(\text{inv}(\zeta))
    
    Which is what was to be shown. Since *ζ* was an arbitrary Sentence, this can generalize over the Corpus 
    
    .. math::
    
        3. \quad \forall \zeta \in C_L: \Delta(\zeta) = \Delta(\text{inv}(\zeta))
    
    ∎
    
    .. _theorem-3-2-4:
    
    **Theorem 3.2.4** :math:`\forall \alpha \in L: \Delta(\alpha) = 0`
    
    This theorem can be stated in natural language as follows: The Delimtier Count of any Word in a Language is zero.
    
    Assume *α* is a Word in Language **L**,
    
    .. math::
    
        1. \quad \alpha \in L
        
    By the :ref:`Discovery Axiom W.1 <axiom-w1>`, all Words in a Language do not have Delimiters,
    
    .. math::
    
        2. \quad \forall i \in N_{l(\alpha)}: \alpha[i] \neq \sigma
    
    Therefore, *α* does not have any Delimiter Characters (*σ*). By :ref:`Definition 3.2.1 <definition-3-2-1>`, *Δ(s)* counts the number of Delimiter Characters (*σ*) in a String *s*. Since *α* hasno Delimiter Characters, the Delimiter Count of *α* must be 0. Therefore,
    
    .. math::
    
        3. \quad \Delta(\alpha) = 0 
    
    Since *α* was an arbitrary Word, this can be generalized over the Language,
    
    .. math::
        
        4. \quad \forall \alpha \in L: \Delta(\alpha) = 0
    
    ∎
    
    .. _theorem-3-2-5:
    
    **Theorem 3.2.5** :math:`\forall \zeta \in C_L: l(\zeta) = \Delta(\zeta) + \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\})`
    
    In natural language, this theorem can be stated as follows: For every Sentence in a Corpus, the String Length of the Sentence is equal to the Delimiter Count of the sentence plus the sum of the String Lengths of its Words.
    
    Assume *ζ* is an arbitrary Sentenc,
    
    .. math::
    
        1. \quad \zeta \in C_L 
    
    Either each *ζ{i}* for :math:`1 \leq i \leq l(\zeta)` is Delimiter or it is a non-Delimiter, with no overlap. By :ref:`Definition 3.2.1 <definition-3-2-1>`, the number of Delimiter Characters in *ζ* is *Δ(ζ)*. 
    
    By the :ref:`Discovery Axiom W.1 <axiom-w1>`, words in **L** do not contain Delimiters. By :ref:`Definition 2.1.3 <definition-2-1-3>`, the Words in :math:`W_{\zeta}` are obtained by splitting *ζ*  at the Delimiters. Therefore, the total number of non-Delimiter characters in *ζ* is the sum of the Word Lengths l(ζ{i}) which is 
    
    .. math::
    
        2. \quad \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\})
    
    Since every Character in *ζ* is either a Delimiter or part of a Word (and not both), the total number of Characters in *ζ* is the sum of the number of Delimiters and the number of Characters in Words. By :ref:`Definition 1.1.3 <definition-1-1-3>` of String Length, the total number of non-Empty characters in ζ is *l(ζ)*. Therefore, the number of non-Empty Characters in *ζ* is equal to the number of Delimiters plus the sum of its Word Lengths,
    
    .. math::
    
        3. \quad l(\zeta) = \Delta(\zeta) + \sum_{i = 1}^{\Lambda(\zeta)} l(\zeta\{i\}) 
    
    Since *ζ* was arbitrary, this can generalize over the Corpus,
    
    .. math::
        
        4. \quad \forall \zeta \in C_L: l(\zeta) = \Delta(\zeta) + \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\})
    
    ∎
    
    .. _theorem-3-2-6:
    
    **Theorem 3.2.6** :math:`\forall \zeta \in C_L: l(\zeta) + 1 = \Lambda(\zeta) + \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\})` 
    
    Applying the results of :ref:`Theorem 3.2.1 <theorem-3-2-1>` and :ref:`Theorem 3.2.5 <theorem-3-2-5>`, this theorem follows from simple algebraic manipulation. ∎
    
    .. _theorem-3-2-7:
    
    **Theorem 3.2.7** :math:`\forall \zeta \in C_L: l(\zeta) \geq \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\})`
    
    This theorem can be stated in natural language as follows: For any Sentence in the Corpus, its String Length is greater than or equal to the sum of the String Length of its Words. 
    
    Assume :math:`ζ \in C_L`. By :ref:`Theorem 3.2.4 <theorem-3-2-4>`,
        
    .. math::
    
        1. \quad \Lambda(\zeta) \geq 1
    
    From :ref:`Theorem 3.2.6 <theorem-3-2-6>`,
    
    .. math::
    
        2. \quad l(\zeta) + 1 - \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\}) = \Lambda(\zeta)
    
    Combining step 1 and step 2, the theorem is obtained through algebraic manipulation and by generalizing the arbitrary Sentence *ζ* over the Corpus,
    
    .. math::
    
        3. \quad l(\zeta) \geq \sum_{i = 1}^{\Lambda(\zeta)} l(\zeta\{i\}) 
    
    ∎
    
    .. _theorem-3-2-8:
    
    **Theorem 3.2.8** :math:`\forall \zeta \in C_L: l(\zeta) \geq \Lambda(\zeta)`
    
    This theorem can be stated in natural language as follows: For any Sentence in a Corpus, its String Length is always greater than or equal to its Word Length.
    
    Let *ζ* be an arbitrary Sentence in :math:`C_L`. Let :math:`W_{\zeta}`` be the Word-level representation of *ζ*. By :ref:`Definition 2.1.4 <definition-2-1-4>`, 
    
    .. math::
    
        1. \quad \Lambda(\zeta) = | W_{\zeta} |
    
    By :ref:`Theorem 1.2.3 <theorem-1-2-3>`, each Word in :math:`W_{\zeta}` consists of one or more non-Empty Characters. By :ref:`Theorem 2.2.5 <theorem-2-2-5>`, every Sentence is a Delimitation of its Words,
    
    .. math::
    
        2. \quad \zeta = D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}
    
    Where the operation of Delimitation inserts Delimiters between the Words of *ζ*. On the other hand, let *t* be the the Limitation of *ζ*,
    
    .. math::
    
        3. \quad t = L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}
    
    By :ref:`Definition 1.2.7 <definition-1-2-7>`, :ref:`Definition 1.2.8 <definition-1-2-8>` and :ref:`Definition 1.1.3 <definition-1-1-3>` of String Length,
    
    .. math::
    
        4. \quad l(D\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\}) = l(\zeta) \geq l(t) = l(L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\})
    
    By :ref:`Definition 1.2.8 <definition-1-2-8>`,
    
    .. math::
    
        5. \quad L\Pi_{i=1}^{\Lambda(\zeta)} \zeta\{i\} = (\zeta\{1\})(\zeta\{2\}) .... (\zeta\{\Lambda(\zeta)-1\})(\zeta\{\Lambda(\zeta)\})
    
    By :ref:`Theorem 1.1.1 <theorem-1-1-1>`, 
    
    .. math::
    
        6. \quad l((\zeta\{1\})(\zeta\{2\}) .... (\zeta\{\Lambda(\zeta)-1\})(\zeta{\Lambda(\zeta)})) = \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\})
    
    Therefore, combining steps 4 and 6
    
    .. math::
    
        7. \quad l(\zeta) \geq \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\})
    
    Consider the summation,
    
    .. math::
    
        8. \quad \sum_{i=1}^{\Lambda(\zeta)} 1
    
    Clearly, since :math:`l(\zeta\{i\}) \geq 1` for all *i*, it follows, 
    
    .. math::
    
        9. \quad \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\}) \geq sum^{i=1}^{\Lambda(\zeta)} 1
    
    By the definition of summations, step 8 can be rewritten as,
    
    .. math::
    
        10. \quad \sum_{i=1}^{\Lambda(\zeta)} 1 = 1 + 1 + 1 + .... + 1 = \Lambda(\zeta)
    
    Combining step 7, step 9 and  step 10,
    
    .. math::
    
        11. \quad l(\zeta) \geq \sum_{i=1}^{\Lambda(\zeta)} l(\zeta\{i\}) \geq \sum_{i=1}^{\Lambda(\zeta)} 1 = \Lambda(\zeta)
    
    Since *ζ* was arbitrary, this can be generalized over the Corpus,
    
    .. math::
    
        12. \quad \forall \zeta \in C_L: l(\zeta) \geq \Lambda(\zeta) 
    
    ∎
    
    .. _theorem-3-2-9:
    
    **Theorem 3.2.9 (Informal)** :math:`\forall u, t \in S: \Delta(ut) = \Delta(u) + \Delta(t)`
    
    Let *u* and *t* be arbitrary strings in S. Let **U** and **T** be the Character-level representations of *u* and *t*, respectively:
    
    .. math::
    
        1. \quad U = (\iota_1, \iota_2, ..., \iota_{l(u)})
    
    .. math::
    
        2. \quad T = (\nu_1, \nu_2, ..., \nu_{l(t)})
    
    The Character-level representation of *ut* is:
    
    .. math::
    
        3. \quad UT = (\iota_1, \iota_2, ..., \iota_{l(u)}, \nu_1, \nu_2, ..., \nu_{l(t)})
    
    By :ref:`Definition 3.2.1 <definition-3-2-1>`, *Δ(u)* is the number of Delimiters in *u*, *Δ(t)* is the number of Delimiters in *t*, and *Δ(ut)* is the number of Delimiters in *ut*.
    
    Since concatenation simply joins two Strings without adding or removing Characters, with the possible exception of Empty Characters through the Basis Clause of Definition 1.1.1, the number of Delimiters in *ut* is the sum of the number of Delimiters in *u* and the number of Delimiters in *t*. ∎
    
    .. _theorem-3-2-9a:
    
    **Theorem 3.2.9 (Formal)**  :math:`\forall u, t \in S: \Delta(ut) = \Delta(u) + \Delta(t)`
    
    Let **D**:sub:`u` be the set of indices of Delimiters in *u*. Let **D**:sub:`t` be the set of indices of Delimiters in *t*. Let **D**:sub:`ut` be the set of indices of delimiters in *ut*,
    
    .. math::
    
        1. \quad D_u = \{ i \mid 1 \leq i \leq l(u) \land u[i] = \sigma \}
    
    .. math::
    
        2. \quad D_t = \{ j \mid 1 \leq j \leq l(t) \land t[j] = \sigma \}
        
    .. math::
    
        3. \quad D_{ut} = \{ k \mid (1 \leq k \leq l(u) + l(t)) \land ((k \leq l(u) \and UT[k] = \sigma) \lor (k > l(u) \land UT[k] = \sigma)) \}
       
    It is clear that D:sub:`ut` is the union of two disjoint sets, since the indices of the Delimiters in *t* have been shifted by *l(u)*. Therefore,
    
    .. math::
    
        4. \lvert D_{ut} \rvert = \lvert D_u \rvert + \lvert D_t \rvert
    
    By :ref:`Definition 3.2.1 <definition-3-2-1>`, this is equivalent to,
    
    .. math::
    
        5. \quad \Delta(ut) = \Delta(u) + \Delta(t)
    
    Since u and t were arbitrary strings, this can be generalized over the set of all Strings,
    
    .. math::
    
        6. \quad \forall u, t \in S: \Delta(ut) = \Delta(u) + \Delta(t) 
    
    ∎
    
    .. _theorem-3-2-10:
    
    **Theorem 3.2.10**  :math:`\forall u, t \in S: \Delta(\text{inv}(ut)) = \Delta(u) + \Delta(t)`
    
    Let *u* and *t* be arbitrary strings in S.
    
    By :ref:`Theorem 3.2.2 <theorem-3-2-2>`,
    
    .. math::
    
        1. \quad \Delta(s) = \Delta(\text{inv}(s))
    
    Therefore, 
    
    .. math::
    
        2. \quad \Delta(ut) = \Delta(\text{inv}(ut)).
    
    By :ref:`Theorem 3.2.9 <theorem-3-2-9>`,
     
    .. math::
    
        3. \quad \Delta(ut) = \Delta(u) + \Delta(t)
    
    Combining steps 2 and 3, it follows, 
    
    .. math::
    
        4. \quad \Delta(\text{inv}(ut)) = \Delta(ut) = \Delta(u) + \Delta(t)
    
    Since *u* and *t* were arbitrary strings, this can be generalized over the set of all Strings,
    
    .. math::
    
        5. \quad \forall u, t \in S: \Delta(\text{inv}(ut)) = \Delta(u) + \Delta(t) 
    
    ∎
    
    .. _theorem-3-2-11:
    
    **Theorem 3.2.11** :math:`\forall t \in S: \Delta(\varsigma(t)) = 0`
    
    This theorem can be stated in natural language as follows: For any String, the Delimiter Count of its *σ*-Reduction is 0.
    
    Let t be an arbitrary string in **S**,
    
    .. math::
    
        1. \quad t \in S
    
    By :ref:`Definition 3.1.2 <definition-3-1-2>`, *ς(t)* is the String obtained by removing all occurrences of the Delimiter character *σ* from *t*. :ref:`Definition 3.2.1 <definition-3-2-1>`, Δ(t) is the number of Delimiter Characters *σ* in a String *t*. Since *ς(t)* has all its Delimiters removed, it contains no occurrences of the Character *σ*. Therefore, 
    
    .. math::
    
        2. \quad \Delta(\varsigma(t)) = 0
    
    Since *t* was an arbitrary String, this can be generalized over the set of all Strings,
    
    .. math::
    
        3. \quad \forall t \in S: \Delta(\varsigma(t)) = 0 
    
    ∎
    
    .. _theorem-3-2-12:
    
    **Theorem 3.2.12** :math:`\forall t \in S: l(\varsigma(t)) + \Delta(t) = l(t)`
    
    Translation: For any String, its String Length is equal to the String Length of its σ-reduction plus its Delimiter Count.
    
    Let *t* be an arbitrary String in **S**,
    
    .. math::
    
       1. \quad t \in S
    
    By :ref:`Definition 3.1.2 <definition-3-1-2>`, *ς(t)* is the String obtained by removing all occurrences of the Delimiter character *σ* from *t*.
    
    By :ref:`Definition 3.2.1 <definition-3-2-1>`, *Δ(t)* is the number of Delimiter characters in *t*.
    
    By :ref:`Definition 1.1.3 <definition-1-1-3>`, *l(t)* is the total number of non-Empty Characters in *t*, including Delimiters.
    
    Similarly, *l(ς(t))* is the number of non-Delimiter Characters in *t*.
    
    Every Character in *t* is either a Delimiter or a non-Delimiter character. Therefore, the total number of characters in *t* is the sum of the number of non-delimiter characters and the number of delimiter characters.
    
    Therefore,
    
    .. math::
    
        2. \quad l(\varsigma(t)) + \Delta(t) = l(t)
    
    Since *t* was an arbitrary String, this can be generalized over the set of all Strings,
    
    .. math::
    
        3. \quad \forall t \in S: l(t) = l(\varsigma(t)) + \Delta(t)  
    
    ∎
    
    :ref:`Theorem 3.2.12 <theorem-3-2-12>` expresses a fundamental relationship between the String Length of a String, the String Length of its σ-reduction, and its Delimiter Count. It essentially states that the original String Length can be decomposed into the String Length of the String without Delimiters (the *σ*-reduction) and the number of Delimiters that were removed (the Delimiter Count).
    
    **Example**
    
    Let :math:`t = (\mathfrak{a})(\sigma)(\mathfrak{b})(\sigma)(\mathfrak{c})`. Then, by :ref:`Definition 3.1.2 <definition-3-1-2>`,
    
    .. math::
    
        \varsigma(t) = \mathfrak{a}\mathfrak{b}\mathfrak{c}
    
    The following quantities can then be calculated,
    
    .. math::
    
        l(t) = 5    
        
    .. math::
    
        \Delta(t) = 2
        
    .. math::
    
        l(\varsigma(t))= 3
    
    And indeed, 
    
    .. math::
    
        l(t) = l(\varsigma(t)) + \Delta(t) 
    
    ∎
    
    .. _theorem-3-2-13:
    
    **Theorem 3.2.13** :math:`\forall \zeta \in C_L: l(\varsigma(t)) + \Lambda(\zeta) = l(\zeta) + 1`
    
    Let *ζ* be an arbitrary Sentence in Corpus :math:`C_L`,
    
    .. math::
    
        1. \quad \zeta \in C_L
    
    By :ref:`Definition 2.1.2 <definition-2-1-2>`, every Sentence is a String. Therefore, :ref:`Theorem 3.2.12 <theorem-3-2-12>` may be applied to *ζ*
    
    .. math::
    
        2. \quad  l(\zeta) = l(\varsigma(\zeta)) + \Delta(\zeta)
    
    By :ref:`Theorem 3.2.1 <theorem-3-2-1>`,
    
    .. math::
    
        3. \quad \Lambda(\zeta) = \Delta(\zeta) + 1
    
    Rearranging,
    
    .. math::
    
        4. \quad \Delta(\zeta) = \Lambda(\zeta) - 1
    
    Substituting the expression for *Δ(ζ)* from step 4 into the equation from step 2,
    
    .. math::
    
        5. \quad l(\zeta) = l(\varsigma(\zeta)) + (\Lambda(\zeta) - 1)
    
    Rearranging the terms, 
    
    .. math::
    
        6. \quad l(\varsigma(\zeta)) + \Lambda(\zeta) = l(\zeta) + 1
    
    Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,
    
    .. math::
    
        7. \quad \forall \zeta \in C_L: l(\varsigma(\zeta)) + \Lambda(\zeta) = l(\zeta) + 1 
    
    ∎

.. _05palindromes:
 
------------------
05_palindromes.rst
------------------

.. raw:: 

    .. _section-iv:
    
    Section IV: Palindromes
    =======================
    
    As mentioned in the introduction of this work, the structure of palindromes is described through the combination of four different attributes or dimensions: *aspect*, *parity*, *case* and *punctuality*. The framework has now been developed to classify the first two palindromic properties with more precision.
    
    Unfortunately, as far as the author knows, punctuation and capitalization are syntactic bearers of semantic meaning that cannot be reduced to purely formal considerations. Both punctuality and case require additional axioms to describe the unique structuring they impose on a Language and its Corpus. In the author's opinion, it is impossible to disentangle these linguistic phenomenon from the realm of semantics.
    
    In what follows, two things are implicitly assumed. These assumptions are made explicit here, so the scope of the results can be properly understood. First, the Alphabet **Σ** is assumed to contain no punctuation marks beyond the Delimiter Character (if one is inclined it to consider a form of punctuation). Second, it is assumed every Character in **Σ** is distinct, meaning all matters of case are ignored. To rephrase the same idea more precisely: there is no assumed semantic relation between Characters in the Alphabet that would allow the identification of distinct Characters as different *cases* of the same Character.
    
    With these assumptions, the analysis is confined to the dimensions of *aspect* and *parity*, which will be defined in the following subsections. After the results are derived, consideration will be given to future work that could potentially integrate semantic considerations into the formal framework of palindromic structures to account for the dimensions of punctuality and case, in addition to symmetries above the Sentence level that might be incorporated into the conditions for Palindromes.
    
    The current analysis now turns towards its goal, using the notions that have been developed up to this point to define the mathematical structure of Palindromes. To motivate the next definition, consider how the operation of *σ*-reduction "*projects*" Palindromes onto an Alphabet where their symmetry is preserved.
    
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
    
    **Theorem 4.2.1** :math:`\forall \zeta \in C_L: \forall i \in N_{l(\zeta)}: \text{inv}(\zeta)[:i] = \zeta[l(\zeta)-i+1:]`
    
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
    
    If :math:`\omega(\zeta) = \frac{l(\zeta)}{2}`, then *l(ζ)* is even by :ref:`Theorem 4.2.7 <theorem-4-2-7>`. From step 3, if :math:`(\varsigma(\zeta)) = \frac{l(\varsigma(\zeta))}{2}`, it follows, 
    
    .. math::
    
        10. \quad \omega(\varsigma(\zeta)) \leq \omega(\zeta) 
    
    If :math:`\omega(\varsigma(\zeta)) = \frac{l(\varsigma(\zeta)) + 1}{2}`, then *l(ς(ζ))* is odd by :ref:`Theorem 4.2.5 <theorem-4-2-5>`. 
    
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
    
    When a Sentence has odd parity, the Character at its pivot, :math:`\zeta[\omega(\zeta)]` will remain at its Pivot under inversion, i.e. the following implication will always obtain,
    
    .. math::
    
        \exists k \in \mathbb{N}: l(\zeta) = 2k+1 \to \zeta[\omega(\zeta)] = \text{inv}(\zeta)[omega(\zeta)]
    
    However, this is not the case when a Sentence has even parity. The Pivot of an inverted Sentence with even parity will shift. First note, by :ref:`Definition 4.2.3 <definition-4-2-3>`, the Pivot only depends on the length of a Sentence. By :ref:`Definition 1.2.4 <definition-1-2-4>`, String Inversion preserves length. Therefore, the Pivots of a Sentence and its Inverse are equal,
    
    .. math::
    
        \omega(\zeta) = \omega(\text{inv}(\zeta))
    
    Consider now the following Sentence and its Inverse,
    
    .. math::
    
        ᚠ = \text{"not on"} \quad ; \quad ᚠ[\omega(ᚠ)] = \text{"t"}
    
    .. math::
    
        \text{inv}(ᚠ) = \text{"no ton"} \quad ; \quad \text{inv}(ᚠ)[\omega(ᚠ)] = \text{" "}
    
    Since Sentences with even parity have no Character about which to reflect, the Pivot switches Characters when the Sentence is inverted. This observation is formalized in the next two theorems.
    
    .. _theorem-4-2-11:
    
    **Theorem 4.2.11** :math:`\forall \zeta in C_L: \zeta[\omega(\zeta)] \neq \text{inv}(\zeta)[\omega(\zeta)]) \to (\exists k \in \mathbb{N}: l(\zeta) = 2k)`
    
    This theorem can be stated in natural language as follows: For all Sentences in the Corpus, if the Character at the Pivot of the Sentence is not equal to the Character at the Pivot of its Inverse, then the String Length of the Sentence is even.
    
    Let *ζ* be an arbitrary sentence in :math:`C_L` such that,
    
    .. math::
    
        1. \quad \zeta[\omega(\zeta)] \neq \text{inv}(\zeta)[\omega(\zeta)]
    
    For the sake of contradiction, assume *l(ζ)* is not even. Then l(ζ) must be odd. If l(ζ) is odd, then by :ref:`Definition 4.2.3 <definition-4-2-3>`,
    
    .. math::
    
        2. \quad \omega(\zeta) = \frac{(l(\zeta) + 1)}{2}
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>` of String Inversion, for any :math:`i \in N_{l(\text{inv}(\zeta))}`,
    
    .. math::
    
        3. \quad \text{inv}(\zeta)[i] = \zeta[l(\zeta) - i + 1]
    
    Let :math:`i = \omega(\zeta)`. Substituting this into step 3 and then using the relation in step 2,
    
    .. math::
    
        4. \quad \text{inv}(\zeta)[\omega(\zeta)] = \zeta[l(\zeta) - \omega(\zeta) + 1] = \zeta[l(\zeta) - \frac{l(\zeta) + 1}{2} + 1] 
        
    .. math::
        
        5. \quad \text{inv}(\zeta)[\omega(\zeta)] = \zeta[\frac{2l(\zeta) - l(\zeta) - 1 + 2}{2}] = \zeta[\frac{l(\zeta) + 1}{2}]
       
    From step 2 and step 5,
    
    .. math::
    
        6. \quad \text{inv}(\zeta)[\omega(\zeta)] = \zeta[\omega(\zeta)]
    
    However, this contradicts the initial assumption in step 1. Therefore, *l(ζ)* cannot be odd and must be even. Since l(ζ) is even, 
    
    .. math::
    
        7. \quad \exists k in \mathbb{N}: l(\zeta) = 2k
    
    Since *ζ* was an arbitrary sentence in :math:`C_L`, this can be generalized over the Corpus,
    
    .. math::
    
        8. \quad \forall \zeta \in C_L: \zeta[\omega(\zeta)] \neq \text(\zeta)[\omega(\zeta)] \to (\exists k \in \mathbb{N}: l(\zeta) = 2k)
    
    ∎
    
    The direction of implication in :ref:`Theorem 4.2.11 <theorem-4-2-11>` is important. From the inequality of the Pivot Characters in a Sentence and its Inverse, the parity of a Sentence may be inferred. However, the converse is not true: from the parity of a Sentence, the inequality of its Pivots Characters may not be inferred, as the simple String *"a ba"* illustrates
    
    TODO
    
    .. _theorem-4-2-12:
    
    **Theorem 4.2.12** :math:`\forall \zeta \in C_L: (\exists k \in \mathbb{N}: l(\zeta)=2k) \to \text{inv}(\zeta)[\omega(\zeta)] = \zeta[\omega(\zeta)+1]`
    
    This theorem can be stated in natural language as follows: For all Sentence in the Corpus, if the String Length of the Sentence is even, then the Pivot Character of its Inverse is equal to the Character at one plus the Pivot index of the original Sentence.
    
    Let *ζ* be an arbitrary sentence in :math:`C_L` such that, 
    
    .. math::
    
        1. \quad \exists k \in \mathbb{N}: l(\zeta) = 2k
    
    We want to show that inv(ζ)[ω(ζ)] = ζ[ω(ζ) + 1].
    
    Since *l(ζ)* is even, by :ref:`Definition 4.2.3 <definition-4-2-3>`,
    
    .. math::
    
        2. \quad \omega(\zeta) = \frac{l(\zeta)}{2}
    
    By :ref:`Definition 1.2.4 <definition-1-2-4>`,
    
    .. math::
    
        3. \quad \text{inv}(\zeta)[i] = \zeta[l(\zeta) - i + 1]
    
    Let :math:`i = ω(\zeta)`. Substituting step 2 into step 3,
    
        4. \quad \text{inv}(\zeta)[\omega(\zeta)] = \zeta[l(\zeta) - \frac{l(\zeta)}{2} + 1]
    
    Simplifying,
    
    .. math::
    
        5. \quad \text{inv}(\zeta)[\omega(\zeta)] = \zeta[l(\zeta)/2 + 1]
    
    Substituting :math:`\omega(\zeta) = \frac{l(\zeta)}{2}`,
    
    .. math::
    
        6. \quad \text{inv}(\zeta)[\omega(\zeta)] = \zeta[\omega(\zeta) + 1]
       
    Since *ζ* was an arbitrary Sentence, this can be generalized over the Corpus,
    
        7. \quad \forall \zeta \in C_L: (\exists k \in \mathbb{ℕ}: l(\zeta) = 2k) \to \text{inv}(\zeta)[\omega(\zeta)] = \zeta[\omega(\zeta) + 1]
    
    ∎
    
    TODO
    
    In other words, from the inequality of Pivot Characters in a Sentence and its Inverse, we can infer even parity. From even parity, we can infer the Pivot Character of the Inverse is equal to the Character at one plus the Pivot Index of the original Sentence. This is the price we pay for repeated Characters. Inside of a full equivalence, we have to be careful in the direction and exact conditions.
    
    TODO
    
    
    
    These properties of Pivots and Partial Sentences will be necessary to state and prove the main results of the work in the next section. In addition, it will be necessary to know the class of Odd Palindromes and the class of Even Palindromes form a partition of the class of all Palindromes. This result is definitively established in :ref:`Theorems 4.2.11 <theorem-4-2-11>` - :ref:`4.2.12 <theorem-4-2-11>`.
    
    .. _theorem-4-2-13:
    
    **Theorem 4.2.13** :math:`P_{+} \cap P_{-} = \emptyset`
    
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
    
    .. _theorem-4-2-14:
    
    **Theorem 4.2.14** :math:`P_{-} \cup P_{+} = P`
    
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

.. _06analysis:
 
---------------
06_analysis.rst
---------------

.. raw:: 

    .. _section-v:
    
    Section V: Analysis
    ===================
    
    The study of Palindromes leads directly into the study of Delimiter distributions. The partitioning of Palindromes into the Perfect and Imperfect aspects highlights the asymmetry which separates the latter from the former class. Consider the pair of Perfect Palindromes, 
    
    - god lived on no devil dog
    - i am civic am i
    
    Since, by :ref:`Definition 4.1.2 <definition-4-1-2>`, Perfect Palindromes are exactly the class of Sentences that are equal to their own Inverses, the Delimiters in a Perfect Palindrome display symmetry. The following barcharts show the Character indices of Delimiters for these examples. Note the horizontal axes are scaled to the Sentence String Length,
    
    .. image:: ../_static/img/sentences/palindromes/delimiter_indices_perfect_palindrome_1.png
      :width: 400
      :alt: Delimiter Indices, Perfect Palindrome, Example #1
    
    .. image:: ../_static/img/sentences/palindromes/delimiter_indices_perfect_palindrome_2.png
      :width: 400
      :alt: Delimiter Indices, Perfect Palindrome, Example #2
    
    Notice the Delimiter indices are symmetrical about the center. Now consider the pair of Imperfect Palindromes, 
    
    - goddesses so pay a possessed dog 
    - borrow or rob
    
    According to :ref:`Definition 4.1.3 <definition-4-1-3>`, Imperfect Palindromes must first be :math:`\sigma\text{-reduced}` to restore their symmetry. An examination of the corresponding barcharts for these examples show why,
    
    .. image:: ../_static/img/sentences/palindromes/delimiter_indices_imperfect_palindrome_1.png
      :width: 400
      :alt: Delimiter Indices, Imperfect Palindrome, Example #1
    
    .. image:: ../_static/img/sentences/palindromes/delimiter_indices_imperfect_palindrome_2.png
      :width: 400
      :alt: Delimiter Indices, Imperfect Palindrome, Example #2
    
    Imperfect Palindromes are exactly those class of Palindromes which do not have symmetrical Delimiter distributions. 
    
    The goal of this section is to understand the Delimiter symmetry displayed by Perfect Palindromes, in order to help further classify Imperfect Palindromes according to the type of Delimiter asymmetry found in a particular instance. In other words, the analysis seeks a method for quantifying a Perfect Palindrome's Delimiter symmetry in order to apply the same method to Imperfect Palindromes, with the hope of gaining greater insight into the syntactical obstacles preventing direct formal access to the class of Imperfect Palindromes.
    
    The essential problem of modelling Delimiter distributions is the method of approach. Analytical methods, if not well constructed, are liable to lead to seemingly well-supported, but logically flawed conclusions. 
    
    Consider taking Sentences from a Corpus and for each one, calculating and returning the Delimiter indices, as in the following,
    
    .. math::
    
      ᚠ = \text{"error is the price we pay for progress"}
    
    .. math::
    
      D_ᚠ = \{ (6, \sigma), (9, \sigma), (13, \sigma), (19, \sigma), (22, \sigma), (26, \sigma), (30, \sigma) \}
    
    Note the set :math:`D_ᚠ` is the set involved in :ref:`Definition 3.2.1 <definition-3-2-1>` of the Delimiter Count function. If a large Corpus is analyzed so that each Sentence is reduced to a set of Delimiter indices, and then the frequency of Delimiter Counts is plotted, an interesting, but potentially misleading result is obtained. The following histograms show the result of this technique for Sentences of various fixed lengths. 
    
    .. image:: ../_static/img/sentences/english/delimiter_distribution_n50.png
      :width: 400
      :alt: Delimiter Distribution, Sentence String Length = 50
    
    .. image:: ../_static/img/sentences/english/delimiter_distribution_n100.png
      :width: 400
      :alt: Delimiter Distribution, Sentence String Length = 100
    
    .. image:: ../_static/img/sentences/english/delimiter_distribution_n200.png
      :width: 400
      :alt: Delimiter Distribution, Sentence String Length = 200
    
    As can be seen from the shape of the histograms, the Delimiter index distribution for Sentences of fixed length is roughly uniform (with a potentially significant spike in the far left tail of each distribution). These graphs suggest the Delimiter Count of a single Character, :math:`\zeta[k]`, can be approximated by a discrete, uniform random variable, conditional on the Sentence String Length,
    
    .. math::
    
      P(\Delta(\hat{\zeta}[k]) | l(\zeta) = \lambda) = \frac{1}{\lambda}
    
    Where :math:`P()` represents the probability of an event, :math:`\hat{\zeta[k]}` represents a random varaible and :math:`\lambda` represents a fixed String Length. However alluring, there is a subtle, but important assumption going into the generation of these histograms that prevents the acceptance of this conclusion.
    
    When Sentences are reduced to Delimiter indices and plotted in aggregate, information related to the relative order of the Delimiter in the Sentence is lost. In other words, the method of construction used to generate these histogram implicitly assumes,
    
    .. math::
    
      P(\Delta(\hat{zeta}[k]) | \Delta(\zeta[k-1]) = \delta_{k-1}, \Delta(\zeta[k-2]) = \delta_{k-2}, ... , \Delta(\zeta[1]) = \delta_1 ) = P(\Delta(\zeta[k]))
    
    To provide a more concrete example, consider the Sentences, 
    
    .. math::
    
      ᚢ = \text{"the dog runs across the field"}
    
    .. math::
      
      ᚦ = \text{"the child laughs at the joke"}
    
    In each case,
    
    .. math::
    
      \Delta(ᚢ[4]) = \Delta(ᚦ[4]) = 1
    
    The presence of the Delimiter after the article *"the"* affects the subsequent appearance of Delimiters in the Sentences. Due to grammatical rules, a noun must follow the article and this has tangible, measureable syntactic effects. Given the information :math:`\Delta(ᚢ[4]) = 1`, this fact greatly decreases (perhaps even nullifies) the event of :math:`\Delta(ᚢ[5]) = 1`. In fact, a probability model that describes linguistic entities might take it as an axiom,
    
    .. math::
    
      P(\Delta(\hat{zeta}[k]) \,|\, \Delta(\zeta[k-1]) = 1 ) = 0
    
    In summary, it cannot be discounted that knowing where a single Delimiter occurs in a Sentence influences the possible locations where other Delimiters in the same Sentence might occur. However, accounting for this contingency presents computational challenges. A Sentence with 100 Characters will have :math:`2^100` possible Delimiter configurations, by the Fundamental Counting Principle. Tracking the Delimiter distribution across different Sentence String Lengths becomes impossible. Enumerating and tallying these outcomes is a prohibitively expensive task, if abstraction is not employed to summarize the Delimiter *"mass"* of a Sentence. 
    
    .. _section-v-i:
    
    Section V.I: Sentence Integrals
    -------------------------------
    
    Before attempting to extricate the probability density of Delimiters within the Sentences of a Corpus, a conceptual apparatus is required for aggregating and assessing the distribution and configuration of Delimiters in a particular Sentence. 
    
    This apparatus is embodied the concept of a *Sentence Integral*. A Sentence Integral is simply the sum of Delimiter indices in a Sentence. The reason for introducing the connotation of *"integration"* into the vernacular will become apparent after the particular form of its definition is appreciated. In short, the term *"integration"* is used here to evoke the idea of summing or accumulating values over a range, similar to the integral in calculus.
    
    Definitions
    ^^^^^^^^^^^
    
    .. _definition-5-1-1:
    
    **Definition 5.1.1: Lefthand Sentence Integrals**
    
    Let *ζ* be an arbitary Sentence from Corpus :math:`C_L` and let *k* be a natural number such that :math:`1 ≤ k ≤ \Lambda(\zeta)`. The *Lefthand Integral* of Sentence *ζ*, denoted :math:`\Phi_{-}(\zeta, k)`, is defined as,
    
    .. math::
    
      \Phi_{-}(\zeta, k) = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[:i])}{l(\zeta)}
        
    ∎
        
    .. _definition-5-1-2:
    
    **Definition 5.1.2: Righthand Sentence Integrals**
    
    The *Right-Hand Integral* of Sentence ζ, denoted :math:`\Phi_{+}(\zeta, k)`, is defined as,
    
    .. math::
    
      \Phi_{+}(\zeta, k) = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[i:])}{l(\zeta)}
        
    ∎
    
    Take note how the Delimiter Count function is employed in this definitions. Since the domain of discourse is Strings and all Characters are Strings, a Character is valid input to the Delimiter Count. The quantity :math:`\Delta(\zeta[i])` is essentially an indicator variable, taking on the values of 0 or 1, depending on if :math:`\zeta[i] = \sigma` or :math:`\zeta[i] \neq \sigma`.To draw an analogy to a famous mathematical function, the Delimiter Count :math:`\Delta(\zeta[i])` acts in a similar way to the a Dirac delta function :math:`\delta(x)`, in that it selects particular values to contribute to the integrand. 
    
    Each Delimiter that is encountered along the length of the String is then weighted by the length of the Partial Sentence. Recall, by :ref:`Definition 4.2.1 <definition-4-2-1>` and :ref:`Definition 4.2.2 <definition-4-2-2>`, the length of Partial Sentences are given by,
    
    .. math::
    
      l(\zeta[:i]) = i
    
    .. math::
    
      l(\zeta[i:]) = l(\zeta) - i + 1
    
    In other words, the weights given to the Delimiter Count are exactly the Character indices *relative to the starting or ending Character in the Sentence*. The Lefthand Sentence Integral represents the sum of Delimiter positions relative to the first Character, normalized by the String Length of the Sentence, while the Righthand Sentence Integral represents the sum of Delimiter positions relative to the last Character, also normalized by the String Length of the Sentence.
    
    The following examples calculate the Lefthand and Righthand Sentence Integrals for various illustrative Palindromes.
    
    **Example** 
    
    1. Let *ᚠ = "live evil"*. Then *l(ᚠ) = 9*. Note *ᚠ* is a Perfect Palindrome.
       
    .. list-table::
      :widths: 10 10 10 10 10 15 15
      :header-rows: 1
    
      * - k
        - ᚠ[k]
        - l(ᚠ[:k])
        - l(ᚠ[k:])
        - Δ(ᚠ[k])
        - :math:`\Phi_{-}(ᚠ ,k)`
        - :math:`\Phi_{+}(ᚠ ,k)`
      * - 1
        - "l"
        - 1
        - 9
        - 0
        - 0
        - 0
      * - 2
        - "i"
        - 2
        - 8
        - 0
        - 0
        - 0
      * - 3
        - "v"
        - 3
        - 7
        - 0
        - 0
        - 0
      * - 4
        - "e"
        - 4
        - 6
        - 0
        - 0
        - 0
      * - 5
        - " "
        - 5
        - 5
        - 1
        - (5/9)
        - (5/9)
      * - 6
        - "e"
        - 6
        - 4
        - 0
        - (5/9)
        - (5/9)
      * - 7
        - "v"
        - 7
        - 3
        - 0
        - (5/9)
        - (5/9)
      * - 8
        - "i"
        - 8
        - 2
        - 0
        - (5/9)
        - (5/9)
      * - 9
        - "l"
        - 9
        - 1
        - 0
        - (5/9)
        - (5/9)
    
    2. Let *ᚠ = "we panic in a pew"*. Then *l(ᚠ) = 17*. Note *ᚠ* is an Imperfect Palindrome with more Non-Delimiter Characters in the first half in comparison to the second half. In other words, most of the Delimiters in *ᚠ* occur in the second half of the Sentence.
       
    .. list-table::
      :widths: 10 10 10 10 10 15 15
      :header-rows: 1
    
      * - k
        - ᚠ[k]
        - l(ᚠ[:k])
        - l(ᚠ[k:])
        - Δ(ᚠ[k])
        - :math:`\Phi_{-}(ᚠ ,k)`
        - :math:`\Phi_{+}(ᚠ ,k)`
      * - 1
        - "w"
        - 1
        - 17
        - 0
        - 0
        - 0
      * - 2
        - "e"
        - 2
        - 16
        - 0
        - 0
        - 0
      * - 3
        - " "
        - 3
        - 15
        - 1
        - (3/17)
        - (15/17)
      * - 4
        - "p"
        - 4
        - 14
        - 0
        - (3/17)
        - (15/17)
      * - 5
        - "a"
        - 5
        - 13
        - 0
        - (3/17)
        - (15/17)
      * - 6
        - "n"
        - 6
        - 12
        - 0
        - (3/17)
        - (15/17)
      * - 7
        - "i"
        - 7
        - 11
        - 0
        - (3/17)
        - (15/17)
      * - 8
        - "c"
        - 8
        - 10
        - 0
        - (3/17)
        - (15/17)
      * - 9
        - " "
        - 9
        - 9
        - 1
        - (12/17)
        - (24/17)
      * - 10
        - "i"
        - 10
        - 8
        - 0
        - (12/17)
        - (24/17)
      * - 11
        - "n"
        - 11
        - 7
        - 0
        - (12/17)
        - (24/17)
      * - 12
        - " "
        - 12
        - 6
        - 1
        - (24/17)
        - (30/17)
      * - 13
        - "a"
        - 13
        - 5
        - 0
        - (24/17)
        - (30/17)
      * - 14
        - " "
        - 14
        - 4
        - 1
        - (38/17)
        - (34/17)
      * - 15
        - "p"
        - 15
        - 3
        - 0
        - (38/17)
        - (34/17)
      * - 16
        - "e"
        - 16
        - 2
        - 0
        - (38/17)
        - (34/17)
      * - 17
        - "w"
        - 17
        - 1
        - 0
        - (38/17)
        - (34/17) 
    
    3. Consider how the Sentence Integrals behave String Inversion. Let *ᚠ = "draw no dray a yard onward"*. Then *l(ᚠ) = 26*. Note *ᚠ* is an Imperfect Palindrome with a similar (but not identical) distribution of Delimiters around the Pivot.
    
    .. list-table::
      :widths: 8 8 12 12 10 10 12 15 15 10 12 18 18
      :header-rows: 1
    
      * - k
        - ᚠ[k]
        - inv(ᚠ)[k]
        - l(ᚠ[:k])
        - l(ᚠ[k:])
        - Δ(ᚠ[k])
        - Δ(inv(ᚠ)[k])
        - :math:`\Phi_{-}(ᚠ ,k)`
        - :math:`\Phi_{+}(ᚠ ,k)`
        - Δ(ᚠ[:k])
        - Δ(inv(ᚠ)[:k])
        - :math:`\Phi_{-}(\text{inv}(ᚠ) ,k)`
        - :math:`\Phi_{+}(\text{inv}(ᚠ) ,k)`
      * - 1
        - "d"
        - "d"
        - 1
        - 26
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
      * - 2
        - "r"
        - "r"
        - 2
        - 25
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
      * - 3
        - "a"
        - "a"
        - 3
        - 24
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
      * - 4
        - "w"
        - "w"
        - 4
        - 23
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
        - 0
      * - 5
        - " "
        - "n"
        - 5
        - 22
        - 1
        - 0
        - (5/26)
        - (22/26)
        - 1
        - 0
        - 0
        - 0
      * - 6
        - "n"
        - "o"
        - 6
        - 21
        - 0
        - 0
        - (5/26)
        - (22/26)
        - 1
        - 0
        - 0
        - 0
      * - 7
        - "o"
        - " "
        - 7
        - 20
        - 0
        - 1
        - (5/26)
        - (22/26)
        - 1
        - 1
        - (7/26)
        - (20/26)
      * - 8
        - " "
        - "d"
        - 8
        - 19
        - 1
        - 0
        - (13/26)
        - (41/26)
        - 2
        - 1
        - (7/26)
        - (20/26)
      * - 9
        - "d"
        - "r"
        - 9
        - 18
        - 0
        - 0
        - (13/26)
        - (41/26)
        - 2
        - 1
        - (7/26)
        - (20/26)
      * - 10
        - "r"
        - "a"
        - 10
        - 17
        - 0
        - 0
        - (13/26)
        - (41/26)
        - 2
        - 1
        - (7/26)
        - (20/26)
      * - 11
        - "a"
        - "y"
        - 11
        - 16
        - 0
        - 0
        - (13/26)
        - (41/26)
        - 2
        - 1
        - (7/26)
        - (20/26)
      * - 12
        - "y"
        - " "
        - 12
        - 15
        - 0
        - 1
        - (13/26)
        - (41/26)
        - 2
        - 2
        - (19/26)
        - (32/26)
      * - 13
        - " "
        - "a"
        - 13
        - 14
        - 1
        - 0
        - (26/26)
        - (55/26)
        - 3
        - 2
        - (19/26)
        - (32/26)
      * - 14
        - "a"
        - " "
        - 14
        - 13
        - 0
        - 1
        - (26/26)
        - (55/26)
        - 3
        - 3
        - (33/26)
        - (46/26)
      * - 15
        - " "
        - "y"
        - 15
        - 12
        - 1
        - 0
        - (41/26)
        - (67/26)
        - 4
        - 3
        - (33/26)
        - (46/26)
      * - 16
        - "y"
        - "a"
        - 16
        - 11
        - 0
        - 0
        - (41/26)
        - (67/26)
        - 4
        - 3
        - (33/26)
        - (46/26)
      * - 17
        - "a"
        - "r"
        - 17
        - 10
        - 0
        - 0
        - (41/26)
        - (67/26)
        - 4
        - 3
        - (33/26)
        - (46/26)
      * - 18
        - "r"
        - "d"
        - 18
        - 9
        - 0
        - 0
        - (41/26)
        - (67/26)
        - 4
        - 3
        - (33/26)
        - (46/26)
      * - 19
        - "d"
        - " "
        - 19
        - 8
        - 0
        - 1
        - (41/26)
        - (67/26)
        - 4
        - 4
        - (52/26)
        - (54/26)
      * - 20
        - " "
        - "o"
        - 20
        - 7
        - 1
        - 0
        - (61/26)
        - (74/26)
        - 5
        - 4
        - (52/26)
        - (54/26)
      * - 21
        - "o"
        - "n"
        - 21
        - 6
        - 0
        - 0
        - (61/26)
        - (74/26)
        - 5
        - 4
        - (52/26)
        - (54/26)
      * - 22
        - "n"
        - " "
        - 22
        - 5
        - 0
        - 1
        - (61/26)
        - (74/26)
        - 5
        - 5
        - (74/26)
        - (59/26)
      * - 23
        - "w"
        - "w"
        - 23
        - 4
        - 0
        - 0
        - (61/26)
        - (74/26)
        - 5
        - 5
        - (74/26)
        - (59/26)
      * - 24
        - "a"
        - "a"
        - 24
        - 3
        - 0
        - 0
        - (61/26)
        - (74/26)
        - 5
        - 5
        - (74/26)
        - (59/26)
      * - 25
        - "r"
        - "r"
        - 25
        - 2
        - 0
        - 0
        - (61/26)
        - (74/26)
        - 5
        - 5
        - (74/26)
        - (59/26)
      * - 26
        - "d"
        - "d"
        - 26
        - 1
        - 0
        - 0
        - (61/26)
        - (74/26)
        - 5
        - 5
        - (74/26)
        - (59/26)
    
    Consider :math:`k = 6`. It's corresponding inverted Character position would be :math:`l(ᚠ) - k + 1 = 26 - 6 + 1 = 21`. The Delimiter Counts of the Partial Sentences up to these indices are given by,
    
      - Δ(ᚠ[:6]) = 1
      - Δ(ᚠ[6:]) = 4
      - Δ(ᚠ[:21]) = 5
      - Δ(ᚠ[21:]) = 0
    
    The Delimiter Counts of the Inverse Partial Sentences up to these indices are given by,
    
      - Δ(inv(ᚠ)[:21]) = 4
      - Δ(inv(ᚠ)[21:]) = 1
      - Δ(inv(ᚠ)[:6]) = 0
      - Δ(inv(ᚠ)[6:]) = 5
    
    Note the total number of Delimiters starting at Character Index 1 up to Character Index 6 in the original Sentence is 1. This corresponds to *Δ(ᚠ)[:6]* and to *Δ(inv(ᚠ)[21:])*. In addition, The total number of Delimiters starting at Character Index 26 and working backwards toward Character Index 21 is 0. This corresponds to *Δ(ᚠ)[21:]* and to *Δ(inv(ᚠ)[:6])*.
    
    Since the String Length of the Sentence and its Inverse are both even, by :ref:`Theorem 4.2.3 <theorem-4-2-3>`, the Pivot is given by,
    
    .. math::
    
      \omega{ᚠ} = 13
    
    Using :ref:`Definition 3.2.1 <definition-3-2-1>`, the Delimiter Count is found by first identifying the Character indices of Delimiters in the Sentence and collecting them into the set :math:`D_{ᚠ}`,
    
    .. math::
    
      D_{ᚠ} = \{ (5, \sigma), (8, \sigma), (13, \sigma), (15, \sigma), (20, \sigma) \}
    
    So that the Delimiter Count is found by taking the cardinality of the set :math:`D_{ᚠ}`,
    
    .. math::
    
      \Delta(ᚠ) = \lvert D_{ᚠ} \rvert = 5
    
    The set :math:`D_{ᚠ}` expresses the distance of the Delimiters relative to the start of the Sentence. The distances can be expressed relative to the Pivot by subtracting the value of :math:`\Phi(\zeta)` from each value in :math:`D_{ᚠ}`,
    
    .. math::
    
        \{ (-8, \sigma), (-5, \sigma), (0, \sigma), (2, \sigma), (7, \sigma) \}
    
    
    This makes clear the Delimiters on the left side of the Pivot are further from the Pivot than the Delimiters on the right side. Furthermore, notice the Delimiter Count of the Inverse is calculated with, 
    
    .. math::
        
        D_{\text{inv}(ᚠ)} = \{ (26 - 20 + 1, \sigma), (26 - 15 + 1, \sigma), (26 - 13 + 1, \sigma), (26 - 8 + 1, \sigma), (26 - 5 + 1, \sigma) \}
    
    .. math::
    
        D_{\text{inv}(ᚠ)} = \{ (7, \sigma), (12, \sigma),  (14, \sigma), (19, \sigma), (22, \sigma) \}
    
    Which confirms :ref:`Theorem 3.2.2 <theorem-3-2-2>`,
    
    .. math::
    
      \Delta(ᚠ) = \lvert D_{ᚠ} \rvert = 5
    
    If the Pivot is subtracted from each coordinate in :math:`D_{\text{inv}(ᚠ)}`,
    
    .. math::
    
        \{ (-6, \sigma), (-1, \sigma), (1, \sigma), (6, \sigma), (9, \sigma) \}
    
    When *ᚠ* is inverted, the index at the Pivot is no longer occupied by the same Character,
    
    .. math::
    
      ᚠ[\omega(\zeta)] = ᚠ[13] = \sigma 
    
    .. math::
    
      \text{inv}(ᚠ)[\omega(\zeta)] = \text{inv}(ᚠ)[13] = "a"
      
    The Lefthand Integral of the Original Sentence is,
    
    .. math::
    
      \Phi_{-}(ᚠ ,26) = \frac{61/26} = 2.3461538461538463
    
    The Righthand Integral of the Original Sentence is,
    
    .. math::
      
      \Phi_{+}(ᚠ ,26) = \frac{74/26} = 2.8461538461538463
    
    The midpoint of the integrals is given by,
    
    .. math::
    
      \frac{\Phi_{+}(ᚠ ,26) + \Phi_{-}(ᚠ ,26)}{2} = 2.5961538461538463
    
    The difference of the integrals is given by,
    
    .. math::
    
      \Phi_{+}(ᚠ ,26) - \Phi_{-}(ᚠ ,26)} = 0.5
    
    TODO
    
    .. math::
    
      \Phi_{-}(\text{inv}(ᚠ) ,26) = \frac{74/26} = 2.8461538461538463
    
    TODO
    
    .. math::
      
      \Phi_{+}(\text{inv}(ᚠ),26) = \frac{61/26} = 2.3461538461538463
    
    ∎
    
    From these examples, it can be seen that Sentence Integrals can be regarded as a measure of *"delimiter mass"*. When the Lefthand Sentence Integral is greater than the Righthand Sentence Integral, this is an indication the Sentence has more Delimiters in its right half than its left half. In other words, the Delimiters positions relative to the start of the Sentence sum to a greater number than the Delimiter positions relative to the end.
    
    For the same reason, if the Righthand Sentence Integral is greater than the Lefthand Sentence Integral, this is an indication the Sentence has more Delimiters in its left half than its right half. In other words, the Delimiters positions relative to the end of the Sentence sum to a greater number than the Delimiter positions relative to the start.
    
    This method of *"weighing"* the Delimiters in a Sentence provides a method for abstractly describing the symmetry of Delimiters in Perfect Palindromes. Before using this method to quantify the symmetry of Perfect Palindromes, the next section will strengthen the definitions of Sentence Integrals with some theorems. 
    
    Theorems
    ^^^^^^^^
    
    As the introduction suggested through example a Sentence Integral can be regarded as a measure of the Delimiter symmetry in a Sentence. A Sentence Integral is the sum of the Delimiter indices. Each contribution of the Delimiter Count (0 or 1) to the integral is weighted by its distance from the starting point of the Sentence or the ending point of the Sentence (the Character index of the Delimiter), depending on if the Left- or Right-hand Sentence Integrals are taken. The theorems in this section will establish the properties of this sentential *"center of delimter mass"*.
    
    The first two theorems, :ref:`Theorem 5-1-1 <theorem-5-1-1>` and :ref:`Theorem 5.1.2 <theorem-5-1-2>`, establish the lower bound for all Sentence Integrals. 
    
    .. _theorem-5-1-1:
    
    **Theorem 5.1.1** :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\zeta, k) \geq 0 \land \Phi_{+}(\zeta,) \geq 0`
    
    This theorem can be stated in natural language as follows: Sentence Integrals are always greater than or equal to zero. 
    
    
    Let *ζ* be an arbitrary Sentence in the Corpus,
    
    .. math::
    
      1. \quad \zeta \in C_L
    
    Let *k* be a natural number such that :math:`1 \leq k \leq l(\zeta)`
    
    By :ref:`Definition 5.1.1 <definition-5-1-1>` and :ref:`Definition <definition-5-1-2>`,
    
    .. math::
    
      2. \quad \Phi_{-} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[:i])}{l(\zeta)}
    
    .. math::
    
      3. \quad \Phi_{+} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[i:])}{l(\zeta)}
    
    By :ref:`Definition 3.2.1 <definition-3-2-1>`, :math:`\Delta(\zeta[i])` is either 0 or 1 for all *i*. *l(ζ[:i])*, *l(ζ[i:])*, and *l(ζ)* are all non-negative, by :ref:`Definition 1.1.3 <definition-1-1-3>`. Therefore, each term in the summations is non-negative (The sum of non-negative terms is always non-negative.
    
    Thus, 
    
    .. math::
    
      4. \quad \Phi_{-}(\zeta, k) \geq 0 \land \Phi_{-}(\zeta, k) \geq 0
    
    Since *ζ* and *k* were arbitrary, this can be generalized over the Corpus,
    
    .. math::
    
      5. \quad \forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\zeta,k) \geq 0 \land \Phi_{+}(\zeta,k) \geq 0
    
    ∎
    
    .. _theorem-5-1-2:
    
    **Theorem 5.1.2** :math:`\forall \zeta in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\varsigma(\zeta), k) = \Phi_{+}(\varsigma(\zeta), k) = 0`
    
    This theorem can be stated in natural language as follows: The Sentence Integral of a :math:`\sigma`-reduction is zero.
    
    Let *ζ* be an arbitrary Sentence in the Corpus,
    
    .. math::
    
      1. \quad \zeta \in C_L
    
    and let *k* be a natural number such that :math:`1 \leq k \leq l(\zeta)`.
    
    By :ref:`Definition 3.1.2 <definition-3-1-2>`, the *σ*-reduction of *ζ*, denoted *ς(ζ)*, is a String obtained by removing all Delimiter Characters (*σ*) from *ζ*. Consider the Left-Hand Integral of *ς(ζ)* up to index k:
    
    .. math::
    
      2. \quad \Phi_{-}(\varsigma(\zeta), k) = \sum_{i=1}^{k} \Delta(\varsigma(\zeta)[:i]) \cdot \frac{l(\varsigma(\zeta)[:i])}{l(\varsigma(\zeta))}
         
    By the :ref:`Definition 4.2.1 <definition-4-2-1>` of Left Partial Sentence and Definition 3.1.2 of *σ*-reduction, *ς(ζ)[:i]* is a String contained in *ς(ζ)* from the beginning up to the *i*:sup:`th` Character. Since *ς(ζ)* contains no Delimiters, *ς(ζ)[:i]* will also contain no Delimiters. Therefore, by Theorem A.2.11,
    
    .. math::
    
      3. \quad \forall i \in N_k: \Delta(\sigma(\zeta)[:i]) = 0
       
    Substituting this into step 4,
    
    .. math::
    
      4. \quad \Phi_{-}(\varsigma(\zeta), k) = \sum_{i=1}^{k} 0 \cdot \frac{l(\varsigma(\zeta)[:i])}{l(\varsigma(\zeta))} = 0
       
    By similar logic, 
    
    .. math::
      
      5. \quad \Phi_{+}(\varsigma(\zeta), k) = 0
    
    Thus, both the Left-Hand and Right-Hand Integrals of *ς(ζ)* are equal to 0,
    
    .. math::
    
      6. \quad \Phi_{+}(\varsigma(\zeta), k) = \Phi_{-}(\varsigma(\zeta), k) = 0
       
    Since *ζ* and *k* were arbitrary, this can be generalized over the Corpus,
    
      7. \quad \forall \zeta in C_L: \forall k \in N_{l(\zeta)}: \Phi_{-}(\varsigma(\zeta), k) = \Phi_{+}(\varsigma(\zeta), k) = 0
    
    ∎
    
    The next two theorems provide a method for calculating the Lefthand and Righthand Sentence Integrals numerically.
    
    .. _theorem-5-1-3:
    
    **Theorem 5.1.3** :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[:i])}{l(\zeta)} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{i}{l(\zeta)}`
    
    Let *ζ* be an arbitrary Sentence in the Corpus,
    
    .. math::
    
      1. \quad \zeta \in C_L 
        
    Let *k* be a natural number such that :math:`1 \leq k \leq N_{l(\zeta)}`. By :ref:`Definition 4.2.1 <definition-4-2-1>` of Left Partial Sentences, for any *i* where :math:`1 \leq i \leq l(\zeta)`,
    
    .. math::
    
      2. \quad l(\zeta[:i]) = i
    
    Substituting step 2 into :ref:`Definition 5.1.1 <definition-5-1-1>` of Lefthand Sentence Integrals and generalizing over the Corpus,
    
    ..  math::
    
      3. \quad \forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[:i])}{l(\zeta)} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{i}{l(\zeta)}
    
    ∎
    
    .. _theorem-5-1-4:
    
    **Theorem 5.1.4** :math:`\forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[i:])}{l(\zeta)} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta)-i+1}{l(\zeta)}`
    
    Let *ζ* be an arbitrary Sentence in the Corpus,
    
    .. math::
    
      1. \quad \zeta \in C_L 
        
    Let *k* be a natural number such that :math:`1 \leq k \leq l(\zeta)`. By :ref:`Definition 4.2.2 <definition-4-2-2>` of Right Partial Sentences, for any *i* where :math:`1 \leq i \leq l(\zeta)`, 
    
    .. math::
    
      2. l(\zeta[i:]) = l(\zeta) - i + 1
      
    Substituting step 2 into :ref:`Definition 5.1.2 <definition-5-1-2>` of Righthand Sentence Integrals and generalizing over the Corpus,
    
    .. math::
    
      \forall \zeta \in C_L: \forall k \in N_{l(\zeta)}: \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta[i:])}{l(\zeta)} = \sum_{i=1}^{k} \Delta(\zeta[i]) \cdot \frac{l(\zeta)-i+1}{l(\zeta)}
    
    ∎
    
    As mentioned previously, the terms *(l(ζ) - i + 1)* and *i* that appear in the Sentence Integral summation may be thought of as the *"weight"* of a Delimiter. Since the Delimiter Count is either 0 or 1 for a single Character, the weight assigned to Delimiters, i.e. when :math:`\Delta(\zeta[i]) = 1`, in a Sentence are the only contributions to the summation in a Sentence Integral. This analogy to the mathematical concepts of density and mass is codified in the following definition.
    
    .. _definition-5-1-3:
    
    **Definition 5.1.3: Delimiter Mass**
    
    Let *ζ* be an arbitrary Sentence in the Corpus :math:`C_L`, and let *I* be a natural number such that :math:`1 \leq i \leq l(\zeta)`. 
    
    The Righthand Delimiter Mass at Character Index *i*, denoted :math:`\mu_sub{+}(\zeta, i)`, is defined as,
    
    .. math::
    
      \mu_{+}(\zeta, i) = \Delta(\zeta[i]) \cdot (l(\zeta) - i + 1)
    
    The Lefthand Delimiter Mass at Character Index *i*, denoted :math:`\mu_sub{-}(\zeta, i)` is defined as,
    
    .. math::
    
      \mu_{-}(\zeta, i) = \Delta(\zeta[i]) \cdot i
    
    ∎
    
    The next theorem uses :ref:`Definition 5.1.3 <definition-5-1-3>` to show if the Delimiters in the left half of Sentence relative to the end *"weigh"* more than the Delimiters in the right half relative to the start, then this can only happen if the Righthand Sentence Integral is greater than the Lefthand Sentence Integral. Note the use of the Pivot :math:`\omega(\zeta)` in following theorem.
    
    .. _theorem-5-1-5:
    
    **Theorem 5.1.5** :math:`\forall \zeta \in C_L: \sum_{i=1}^{\omega(\zeta)} \mu_{+}(\zeta,i) > \sum_{\omega(\zeta)+1}^{l(\zeta) \mu_{-}(\zeta, i) \leftrightarrow \Phi_{+}(\zeta, l(\zeta)) > \Phi_{-}(\zeta, l(\zeta))`
    
    
    (→) Let *ζ* be an arbitrary Sentence in the Corpus. Assume,
    
    .. math::
      
      1. \quad \sum_{i=1}^{\omega(\zeta)} \mu_{+}(\zeta,i) > \sum_{i=\omega(\zeta)+1}^{l(\zeta)} \mu_{-}(\zeta,i)
    
    By :ref:`Definition 5.1.3 <definition-5-1-3>`, this is equivalent to,
    
    .. math::
    
      2. \quad \sum_{i=1}^{\omega(\zeta)} \Delta(\zeta[i]) \cdot (l(\zeta - 1 + 1)) > \sum_{i=\omega(\zeta)+1}^{l(\zeta)} \Delta(\zeta[i]) \cdot i
    
    In other words, the assumption in step 1 is equivalent to claiming the sum of the Delimiters weights in the first half of the Sentence (up to and including the Pivot) is greater than the dum of Delimiter weights in the second half (after the Pivot). It is to be shown,
    
    .. math::
    
      2. \quad \Phi_{-}(\zeta, l(\zeta)) > \Phi_{-}(\zeta, l(\zeta))
    
    Expanding the integrals,
    
        1. Ω:sub:`-`(ζ,l(ζ)) = Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (i/l(ζ)) + Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * (i/l(ζ))
    
        2. Ω:sub:`+`(ζ,l(ζ)) = Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) + Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ))
    
    We can rewrite the assumption as:
    
        6. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (l(ζ) - i + 1) > Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * i
    
    Divide both sides by l(ζ):
    
        7. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) > Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * (i/l(ζ))
    
    Notice that the left-hand side of this inequality is part of the Right-Hand Integral *Ω*:sub:`+`(*ζ,l(ζ)*), and the right-hand side is part of the Left-Hand Integral *Ω*:sub:`-`(*ζ,l(ζ)*).
    
    Since *l(ζ) - i + 1* > *i* for all *i ≤ m*, the weighted contribution of each Delimiter in the first half is larger in the Right-Hand Integral than in the Left-Hand Integral.
    
    In addition, for *i > m*, we have *i > l(ζ) - i + 1*, meaning the weights *i/l(ζ)* are greater in the Left-Hand Integral than the corresponding weights *(l(ζ) - i + 1)/l(ζ)* in the Right-Hand Integral. Therefore, if the weighted sum of delimiters in the first half (weighted for the Right-Hand Integral) is greater than the weighted sum of delimiters in the second half (weighted for the Left-Hand Integral), this implies that the overall Right-Hand Integral must be greater than the overall Left-Hand Integral. Thus, 
    
        8. Ω:sub:`+`(ζ,l(ζ)) > Ω:sub:`-`(ζ,l(ζ))
    
    (←) Assume,
    
        1. Ω:sub:`+`(ζ,l(ζ)) > Ω:sub:`-`(ζ,l(ζ))
    
    By Definition A.8.1,
    
        2. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) + Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) > Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (i/l(ζ)) + Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * (i/l(ζ))
    
    Rearranging the terms,
    
        3. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ)) - Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (i/l(ζ)) > Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * (i/l(ζ)) - Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ))
    
    Simplifying,
    
        4. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * ((l(ζ) - 2i + 1)/l(ζ)) > Σ:sub:`i=m+1`:sup:l(ζ)Δ(ζ[i]) * (2i - l(ζ) - 1)/l(ζ)
    
    Since *l(ζ) - 2i + 1 > 0* for *i ≤ m* and *2i - l(ζ) - 1 > 0* for *i > m*, it can be inferred for the inequality to hold, the weighted sum of Delimiters in the first half must be greater than the weighted sum of Delimiters in the second half, where the weights are determined by their distance from the respective ends of the sentence.
    
        5. Σ:sub:`i=1`:sup:`m` Δ(ζ[i]) * (l(ζ) - i + 1) > Σ:sub:`i=m+1`:sup:`l(ζ)` Δ(ζ[i]) * i.
    
    Plugging in Definition A.8.2,
    
        6. Σ:sub:`i=1`:sup:`m` μ:sub:`+`(ζ, i) > Σ:sub:`i=m+1`:sup:`l(ζ)` μ:sub:`-`(ζ, i)
    
    
    Since both directions of the equivalence hold and *ζ* was arbitrary, this can generalize over the Corpus,
     
        ∀ ζ ∈ C:sub:`L``: Σ:sub:`i=1`:sup:`ω(ζ)` μ:sub:`+`(ζ, i)  > Σ:sub:`i=ω(ζ)+1`:sup:`l(ζ)` μ:sub:`-`(ζ, i) ↔ Ω:sub:`+`(ζ,l(ζ)) > Ω:sub:`-`(ζ,l(ζ)) 
      
    ∎
    
    TODO
    
    .. _theorem-5-1-6:
    
    **Theorem 5.1.6** ∀ ζ ∈ PP: ∀ i ∈ N:sub:`l(ζ)`: Ω:sub:`-`(ζ,i) = Ω:sub:`+`(ζ,i)
    
    Let *ζ* be an arbitrary Perfect Palindrome in the Corpus C:sub:`L`,
    
        1. ζ ∈ PP
    
    and let *k* be a natural number such that *1 ≤ k ≤ l(ζ)*. By Definition 3.2.2, since *ζ* is a Perfect Palindrome,
    
       2. ζ = inv(ζ)
       
    This means that the Sentence reads the same forwards as backwards. By Definition A.8.1, the Left-Hand Integral of *ζ* up to index *k* is:
    
       3. Ω:sub:`-`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[:i]) * (l(ζ[:i])/l(ζ))
    
    And the Right-Hand Integral of ζ up to index k is:
    
       4. Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i:]) * (l(ζ[i:])/l(ζ))
       
    It must be shown that,
    
       5. Ω:sub:`-`(ζ,k) = Ω:sub:`+`(ζ,k).
    
    Since *ζ = inv(ζ)*, by Definition 1.2.4 of String Inversion
    
       6. ∀ i ∈ N:sub:`l(ζ)` ζ[i] = inv(ζ)[l(ζ) - i + 1]
    
    Now consider the Delimiter Count Function *Δ(ζ[:i])*. By Definition A.2.1, this function counts the number of Delimiters in the Left Partial Sentence up to index *i*. By Theorem A.2.2, the Delimiter Count is invariant under inversion. 
    
    Furthermore, since *ζ* is a Perfect Palindrome, the Left Partial Sentence up to index i is the inverse of the Right Partial Sentence starting at index l(ζ) - i + 1. In other words:
    
       7. ζ[:i] = inv(ζ[l(ζ) - i + 1:])
       
    Therefore,
    
       8. Δ(ζ[:i]) = Δ(inv(ζ[l(ζ) - i + 1:])) =  Δ(ζ[l(ζ) - i + 1:])
       
    Now consider the Right-Hand Integral,
    
       9. Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i:]) * (l(ζ[i:])/l(ζ))
    
    Make the following change of variables in the summation. Let *j = l(ζ) - i + 1*. Then, as *i* goes from 1 to *k*, *j* goes from *l(ζ)* to *l(ζ) - k + 1*,
    
       10. Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[l(ζ) - j + 1:]) * (l(ζ[l(ζ) - j + 1:])/l(ζ))
       
    Substituting in step 8,
    
       11. Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ[l(ζ) - j + 1:])/l(ζ))
       
    By Theorem 3.2.13, 
    
       12. l(ζ[l(ζ) - j + 1:]) = l(ζ) - l(ζ[:j]) + 1. 
    
    Substituting this into step 11,
    
       13.  Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - l(ζ[:j]) + 1)/l(ζ)
       14.  Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - j + 1)/l(ζ)
    
    Since *ζ* is a Perfect Palindrome,
    
       15.  Δ(ζ[:j]) = Δ(ζ[l(ζ) - j + 1:])
    
    Furthermore, from Definition 3.2.5 of Left Partial Sentences, 
    
       16.  l(ζ[:j]) = j
       
    Substituting step 15 in step 10,
    
       17.  Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - l(ζ[:j]) + 1)/l(ζ)
    
    And then substituting step 16 into step 17,
        
       18.  Ω:sub:`+`(ζ,k) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - j + 1)/l(ζ)
    
    This expression is almost the same as the Left-Hand Integral, except for the summation limits. However, since the summation is over a Perfect Palindrome, by step 6, the terms from *j = k + 1* to *l(ζ)* in the Right-Hand Integral will correspond to the terms from *i = 1* to *l(ζ) - k* in the Left-Hand Integral.
    
    In other words, the terms "missing" in the Right-Hand Integral by summing from *l(ζ) - k + 1 to l(ζ)* are exactly the terms that are "extra" in the Left-Hand Integral by summing from *1* to *k*. Because of the symmetry of the Palindrome and the invariance of the Delimiter Count under inversion, these extra terms will cancel each other out. Formally, 
    
        19. Σ:sub:`i=1`:sup:`k` Δ(ζ[:i]) * (l(ζ[:i])/l(ζ)) = Σ:sub:`j=l(ζ)-k+1`:sup:`l(ζ)` Δ(ζ[:j]) * (l(ζ) - j + 1)/l(ζ)
    
    Therefore,
    
       20.  Ω:sub:`-`(ζ,k) = Ω:sub:`+`(ζ,k)
    
    Since *ζ* and *k* were arbitrary, this can generalize over the class of Perfect Palindromes,
    
       21.  ∀ ζ ∈ PP: ∀ k ∈ N:sub:`Λ(ζ)`: Ω:sub:`-`(ζ,k) = Ω:sub:`+`(ζ,k) 
    
    ∎
    
    As a direct result of Theorem A.8.4, the class of Perfect Palindromes can be regarded as part of the class of Sentences that are *invariant* of Sentence Integrals,
    
        Ω:sub:`-`(ζ,k) - Ω:sub:`+`(ζ,k) = 0
    
    In other words, Perfect Palindromes are a class of sentences that *"balance"* out Delimiter-wise. It stands to reason, given the examples that have been presented so far, and the definition of Imperfect Palindromes as those Palindromes which are *not* Perfect, the class of Imperfect Palindromes *do not* balance out their Delimiters. However, this is not the case, and the reason why this is not the case will illuminate a structural component of language that has heretofore been relegated to novelties like *Zipf's Law*. 
    
    The shortcut formulae for Sentence Integrals given in Theorem 3.3.1 and Theorem 3.3.2, given below, may be viewed as measures of the *distribution* of Delimiters in a Sentence at some Character index *k*,
    
        Ω:sub:`-`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (i/l(ζ))
    
        Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * ((l(ζ) - i + 1)/l(ζ))
    
    Theorem 3.3.5 shows for the highly symmetric and involutive class of Perfect Palindromes, these quantities are perfectly balanced. The Delimiter placement relative to the start of a Perfect Palindrome exactly mirrors the Delimiter placement relative to the end. When these quantities are *not* equal, it is an indication of Delimiter asymmetry in the Sentence. 
    
    However, when these quantities are equal, it cannot be said the Sentence is definitively a symmetric with respect to Delimiters. To see why, the *difference* of the Lefthand and Right Integral may be expressed as,
    
        Ω:sub:`-`(ζ,k) - Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * [i - (l(ζ) - i + 1)]/l(ζ)
    
    Simplifying, 
    
        Ω:sub:`-`(ζ,k) - Ω:sub:`+`(ζ,k) = Σ:sub:`i=1`:sup:`k` Δ(ζ[i]) * (2i - l(ζ) - 1)/l(ζ)
    
    When this quantity equals zero, it leads to a special type of linear, homogenous Diophantine equation,
    
        Σ:sub:`i=1`:sup:`l(ζ)` Δ(ζ[i]) * (2i - l(ζ) - 1) = 0
    
    Where the quantities *Δ(ζ[i])* may be viewed as variables that are constrained to assume the values 0 or 1. In the case of Perfect Palindromes, since every Character has a corresponding inverted Character, the Delimiter symmetry will lead to a perfect cancellation of terms.
    
    It is not the case, however, that this equation only admits of symmetrical solutions. To show this is the case, it suffices to demonstrate a single asymmetrical Delimiter configuration that satisfies the homogenity condition.
    
    To establish the existence of asymmetrical solutions, consider the difference of Sentence Integrals over the entire String Length of the Sentence,
    
        Ω:sub:`-`(ζ,l(ζ)) - Ω:sub:`+`(ζ,l(ζ))
    
    In this case, the summation will range from (1 - l(ζ)) to (l(ζ) - 1). Furthermore, note the coefficient *(2i - l(ζ) - 1)* increases at twice the rate as the index *i* in *Δ(ζ[i]*). This means, depending on the parity of the Sentence, the equation will either consist of odd integer coefficients or even integer coefficients. 
    
    A pair of examples will help illustrate this. 
    
    **Example**
    
    Let :math:`\zeta = (\iota_1)(\iota_2)(\iota_3)(\iota_4)(\iota_5)(\iota_6)`. In this case, :math:`l(\zeta) = 6`. The expansion of the summation can be written,
    
    .. math::
    
      -5 \cdot \Delta(\zeta[1]) -3 \cdot \Delta(\zeta[2]) - 1 \cdot \Delta(\zeta[3]) +1 \cdot \Delta(\zeta[4]) + 3 \cdot \Delta(\zeta[5]) + 5 \cdot \Delta(\zeta[6])
    
    Let :math:`\xi = (\iota_1)(\iota_2)(\iota_3)(\iota_4)(\iota_5)(\iota_6)(\iota_7)`. In this case, :math:`l(\zeta) = 7`. The expansion of the summation can be written,
    
    .. math::
    
      -6 \cdot \Delta(\zeta[1]) -4 \cdot \Delta(\zeta[2]) - 2 \cdot \Delta(\zeta[3]) + 0 \cdot (\Delta(\zeta[4])) + 2 \cdot \Delta(\zeta[5]) + 4 \cdot \Delta(\zeta[6]) + 6 \cdot \Delta(\zeta[7])
    
    Note the Pivot Character, :math:`\omega(\zeta) = 4` , never contributes to an odd sum. ∎
    
    In the odd integer coefficient example, an assignment of :math:`\Delta(\zeta[1]) = \Delta(\zeta[5]) = \Delta(\zeta[6]) = 1` result in a solution that balances the equations to 0. 
    
    In the even integer coefficient example, an assignment of :math:`\Delta(\zeta[1]) = \Delta(\zeta[5]) = Delta(\zeta[6]) = 1` will also result in a solution that balances the equation to 0.
    
    In other words, any time a Character index coefficient can be expressed as the sum of coefficients of other Character indexes, a solution exists. It is worth noting this species of solutions to the Sentence Integral difference expansion does not seem to correspond to meaning Sentence structure, i.e. both solutions correspond to sequences of consecutive Delimiters. 
    
    This cursory analysis suggests, while the Sentence Integral may not provide a necessary and sufficient condition for classifying Imperfect Palindrome's delimiter asymmetry, it may nevertheless be an important diagnostic tool for understanding the distribution of Delimiters in a Corpus of Sentence. 
    
    .. _section-v-ii:
    
    Section V.II: Probability
    -------------------------
    
    A probabilistic framework is now constructed on top of the formal system developed thus far. In particular, a *sample space*, *sigma algebra (event space)* and *probability measure* that conform to the strictures of Kolmogrov's Axioms of Probability are defined in this section.
    
    It is the intention of this analysis to treat the observance of a single Character in a Sentence as an elementary random event. In other words, the integrand in :ref:`Definitions 5.1.1 <definition-5-1-1>` - :ref:`5.1.2 <definition-5-1-2>`, :math:`\Delta(\zeta[i])`, can be understood as a function of a random variable. In other to construct this probabilistic interpretation of Sentence Integrals, it is necessary to define the sample space on which they operate. There lies a problem with this approach that will become apparent after some preliminary notation is introducted. 
    
      1. *Sample Space* (:math:`\Omega`): The uppercase Greek Omega is reserved for the sample space of a probability measure, *P*.
      2. *Sentential Random Variables* (:math:`\hat{\zeta}`, :math:`\hat{\xi}`). When a variable has a hat, it is to be understood as a *random* variable. For instance, :math:`\zeta` is a Sentence Variable, whereas :math:`\hat{\zeta}` is a Sentential Random Variable. 
    
    The event of observing a particular (indeterminate) Sentence :math:`\zeta` is denoted,
    
    .. math::
    
      \hat{\zeta} = \zeta 
    
    Since a String is determined by its concatenated characters, the following equivalence should hold in any probability model,
    
    .. math::
    
      (\hat{\zeta} = \zeta) \leftrightarrow \cap_{i=1}^{l(\zeta)} (\hat{\zeta[i]} = \zeta[i])
    
    To state this plainly: the event of observing a particular Sentence is equivalent to the intersection of the events of observing its individual Characters at their given positions. This formulation of a Sentence event possesses an appealing characteristic, namely that its constitutent Character events are not mutually exclusive, i.e. it cannot happen the event,
    
    .. math::
    
      (\hat{\zeta[1]} = \zeta[1]) \cap (\hat{\zeta[2]} = \zeta[2]) = \emptyset
    
    Unless there are no Sentences in there Corpus that begin with the concatenation :math:`(\zeta[1])(\zeta[2])`. Another way of looking at this same relation would be, for any Character indices *i* and *j* such that :math:`i, j \in N_{l(\zeta)}`,
    
    .. math::
    
      \lvert (\hat{\zeta[j]} = \zeta[j]) \cup (\hat{\zeta[j]} = \zeta[i]) \rvert \geq \lvert \hat{\zeta[j]} = \zeta[j] \rvert + \lvert \hat{\zeta[i]} = \zeta[i] \lvert
    
    As example of this, consider an unknown Sentence :math:`\hat{\zeta}` with fixed String Lenth :math:`l(\zeta) = 8`. The event of :math:`\hat{\zeta[5]} = \text{"w"}` shares outcomes with :math:`\hat{\zeta[6]} = \text{"o"}`. For instance, any Sentence that begin with the phrase, *"the word"* or *"the worm"* would belong to both Character events. 
     
    Given this fact, that a Sentence event is an intersection of simpler Character events, it might seem natural to define the sample space as simply :math:`\Sigma`, but this leads to theoretical difficulties in defining a probability measure, since there is no sigma algebra that can be constructed on this sample space where events would correspond to the event of a Sentence. To see this, note *"not"* and *"ton"* would be considered the same event, namely,
    
    .. math::
    
      E = \{ \text{"n"}, \text{"o"}, \text{"t"} \} = \{ \text{"t"}, \text{"o"}, \text{"n"} \}
    
    This sample space does not capture the ordinality of Strings, i.e. their ability to be ordered in sequence. A possible solution for differentiating outcomes like :math:`(1, \text{"a"})` and :math:`(2, \text{"a"})` in the sample space is to take the Cartesian product of the natural numbers with the Alphabet,
    
    .. math::
    
      \mathbb{N} \times \Sigma
    
    In this way, the event of a Word may be described in a way analogous to :ref:`Definition 1.1.2 <definition-1-1-2>`, where it is associated with a set of ordered pairs,
    
    .. math::
    
      E = \{ (1, \text{"d"}), (2, \text{"o"}), (3, \text{"g"}) \}
    
    More complicated Sentence-level events can then be constructed through unions, intersections and complementations. But this immediately leads to two technical difficulties. 
    
    First, this implies a sample space with infinite cardinality which can lead to overly technical and mathematical caveats to prevent paradoxes and inconsistencies from arising in the probability model. However, this difficulty can be overcome with the adoption of an axiom that prohibits Sentences of infinite length,
    
    .. _axiom-s3:
    
    **Axiom S.3: The Finite Axiom**
    
    .. math::
    
      \exists N \in \mathbb{N}: \forall \zeta \in C_L: l(\zeta) \leq N
    
    ∎
    
    This axiom captures the common-sense notion that every Sentence in a Corpus must be finite. With this addition, the sample space might be defined as,
    
    .. math::
    
      \Omega = \{ (i, \iota) | (i \in \mathbb{N}) \land (1 \leq i \leq N) \land (\iota \in \Sigma_{\epsilon}) \}
    
    Adoption of :ref:`Axiom S.3 <axiom-s3>` and this sample space would immediately solve the problem of infinitude. However, a deeper and more subtle problem lurks in this formulation that cannot be axiomatized away.
    
    If the sigma algebra is defined as the power set of :math:`\mathbb{N} \times \Sigma`, then the complement of **E**, denoted :math:`E^{c}`, would consist of every possible combination of ordered Characters that does not involve :math:`(1, \text{"d"})`, :math:`(2, \text{"o"})` or :math:`(3, \text{"g"})`. For example, the following would be true,
    
    .. math::
    
      \forall i \in \mathbb{N}: (i, \sigma) \in E^{c}
    
    From this, it can be seen the complement of **E** in a :math:`\mathbb{N} \times \Sigma` sample space contains a multiplicity of ordered pairs that cannot be put into any definite order. In other words, :math:`E^c` is not *semantically coherent*. Attempting to restrict the sigma algebra defined on :math:`\mathbb{N} \times \Sigma` to only those strings which are semantic leads to insurmountable obstacles, since the grammatical rules which construct semantically coherent and admissible Strings would need to be known a priori. Moreover, it would need to be shown the operations of complementation and finite unions are closed, which is to say, these operations only produce classes of grammatical Strings. 
    
    A more technically feasible approach would be to define the sample space as the Corpus and then define basis events on this sample space as Character level events. This leads to the following definition,
    
    .. admonition:: TODO
      
      **Definition 5.2.1: Sample Space**
    
      The sample space for a linguistic experiment is the Corpus of its Language, 
    
      .. math::
    
        \Omega = C_L
    
      ∎
    
      TODO
    
      **Definition 5.2.2: Basis Events**
    
      TODO 
    
      .. math::
    
        E_{(i, \iota)} = \{ \zeta \in \Omega | \zeta[i] = \iota \}
    
      ∎
    
      TODO

.. _07postulates:
 
-----------------
07_postulates.rst
-----------------

.. raw:: 

    .. _section-vi:
    
    Section VI.III: Postulates
    --------------------------
    
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
    
    By Theorem 2.2.4 (Λ(ζ) ≥ 1), step 2 and by :ref:`Definition 4.1.1 <definition-4-1-1>`1, there are two possible cases to consider,
    
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
    
    Using :ref:`Definition 4.1.1 <definition-4-1-1>`1, Let 
    
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
    
    .. admonition:: TODO
    
        **Theorem: The Perfect Pivot Postulate**
    
        ζ ∈ PP ↔ [∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:`s` α) ∧ (α ∈ R) ] ∨ (ζ[ω(ζ)] = σ)
    
        Proof:
    
        (→)  Assume ζ ∈ PP (ζ is a Perfect Palindrome).
    
        Word-level representation: Let W:sub:ζ = (α₁ , α₂ , ..., αₙ) be the Word-level representation of ζ, where n = Λ(ζ).
    
        Pivot: Let ω:sub:ζ be the Pivot of ζ. There are two cases:
    
        Case 1: ω:sub:ζ = σ (Delimiter Pivot). In this case, the condition (ω:sub:ζ = σ) is satisfied, and the right-hand side of the biconditional is true.
    
        Case 2: ω:sub:ζ ≠ σ (Non-Delimiter Pivot).
    
        In this case, the Pivot is a Character within a Word. Let k be the index such that αₖ contains ω:sub:ζ.
        Since ζ is a Perfect Palindrome, by :ref:`Definition 4.1.1 <definition-4-1-1>`, ζ = inv(ζ).
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
    
    
    
    
        Reformulation of the Theorem:
    
        Let's first slightly reformulate the theorem to make it even clearer and more precise:
    
        Theorem 3.2.4:
    
        ζ ∈ PP ↔ [ (∃ α ∈ L: (ζ[ω(ζ)] ⊂:sub:s α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (inv(α:sub:ζ:sup:-ω) ⊂:sub:s α:sub:ζ:sup:+ω) ∨ (inv(α:sub:ζ:sup:+ω) ⊂:sub:s α:sub:ζ:sup:-ω)) ]
    
        Translation: A sentence ζ is a perfect palindrome if and only if one of the following conditions holds:
    
        The character at the pivot index ω(ζ) is contained in a reflective word α that is in the language.
        The character at the pivot index ω(ζ) is a delimiter (σ), and the inverse of the left pivot word is contained in the right pivot word, or the inverse of the right pivot word is contained in the left pivot word.
    
        Proof:
    
        (↔) Direction:
    
        Assume ζ ∈ PP.
    
        Definition of Perfect Palindrome: By :ref:`Definition 4.1.2 <definition-4-1-2>`, ζ = inv(ζ).
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
    
    
    
    
        Theorem 3.2.4:
    
        ∀ ζ ∈ PP: (∃ α ∈ L: (ζ[ω(ζ)] ⊂ α) ∧ (α ∈ R)) ∨ (ζ[ω(ζ)] = σ ∧ (α:sub:ζ:sup:-ω ∈ I))
    
        Translation: For every perfect palindrome ζ, either:
    
        There exists a word α in the language L such that the character at the pivot index ω(ζ) is contained in α, and α is a reflective word (α ∈ R), OR
        The character at the pivot index ω(ζ) is a delimiter (σ), and the left pivot word is invertible (α:sub:ζ:sup:-ω ∈ I).
        Proof:
    
        Let ζ be an arbitrary perfect palindrome in PP.
    
        Definition of Perfect Palindrome: By :ref:`Definition 4.1.1 <definition-4-1-1>`, ζ = inv(ζ).
    
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

.. _08appendix:
 
---------------
08_appendix.rst
---------------

.. raw:: 

    .. _section-vii:
    
    Section VII: Appendix
    =====================
    
    This section contains notes and ideas that do not serve to establish the main results of the work, but the author believes may nevertheless prove useful in extending the formal theory into other epistemological domains.
    
    Table of Contents
    ^^^^^^^^^^^^^^^^^
    - Section A.I: Compound Words
    - Section A.II: Palindromic Pairs
    - Section A.III: Categories
    - Section A.IV: Sigma Induction
    - Section A.V: Reflective Structures
    
    Section A.I: Compound Words 
    ---------------------------
    
    .. note::
    
        Part of the ambiguity in imperfect palindromes is that multiple different palindromes can map to the same *σ-reduced* form. When Delimiters are removed from a Sentence, a certain class of Words can remain in the Language, because their semantic content *"transmutes"*. In the author's opinion, the class of Compound Words bears some relation to palindromic structures, but the exact relation has yet to be uncovered.
    
    **Definition A.1.1: Compound Words** η ∈ CW:sub:`L` ↔ [(∃ α, β ∈ L: η = αβ)  ∨  (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ)] ∧ (η ∈ L)
    
    This formalization can be translated into natural language as follows: A Word *η* in a Language **L** is a Compound Word if and only if,
    
        1. Base Case (*∃ α, β ∈ L: η = αβ*) ∧ (η ∈ L):  *η* can be formed by concatenating two words from **L**, and *η* belongs to **L**.
        2. Recursive Step [ (∃ α ∈ L, ∃ γ ∈ CW:sub:`L`: η = αγ) ∧ (η ∈ L) ]: *η* can be formed by concatenating a word from **L** with a Compound Word from **L**, and *η* belongs to **L**. ∎
    
    The constraint *w ∈* **L** ensures that the concatenated String *η* is not just a String, but also a valid Word within the Language **L**.
    
    **Examples**
    
    *"teapot"* is a Compound Word because it can be formed by concatenating *"tea"* and *"pot"*, and *"racecar"* is itself a word in English.
    
    *"nevertheless"* is a Compound Word formed from *"never"*, *"the"*, and *"less"*
    
    *"formrat"* is not a Compound Word, even though it can be formed by concatenating Words from the Language, i.e. *"form"* and *"rat"* are both valid words, the concatenation *"formrat"* is not a valid Word in English.
    
    **Definition A.1.2: Compound Invertible Words** η ∈ CIW:sub:`L`  ↔ [ (η ∈ CW:sub:`L`)  ∧ (η ∈ I) ]
    
    In natural language: A word η in a language **L** is a Compound Invertible Word if and only if it is both a Compound Word and an Invertible Word. Using notation for set intersections, this definition can be revised to read,
    
        CIW:sub:`L` = CW:sub:`L` ∩ I ∎
    
    **Example**
    
    "racecar" is a compound invertible word because it's both a compound word and its own inverse.
    
    Section A.II: Palindromic Pairs
    --------------------------------
    
    The only constraint on a Language is that it must consist of Words. This is guaranteed by the Extraction Axiom S.2. The only constraint on Words is that they must not contain the Delimiter. This is guaranteed by the Delimiter Axiom W.1. 
    
    Since *σ-reduction* removes the Delimiter Character when it projects a Sentence onto the *σ-reduced* Alphabet, this process can viewed as the construction of another formal Language. In other words, given a Language and Corpus, the operation of *σ-reduction* implies the existence of a second Language which encodes the original Sentences. This second Language loses much of its semantic coherence with respect to its "*mother*" Corpus, but it nevertheless contains semantic information. 
    
    This idea motives the definition of a *σ-Pairing Language*.
    
    **Definition A.2.1: σ-Pairing Language**
    
    The σ-Pairing Language L:sub:`σ` of a Corpus C:sub:`L` is defined as the set of Words *α* that satisfy the following formula, 
    
        α ∈ L:sub:`σ` ↔ ∃ ζ ∈ C:sub:`L`: α = (ζ ⋅ Σ:sub:`σ`)
    
    This definition captures the idea that the σ-Pairing Language consists of all the Strings that can be generated by applying σ-reduction to the Sentences in the Corpus. It directly links the elements of L:sub:σ to the σ-reduced forms of the Sentences, ensuring that the Pairing Language is derived from the original Corpus.
    
    **Theorem A.2.1** ∀ α ∈ L: α ∈ L:sub:`σ` ↔ [ ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:s α ]
    
    This theorem can be stated in natural language as follows: The *σ*-Pairing Language contains a Word *α* if and only if there exists a Sentence *ζ* and a Word *β* that belongs to Sentence *ζ* such that *α* is contained in *Ζ ⋅ Σ*:sub:`σ`.
    
    (→) Assume,
    
        1. α ∈ L:sub:`σ`
        
    By Definition A.1.1, 
    
        2. ∃ ζ ∈ C:sub:`L`: α = (Ζ ⋅ Σ:sub:`σ`).
    
    By Definition (TODO) of *σ-reduction*, (*ζ* ⋅ **Σ**:sub:`σ`) is obtained by concatenating the Words *ζ{i}* for 1 ≤ i ≤ Λ(ζ) without Delimiters,
    
        3. α = (ζ ⋅ Σ:sub:`σ`) = (ζ{1})(ζ{2})...(ζ{n})
    
    Since each *ζ{i}* is a contiguous subsequence of *α*, it follows from Theorem 1.2.2,
    
        4. ∀ i ∈ N:sub:`n`: ζ{i} ⊂:sub:`s` α.
    
    Therefore, 
    
        5. ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` α 
    
    (←) Assume,
    
        1. ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` α.
    
    Let *ζ{i}* be the Word in *ζ* such that *1 ≤ i ≤ Λ(ζ)* and
    
        2. ζ{i} ⊂:sub:s α.
    
    By Definition (TODO) of *σ-reduction*, (*ζ* ⋅ **Σ**:sub:`σ`) is obtained by concatenating the Words in *ζ{i}* without Delimiters,
    
        3. (ζ ⋅ Σ:sub:`σ`) = (ζ{1})(ζ{2})...(ζ{n})
    
    Since *ζ{i}* *⊂*:sub:`s` *α* and *α* is a String formed by concatenating Words, it follows that *α* must be a contiguous subsequence of (*ζ* ⋅ **Σ**:sub:`σ`).
    
    Since *α* is a contiguous subsequence of (ζ* ⋅ **Σ**:sub:`σ`) and both are Strings formed by concatenating the same Words in the same order (without Delimiters), it follows that,
    
        4. α = (ζ ⋅ Σ:sub:`σ`).
    
    Therefore, by Definition 3.1.3,
    
        5. α ∈ L:sub:`σ` 
    
    Since both directions of the implication has been proven, the theorem is established:
    
        ∀ α ∈ L: α ∈ L:sub:`σ` ↔ [ ∃ ζ ∈ C:sub:`L`: ∃ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:s α ] ∎
    
    This theorem effectively characterizes the elements of the σ-Pairing Language. It states that a String belongs to the σ-Pairing Language if and only if it contains a Word from some Sentence in the Corpus. This highlights the connection between the σ-Pairing Language and the original Language and Corpus.
    
    **Definition A.2.2: Palindromic Pairing Language**
    
    Definition A.1.4 is altered in the following definition to quantify over the set of Palindromes in a Corpus. The Pairing Language that results is denoted L:sub:`P`. The set of Words *α* which satisfy this definition are referred to as the Palindromic Pairing Language of Language **L**, 
    
        α ∈ L:sub:`P` ↔  ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)
    
    In particuar, if *α ∈ L*:sub:`P`, *α* is called the *Palindromic Image* of the Sentences *ζ* which generate it.
    
    This definition is used to prove the following theorems.
    
    **Theorem A.2.2** L:sub:`P` ⊂ L:sub:`σ`
    
    Assume 
        
        1. α ∈ L:sub:`P`
    
    By Definition A.1.2,
    
        ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)
    
    By Definition 3.2.1 of Palindromes, the set of Palindromes **P** is a subset of C:sub:`L`. Therefore, 
    
        ζ ∈ C:sub:`L`
    
    From step 2 and step 3, by Definition A.1.1, it follows,
    
        α ∈ L:sub:`σ`.
    
    Therefore, 
        
        α ∈ L:sub:`P` → α ∈ L:sub:`σ`
        
    This is exactly the definitio of a subset,
    
        L:sub:`P` ⊂ L:sub:`σ`. ∎
    
    **Theorem A.2.3**: ∀ α ∈ L:sub:`P`: α = inv(α)
    
    This theorem can be stated in natural language as follows: All Words in a Palindromic Pairing Language are their own Inverses. 
    
    Assume 
    
        1. α ∈ L:sub:`P`. 
        
    By Definition A.1.2,
    
        2. ∃ ζ ∈ P: α = (ζ  ⋅ Σ:sub:`σ`)
    
    Since *ζ* *∈* **P**, by Definition TODO:
    
        3. (ζ  ⋅ Σ:sub:`σ`) = inv(ζ  ⋅ Σ:sub:`σ`)
    
    Substituting *α* from step 2 into the equation in step 3,
    
        4. α = inv(α)
    
    Therefore, 
    
        ∀ α ∈ L:sub:`P`: α = inv(α). ∎
    
    This proof demonstrates that every String in the Palindromic Pairing Language is its own inverse. This follows directly from the definitions of Palindromes and the Palindromic Pairing Language. Since every String in the Palindromic Pairing Language is derived from a Palindrome, and Palindromes are defined by the invariance of their *σ-reduction* under inversion, the Strings in the Palindromic Pairing Language must also exhibit this invariance.
    
    This theorem highlights a key property of the Palindromic Pairing Language: it consists solely of Strings that are symmetrical with respect to inversion. This property could be useful in various applications, such as identifying potential palindromes or generating text with specific symmetrical structures.
    
    **Theorem A.2.4** L ∩ L:sub:`P` ⊆ R
    
    This theorem can be stated in natural language as follows: The intersection of a Language **L** and its Palindromic Pair **L**:sub:`P` is a subset of the Language's Reflective Words **R**.
    
    Assume 
    
        1. α ∈ L ∩ L:sub:P.
    
    Since *α* *∈* **L**, it is a Word in the Language. Since *α* *∈* **L**:sub:`P`, by Theorem A.1.3, 
    
        α = inv(α).
    
    By Definition 1.2.4 of String Inversion,
    
        ∀ i ∈ N:sub:`l(α)`: α[i] = α[l(α) - i + 1]
    
    By Definition 1.3.1, it follows,
    
        α ∈ R.
    
    Therefore, 
    
        α ∈ L ∩ L:sub:`P` → α ∈ R. 
        
    This in turn implies,
    
        L ∩ L:sub:`P` ⊆ R. ∎
    
    Before moving onto the last theorem of this section, some terminology is introduced. **R** was introduced in Section I.III to refer to the class of Reflective Words in a Language **L**. To be more explicit in the dependence of **R** on **L**, the notation **R**:sub:`L` will be used to make explicit the Language to which the class of Reflective Words refers.
    
    With this notation adopted, the following theorem can be proven.
    
    **Theorem A.2.5** L:sub:`P` ⊂ R:sub:`L_σ`
    
    This theorem can be state in natural language as follows: Given a Language L, all words in its Palindromic Pairing Language are also Reflective Words in the σ-Pairing Language. 
    
    In other show this theorem, it must be shown,
    
        1. ∀ α ∈ L: α ∈ L:sub:`P` → α ∈ R:sub:`L_σ`
    
    Since by Definition 1.3.1, 
    
        2. α ∈ R:sub:`L_σ` ↔ inv(α) = α
    
    If it can be shown,
    
        3. α ∈ L:sub:`P` → inv(α) = α
    
    Then the theorem will follow tautologically from the laws of deduction. But step 3 is exactly Theorem 3.1.9. Therefore, the proof is complete. ∎
    
    Section A.III: Categories
    -------------------------
    
    Before introducing the notion of Categories, it must be kept in mind a Language **L** and a Corpous **C**:sub:`L` are treated as fixed sets known a priori to the construction of the current formal system. In a sense, Language and its Corpus are taken as primitive terms. It assumed a semantic assignment has occured outside of the confines of the formal system and the Words of a Language and Sentences of a Corpus have already been given determinate meanings. 
    
    The notion of a *Category* is meant to explicate the linguistic entities which are colloquially referred to as a *"parts of speech"*, e.g nouns, verbs, adjectives, etc. However, it not the intention of this formal system to treat the semantic meaning of these grammatical categories in so far that certain schema of Categories provide a method of constructing semantic Sentences. The formal system takes no opinion on what constitutes its Categories, or how these Categories are used to construct a grammatical and meaningful Sentence; rather, the formal system assumes these Categories are used in exactly that capacity in order to derive the syntactical constraints they must abide in order to be considered categorical. 
    
    This does not preclude the idea that a Category could map to the everyday notion of *noun* or *verb*, but the formal construction of grammatical categories cannot assume anything about the categorical structure of Sentences (e.g. noun-verb-noun is a valid Sentence form) without tying it to a specific semantic interpretation of what qualifies a Word to function in its categorical capacity. 
    
    **Definition A.3.1: Category**
    
    A semantic Category in a language **L**, denoted C:sub:`L`(m), is a set of Words in **L**, where *m* is a natural number representing the Category's index. ∎
    
    Axioms 
    ^^^^^^
    
    The fundamental assumptions regarding linguistic Categories in this formal system are now introduced. Each axiom will be justified by appeal to self-evidence. To see the motivation behind the first formal assumption about Categories adopted, note that every Word in a Language plays the role of a "part of speech". Grammar requires that any Word that is employed must belong to *at least* one grammatical categories, e.g. *noun*, *verb*, etc.
    
    **Axiom G.1: The Aggregation Axiom**
    
        ∃ m ∈ ℕ: L = ∪:sub:`1`:sup:`m` C:sub:`L`(i) ∎
    
    This leads to the Definition of a Languages's *Categorical Size*. By this, it is meant the total number of grammatical Categories that span the Language set through their union. In other words, Language can be conceived as the aggregation of all its grammatical Categories.
    
    **Definition A.3.1 Categorical Size**
    
    The *m* such that,
    
        L = ∪:sub:`1`:sup:`m` C:sub:`L`(i)
    
    is denoted with the lowercase Greek kappa, *κ*. *κ* is called the Categorical Size of a Language. ∎
    
    It is important to note, the formal system takes no opinion on the nature of its Categories, i.e. what role a particular Category serves in the formation of a grammatical Sentence. Instead, the Aggregation Axiom G.2 simply states, no matter the semantic function assigned to a Category, it must obtain syntactically that these assignments must span the entire set of Language. 
    
    The choice of axioms for governing the logical calculus of Categories in the formal system is critical. Since the notion of a *"grammatical categories"* is inherently tied to the semantic interpretation of a Language and Corpus, the assumptions introduced about their nature must not violate the empirical reality of natural languages. 
    
    To see what is meant by this, consider the proposed axiom, the Uniqueness Axiom.
    
    **Proposed Axiom: The Uniqueness Axiom**
    
        ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: (∃! m ∈ N:sub:`κ`: ζ{i} ∈ C:sub:`L`(m)) ∧ ( (i, C:sub:`L`(m)) ∈ C:sub:`ζ` ) ∎
    
    In natural language, the Uniqueness Axiom states: For every sentence *ζ* in the Corpus and for every Word index *i* in *ζ*, there exists a unique Category index *m* such that the *i*:sup:`th` Word of *ζ* belongs to Category **C**:sub:`L`(*m*), and this Category is recorded in the Categorical-level representation **C**:sub:`ζ` at index *i*.
    
    This axiom captures a common-sense (though subtly flawed) notion that each Word in a Sentence maps to a single Category. However, this picture of *"grammaticality"* is tacitly assuming a *single* available semantic interpretation. To see a concrete example of why this axiom should not be adopted in a formal system that is meant to model *any* language, it suffices to look at a single example in a known language which contradicts it.
    
    Consider the sentence *ᚠ = "visting friends can be annoying"*. In this case,there are two valid Categorical-level representations of this Sentence in English,
    
    
        C:sub:`ζ`:sub:`1` = { (1, Verb), (2, Noun), (3, Verb), (4, Verb), (5, Adjective) }
        
        C:sub:`ζ`:sup:`2` = { (1, Adjective), (2, Noun), (3, Verb), (4, Verb), (5, Adjective) }
    
    Therefore, if the formal system wishes to account for the subtle ambiguities of natural language, the Uniqueness Axiom can not be adopted as an assumption.
    
    Theorems
    ^^^^^^^^
    
    **Theorem A.3.1**: ∀ α ∈ L: ∃ i ∈ N:sub:`κ`: α ∈ C:sub:`L`(i)
    
    By Axiom G.1, 
    
         L = ∪:sub:`1`:sup:`m` C:sub:`L`(i)
    
    Therefore, any word *α* in **L** must belong to at least one of these Categories. ∎
    
    Categorical Length
    ^^^^^^^^^^^^^^^^^^
    
    Consider the English sentences, *ᚠ = "the man ran over the bridge* and *ᚢ = "the novel novel about a rose rose to the top"*
    
    In *ᚠ*, both *"man"* and *"bridge"* map to the same Category, namely *nouns*. In other words, the Sentence can have multiple Words that belong to the same Category.  
    
    In *ᚢ*, both occurrences of *"novel"* map to different Categories, namely *adjectives* and *nouns*. Further confounding the matter, another example of the ability of a single Word to map to multiple Categories is given through the simultaneous *noun*-*verb* mapping of *"rose"*
    
    Since multiple Words can belong to the same Category, and conversely, the same Word can belong to multiple Categories, a notion of measuring the *Categorical Length* of a Sentence is now introduced. This notion will only measure the *unique* Categories found in a Sentence. For example, *"man"* and *"bridge"* would both be occurrences of the *noun* Category and would thus contribute a length of 1 to *Categorical Length*.
    
    Similar to the construction of the Character-level and Word-level representation of a String, a method for constructing the Category-level representation of a Sentence is given below in the next definition. 
    
    **Definition A.4.2: Categorical-level Representation**
    
    Let *ζ* be an arbitrary sentence from Corpus C:sub:`L`. The Categorical-level representation of a *ζ*, denoted **C**:sub:`ζ`, is defined as the set of sets *x* which satisfy the following open formula,
    
    
        x ∈ C:sub:`ζ` ↔ x = { (i, C:sub:`L`(m)) | ∀ i ∈ N:sub:`Λ(ζ)`: (ζ{i} ∈ C:sub:`L`(m)) } ∎
    
    **Definition A.4.3: Categorical Interpretation**
    
    Let *ζ* be an arbitrary sentence from Corpus C:sub:`L`. The *i*:sub:`th` Categorical Interpretation of *ζ*, denoted C:sub:`ζ`(i), is defined as,
    
    
        C:sub:`ζ`(i) ∈ C:sub:`ζ` ∎
    
    **Definition A.4.4: Interpretation Length**
    
    Let *ζ* be an arbitrary sentence from Corpus C:sub:`L`.  The *Interpretation Length* of a Sentence *ζ*, denoted by *ι(ζ)*, is defined as the number such that,
    
        ι(ζ) = | C:sub:`ζ` | ∎
    
    **Definition A.4.5: Categorical Length**
    
    Let *ζ* be an arbitrary sentence from Corpus C:sub:`L`. The *Categorical Length* of the *i*:sup:`th` Categorical Interpretation of *ζ*, denoted *λ(ζ, i)*, is defined as,
    
        λ(ζ, i) = | C:sub:`ζ`(i) | ∎
    
    Section A.V: Sigma Inductions
    -----------------------------
    
    The operation of *σ*-reduction possesses unique characteristics that distinguish it from typical arithemtical or geometrical operations studied in abstract algebra. If linguistics is said to have an algebraic structure and *σ*-reduction is to be identified as it one of its essential components, then this presents a problem with respect to the operation which is to be understood as the *inverse* of *σ*-reduction. Strictly speaking, *σ*-reduction does not possess an inverse operation. Once a Sentence has been projected onto the *σ*-reduced Alphabet, necessary and sufficient information for the construction of its semantic interpretation has been lost. However, analogous to the case of a square root, this does not imply an a *σ*-induction cannot be defined, if the range of its inversion is suitably restricted. 
    
    The analysis of this problem will carry the work heavily into combinatorics. This section of the Appendix is a preliminary analysis of the challenges and problems any formulation of *σ*-induction must overcome in order to claim validity as a linguistic operation.
    
    To start, note that knowing the length of a *σ*-reduced Sentence, *l(ς(ζ))*, and the number of Words in the original Sentence, *Λ(ζ)*, significantly constrains the possibilities for reconstructing the original Sentence from its σ-reduced form. This has implications for the potential reversibility of σ-reduction and for understanding the structure of Sentences.
    
    *l(ς(ζ))* contains information about the non-Delimiter Characters in the original Sentence *ζ*, and their relative ordering, as demonstrated by Theorem 3.1.6. In other words, although the Word are no longer delimited, the *σ*-reduction of a Sentence still contains every Word in the original Sentence, 
    
        ∀ ζ ∈ C:sub:`L`: ∀ i ∈ N:sub:`Λ(ζ)`: ζ{i} ⊂:sub:`s` ς(ζ)
    
    If the additional piece of information Λ(ζ) is at hand, then from Theorem 2.4.1,
    
        Λ(ζ) = Δ(ζ) + 1. 
        
    In other words, the number of Delimiters is always one less than the number of Words. This provides a constraint on the number of possible combinations that need considered when inducing in the *σ*-reduced space. The delimiters must be placed between the Words in a way that creates valid Words in the Language **L** and not all arrangements of Delimiters will result in valid wWrds.
    
    The problem of reconstructing the original Sentence from its *σ*-reduced form and the number of Words is analogous to the problem of integer partitioning in number theory. Integer partitioning is the problem of finding all possible ways to write an integer as a sum of positive integers. For example, the integer 4 can be partitioned in the following ways,
    
        4
        3 + 1
        2 + 2
        2 + 1 + 1
        1 + 1 + 1 + 1
    
    In the case of *σ*-reductions, the String Length of the reduction, *l(ς(ζ))*, is analogous to the integer being partitioned, while *Λ(ζ)* is analogous to the number of parts in the partition. The String Lengths of the individual words in the sentence are analogous to the summands in the partition.
    
    While σ-reduction is not strictly reversible, knowing *l(ς(ζ))* and *Λ(ζ)* significantly reduces the number of possible Sentences that could have produced the given *σ*-reduced form. 
    
    In some cases, if the Language **L** has strong constraints on Word formation and if *l(ς(ζ))* and *Λ(ζ)*, are sufficiently restrictive, it is conceivable to uniquely reconstruct the original Sentence, or at least narrow it down to a small set of possibilities. 
    
    These insights lead to a formal definition of a *σ*-induction.
    
    .. admonition:: TODO
            
        **Definition A.4.1: σ-induction**
    
        Let s be a string in Σ:sub:σ (a σ-reduced string), let m be a natural number representing the desired number of "word-forms" (intended to correspond to words or potentially other linguistic units) in the resulting strings, and let X be a set of strings (either S, the set of all strings, or C:sub:L, the set of sentences in language L).
    
        The σ-induction of s with m word-forms over the set X, denoted σ_induce(s, m, X), is the set of all possible strings that can be formed by inserting m-1 delimiters into s such that:
    
        Delimiter Placement: Delimiters are inserted only between characters of s or at the beginning or end of s.
        Word-Form Validity: Each of the m resulting substrings (separated by delimiters) is a valid string in the set X.
        Number of Word-Forms: The resulting string has exactly m word-forms.
        Order Preservation: The relative order of the characters in s is preserved in the resulting string.
        Formally:
    
        σ_induce(s, m, X) = { x ∈ X | σ_reduce(x) = s and Λ(x) = m }
    
        Explanation:
    
        Input: The function takes a σ-reduced string s, the desired number of word-forms m, and a set of strings X as input.
        Output: It returns a set of strings, where each string is a possible "re-delimitation" of s that satisfies the given conditions, and Crucially, each "re-delimitation" belongs to the set X..
        Conditions:
        Delimiter Placement: Ensures that delimiters are placed in valid positions.
        Word-Form Validity: Ensures that all the resulting substrings are valid members of the set X. If X = S, then no check is made beyond ensuring the substrings are valid strings. If X = C:sub:L, then each substring is verified as a valid word in the Language L.
        Number of Word-Forms: Ensures that each string has exactly m word-forms.
        Order Preservation: Ensures that the non-delimiter characters in the resulting strings maintain the same order as in the input string s.
        Examples:
    
        Let s = "nowart" and L = { "no", "now", "wart", "art", "a", "on" }.
    
        σ_induce(s, 2, S) = { "no wart", "now art", "noσwart", "nowσart", ...}
        σ_induce(s, 2, C:sub:L) = { "no wart", "now art" }
        σ_induce(s, 3, S) = { "noσwart", "nowσart", ...}
        σ_induce(s, 3, C:sub:L) = { } (no valid sentences with 3 words)
        Observations:
    
        Flexibility: This definition allows us to perform σ-induction over different sets of strings, providing flexibility in our analysis.
        Relationship to Previous Definitions:
        σ_induce(s, m, C:sub:L) is equivalent to our previous definition where the resulting strings had to be valid sentences in the language L.
        σ_induce(s, m, S) is equivalent to the original idea where we considered all possible strings, regardless of whether they were valid sentences.
        Further Considerations:
    
        Computational Complexity: Generating σ_induce(s, m, S) is computationally simpler than generating σ_induce(s, m, C:sub:L), as it doesn't require checking for word validity in L.
        Linguistic Relevance: σ_induce(s, m, C:sub:L) is more linguistically relevant, as it focuses on valid sentences.
        Empty String: It might be worth explicitly stating what happens when s is the empty string or when m is less than 1.
        This revised definition of σ-induction is a significant improvement. It's more general, flexible, and addresses the distinction between inducing over all strings and inducing over sentences in a specific language. It also clarifies the concept of "word-forms" which might not always be actual words, but could represent other linguistic units in the future.
    
    
        **Theorem** 
    
        Here's the corrected theorem statement and a revised proof:
    
        Corrected Theorem 3.1.16:
    
        ∀ s ∈ S, ∀ m ∈ ℕ: |σ_induce(s, m, C:sub:L)| ≤ C(l(σ_reduce(s)), m - 1)
    
        Translation: For any string s and any natural number m (representing the number of words), the cardinality of the set of sentences in C:sub:L obtained by σ-induction of s with m words is less than or equal to the number of combinations of choosing m-1 delimiter positions from l(σ_reduce(s)) possible positions.
    
        Proof:
    
        Let s be an arbitrary string in S, and let m be a natural number.
    
        Length of σ_reduce(s): Let n = l(σ_reduce(s)). Since s is a σ-reduced string, it has no delimiters.
    
        Delimiter Positions: In order to form a sentence with m words from σ_reduce(s), we need to insert m-1 delimiters.
    
        Possible Positions: There are n-1 possible positions where we can insert delimiters between the characters of σ_reduce(s).
    
        Combinations: The number of ways to choose m-1 positions out of n-1 positions is given by the binomial coefficient C(n-1, m-1), which is calculated as:
    
        C(n-1, m-1) = (n-1)! / [(m-1)! * (n-m)!]
        Upper Bound: The set σ_induce(s, m, C:sub:L) contains sentences formed by inserting m-1 delimiters into s such that the resulting substrings are valid words in L. Since there are at most C(n-1, m-1) ways to insert the delimiters, the number of valid sentences in σ_induce(s, m, C:sub:L) cannot be greater than this number.
    
        Conclusion: Therefore:
    
        |σ_induce(s, m, C:sub:L)| ≤ C(l(σ_reduce(s)), m - 1)
        Since s and m were arbitrary, we can generalize:
    
        *   ∀ s ∈ S, ∀ m ∈ ℕ: |σ_induce(s, m, C:sub:`L`)| ≤ C(l(σ_reduce(s)), m - 1)
        This completes the proof. ∎
    
        Explanation:
    
        The proof now correctly operates on the string s in S.
        The binomial coefficient C(n-1, m-1) gives us the maximum number of ways to insert delimiters, but the actual number of valid sentences might be less due to the constraint that the resulting substrings must be valid words in L.
    
        Implications:
    
        Upper Bound: This theorem provides an upper bound on the number of possible sentences that can be generated by σ-induction.
        Combinatorial Nature: It highlights the combinatorial nature of the problem of reconstructing sentences from their σ-reduced forms.
        Language Constraints: The actual number of valid sentences will be less than or equal to C(l(σ_reduce(s)) - 1, m - 1) and will depend on the specific constraints imposed by the language L.
    
    
        Simplified Problem:
    
        We now have:
    
        s: A σ-reduced string (with no delimiters).
        m: The desired number of "words" (or substrings separated by delimiters).
        σ_induce(s, m, S): The set of all strings formed by inserting m-1 delimiters into s, with the only constraint being that delimiters can be placed at the beginning or end of s or between any two characters of s.
        Calculation:
    
        Length of s: Let n = l(s).
    
        Possible Delimiter Positions: There are n-1 positions between the characters of s, plus the position before the first character and the position after the last character. So, there are a total of n+1 potential positions for delimiters. However, we know no delimiters can be in a word, so there are n-1 positions where m-1 delimiters can be placed.
    
        Choosing Delimiter Positions: We need to choose m-1 positions out of these n-1 valid positions. Since the order of placing delimiters doesn't matter, this is a combination problem.
    
        Combinations: The number of ways to choose m-1 positions from n-1 is given by the binomial coefficient:
    
        C(n-1, m-1) = (n-1)! / [(m-1)! * (n-m)!]
        Theorem 3.1.17:
    
        ∀ s ∈ Σ:sub:σ, ∀ m ∈ ℕ: |σ_induce(s, m, S)| = C(l(s) - 1, m - 1)
    
        Proof:
    
        Let s be an arbitrary σ-reduced string in Σ:sub:σ, and let m be a natural number.
    
        Length of s: Let n = l(s).
    
        Delimiter Positions:  To form a string with m words from s, we need to insert m-1 delimiters.
    
        Possible Positions: In a σ-reduced string of length n, there are n-1 positions between the characters where delimiters can be inserted.
    
        Combinations: The number of ways to choose m-1 positions out of n-1 positions is given by the binomial coefficient C(n-1, m-1):
    
        C(n-1, m-1) = (n-1)! / [(m-1)! * (n-m)!]
        σ_induce(s, m, S): The set σ_induce(s, m, S) contains all strings formed by inserting m-1 delimiters into s in any of the possible positions. Since each combination of delimiter placements results in a unique string, the cardinality of σ_induce(s, m, S) is equal to the number of possible combinations.
    
        Conclusion: Therefore:
    
        |σ_induce(s, m, S)| = C(l(s) - 1, m - 1)
        Since s and m were arbitrary, we can generalize:
    
        *   ∀ s ∈ Σ:sub:`σ`, ∀ m ∈ ℕ: |σ_induce(s, m, S)| = C(l(s) - 1, m - 1)
        This completes the proof. ∎
    
    
        Let's prove this formula using a combinatorial argument known as "stars and bars":
    
        Theorem 3.1.17: ∀ s ∈ Σ:sub:σ, ∀ m ∈ ℕ: |σ_induce(s, m, S)| = C(l(s) + m - 2, m - 1) = C(l(s) + m - 2, l(s) - 1)
    
        Proof:
    
        Let s be an arbitrary σ-reduced string in Σ:sub:σ, and let m be a natural number.
    
        Length of s: Let n = l(s).
    
        Delimiter Positions: To form a string with m "words" (substrings separated by delimiters) from s, we need to insert m-1 delimiters.
    
        Possible Positions: In a string of length n, there are n-1 positions between the characters where we can potentially place delimiters. Additionally, we can place delimiters at the beginning or the end of the string. However, we must exclude the possibility of placing two delimiters consecutively, or placing a delimiter next to an already existing delimiter.
    
        Stars and Bars: We can represent the characters of s as "stars" (*) and the delimiters as "bars" (|). For example, if s = "abc" and we want to insert 2 delimiters (m=3), one possible arrangement is:
    
        "a|b|c" (represented as ||*)
        Another arrangement could be:
    
        "|abc|" (represented as |***|)
        Notice that we have n "stars" and m-1 "bars".
    
        Combinatorial Problem: The problem of placing m-1 delimiters in a string of length n is equivalent to arranging n "stars" and m-1 "bars" in a sequence. However, we must make the restriction that no two bars can be adjacent to each other. This is not possible if we are inducing over the set of all strings S, since we are explicitly allowing for any possible combination of delimiters and characters, so long as no two delimiters are adjacent.
    
        Number of Arrangements: The number of ways to arrange n stars and m-1 bars is given by the binomial coefficient C(n + m - 1, m - 1) or equivalently C(n + m - 1, n). However, since we do not allow for two delimiters to be adjacent in our definition of the delimiter count function, we must subtract one from each star to get the correct value. Since n = l(s), there are C(l(s) + m - 2, m - 1) possible ways to arrange the delimiters.
    
        σ_induce(s, m, S): The set σ_induce(s, m, S) contains all strings formed by inserting m-1 delimiters into s in any of the possible positions. Since each combination of delimiter placements results in a unique string, the cardinality of σ_induce(s, m, S) is equal to the number of possible combinations, C(l(s) + m - 2, m - 1).
    
        Conclusion: Therefore:
    
        |σ_induce(s, m, S)| = C(l(s) + m - 2, m - 1)
        Since s and m were arbitrary, we can generalize:
    
        *   ∀ s ∈ Σ:sub:`σ`, ∀ m ∈ ℕ: |σ_induce(s, m, S)| = C(l(s) + m - 2, m - 1) = C(l(s) + m - 2, l(s) - 1)
    
    
    
    
    
        How This Helps with σ-induction:
    
        The theorems about delimiter symmetry in perfect palindromes (3.2.4 and 3.2.5) are key to simplifying the calculation of |σ_induce(s, m, S)| when s is the σ-reduction of a perfect palindrome.
    
        Here's how:
    
        Reduced Search Space: Instead of considering all possible delimiter placements in s, we only need to consider placements in the left half of s (up to the pivot). The placements in the right half are then determined by symmetry.
    
        Simplified Combinations:
    
        For even-length perfect palindromes with an even number of words m, we need to choose (m-2)/2 delimiter positions in the left half (of length l(s)/2).
        For even-length perfect palindromes with an odd number of words m, we need to choose (m-1)/2 delimiter positions in the left half (of length l(s)/2).
        For odd-length perfect palindromes with an even number of words m, we need to choose (m-2)/2 delimiter positions in the left half (of length (l(s)-1)/2).
        For odd-length perfect palindromes with an odd number of words m, we need to choose (m-1)/2 delimiter positions in the left half (of length (l(s)-1)/2).
        Calculating |σ_induce(s, m, S)| for Perfect Palindromes:
    
        Let's derive formulas for each case, assuming s is the σ-reduction of a perfect palindrome ζ (i.e., s = σ_reduce(ζ) and ζ ∈ PP):
    
        Case 1: Even-length s (l(s) = 2k), Even m (m = 2j):
    
        |σ_induce(s, m, S)| = C(k - 1, j - 1) = C(l(s)/2 - 1, m/2 - 1)
        Case 2: Even-length s (l(s) = 2k), Odd m (m = 2j + 1):
    
        |σ_induce(s, m, S)| = C(k - 1, j) = C(l(s)/2 - 1, (m-1)/2)
        Case 3: Odd-length s (l(s) = 2k + 1), Even m (m = 2j):
    
        |σ_induce(s, m, S)| = C(k - 1, j - 1) = C((l(s)-1)/2 - 1, m/2 - 1)
        Case 4: Odd-length s (l(s) = 2k + 1), Odd m (m = 2j + 1):
    
        |σ_induce(s, m, S)| = C(k - 1, j - 1) = C((l(s)-1)/2 - 1, (m-1)/2)
        Explanation:
    
        We divide the length of s by 2 (or subtract one and then divide by 2 for odd-length s) to get the length of the left half.
        We divide m by 2 (or subtract one or two depending on parity and then divide by 2) to get the number of delimiters to place in the left half.
        We use the combination formula C(n, r) to calculate the number of ways to choose r delimiter positions from n available positions.
    
    
        Theorem 3.2.6:
    
        Let ζ ∈ PP with s = σ_reduce(ζ), n = l(s), and m be the desired number of words. Then:
    
        Case 1: Even-length s (n = 2k), Even m (m = 2j):
    
        |σ_induce(s, m, S)| = C(k - 1, j - 1) = C(n/2 - 1, m/2 - 1)
        Case 2: Even-length s (n = 2k), Odd m (m = 2j + 1):
    
        |σ_induce(s, m, S)| = C(k - 1, j) = C(n/2 - 1, (m-1)/2)
        Case 3: Odd-length s (n = 2k + 1), Even m (m = 2j):
    
        |σ_induce(s, m, S)| = C(k - 1, j - 1) = C((n-1)/2 - 1, m/2 - 1)
        Case 4: Odd-length s (n = 2k + 1), Odd m (m = 2j + 1):
    
        |σ_induce(s, m, S)| = C(k, j) = C((n-1)/2, (m-1)/2)
        Proof:
    
        Let ζ be an arbitrary perfect palindrome (ζ ∈ PP) and let s = σ_reduce(ζ), n = l(s), and m be the desired number of words.
    
        Case 1: Even-length s (n = 2k), Even m (m = 2j):
    
        Pivot: Since n is even, the pivot of ζ falls between two characters. By Theorem 3.1.9, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1. Since ζ is a perfect palindrome, by theorem 3.1.6, σ_reduce(ζ) = inv(σ_reduce(ζ)). The pivot of s lies between the characters at indices k and k+1.
    
        Delimiter Placement: To form m = 2j words, we need to place m-1 = 2j-1 delimiters. By Theorem 3.2.4, the delimiters must be placed symmetrically around the pivot. We place j-1 delimiters in the left half of s (excluding the pivot character) and mirror them to the right half.
    
        Left Half: The left half of s has length k. We have k-1 possible positions to place delimiters (excluding the character at index k itself because n is even).
    
        Combinations: We need to choose j-1 positions out of k-1 to place the delimiters. The number of ways to do this is C(k-1, j-1).
    
        Symmetry: For each valid placement in the left half, there's a unique corresponding symmetrical placement in the right half.
    
        Conclusion: Therefore, |σ_induce(s, m, S)| = C(k - 1, j - 1) = C(n/2 - 1, m/2 - 1).
    
        Case 2: Even-length s (n = 2k), Odd m (m = 2j + 1):
    
        Pivot: Since n is even, the pivot of ζ falls between two characters. By Theorem 3.1.9, l(ζ[:ω(ζ)]) = l(ζ[ω(ζ):]) + 1. Since ζ is a perfect palindrome, by theorem 3.1.6, σ_reduce(ζ) = inv(σ_reduce(ζ)). The pivot of s lies between the characters at indices k and k+1.
    
        Delimiter Placement: To form m = 2j+1 words, we need to place m-1 = 2j delimiters. We place j delimiters in the left half of s (excluding the pivot character) and mirror them to the right half.
    
        Left Half: The left half of s has length k. We have k-1 possible positions to place delimiters (excluding the character at index k itself because n is even).
    
        Combinations: We need to choose j positions out of k-1 to place the delimiters. The number of ways to do this is C(k-1, j).
    
        Symmetry: For each valid placement in the left half, there's a unique corresponding symmetrical placement in the right half.
    
        Conclusion: Therefore, |σ_induce(s, m, S)| = C(k - 1, j) = C(n/2 - 1, (m-1)/2).
    
        Case 3: Odd-length s (n = 2k + 1), Even m (m = 2j):
    
        Pivot: Since n is odd, the pivot of ζ falls on a character. By Theorem 3.1.8, since ζ is a perfect palindrome, σ_reduce(ζ) = inv(σ_reduce(ζ)). The pivot of s is the character at index k+1. Since m is even, by Theorem 3.2.5, this pivot character cannot be a delimiter.
    
        Delimiter Placement: To form m = 2j words, we need to place m-1 = 2j-1 delimiters. We place j-1 delimiters in the left half of s (excluding the pivot character) and mirror them to the right half. The remaining delimiter is placed at the pivot.
    
        Left Half: The left half of s, excluding the pivot character, has length k. We have k-1 possible positions to place delimiters (excluding the character at index k itself because n is odd).
    
        Combinations: We need to choose j-1 positions out of k-1 to place the delimiters. The number of ways to do this is C(k-1, j-1).
    
        Symmetry: For each valid placement in the left half, there's a unique corresponding symmetrical placement in the right half.
    
        Conclusion: Therefore, |σ_induce(s, m, S)| = C(k - 1, j - 1) = C((n-1)/2 - 1, m/2 - 1).
    
        Case 4: Odd-length s (n = 2k + 1), Odd m (m = 2j + 1):
    
        Pivot: Since n is odd, the pivot of ζ falls on a character. By Theorem 3.1.8, since ζ is a perfect palindrome, σ_reduce(ζ) = inv(σ_reduce(ζ)). The pivot of s is the character at index k+1. Since m is odd, by Theorem 3.2.5, this pivot character cannot be a delimiter.
    
        Delimiter Placement: To form m = 2j+1 words, we need to place m-1 = 2j delimiters. We place j delimiters in the left half of s (excluding the pivot character) and mirror them to the right half.
    
        Left Half: The left half of s, excluding the pivot character, has length k.
    
        Combinations: We need to choose j positions out of k to place the delimiters. The number of ways to do this is C(k, j).
    
        Symmetry: For each valid placement in the left half, there's a unique corresponding symmetrical placement in the right half.
    
        Conclusion: Therefore, |σ_induce(s, m, S)| = C(k, j) = C((n-1)/2, (m-1)/2).
    
        Final Result:
    
        Combining all four cases, we have proven the theorem:
    
        Let ζ ∈ PP with s = σ_reduce(ζ), n = l(s), and m be the desired number of words. Then:
    
        Case 1: Even-length s (n = 2k), Even m (m = 2j):
    
        |σ_induce(s, m, S)| = C(k - 1, j - 1) = C(n/2 - 1, m/2 - 1)
        Case 2: Even-length s (n = 2k), Odd m (m = 2j + 1):
    
        |σ_induce(s, m, S)| = C(k - 1, j) = C(n/2 - 1, (m-1)/2)
        Case 3: Odd-length s (n = 2k + 1), Even m (m = 2j):
    
        |σ_induce(s, m, S)| = C(k - 1, j - 1) = C((n-1)/2 - 1, m/2 - 1)
        Case 4: Odd-length s (n = 2k + 1), Odd m (m = 2j + 1):
    
        |σ_induce(s, m, S)| = C(k, j) = C((n-1)/2, (m-1)/2)
        This completes the proof. ∎
    
    
    
    Section A.V: Reflective Structures
    -----------------------------------
    
    **Definition A.5.1: Reflective Structure**
    
    A Reflective Structure, denoted **RS**, is the set of Strings *s* which satisfy the following formula,
    
        s ∈ RS ↔ [∃ n ∈ ℕ, ∃ p ∈ Χ:sub:`L`(n): (s = Π:sub:`i=1`:sup:`n` p(i)) ∧ (ς(S) = inv(ς(s)))]
    
    .. admonition:: TODO
    
        **Theorem A.6.1** R ⊆ RS
    
        TODO 
    
        **Theorem A.6.2** ∀ α ∈ L: α ∈ RS ↔ (α)(σ)(inv(α)) ∈ RS
    
        TODO 
    
        **Theorem A.6.3** ∀ α ∈ L: α ∈ RS ↔ (α)(inv(α)) ∈ RS
    
        TODO 
    
        **Theorem A.6.4**  ∀ p ∈ X:sub:`L`(2): Π:sub:`i=1`:sup:`2` p(i) ∈ RS ↔ Π:sub:`i=1`:sup:`1` p(i) = inv(Π:sub:`i=2`:sup:`2` p(i))
    
        TODO 
    
        **Theorem A.6.5** P ⊆ RS
    
        TODO 

.. _09data:
 
-----------
09_data.rst
-----------

.. raw:: 

    .. _section-viii:
    
    Section VIII: Data
    ==================
    
    .. _english-data:
    
    English 
    =======
    
    .. _reflective-words-data:
    
    Reflective Words
    ----------------
    
    The following spreadsheet contains a sample of reflective words in English.
    
    .. csv-table:: Reflective Words
       :file: ../_static/csv/words/reflective_words.csv
    
    .. _invertible-words-data:
    
    Invertible Words
    ----------------
    
    The following spreadsheet contains a sampe of invertible words (minus reflective words) in English.
    
    .. csv-table:: Invertible Words
       :file: ../_static/csv/words/invertible_words.csv
    
    .. _ambiguous-words-data:
    
    Ambiguous Words
    ---------------
    
    The following spreadsheet contains a sample of ambiguous words in English.
    
    .. csv-table:: Ambiguous Words
       :file: ../_static/csv/words/ambiguous_words.csv
    
    .. _palindrome-data:
    
    Palindromes
    ------------
    
    The following spreadsheet contains the results of palindromic analysis conducted on a sample of English palindromes. 
    
    .. csv-table:: English Palindrome Analysis
       :file: ../_static/csv/palindromes/english_palindromes.csv
    
    .. _latin-data:
    
    Latin
    =====
    
    .. _latin-palindrome-data:
    
    Palindromes
    -----------
    
    .. csv-table:: Latin Palindromes
       :file: ../_static/csv/palindromes/latin_palindromes.csv

.. _10app:
 
----------
10_app.rst
----------

.. raw:: 

    .. _section_viii:
    
    Section VIII: Code
    ==================
    
    Main
    ----
    
    .. literalinclude:: ../_apps/palindromes/main.py
        :language: python
    
    Model
    -----
    
    .. literalinclude:: ../_apps/palindromes/model.py
        :language: python
    
    
    Estimators
    ----------
    
    .. literalinclude:: ../_apps/palindromes/estimators.py
        :language: python
    
    Graphs 
    ------
    
    .. literalinclude:: ../_apps/palindromes/graphs.py
        :language: python
    
    Parse
    -----
    
    .. literalinclude:: ../_apps/palindromes/parse.py
        :language: python
    

.. _index:
 
---------
index.rst
---------

.. raw:: 

    .. _palindromia:
    
    ===========
    Palindromia
    ===========
    
    .. toctree::
       :maxdepth: 2
       :caption: Contents:
    
       00_glossary
       01_introduction
       02_language
       03_corpora
       04_structures
       05_palindromes
       06_analysis
       07_postulates
       08_appendix
       09_data
       10_app

.. _history:

Conversation History
####################

This section contains your correspondence history. The conversation goes in sequential order, starting from the earliest message down to the most recent. Each message in the correspondence is contained in a ``.. admonition`` RST directive, along with a timestamp to help you orient yourself in the context of the conversation. The last item in this section is Grant's latest prompt.


.. admonition:: grant

    **Timestamp**: 02-02 17:31

    hello
    
