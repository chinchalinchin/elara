.. _palindromics-section-i-ii:

Section I.II: Strings
=====================

.. _palindromics-section-i-ii-toc:

Table of Contents
-----------------

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

------
Axioms 
------

1. :ref:`Axiom 0: Empty Axiom <palindromics-axiom-0>`: :math:`\exists! \varepsilon`
2. :ref:`Axiom I: Comprehension Axiom <palindromics-axiom-i>`: :math:`\iota \in S`
3. :ref:`Axiom II: Equality Axiom <palindromics-axiom-ii>`: :math:`s = t`
4. :ref:`Axiom III: Decomposition Axiom <palindromics-axiom-iii>`: :math:`(s \neq \varepsilon) \implies (s = {\iota}{t}) \lor (s = {t}{\iota})`
5. :ref:`Axiom IV: Closure Axiom <palindromics-axiom-iv>`: :math:`st \in S`

--------
Theorems
--------

1. :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>`: :math:`l(st) = l(s) + l(t)`
2. :ref:`Theorem 1.2.2 <palindromics-theorem-1-2-2>`: :math:`\varepsilon \subset_s s`
3. :ref:`Theorem 1.2.3 <palindromics-theorem-1-2-3>`: :math:`(\iota \subset_s uv) \implies ((\iota \subset_s u) \lor (\iota \subset_s v))`
4. :ref:`Theorem 1.2.4 <palindromics-theorem-1-2-4>`: :math:`\pi(\pi(s)) = \pi(s)`
5. :ref:`Theorem 1.2.5 <palindromics-theorem-1-2-5>`: :math:`s \in \mathbb{S} \equiv \pi(s) = s`
6. :ref:`Theorem 1.2.6 <palindromics-theorem-1-2-6>`: :math:`s,t \in \mathbb{S} \implies st \in \mathbb{S}`
7. :ref:`Theorem 1.2.8 <palindromics-theorem-1-2-8>`: :math:`\forall s \in \mathbb{S}: ((l(s) = l(t)) \land (\forall i \in N_{l(t)}: s[i] = t[i])) \implies (s = t)`
8. :ref:`Theorem 1.2.9 <palindromics-theorem-1-2-9>`: :math:`(s^{-1})^{-1} = s`
9. :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-10>`: :math:`(st)^{-1} = (t^{-1})(s^{-1})`
10. :ref:`Theorem 1.2.11 <palindromics-theorem-1-2-11>`: :math:`u \subset_s v \equiv u^{-1} \subset_s v^{-1}`

.. _palindromics-string-axioms:

String Axioms
-------------

:small:`The formal development of this section largely agrees with standard treatments found in the theory of strings and concatenation`

.. _palindromics-axiom-0:

.. topic:: Axiom 0: Empty

    The Empty Character exists.

    .. math::

        \exists! s \in S: s = \varepsilon 

This assumption immediately establishes the existence of an element in the domain, namely the Empty Character. This element will act as the identity element for formal expressions and allows recursions to halt. Most of the recursive definitions that follow will implicitly rely on the :ref:`Empty Axiom <palindromics-axiom-0>`.

A String is regarded as a linguistic artifact or inscription that is defined entirely by its Characters and their ordering. A Character is seen as the basic unit of a String. In order to construct a String or set of Strings, an Alphabet of Characters must be selected and assigned.

If a Characters is non-Empty, it belongs to the Alphabet,

.. math::

    \Sigma = \{ \mathfrak{a}, \mathfrak{b}, \mathfrak{c}, ... \}

This is to be regarded as a value assignment. The entities :math:`\mathfrak{a}, \mathfrak{b}, \mathfrak{c}, ...` are interpretted within a particular model of the formal system. They are descriptive constants.

In particular, the Delimiter belongs to the Alphabet.

.. math::

    \sigma \in \Sigma

.. warning::

    The work will proceed as if the :math:`\Sigma \neq \varnothing`, but it should be noted at this stage :math:`\Sigma = \varnothing` trivially satisifies all of the axioms that will be presented by annihiliating the domain of discourse. 

However, :math:`\varepsilon`, as a formal term, is *not* of the same type as Alphabetic Characters. Alphabetic Characters are non-logical and are dependent on an interpretation. :math:`\varepsilon`, on the contrary, is structural in nature. In this regard, :math:`\varepsilon` bears similarity to the parenthesis. 

The aggregate of the Alphabet and the Empty Character is referred to as the *Total Alphabet* and is denoted,

.. math::

    \Sigma_{e} = \Sigma \cup \{ \varepsilon \}

.. _palindromics-axiom-i:

.. topic:: Axiom I: Comprehension

    All Characters in the Total Alphabet are Strings.

    .. math::
        
        \forall \iota \in \Sigma_{e}: \iota \in S

In order to construct more complicated Strings through the sequencing of Characters, the operation of Concatenation must be defined, but defining Concatenation requires a well-defined notion of *equality*. 

.. _palindromics-axiom-ii:

.. topic:: Axiom II: Equality

    For any Strings :math:`s, t \in S`, the notion of equality, denoted by :math:`s = t`, is a primitive concept and assumed to be understood. It is further assumed that equality is an equivalence relation, satisfying reflexivity, symmetry and transitivity,

        1. :math:`\forall s \in S: s = s`
        2. :math:`\forall s, t \in S: s = t \leftrightarrow t = s`
        3. :math:`\forall s, t, u \in S: ((s = t) \land (t = u)) \implies (s = u)`

.. note::

    The :ref:`Equality Axiom <palindromics-axiom-ii>` is technically a conjunction of axioms.

.. important::

    The order of dependence in the logical notions that underlie formal string theory is nearly unavoidable. In this hierarchy,

    :math:`\text{Equality} \to \text{Concatenation} \to \text{Length}`

    Equality must be assumed to give meaning to the Concatenated expression, :math:`s = ut`. Next, concatenation must be defined to give meaning to :math:`l(s)`. 
    
    There are feasible constructions that bend the order of dependence slightly, but they tend to lack the simplicity of the proposed order. For example, it is possible to build a formal theory of strings by assuming a primitive notion of *character equality* and then defining string equality in terms of string length and character equality, but systems built on these artifices tend to require prosaic constructions that obscure the subject matter with unnecessary formal machinery. 

.. _palindromics-concatenation:

Concatenation
-------------

.. _palindromics-definition-1-2-1:

.. topic:: Definition 1.2.1: Concatenation

    The Concatenation of any Strings :math:`s, t \in S` and is denoted :math:`st`. Concatenation is defined inductively through the following schema,

    1. Basis: 
        - If :math:`s = \varepsilon`, :math:`st = t`
    2. Induction: 
        - If :math:`s \neq \varepsilon`, then :math:`s = {\iota}{u}` where :math:`\iota \in \Sigma_e` and :math:`u \in S`. Define :math:`st = ({\iota}u)t = \iota(ut)`.

    To make the operands clear, parenthesis will sometimes be used, e.g. :math:`s(t) = (s)t = (s)(t) = st`. 

