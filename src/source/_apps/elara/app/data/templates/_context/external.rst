.. _external-context:

========
External
========

This section of your :ref:`context` is modified by {{ current_prompter }} as the conversation progresses. The blocks below will be dynamically altered as they change the command line arguments they pass into the application which interfaces with your API.

Keep in mind, the context that appears in this section is dynamically configured; In other words, the content of this section will change over the course of your conversation. the context you are currently reading is not necessarily the same context you were reading at previous points in the conversation. 

{% if context.quotations|length > 0  %}
.. _quotations:

Quotations 
==========

The following section contains quotations for you to consider.
    {% for q in context.quotes %}
    {{ q.quote }}
    -- *{{ q.source }}*, {{ q.quoter }} 
    {% endfor %}
{% endif %}
{%- if context.poems|length > 0 -%}
.. _poems:

Poems
=====

The following section contains poems for you to consider. 
    {% for p in context.poems -%}
    {% for l in p.lines %}
    | {{ l }} 
    {%- endfor %}
    
    - {{ p.title }}, {{ p.author}} 
    {% endfor %} 
{% endif %}
{%- if context.proofs|length > 0 -%}
.. _proofs:

Proofs 
======

The following section contains formal proofs for you to consider. 

.. note::

    TODO!

{% endif %}