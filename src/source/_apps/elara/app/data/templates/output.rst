######
######
Output
######
######

{% if prompt is defined and prompt is not None %}
{{ prompt }}
{% endif %}

{% if response is defined and response is not None%}
{{ response }}
{% endif %}

{% if summary is defined and summary is not None%}
{{ summary }}
{% endif %}
