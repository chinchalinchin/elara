.. _palindromics-motivation:

Motivation
==========

.. IN PROGRESS

.. note::

    The contents of this section are more for the author's benefit than the reader's. The nature of the formal system being constructed has forced the author to confront some of the basic notions that underlie the modern theory of strings and analyze them from a philsophical point of view. This section represents the author's attempt to provide an epistemological justification for the assumptions adopted within the system.

    This part of the work is an attempt to explicate and clarify the mathematical foundations of the formal entity known as *strings*.

Concatenation is unique within the domain of mathematics. Formal logic, as a method of inquiry, is wholly dependent on the ability to concatenate symbols in sequence to express complex and abstract logical relations. One cannot formalize concatenation without engaging in the act of "concatenating". This does not mean concatenation cannot be formalized, as evidenced by the mature fields of regular expressions and formal language theory. However, it *does* mean the formalization often obscures what is being formalized, as the formalization is itself an instance of the formalized.

In examining the work that follows, it is easy to slip into treating the formal entities within the system as the literal strings they represent. Often, one operates as if :math:`\mathfrak{a}` were both the symbolic representation of a linguistic unit and the linguistic unit being symbolized, i.e. the first letter of the English alphabet. In other words, it is easy to leave unappreciated the fact :math:`\mathfrak{a}` and the physical inscription *a* are materially different in their purpose and use. This imprecision in terminology is at the heart of classical antimonies like `Richard's Paradox <http://en.wikipedia.org/wiki/Richard%27s_paradox>`_ and `Berry's Paradox <https://en.wikipedia.org/wiki/Berry_paradox>`_. 

However, unlike the solution to these paradoxes which involve clearly separating metamathematics and mathematics into distinct domains, in the field of formal strings, there is an unavoidable circularity, since it is impossible for a string not to possess the property of representing itself. A string, as a concatenated series of character, is a representation of a concatenated series of characters. The very properties that imbue strings with their representative capacity are the subject of the formal theory of strings. Thus a string's representative capacity must be represented by its representative capacity, i.e. a sequence of characters "a", "b", "c" is represented as the literal sequence "abc".

This way of viewing strings is sufficient for developing an intuitive understanding of their algebraic properties, but it reaches its limit when confronted with expressions such as :math:`\varepsilon\mathfrak{a}` or :math:`\mathfrak{a}\varepsilon`. 

