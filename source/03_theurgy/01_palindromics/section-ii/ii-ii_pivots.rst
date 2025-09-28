
.. _palindromics-section-ii-ii:

Section II.II: Pivots
=====================

.. _palindromics-pivot-characters:

Pivot Characters
----------------

.. _palindromics-definition-2-2-1:

.. topic:: Definition 2.2.1: Pivot Characters

    Let :math:`s \in S`.

    The Left Pivot Character of :math:`s`, denoted :math:`\overrightarrow{\omega_s}`, is defined as the Character :math:`s[\overrightarrow{i}]`, where :math:`\overrightarrow{i}` is called the *Left Pivot Character Index*, which satisies the following conditions,

    1. If :math:`l(s)` is odd, then :math:`\overrightarrow{i} = \frac{l(s) + 1}{2}`
    2. If :math:`l(s)` is even, then :math:`\overrightarrow{i} = \frac{l(s)}{2}` 

    The Right Pivot, denoted :math:`\overleftarrow{\omega_s}`, is defined as the Character :math:`s[\overleftarrow{i}]`, where :math:`\overleftarrow{i}` is called the *Right Pivot Character Index*, which satisfies the following conditions,

    1. If :math:`l(s)` is odd, then :math:`\overleftarrow{i} = \frac{l(s) + 1}{2}`
    2. If :math:`l(s)` is even, then :math:`\overleftarrow{i} = \frac{l(s) + 2}{2}` 

    The *Pivot Character*, denoted :math:`\omega_s`, is defined as the Character which satisfies the following conditions,

    1. If :math:`\overleftarrow{\omega_s} = \overrightarrow{\omega_s}`, then :math:`\omega_s = \overleftarrow{\omega_s} = \overrightarrow{\omega_s}`
    2. If :math:`\overleftarrow{\omega_s} \neq \overrightarrow{\omega_s}`, then :math:`\omega_s = \varepsilon`

**Example** Let :math:`ᚠ = \text{strap on no parts}`. Then :math:`l(ᚠ) = 17`.

Thus, since :math:`l(ᚠ) = 17` is odd,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{17 + 1}{2} = 9`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{17 + 1}{2} = 9`
- *Left Pivot Character*: :math:`\overrightarrow{\omega_{ᚠ}} = ᚠ[9] = \sigma`
- *Right Pivot Character*: :math:`\overleftarrow{\omega_{ᚠ}} = ᚠ[9] = \sigma`
- *Pivot Character*: :math:`\omega_{ᚠ} =  ᚠ[9] = \sigma`

∎

**Example** Let :math:`ᚠ = \text{no noon on}`. Then `l(ᚠ)= 10`.

Thus, since :math:`l(ᚠ)= 10` is even,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{10}{2} = 5`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{10 + 2}{2} = 6`
- *Left Pivot Character*: :math:`\overrightarrow{\omega_{ᚠ}} = ᚠ[5] = \text{o}`
- *Right Pivot Character*: :math:`\overleftarrow{\omega_{ᚠ}} = ᚠ[6] = \text{o}`
- *Pivot Character*: :math:`\omega_{ᚠ} = \text{o}`

∎

**Example** Let :math:`ᚠ = \text{draw no dray a yard onward}`. Then `l(ᚠ)= 26`.

Thus, since :math:`l(ᚠ)= 26` is even,

- *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{26}{2} = 13`
- *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{26 + 2}{2} = 14`
- *Left Pivot Character*: :math:`\overrightarrow{\omega_{ᚠ}} = ᚠ[13] = \sigma`
- *Right Pivot Character*: :math:`\overleftarrow{\omega_{ᚠ}} = ᚠ[14] = \text{a}`
- *Pivot Character*: :math:`\omega_{ᚠ} = \varepsilon`

∎

.. note::

    From the previous examples, it should be clear a Pivot Character of a String is a Empty Character then the String Length is even. However, if a Pivot Characteris a non-Empty Character, then it cannot be concluded whether the String Length is odd or even.

    However, it should be clear that if a Pivot Character is non-Empty, it imposes certain structural constraints on the String. These structural constraints will be more fully elaborated in the next series of theorems.

.. _palindromics-theorem-2-2-1:

