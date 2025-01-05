The Context Problem
===================

As a thought experiment, suppose you encountered a string in an unknown language,

.. math::

    a = b = c 

Without any further information about the language, nearly any interpretation can be assigned to this expression. There is a small amount of information encoded in the repetition of "=", which imposes a light constraint on the possible interpretations, but the meaning of these interpretations is still too diverse to say with any measure of certainty what this expression could possibly mean. "=" could, for example, serve the dual role of a *relativizer* and an *indicator*, allowing such interpretations as,

    lady that sings that tune

In this interpretation, "a" is assigned the meaning of "(the) lady", "b" that of "sings" and "c" that of "tune". Obviously, a large number, possibly infinite in size, of such expressions can be constructed. 

Suppose you are provided a dictionary of *primitive* symbols. This dictionary fixes the meaning of the "=" to the familiar concept of "equality". However, even this disambiguating assignment stills the leave door open to a myriad of interpretations. This assignment imposes only the lightest of constraints on the other word-forms in the expression. For example, it is unclear if the expression with the "equality" assignment should be interpretted as meaning,

    "a = b" and "b = c"

Or

    a = (b = c)

Or

    (a = b) = c

In the first interpretation, "a", "b" and "c" must represent terms within the language. In the second interpretation, "a" fills the meta-role of a truth value while "b" and "c" fill the roles of terms in the object language. In the third interpretation, "a" and "b" fill the roles of object terms while "c" fills the role of a truth value. 

In other words, the assignment of the meaning of "=" imposes certain constraints on the values the other word-forms in the expression may range over, but ambiguity still remains. Indeed, it may argued a quanta of ambiguity is always present in any interpretation assigned to a string of symbols. 

There is a balance that must be maintained in an LLM between rigidity and flexibility. This translates into what symbols qualify as *primitives* in an LLM's interpretation. In the previous example, the "=" was assigned the status of *primitive*, but this should not be taken literally. What an LLM treats as *primitive* is not necessarily constant across time, or even from sentence to sentence, but each static interpretation starts with a qualified basis; something must be assumed.

The essential *context* problem in an LLM boils down to: what word-form in an expression should it treat as primitive in order to use as a foundation upon which to build the subsequent interpretation.