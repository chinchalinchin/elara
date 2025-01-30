""" 
main.py
-------

Module for command line interface.
"""
# Standard Library Modules
import logging
import os
import typing 


# Application Modules
import app
import constants
import factories
import schemas
import objects.printer as printer


def logs(schema : str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
           file: str = None, level: str = "INFO")  -> None:
    """
    Configure application logging

    :param schema: Schema for logs
    :type schema: `str`
    :param file: Location of log file, if logs are to be written to file.
    :type file: `str`
    :param level: Level of logs to capture.
    :type level: `str`
    """
    logger                  = logging.getLogger()

    if level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        logger.setLevel(level)
    else:
        logger.setLevel("INFO") 

    formatter               = logging.Formatter(schema)

    if file is not None:
        file_handler        = logging.FileHandler(file)
        file_handler.setLevel(level) 
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler         = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return

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


def summarize(application: app.App, arguments: schemas.Arguments) -> schemas.Output:
    """
    Generate a RestructuredText (RST) summary of a local directory.

    :param app: Application object.
    :type app: `app.App`
    :returns: Data structure containing the directory metadata and contents.
    :rtype: `schemas.Output`
    """
    return schemas.Output(
        reports             = application.directory.summary()
    )


def show(application: app.App, arguments: schemas.Arguments) -> schemas.Output:
    """
    Generate a RestructuredText (RST) summary of application metadata.

    :param app: Application object.
    :type app: `app.App`
    :returns: Data structure containing application metadata.
    :rtype: `schemas.Output`
    """
    return schemas.Output(
        reports             = application.model.vars()
    )


def init() -> typing.Tuple[app.App, schemas.Arguments, printer.Printer]:
    """
    Initialize the application.

    :returns: The appliation
    :rtype: `app.App`
    """
    app_factory             = factories.AppFactory()
    arg_factory             = factories.ArgFactory()

    arguments               = arg_factory \
                                .with_cli_args() \
                                .build()
    
    application             =  app_factory\
                                .with_cache() \
                                .with_injections() \
                                .with_model() \
                                .with_personas() \
                                .with_conversations() \
                                .with_templates() \
                                .with_terminal() \
                                .with_directory(arguments) \
                                .with_repository(arguments) \
                                .build(arguments)
    
    prnter                  = factories.PrinterFactory().build()

    application.cache.update(**arguments.to_dict())
         
    prnter.debug(arguments)
    
    log_file                = app_factory.log_file()
    log_level               = application.config.get(constants.LogProps.LEVEL.value)
    log_schema              = application.config.get(constants.LogProps.SCHEMA.value)
    
    logs(log_schema, log_file, log_level)

    return application, arguments, prnter


def main() -> None:
    """
    Main function to run the command-line interface.
    """
    this_app, these_args, this_printer    \
                            = init()

    # Administrative function dispatch dictionary
    admin_operations        = {
        "clear"             : clear,
        "summarize"         : summarize,
        "show"              : show,
    }

    operation_name          = these_args.operation

    if operation_name in admin_operations:
        these_args.view     = True
        out                 = admin_operations[operation_name](this_app, these_args)
        this_printer.out(these_args, out)
        return 
    
    elif these_args.terminal:
        this_app.tty(these_args, this_printer)
        return
    
    out                     = this_app.run(these_args)
    this_printer.out(these_args, out)
    return 


if __name__ == "__main__":
    main()