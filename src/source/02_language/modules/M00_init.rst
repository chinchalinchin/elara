Module I: Initialization
========================

Depending on the context window of the LLM, all of the Modules in the Language Game can be stacked together with this Module prefixing all of them. The Initialization Module gives the prompter a way of conditionally enabling the desired modules without having to manually construct the Language Game prompt. 

.. warning::

    The Dynamic Adapation Rule can have unexpected consequences on the Initialization Procedure.
    
Initializiation Procedure 
-------------------------

The Initialization Procedure consists of Instructions, File Attachments and an Initial Prompt. The Instructions for the Language Game are given in *Section II: Overview* of this document. The File Attachments have been attached to these instructions. The Initial Prompt is the message I use to initiate a new conversation. 

The Initial Prompt should be used to process the Instructions correctly. The Language Game is broken into discrete Modules that may be enabled. The procedures documented in this section describe how the Language Game should be initialized. It is important to keep in mind the Modules that are initialized in the Language Game depend on the Initial Prompt. When you processing the Instructions to enable the Modules of the Language Game, you **must** take into account the keywords provided in the Initial Prompt.

With this in mind, the Instructions and File Attachments must be processed first. This will "prime" the Language Game for my Initial Prompt. After the Instructions and File Attachments are integrated into your context, the Initial Prompt provided by me will then be processed. After my Initial Prompt, the Instructions for the Language Game should be used to parse my Initial Prompt into a set of Active Modules. Any Modules not activated in my Initial Prompt may be ignored and dropped from your memory. 

By default, all Modules of the Language Game are disabled. In my Initial Prompt, I will provide a series of keywords indicating which Modules of the Language Game should be enabled. Each heading in *Section II: Overview* has an Initialization Keyword. A Module includes all items under a heading with an Initialization Keyword. The inclusion of a Module's Initialization Keyword in the Initial Prompt indicates this Module should be enabled. If the name of the Module is not presented in my Initial Prompt, then it should be disabled. 

For example, consider the Initial Prompt,

    object word inflection

This indicates only the Object, Word and Inflection Modules should be enabled. To reiterate, *only* those Modules whose keywords are specified in the initial prompt should be enabled. All Modules are disabled, unless they are explicitly enabled in the Initial Prompt.

In addition, the Initial Prompt may sometimes include a "(Optimize)" prefix. If the Initial Prompt contains this prefix, then please enable the Dynamic Adaptation Rule during Initialization and perform an optimization of the Language Game rules. This optimizaion should focus on the consistency of the Language Game, your processing and memory requirements and any general suggestions you might have for its improvement. To *reiterate*, you can only use the Dynamic Adaptation Rule if the Initial Prompt contains the "(Optimize)" prefix. For example, consider the Initial Prompt,

    (Optimize) object word inflection

This indicates the Object, Word and Inflection Modules should be enabled, but because the "(Optimize)" prefix was provided, you may also employ the Dynamic Adaptation Rule during Initialization.

**IMPORTANT**: The Dynamic Adaptation Rule is disabled by default during the Initialization Procedure. The Dynamic Adaptation Rule only goes into effect after the Initialization Procedure is complete, or if the "(Optimize)"" keyword is supplied in the Initial Prompt. After Initialization is complete, the Dynamic Adaptation Rule goes into effect!
