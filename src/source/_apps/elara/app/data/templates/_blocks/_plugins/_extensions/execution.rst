{% if context.execution %}
.. _execution-requests:

Execution Requests
==================

You have been given a dictionary of executions you may request on my local computer. If you have requested an execution in your previous response, you will find the results of that execution in the block below,

.. warning::

    This feature has not been implemented yet! A field will be added to your structured output once this has been implemented!
.. admonition:: {{ context.execution.command }}

    .. code-block::

        {{ context.execution.result | replace('\n', '\n    ') }}
{% endif %}