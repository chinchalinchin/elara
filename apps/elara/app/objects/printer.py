"""
printer.py
----------

Functions for displaying and saving application output.
"""
# Application Modules
import schemas

class Printer:
    """
    TODO: explain
    """

    def out(self, arguments: schemas.Arguments, output: str) -> None:
        """
        Write output to appropriate location. Output should follow the format,

    
        :param application: Application
        :type application: `app.App`
        :param output: Application output to be written to file.
        :type output: `schemas.Output`
        """
        if arguments.output:
            with open(arguments.output, "w") as outfile:
                outfile.write(output)

        if arguments.view:
            print(output)

        return 