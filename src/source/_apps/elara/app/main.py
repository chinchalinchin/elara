""" 
main.py
-------

Module for command line interface.
"""
# Application Modules
import app
import util
import factory
import printer
import schemas


def clear(application: app.App)         -> schemas.Output:
    """
    Parses command line arguments and uses them to clear application data.

    :param app: Application object.
    :type app: `app.App`
    :returns: Null data structure
    :rtype: `schemas.Output`
    """
    for persona in application.arguments.clear:
        application.conversations.clear(persona)

    return schemas.Output()


def set(application : app.App)          -> schemas.Output:
    """
    Parses command line arguments and uses them to update the cache.

    :param app: Application object.
    :type app: `app.App`
    :returns: Null data structure
    :rtype: `schemas.Output`
    """
    cache                               = {}

    for item in application.arguments.pairs:
        if "=" not in item:
            application.logger.error(
                f"Invalid cache format. Expected 'key=value'."
            )
            continue
        
        key, value                      = item.split("=", 1)
        cache[key]                      = value

    if cache and application.cache.update(**cache):
        application.logger.info("Updated cache.")
        return schemas.Output()
        
    application.logger.warning("No configuration pairs provided.")
    return schemas.Output()


def summarize(application: app.App)     -> schemas.Output:
    """
    Generate a RestructuredText (RST) summary of a local directory.

    :param app: Application object.
    :type app: `app.App`
    :returns: Data structure containing the directory metadata and contents.
    :rtype: `schemas.Output`
    """
    return schemas.Output(
        includes                        = application.directory.summary()
    )


def show(application: app.App)          -> schemas.Output:
    """
    Generate a RestructuredText (RST) summary of application metadata.

    :param app: Application object.
    :type app: `app.App`
    :returns: Data structure containing application metadata.
    :rtype: `schemas.Output`
    """
    application.arguments.view          = True
    return schemas.Output(
        includes                        = application.model.vars()
    )


def init(
    command_line : bool                 = False
)                                       -> app.App:
    """
    Initialize the application.

    :returns: The appliation
    :rtype: app.App
    """
    application                         = factory.AppFactory()

    if command_line:
        application                     = application.with_cli_args()

    application                         = application \
                                            .with_logger() \
                                            .with_cache() \
                                            .with_language() \
                                            .with_model() \
                                            .with_personas() \
                                            .with_conversations() \
                                            .with_templates() \
                                            .with_terminal() \
                                            .with_directory() \
                                            .with_repository() \
                                            .build()

    if command_line:
        application.logger.debug("Writing command line arguments to cache.")
        application.cache.update(**vars(application.arguments))
         
    printer.debug(application)
    
    return application


def main()                              -> bool:
    """
    Main function to run the command-line interface.

    :returns: A signal the application has halted.
    :rtype: `bool`
    """
    # TODO: move dispatch logic into app.App.run()
    this_app : app.App                  = init(
        command_line                    = True
    )

    operations : dict                   = {
        # Administrative functions
        "set"                           : set,
        "clear"                         : clear,
        # Meta functions
        "summarize"                     : summarize,
        "show"                          : show,
        # Application Functions
        "converse"                      : lambda app: app.converse(),
        "review"                        : lambda app: app.review(),
        "request"                       : lambda app: app.request(),
        "tune"                          : lambda app: app.tune(),
        "analyze"                       : lambda app: app.analyze(),
    }

    operation_name                      = this_app.arguments.operation
    arguments                           = vars(this_app.arguments) 

    tty                                 = "terminal" in arguments \
                                            and arguments["terminal"]
    
    if operation_name not in operations:
        return False 
    
    if tty and operation_name == "converse": 
        this_app.arguments.view         = True
        this_app.terminal.interact(
            callable                    = lambda app: app.converse(),
            printer                     = printer.out,
            app                         = this_app
        )
        return True
        
    out                                 = operations[operation_name](this_app)
        
    printer.out(
        application                     = this_app,
        output                          = out
    )
    return True

if __name__ == "__main__":
    main()