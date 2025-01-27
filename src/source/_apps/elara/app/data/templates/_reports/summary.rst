{%- set summary = includes.get('summary') %}
.. _{{ summary.get('directory').replace("/", "-").replace(".", "-")}}-directory-report:

{{ '-' * summary.get('directory') | length }}
{{ summary.get('directory') }}
{{ '-' * summary.get('directory') | length }}

.. _directory-structure:

Structure
---------

The following block shows the directory structure of the files given in the :ref:`directory-files` section.

.. code-block:: bash

{{ summary.get('tree') }}

.. _directory-files:

Files
-----

.. note::

    Some of the files may have been excluded from the summary to conserve space.
{% for file in summary.get('files') %}
.. _{{ file.name.split('.')[0].replace("/", "-").replace(".", "-") }}:
 
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
{% endfor %}