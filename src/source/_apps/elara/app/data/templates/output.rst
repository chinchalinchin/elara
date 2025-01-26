.. _output:

######
Output
######
######
{% if prompt -%}
.. _prompt:

Prompt
######
######

{{ prompt }}
{%- endif -%}
{% if response -%}
.. _response:

Response
########
########

{{ response }}
{%- endif -%}
{% if includes -%}
.. _reports:

Reports
#######
#######

{%- if includes.get('summary') -%}
.. _summary-report:
Summary
#######
{% include '_meta/summary.rst' %}
{% endif %}
{% if includes.get('models') %}
.. _model-report: 

Models
######
{% include '_meta/models.rst' %}
{% endif %}
{% endif %}