.. topic:: Theorem 2.2.1

    If a Canonical String has an odd number of Delimiter Characters and is equal to its own Inverse, then its Left and Right Pivot Characters are equal.

    .. math::
    
        \forall s \in S: ((\exists n \in \mathbb{N}: \Delta(s) = 2n + 1) \land (s = s^{-1})) \implies (\overrightarrow{\omega_s} = \overleftarrow{\omega_s})

**Proof**: Let :math:`s \in S` such that :math:`\Delta(s) = 2n + 1` for some :math:`n \in \mathbb{N}` and :math:`s = s^{-1}`. Then, by :ref:`Theorem 2.1.6 <palindromics-theorem-2-1-6>`,

.. math::

    \exists i \in N_{l(t)}: l(s) = 2i - 1

Therefore, :math:`l(s)` is odd. By :ref:`definition of Pivot Characters <palindromics-definition-2-2-1>`,

.. math::

    \overrightarrow{\omega_s} = s[\frac{l(s) + 1}{2}]

.. math::

    \overleftarrow{\omega_s} = s[\frac{l(s) + 1}{2}]

Thus,

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

Summarizing and generalizing,

.. math::

    \forall s \in S: ((\exists n \in \mathbb{N}: \Delta(s) = 2n + 1)) \implies (\overrightarrow{\omega_s} = \overleftarrow{\omega_s})

∎

.. _palindromics-theorem-2-2-2:

.. topic:: Theorem 2.2.2

    If a String in the Dialect has an even String Length and is equal to its own inverse, then its Left and Right Pivot Characters cannot be Delimiters.

    .. math::

        \forall s \in D: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies ((\overrightarrow{\omega_s} \neq \sigma) \land  (\overleftarrow{\omega_s} \neq \sigma))

**Proof** The proof is similar to :ref:`Theoreom 2.1.5 <palindromics-theorem-2-1-5>`. Let :math:`s,t \in D` such that :math:`\Delta(s) = 2n` for some :math:`n \in \mathbb{N}` and :math:`t = s^{-1}` with :math:`s = t`. Let :math:`m = l(s)`. Let :math:`P` be the set of Delimiter indices in :math:`s`,

.. math::

    P = \{ i \mid s[i] = \sigma \}

Then :math:`\lvert P \rvert = \Delta(s) = 2n` by assumption.

By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    t[i] = s[m - i + 1]

There are two cases to consider, :math:`l(s)` is even or :math:`l(s)` is odd.

.. EVEN CASE 

:underline:`Case I`: :math:`l(s) = m` is even.

Assume, for the sake of contradiction, :math:`s[\frac{l(s)}{2}] = s[\frac{m}{2}]= \sigma`. Then, every Delimiter must have a symmetric pair in :math:`P`.

.. math::

    t[i] = s[m - i  + 1]

So, using :math:`i = \frac{m}{2}`

.. math::

    t[\frac{m}{2}] = s[\frac{m}{2} + 1]

Therefore, 

.. math::

    s[\frac{m}{2}] = \sigma

.. math::

    s[\frac{m}{2} + 1] = \sigma

That is, two consecutive Characters in :math:`s` are Delimiters. But this is impossible if :math:`s \in D`. Therefore, it must be the case :math:`s[\frac{l(s)}{2}] \neq \sigma`. Likewise, :math:`s[\frac{l(s)}{2} + 1] \neq \sigma`. Since :math:`l(s)` is even, by :ref:`definition of Pivot Characters <palindromics-definition-2-2-1>`,

.. math::

    s[\frac{l(s) + 2}{2}] = \overleftarrow{\omega_s}

.. math::

    s[\frac{l(s)}{2}] = \overrightarrow{\omega_s}

It follows from this,

.. math::

    (\overleftarrow{\omega_s} \neq \sigma) \land (\overrightarrow{\omega_s} \neq \sigma)

.. ODD CASE 

:underline:`Case II`: :math:`l(s) = m` is odd. 

By :ref:`Theorem 2.1.7 <palindromics-theorem-2-2-1>`,

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s} \quad \text{ (1) }

Where, by :ref:`definition of Pivot Characters <palindromics-definition-2-2-1>`,

.. math::
    
    \omega_s = \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

.. math::

    \omega_s = s[\frac{l(s) + 1}{2}]

Assume, for the sake of contradiction, :math:`\omega_s = \sigma`. Then, by :ref:`Containment <palindromics-definition-1-2-5>`

