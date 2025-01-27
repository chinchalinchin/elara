{%- set review = response.get('review') %}
.. important::

    SCORE: {{ review.get('score') }}

Assessment
##########

{{ review.get('overall') }}

Files 
#####
{% for f in review.get('files') %}
{{ '=' * f.get('path') | length }}
{{ f.path }}
{{ '=' * f.get('path') | length }}

General Comments
----------------

{{ f.get("comments") }}
{%- if f.get('bugs') %}
Bugs
----

{{ f.get('bugs') }}
{%- endif %}
{% if f.get('amendments') %}
Amended Code
------------

{{ f.get('amendments') }}
{%- endif %}
{% endfor %}