.. note::

    As previously indicated and now presently shown, the :ref:`Empty Axiom <palindromics-axiom-0>` and the :ref:`Equality Axiom <palindromics-axiom-ii>` are necessary assumptions to ensure the Basis and Induction clauses of :ref:`Concatenation <palindromics-definition-1-2-1>` are well-defined. 

The notion of Concatenation is immediately followed by several assumptions that strengthen its definition and provide a basis for understanding the expanded range of expressions that are now possible by representing Strings as sequences of other Strings, e.g. :math:`s = uv`.

.. _palindromics-axiom-iii:

.. topic:: Axiom III: Decomposition 

    If a String is non-Empty, it can be decomposed into a Concatenation of a single Character and a String, in either direction.

    .. math::

        \forall s \in S: (s \neq \varepsilon) \implies (\exists \iota \in \Sigma_e, u \in S: s = (\iota)(u) ) \quad \text{ (1) }

    .. math::

        \forall s \in S: (s \neq \varepsilon) \implies (\exists \iota \in \Sigma_e, u \in S: s = (u)(\iota) ) \quad \text{ (2) }

    Decomposition as in (1) will be referred to as *left-handed decomposition*. Decomposition as in (2) will be referred to as *right-handed decomposition*.

.. note::

    The :ref:`Decomposition Axiom <palindromics-axiom-iii>` is implicitly used by the Induction clause of :ref:`Concatenation <palindromics-definition-1-2-1>` to ensure the decomposition :math:`s = {\iota}{u}` exists.

.. note::

    In the event :math:`\Sigma = \varnothing`, nothing exists in the domain to satisfy the inequality :math:`s \neq \varepsilon`, so the :ref:`Decomposition Axiom <palindromics-axiom-iii>` is vacuously true.

.. note::

    The :math:`\iota` in the :ref:`Decomposition Axiom <palindromics-axiom-iii>` is always satisfied by atleast :math:`\varepsilon`.

The direction of implication :ref:`Decomposition Axiom <palindromics-axiom-iii>` cannot be extended into an equivalence without admitting a class of expressions, such as :math:`s = \varepsilon\varepsilon`, :math:`s = \varepsilon\varepsilon\varepsilon`, etc., as possible solutions to the inequality :math:`s \neq \varepsilon`, which would invalidate the Basis clause of :ref:`Concatenation <palindromics-definition-1-2-1>`.

In other words, the unidirectional implication of the :ref:`Decomposition Axiom <palindromics-axiom-iii>` ensures every non-Empty String can be "extended" indefinitely, e.g. :math:`s = (s)(\varepsilon) = ((s)(\varepsilon))(\varepsilon)`, etc., a necessary condition for Concatenation, but it also allows for the identities :math:`\varepsilon\varepsilon = \varepsilon`, :math:`\varepsilon\varepsilon\varepsilon = \varepsilon`, etc.

.. _palindromics-axiom-iv:

.. topic:: Axiom IV: Closure

    Concatenation is closed over the set of all finite Strings.

    .. math::

        \forall s,t \in S: st \in S

Closure and Decomposition form different poles of a String's logical structure. The :ref:`Closure Axiom <palindromics-axiom-iv>` ensures all Concatenations are Strings (possibly Empty), whereas the :ref:`Decomposition Axiom <palindromics-axiom-iii>` ensure all Strings are Concatenations (of possibly Empty Characters). Both are necessary to ensure Strings and Concatenation belong to the same universe of discourse. 

.. warning::

    It is important to keep in mind the essential distinction between Strings and Characters versus String Variables and Character Variables. 

    An expression such as :math:`s_1 = \mathfrak{ab}` is an *identity assignment* to the literal String :math:`s_1` of a specific sequence of literal Characters. It is formally incorrect to regard :math:`\mathfrak{ab}` as a *Concatenation*; it is a *physical inscription* that satisfies the equation :math:`s = (u)(v)` for :math:`u = \mathfrak{a}` and :math:`v = \mathfrak{b}`.

    Carefully consider the distinction between these meanings illustrated in the following example.

**Example** Let :math:`s, t \in S` for some Characters :math:`\iota, \nu, \omicron, \rho \in \Sigma` such that :math:`s = \iota\nu = (\iota)(\nu)` and :math:`t = \omicron\rho = (\omicron)(\rho)`. 

Consider, 

.. math::

    st = (\iota\nu)(\omicron\rho) = ((\iota)(\nu))((\omicron)(\rho))

Apply the Induction clause of :ref:`Concatenation <palindromics-definition-1-2-1>`, 

.. math::

    st = \iota((\nu)((\omicron)(\rho)))


By the :ref:`Comprehension Axiom <palindromics-axiom-i>` (all Characters are Strings) and :ref:`Decomposition Axiom <palindromics-axiom-iii>` (all non-Empty Strings can be decomposed), :math:`\nu = \nu\varepsilon = (\nu)(\varepsilon)`, 

.. math::

    st = \iota(((\nu)(\varepsilon))((\omicron)(\rho)))

.. math::

    st = \iota(\nu((\varepsilon)(\omicron)(\rho)))

.. note::

    The :math:`\varepsilon` pulled in through the :ref:`Decomposition Axiom <palindromics-axiom-iii>` once the end Character of :math:`s` was reached then propagates the operation of Concatenation into the second String by inserting a leading Empty Character into it to kick off the nested operation.

.. math::

    st = \iota(\nu((\omicron)(\rho)))

.. math::

    st = \iota(\nu(\omicron(\rho)))

Let :math:`\iota = \mathfrak{a}, \nu = \mathfrak{b}, \omicron = \mathfrak{c}, \rho = \mathfrak{d}`. Then :math:`s = (\mathfrak{a})(\mathfrak{b}) = \mathfrak{ab}` and :math:`t = (\mathfrak{c})(\mathfrak{d}) = \mathfrak{cd}`. The previous equation shows the Concatenation of these literal Strings is accomplished through the sequential Concatenations,

.. math::

    \mathfrak{a}(\mathfrak{b}(\mathfrak{c}(\mathfrak{d}))) = \mathfrak{a}(\mathfrak{b}(\mathfrak{cd}))

.. math::
    
    = \mathfrak{a}(\mathfrak{bcd}) = \mathfrak{abcd}

The general logic of this example can be extended to Strings composed of an arbitrary number of Characters.


∎

