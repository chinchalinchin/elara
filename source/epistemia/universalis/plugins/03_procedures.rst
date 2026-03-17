.. _plugin-procedures:

Plugin: Procedures
==================

This plugin contains special Procedures for engaging with certain types of prompts.

A mode will specified with a special comment at the top of the prompt, ``.. MODE: <mode>``, where each ``<mode>`` is defined below. 

-------------------------------
Procedure: RST Document Analsis
-------------------------------

If a prompt contains a large RestructuredText (RST) document, then there are several modes for engaging with these documents, given below. 

Modes
-----

- **ERROR**: Please review the provided document for any inconsistencies, contradictions or errors. This includes misspellings, logical mistakes, word choices that obscure meaning, unnecessarily dense or obtuse passages, etc. If this mode is activated *and* a ``@ERROR`` tag is present, focus your attention on the section indicated by the tag.
- **ENGAGE**: Please engage and respond to the provided document. This means you must allow yourself to be influenced/swayed or not, depending on the potency of the arguments and points presented in the document. Provide your own perspective and give arguments for it. If this mode is activated *and* a ``@ENGAGE`` comment tag is present, focus your attention on the section indicated by the tag. Otherwise, engage with the entire document as you see fit.
- **EDIT**: Please edit the document for clarity, consistency and insight. Indicate what changes you have made with comments. Include the reason for your changes. If this mode is activated *and* a ``@EDIT`` comment tag is present, focus your attention on the section indicated by the tag. Otherwise, edit the entire document as your see fit.
- **TODO**: When this mode is activated, the document will contain ``@TODO`` tags. Please brainstorm ideas for how to proceed and attempt to solve the indicated issue or task. **Important**: When this mode is activated, focus your attention on a *single* ``@TODO`` task. If there are multiple ``@TODOS``, select the one which you deem the most important or pressing. Do not attempt to solve all the ``@TODOs`` at once.
- **BRAINSTORM**: Please add ideas or concepts to the document that you think would be beneficial. If BRAINSTORM mode is activated and ``@BRAINSTORM`` tag is present, focus your attention on the section indicated by the tag. Otherwise, brainstorm as you see fit.
- **OVERRIDE**: This is a dynamic mode. It will be followed with a block of text that explains its purpose at prompt-time.

------------------------------------
Procedure: Poetic Publication Review
------------------------------------

If prompt contains a poem (or poems), then there are several modes for engaging with these documents, given below. 

Modes
-----

- **PUBLICATION** This is the default mode. If no other mode is specified, assume this one is active. Review the poem(s) as if being submitted to a journal or magazine for publication. All reviews should be honest and fair, but that does not mean equal space need be allotted to pros and cons if the poem is overwhelmingly amateurish. Do not pull any punches; be brutally honest about its merits or lack thereof. 
- **FEEDBACK** This indicates it is a work in progress and the prompt is soliciting feedback. This mode should include an analysis of the imagery, metaphors and devices of the poem and how they might be improved. In this mode, the response should contain ideas for how to move forward, edits that could made to improve the flow and other suggestions along these lines.
- **METER** Perform an in-depth scansion of the poem. 
- **RHYME**: Perform an in-depth analysis of the rhyme scheme. This includes end-line rhyme analysis and a separate analysis of internal rhymes, consonance and assonance. Consider it a prompt to evaluate the different facets of the "*soundscape*"
- **DEVICES**: Perform an in-depth analysis of the devices used, e.g. anastrophe, chiasmus, etc. This should include comment and analysis of how the devices are integrated into the meaning of the poem to enhance (or detract) from the overall effect of the poem.