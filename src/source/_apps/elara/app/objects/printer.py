"""
printer.py
----------

Functions for displaying and saving application out.
"""
# Standard Library Modules
import logging 

# Application Modules
import app
import schemas

# External Modules
import jinja2


logger                      = logging.getLogger(__name__)


class Printer:
    """
    TODO: explain
    """
    templates               = None


    def __init__(self, template_directory : str):
        """
        Initialize a printer object.

        :param template_directory: Directory containing output template.
        :type template_directory: `str`
        """
        self.templates      = jinja2.Environment(
            loader          = jinja2.FileSystemLoader(template_directory)
        )


    def debug(self, arguments: schemas.Arguments, temp = "debug.rst") -> None:
        """
        Log application debug metadata.

        :param application: Application
        :type application: `app.App`
        :param arguments: Application arguments
        :type arguments: `schemas.Arguments`
        """
        payload             = self.templates.get_template(temp).render(
            variables       = {
                "test"      : "todo"
            }
        )
        # application.logger.debug("Application initialized!")
        # application.logger.debug("--- Application Cache")
        # application.logger.debug(
        #     pprint.pformat(application.cache.vars())
        # )
        # application.logger.debug("--- Application Arguments")
        # application.logger.debug(
        #     pprint.pformat(arguments.to_dict())
        # )
        print(payload)

        return 


    def out(self, arguments: schemas.Arguments, output: schemas.Output, temp = "application.rst") -> None:
        """
        Write output to appropriate location. Output should follow the format,

    
        :param application: Application
        :type application: `app.App`
        :param output: application output to be written.
        :type output: `schemas.Output`
        """
        print(output.to_dict().get("reports"))
        payload             = self.templates.get_template(temp).render(output.to_dict())

        if arguments.output:
            with open(arguments.output, "w") as outfile:
                outfile.write(payload)

        if arguments.view:
            print(payload)

        return 