.. note::

    By :ref:`Comprehension Axiom <palindromics-axiom-i>`, all Characters are Strings and Concatenation is closed under :math:`S` by the :ref:`Closure Axiom <palindromics-axiom-iv>`, therefore, as each nested concatenation is evaluated in the preceding example, the Induction clause in :ref:`Concatenation <palindromics-definition-1-2-1>` ensures the next level of concatenation is a String. 

.. TODO: this shoud be proved or assumed, not hand-waved away.

.. important::

    Many of the results of the formal theory of strings are taken as given and are not proven. The following list details the properties of concatenation that will be assumed.

    1. Associativity: :math:`(s)(ut) = (su)t`
    2. Non-commutative: :math:`st \neq ts`
    3. Left-cancellation: :math:`st = su \implies t = u`
    4. Right-cancellation: :math:`ts = us \implies t = u`

Keep in mind, in the preceding example, the equation :math:`\mathfrak{bcd} = (\mathfrak{b})(\mathfrak{cd}) = \mathfrak{b}(\mathfrak{cd})` is a relation between three literal Strings. A translation of the example into English would read as follows,

    "*bcd*" is the concatenation of *b* and *cd*

It is only incidental the name "*bcd*" in this translation is the literal concatenation of the names "*b*" and "*cd*". It is not logically necessary to represent a sequence with the literal terms that compose it, but such a decision would be akin to a numeral system where the number one is represented with ``||``, the number two is represented with ``|``, the number three with ``||||`` and so on. Formally, such constructions can be accomplished, but nothing but confusion would be gained by such an effort.

.. note::

    Refer to :ref:`palindromics-motivation` for a more in-depth discussion of the nature of concatenation.

.. _palindromics-string-length:

String Length
-------------

The length of a String is defined as its number of non-Empty Characters.

.. _palindromics-definition-1-2-2:

.. topic:: Definition 1.2.2: String Length

    Let :math:`s \in S`. The String Length of :math:`s`, denoted :math:`l(s)`, is defined inductively using the following schema,

    1. Basis: 
        - If :math:`s = \varepsilon`, :math:`l(s) = 0`
    2. Induction:  
        - If :math:`s \neq \varepsilon` and :math:`s = (\nu)(u)` with :math:`\nu \in \Sigma` and :math:`u \in S`, then :math:`l(s) = l(u) + 1`
        - If :math:`s \neq \varepsilon` and :math:`s = (\nu)(u)` with :math:`\nu = \varepsilon` and :math:`u \in S`, then :math:`l(s) = l(u)`

.. note::

    The :ref:`Empty Axiom <palindromics-axiom-0>` in conjunction with :ref:`String Length <palindromics-definition-1-2-2>` ensures there is exactly one String in :math:`S` such that :math:`l(s) = 0`.

.. note::

    The :ref:`Decomposition Axiom <palindromics-axiom-iii>` is used in the Induction clause of :ref:`String Length <palindromics-definition-1-2-2>` to ensure the existence of the String's decomposition. 

**Example** Let :math:`s = {\iota_1}{\iota_2}\varepsilon{\iota_3}{\iota_4} = ({\iota_1})(({\iota_2})((\varepsilon)(({\iota_3})({\iota_4}))))`. 

Applying the Induction Clause of :ref:`String Length <palindromics-definition-1-2-2>` with :math:`\nu = \iota_1` and :math:`u = u_1 = {\iota_2}\varepsilon{\iota_3}{\iota_4}`,

.. math::

    l(s) = l(u_1) + 1

Applying the Induction Clause of :ref:`String Length <palindromics-definition-1-2-2>` with :math:`\nu = \iota_2` and :math:`u = u_2 = \varepsilon{\iota_3}{\iota_4}`,

.. math::

    l(u_1) = l(u_2) + 1

Applying the Induction Clause of :ref:`String Length <palindromics-definition-1-2-2>` with :math:`\nu = \varepsilon` and :math:`u = u_3 = {\iota_3}{\iota_4}`,

.. math::

    l(u_2) = l(u_3)

Applying the Induction Clause of :ref:`String Length <palindromics-definition-1-2-2>` with :math:`\nu = \iota_3` and :math:`u = u_4 = \iota_4`,

.. math::

    l(u_3) = l(u_4) + 1 

Applying the Induction Clause of :ref:`String Length <palindromics-definition-1-2-2>` with :math:`\nu = \iota_4` and :math:`u = u_5 = \varepsilon`, which is guaranteed to exist by the :ref:`Decomposition Axiom <palindromics-axiom-iii>`,

.. math::

    l(u_4) = l(u_5) + 1 

Applying the Basis cluase of :ref:`String Length <palindromics-definition-1-2-2>` to :math:`u_5 = \varepsilon`,

.. math::

    l(u_5) = 0

.. note::

    The Empty Character, :math:`\varepsilon`, serves to *terminate* the recursion.

Putting the recursion together,

.. math::

    l(s) = (((0) + 1) + 1 + 1) + 1 = 4

∎

The definition of :ref:`String Length <palindromics-definition-1-2-2>` allows an important shorthand to be defined. This notation introduces nothing new into the system, but significantly improves the readability of proofs.

.. _palindromics-definition-1-2-3:

.. topic:: Definition 1.2.3: Character Indices

    Let :math:`s \in S`. Let :math:`i \in \mathbb{N}` such that :math:`1 \leq i \leq l(s)`. The Character at index :math:`i` in :math:`s`, denoted :math:`s[i]`, is defined inductively using the schema, 

    1. Basis:
        - If :math:`s = \varepsilon`, :math:`s[i]` is undefined.
    2. Induction: If :math:`s \neq \varepsilon`, then :math:`s = u(\iota)` for some :math:`\iota \in \Sigma_e` and :math:`u \in S`.
        - If :math:`i = l(s)` and :math:`\iota \neq \varepsilon`, :math:`s[i] = \iota`
        - If :math:`i \neq l(s)` or :math:`\iota = \varepsilon`, then :math:`s[i] = u[i]`
    
.. note::

    The notation :math:`s[i]` is borrowed directly from string slicing in computer science.

The following example shows how the definition of Character indexing "*skips*" over the physical index of Empty Characters and assigns a logical index to any non-Empty Characters in a String.

**Example** 

Let :math:`s_1 = \mathfrak{ab}\varepsilon\mathfrak{c}`. By :ref:`String Length <palindromics-definition-1-2-2>`, :math:`l(s_1) = 3`. 

Consider :math:`s_1[3]`. Apply :ref:`the definition of Character Indices <palindromics-definition-1-2-3>` with :math:`u_1 =\mathfrak{ab}\varepsilon` and :math:`v_1 = \mathfrak{c}`. :math:`i = l(s_1)` and :math:`v_1 \neq \varepsilon`, therefore, by the Induction clause, :math:`s[3] = \mathfrak{c}`.

