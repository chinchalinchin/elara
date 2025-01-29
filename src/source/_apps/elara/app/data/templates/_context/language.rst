{% if language.values() | select() | list | length > 0 %}
.. _language-modules:

================
Language Modules
================

This section contains modules for your Language processing. These modules have information about the rules and syntax for your responses. Use these rules to generate valid responses. 
{% if language.get('object') %}
{% include '_context/_language/object.rst' %}
{%- endif %}
{%- if language.get('inflection') %}
{% include '_context/_language/inflection.rst' %}
{%- endif -%}
{%- if language.get('voice') %}
{% include '_context/_language/voice.rst' %}
{%- endif -%}
{%- if language.get('words') %}
{% include '_context/_language/words.rst' %}
{%- endif -%}
{%- endif -%}