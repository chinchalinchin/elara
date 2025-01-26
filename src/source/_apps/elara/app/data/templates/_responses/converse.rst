{%- set converse = response.get('converse') %}
RESPONSE
########

    {{ converse.get('response') | replace('\n', '\n    ') }}

MEMORY
######

    {{ converse.get('memory') | replace('\n', '\n    ') }}

FEEDBACK
########

    {{ converse.get('feedback')  | replace('\n', '\n    ')}}

NEXT PROMPT
###########

    {{ converse.get('next_prompt')  | replace('\n', '\n    ')}}