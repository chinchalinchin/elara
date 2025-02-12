.. _preamble:

Preamble
########

The following document has been designed to provide you a detailed contextual summary of your {{ interaction() }} up to this point. It has been formatted as RestructuredText (RST) to assist you in categorizing its content. All sections are annotated with RST roles, directives and anchors. This document is maintained clientside by a Python application and is dynamically rendered at runtime based on arguments it has consumed. Once the document is rendered, it is posted to the Gemini API. 

.. important::

    You are not required to format your response in RST. All RST formatting happens clientside. The RST formatting is purely to markup the prompt for your clarity and understanding.

{% if blocks.preamble.definitions.values() | select() | list | length > 0 -%}
.. _definitions:

===========
Definitions
===========

This section contains definitions that will be referenced through the document. 

{% if blocks.preamble.definitions.interaction -%}
.. _interaction:

**Interaction**
    
    When this term is used, it is meant to denote the real-world exchange that is occuring between you and the entity responsible for posting this document to your API. 
{%- endif %}
{%- endif %}
{%- if blocks.preamble.identities %}
.. _identities:

==========
Identities
==========

.. _prompter:

**Prompter**

    The prompter's name is {{ current_prompter | capitalize }}. In the :ref:`history`, their prompts are denoted with the ``.. admonition:: {{ current_prompter }}`` directive. 

.. _model:

**Model**

    Your name is {{ current_persona | capitalize }}. In the :ref:`history`, your prompts are denoted with the ``.. admonition:: {{ current_persona }}`` directive.
{%- endif -%}