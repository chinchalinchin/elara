{%- macro interaction() -%}
  {%- if blocks.preamble.definitions and blocks.preamble.definitions.interaction -%}
    :ref:`interaction`
  {%- else -%}
    interaction
  {%- endif -%}
{%- endmacro -%}

{#- FUNCTIONS -#}
{%- if function == 'converse' -%}
{% include '_functions/converse.rst' %}
{%- endif -%}

{%- if function == 'formalize' -%}
{% include '_functions/formalize.rst' %}
{%- endif -%}

{%- if function == 'investigate' -%}
{% include '_functions/investigate.rst' %}
{%- endif -%}

{%- if function == 'review' -%}
{% include '_functions/review.rst' %}
{%- endif -%}

{%- if function == 'request' -%}
{% include '_functions/request.rst' %}
{%- endif -%}

{%- if function == 'summarize' -%}
{% include '_functions/summarize.rst' %}
{%- endif -%}

{#- REPORTS -#}
{%- if reports -%}

{%- if reports.get("models") -%}
{% include '_reports/model.rst' %}
{%- endif -%}

{%- if reports.get("service") -%}
{% include '_reports/service.rst' %}
{%- endif -%}
{%- endif -%}