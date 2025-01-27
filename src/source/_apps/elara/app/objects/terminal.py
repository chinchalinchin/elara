""" 
objects.terminal
----------------

Object for managing terminal input.
"""
# Standard Library Modules
import logging 
import typing
import re

logger                                      = logging.getLogger(__name__)

class Terminal:
    """
    Application terminal interface for Gemini API. Initiates shell-based input loops.
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
    

    @staticmethod
    def _extract(
        string                              : str
    )                                       -> tuple:
        """
        Extract function word and argument from a terminal command.

        :param string: String against which to match.
        :type string: `str`
        :returns: Ordered pair of (function, argument)
        :rtype: `tuple`
        """

        # Matches "word(word)"
        pattern = r"^([a-zA-Z]+)\(([a-zA-Z]+)\)$" 

        match = re.match(pattern, string)
        if match:
            return match.group(1), match.group(2)
        
        return None, None
        
    
    def gherkin(self)                       -> dict:
        """
        Generate a Gherkin script using terminal input

        :returns: A Gherkin script dictionary.
        :rtype: `dict`
        """
        logger.info(self.config["GHERKIN"]["HELP"])

        feat                                = { }
        feat["request"]                     = { }

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

            callable(application: app.App)

        Similary, the function used to print the output to string should have the following signature,

            printer(application: app.App, output: app.Output)

        The output from the `callable` function will be passed into the printer along with the application..
        
        :param callable: Function to invoke over the course of an interaction. 
        :type callable: `typing.Callable`
        :param app: Application object
        :type app: `app.App`
        :param printer: Function to print output.
        :type printer: `typing.Callable`
        :returns: Boolean flag
        :rtype: `bool`
        """

        interacting                         = True
        commands                            = self.config["CONVERSE"]["COMMANDS"]
        functions                           = self.config["CONVERSE"]["FUNCTIONS"]
        display                             = self.config["CONVERSE"]["DISPLAY"]

        # @DEVELOPMENT
        #   Hey Milton, this is pretty basic for now, but we're separating the 
        #   INIT, TITLE and START outputs so we can make them fancier down the
        #   line. The CFO loves green text and all of those bullshit emojis. 
        #   He wants the user shell to be vibrant and full of energy, so this
        #   is where we will inject all his frilly nonsense.
        print(display["INIT"])
        print(display["TITLE"])

        while interacting:
            print(display["START"])
            prompt                          = input(display["PROMPT"])
            func, arg                       = self._extract(prompt)

            if prompt == commands["EXIT"]:
                break

            elif prompt == commands["HELP"]:
                print(display["HELP"])
                continue

            elif func in functions:
                setattr(app.arguments, func, arg)

            app.arguments.prompt            = prompt
            out                             = callable(app)
            
            printer(app, out)

        return True