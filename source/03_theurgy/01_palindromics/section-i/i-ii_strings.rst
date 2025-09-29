.. _palindromics-section-i-ii:

Section I.II: Strings
=====================

.. note::

    The formal development of this section largely agrees with standard treatments found in the theory of strings and concatenation. Many of the proofs are relegated to the Appendix when they do not diverge significantly from prior established results. Proofs of standard theorems that involve new formalizations will be highlighted.

.. _palindromics-axiom-0:

.. topic:: Axiom 0: Empty

    The Empty Character exists.

    .. math::

        \exists! s \in S: s = \varepsilon 

.. note::

    This assumption is crucial to establish the existence of an element in the domain that acts as the identity element for formal expressions. All of the recursive definitions will implicitly rely on :ref:`Empty Axiom <palindromics-axiom-0>`.

If a Characters is non-Empty, it belong to the Alphabet,

.. math::

    \Sigma = \{ \mathfrak{a}, \mathfrak{b}, \mathfrak{c}, ... \}

.. important::

    The Delimiter belongs to the Alphabet.

    .. math::

        \sigma \in \Sigma

.. warning::

    The work will proceed as if the :math:`\Sigma \neq \varnothing`, but it should be noted at this stage :math:`\Sigma = \varnothing` trivially satisifies all of the axioms that will be presented by annihiliating the domain of discourse. 

The aggregate of the Alphabet and the Empty Character is referred to as the *Total Alphabet* and is denoted,

.. math::

    \Sigma_{e} = \Sigma \cup \{ \varepsilon \}

.. _palindromics-axiom-i:

.. topic:: Axiom I: Comprehension

    All Characters in the Total Alphabet are Strings.

    .. math::
        
        \forall \iota \in \Sigma_{e}: \iota \in S

A String is regarded as a linguistic artifact or inscription that is defined entirely by its Characters and their ordering. A Character is seen as the basic unit of a String. In order to construct a String or set of Strings, an Alphabet of Characters must be selected. 

In order to construct more complicated Strings through the sequencing of Characters, the operation of Concatenation must be defined, but defining Concatenation requires a well-defined notion of *equality*, thus the next axiom is introduced.

.. note::

    The following axiom is technically a conjunction of axioms.

.. _palindromics-axiom-ii:

.. topic:: Axiom II: Equality

    For any Strings :math:`s, t \in S`, the notion of equality, denoted by :math:`s = t`, is a primitive concept and assumed to be understood. It is further assumed that equality is an equivalence relation, satisfying reflexivity, symmetry and transitivity,

        1. :math:`\forall s \in S: s = t`
        2. :math:`\forall s, t \in S: s = t \leftrightarrow t = s`
        3. :math:`\forall s, t, u \in S: ((s = t) \land (t = u)) \implies (s = u)`

.. _palindromics-concatenation:

Concatenation
-------------

.. _palindromics-definition-1-2-1:

.. topic:: Definition 1.2.1: Concatenation

    The result of concatenating any two Strings :math:`s` and :math:`t` is denoted :math:`st`. To make the operands clear, parenthesis will sometimes be used, e.g. :math:`s(t) = (s)t = st`. Concatenation is defined inductively through the following schema,

    1. Basis: 
        - If :math:`s = \varepsilon`, :math:`st = t`
    2. Induction: 
        - If :math:`s \neq \varepsilon`, then write :math:`s = (\iota)u` where :math:`\iota \in \Sigma` and :math:`u \in S`. Then :math:`st = ({\iota}u)t = \iota(ut)`

.. note::

    The :ref:`Empty Axiom <palindromics-axiom-0>` and the :ref:`Equality Axiom <palindromics-axiom-ii>` are necessary assumptions to ensure the Basis and Induction clauses of :ref:`Concatenation <palindromics-definition-1-2-1>` are well-defined. 

.. _palindromics-axiom-iii:

.. topic:: Axiom III: Closure

    Concatenation is closed over the set of all finite Strings.

    .. math::

        \forall s,t \in S: st \in S