.. math::

    s = (u)(\sigma)(v)

From the :ref:`definition of Delimiter Count <palindromics-definition-2-1-1>`,

.. math::

    \Delta(s) = \Delta(u) + \Delta(v) + 1 = \Delta(uv) + 1

Where the last equality follows from :ref:`Theorem 2.1.4 <palindromics-theorem-2-1-4>`. Thus, since :math:`\Delta(s)` is even, the number of Delimiters in :math:`uv` is odd,

.. math::

    \Delta(uv) = 2n - 1

Furthermore, by repeated application of :ref:`Theorem 1.2.1 <palindromics-theorem-1-2-1>`

.. math::

    l(s) = l(u) + l(\sigma) + l(v) = l(u) + l(v) + 1 = l(uv) + 1

Thus,

.. math::
    
    l(uv) = l(s) - 1 = m - 1 \quad \text{ (2) }
 
From which it follows :math:`l(uv)` is even.

By repeated application of :ref:`Theorem 1.2.10 <palindromics-theorem-1-2-10>`

.. math::

    s^{-1} = ((u)(\sigma)(v))^{-1} = (v^{-1})(\sigma^{-1})(u^{-1})

By assumption, :math:`s = s^{-1}`. Using :math:`\sigma^{-1} = \sigma`, the previous equation becomes,

.. math::

    (u)(\sigma)(v) = (v^{-1})(\sigma)(u^{-1})

Note :math:`\sigma` in :math:`(u)(\sigma)(v)` occupies the same Character Index as the :math:`\sigma` in :math:`(v^{-1})(\sigma)(u^{-1})`, since :math:`\omega_s = s[\frac{l(s) + 1}{2}] = \sigma` and :math:`\omega_{s^{-1}} = s[\frac{l(s) + 1}{2}] = \sigma`. By the Left and Right Cancellation property of :ref:`Equality Axiom <palindromics-axiom-ii>`, it follows,

.. math::

    u = v^{-1}

And 

.. math::

    v = u^{-1}

Therefore,

.. math::

    uv = (v^{-1})(u^{-1}) = (uv)^{-1}

Now, consider what has been shown of :math:`uv`. :math:`\Delta(uv) = 2n - 1` and :math:`uv = (uv)^{-1}`. By :ref:`Theorem 2.1.6 <palindromics-theorem-2-1-6>`, this implies 

.. math::

    \exists j \in N_{l(uv)}: l(uv) = 2j - 1

But this contradicts (2), which states :math:`l(uv)` is even, which in turn followed directly from the assumption :math:`l(s)` is odd. Therefore, the only possibility is :math:`\omega_s \neq \sigma`. Therefore, from (1),

.. math::

    \overleftarrow{\omega_s} \neq \sigma

.. math::

    \overrightarrow{\omega_s} \neq \sigma

∎

.. _palindromics-theorem-2-2-3:

.. topic:: Theorem 2.2.3

    .. math::

        \forall s \in S: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

**Proof** Let :math:`s \in S` such that :math:`s = s^{-1}`. Let :math:`t \in D` such :math:`t = s^{-1}` and :math:`\Delta(s) = 2n` for some :math:`n \in \mathbb{N}`. Let :math:`m = l(s)`. Let :math:`P` be the set of Delimiter indices in :math:`s`,

.. math::

    P = \{ i \mid s[i] = \sigma \}

Then :math:`\lvert P \rvert = \Delta(s) = 2n` by assumption.

By :ref:`String Inversion <palindromics-definition-1-2-8>`,

.. math::

    t[i] = s[m - i + 1]

There are two cases to consider, :math:`l(s)` is even or :math:`l(s)` is odd.

.. EVEN CASE 

:underline:`Case I`: :math:`l(s) = m` is even.

By :ref:`Definition of Pivot Characters <palindromics-definition-2-2-1>`,

.. math::

    \overrightarrow{i} = \frac{l(s)}{2} = \frac{m}{2} \quad \text{ (1) }

.. math::

    \overleftarrow{i} = \frac{l(s)}{2} + 1  = \frac{m}{2} + 1 \quad \text{ (2) }

Therefore, the Pivot Characters must be consecutive Characters. 

Since :math:`\lvert P \rvert`, each index :math:`i` has a symmetric pair given by the inversion :math:`m - i + 1`,