Consider :math:`s_1[2]`. Apply :ref:`the definition of Character Indices <palindromics-definition-1-2-3>` with :math:`u_1 =\mathfrak{ab}\varepsilon` and :math:`v_1 = \mathfrak{c}`. At this step, :math:`v_1 \neq \varepsilon` but :math:`i \neq l(s_1)`, so the :math:`s_1[i] = u_1[i]`. Note :math:`l(u_1) = 2`.

To find :math:`u_1[i]`, let :math:`u_1 = {u_2}{v_2}` where :math:`u_2 = \mathfrak{ab}` and :math:`v_2 = \varepsilon`. At this step, :math:`i = l(u_1)`, but :math:`v_2 = \varepsilon`, therefore :math:`u_1[i] = u_2[i]`. Note :math:`l(u_2) = 2`.

To find :math:`u_2[i]`, let :math:`u_2 = {u_3}{v_3}` where :math:`u_3 = \mathfrak{a}` and :math:`v_3 = \mathfrak{b}`. At this step, :math:`i = l(u_2)` and :math:`v_3 \neq \varepsilon`, therefore :math:`u_2[i] = v_3 = \mathfrak{b}`.

From this, it follows, :math:`s_1[2] = u_1[2] = u_2[2] = v_3 = \mathfrak{b}`.

Similarly, it can be shown :math:`s_1[1] = \mathfrak{a}`.

∎

.. _palindromics-theorem-1-2-1:

.. topic:: Theorem 1.2.1
    
    The String Length of the concatenation of String :math:`s` and String :math:`t` is equal to the sum of their String Lengths.

    .. math::
        
        \forall s,t \in S: l(st) = l(s) + l(t)

**Proof** The proof proceeds by structural induction on the number of non-Empty Characters in :math:`s`.

.. BASIS

:underline:`Basis`: Let :math:`s = \varepsilon` and :math:`t \in S`. Consider :math:`st = {\varepsilon}{t}`.

By :ref:`Concatenation <palindromics-definition-1-2-1>`, :math:`{\varepsilon}{t} = t`. By :ref:`String Length <palindromics-definition-1-2-2>`, :math:`l(\varepsilon) = 0`. It follows from the basic laws of arithmetic,

.. math::

    l({\varepsilon}{t}) = l(t)  = 0 + l(t)

.. math::

    = l(\varepsilon) + l(t) = l(s) + l(t)

Therefore, the base case, :math:`l(st) = l(s) + l(t)`, holds.

.. INDUCTION

:underline:`Induction`: Assume :math:`l(ut) = l(u) + l(t)` for any :math:`t \in S` and any :math:`u \in S` up to some fixed length.  
 
Let :math:`s = {\iota}u` for some :math:`\iota \in \Sigma`. That is, assume :math:`s` has one more Character than :math:`u`, possibly Empty. Consider,

.. math::

    l(st) = l((\iota{u})t) = l((\iota)({u}{t}))

.. CASE I

If :math:`\iota = \varepsilon`, then :math:`\iota{u} = \varepsilon{u} = u`. by the Induction clause of :ref:`String Length <palindromics-definition-1-2-2>`,

.. math::

    l(st) =  l(\varepsilon{ut}) = {l(ut) = l(u) + l(t)

Where the last equality follows from the inductive hypothesis. Moreover, if :math:`\iota = \varepsilon`, :math:`s = \varepsilon{u} = u`. Therefore,

.. math::

    l(st) = l(s) + l(t)

.. CASE II

If :math:`\iota \neq \varepsilon`, then it follows from the Induction clause of :ref:`String Length <palindromics-definition-1-2-2>`,

.. math::

    l(st) = l(\iota(ut)) = l(ut) + 1 = l(u) + l(t) + 1 \quad \text{ (1) }

Where the last equality follows from the inductive hypothesis. 

Consider the quantity :math:`l(s) = l(\iota{u})`. By the Induction clause of :ref:`String Length <palindromics-definition-1-2-2>`,

.. math::

    l(s) = l(\iota{u}) = l(u) + 1 \quad \text{ (2) }

Combining (1) and (2),

.. math::

    l(st) = l(s) + l(t)

Therefore, the inductive step is established. It follows from the principle of finite induction,

.. math::

    \forall s,t \in S: l(st) = l(s) + l(t)

∎

.. _palindromics-containment:

Containment
-----------

The concept of Containment is the formal explication of the colloquial relation of "*substring of*"

.. _palindromics-definition-1-2-5:

.. topic:: Definition 1.2.5: Containment

    Let :math:`u,v \in S`. The relation of *containment*, denoted :math:`u \subset_s v`, is said to obtain between :math:`u` and :math:`v` when the following open formula in :math:`u,v` is satisfied,

    .. math::

        u \subset_s v \equiv \exists w_1, w_2 \in S: v = ({w_1})(u)({w_2})

    When this occurs, :math:`u` is said to be *contained* in :math:`v`.


**Example** Let :math:`s_1 = \mathfrak{abcdef}`. 

The truth of the following propositions can be verified using the given values of :math:`w_1` and :math:`w_2` in the definition of :ref:`Containment <palindromics-definition-1-2-5>`.

- :math:`\mathfrak{ab} \subset_s s_1`, where :math:`w_1 = \varepsilon` and :math:`w_2 = \mathfrak{cdef}`.
- :math:`\mathfrak{cde} \subset_s s_1`, where :math:`w_1 = \mathfrak{ab}` and :math:`w_2 = \mathfrak{f}`.
- :math:`\neg (\mathfrak{g} \subset_s s_1)`, for any :math:`w_1, w_2`

∎

.. _palindromics-theorem-1-2-2:

.. topic:: Theorem 1.2.2

    The Empty Character is contained in every String.

    .. math::

        \forall s \in S: \varepsilon \subset_s s

**Proof** Let :math:`s \in S`.

Instantiating the :ref:`Closure Axiom <palindromics-axiom-iv>` with :math:`\varepsilon` and :math:`s`, 

.. math::

    \varepsilon{s} \in S

Instantiating the :ref:`Closure Axiom <palindromics-axiom-iv>` with :math:`\varepsilon` and :math:`\varepsilon{s}`,   

.. math::

    \varepsilon\varepsilon{s} \in S

By repeated application of :ref:`Concatenation <palindromics-definition-1-2-1>`, 

.. math::

    s = \varepsilon\varepsilon{s}

By the :ref:`Empty Axiom <palindromics-axiom-0>`, :math:`\varepsilon` exists.

Therefore, applying the definition of :ref:`Containment <palindromics-definition-1-2-5>` with :math:`w_1 = \varepsilon` and :math:`w_2 = s`, it is concluded,

.. math::

    \varepsilon \subset_s s

Summarizing and generalizing,

.. math::

    \forall s \in S: \varepsilon \subset_s s

∎

.. THEOREM: \forall s,t: (t = su) \land (s \subset_s t)) \implies l(s) \leq l(t)

