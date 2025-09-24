.. _palindromics-introduction:

Introduction
============

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   :hidden:

   intro-i_overview
   intro-ii_motivation

.. _palindromics-table-of-contents:

Table Of Contents
-----------------

- :ref:`Introduction <palindromics-introduction>`
    - :ref:`Table of Content <palindromics-table-of-contents>`
    - :ref:`Glossary <palindromics-glossary>`
    - :ref:`Overview <palindromics-overview>`
    - :ref:`Motivation <palindromics-motivation>`
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

.. _palindromics-glossary:

Glossary
--------

.. NOTE: Glossary isn't done yet.

.. _palindromics-definitions:

-----------
Definitions
-----------

1. :ref:`Definition 1.2.1: Concatenation <palindromics-definition-1-2-1>`: :math:`st`
2. :ref:`Definition 1.2.2: String Length <palindromics-definition-1-2-2>`: :math:`l(s)`
3. :ref:`Definition 1.2.3: Character Indices <palindromics-definition-1-2-3>`: :math:`s[i]`
4. :ref:`Definition 1.2.5: Containment <palindromics-definition-1-2-5>`: :math:`t \subset_s s`
5. :ref:`Definition 1.2.6: Canonization <palindromics-definition-1-2-6>`: :math:`\pi(s)`
6. :ref:`Definition 1.2.7: Canon <palindromics-definition-1-2-7>`: :math:`\mathbb{S} = \{ \pi(s) \mid s \in S \}` 
7. :ref:`Definition 1.2.8: String Inversion <palindromics-definition-1-2-8>`: :math:`s^{-1}`
8. :ref:`Definition 1.3.1: Reflective Words <palindromics-definition-1-3-1>`: :math:`\alpha \in R \equiv \alpha = {\alpha}^{-1}`
9. :ref:`Definition 1.3.2: Invertible Words <palindromics-definition-1-3-2>` :math:`\alpha \in I \equiv {\alpha}^{-1} \in L`
10. :ref:`Definition 1.3.3: Phrases <palindromics-definition-1-3-3>`: :math:`P_n = (p(1), ..., p(n))`
11. :ref:`Definition 1.3.4: Lexicons <palindromics-definition-1-3-4>`: :math:`L_n = \{ p \mid \forall p: p = P_n \}`
12. :ref:`Definition 1.3.5: Limitation <palindromics-definition-1-3-5>`: :math:`\Pi_{i=1}^{n} p(i)`
13. :ref:`Definition 1.3.6: Dialect <palindromics-definition-1-3-6>`: :math:`D = \bigcup_{i=1}^{\infty} \{ s \in S \mid \exists p \in L_i: s = \Pi_{j=1}^{i} p(j) \}`
14. :ref:`Definition 1.4.1: Word Length <palindromics-definition-1-4-1>`: :math:`\Lambda(\zeta)`
15. :ref:`Definition 1.4.2: Word Indices <palindromics-definition-1-4-2>`: :math:`\zeta[[i]]`
16. :ref:`Definition 1.4.3: Invertible Sentences <palindromics-definition-1-4-3>`: :math:`\zeta \in K \equiv {\zeta}^{-1} \in C`
17. :ref:`Definition 2.1.1: Delimiter Count <palindromics-definition-2-1-1>`: :math:`\Delta(s)`
18. :ref:`Definition 2.1.2: Pivot Characters <palindromics-definition-2-1-2>`: :math:`\overleftarrow(\omega_s), \overrightarrow(\omega_s)`
19. :ref:`Definition 2.2.1: σ-Reduction <palindromics-definition-2-2-1>`: :math:`\varsigma(s)`

.. _palindromics-axioms:

------
Axioms
------

