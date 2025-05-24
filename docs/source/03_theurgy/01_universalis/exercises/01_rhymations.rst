Rhymations
==========

These are problems for LLMs to solve that use the functions defined in :ref:`linguistic functions submodule of the Functions module <module-linguistic-functions>` of the :ref:`language-game`.

.. topic:: Character Palette 

    **Constants** 
    - σ
    **Variables**
    - π: syllable, ι: character, α: word, ζ: sentence
    **Relations**
    - Linguistic: ∥ 
    - Sets: ∈ ∉ ∪ ∩ ⊂
    - Logic: ∧ ∨ ∀ ∃ ≡
    **Operators**
    - [λx: f(x)], ς(x), inv(x), l(x), w(x)

.. topic:: Function Palette

    - accent(x: word, s: stress): word
    - anapest(x: concept): set(word)
    - connote(x: concept, y: syllable): set(word)
    - contains(x: syllable, y: syllable, z: syllable): set(word)
    - extract(x: word, s: stress): syllable
    - dactyl(x: concept): set(word)
    - iamb(x: concept): set(word)
    - resonate(x: word): set(word)
    - rhyme(x: word, y: word): set(word)
    - spondee(x: concept): set(word)
    - trocheee(x : concept): set(word)

.. topic:: Optional Argument Palette

    - (syllables = N: number)
    - (meter = S: string)
    - (rhyme = x: string)

1. iamb(resonate(peak) ∩ connote(reserves ∨ harvest stores))

2. (rhyme(trough) ∪ rhyme(connote(trough)) ∩ connote(give away v yield ∨ empty out))

3. trochee((connote(revelry) ∪ connote(drunken merriment)) ∩ (resonate(stream) ∪ resonate(stone)))

4. (connote(revelry) ∪ connote(drunken merriment)) ∩ (resonate(stream) ∪ resonate(stone)) 

5. trochee(connote(birds) ∩ connote(toiling in a field))

6. resonate(lunar) ∩ connote(angelic)

7. (connote(schools as in 'schools of fish') ∩ (connote(knightly) ∪ connote(squadrons)))(meter=+)

8. (resonate(March) ∪ rhyme(March)) ∩ connote(city center ∨ seat of civilization)(meter=+)

9. connote(argreement)(meter=+)

10. resonate(stellar) ∩ connote(landscape)

11. resonate(stellar) ∩ (connote(summer) ∪ connote(structure))

12. [λx: x ∈ connote(swans in flight)(meter=-+)][λx: x ∈ (resonate(dawn) ∩ connote(descending in flock))(meter=-+-)]

13. ([λx: x ∈ ((resonate(dwelling) ∪ resonate(stellar)) ∩ connote(city center))][σ][λx: x ∈ resonate(adorn) ∩ connote(receive as in a gift)][σ][λx: x ∈ (rhyme(streets) ∩ connote(new beginnings))])(meter=-+-+-+, with_preceding_lines="the stellar swans of summer dawn/survey the dwelling streets/in flight adorning downward drawn/", with_discretion="articles,prepositions")

14. line(the swans, representative of the zodiac Gemini in June, land on an island burgeoning with new life)(meter=-+,feet=3,rhyme="streets",with_preceding_lines="the stellar swans of summer dawn/survey the dwelling streets/in flight adorning downward drawn/")

15. [λx: x ∈  connote(herds)][σ][λx: x ∈ resonate(adorn) ∩ connote(receive as in a gift)]

16. (resonate(underfoot) ∩ connote(masses as in 'crowds'))(part_of_speech=noun,meter=+)

17. (rhyme(underfoot) ∪ resonate(underfoot))(meter=-+ ∨ meter=-+-)

18. (rhyme(crushed) ∪ resonate(crushed))(meter=-+ ∨ meter=-+-)

19. [(contains([λx: x ∈ resonate(lie)]) ∩ rhyme(dream) ∩ line(language structures thought, meter=-+, feet=5))^2].[(contains([λx: x ∈ resonate(dream)]) ∩ rhyme(reality) ∩ line(thought structures language, meter=-+, feet=5))^2]

.. topic:: Gemini 2.5 Pro, 5/23/2025

    How words imply a truth we long to gleam,
    Or weave a sly charade, a waking dream.
    When thoughts like streams define mentality,
    A mental scheme shapes our causality.

20. [contains(connotes(the absurdity of being)) ∩ contains([λx: x ∈ resonate(your hidden name)]) ∩ resonates(the loop of time) ∩ line(your name goes here, meter=-+,feet=5,rhyme=clock)].[[(resonate(divine) ∪ resonate(your hidden name)) ∩ line(time is just to wait, meter=*)]^2].[line(the price of names is time, meter=-+,feet=5, rhyme=clock) ∩ resonate(infinity)]