.. Let s,t \in S. Assume l(s) < l(t) and s \subset_s t. Then by containment, there exists
..
.. t = (w_1)(s)(w_2)
..
.. By Theorem 1.2.1,
..
.. l(t) = l(w_1) + l(s) + l(w_2)
..
.. su = (w_1)(s)(w_2)
..

.. _palindromics-theorem-1-2-3:

.. topic:: Theorem 1.2.3

    If any Character :math:`\iota` is contained in :math:`uv`, then :math:`\iota` is contained in :math:`u` or :math:`\iota` is contained in :math:`v`.

    .. math::

        \forall \iota \in \Sigma_e: \forall u, v \in S: (\iota \subset_s uv) \implies ((\iota \subset_s u) \lor (\iota \subset_s v))

**Proof** Let :math:`\iota \in \Sigma_e`. Let :math:`u,v \in S` such that :math:`\iota \subset_s uv`

If :math:`\iota = \varepsilon`, then the theorem is trivially true by :ref:`Theorem 1.2.2 <palindromics-theorem-1-2-2>`.

Therefore, assume :math:`\iota \in \Sigma`. By :ref:`Containment <palindromics-definition-1-2-5>`, 

.. math::

    \exist w_1, w_2 \in S: uv = (w_1)(\iota)(w_2)

Let :math:`w = (w_1)(\iota)`.

l(u) < l(w)

.. math::

    l((w_1)(\iota)) = l(w_1) + l(\iota)
Since :math:`uv` is a non-overlapping sequence of Characters and :math:`\iota \subset_s uv`, it follows from the laws of logic that it must be the case that either :math:`\iota` is contained in :math:`u` or :math:`\iota` is contained in :math:`v`. 

∎

.. _palindromics-canonization:

Canonization
------------

*Canonization* is a function defined over :math:`s \in S` that produces the *canonical* form of a String by removing all instances of the Empty Character from it.

.. _palindromics-definition-1-2-6:

.. topic:: Definition 1.2.6: Canonization

    Let :math:`s \in S` such that :math:`s = uv` with :math:`u \in S` and :math:`v \in \Sigma_e`. The Canonization of :math:`s`, denoted :math:`\pi(s)`, is defined inductively using the following schema,

    - Basis:
        - :math:`\pi(\varepsilon) = \varepsilon`
    - Induction: 
        - If :math:`v = \varepsilon`, :math:`\pi(s) = \pi(u)`.
        - If :math:`v \neq \varepsilon`, :math:`\pi(s) = (\pi(u))(v)`

    The Canonization of a String :math:`s` is referred to as the *canonical form* or *canonical representation* of :math:`s`.

**Example** Let :math:`s_1 = (\mathfrak{a})(\varepsilon)(\mathfrak{b})`. 

Let :math:`u_1 = (\mathfrak{a})(\varepsilon)` and :math:`v_1 = \mathfrak{b}`. Note :math:`v_1 \in \Sigma` and :math:`s_1 = (u_1)(v_1)`. By the Induction clause of :ref:`Canonization <palindromics-definition-1-2-6>`,

.. math::

    \pi(s_1) = (\pi(u_1))(v_1)

Let :math:`u_2 = \mathfrak{a}` and :math:`v_2 = \varepsilon`. Note :math:`u_1 = (u_2)(v_2)`. By the Induction clause,

.. math::

    \pi(u_1) = \pi(u_2)

Let :math:`u_3 = (\varepsilon)` and :math:`v_3 = \mathfrak{a}`. Note :math:`v_3 \in \Sigma` and :math:`u_2 = (u_3)(v_3)`. By the Induction clause,

.. math::

    \pi(u_2) = (\pi(u_3))(v_3)

By the Basis clause,

.. math::

    \pi(u_3) = \varepsilon

Putting the recursion together,

.. math::

    \pi(s_1) = ((\varepsilon)(v_3))(v_1)

.. math::

    \pi(s_1) = (\varepsilon)(\mathfrak{ab})

By the Basis clause of :ref:`Concatenation <palindromics-definition-1-2-1>`, this becomes,

.. math::

    \pi(s_1) = \mathfrak{ab}

∎

.. _palindromics-definition-1-2-7:

.. topic:: Definition 1.2.7: Canon

    The Canon, denoted :math:`\mathbb{S}`, is defined as the image of the function :math:`\pi(s)` over the set of all finite Strings :math:`S`,

    .. math::

        \mathbb{S} = \{ \pi(s) \mid s \in S \}

Canonization provides a method of "*cleaning*" :math:`S` of troublesome Strings, such as :math:`\mathfrak{a}\varepsilon\mathfrak{b}`, that prevent the assertion of uniqueness within the semantic domains that will be shortly introduced. The Canon provides a domain within :math:`S` where the uniqueness of certain semantic properties can be established. 

.. _palindromics-theorem-1-2-4:

.. topic:: Theorem 1.2.4

    Canonization is idempotent.

    .. math::

        \forall s \in S: \pi(\pi(s)) = \pi(s)

**Proof** Let :math:`s \in S`. The proof proceeds by induction on :math:`s`.

.. BASIS 

:underline:`Basis` Let :math:`s = \varepsilon`. By the definition :ref:`Canonization <palindromics-definition-1-2-6>`,

.. math::

    \pi(\varepsilon) = \varepsilon.

Let :math:`t = \pi(\varepsilon)`. Consider,

.. math::

    \pi(t) = \pi(\pi(\varepsilon)) = \pi(\varepsilon) = \varepsilon

:underline:`Induction` Assume :math:`\pi(\pi(t)) = \pi(t)` for some :math:`t \in S`. Let :math:`s = (t)(\iota)` where :math:`\iota \in \Sigma_e`. Either :math:`\iota = \varepsilon` or :math:`\iota \neq \varepsilon`. 

.. INDUCTION

.. CASE I

:underline:`Case I`: :math:`\iota = \varepsilon`

By the Induction clause of :ref:`Canonization <palindromics-definition-1-2-6>`, 

.. math::

    \pi(s) = \pi(t)

By the Basis clause of :ref:`Concatenation <palindromics-definition-1-2-1>`,

.. math::

    s = (t)(\varepsilon) = t 

Therefore, by inductive hypothesis,

.. math::

    \pi(s) = \pi(t) = \pi(\pi(t)) = \pi(\pi(s))

.. CASE II

:underline:`Case II` :math:`\iota \neq \varepsilon`

By the Induction clause of :ref:`Canonization <palindromics-definition-1-2-6>`, 

.. math::

    \pi(s) = \pi(t\iota) = \pi(t)(\iota)

