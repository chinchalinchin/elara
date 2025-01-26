{%- set summary = includes.get('summary') %}
{{ '-' * summary.get('directory') | length }}
{{ summary.get('directory') }}
{{ '-' * summary.get('directory') | length }}

.. _directory-structure:

Structure
---------

.. code-block:: bash

    {{ summary.get('tree') }}

{# Template files #}
{%- for file in summary.get('files') -%}
.. _{{ file.name | split(',') | first }}:
 
{{ file.name }}
{{ '^' * file.name | length }}

{# File directive #}
{%- if file.type == 'code' -%}
.. code-block:: {{ file.lang }}

    {{ file.data | replace('\n', '\n    ') }}
{%- elif file.type == 'raw' -%}
.. raw:: {% if file.lang is defined %}{{ file.lang }}{% endif %}

    {{ file.data | replace('\n', '\n    ') }}
{%- endif -%}
{%- endfor -%}