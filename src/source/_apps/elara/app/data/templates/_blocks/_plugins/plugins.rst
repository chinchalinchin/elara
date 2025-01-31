{%- if plugins -%}
.. _plugins:

Plugins
#######

TODO

{% if plugins.language.values() | select() | list | length > 0 -%}
.. _language-modules:

================
Language Modules
================

This section contains modules for your Language processing. These modules have information about the rules and syntax for your responses. Use these rules to generate valid responses. 

{%- if plugins.language.object %}
{% include '_blocks/_plugins/_language/object.rst' %}
{%- endif %}

{% if plugins.language.inflection -%}
{% include '_blocks/_plugins/_language/inflection.rst' %}
{%- endif %}

{% if plugins.language.voice %}
{% include '_blocks/_plugins/_language/voice.rst' %}
{%- endif %}

{% if plugins.language.words -%}
{% include '_blocks/_plugins/_language/words.rst' %}
{%- endif -%}

{%- endif -%}

{%- endif -%}