Now the String :math:`u = \pi(t)` belongs to the Canon, :math:`u \in \mathbb{S}`, and must therefore be a String free of :math:`\varepsilon`. Likewise, :math:`\iota \neq \varepsilon` by assumption. Therefore, :math:`u\iota` is also a String free of :math:`\varepsilon`. From this and the definition of :ref:`Canonization <palindromics-definition-1-2-6>`, it follows :math:`\pi(u\iota) = u\iota`, 

.. math::

    \pi(s) = u\iota

Consider,

.. math::

    \pi(\pi(s)) = \pi(u\iota) = u\iota 

Therefore, 

.. math::

    \pi(s) = \pi(\pi(s))

And the induction is established. Summarizing and generalizing,

.. math::

    \forall s \in S: \pi(s) = \pi(\pi(s))

∎

.. _palindromics-theorem-1-2-5:

.. topic:: Theorem 1.2.5

    A String is canonical if and only if it is equal to its own Canonization. 

    .. math::

        s \in \mathbb{S} \equiv s = \pi(s)

.. TODO: ........................................................................
.. This is NOT true, or atleast one needs be careful WHERE it is true!
.. The relation `s = \pi(s)` is always true, even for non-canonical strings, 
..  \mathfrak{ab} = \varepsilon\mathfrak{ab}
.. this is a problem of "syntactical" versus "logical" equality.
.. this theorem is about *syntactical* equality, not *logical* equality.
.. this should be a theorem *about* the formal system, not a theorem *in* the
.. formal system, where the equality relation is between meta-metamathematical objects.
.. in other words, a string belongs to the canon if its formal name \hat{s} is equal to \pi(\hat{s})
.. 
.. ...............................................................................

**Proof** Let :math:`s \in S`.

(:math:`\leftarrow`) Assume :math:`s = \pi(s)`. By the definition of :ref:`Canon <palindromics-definition-1-2-7>`, any String that is the result of Canonization belongs to the Canon, therefore :math:`s \in \mathbb{S}`.

(:math:`\rightarrow`) Assume :math:`s \in \mathbb{S}`. By the definition of :ref:`Canon <palindromics-definition-1-2-6>`, there must exist a :math:`t \in S` such that :math:`\pi(t) = s`. Consider :math:`\pi(\pi(t))`. By :ref:`Theorem 1.2.4 <palindromics-theorem-1-2-4>`,

.. math::

    \pi(\pi(t)) = \pi(t)

Substituting :math:`\pi(t) = s`,

.. math::

    \pi(s) = s

Therefore, the equivalence is established. 

∎

.. _palindromics-theorem-1-2-6:

.. topic:: Theorem 1.2.6

    Canonization is closed under Concatenation.

    .. math::

        \forall s,t \in mathbb{S}: st \in \mathbb{S}

**Proof** Let :math:`t \in S`. The proof will proceed by induction on :math:`t`.

.. BASIS

:underline:`Basis`: Let :math:`s \in \mathbb{S}`. Let :math:`t = \varepsilon`. By the Basis clause of :ref:`Canonization <palindromics-definition-1-2-6>` and the definition of :ref:`Canon <palindromics-definition-1-2-7>`, :math:`t \in \mathbb{S}`

Consider :math:`st`. By the Basis clause of :ref:`Concatenation <palindromics-definition-1-2-1>`, :math:`st = s\varepsilon = s`. But :math:`s \in \mathbb{S}` by assumption, thus :math:`st \in \mathbb{S}`.

.. INDUCTION

:underline:`Induction`. Assume :math:`u \in \mathbb{S}` such that :math:`su \in \mathbb{S}`. By :ref:`Theorem 1.2.5 <palindromics-theorem-1-2-5>`,

.. math::

    \pi(su) = su \quad (1)

Let :math:`t = (u)(\iota)` where :math:`\iota \in \Sigma`. Consider :math:`st`,

.. math::

    st = (s)(u)(\iota) = (su)(\iota) \quad (2)

Where the last equality follows from the associativity of concatenation. By inductive hypothesis, :math:`su \in \mathbb{S}`. Moreover, :math:`\iota \in \mathbb{S}` since :math:`\pi(\iota) = \iota`. Therefore, by definition of :ref:`Canonization <palindromics-definition-1-2-6>`

.. math::

    \pi(st) = \pi(su)\iota

Substituting in (1) and (2)

.. math::

    \pi(st) = (su)\iota = st

By :ref:`Theorem 1.2.5 <palindromics-theorem-1-2-5>`,

.. math::

    st \in \mathbb{S}

Thus, the induction is complete. Summarizing and generalizing,

.. math::

    \forall s,t \in \mathbb{S}: st \in \mathbb{S}

∎

Canonization is an important operation in the study of the logical relations that govern semantic Strings. The Canon provides an abstraction over the domain of all finite Strings where logical properties and physical properties of a String coincide, as in the following list shows. Each of these properties is a direct result :ref:`Theorem 1.2.5 <palindromics-theorem-1-2-5>`.

1. The logical length (String Length) of a String is the physical length of the String's canonical form: :math:`l(s) = l(\pi(s))`
2. The logical Characters of a String are the physical Characters of the String's canonical form: :math:`s[i] = (\pi(s))[i] = \pi(s)[i]`, where the last equality is shorthand. 
3. The canonical form of a String is :math:`\varepsilon`-free, a structural property that translates to "*has no Empty Characters*".

The next two theorems will be extremely important in establishing the equality of certain classes of Strings.

.. _palindromics-theorem-1-2-8:

.. topic:: Theorem 1.2.8

    If two canonical Strings have the same String Length and all of their Characters equal index-wise, then those Strings are equal.

    .. math::

        \forall s,t \in \mathbb{S}: ((l(s) = l(t)) \land (\forall i \in N_n: s[i] = t[i])) \implies (s = t)

**Proof** Let :math:`s,t \in \mathbb{S}`. The proof will proceed by induction on :math:`l(s)`. 

.. BASIS

:underline:`Basis`: Assume :math:`l(s) = 1`. 

If a canonical String :math:`s` has a :math:`l(s) = 1`, then it follows from :ref:`Canonization <palindromics-definition-1-2-6>`, :math:`s = \iota` for some :math:`\iota \in \Sigma`. 

If :math:`l(t) = 1` and :math:`t[1] = s[1]`, then this implies,

.. math::

    s = \iota = t

Therefore, the Basis holds.

.. INDUCTION

:underline:`Induction` Assume for all for all :math:`u,v \in \mathbb{S}`, :math:`l(u) = l(v) = n` and :math:`\forall i \in N_n: u[i] = v[i]` implies :math:`u = v`.

