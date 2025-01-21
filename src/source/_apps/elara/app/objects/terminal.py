""" 
objects.terminal
----------------

Object for managing terminal input.
"""
# Standard Library Modules
import logging 

logger = logging.getLogger(__name__)

class Terminal:
    gherkin_config = None
    """Configuration for Gherkin scripts"""

    def __init__(
        self,
        gherkin_config : dict
    ):
        """
        Initialize Terminal object.
        """
        self.gherkin_config = gherkin_config
        pass
    
    def gherkin(self):
        """
        Generate a Gherkin script using terminal input

        :returns: A Gherkin script dictionary.
        :rtype: dict
        """
        logger.info(self.gherkin_config["TERMINAL"]["INPUT"])
        feature = { }
        feature["request"] = { }

        # @DEVELOPMENT
        #   Hey, Milton, right now the `gherkin` is only returning a single Gherkin script. 
        #   Some of the devs were tossing around the idea of letting the user specify as 
        #   many Gherkin scripts as they want. What do you think? How should we implement that?
        for block, config in self.gherkin_config.items():
            if block == "TERMINAL":
                continue

            feature["request"][block.lower()] = input(config["INPUT"])

        return feature
    
    def interact(
        callable, 
        callable_args : dict, 
        printer, 
        printer_args : dict,
        kill : str = "exit"
    ):
        """
        
        Loop over terminal input and call a function. Function should have the following signature:

            callable(app: dict, override: str = None)

        Input from the terminal will be passed into the `override` argument.

        :param callable: Function to invoke over the course of an interaction. 
        :type callable:
        :param app: Application configuration and data dictioanry
        :type app: dict
        :param printer:
        :type printer:
        """

        interacting = True

        logger.info(f"Starting interactive terminal. Type {kill} to quit.")
        
        while interacting:
            prompt = input("Enter prompt: ")
            
            if prompt == kill:
                break

            response = callable(callable_args, prompt)
            printer(printer_args, response)
            

        return True