"""
printer.py
----------

Functions for displaying and saving application out.
"""

# Standard Library Modules
import argparse
import pprint

# Application Modules
import app
import schemas


def _output(args: argparse.Namespace)   -> bool:
    """
    Determine if ``output`` has been passed into the application arguments.

    :params args: Application arguments
    :type args: `argparse.Namespace`
    """
    return "output" in vars(args).keys() and args.output


def _view(args: argparse.Namespace)     -> bool:
    """
    Determine if ``view`` has been passed into the application arguments.

    :param application: Application
    :type application: `app.App`
    """
    return "view" in vars(args).keys() and args.view


def debug(application: app.App)         -> None:
    """
    Log application debug metadata.

    :param application: Application
    :type application: `app.App`
    """
    application.logger.debug("Application initialized!")
    application.logger.debug("--- Application Configuration")
    application.logger.debug(
        pprint.pformat(application.config.vars())
    )
    application.logger.debug("--- Application Cache")
    application.logger.debug(
        pprint.pformat(application.cache.vars())
    )
    application.logger.debug("--- Application Arguments")
    application.logger.debug(
        pprint.pformat(application.arguments)
    )


def out(application: app.App, output: schemas.Output) -> None:
    """
    Write output to appropriate location. Output should follow the format,

s
    :param application: Application
    :type application: `app.App`
    :param output: application output to be written.
    :type output: `schemas.Output`
    """
    payload                             = application.templates.render(
        temp                            = "output", 
        variables                       = output.to_dict()
    )

    if _output(application.arguments):
        with open(application.arguments.output, "w") as outfile:
            outfile.write(payload)

    if _view(application.arguments):
        print(payload)
