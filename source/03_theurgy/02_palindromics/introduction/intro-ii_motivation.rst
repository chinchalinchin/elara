.. _palindromics-motivation:

Motivation
==========

.. note::

    The contents of this section are more for the author's benefit than the reader's. The nature of the formal system being constructed has forced the author to confront some of the basic notions that underlie the modern theory of strings and analyze them from a philsophical point of view. This section represents the author's attempt to provide an epistemological justification for the assumptions adopted within the system.

Concatenation is unique within the domain of mathematics. Formal logic, as a method of inquiry, is wholly dependent on the ability to concatenate symbols in sequence to express complex and abstract logical relations. One cannot formalize concatenation without engaging in the act of "concatenating". This does not mean concatenation cannot be formalized, as evidenced by the mature fields of regular expressions and formal language theory. However, it *does* mean the formalization often obscures what is being formalized, as the formalization is itself an instance of the formalized.

What is meant by the formal expression ":math:`\mathfrak{a}\varepsilon\mathfrak{b}`"? And in what ways does this expression differ from the formal expression ":math:`\mathfrak{ab}`"? [#1]_ More fundamentally, what is meant by the singular formal entity, ":math:`\mathfrak{a}`" and what relation does it bear to the physical inscription *a*? 

Often, one operates as if ":math:`\mathfrak{a}`" were both the symbolic representation of a linguistic unit and the linguistic unit being symbolized, i.e. the first letter of the English alphabet. In other words, it is easy to leave unappreciated the fact ":math:`\mathfrak{a}`" and the physical inscription *a* are materially different in their purpose and use. 

This problem is reminiscent of the indefinablity of truth, discussed by Alfred Tarski in his landmark *On The Concept of Truth in Formalized Languages* published in 1933, where his examinations of the antimony

    "x" is true if and only if x

led him to rigorously elaborate a structural definition of logical sentences, in which expressions about a language could be asserted and proven. Like Tarski advised in his construction, it is important to distinguish between the *name* of entity within a formal system, and the *entity* itself. Likewise, as the current formal system is developed, it important to keep the following in mind,

    ":math:`\mathfrak{a}`" is the name of *a*

The symbol ":math:`\mathfrak{a}`" is the logical abstraction assigned to the physical entity *a* **within the formal system**. It is a metamathematical object. Expressions within which it occurs do not occur within the same language about which it is making assertions.

For this reason ":math:`\mathfrak{a}\varepsilon\mathfrak{b}`" should not be treated as a literal string, no more than the arithmetical expression ":math:`1 + 0`" should be taken as the literal number which it represents, e.g. ":math:`1`". Arithmetical expressions are logical abstractions of the numbers they represent; In Fregean terms, they are *references*, not *referents*. 

":math:`\varepsilon`" is not a literal string. There are no literal strings to be found in natural language that are formed by sequencing an empty character with other characters, let alone a string composed of nothing but the empty character. The formal strings

.. math::

    \mathfrak{a}\varepsilon, \mathfrak{a}\varepsilon\varepsilon, \mathfrak{a}\varepsilon\varepsilon\varepsilon, ...

are not representative of unique physical strings. They are artifacts of abstraction, akin to :math:`1.0, 1.00, 1.000, 1.0000, ...`. It must be kept in mind they are *logically equivalent* representatives of the same underlying physical string, namely the string denoted by the name ":math:`\mathfrak{a}`". The formal system adopts the adage of Alain Badiou, "the name of the void is a pure *proper name*, which indicates itself, which does not bestow any index of difference within what it refers to, and which auto-declares itself in the form of the multiple, despite there being nothing which is numbered by it."

When one is engaged in language, there are no ":math:`\varepsilon`"'s; the term is meaningless; it has no *referent* at the object level. Just as one carries a ":math:`1`" and adds a ":math:`0`" when performing the operation described in the expression denoted by the name ":math:`5 + 5`" [#2]_, yet understands this process in no way maps to physically rearranging groups of objects in the world, one must keep in mind ":math:`\mathfrak{ab}\varepsilon`" is nothing more than a bookkeeping mechanism. 

The question then arises, what *is* ":math:`S`", the domain of all finite Strings? If the preceding has been understood, then the only answer is: it is a set of *references*, not *referents*. In other words, ":math:`\varepsilon\mathfrak{a}`", ":math:`\varepsilon\varepsilon\mathfrak{a}`", etc. all belong to the set denoted by ":math:`S`". Statements and assertions made regarding ":math:`S`" are statements about the *names* of strings. 

However, due to the inescapable circle of having to represent the operation of concatenation with concatenated strings, there arises a confounding problem in the formal theory of strings. The set of strings denoted by ":math:`S`" that bear the property of being ":math:`\varepsilon`-free" directly map to the *physical inscription* they represent. Moreover, this set of strings has special properties. 

In the course of :ref:`Section I <palindromics-section-i>`, the operation of canonization, ":math:`\pi(s)`", will be discussed in detail. For the current purposes, it suffices to think of ":math:`\pi(s)`" as function that strips *the name of the string* of empty characters and produces the *canonical* form of a string. The set of all canonical strings is then isomorphic to the *physical* strings it represents. 

The metamathematical properties of canonical strings are therefore *physical* properties of the strings they represent. For this reason, the formalization and the objectification intersect. The properties of canonical strings in a formal system are exactly the properties exhibited by strings in the model which satisfies the formalization.

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

Which illustrates that inversion is simply an instruction to concatenate its input in a certain order. The basis clause of concatenation, ":math:`s = {\varepsilon}{s}`", a standard definition, implicitly involves stripping as string of its empty characters, meaning once the output of concatenation has been assigned it no longer bares any ":math:`\varepsilon`", i.e. has property ":math:`\varepsilon`-free". It is this property that allows expressions such as ":math:`s = {\varepsilon}{s}`", for the right hand side is simply a *name* of the left hand side. [#3]_

The expression

.. math::

    (\mathfrak{ab}\varepsilon)^{-1}

must therefore be attended to with careful scrutiny. The inversion is **not** being applied to the literal string ":math:`\mathfrak{ab}\varepsilon`", for this quantity is a formal entity, as evidenced by the presence of ":math:`\varepsilon`" within it. The inversion does not operate on *formal entities*, it operates on the *objects* to which they refer. Therefore, inversion does **not** apply to the domain ":math:`S`". 

The typical recursive definition of inversion, while rigorous and correct, obscures this fact by seeming to imply through its basis clause the result of an inversion may be an empty string. However, execution of the algorithm reveals it is hiding the removal of ":math:`\varepsilon`" through concatenation.

.. No, not quite. the standard definition implies through the induction clause and concatenation that it does not operate on empty strings, because the concatenation implicitly removes it before it gets to the inversion "function call".

Consider ":math:`\mathfrak{a}^{-1}`". By the induction hypothesis, it is required to express this string as a concatenation, :math:`s = ({a}{\varepsilon})`, so the definition may recursively call the basis clause to end its "function call". Indeed,

.. math::

    \mathfrak{a}^{-1} = (\mathfrak{a}\varepsilon)^{-1} = (\varepsilon^{-1})(\mathfrak{a})

And the quantity ":math:`\varepsilon^{-1}`" ends the recursion by yielding ":math:`\varepsilon`", which is then concatenated into the result to yield, 

.. math::

    \mathfrak{a}

However, it should be noted this is a purely formal process. It describes the structural and metamathematical properties of strings. It is the *bookkeeping* mechanism that formalizes the object-level operation of inversion. 

.. IN PROGRESS

.. [#1] Or :math:`\varepsilon\mathfrak{ab}`, or :math:`\mathfrak{ab}\varepsilon\varepsilon`, etc.? 

.. [#2] It should go without saying this is an artifact of the decimal representation of numbers. A different base would correspond to different addition rules, e.g. ":math:`5 + 5 = A`" in hexidecimal notation. However, the structural feature of ":math:`0`" exists in all bases, e.g. ":math:`\exists 0: x + 0 = x`" is true regardless of the physical and literal form of the algebraic abstraction ":math:`x`". This is roughly analogous to ":math:`\varepsilon`" and ":math:`\mathfrak{a}`"; the former represent a structural feature of concatenated sequences whereas the latter corresponds to a physical character within the alphabet, i.e. the "base" of the system of concatenation. Regardless of the language and alphabet, the logical structure of concatenated expressions requires a metamathematical term to play the role of identity, e.g. ":math:`\varepsilon`", whereas the characters, e.g. ":math:`\frak{a}`", are symbolic representations of physical entities.

.. [#3] One should **not** conclude from this the left hand side is a literal string and this expression has the form of a definition, i.e. "*name = definition*". In fact, ":math:`s`" is also a *name*; it the *canonical* name of the string on the right hand-side. ":math:`s = {\varepsilon}{s}`" is an expression that identifies two different *names* (*references*) as pointing to the same *object* (*referent*).