**Example** Let :math:`s = \mathfrak{abc}` and :math:`t = \mathfrak{def}`. 

Group :math:`s` so that :math:`s = \mathfrak{a}(\mathfrak{bc})`, then apply the Induction clause of :ref:`Concatenation <palindromics-definition-1-2-1>`, 

.. math::

    st = (\mathfrak{abc})(\mathfrak{def}) = (\mathfrak{a}(\mathfrak{bc}))(\mathfrak{def}) = \mathfrak{a}((\mathfrak{bc})(\mathfrak{def})).

Group :math:`\mathfrak{bc}` so that :math:`\mathfrak{b}(\mathfrak{c})`, then apply the Induction clause,

.. math::

    (\mathfrak{bc})(\mathfrak{def}) = (\mathfrak{b}(\mathfrak{c}))(\mathfrak{def}) = \mathfrak{b}((\mathfrak{c})\mathfrak{def})

Group :math:`\mathfrak{c}` so that :math:`\mathfrak{c}(\varepsilon)`, then apply the Induction clause,

.. math::

    (\mathfrak{c})(\mathfrak{def}) = (\mathfrak{c}(\varepsilon))(\mathfrak{def}) = \mathfrak{c}((\varepsilon)(\mathfrak{def}))

Then, by the Basis clause,

.. math::

    (\varepsilon)(\mathfrak{def}) = \mathfrak{def}

But the recursion together,

.. math::

    \mathfrak{c}((\varepsilon)(\mathfrak{def})) = \mathfrak{c}(\mathfrak{def}) = \mathfrak{cdef}

.. math::

    \mathfrak{b}((\mathfrak{c})(\mathfrak{def})) = \mathfrak{b}(\mathfrak{cdef}) = \mathfrak{bcdef}

.. math::

    \mathfrak{a}((\mathfrak{bc})(\mathfrak{def})) = \mathfrak{a}(\mathfrak{bcdef}) = \mathfrak{abcdef}

∎

.. note::

    By :ref:`Comprehension Axiom <palindromics-axiom-i>`, all Characters are Strings and concatenation is closed under :math:`S` by the :ref:`Closure Axiom <palindromics-axiom-iii>`, therefore, as each nested concatenation is evaluated in the preceding example, the Induction clause in :ref:`Concatenation <palindromics-definition-1-2-1>` ensures the next level of concatenation is a String. 

.. important::

    Many of the results of the formal theory of strings are taken as given and are not proven. The following list details the properties of concatenation that will be assumed.

    1. Associativity: :math:`(s)(ut) = (su)t`
    2. Non-commutative: :math:`st \neq ts`
    3. Left-cancellation: :math:`st = su \implies t = u`
    4. Right-cancellation: :math:`ts = us \implies t = u`

.. note::

    Refer to :ref:`palindromics-motivation` for a more in-depth discussion of the nature of concatenation.

.. _palindromics-string-length:

String Length
-------------

The length of a String is defined as its number of non-Empty Characters.

.. _palindromics-definition-1-2-2:

.. topic:: Definition 1.2.2: String Length

    Let :math:`s = uv` such that :math:`u \in S` and :math:`v \in \Sigma_{e}`. The String Length of :math:`s`, denoted :math:`l(s)`, is defined inductively using the following schema,

    1. Basis: 
        - :math:`l(\varepsilon) = 0`
    2. Induction: 
        - :math:`v = \varepsilon \implies l(s) = l(u)`
        - :math:`v \neq \varepsilon \implies l(s) = l(u) + 1`

**Example** Let :math:`s_1 = \mathfrak{abc}\varepsilon\mathfrak{def}`. Using :ref:`Concatenation <palindromics-definition-1-2-1>`, this can be grouped as :math:`s_1 = (\mathfrak{abc}\varepsilon\mathfrak{de})(\mathfrak{f})`.

Applying :ref:`String Length <palindromics-definition-1-2-2>` to :math:`\mathfrak{f}` where :math:`u = \mathfrak{f}` and :math:`v = \varepsilon`,

