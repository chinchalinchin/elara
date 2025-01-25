######
######
Output
######
######

{% if prompt is defined and prompt is not none %}
.. _prompt:

Prompt
######
######

{{ prompt }}
{% endif %}

{% if response is defined and response is not none %}
.. _response:

Response
########
########

{{ response }}
{% endif %}

{% if report is defined and report is not none %}
Report
######
######

{{ report }}
{% endif %}
