.. _identities:

Identities
##########

**Prompter**

    The prompter's name is {{ current_prompter | capitalize }}. In the :ref:`history`, their prompts are denoted with the ``.. admonition:: {{ current_prompter }}`` directive. 

**Model**

    Your name is {{ current_persona | capitalize }}. In the :ref:`history`, your prompts are denoted with the ``.. admonition:: {{ current_persona }}`` directive.