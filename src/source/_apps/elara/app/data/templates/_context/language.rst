{%- if language is defined -%}
{% set any_true = false %}
{% for key, value in language.items() %}
  {% if value %}
    {% set any_true = true %}
    {% break %}
  {% endif %}
{% endfor %}
{% if any_true %}
.. _language-modules:

================
Language Modules
================

This section contains modules for your Language processing. These modules have information about the rules and syntax for your responses. Use these rules to generate valid responses. 
{% if language.get('object') %}
{% include '_language/object.rst' %}
{%- endif %}
{%- if language.get('inflection') %}
{% include '_language/inflection.rst' %}
{%- endif -%}
{%- if language.get('voice') %}
{% include '_language/voice.rst' %}
{%- endif -%}
{%- if language.get('words') %}
{% include '_language/words.rst' %}
{%- endif -%}
{%- endif -%}
{%- endif -%}