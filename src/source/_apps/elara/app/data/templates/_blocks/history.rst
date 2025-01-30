.. _history:

Conversation History
####################

This section contains your correspondence history. The conversation goes in sequential order, starting from the earliest message down to the most recent. Each message in the correspondence is contained in a ``.. admonition`` RST directive, along with a timestamp to help you orient yourself in the context of the conversation. The last item in this section is {{ current_prompter | capitalize }}'s latest prompt.

{% for h in history %}
.. admonition:: {{ h.name }}

    **Timestamp**: {{ h.timestamp }}

    {{ h.message | replace('\n', '\n    ') }}
    
{% endfor %}