.. math::

    \overrightarrow{i}_{\text{pair}} = m - \overrightarrow{i} + 1 = \frac{m}{2} + 1 \quad \text{ (3) }

.. math:: 

    \overleftarrow{i}_{\text{pair}} = m - \overleftarrow{i} + 1 = \frac{m}{2} \quad \text{ (4) }

Therefore, from (1) and (4) the Left Pivot Character Index pairs with the Right Pivot Character Index, and from (2) and (3) the Right Pivot Character Index pairs with Left Pivot Character Index,

.. math::

    \overrightarrow{i}_{\text{pair}} = \overleftarrow{i}

.. math::

    \overleftarrow{i}_{\text{pair}} = \overrightarrow{i}

By :ref:`definition of String Inversion <palindromics-definition-1-2-8>`,

.. math::

    t[\overrightarrow{i}] = s[\overrightarrow{i}_{\text{pair}}] = s[\overleftarrow{i}]

.. math::

    t[\overleftarrow{i}] = s[\overleftarrow{i}_{\text{pair}}] = s[\overrightarrow{i}]

Plugging in values,

.. math::

    t[\frac{m}{2}] = s[\frac{m}{2} + 1]

.. math::

    t[\frac{m}{2} +1] = s[\frac{m}{2}]

Using the assumption :math:`s = t`, it follows,

.. math::

    s[\frac{m}{2} + 1] = s[\frac{m}{2}]

Therefore,

.. math::

    \overleftarrow{\omega_s} = \overrightarrow{\omega_s}

.. ODD CASE 

:underline:`Case I`: :math:`l(s) = m` is odd.

This follows directly from the :ref:`definition of Pivot Characters <palindromics-definition-2-2-1>`. Therefore, both cases are established. Summarizing and generalizing,

.. math::

    \forall s \in S: ((\exists n \in \mathbb{N}: \Delta(s) = 2n) \land (s = s^{-1})) \implies \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

∎

.. _palindromics-theorem-2-2-4:

.. topic:: Theorem 2.2.4

    If a String is equal to its own Inverse, then its Pivot Character is non-empty.
    
    .. math::

        \forall s \in S: (s = s^{-1}) \implies (\omega_s \neq \varepsilon)

**Proof** Let :math:`s \in S` such that :math:`s = s^{-1}`. 

By the laws of arithmetic, either :math:`\Delta(s)` is odd or it is even. 

If :math:`\Delta(s)` is odd, then by :ref:`Theorem 2.2.1 <palindromics-theorem-2-2-1>`, 

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

If :math:`\Delta(s)` is even, then by :ref:`Theorem 2.2.3 <palindromics-theorem-2-2-3>`,

.. math::

    \overrightarrow{\omega_s} = \overleftarrow{\omega_s}

In either case, the conclusion follows. Thus, summarizing and generalizing,

.. math::

    \forall s \in S: (s = s^{-1}) \implies (\omega_s \neq \varepsilon)

∎

.. note::

    :ref:`Theorem 2.1.10 <palindromics-theorem-2-2-4>` establishes that all invertible Strings in the Canon have a non-Empty Pivot Character. As an immediate corollary to this theorem, if a canonical String has an Empty Pivot Character, then it cannot be invertible.

    Furthemore, the contrapositive establishes a sufficient condition for *non-invertibiility*. In other words, if :math:`\omega_s = \varepsilon` it can be concluded :math:`s` is uninvertible. 

.. _palindromics-pivot-words:

Pivot Words
-----------

.. _palindromics-definition-2-2-2:

.. topic:: Definition 2.2.2: Pivot Word

    Let :math:`\zeta \in C`.

    The Left Pivot Word of :math:`\zeta`, denoted :math:`\overrightarrow{\Omega_{\zeta}}`, is defined as the Word :math:`\zeta[[\overrightarrow{j}]]`, where :math:`\overrightarrow{j}` is called the *Left Pivot Word Index*, which satisies the following conditions,

    1. If :math:`\Lambda(\zeta)` is odd, then :math:`\overrightarrow{j} = \frac{\Lambda(\zeta) + 1}{2}`
    2. If :math:`\Lambda(\zeta)` is even, then :math:`\overrightarrow{j} = \frac{\Lambda(\zeta)}{2}` 

    The Right Pivot Word, denoted :math:`\overleftarrow{\Omega_{\zeta}}`, is defined as the Word :math:`\zeta[[\overleftarrow{j}]]`, where :math:`\overleftarrow{j}` is called the *Right Pivot Word Index*, which satisfies the following conditions,

    1. If :math:`\Lambda(\zeta)` is odd, then :math:`\overleftarrow{j} = \frac{\Lambda(\zeta) + 1}{2}`
    2. If :math:`\Lambda(\zeta)` is even, then :math:`\overleftarrow{i} = \frac{\Lambda(\zeta) + 2}{2}` 

    The *Pivot Word*, denoted :math:`\Omega_{\zeta}`, is defined as the Character which satisfies the following conditions,

    1. If :math:`\overrightarrow{\Omega_{\zeta}} = (\overleftarrow{\Omega_{\zeta}})^{-1}`, then :math:`\overrightarrow{\Omega_{\zeta}} = (\overleftarrow{\Omega_{\zeta}})^{-1} = \Omega_{\zeta}`
    2. If :math:`\overrightarrow{\Omega_{\zeta}} \neq (\overleftarrow{\Omega_{\zeta}})^{-1}`, then :math:`\Omega_{\zeta} = \varepsilon`

.. note::

    In essence, the existence of a Pivot Character or Pivot Word in a Sentence is a property of a String's *self-invertibility*, i.e. :math:`s = s^{-1}`. All self-invertible Strings possess the property "*has a Pivot Character and Word*", but having this propery is not a *sufficient* for establishing self-invertibility.

    The existence of a Pivot Character and Pivot Word in a Sentence define a class of Sentences in the Corpus. However, the relationship between Pivot Characters and Pivot Words is deceptively subtle, as these next examples illustrate. 

**Example** 

1. Let :math:`ᚠ_1 = \text{i had not thought death had undone so many}`. Note :math:`\Lambda(ᚠ_1) = 9` and :math:`l(ᚠ_1) =  42`.

    The Pivot Word calculations proceed as follows,

    - *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{10}{2} = 5`
    - *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{10}{2} = 5`
    - *Left Pivot Word*: :math:`ᚠ_1[[3]] = \overrightarrow{\Omega_{ᚠ_1}} = \text{death}`
    - *Right Pivot Word*: :math:`ᚠ_1[[4]] = \overleftarrow{\Omega_{ᚠ_1}} = \text{death}`
    - *Pivot Word*: :math:`\Omega_{ᚠ_1} = \varepsilon`

    The Pivot Character calculations proceed as follows,

    - *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{42}{2} = 21`
    - *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{44}{2} = 22`
    - *Left Pivot Character*: :math:`ᚠ_1[21]= \text{a}`
    - *Right Pivot Character*: :math:`ᚠ_1[22]= \text{t}`
    - *Pivot Character*: :math:`\omega_{ᚠ_1} = \varepsilon`

2. Let :math:`ᚠ_2 = \text{no radar on}`. Note :math:`\Lambda(ᚠ_2) = 3` and :math:`l(ᚠ_2) = 11`

    The Pivot Word calculations proceed as follows,

    - *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{4}{2} = 2`
    - *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{4}{2} = 2`
    - *Left Pivot Word*: :math:`ᚠ_2[[2]] = \overrightarrow{\Omega_{ᚠ_2}} = \text{radar}`
    - *Right Pivot Word*: :math:`ᚠ_2[[4]] = \overleftarrow{\Omega_{ᚠ_2}} = \text{radar}`
    - *Pivot Word*: :math:`\Omega_{ᚠ_2} = \overrightarrow{\Omega_{ᚠ_2}} = (\overleftarrow{\Omega_{ᚠ_2}})^{-1} = \text{radar}`

    The Pivot Character calculations proceed as follows,

    - *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{12}{2} = 6`
    - *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{12}{2} = 6`
    - *Left Pivot Character*: :math:`ᚠ_2[6]= \text{d}`
    - *Right Pivot Character*: :math:`ᚠ_2[6]= \text{d}`
    - *Pivot Character*: :math:`\omega_{ᚠ_2} = \text{d}`

