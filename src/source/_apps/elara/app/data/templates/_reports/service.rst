{%- set service = includes.get('service') %}
.. _service-report:

Service
#######

.. _service-response:

===============
Service Response
================

**Service**
    {{ service.name }}

**Status**
    {{ service.status }}

{% if service.body.get("url") %}
**Url**
    {{ service.body.url }}
{% endif %}