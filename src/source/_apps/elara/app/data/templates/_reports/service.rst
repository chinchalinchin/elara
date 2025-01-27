{%- set service = includes.get('service') %}

Service Response
----------------

**Service**
    {{ service.name }}

**Status**
    {{ service.status }}

{{ service.body }}