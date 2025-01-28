{%- set converse = response.get('converse') %}
RESPONSE
########

    {{ converse.get('response') | replace('\n', '\n    ') }}
{% if converse.get('memory') %}
MEMORY
######

    {{ converse.get('memory') | replace('\n', '\n    ') }}
{% endif %}