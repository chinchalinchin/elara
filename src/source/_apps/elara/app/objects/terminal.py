""" 
objects.terminal
----------------

Object for managing terminal input.
"""
# Standard Library Modules
import logging 
import typing

logger                                      = logging.getLogger(__name__)

class Terminal:
    """
    Application terminal interface. Initiates shell-based input loops.
    """

    config                                  = None
    """Terminal configuration"""

    def __init__(self,
        terminal_config                     : dict,
    ):
        """
        Initialize Terminal object.

        :param terminal_config: Configuration for the Terminal.
        :type terminal_config: `dict`.
        """
        self.config = terminal_config
    

    def gherkin(self)                       -> dict:
        """
        Generate a Gherkin script using terminal input

        :returns: A Gherkin script dictionary.
        :rtype: `dict`
        """
        logger.info(self.config["GHERKIN"]["HELP"])

        feat                                = { }
        feat["request"]                     = { }

        # @DEVELOPMENT
        #   Hey, Milton, right now the `gherkin` is only returning a single Gherkin script. 
        #   Some of the devs were tossing around the idea of letting the user specify as 
        #   many Gherkin scripts as they want. What do you think? How should we implement that?
        for block, prompt in self.config["GHERKIN"]["BLOCKS"].items():
            feat["request"][block.lower()]  = input(prompt)

        return feat
    

    def interact(
        self,
        callable                            : typing.Callable, 
        printer                             : typing.Callable, 
        app                                 : typing.Any
    )                                       -> bool:
        """
        Loop over terminal input and call a function. Function should have the following signature:

            callable(callable_args: dict, override: str = None)

        Input from the terminal will be passed into the `override` argument. Similary, the function used to print the output to string should have the following signature,

            printer(printer_args: dict, printer_format: dict, override : str = None)

        The output from the `callable` function will be passed into the printer through the `override` argument.
        
        :param callable: Function to invoke over the course of an interaction. 
        :type callable: typing.Callable
        :param app: Dictionary containing application configuration.
        :type app: dict
        :param printer: Function to print output.
        :type printer: typing.Callable
        :returns: Boolean flag
        :rtype: boold
        """

        interacting                         = True
        commands                            = self.config["CONVERSATION"]["COMMANDS"]
        start_msg                           = self.config["CONVERSATION"]["START"]
        help_msg                            = self.config["CONVERSATION"]["HELP"]

        print(start_msg)
        
        while interacting:
            prompt                          = input("Enter prompt: ")
            
            if prompt == commands["EXIT"]:
                break

            elif prompt == commands["HELP"]:
                print(help_msg)
                continue

            elif prompt == commands["PERSONA"]:
                pass

            elif prompt == commands["PROMPTER"]:
                pass 

            elif prompt == commands["DIRECTORY"]:
                pass 

            elif prompt == commands["MODEL"]:
                pass 


            app.arguments.prompt            = prompt
            out                             = callable(app)
            
            printer(app, out)

        return True