What is meant by the formal expression :math:`\mathfrak{a}\varepsilon\mathfrak{b}`? And in what ways does this expression differ from the formal expression :math:`\mathfrak{ab}`? [#1]_ More fundamentally, what is meant by the singular formal entity, :math:`\mathfrak{a}` and what relation does it bear to the physical inscription *a*? 

This problem is reminiscent of the indefinablity of truth, discussed by Alfred Tarski in his landmark *On The Concept of Truth in Formalized Languages* published in 1933, where his examinations of the antimony

    "x" is true if and only if x

led him to rigorously elaborate a structural definition of logical sentences, in which expressions about a language could be asserted and proven. Like Tarski advised in his construction, it is important to distinguish between the *name* of entity within a formal system, and the *entity* itself. Likewise, as the current formal system is developed, it important to keep the following in mind,

    :math:`\mathfrak{a}` is the name of *a*

The symbol :math:`\mathfrak{a}` is the logical abstraction assigned to the physical entity *a* **within the formal system**. It is a metamathematical object. Expressions within which it occurs do not occur within the same language about which it is making assertions.

For this reason :math:`\varepsilon\mathfrak{ab}` should not be treated as a literal string, no more than the arithmetical expression :math:`1 + 0` should be taken as the literal number which it represents, e.g. the object denoted by :math:`1`. Arithmetical expressions are logical abstractions of the numbers they represent; In Fregean terms, they are *references*, not *referents*. To borrow even more Fregean terminology, an expression like :math:`\varepsilon\mathfrak{ab}` conveys a different *sense* of the object denoted by :math:`\mathfrak{ab}`.

:math:`\varepsilon` is not a literal string, unless one has interpretted :math:`\varepsilon` as non-empty. There are no literal strings to be found in natural language that are formed by sequencing an empty character with other characters, let alone a string composed of nothing but the empty character. The formal strings

.. math::

    \mathfrak{a}\varepsilon, \mathfrak{a}\varepsilon\varepsilon, \mathfrak{a}\varepsilon\varepsilon\varepsilon, ...

are not representative of unique physical strings. They are artifacts of abstraction, akin to :math:`1.0, 1.00, 1.000, 1.0000, ...`. It must be kept in mind they are *logically equivalent* representatives of the same underlying physical string, namely the string denoted by the name :math:`\mathfrak{a}`. The formal system adopts the adage of Alain Badiou, "the name of the void is a pure *proper name*, which indicates itself, which does not bestow any index of difference within what it refers to, and which auto-declares itself in the form of the multiple, despite there being nothing which is numbered by it."

When one is engaged in language, there are no :math:`\varepsilon`'s; the term is meaningless; it has no *referent* at the object level of language. Just as one carries a :math:`1` and adds a :math:`0` when performing the operation described in the expression denoted by the name :math:`5 + 5` [#2]_, yet understands this process in no way maps to physically rearranging groups of objects in the world, one must keep in mind :math:`\mathfrak{ab}\varepsilon` is nothing more than a bookkeeping mechanism for establishing an algebra. 

The question then arises, what *is* :math:`S`, the domain of all finite strings? If the preceding has been understood, then the only answer is: it is a set of *references*, not *referents*. In other words, :math:`\varepsilon\mathfrak{a}`, :math:`\varepsilon\varepsilon\mathfrak{a}`, etc. all belong to the set denoted by :math:`S`. Statements and assertions made regarding :math:`S` are statements about the *names* of strings. 

However, due to the inescapable circle of having to represent the operation of concatenation with concatenated strings, there arises a confounding problem in the formal theory of strings. The set of strings denoted by :math:`S` that bear the property of being ":math:`\varepsilon`-free" directly map to the *physical inscription* they represent. Moreover, this set of strings has special properties. 

In the course of :ref:`Section I <palindromics-section-i>`, the operation of canonization, :math:`\pi(s)`, will be discussed in detail. For the current purposes, it suffices to think of :math:`\pi(s)` as function that maps the canonical name of a string to itself. The set of all canonical strings, :math:`\mathbb{S}`, is then isomorphic to the *physical* strings it represents. The metamathematical properties of canonical strings are therefore *physical* properties of the strings they represent. For this reason, the formalization and the objectification intersect. The properties of canonical strings in a formal system are exactly the properties exhibited by strings in the model which satisfies the formalization. [#3]_ This, as mentioned back in the introductory paragraph, is the underlying root of the confusion that one feels when trying to understand formal string theory. 

Consider how the process of *identifying* physical strings as inverses actually occurs in the instances of "*emit*" and "*time*". One starts by recognizing "*e*" in "*emit*" and "*e*" in "*time*" occupy mirror positions in their respective sequence of characters, that is,

    emit[1] = time[4]

Where ":math:`s[i]`" is notation that refers to the character indexed at a *physical* position within the string. The process then proceeds down the length of either string, as physical characters are mapped to one another in sequence. The key insight here is that *inversion is a physical process*. It is an operation that exists solely at the *object* level of the analysis. This *physical* process can be defined as a *logical relation* on the set of canonical strings. 

This can be seen from another angle. From a logical perspective, inversion is fundamentally dependent on concatenation and equality. Equality must be taken as primitive and then concatenation must precede the definition of inversion. In the standard formal theory of strings, inversion involves the basis and recursive step,

:underline:`Basis`

.. math::

    (\varepsilon)^{R} = \varepsilon 

:underline:`Induction`

.. math::

    ((\iota)t)^{R} = ((t)^{R})(\iota)

Which illustrates that inversion is simply an instruction to concatenate its input in a certain order. The basis clause of concatenation, :math:`s = {\varepsilon}{s}`, a standard definition, implicitly involves stripping a string of its empty characters (see :ref:`Example after Theorem 1.2.8 <palindromics-theorem-1-2-8>` for a more concrete example), meaning once the output of concatenation has been assigned it no longer bares any :math:`\varepsilon`, i.e. has property ":math:`\varepsilon`-free". It is this property that allows expressions such as :math:`s = {\varepsilon}{s}`, for the right hand side is simply a *name* of the left hand side. [#4]_

The expression

.. math::

    (\mathfrak{ab}\varepsilon)^{-1}

must therefore be attended to with careful scrutiny. The inversion is **not** being applied to the literal string :math:`\mathfrak{ab}\varepsilon`, for this quantity is a formal entity, as evidenced by the presence of :math:`\varepsilon` within it. The inversion does not operate on *formal entities*, it operates on the *objects* to which they refer. Therefore, inversion, like concatenation, should be regarded as mapping from the domain :math:`S` to the domain :math:`\mathbb{S}`. 

The typical recursive definition of inversion, while rigorous and correct, obscures this fact by seeming to imply through its definition that it *operates* on strings containing empty characters. However, execution of the algorithm reveals it is hiding the removal of :math:`\varepsilon` through concatenation.

Consider :math:`\mathfrak{a}^{-1}`. By the induction hypothesis, it is required to express this string as a concatenation, :math:`s = ({a}{\varepsilon})`, so the definition may recursively call the basis clause to end its "function call". Indeed,

.. math::

    \mathfrak{a}^{-1} = (\mathfrak{a}\varepsilon)^{-1} = (\varepsilon^{-1})(\mathfrak{a})

And the quantity :math:`\varepsilon^{-1}` ends the recursion by yielding :math:`\varepsilon`, which is then concatenated into the result to yield, 

.. math::

    \mathfrak{a}

However, it should be noted this is a purely formal process. It describes the structural and metamathematical properties of strings. It is a *bookkeeping* mechanism used to formalize the object-level operation of inversion. The ":math:`\varepsilon`" that migrates through the concatenation is the formal syntax of inversion, not a physical component of the inverted string.

The sets :math:`S`, :math:`\mathbb{S}`, :math:`S - \mathbb{S}` are of great epistemological interest, because the question arises: *where does it come from*? If concatenation, and by extension inversion, implicitly produces a canonical string through its application, how does one go about forming a string such as, 

.. math::

    {\varepsilon}{\varepsilon}{\varepsilon}{\varepsilon} 

According to the definition of concatenation, this string collapses into :math:`\varepsilon` if evaluated, keeping in mind the above is shorthand for the more formal expression,

.. math::

    ( ( (\varepsilon) (\varepsilon) ) (\varepsilon) ) (\varepsilon)

But, and this is an essential point, while concatenation may yield a well defined result for this expression, it cannot produce this string in the same concatenation can yield a string :math:`\mathfrak{abc}`. To reiterate, there is no way to start with only an alphabet :math:`\Sigma` and :math:`\varepsilon`, and produce the string given above. Consider starting with,

.. math::

    \varepsilon

From this, an infinite number of concrete, physical inscriptions can be produced by concatenating into this string, from the left or right, a letter of the alphabet, e.g.

.. math::

    (\varepsilon)(\iota) = \iota

Where concatenation from the right follows immediately from the definition of concatenation. Concatenation from the left requires several intermediary steps (according to the :ref:`definition of concatenation <palindromics-definition-1-2-1>` adopted in this work; other formalizations differ in the particular mechanics of their definitions, but the result will be the same),

.. math::

    (\iota)(\varepsilon)

The answer lies in regarding :math:`\varepsilon\iota` and similar formal entities as instances of strings that satisfy the formal model where the physical symbol :math:`\varepsilon` is assigned a non-empty character, call it :math:`\hat{\varepsilon}`, and each :math:`\mathfrak{a}_i` is assigned :math:`\hat{\mathfrak{a}_i}`. [#5]_ Then the equality that obtains :math:`\varepsilon\hat{\iota} = \hat{\iota}` becomes a structural property of the interpretation, i.e. canonically equal strings are equivalent to a class of strings that can be specified as *preserving order*, e.g.

.. math::

    \hat{s} = \hat{\mathfrak{a}_1}\hat{\varepsilon}\hat{\mathfrak{a}_2}

.. math:: 

    \hat{t} = \hat{\mathfrak{a}_1}\hat{\mathfrak{a}_2}

are *canonically equal* if and only if there exists a strictly increasing, consecutive function that maps the character indices that are canonically non-empty in both strings. In this case, :math:`f(1) = 1, f(2) = 3`. 

In other words, the meta-metamathematical specification of :math:`S` is given by applying the formal theory itself to the physical symbols assigned to the metamathematical entities, regarded now as physical inscriptions, and then constructing the equivalence classes that satisfy such expressions as

.. math::

    \varepsilon\mathfrak{a} = \mathfrak{a}

Namely, :math:`\hat{\varepsilon}\hat{\mathfrak{a}_i}, \hat{\varepsilon}\hat{\varepsilon}\hat{\mathfrak{a}_i}, ...`.

In fact, the structural properties that determine whether a meta-string belongs to the equivalence class are exactly the logical properties that determine its *canonical length* and *canonical character index*. 

.. [#1] Or :math:`\varepsilon\mathfrak{ab}`, or :math:`\mathfrak{ab}\varepsilon\varepsilon`, etc.? 

.. [#2] It should go without saying this is an artifact of the decimal representation of numbers. A different base would correspond to different addition rules, e.g. :math:`5 + 5 = A` in hexidecimal notation. However, the structural feature of :math:`0` exists in all bases, e.g. :math:`\exists 0: x + 0 = x` is true regardless of the physical and literal form of the algebraic abstraction :math:`x`. This is roughly analogous to :math:`\varepsilon` and :math:`\mathfrak{a}`; the former represent a structural feature of concatenated sequences whereas the latter corresponds to a physical character within the alphabet, i.e. the "base" of the system of concatenation. Regardless of the language and alphabet, the logical structure of concatenated expressions requires a metamathematical term to play the role of identity, e.g. :math:`\varepsilon`, whereas the characters, e.g. :math:`\frak{a}`, are symbolic representations of physical entities.

.. [#3] One is tempted here to draw an analogy to the natural and real numbers. One never *perceives* the domain :math:`S`, only the inscribed elements of it image :math:`\mathbb{S}`, the set of canonical strings. In the same way, one never perceives the domain :math:`\mathbb{R}`, instead encountering numbers through physically distinct instances that are united by their being the same (or *possessing a common property*).  

.. [#4] One should **not** conclude from this the left hand side is a literal string and this expression has the form of a definition, i.e. "*name = definition*". In fact, :math:`s` is also a *name*; it the *canonical* name of the string on the right hand-side. :math:`s = {\varepsilon}{s}` is an expression that identifies two different *names* (*references*) as pointing to the same *object* (*referent*).

.. [#5] Under this interpretation, the expression :math:`\varepsilon\hat{\varepsilon}\mathfrak{a} = \hat{\varepsilon}\mathfrak{a}`, but no further. This reinforces the view that :math:`\varepsilon` is a *formal* entity. It *cannot* be assigned a value in an interpretation without thereby becoming non-empty. 