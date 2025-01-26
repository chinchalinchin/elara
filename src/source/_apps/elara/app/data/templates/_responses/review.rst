{%- set review = response.get('review') %}

.. important::

    SCORE: {{ review.get('score') }}

Files 
#####

{% for f in files %}

{{ '=' * f.get('filepath') | length }}
{{ f.filepath }}
{{ '=' * f.get('filepath') | length }}

General Comments
----------------

{{ f.get("general_comments")

{% if f.get('potential_bugs') %}
Potential Bugs
--------------

{{ f.get('potential_bugs') }}
{% endif %}
{% if f.get('potential_optimizations') %}
Potential Optimizations
-----------------------

{{ f.get('potential_optimizations') }}
{% endif %}

{% if f.get('amended_code') %}
Amended Code
------------

{{ f.get('amended_code') }}
{% endif %}