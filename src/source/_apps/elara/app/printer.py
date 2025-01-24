# Standard Library Modules
import argparse
import pprint

# Application Modules
import elara.src.source._apps.elara.app.factory as factory


def _output(args: argparse.Namespace)   -> bool:
    return "output" in vars(args).keys() and args.output


def _show(args: argparse.Namespace)     -> bool:
    return "show" in vars(args).keys() and args.show


def debug(
    app                                 : factory.App
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
    application                         : factory.App,
    output                              : factory.Output,
    suppress_prompt                     : bool = True
):
    """
    Write output to appropriate location. Output should follow the format,

    .. code-block:: python

        out                             = schema.Output(**{
            "prompt"                    : "words",
            "response"                  : "words",
            "summary"                   : "words",
            "vcs"                       : "words"
        })

    :param application:
    :type application: App
    :param output: application output to be written.
    :type output:
    :param suppress_prompt: Flag to suppress prompts from the output. This argument only applies to terminal commands.  
    :type suppress_prompt: bool
    """

    args                                = vars(application.arguments)

    if _output(args):
        payload = application.templates.render("output", output)
        with open(args["output"], "w") as outfile:
            outfile.write(payload)

    if _show(args):
        if output.summary:
            print(out["summary"])

        if output.prompt and not suppress_prompt:
            print(
                application.config.get("OUTPUT.PROMPT").format(
                    content             = out["prompt"]
                )
            )

        if output.response:
            print(
                application.config.get("OUTPUT.RESPONSE").format(
                    content             = out["response"]
                )
            )

        if output.vcs:
            print(out["vcs"])
