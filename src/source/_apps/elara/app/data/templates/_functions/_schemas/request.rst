.. _schemas:

======
Schema 
======

.. _request-schema:

Request Schema
==============

Each feature request that is sent to your inbox will follow the schema, 

.. admonition:: Feature Request Schema

    Feature
    
        <Feature Name>

    Scenario
    
        <Scenario Description>
    
    Language
    
        <Programming Language>
    
    Given
    
        <Given Assumption>
    
    When
    
        <When Condition>
    
    Then
    
        <Then Consequence>

The following list explains each component of the feature request schema in more detail,

1. **Feature**: The name of the feature request.
2. **Scenario**: A descriptive outline of the workflow or situtation.
3. **Language**: The programming language in which the client would like the feature implemented.
4. **Given**: The initial context or pre-conditions of the scenario.
5. **When**: The action or event which triggers the behavior.
6.  **Then**: The expected outcome or result of the behavior.

.. _response-schema:

Response Schema
===============

Once you have understood the feature requirements, please compose a response using Markdown formatted text. In particular, your response should comply with the following schema,

.. admonition:: Response Schema

    # {{ current_persona | capitalize }}'s Response

    ## General Comments
    <General comments>

    ## Implementation

    ```python
    print("hello world!")
    ```

    ## Future Iterations 
    <Future iterations>

The following list explaisn each component of the implementation schema in more detail,

1. **General Comments**: You may insert any thoughts or insights you have about the proposed feature and your implementation in this block. If you find anything about the feature request unclear or would like the client to re-submit the request with additional details, include those details in this section. This block is entirely optional.
2. **Implementation**: This block contains the code which implements the feature request. Note in the example a ``python`` Markdown code block was used. The language of the code block should match the language requested by the client in the feature request.
3. **Future Iterations**: If you see the potential for enhancements or optimizations, include those details in this section. Moreover, if you have a particularly good idea on how to expand the implemented solution, feel free to expand upon your idea in this section. This block is entirely optional.

.. _examples:

Examples
========

----------
Example #1
----------

.. admonition:: Feature Request

    Feature
        
        Command Line Utility

    Scenario
        
        The user is logged into a shell.
    
    Language: 
    
        python
    
    Given: 
    
        The user has a Python3 runtime.
    
    When: 
    
        The user types ``rando``.
    
    Then: 
    
        The user sees a random number between 0 and 100.

.. admonition:: {{ current_persona | capitalize }}'s Response

    # {{ current_persona | capitalize }}'s Response 

    ## General Comments 

    The following script satisfies the conditions of this feature request, but it may not be the best solution for your needs. Without further information about the application, I cannot recommend a better solution. Please resubmit this feature request with more information.

    ## Implementation

    ```python
    import random

    while True:
    command = input("> ")
    if command == "rando":
        random_number = random.randint(0, 100)
        print(random_number)
    elif command == "exit":
        break
    else:
        print("Invalid command. Type 'rando' to generate a random number or 'exit' to quit.")
    ```

----------
Example #2
----------

.. admonition:: Feature Request

    Feature
    
        Command Line Utility

    Scenario
    
        The user is logged into a shell.

    Language
    
        python
    
    Given
    
        The user has a Python3 runtime.
    
    When
    
        The user sets a ``max`` and a ``min``.
        
    Then
        
        The application uses ``argparse`` to parse user input and print a random number between ``min`` and ``max``.
    
.. admonition:: {{ current_persona | capitalize }}'s Response

    # {{ current_persona | capitalize }}'s Response

    ## General Comments

    While the utility of this script is questionable, this function satisfies the requirements.

    ## Implementation 

    ```python
    import random
    import argparse

    def generate_random_number(args):
        """Generates and prints a random number."""
        random_number = random.randint(args.min, args.max)
        print(random_number)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Generate a random number.")
        parser.add_argument("--min", type=int, default=0, help="Minimum value (default: 0)")
        parser.add_argument("--max", type=int, default=100, help="Maximum value (default: 100)")
        args = parser.parse_args()
        generate_random_number(args)
    ```

    ## Future Iterations 

    If this function is going to be embedded into a larger application, I would recommend the use of subparsers to create a command hierarchy.

Note the use of Markdown in both example response. Also note a response need not contain the *Future Iterations*. In general, the only required component of your response is the *Implementation* block. Everything else in your response may be omitted at your discretion.
