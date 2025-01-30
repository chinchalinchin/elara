{% if context.quotes|length > 0  %}
.. _quotations:

Quotations 
==========

The following section contains quotations for you to consider.
    {% for q in context.quotes %}
    {{ q.quote }}
    -- *{{ q.source }}*, {{ q.quoter }} 
    {% endfor %}
{% endif %}