3. Let :math:`ᚠ_3 = \text{tell me stories}`. Note :math:`\Lambda(ᚠ_3) = 3` and :math:`l(ᚠ_3) = 15`

    The Pivot Word calculations proceed as follows,

    - *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{4}{2} = 2`
    - *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{4}{2} = 2`
    - *Left Pivot Word*: :math:`ᚠ_3[[2]] = \overrightarrow{\Omega_{ᚠ_3}} = \text{me}`
    - *Right Pivot Word*: :math:`ᚠ_3[[4]] = \overleftarrow{\Omega_{ᚠ_3}} = \text{me}`
    - *Pivot Word*: :math:`\Omega_{ᚠ_3} = \varepsilon`

    The Pivot Character calculations proceed as follows,

    - *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{16}{2} = 8`
    - *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{16}{2} = 8`
    - *Left Pivot Character*: :math:`ᚠ_4[6]= \sigma`
    - *Right Pivot Character*: :math:`ᚠ_4[6]= \sigma`
    - *Pivot Character*: :math:`\omega_{ᚠ_4} = \sigma`

4. Let :math:`ᚠ_5 = \text{emit naps noon span time}`. Note :math:`\Lambda(ᚠ_4) = 5` and :math:`l(ᚠ_4) = 24`.

    The Pivot Word calculations proceed as follows,

    - *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{6}{2} = 3`
    - *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{6}{2} = 3`
    - *Left Pivot Word*: :math:`ᚠ_4[[3]] = \overrightarrow{\Omega_{ᚠ_4}} = \text{noon}`
    - *Right Pivot Word*: :math:`ᚠ_4[[3]] = \overleftarrow{\Omega_{ᚠ_4}} = \text{noon}`
    - *Pivot Word*: :math:`\Omega_{ᚠ_4} = \overrightarrow{\Omega_{ᚠ_4}} = (\overleftarrow{\Omega_{ᚠ_5}})^{-1} = \text{noon}`

    The Pivot Character calculations proceed as follows,

    - *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{24}{2} = 12`
    - *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{26}{2} = 13`
    - *Left Pivot Character*: :math:`ᚠ_4[12]= \text{o}`
    - *Right Pivot Character*: :math:`ᚠ_4[6]= \text{o}`
    - *Pivot Character*: :math:`\omega_{ᚠ_4} = \text{o}`

5. Let :math:`ᚠ_5 = \text{the naps span now}`. Note :math:`\Lambda(ᚠ_5) = 4` and :math:`l(ᚠ_5) = 17`.

    The Pivot Word calculations proceed as follows,

    - *Left Pivot Word Index*: :math:`\overrightarrow{j} = \frac{4}{2} = 2`
    - *Right Pivot Word Index*: :math:`\overleftarrow{j} = \frac{6}{2} = 3`
    - *Left Pivot Word*: :math:`ᚠ_5[[2]] = \overrightarrow{\Omega_{ᚠ_5}} = \text{naps}`
    - *Right Pivot Word*: :math:`ᚠ_5[[3]] = \overleftarrow{\Omega_{ᚠ_5}} = \text{span}`
    - *Pivot Word*: :math:`\Omega_{ᚠ_5} = \overrightarrow{\Omega_{ᚠ_5}} = (\overleftarrow{\Omega_{ᚠ_5}})^{-1} = \text{naps}`

    The Pivot Character calculations proceed as follows,

    - *Left Pivot Character Index*: :math:`\overrightarrow{i} = \frac{18}{2} = 9`
    - *Right Pivot Character Index*: :math:`\overleftarrow{i} = \frac{18}{2} = 9`
    - *Left Pivot Character*: :math:`ᚠ_5[9]= \sigma`
    - *Right Pivot Character*: :math:`ᚠ_5[9]= \sigma`
    - *Pivot Character*: :math:`\omega_{ᚠ_5} = \sigma`

∎

.. _palindromics-theorem-2-2-5:

.. topic:: Theorem 2.2.5

    If a Sentence has an even Delimiter Count and the Pivot Word is non-Empty, then the Pivot Word is Reflective.

    .. math::

        \forall \zeta \in C: ((\exists i \in \mathbb{N}: \Delta(\zeta) = 2i) \land (\Omega_{\zeta} \neq \varepsilon)) \implies (\Omega_{\zeta} \in R)

**Proof** Let :math:`\zeta \in C`. Assume :math:`\Delta(\zeta) = 2i` for some :math:`i \in \mathbb{N}`. Then, by :ref:`Theroem 2.1.1 <palindromics-theorem-2-1-1>`,

