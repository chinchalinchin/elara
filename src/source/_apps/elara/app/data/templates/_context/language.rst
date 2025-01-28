{%- if language is defined -%}
.. _language-modules:

================
Language Modules
================

This section contains modules for your Language processing. These modules have information about the rules and syntax for your responses. Use these rules to generate valid responses. 
{% if object is defined %}
{% include '_language/object.rst' %}
{%- endif %}
{%- if inflection is defined %}
{% include '_language/inflection.rst' %}
{%- endif -%}
{%- if voice is defined %}
{% include '_language/voice.rst' %}
{%- endif -%}
{%- if words is defined %}
{% include '_language/words.rst' %}
{%- endif -%}
{%- endif -%}