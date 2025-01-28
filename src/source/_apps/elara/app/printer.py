"""
printer.py
----------

Functions for displaying and saving application out.
"""

# Standard Library Modules
import pprint

# Application Modules
import app
import schemas


def debug(application: app.App, arguments: schemas.Arguments) -> None:
    """
    Log application debug metadata.

    :param application: Application
    :type application: `app.App`
    """
    application.logger.debug("Application initialized!")
    application.logger.debug("--- Application Cache")
    application.logger.debug(
        pprint.pformat(application.cache.vars())
    )
    application.logger.debug("--- Application Arguments")
    application.logger.debug(
        pprint.pformat(arguments.to_dict())
    )


def out(arguments: schemas.Arguments, output: schemas.Output) -> None:
    """
    Write output to appropriate location. Output should follow the format,

s
    :param application: Application
    :type application: `app.App`
    :param output: application output to be written.
    :type output: `schemas.Output`
    """
    payload             = application.templates.render(
        temp            = "output", 
        variables       = output.to_dict()
    )

    if arguments.output:
        with open(arguments.output, "w") as outfile:
            outfile.write(payload)

    if arguments.view:
        print(payload)