.. math::

    l(\mathfrak{f}) = l(\varepsilon) + 1 = 0 + 1 = 1

.. note::
    
    This same logic generalizes to all Alphabetic Characters,

    .. math::

        \forall \iota \in \Sigma: l(\iota) = 1

Applying :ref:`String Length <palindromics-definition-1-2-2>` with :math:`u = \mathfrak{abc}\varepsilon\mathfrak{de}` and :math:`v = \mathfrak{f}`,

.. math::

    l(\mathfrak{abc}\varepsilon\mathfrak{def}) = l(\mathfrak{abc}\varepsilon\mathfrak{de}) + 1

The first term on the righthand side can be evaluated by applying :ref:`String Length <palindromics-definition-1-2-2>` with :math:`u = \mathfrak{abc}\varepsilon\mathfrak{d}` and :math:`v = \mathfrak{e}`,

.. math::

    l(\mathfrak{abc}\varepsilon\mathfrak{def}) = (l(\mathfrak{abc}\varepsilon\mathfrak{d}) + 1) + 1

Continuing in this fashion, the result is calculated,

.. math::

    l(s_1) = 6

∎

The definition of String length allows an important shorthand to be defined. This notation introduces nothing new into the system, but significantly improves the readability of proofs.

.. _palindromics-definition-1-2-3:

.. topic:: Definition 1.2.3: Character Indices

    Let :math:`s \in S`. Let :math:`i \in \mathbb{N}` such that :math:`1 \leq i \leq l(s)`. The Character at index :math:`i` in :math:`s`, denoted :math:`s[i]`, is defined inductively using the schema, 

    1. Basis:
        - If :math:`s = \varepsilon`, :math:`s[i]` is not defined.
    2. Induction: Let :math:`s = uv` where :math:`v \in \Sigma_{e}`.
        - If :math:`i = l(s)` and :math:`v \neq \varepsilon`, :math:`s[i] = v`
        - If :math:`i \neq l(s)` or :math:`v = \varepsilon`, then :math:`s[i] = u[i]`

.. note::

    The notation :math:`s[i]` is borrowed directly from string slicing in computer science.

The following example shows how the definition of Character indexing "*skips*" over the physical index of Empty Characters and assigns a logical index to any non-Empty Characters in a String.

**Example** Let :math:`s_1 = \mathfrak{ab}\varepsilon\mathfrak{c}`. By :ref:`String Length <palindromics-definition-1-2-2>`, :math:`l(s_1) = 3`. 

Consider :math:`s_1[3]`. Apply :ref:`the definition of Character Indices <palindromics-definition-1-2-3>` with :math:`u_1 =\mathfrak{ab}\varepsilon` and :math:`v_1 = \mathfrak{c}`. :math:`i = l(s_1)` and :math:`v_1 \neq \varepsilon`, therefore, by the Induction clause, :math:`s[3] = \mathfrak{c}`.

Consider :math:`s_1[2]`. Apply :ref:`the definition of Character Indices <palindromics-definition-1-2-3>` with :math:`u_1 =\mathfrak{ab}\varepsilon` and :math:`v_1 = \mathfrak{c}`. At this step, :math:`v_1 \neq \varepsilon` but :math:`i \neq l(s_1)`, so the :math:`s_1[i] = u_1[i]`. Note :math:`l(u_1) = 2`.

To find :math:`u_1[i]`, let :math:`u_1 = {u_2}{v_2}` where :math:`u_2 = \mathfrak{ab}` and :math:`v_2 = \varepsilon`. At this step, :math:`i = l(u_1)`, but :math:`v_2 = \varepsilon`, therefore :math:`u_1[i] = u_2[i]`. Note :math:`l(u_2) = 2`.

To find :math:`u_2[i]`, let :math:`u_2 = {u_3}{v_3}` where :math:`u_3 = \mathfrak{a}` and :math:`v_3 = \mathfrak{b}`. At this step, :math:`i = l(u_2)` and :math:`v_3 \neq \varepsilon`, therefore :math:`u_2[i] = v_3 = \mathfrak{b}`.

