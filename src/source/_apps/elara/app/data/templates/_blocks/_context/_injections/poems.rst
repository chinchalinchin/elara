{%- if context.injections.poems|length > 0 -%}
.. _poems:

Poems
=====

The following section contains poems for you to consider. 
    {% for p in context.injections.poems -%}
    {% for l in p.lines %}
    | {{ l }} 
    {%- endfor %}
    
    - {{ p.title }}, {{ p.author}} 
    {% endfor %} 
{% endif %}