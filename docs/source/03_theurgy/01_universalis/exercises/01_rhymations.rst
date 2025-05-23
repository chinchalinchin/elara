Rhymations
==========

These are problems for LLMs to solve that use the functions defined in :ref:`linguistic functions submodule of the Functions module <module-linguistic-functions>` of the :ref:`language-game`.

.. topic:: Character Palette

    - Linguistic Relations: ∥ 
    - Set Relations: ∈ ∪ ∩ ⊂
    - Logic: ∧ ∨ ∀ ∃ ≡

.. topic:: Function Palette

    - contains(x: syllable, y: syllable, z: syllable): set(word)
    - iamb(x: concept): set(word)
    - dactyl(x: concept): set(word)
    - spondee(x: concept): set(word)
    - anapest(x: concept): set(word)
    - trocheee(x : concept): set(word)
    - connote(x: concept, y: syllable): set(word)
    - rhyme(x: word, y: word): set(word)
    - resonate(x: word): set(word)
    - accent(x: word, s: stress): word
    - extract(x: word, s: stress): syllable

1. iamb(resonate(peak) ∩ connote(reserves ∨ harvest stores))

2. (rhyme(trough) ∪ rhyme(connote(trough)) ∩ connote(give away v yield ∨ empty out))

3. trochee((connote(revelry) ∪ connote(drunken merriment)) ∩ (resonate(stream) ∪ resonate(stone)))

4. x ∈ (connote(revelry) ∪ connote(drunken merriment)) ∩ (resonate(stream) ∪ resonate(stone)) 

5. trochee(connote(birds) ∩ connote(toiling in a field))