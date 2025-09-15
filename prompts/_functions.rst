.. topic:: accent(x: syllable, s: stress) -> set(word)

    If a prompt contains ``accent(x,s)``, this prompt is asking for a set of words, possibly empty, that contain the syllable ``x`` with the stress ``s``, where ``s = +`` means stressed and ``s = -`` means unstressed. For example, ``concord (CON-cord)`` is a solution to ``accent(con,+)`` whereas ``connect`` (con-NECT) is a solution to ``accent(con,-)``. 

    Regex-like expressions are sometimes used to denote where the stress should be inserted, e.g. ``accent(gen,.-.*)`` means any word where the second syllable ``gen`` is unstressed followed by an arbitrary number of syllables, such as ``regencies`` or ``agent``; in other words "." are used to denote single syllables and ".*" are used to denote an arbitrary number of syllables.

.. topic:: extract(x: word, s: stress) -> syllable

    Shorthand: ``ext(x,s)``

    If a prompt contains ``extract(x,S)``, this prompt is asking to extract a specific syllable from word ``x`` based on the stress ``S``: if ``S = +``, it refers to the main stressed syllable; if ``S = -``, it refers to an unstressed syllable (e.g., the first such syllable if multiple exist). For example, ``turn`` is the valid solution to ``extract(return,+)`` whereas ``re`` is the valid solution to ``extract(return,-)``.

.. topic:: line(x: concept) -> string

    Shorthand: ``li(x)``

    If a prompt contains ``line(x)``, for any string ``x``, this prompt is asking for a line that implements the description given in ``x``. This function is often used with optional arguments ``meter`` and ``feet``. 

.. topic:: chiasmate(x: sentence) -> sentence

    Shorthand: ``ch(x)``

    If a prompt contains ``chiasmate(x)`` or ``ch(x)``, the prompt is asking for a sentence that bears the relation of *chiasmus* with the sentence ``x``. For example, ``beauty is truth`` is ``chiasmate(truth is beauty)``.

.. topic:: etymology(x: word) -> description 

    Shorthand: ``ety(x)``

    If a prompt contains ``etymology(x)``, the prompt is asking for a detailed etymological breakdown of the word ``x``. For example, ``ety(is)`` should provide a historical account starting with the earliest documented linguistic records up to modern English.

.. topic:: graph(x: description) -> matplotlib script

    If a prompt contains ``graph(x)``, where ``x`` is a description, this prompt is asking for a ``matplotlib`` script to generate a plot of the concept ``x``.