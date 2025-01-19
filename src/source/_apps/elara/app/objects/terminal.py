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
        """
        logger.info(self.gherkin_config["TERMINAL"]["INPUT"])
        feature = { }
        feature["request"] = { }

        for block, config in self.gherkin_config.items():
            if block == "TERMINAL":
                continue

            feature["request"][block.lower()] = input(config["INPUT"])

        return feature