.. math::

    \Lambda(\zeta) = 2i + 1.

Thus, :math:`\Lambda(\zeta)` is odd. By the :ref:`definition of Pivot Words <palindromics-definition-2-2-2>`,

.. math::

    \overrightarrow{j} = \frac{\Lambda(\zeta) + 1}{2}

.. math::

    \overleftarrow{j} = \frac{\Lambda(\zeta) + 1}{2}

Thus, 

.. math::

    \overrightarrow{\Omega_{\zeta}} = \overleftarrow{\Omega_{\zeta}}

If :math:`\Omega_{\zeta} \neq \varepsilon`, then by :ref:`definition of Pivot Words <palindromics-definition-2-2-2>`,

.. math::

    \Omega_{\zeta} = \overrightarrow{\Omega_{\zeta}} = ({\overleftarrow{\Omega_{\zeta}}})^{-1}

Thus, since the Pivot Words are the same Word,

.. math::

    \Omega_{\zeta} = {\Omega_{\zeta}}^{-1}

By :ref:`definition of Reflective Words <palindromics-definition-1-3-1>`,

.. math::

    \Omega_{zeta} \in R

Therefore, summarizing and generalizing,

.. math::

    \forall \zeta \in C: ((\exists i \in \mathbb{N}: \Delta(\zeta) = 2i) \land (\Omega_{\zeta} \neq \varepsilon)) \implies (\Omega_{\zeta} \in R)

∎

.. _palindromics-theorem-2-2-6:

.. topic:: Theorem 2.2.6

    If the Delimiter Count of a Sentence is odd and the Pivot Word exists, then the Pivot Word is Invertible.

    .. math::

        \forall \zeta \in C: (\exists i \in \mathbb{N}: \Delta(\zeta) = 2i + 1) \land (\Omega_{\zeta} \neq \varepsilon) \implies (\Omega_{\zeta} \in I)

**Proof** Let :math:`\zeta \in C` with :math:`\Delta(\zeta) = 2i + 1` for some :math:`i \in \mathbb{N}`. By :ref:`Theorem 2.1.1 <palindromics-theorem-2-1-1>`,

.. math::

    \Lambda(\zeta) = 2i + 2

Let :math:`m = \Lambda(\zeta)`. Therefore, by :ref:`definition of Pivot Words <palindromics-definition-2-2-2>`,

.. math::
    
    \overrightarrow{\Omega_{\zeta}} = \zeta[[\frac{m}{2}]]

.. math::

    \overleftarrow{\Omega_{\zeta}} = \zeta[[\frac{m + 2}{2}]]

Let :math:`\alpha_1 = \zeta[[\frac{m}{2}]] = \overrightarrow{\Omega_{\zeta}}` and :math:`\alpha_2 = \zeta[[\frac{m+2}{2}]] = \overleftarrow{\Omega_{\zeta}}`. By definition of a Sentence,

.. math::

    \alpha_1 \in L

.. math::

    \alpha_2 \in L

If :math:`\Omega_{\zeta} \neq \varepsilon`, then 

.. math::

    \Omega_{\zeta} = \alpha_1 = {\alpha_2}^{-1}

Applying :ref:`Theorem 1.2.9 <palindromics-theorem-1-2-9>`,

.. math::

    \Omega_{\zeta}^{-1} = {\alpha_1}^{-1} = \alpha_2

Therefore, since :math:`\Omega_{\zeta}^{-1} \in L`, from the :ref:`definition of Invertible Words <palindromics-definition-1-3-2>`,

.. math::

    \Omega_{\zeta} \in I

Summarizing and generalizing,

.. math::

    \forall \zeta \in C: (\exists i \in \mathbb{N}: \Delta(\zeta) = 2i + 1) \land (\Omega_{\zeta} \neq \varepsilon) \implies (\Omega_{\zeta} \in I)

∎

.. _palindromics-theorem-2-2-7:

.. topic:: Theorem 2.2.7

    The Inverse Pivot Word of an Invertible Sentence is the Pivot Word of its Inverse.

    .. math::

        \forall \zeta \in J: {\Omega_{\zeta}}^{-1} = \Omega_{\zeta^{-1}}


**Proof** Let :math:`\zeta \in J` with :math:`m = \Lambda(\zeta)`. 

