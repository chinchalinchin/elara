.. _history:

History
=======

The conversation goes in sequential order, starting from the earliest message down to the most recent. The last item in this section is my latest prompt.

{% for msg in history %}
.. admonition:: {{ msg.name }}

    **Timestamp**: {{ msg.timestamp }}

    {{ msg.text }}

{% endfor %}