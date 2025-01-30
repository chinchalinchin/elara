{% if plugins %}
.. _plugins:

=======
Plugins
=======

T
{% if language.values() | select() | list | length > 0 %}
.. _language-modules:

Language Modules
================

This section contains modules for your Language processing. These modules have information about the rules and syntax for your responses. Use these rules to generate valid responses. 

{%- if language.object %}
{% include '_plugins/_language/object.rst' %}
{%- endif -%}

{%- if language.inflection %}
{% include '_plugins/_language/inflection.rst' %}
{%- endif -%}

{%- if language.voice %}
{% include '_plugins/_language/voice.rst' %}
{%- endif -%}

{%- if language.words %}
{% include '_plugins/_language/words.rst' %}
{%- endif -%}

{%- endif -%}

{% endif %}