By :ref:`Theorem 1.4.12 <palindromics-theorem-1-4-12>`, :math:`\Lambda(\zeta^{-1}) = m`

By :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>`, 

.. math::

    {\zeta}^{-1}[[i]] = (\zeta[[m - i + 1]])^{-1}

.. TODO: need to establish Pivot Word is non-Empoty.

.. CASE I

:underline:`Case I`: :math:`m = 2i`.

By :ref:`Theorem 2.1.1 <palindromics-theorem-2-1-1>`, :math:`Delta(\zeta)` is odd.

TODO

:underline:`Case II`: :math:`2i + 1`

Since :math:`m` is odd, there must be an inverse index which is equal to its original index,

    i = m - i + 1 

.. math::

    i = \frac{m+ 1}{2}.

By :ref:`Theorem 2.1.1 <palindromics-theorem-2-1-1>`, :math:`Delta(\zeta)` is even. 

TODO 

.. The next line only follows if it is established Pivot Word is non-empty. 

By :ref:`Theorem 2.2.5 <palindromics-theorem-2-2-5>`, :math:`\Omega_{\zeta} \in R`.

TODO

.. ..............................................................................
.. ................................. TODO .......................................
.. ..............................................................................

∎

.. _palindromics-subvertible-sentences:

Subvertible Sentences
---------------------

.. _palindromics-definition-2-2-3:

.. topic:: Definition 2.2.3: Subvertible Sentences

    The set of Subvertible Sentences, denoted :math:`\cancel{J}`, is defined as the set of Sentences which satisfy the open formula,

    .. math::

        \zeta \in \cancel{J} \equiv ((\Omega_\zeta \neq \varepsilon) \land (\omega_\zeta \neq \varepsilon))

    A Sentence is called *Subvertible* if it belongs to the class :math:`\cancel{J}`

**Example** The following table lists some Subvertible Sentences in :math:`L_\text{english}`

.. list-table:: 
    :widths: 50 50 50
    :header-rows: 1
    
    * - Subvertible Sentence
      - Pivot Character
      - Pivot Word
    * - the level was
      - v
      - level
    * - he sees me
      - e
      - sees
    * - what mom said
      - o
      - mom
    * - that devil lived here
      - :math:`\sigma`
      - devil
    * - his gateman nametag read
      - n
      - gateman
    * - my dad recovers
      - r
      - dad

∎

.. note::

    As the previous example demonstrates, Invertible and Subvertible Sentences form a pair of overlapping sets. In other words, all Sentences can be classified according to one of the following cases,

    - Invertible and Subvertible: :math:`J \cap \cancel{J}` 
    - Invertible and Not Subvertible: :math:`J \cap \cancel{J}^{c}`
    - Not Invertible and Subvertible: :math:`J^{c} \cap \cancel{J}`
    - Not Invertible and Not Subvertible: :math:`J^{c} \cap \cancel{J}^{c}`

    As example of a :math:`ᚠ \in J_{\text{english}} \cap \cancel{J}^{c}_{\text{english}`,

    .. math::

        ᚠ = \text{emit naps} 

    .. math::

        ᚠ^{-1} = \text{span time}

    But,

    .. math::

        \Omega_{ᚠ} = \varepsilon

.. ..............................................................................
.. ................................. TODO .......................................
.. ..............................................................................


.. _palindromics-theorem-2-2-8:

.. topic:: Theorem 2.2.8

    All Invertible Sentences do not contain a Reflective Word if and only if the intersection of Invertible and Subvertible Sentences is null.

    .. math::

        \forall \zeta \in J: (\nexists \alpha \in R: \alpha \subset_s \zeta) \equiv (\cancel{J} \cap J = \varnothing)

**Proof** Let :math:`\zeta \in K`. Let :math:`n = Lambda(\zeta)` and :math:`m = l(\zeta)`. Then, by :ref:`Theorem 1.4.11 <palindromics-theorem-1-4-11>`, for all :math:`i \in N_n`,`

.. math::

    {\zeta}^{-1}[[i]] = (\zeta[[\Lambda(\zeta) - i + 1]])^{-1}

(:math:`\rightarrow`) Assume :math:`\forall \alpha \in R: \neg(\alpha \subset_s \zeta)`.

TODO 

(:math:`\leftarrow`) Assume :math:`(J \cap \cancel{J} \neq \varnothing)`

TODO

.. 