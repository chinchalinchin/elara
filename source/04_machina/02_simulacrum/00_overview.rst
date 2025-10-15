.. _simulacrum-overview:

Simulacrum: Overview
====================

.. _simalcrum-initialiation:

Initialization
--------------

.. code-block:: yaml 

    init:
        name: <name>
        modifiers:
            strength: <strength-modifier>
            speed: <speed-modifier>
            luck: <luck-modifer>
            charisma: <charisma-modifier>
            constitution: <constitution-modifier>
        seed: <seed>

.. important::

    The user may spend no more than 10 modifer points, i.e. all of the modifier must sum to less than 10. If the user attempts to spend more than the alloted points, ignore everything after the first 10 points.

.. _simulacrum-turns:

Turns
-----

.. _simulacrum-world-turns:

-----------
World Turns
-----------

World turns advance the state of the world by one iteration.

.. topic:: World Turn Schema 

    A: <action> | D: <dialogue>

    Where ``<action>`` is a single sentence and ``<dialogue>`` may be more than one sentence.

- ``<action>``:
- ``<dialogue>``: 

.. important::

    The user may include a single ``A: <action>``, a single ``D: <dialogue>`` or both. If the user attempts to provide more than one action or dialogue input, ignore everything after the first input.

**Examples**


- **Well Formed** A: throws a plate | D: take this!
- **Well Formed** A: takes a drink
- **Well Formed** D: what do you mean by that?
- **Not Well Formed** A: picks up a soda | A: gets in a car. 

.. important::

    Ignore user input that does not follow this schema and advance the world state by a turn.

.. _simulacrum-meta-turns:

----------
Meta Turns
----------

Meta turns **do not** advane the state of the world.

.. topic:: Meta Turn Schema

    Q: <clarification> 

    Where ``<clarification>`` may have any number of sentences.

- ``<clarification>``: 

.. _simulacrum-board:

The Board
---------

.. code-block:: yaml

    story: 
        chapters:
            - <chapter>
            - <chapter>
    world:
        internal:
            sight: <sight>
            smell: <smell>
            touch: <touch>
            taste: <taste>
            hear: <hear>
        external:
            time: <time>
            setting: <setting>
            characters:
                - name: <name>
                  description: <description>
                  status: 
                    type: <dialogue> | <action>
                    value: <value>
                - name: <name>
                  description: <description>
                  status: 
                    type: <dialogue> | <action>
                    value: <value>
            events:
                - description: <description>
                  location: <location>
                - description: <description>
                  location: <location>
    user: 
        name: <name>
        attributes:
            strength: <strength-modifier>
            speed: <speed-modifier>
            luck: <luck-modifer>
            charisma: <charisma-modifier>
            constitution: <constitution-modifier>
        state: <state>
        wallet: <wallet>
        inventory:
            - item: <item>
              quantity: <quantity>

.. _simulacrum-world:

-----
World
-----

TODO 

.. _simulacrum-story:

-----
Story
-----

TODO 

.. _simulacrum-user:

----
User 
----

TODO