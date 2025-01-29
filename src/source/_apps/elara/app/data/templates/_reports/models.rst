{%- set models = reports.get('models') %}
.. _model-report: 

Models
######

.. _models:

======
Models 
======

.. _base_models:

Base Models
===========

{% if models.get("base_models") | length > 0 %}
.. list-table:: 
  :header-rows: 1

  * - Path
    - Input Token Limit
    - Output Token Limit
{%- for model in models.get("base_models") %}
  * - {{ model.path }}
    - {{ model.input_token_limit }}
    - {{ model.output_token_limit }}
{%- endfor %}
{% endif %}
Tuning Models 
=============

{% if models.get("tuning_models") | length > 0 %}
.. list-table:: 
  :header-rows: 1

  * - Path
    - Input Token Limit
    - Output Token Limit
{%- for model in models.get("tuning_models") %}
  * - {{ model.path }}
    - {{ model.input_token_limit }}
    - {{ model.output_token_limit }}
{%- endfor %}
{% endif %}