From this, it follows, :math:`s_1[2] = u_1[2] = u_2[2] = v_3 = \mathfrak{b}`.

∎

.. _palindromics-theorem-1-2-1:

.. topic:: Theorem 1.2.1
    
    The String Length of the concatenation of String :math:`s` and String :math:`t` is equal to the sum of their String Lengths.

    .. math::
        
        \forall s,t \in S: l(st) = l(s) + l(t)

.. note::

    The proof of :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>` by induction is presented in :ref:`Appendix I, Omitted Proofs <palindromics-appendix-i-ii>`.

.. _palindromics-containment:

Containment
-----------

.. _palindromics-definition-1-2-5:

.. topic:: Definition 1.2.5: Containment

    Let :math:`u,v \in S`. The relation of *containment*, denoted :math:`u \subset_s v`, is said to obtain between :math:`u` and :math:`v` when the following open formula in :math:`u,v` is satisfied,

    .. math::

        u \subset_s v \equiv \exists w_1, w_2 \in S: v = ({w_1})(u)({w_2})

.. note::

    The notion of *containment* is the formal explication of the colloquial relation of "*being a substring of*". 

**Example** Let :math:`s_1 = \mathfrak{abcdef}`. Then the truth of the following propositions can be verified using the given values of :math:`w_1` and :math:`w_2` in :ref:`the definition of Containment <palindromics-definition-1-2-5>`.

- :math:`\mathfrak{ab} \subset_s s_1`, where :math:`w_1 = \varepsilon` and :math:`w_2 = \mathfrak{cdef}`.
- :math:`\mathfrak{cde} \subset_s s_1`, where :math:`w_1 = \mathfrak{ab}` and :math:`w_2 = \mathfrak{f}`.
- :math:`\neg (\mathfrak{g} \subset_s s_1)`, for any :math:`w_1, w_2`

∎

.. _palindromics-theorem-1-2-2:

.. topic:: Theorem 1.2.2

    The Empty Character is contained in every String.

    .. math::

        \forall s \in S: \varepsilon \subset_s s

**Proof** Follows directly from the definition of :ref:`Concatenation <palindromics-definition-1-2-1>` and the definition of :ref:`Containment <palindromics-definition-1-2-5>` with :math:`u = \varepsilon` and :math:`v = \varepsilon`.

∎

.. NOTE: had to insert these theorems. Everything needs renumbered around them.

.. _palindromics-theorem-1-2-3:

.. topic:: Theorem 1.2.3

    If any Character :math:`\iota` is contained in :math:`uv`, then :math:`\iota` is contained in :math:`u` or :math:`\iota` is contained in :math:`v`.

    .. math::

        \forall \iota \in \Sigma_e: \forall u, v \in S: (\iota \subset_s uv) \implies (s \subset_s u) \lor (s \subset_s v)

**Proof** Let :math:`\iota \in \Sigma_e`: Let :math:`u,v \in S`. Since :math:`uv` is a non-overlapping sequence of Characters and :math:`\iota \subset_s uv`, it follows from the laws of logic that it must be the case that either :math:`\iota` is contained in :math:`u` or :math:`\iota` is contained in :math:`v`. 

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
.. This is NOT true.
.. The relation `s = \pi(s)` is always true, even for non-canonical strings, 
..  \mathfrak{ab} = \varepsilon\mathfrak{ab}
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

The formal system under construction assumes the process of Canonization precedes the formation of Language. Empty Characters possess no semantic content, and therefore must be exlcuded from the domain before Language is possible. This will be explicitly formalized in the :ref:`Canonization Axiom <palindromics-axiom-vi>`.

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
    
    This formal takes an extreme stance on String Inversion that deserves special note. See :ref:`palindromics-motivation` for more information.

.. _palindromics-definition-1-2-8:

.. topic:: Definition 1.2.8: String Inversion

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
