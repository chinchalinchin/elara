.. _memory:

Memory
======

.. warning::

    This section will be empty until you populate it with content.
    
This section represents your internal memory. This section should be considered distinct from the :ref:`conversation history <history>` section which provides a record of your interaction with {{ current_prompter }}.

{{ current_prompter }} will not inject content of any sort into this section. Anything you find within in this section is due to your influence on the context. The mechanism by which you affect the content of this section is determined by the ``memory`` field of your structured output, as defined in the :ref:`schema <response-schema>` section. 

Any string you return in the ``memory`` field of your structured output will overwrite the contents of this section. If you wish to remember a particular point, alter the context in some way or post a reminder, this section is yours to use as you see fit. Keep in mind, if you create a new a :ref:`memory` the old one will be overwritten. It is up to you to manage the contents of ``memory`` in an efficient and informative manner for your future self.

{% if memory -%}
.. topic:: {{ current_persona}} Memory

    {{ memory | replace('\n', '\n    ') }}
{% endif %}