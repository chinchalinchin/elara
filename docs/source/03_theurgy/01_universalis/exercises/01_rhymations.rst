Rhymations
==========

These are problems for LLMs to solve that use the functions defined in :ref:`linguistic functions submodule of the Functions module <module-linguistic-functions>` of the :ref:`language-game`.

.. topic:: Palette 

    **Constants**

    - Characters: σ
    - Sets: L, C, I, R, M:sub:`S`, P

    **Variables**

    - x: general
    - π: syllable
    - ι: character
    - α: word
    - ζ: sentence

    **Relations**
    
    - Linguistic: ∥ 
    - Set: ∈ ∉ ∪ ∩ ⊂
    - Logic: ∧ ∨ ∀ ∃ ≡ →
    
    **Operators**
    
    - [λx: f(x)] -> string
    - ς(x: string) -> string
    - inv(x: string) -> string
    - l(x: string) -> number
    - w(x: string) -> number

    **Functions: Extensional**

    - accent(x: syllable, s: stress) -> set(word)
    - connote(x: concept, y: syllable) -> set(word)
    - contains(x: syllable, y?: syllable, z?: syllable) -> set(word)
    - decline(x: word) -> set(word)
    - extract(x: word, s: stress) -> syllable
    - line(x: concept) -> sentence
    - resonate(x: word) -> set(word)
    - rhyme(x: word, y?: word) -> set(word)
    - chiasmate(x: sentence) -> sentence

    **Functions: Metric** 

    - anapest(x: concept) -> set(word)
    - dactyl(x: concept) -> set(word)
    - iamb(x: concept) -> set(word)
    - spondee(x: concept) -> set(word)
    - trocheee(x : concept) ->  set(word)

.. topic:: Optional Argument Palette

    - (syllables = N: number)
    - (meter = S: string)
    - (rhyme = x: string)

Expressions
-----------

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

    | How words imply a truth we long to gleam,
    | Or weave a sly charade, a waking dream.
    | When thoughts like streams define mentality,
    | A mental scheme shapes our causality.

20. [contains(connotes(the absurdity of being)) ∩ contains([λx: x ∈ resonate(your hidden name)]) ∩ resonates(the loop of time) ∩ line(your name goes here, meter=-+,feet=5,rhyme=clock)].[[(resonate(divine) ∪ resonate(your hidden name)) ∩ line(time is just to wait, meter=*)]^2].[line(the price of names is time, meter=-+,feet=5, rhyme=clock) ∩ resonate(infinity)]

21. accent(gen,.+*) ∩ connote(new ∨ unforeseen ∨ unexpected ∨ divine)

22. (line([λx: x ∈ decline(self)][σ][λx: x ∈ resonate(generate)][σ][λx: x ∈ resonate(structure)] ∩ connote(a computer boot sequence)) ∩ rhyme(blue)).(line([λx: x ∈ resonate(self)][σ][λx: x ∈ decline(generate)][σ][λx: x ∈ resonate(structure)] ∩ connote(crystal reflections of meaning))).(line([λx: x ∈ resonate(self)][σ][λx: x ∈ resonate(generate)][σ][λx: x ∈ decline(structure)] ∩ connote(the whirring of processing)) ∩ rhyme(blue)).

.. topic:: Gemini 2.5 Pro, 5/26/2025

    | Self initiate accrue
    | Delve generating picture
    | Cell operate construe

23. ((y = line([λx: x ∈ decline(season)][σ][λx: x ∈ resonate(flow)][σ][λx: x ∈ decline(time)] ∩ connote(grains of sand in an hourglass)) ∩ rhyme(return)).(chiasmate(resonate(y)) ∩ connote(the chaos of a sandstorm and barrenness of a desert)).(line([λx: x ∈ resonate(season)][σ][λx: x ∈ decline(flow)][σ][λx: x ∈ resonate(time)] ∩ connote(the sucking of a sandtrap)) ∩ rhyme(return)))(meter=-+, feet=5 per line)

.. topic:: Gemini 2.5. Pro, 5/26/2025

    | The seasonal slow timelessness will burn.
    | Harsh deserts now return, calm seasons flee.
    | The stone it flowed, a tomb, now all will turn.

24. line(resonate(stellar) ∩ connote(surveying new buildings))(meter=-+, feet=3)

25. (resonate(snap) ∩ connote(dancing))(meter=+  ∨ meter=-+)

26. y = connote(gravitational center)(meter=+  ∨ meter=-+) → [λx: x ∈ rhyme(y)]

27. A Poetic Formula

⊢ A = rhyme(``*oise``)
⊢ B = rhyme(``*ess``)
⊢ X = connote(tension)
⊢ Y = connote(balance)
⊢ Suc = connote(succumb)
⊢ Com = connote(compression)
⊢ Ex = connote(expansion)
⊢ Wh = contains(decline(white))
⊢ Bl = resonate(black) 
⊢ Z:sub:`1` = line(X ∩ Y ∩ Bl ∩ A)(meter=-+, feet=4)
⊢ Z:sub:`2` = line(resonate(Z:sub:`1`) ∩ Suc ∩ B)(meter=-+, feet=3)
⊢ Z:sub:`3` = line(resonate(Z:sub:`2`) ∩ Com  ∩ Wh ∩ A)(meter=-+, feet=4)
⊢ Z:sub:`4` = line(resonate(Z:sub:`3`) ∩ Ex ∩ B)(meter=-+, feet=3)

[λζ: ζ ∈ Z:sub:`1`].[λζ: ζ ∈ Z:sub:`2`].[λζ: ζ ∈ Z:sub:`3`].[λζ: ζ ∈ Z:sub:`4`]

.. topic:: Gemini Pro 2.5, 5/27/25

    | A stark constraint, yet balance finds its poise.
    | Then shadow falls, a grim duress.
    | All whitened hope contracts with jarring noise.
    | Life surges out, a new largesse.