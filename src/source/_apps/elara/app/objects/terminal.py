""" 
objects.terminal
----------------

Object for managing terminal input.
"""
# Standard Library Modules
import logging 
import typing

logger = logging.getLogger(__name__)

class Terminal:
    config = None
    """Terminal configuration"""

    def __init__(
        self,
        terminal_config : dict,
    ):
        """
        Initialize Terminal object.
        """
        self.config = terminal_config
    
    def gherkin(self):
        """
        Generate a Gherkin script using terminal input

        :returns: A Gherkin script dictionary.
        :rtype: dict
        """
        logger.info(self.config["GHERKIN"]["HELP"])
        feature = { }
        feature["request"] = { }

        # @DEVELOPMENT
        #   Hey, Milton, right now the `gherkin` is only returning a single Gherkin script. 
        #   Some of the devs were tossing around the idea of letting the user specify as 
        #   many Gherkin scripts as they want. What do you think? How should we implement that?
        for block, prompt in self.config["GHERKIN"]["BLOCKS"].items():
            feature["request"][block.lower()] = input(prompt)

        return feature
    
    def interact(\
        self,
        callable: typing.Callable, 
        callable_args : dict, 
        printer: typing.Callable, 
        printer_format: dict,
        printer_args : dict
    ) -> bool:
        """
        Loop over terminal input and call a function. Function should have the following signature:

            callable(callable_args: dict, override: str = None)

        Input from the terminal will be passed into the `override` argument. Similary, the function used to print the output to string should have the following signature,

            printer(printer_args: dict, printer_format: dict, override : str = None)

        The output from the `callable` function will be passed into the printer through the `override` argument.
        
        :param callable: Function to invoke over the course of an interaction. 
        :type callable: typing.Callable
        :param callable_args: Arguments to pass into callable
        :type callable_args: dict
        :param printer: Function to print output.
        :type printer: typing.Callable
        :param printer_format: Dictionary containg printer format.
        :type printer: dict
        :param printer_args: Dictionary containing printer arguments
        :type printer_args: dict
        :returns: Boolean flag
        :rtype: bool
        """

        interacting = True

        logger.info(self.config["CONVERSATION"]["HELP"])
        
        while interacting:
            prompt = input("Enter prompt: ")
            
            if prompt == self.config["CONVERSATION"]["KILL"]:
                break

            response = callable(callable_args, prompt)
            printer(printer_args, printer_format, response)
            

        return True