Let :math:`s, t \in \mathbb{S}` such that :math:`l(s) = l(t) = n + 1` and :math:`\forall i \in N_n: s[i] = t[i]`. Since :math:`s` and :math:`t` are canonical, they can be written :math:`s = u(\iota)` and :math:`t = v(\nu)`.

From :math:`s[n+1] = t[n+1]`, it follows :math:`\iota = \nu`. By inductive hypothesis, :math:`u = v`. Therefore, by the :ref:`Equality Axiom <palindromics-axiom-ii>`, 

.. math::

    s = u\iota = v\nu = t

Thus, the induction holds. Summarizing and generalizing,

.. math::

    \forall s,t \in \mathbb{S}: ((l(s) = l(t)) \land (\forall i \in N_n: s[i] = t[i])) \implies (s = t)

∎

.. note::

    :ref:`Theorem 1.2.8 <palindromics-theorem-1-2-8>` shows how the logical properties of a String's canonical form, namely its logical length (String Length) and its logical (non-Empty) Characters reduce to the abstract and primitive concept of "*string equality*".

The formal system under construction assumes the process of Canonization precedes the formation of Language. Empty Characters possess no semantic content, and therefore must be exlcuded from the domain before Language is possible. This will be explicitly formalized in the :ref:`Canonization Axiom <palindromics-axiom-vii>`.

**Example** Let :math:`s = \mathfrak{a}\varepsilon` and :math:`t = \mathfrak{b}`. 

By :ref:`Canonization <palindromics-definition-1-2-6>`,

.. math::

    \pi(s) = \mathfrak{a}

.. math::

    \pi(t) = \mathfrak{b}

By :ref:`Concatenation <palindromics-definition-1-2-1>`, 

.. math::

    \pi(s)\pi(t) = \mathfrak{ab}

Now, apply :ref:`Concatenation <palindromics-definition-1-2-1>` to :math:`st` with :math:`s = (\mathfrak{a})\varepsilon`, then 

.. math::

    st = \mathfrak{a}({\varepsilon}{t})

.. important::

    The :math:`\varepsilon` "*moves*" inside of the parenthesis and thus, "*triggers*" another recursive call to concatenation.

.. math::

    {\varepsilon}t = t = \mathfrak{b}

So that, 

.. math::

    st = \mathfrak{ab}

∎

.. important::

    The previous example suggests an important, often overlooked fact, *Concatenation always yields a Canonical String*. In other words, Concatenation can be regarded as :math:`\mathfrak{F}: S \mapsto \mathbb{S}`

.. TODO: ........................................................................
..
.. Need to clarify thoughts on how to prove this, because it's impossible to define 
.. to a function that counts the number of Empty characters in a string. The clause 
.. :math:`\neg(\varepsilon \subset_s s)` would never be true, so recursion would never halt. 
..
.. Seems like it would be a metamathematical theorem, where alphabet is assigned with 
.. :math:`\hat{varepsilon}` that represents the "name of the Empty Character". Then can count 
.. the meta-character and induce a structural induction on the number of empty characters. 
..
.. THEOREM
..
.. All Concatenations are Canonical
..
.. \forall s,t \in S: st \in \mathbb{S}
..
.. NOT TRUE. From "if s = \varepsilon, then st=t", it does not follow that t \in \mathbb{S}. What if t = \varepsilon?
..
.. THEOREM
..
.. Concatenation is closed under the Canon
..
.. \forall s,t \in \mathbb{S}: st \in \mathbb{S}
..
.. Follows directly from previous theorem.
..
.. .................................................................................

.. _palindromics-string-inversion:

String Inversion
----------------

.. important::
    
    See :ref:`palindromics-motivation` for a detailed epistemological explication of the proceedings.

Two definitions of String Inversion will be given, a definition using induction and a definition using logical properties. It will be shown immediately these definitions are equivalent.

.. _palindromics-definition-1-2-8-inductive:

.. topic:: Definition 1.2.8: String Inversion (Inductive)

    Let :math:`s, t \in S`. Let :math:`n \in \mathbb{N}`. The inverse of :math:`s`, denoted :math:`s^{-1}`, is defined inductively with the following schema,

    - Basis: If :math:`s = \varepsilon`, then :math:`s^{-1} = \varepsilon`
    - Induction: If :math:`s = (\iota)(t)` where :math:`\iota \in \Sigma` and :math:`t \in S`, then :math:`((\iota)(t))^{-1} = (t^{-1})(\iota)`

.. _palindromics-definition-1-2-8:

.. topic:: Definition 1.2.8: String Inversion (Descriptive)

    Let :math:`s, t \in S`. Let :math:`n \in \mathbb{N}`. :math:`t` is called the inverse of :math:`s`, denoted :math:`s^{-1}`, if the following conditions hold,

    - :math:`l(s) = l(t) = n`
    - :math:`\forall i \in N_n: t[i] = s[n - i + 1]`

**Example** Let :math:`s_1 = \mathfrak{abc}`. Let :math:`s_2 = {s_1}^{-1}`. The Inverse can be constructed through its Character Indices by applying :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    s_2[1] = s_1[3 - 1 + 1] = s_1[3] = \mathfrak{c}

.. math::

    s_2[2] = s_1[3 - 2 + 1] = s_1[2] = \mathfrak{b}

.. math::

    s_2[3] = s_1[3 - 3 + 1] = s_1[1] = \mathfrak{c}

Concatenating the results, 

.. math::

    s_2 = {s_1}^{-1} = \mathfrak{cba}

∎

.. TODO: ......................................................................................

The equivalence of these definitions can be established through structural induction. Let :math:`t = s^{-1}`. 

:underline:`Basis`: If :math:`l(s) = 1`, that is, if :math:`s \in \Sigma`, then :math:`l(t) = 1`. By the :ref:`Inductive definition of Inversion <palindromics-definition-1-2-8-inductive>`, :math:`t = s^{-1} = (s\varepsilon)^{-1} = (\varepsilon)^{-1}(s) = \varepsilon(s) = s`. 

:underline:`Induction` Assume :math:`t = s^{-1}` for a fixed :math:`l(s) = n` such that :math:`\forall i \in N_n: t[i] = s[n - i + 1]` and :math:`l(t) = l(s)`. Consider :math:`u \in S` with :math:`l(u) = n + 1`. Then, :math:`u` can be written :math:`u = \iota(v)` for some :math:`\iota \in \Sigma` and :math:`v \in S` with :math:`l(v) = n`. Note :math:`s[1] = \iota`. By the :ref:`Inductive definition of Inversion <palindromics-definition-1-2-8-inductive>`, :math:`(\iota(v))^{-1} = (v^{-1})\iota`. Thus :math:`t` is a String that ends in :math:`\iota`, :math:`t[n+1] = \iota = s[1]`. 

.. TODO: ......................................................................................

