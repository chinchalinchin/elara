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

def _output(args: argparse.Namespace)   -> bool:
    """
    Determine if ``output`` has been passed into the application arguments.

    :params args: Application arguments
    :type args: `argparse.Namespace`
    """
    return "output" in vars(args).keys() and args.output


def _show(args: argparse.Namespace)     -> bool:
    """
    Determine if ``show`` has been passed into the application arguments.

    :param application: Application
    :type application: `app.App`
    """
    return "show" in vars(args).keys() and args.show


def debug(
    application                         : app.App
):
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


def out(
    application                         : app.App,
    output                              : app.Output,
    suppress_prompt                     : bool = True
):
    """
    Write output to appropriate location. Output should follow the format,


    :param application: Application
    :type application: `app.App`
    :param output: application output to be written.
    :type output: `app.Output`
    :param suppress_prompt: Flag to suppress prompts from the output. This argument only applies to terminal commands.  
    :type suppress_prompt: `bool`
    """

    if _output(application.arguments):
        payload                         = application.templates.render(
            temp                        = "output", 
            variables                   = output.to_dict()
        )

        with open(application.arguments.output, "w") as outfile:
            outfile.write(payload)

    if _show(application.arguments):
        if output.summary:
            print(output.summary)

        if output.prompt and not suppress_prompt:
            print(
                application.config.get("OUTPUT.PROMPT").format(
                    content             = output.prompt
                )
            )

        if output.response:
            print(
                application.config.get("OUTPUT.RESPONSE").format(
                    content             = output.response
                )
            )

        if output.vcs:
            print(output.vcs)
