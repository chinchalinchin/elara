{%- set repository = reports.get('repository') %}
.. _repository-report:

Repository
##########

.. _respository-responses:

====================
Repository Responses
====================
{% for r in repository %}
.. admonition:: Response #{{ loop.index }}

    **Service**
        {{ r.service.name }}

    **Status**
        {{ r.service.status }}

    **Url**
        {{ r.service.body.url }}
{% endfor %}