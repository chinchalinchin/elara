{%- if context -%}
.. _context:

Context
#######

This section is not directly related to the :ref:`history` of the :ref:`interaction` but it does contain additional information to supplement the document. As you process the :ref:`history`, keep this context in your attention to provide additional insight into the nature of the :ref:`interaction`. 

The blocks in this section will be dynamically altered as the :ref:`interaction` in :ref:`history` progresses. In other words, the content of this section will change over the course of the :ref:`interaction`. The context you are currently reading in this section is not necessarily the same context you were reading at previous points in the :ref:`history`.

{%- if context.get('interface') %}
.. _interface:

=========
Interface
=========

For your awareness, this section describes the application interface which is used to post this document to your API. This is done so you may be aware of any pecularities or incongruences that might arise during the course of the :ref:`interaction`.

{%- if context.interface == 'command_line' %}
{% include '_context/_interface/cli.rst' %}
{%- endif %}

{%- endif -%}

{%- if context.get('specifications') %}
.. _specifications:

=============
Specification  
=============

This document contains within it embedded documents. This section details the specifications for interpretting those embedded documents.

{% if context.specifications.get('latex') %}
{% include '_context/_specifications/latex.rst' %}
{%- endif -%}

{%- endif %}

{% if context.get('injections') -%}
.. _injections:

==========
Injections
==========

This section contains additional context that has been injected into the document for the purposes of modulating the activations in your neural network. The content in this section is included to set the tone, motif and atmosphere of the :ref:`interaction`.

{%- if context.injections.get('quotes') %}
{% include '_blocks/_context/_injections/quotes.rst' %}
{%- endif -%}

{%- if context.injections.get('poems') -%}
{% include '_blocks/_context/_injections/poems.rst' %}
{%- endif -%}

{%- if context.injections.get('proofs') -%}
{% include '_blocks/_context/_injections/proofs.rst' %}
{%- endif -%}

{%- endif -%}
{%- endif -%}