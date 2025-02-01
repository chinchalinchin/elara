""" 
objects.terminal
----------------

Object for managing terminal input.
"""
# Standard Library Modules
import logging 
import typing
import re

# Application Modules
import properties
import schemas
import objects.printer as printer


logger                          = logging.getLogger(__name__)


class Terminal:
    """
    Application terminal interface for Gemini API. Initiates shell-based input loops.
    """

    config                      = None
    """Terminal configuration"""


    # Terminal Properties
    _prop_req                   = properties.TerminalProps.REQUEST.value
    _prop_cmds                  = properties.TerminalProps.COMMANDS.value 
    _prop_func                  = properties.TerminalProps.FUNCTIONS.value
    _prop_disp                  = properties.TerminalProps.DISPLAY.value
    _prop_init                  = properties.TerminalProps.INIT.value
    _prop_titl                  = properties.TerminalProps.TITLE.value
    _prop_star                  = properties.TerminalProps.START.value
    _prop_exit                  = properties.TerminalProps.EXIT.value
    _prop_help                  = properties.TerminalProps.HELP.value
    _prop_prom                  = properties.TerminalProps.PROMPT.value
    ## Gherkin Properties
    _prop_gher                  = properties.TerminalProps.GHERKIN.value
    _prop_gher_blks             = properties.TerminalProps.GHERKIN_BLOCKS.value
    _prop_gher_help             = properties.TerminalProps.GHERKIN_HELP.value

    def __init__(self, terminal_config: dict):
        """
        Initialize Terminal object.

        :param terminal_config: Configuration for the Terminal.
        :type terminal_config: `dict`.
        """
        self.config             = terminal_config
    

    @staticmethod
    def _extract(string: str) -> tuple:
        """
        Extract function word and argument from a terminal command.

        :param string: String against which to match.
        :type string: `str`
        :returns: Ordered pair of (function, argument)
        :rtype: `tuple`
        """

        # Matches "word_word(word)"
        pattern                 = r"^([a-zA-Z_]+)\(([a-zA-Z]+)\)$" 

        match                   = re.match(pattern, string)
        if match:
            return match.group(1), match.group(2)
        
        return None, None
        
    
    def gherkin(self) -> dict:
        """
        Generate a Gherkin script using terminal input

        :returns: A Gherkin script dictionary.
        :rtype: `dict`
        """
        # TODO: pass in printer and use that instead of logger
        logger.info(self.config[self._prop_gher][self._prop_gher_help])

        feat                    = { }
        feat[self._prop_req]    = { }

        for block, prompt in self.config[self._prop_gher][self._prop_gher_blks].items():
            feat[self._prop_req][block]  \
                                = input(prompt)

        return feat
    

    def interact(self, callable: typing.Callable, printer: printer.Printer, args: schemas.Arguments) -> bool:
        """
        Loop over terminal input and call a function. Function should have the following signature:

            callable(args: schemas.Arguments)

        Similary, the function used to print the output to string should have the following signature,

            printer(args: schemas.Arguments, output: schemas.Output)

        The input from the terminal will be used to mutate the `args` object before passing it into the `callable` function.
        
        :param callable: Function to invoke over the course of an interaction. 
        :type callable: `typing.Callable`
        :param args: Argumnets object
        :type args: `schemas.Arguments`
        :param printer: Function to print output.
        :type printer: `typing.Callable`
        :returns: Boolean flag
        :rtype: `bool`
        """

        interacting             = True
        commands                = self.config[self._prop_cmds]
        functions               = self.config[self._prop_func]
        display                 = self.config[self._prop_disp]

        print(display[self._prop_init]) # TODO: subsume into printer
        print(display[self._prop_titl]) # TODO: subsume into printer

        while interacting:
            print(display[self._prop_star]) # TODO: subsume into printer
            prompt              = input(display[self._prop_prom])
            func, arg           = self._extract(prompt)

            if prompt == commands[self._prop_exit]:
                break

            elif prompt == commands[self._prop_help]:
                print(display[self._prop_help]) # TODO: subsume into printer
                continue

            elif func in functions:
                setattr(args, func, arg)

            args.prompt                     = prompt
            out                             = callable(args)
            
            printer.out(args, out)

        return True