1. :ref:`Axiom 0: Empty Axiom <palindromics-axiom-0>`: :math:`\exists! \varepsilon`
2. :ref:`Axiom I: Comprehension Axiom <palindromics-axiom-i>`: :math:`\iota \in S`
3. :ref:`Axiom II: Equality Axiom <palindromics-axiom-ii>`: :math:`s = t`
4. :ref:`Axiom III: Closure Axiom <palindromics-axiom-iii>`: :math:`st \in S`
5. :ref:`Axiom IV: Measure Axiom <palindromics-axiom-iv>`: :math:`l(\alpha) \neq 0`
6. :ref:`Axiom V: Discovery Axiom <palindromics-axiom-v>`: :math:`\alpha[i] \neq \sigma`
7. :ref:`Axiom VI: Canonization Axiom <palindromics-axiom-vi>`: :math:`\alpha \in \mathbb{S}`

.. _palindromics-theorems:

--------
Theorems
--------

1. :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>`: :math:`l(st) = l(s) + l(t)`
2. :ref:`Theorem 1.2.2 <palindromics-theorem-1-2-2>`: :math:`\varepsilon \subset_s s`
3. :ref:`Theorem x.x.x <palindromics-theorem-x-x-x>`: :math:`(\iota \subset_s uv) \implies ((\iota \subset_s u) \lor (\iota \subset_s v))`
4. :ref:`Theorem x.x.y <palindromics-theorem-x-x-y>`: :math:`(\neg(\iota \subset_s u) \land \neg(\iota \subset_s u)) \implies \neg(\iota \subset_s uv)`
5. :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`: :math:`\pi(\pi(s)) = \pi(s)`
6. :ref:`Theorem 1.2.4 <palindromics-theorem-1-2-4>`: :math:`s \in \mathbb{S} \equiv \pi(s) = s`
7. :ref:`Theorem 1.2.5 <palindromics-theorem-1-2-5>`: :math:`s,t \in \mathbb{S} \implies st \in \mathbb{S}`
8. :ref:`Theorem 1.2.6 <palindromics-theorem-1-2-6>`: :math:`((l(s) = l(t)) \land (\forall i \in N_{l(t)}: s[i] = t[i])) \implies (s = t)`
9. :ref:`Theorem 1.2.8 <palindromics-theorem-1-2-8>`: :math:`(s^{-1})^{-1} = s`
10. :ref:`Theorem 1.2.9 <palindromics-theorem-1-2-9>`: :math:`(st)^{-1} = (t^{-1})(s^{-1})`
11. :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-10>`: :math:`u \subset_s v \equiv u^{-1} \subset_s v^{-1}`
12. :ref:`Theorem 1.3.1 <palindromics-theorem-1-3-1>`: :math:`\alpha \in I \equiv {\alpha}^{-1} \in I`
13. :ref:`Theorem 1.3.2 <palindromics-theorem-1-3-2>`: :math:`R \subset I`
14. :ref:`Theorem 1.3.3 <palindromics-theorem-1-3-3>`: :math:`\exists! s = \Pi_{i=1}^{n} p(i)` 
15. :ref:`Theorem 1.4.1 <palindromics-theorem-1-4-1>`: :math:`\sum_{j=1}^{\Lambda(\zeta)} l(\zeta[[j]]) \geq \Lambda(\zeta)`
16. :ref:`Theorem 1.4.2 <palindromics-theorem-1-4-2>`: :math:`\Lambda(\zeta\xi) \leq \Lambda(\zeta) + \Lambda(\xi)` 
17. :ref:`Theorem 1.4.3 <palindromics-theorem-1-4-3>`: :math:`\zeta = \Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]]`
18. :ref:`Theorem 1.4.4 <palindromics-theorem-1-4-4>`: :math:`(\Pi_{i=1}^{\Lambda(\zeta)} \zeta[[i]])^{-1} = \Pi_{i=1}^{\Lambda(\zeta)} (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}`
19. :ref:`Theorem 1.4.5 <palindromics-theorem-1-4-5>`: :math:`\Lambda((s)(\sigma)(t)) = \Lambda(s) + \Lambda(t)`
20. :ref:`Theorem 1.4.6 <palindromics-theorem-1-4-6>`: :math:`C \subseteq D`
21. :ref:`Theorem 1.4.7 <palindromics-theorem-1-4-7>`: :math:`\Lambda((\zeta)(\sigma)(\xi)) = \Lambda(\zeta) + \Lambda(\xi)`
22. :ref:`Theorem 1.4.8 <palindromics-theorem-1-4-8>`: :math:`C \subset \mathbb{S}`
23. :ref:`Theorem 1.4.9 <palindromics-theorem-1-4-9>`: :math:`\zeta \in K \equiv {\zeta}^{-1} \in K`
24. :ref:`Theorem 1.4.10 <palindromics-theorem-1-4-10>`: :math:`\zeta \in K \implies \zeta[[i]] \in I`
25. :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>`: :math:`\zeta \in K \implies {\zeta}^{-1}[[i]] = (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}`
26. :ref:`Theorem 2.1.1 <palindromics-theorem-2-1-1>`: :math:`\Lambda(\zeta) = \Delta(\zeta) + 1`
27. :ref:`Theorem 2.1.2 <palindromics-theorem-2-1-1>`: :math:`\Delta(s) = \Delta(s^{-1})`
28. :ref:`Theorem 2.1.3 <palindromics-theorem-2-1-3>`: :math:`l(\zeta) = \Delta(\zeta) + \sum_{i=1}^{\Lambda(\zeta)} l(\zeta[[i]])`
29. :ref:`Theorem 2.1.4 <palindromics-theorem-2-1-4>`: :math:`\Delta(st) = \Delta(s) + \Delta(t)`
30. :ref:`Theorem 2.1.5 <palindromics-theorem-2-1-5>`: :math:`((\Delta(s) = 2n +1) \land (s = s^{-1})) \implies (s[\frac{l(s)+1}{2}] = \sigma)`
31. :ref:`Theorem 2.1.6 <palindromics-theorem-2-1-6>`: :math:`((\Delta(s) = 2n + 1) \land (s = s^{-1})) \implies \exists i: l(s) = 2i - 1`
32. :ref:`Theorem 2.1.7 <palindromics-theorem-2-1-7>`: :math:`((\Delta(s) = 2n + 1) \land (s = s^{-1})) \implies (\overrightarrow{\omega_s} = \overleftarrow{\omega_s})`
33. :ref:`Theorem 2.1.8 <palindromics-theorem-2-1-8>`: :math:`((\Delta(s) = 2n) \land (s = s^{-1})) \implies ((\overrightarrow{\omega_s} \neq \sigma) \land (\overleftarrow(\omega_s) \neq \sigma))`
34. :ref:`Theorem 2.1.8 <palindromics-theorem-2-1-9>`: :math:`((\Delta(s) = 2n) \land (s = s^{-1})) \implies \overrightarrow{\omega_s} = \overleftarrow(\omega_s)`
35. :ref:`Theorem 2.2.1 <palindromics-theorem-2-2-1>`: :math:`\varsigma(st) = (\varsigma(s))(\varsigma(t))`
36. :ref:`Theorem 2.2.2 <palindromics-theorem-2-2-2>`: :math:`\Delta(s) = 0 \equiv \varsigma(s) = s`
37. :ref:`Theorem 2.2.3 <palindromics-theorem-2-2-3>`: :math:`(\varsigma(s))^{-1} = \varsigma(s^{-1})`
38. :ref:`Theorem 2.2.4 <palindromics-theorem-2-2-4>`: :math:`\varsigma(\varsigma(s)) = \varsigma(s)`
39. :ref:`Theorem 2.2.5 <palindromics-theorem-2-2-5>`: :math:`s \subset_s t \equiv \varsigma(s) \subset_s \varsigma(t)`
40. :ref:`Theorem 2.2.6 <palindromics-theorem-2-2-6>`: :math:`\zeta[[i]] \subset_s \varsigma(\zeta)`