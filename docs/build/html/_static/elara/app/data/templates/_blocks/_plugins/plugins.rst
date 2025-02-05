{%- if plugins -%}
.. _plugins:

Plugins
#######

This section describes additional features that should be implemented in your response. These plugins should alter various aspects of your reply. 

{% if plugins.language.values() | select() | list | length > 0 -%}
.. _language-modules:

================
Language Modules
================

This section contains modules for your language processing. These modules have information about the rules and syntax for your written responses. Use these rules to generate valid responses. 

{% if plugins.language.object -%}
{% include '_blocks/_plugins/_language/object.rst' %}
{%- endif %}

{%- if plugins.language.inflection -%}
{% include '_blocks/_plugins/_language/inflection.rst' %}
{%- endif %}

{% if plugins.language.voice -%}
{% include '_blocks/_plugins/_language/voice.rst' %}
{%- endif %}

{% if plugins.language.words -%}
{% include '_blocks/_plugins/_language/words.rst' %}
{%- endif -%}
{%- endif -%}
{%- endif -%}