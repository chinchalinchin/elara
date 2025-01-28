.. _application:

###########
Application
###########
###########
{% if prompt %}
.. _prompt:

Prompt
######
######

{{ prompt }}
{%- endif %}
{%- if response -%}
.. _response:

Response
########
########

{% if response.get("converse") %}
{% include '_responses/converse.rst' %}
{% endif %}
{% if response.get("analyze") %}
{% include '_responses/analyze.rst' %}
{% endif %}
{% if response.get("review") %}
{% include '_responses/review.rst' %}
{% endif %}
{% if response.get("request") %}
{% include '_responses/request.rst' %}
{% endif -%}
{%- endif -%}
{% if includes %}
.. _reports:

Reports
#######
#######
{% if includes.get("summary") %}
.. _summary-report:

Summary
#######
{% include '_reports/summary.rst' %}
{% endif %}
{% if includes.get("models") %}
{% include '_reports/models.rst' %}
{% endif %}
{%- if includes.get("repository") -%}
{% include '_reports/repository.rst' %}
{% endif %}
{% endif %}