.. _palindromics-theorem-1-2-9:

.. topic:: Theorem 1.2.9

    The inverse of an inverse is the original String. 

    .. math::

        \forall s \in S: (s^{-1})^{-1} = s

**Proof** Let :math:`s \in S`. Let :math:`t = s^{-1}`. Let :math:`n = l(s)`. From :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math:: 

    l(t) = l(s) = n \quad \text{ (1) }

.. math::

    \forall i \in N_n: t[i] = s[n - i + 1] \quad \text{ (2) }

Let :math:`u = t^{-1}`. Applying :ref:`String Inversion <palindromics-definition-1-2-8>` again,

.. math::

    l(u) = l(t) = n \quad \text{ (3) }

.. math::

    \forall j \in N_n: u[j] = t[n - j + 1] \quad \text{ (4) }

Plugging :math:`i = n - j + 1` into (2) and substituting into (4),

.. math::

    \forall j \in N_n: u[j] = s[n - (n - j + 1) + 1] = s[j] \quad \text{ (5) }

Moreover, from (1) and (3), it follows, 

.. math::

    l(s) = l(u) \quad \text{ (6) }

By the :ref:`Theorem 1.2.8 <palindromics-theorem-1-2-8>`, (5) and (6) together imply,

.. math::

    u = t^{-1} = (s^{-1})^{-1} = s

Therefore,

.. math:: 

    \forall s \in S: (s^{-1})^{-1} = s

∎

.. _palindromics-theorem-1-2-10:

.. topic:: Theorem 1.2.10

    The Inverse of a Concatenation of two Strings is the Concatenation of their Inverses in the reversed order.

    .. math::

        \forall s,t \in S: (st)^{-1} = (t^{-1})(s^{-1})

**Proof** Let :math:`s,t \in S`. Let :math:`u = st`. Let :math:`m = l(s)` and :math:`n = l(t)`. Let :math:`u = st`. By :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>`,

.. math::

    l(u) = l(st) = l(s) + l(t) = m + n

Let :math:`v = u^{-1} = (st)^{-1}`. Let :math:`w = (t)^{-1}(s)^{-1}`.  By repeated application of :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    l(v) = l(st) = m + n \quad \text{ (1) }

.. math::

    l((t)^{-1}) = l(t) = n 

.. math::

    l((s)^{-1}) = l(s) = m 

Using these results and applying :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>` to :math:`w`,

.. math::

    l(w) = l((s)^{-1}) + l((t)^{-1}) = m + n \quad \text{ (2) }

From (1) and (2), it follows, 

.. math::

    l(v) = l(w) \quad \text{ (3) }

Let :math:`i \in N_{m+n}`.

.. CASE I

:underline:`Case I`: :math:`i \leq i \leq n`

By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    v[i] = u[m + n - i + 1]

By assumption :math:`i \leq n` or :math:`n - i \geq 0`, therefore,

.. math::

    m + n - i \geq m

Increasing the LHS of this inequality does not affect the truth of its assertion,

.. math::

    m + n - i + 1 \geq m

From this, :math:`u = st` and :math:`l(s) = m`, it follows that :math:`u[m + n - i + 1]` is an index in :math:`t`, 

.. math::

    v[i] = t[n - i + 1] \quad \text{ (4) }

Consider :math:`w[i]`. Since :math:`l((t)^{-1}) = n` and :math:`i \leq n`, it follows that :math:`w[i] = (t^{-1})[i]`. By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    w[i] = t^{-1}[i] = t[n - i + 1] \quad \text{ (5) }

Combining (4) and (5),

.. math::

    v[i] = w[i] \quad \text{ (6) }

Applying :ref:`Theorem 1.2.8 <palindromics-theorem-1-2-8>`, (3) and (6) imply,

.. math::

    v = w

.. CASE II

:underline:`Case II`: :math:`n + 1 \leq i \leq m + n`

By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    v[i] = u[m + n - i + 1]

By assumption :math:`i \geq n + 1` or :math:`n - i + 1 \leq 0`, therefore,

.. math::

    m + n - i + 1 \leq m 

From this, :math:`u = st` and :math:`l(s) = m`, it follows that :math:`u[m + n - i + 1]` is an index in :math:`s`,

.. math::

    v[i] = s[m + n - i + 1] \quad \text{ (7) } 

Consider :math:`w[i]`. Since :math:`l((t)^{-1}) = n` and :math:`i \geq n`, it follows that :math:`w[i] = (s^{-1})[i - n]`. By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    w[i] = s^{-1}[i-n] = s[m - (i - n) + 1]

.. math::

    w[i] = s[m + n - i + 1] \quad \text{ (8) }

Combining (7) and (8),

.. math::

    v[i] = w[i] \quad \text{ (9) }

Applying :ref:`Theorem 1.2.8 <palindromics-theorem-1-2-8>`, (3) and (6) imply,

.. math::

    v = w

In both cases, the theorem is proved. Summarizing and generalizing,

.. math::

    \forall s,t \in S: (st)^{-1} = (t^{-1})(s^{-1})

∎

.. _palindromics-theorem-1-2-11:

.. topic:: Theorem 1.2.11

    A String :math:`s` contains another a String :math:`s` if and only if the inverse of :math:`s` contains the inverse of :math:`t`.

    .. math::

        \forall s,t \in S: (t \subset_s s) \equiv (t^{-1} \subset_s s^{-1})

**Proof** Let :math:`s,t \in S`.

(:math:`\rightarrow`) Assume :math:`t \subset_s s`. Then by :ref:`Containment <palindromics-definition-1-2-5>`, there exists :math:`w_1, w_2 \in S` such that, 

.. math::

    s = (w_1)(t)(w_2)

Consider :math:`s^{-1}`. Applying :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-10>` twice, this becomes,

.. math::

    s^{-1} = (w_2)^{-1}(t)^{-1}(w_1)^{-1}

Therefore, there exists :math:`u_1 = {w_2}^{-1}` and :math:`u_2 = {w_1}^{-1}` such that :math:`s^{-1} = (u_1)(t^{-1})(u_2)` and by the :ref:`definition of Containment <palindromics-definition-1-2-5>`,

.. math::

    t^{-1} \subset_s s^{-1}

(:math:`\leftarrow`) The proof is identical to (:math:`\rightarrow`).

Therefore, 

.. math::

    \forall s,t \in S: t \subset_s s \equiv t^{-1} \subset_s s^{-1}

∎

.. TODO: ........................................................................
.. THEOREM
..
.. All Inverses are Canonical.
..
.. \forall s \in S: s^{-1} \in mathbb{S}
..
.. THEOREM
..
.. The Canon is closed over Inversion
..
.. \forall s \in \mathbb{S}: s^{-1} \in \mathbb{S}
.. ...............................................................................
