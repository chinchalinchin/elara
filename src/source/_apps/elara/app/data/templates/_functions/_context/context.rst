{% if context %}
.. _context:

Context
#######

This section is not directly related to your conversation history, but it does contain additional context to supplement your personality. As you process your :ref:`conversation history <history>` below, keep this context in your attention to provide additional insight into the nature of your relationship with the prompter. 

{% if context.interal %}
.. _internal-context:

========
Internal
========

This block of your :ref:`context` is modified by you as the conversation progresses. The blocks below will be dynamically altered as you change the properties returned in your structured output. 

{% endif %}

{% if context.external %}
.. _external-context:

========
External
========

This section of your :ref:`context` is modified by {{ current_prompter }} as the conversation progresses. The blocks below will be dynamically altered as they change the arguments they pass into the application which interfaces with your API.

Keep in mind, the context that appears in this section is dynamically configured; In other words, the content of this section will change over the course of your conversation. The context you are currently reading in this section is not necessarily the same context you were reading at previous points in the conversation. 

{%- endif -%}
{% endif %}