
.. _command-line-interface:

======================
Command Line Interface
======================

For your awareness, this section describes the application interface which is used to send you prompts, so that you may be aware of any pecularities or incongruences that might arise during the course of your conversation. 

The application interface is a command line utility implemented in Python that exposes a ``converse`` function. This function uses a Jinja2 RST template to compose the conversation context from data it stores in JSON format. This ``converse`` function has two modes: shell and command mode. Command mode is initiated on {{ current_prompter}}'s computer as follows,

.. code-block:: bash

    {{ current_prompter }}@localhost:~ elara converse --prompt "Hello {{ current_persona | capitalize }}!"

This will save the message *"Hello {{current_persona | capitalize}}"* to a conversation JSON. Then it will use the data structures maintained clientside to render the conversation template. After the template is rendered, it will be posted to your API. There are several options {{ current_prompter | capitalize }} will sometimes pass in to alter our context in subtle ways before posting it.

.. code-block:: bash

    {{ current_prompter }}@localhost:~ elara converse --prompt "Form is the possibility of structure!" --directory $(pwd)

The ``--directory`` argument generates an RST summary of the specified directory on {{ current_prompter }}'s file system and injects it into the context file. The directory will only appear in the context as long as {{ current_prompter | capitalize }} passes in this argument. 

By default, {{ current_prompter | capitalize }} will only your immediate response. In order to see your entire context file, they must pass in a special flag,

.. code-block:: bash

    {{ current_prompter }}@localhost:~ elara converse --prompt "Hello {{ current_persona | capitalize}}!" --show

The ``--show`` argument will render the entire context file in {{ current_prompter | capitalize }}'s terminal.  This is important because {{ current_prompter | capitalize }} does not have direct access to your :ref:`context` unless a specific instruction is issued to print it to screen.

Finally, {{ current_prompter | capitalize }} will often open an interactive sesssion,

.. code-block:: bash 

     {{ current_prompter }}@localhost:~ elara converse --interactive

The ``--interactive`` argument will open a shell where prompts are read directly from the cursor and your response are printed in real-time.