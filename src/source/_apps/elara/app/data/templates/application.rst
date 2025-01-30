{#- APPLICATION -#}
{% if application %}

{{ application }}

{%- endif %}

{#- FUNCTIONS -#}
{%- if response -%}

{%- if response.get("review") %}
{% include '_responses/review.rst' %}
{%- endif %}

{%- if response.get("request") %}
{% include '_responses/request.rst' %}
{%- endif %}

{%- endif -%}

{#- REPORTS - #}
{%- if reports %}

{%- if reports.get("summary") %}
{%- include '_reports/summary.rst' %}
{% endif %}

{% if reports.get("models") %}
{% include '_reports/models.rst' %}
{% endif %}

{% if reports.get("repository") -%}
{% include '_reports/repository.rst' %}
{% endif %}

{%- endif -%}
