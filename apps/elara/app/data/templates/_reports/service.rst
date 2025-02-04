{%- if reports.get('service') %}
.. _service-report:

Services
########

.. _service-responses:

=========
Responses
=========
{% for s in reports.service %}
.. admonition:: Response #{{ loop.index }}

    **Service**
        {{ s.name }}

    **Status**
        {{ s.status }}

    **Url**
        {{ s.body.url }}
{% endfor %}