

Probabilistic Truth
-------------------

Before we attempt to introduce interpretations, let's refine the primitive notions of this emergent explication of the notion of "*truth*". I think your line of thought about equating samples spaces with interpretations is along the right lines, but before making that jump, let's set a strong foundation. I propose the following (slight) modification of Kolmogrov's axioms of probability,

.. topic:: Definitions 

    1. Elementary Events: Lowercase letters from the beginning of the alphabet denote elementary events, *a*, *b*, *c*, etc.
    2. Abstract Events: Uppercase letters denote random events, **A**, **B**, **C**, etc. 
    3. Sample Space: The capital letter, **S**.
    4. Propositions: Lowercase letters from the middle of the alphabet denote propositions, *p*, *q*, *r*, etc. 
   
The sample space is the aggregation of elementary events. Abstract events are taken from the power-set (field) of the sample space. Furthermore, a simplified version of Kolmogrov's axiom will be adopted. 

.. math::

    \forall A: P(A) \geq 0

.. math::

    P(S) = 1

.. math::

    \forall i \neq j: A_i \cap A_j = \varnothing \implies P(\bigcup\limits_{i=1}^{n} A_i) = \sum_{i=1}^n P(A_i)

We refine the notion of an *elementary event* to be the *actual* occurence of an object. It is not a truth-value, it is a term (possibly compound) of the language. 

**Example**

    *c* = "the coin"

Notice I am begin careful to let *c* be an *object term*. It represent a *thing* which has the ability to be indeterminate in a random manner. It can be assigned descriptive, semantic content in a language. Notice moreover, I am using a *particularizing* article in addressing the object in the propositional component, namely *the* coin. Then the notion of an abstract event is exactly equivalent to the assertion of *the coin* belonging to the class of things that are "*heads up*" or "*heads down*", e.g. 

**Example**

    **H** = "heads up"

    **T** = "heads down"

So, an event is *measureable* if and only if is an assertion of the relation of belonging that obtains between an elementary event and an abstract event, 

.. math::

    c \in H

In other words, every *measureable event* is a truth-value, i.e. an assertion of belonging to one class to the exclusion of others. 

With these assumptions, the following explication of the truth predicate is presented,

.. topic:: Probabilistic Explication of Truth

    .. math::

        p \equiv ((p = a \in A) \equiv P(A) = 1)

Let's think about how we analyze a simple example in classical probability. A coin is flipped and has two outcomes *h* and *t*. We say the outcome is heads by defining the events of "getting a head" and "getting a tail" as :math:`H` and :math:`H^c`

.. math::

    S = \{ h, t \}

.. math::

    H = \{ h \}

.. math::

    T = \{ t \}

In order to talk about the outcomes, i.e. the source of randomness, they must first be wrapped in a layer of abstraction via categorization, so that they can then be counted and the probability can be naively approximated as the ratio of outcomes,

.. math::

    P(H) = \frac{n(H)}{n(S)}

But this is a vast over-simplification. It is not clear in Kolmogrov's formulation of probability what an *elementary event* is, only that measureable events should be sets of them. There does not appear to be room to talk about the "coin" in this formulation; i.e. the object being measured has been split into a multiplicity of elementary events. It is not that the "coin" is one object two sides, but that the "coin" is really two things simultaneously.

In other words, "the coins is heads" is not a proposition in the language of Kolmogrov's probability. Rather, the "the token of an outcome belongs to a measurable event" is all that is being asserted with Kolmogrov's probability predicate. 

.. math::

    \mathbb{X}: \text{powerset}(S) \rightarrow [0, 1]

.. math::

    \text{coin is heads} \equiv h \in H

.. math::

    \text{coin is tails} \equiv 