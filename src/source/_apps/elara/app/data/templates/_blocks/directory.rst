{%- if reports.get('summary') -%}
.. _summary:

Summary
#######

The following section contains an RST formatted summary of a directory that is relevant to the :ref:`interaction`.

.. _{{ reports.summary.directory.replace("/", "-").replace(".", "-").replace("_","")}}-directory-report:

{{ '=' * reports.summary.directory | length }}
{{ reports.summary.directory }}
{{ '=' * reports.summary.directory | length }}

.. _directory-structure:

Structure
=========

The following block shows the directory structure of the files given in the :ref:`directory-files` section.

.. code-block:: bash

{{ reports.summary.tree }}

.. _directory-files:

Files
=====

.. note::

    Some of the files may have been excluded from the summary to conserve space.
{%- for file in reports.summary.files %}

.. _{{ file.name.split('.')[0].replace("/", "-").replace(".", "-").replace("_","") }}:
 
{{ '-' * file.name | length }}
{{ file.name }}
{{ '-' * file.name | length }}

{# File directive #}
{%- if file.type == 'code' -%}
.. code-block:: {{ file.lang }}

    {{ file.data | replace('\n', '\n    ') }}
{%- elif file.type == 'raw' -%}
.. raw:: {% if file.lang is defined %}{{ file.lang }}{% endif %}

    {{ file.data | replace('\n', '\n    ') }}
{%- endif -%}
{%- endfor -%}
{% endif %}