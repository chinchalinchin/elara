# Standard Library Modules
import argparse
import pprint

# Application Modules
import app

def _output(args: argparse.Namespace)   -> bool:
    return "output" in vars(args).keys() and args.output


def _show(args: argparse.Namespace)     -> bool:
    return "show" in vars(args).keys() and args.show


def debug(
    app                                 : app.App
):
    app.logger.debug("Application initialized!")
    app.logger.debug("--- Application Configuration")
    app.logger.debug(
        pprint.pformat(app.config.vars())
    )
    app.logger.debug("--- Application Cache")
    app.logger.debug(
        pprint.pformat(app.cache.vars())
    )
    app.logger.debug("--- Application Arguments")
    app.logger.debug(
        pprint.pformat(app.arguments)
    )

def out(
    application                         : app.App,
    output                              : app.Output,
    suppress_prompt                     : bool = True
):
    """
    Write output to appropriate location. Output should follow the format,


    :param application: Application
    :type application: app.App
    :param output: application output to be written.
    :type output: app.Output
    :param suppress_prompt: Flag to suppress prompts from the output. This argument only applies to terminal commands.  
    :type suppress_prompt: bool
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
