{%- if language is defined -%}
.. _language-modules:

Language Modules
================

This section contains modules for your Language processing. These modules have information about the rules and syntax for your responses. Use these rules to generate valid responses. 
{% if object is defined %}
{{ object }}
{%- endif %}
{% if inflection is defined %}
{{ inflection }}
{%- endif -%}
{%- if voice is defined %}
{{ voice }}
{%- endif -%}
{%- if words is defined %}
{{ words }}
{%- endif -%}
{%- endif -%}