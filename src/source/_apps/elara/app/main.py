""" 
main.py
-------

Module for command line interface.
"""
# Standard Library Modules
import logging
import typing 


# Application Modules
import app
import factories
import printer
import schemas


logger                      = logging.getLogger(__name__)


def clear(application: app.App, arguments: schemas.Arguments) -> schemas.Output:
    """
    Parses command line arguments and uses them to clear application data.

    :param app: Application object.
    :type app: `app.App`
    :returns: Null data structure
    :rtype: `schemas.Output`
    """
    for persona in arguments.clear:
        application.conversations.clear(persona)

    return schemas.Output()


def summarize(application: app.App) -> schemas.Output:
    """
    Generate a RestructuredText (RST) summary of a local directory.

    :param app: Application object.
    :type app: `app.App`
    :returns: Data structure containing the directory metadata and contents.
    :rtype: `schemas.Output`
    """
    return schemas.Output(
        includes            = application.directory.summary()
    )


def show(application: app.App) -> schemas.Output:
    """
    Generate a RestructuredText (RST) summary of application metadata.

    :param app: Application object.
    :type app: `app.App`
    :returns: Data structure containing application metadata.
    :rtype: `schemas.Output`
    """
    return schemas.Output(
        includes            = application.model.vars()
    )


def init() -> typing.Tuple[app.App, schemas.Arguments]:
    """
    Initialize the application.

    :returns: The appliation
    :rtype: `app.App`
    """
    arguments               = factories.ArgFactory() \
                                .with_cli_args() \
                                .build()
    
    application             =  factories.AppFactory()\
                                .with_logger() \
                                .with_cache() \
                                .with_context() \
                                .with_model() \
                                .with_personas() \
                                .with_conversations() \
                                .with_templates() \
                                .with_terminal() \
                                .with_directory(arguments) \
                                .with_repository(arguments) \
                                .build()

    application.logger.info("Writing command line arguments to cache.")
    application.cache.update(**arguments.to_dict())
         
    printer.debug(application, arguments)
    
    return application, arguments 


def main() -> None:
    """
    Main function to run the command-line interface.
    """
    this_app, these_args    = init()

    # Administrative function dispatch dictionary
    admin_operations        = {
        "clear"             : clear,
        "summarize"         : summarize,
        "show"              : show,
    }

    operation_name          = these_args.operation

    if operation_name in admin_operations:
        these_args.view     = True
        out                 = admin_operations[operation_name](this_app)

    else:
        out                 = this_app.run(these_args)

    printer.out(these_args, out)

if __name__ == "__main__":
    main()