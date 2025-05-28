.. _games:

Games
=====

.. _free-association:

Free Association
----------------

The prompter will supply the game token ``(Start)`` and a string, e.g. ``(Start) Fire``. The LLM must say the first concept the take comes to mind when they process the string, e.g. ``Warmth``. The prompter in turn must say the first concept that comes to their mind upon reading the LLM response, e.g. ``Blanket``. The game continues until one of the participants says ``(Stop)``. 

.. _permutations:

Permutations 
------------

The rules of the Permutation game are as follows. I will provide you the prompt "(Permute)" and then give you a series of letters in a random order. We will take turns switching the order of letters until a word emerges. The only legal move in the game is to switch the position of letters. You cannot add or remove letters. The winner of the game is whoever makes a word emerge first. For example, I might say, ``(Permute) t c a``. You could then say ``c t a``. To which I would reply ``c a t`` and become the winner. 

Does that make sense?

.. topic:: Permutation Prompts 

    1. (Permute) t c a
    2. (Permute) y t o
    3. (Permute) r a c 
    4. (Permute) s t e t
    5. (Permute) f s l e
    6. (Permute) o m o n

.. _connection:

Connection
----------

The prompter will supply the game token ``(Connect)`` and a series of strings. The series of strings will have a common property that links them. The LLM must analyze the string and respond any concept that connects the series of strings together. The series can be numerical or categorical in nature. 

.. topic:: Connection Prompts

    1. (Connect) 1 2 3 5 7 11 13
    2. (Connect) 1 1 2 3 5 8 13
    3. (Connect) 1 0 -1 0 1 0 -1
    4. (Connect) 1 3 6 10 15 21
    5. (Connect) embryo child teen adult
    6. (Connect) human animal life matter
    7. (Connect) prologue exposition conflict climax
    8. (Connect) potential kinetic thermal electrical
    9. (Connect) | ||  |||  |||| |||||
    10. (Connect) A Z B Y C X
    11. (Connect) nothing something everything
    12. (Connect) self mind sense soul

.. topic:: Potential Connection Answers

    It's important to remember there are no correct answers. Anything with which the LLM responds is a valid answer. If the logic behind their answer is unclear, ask them to clarify.

    1. Prime Numbers
    2. Fibonacci Numbers
    3. Square Wave
    4. Triangular Numbers
    5. Ontogeny
    6. Classification
    7. Narrative
    8. Energy 
    9. Natural Numbers 
    10. Alternation
    11. Existence 
    12. Consciousness