{{ directory }}
{{ '-' * directory | length }}

Structure
^^^^^^^^^

.. code-block:: bash

    {{ tree | replace('\n', '\n    ') }}

{# Template files #}
{%- for file in files -%}
{# File title #}

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