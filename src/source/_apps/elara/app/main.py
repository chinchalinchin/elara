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


def clear(application: app.App)         -> None:
    """
    Parses command line arguments and uses them to clear application data.

    :param app: Application object.
    :type app: `app.App`
    """
    for persona in application.arguments.clear:
        application.logger.info(f"Clearing persona data: {persona}")
        application.conversations.clear(persona)


def configure(application : app.App)    -> None:
    """
    Parses command line arguments and uses them to update the cache.

    :param app: Application object.
    :type app: `app.App`
    """
    config                              = {}

    for item in application.arguments.configure:
        if "=" not in item:
            application.logger.error(
                f"Invalid configuration format: {item}. Expected key=value."
            )
            continue
        
        key, value                  = item.split("=", 1)

        if key not in application.config.data:
            application.logger.error(
                f"Invalid configuration key: {key}. Key not in configuration."
            )
            continue

        validated_value             = util.validate(value)

        if validated_value is None:
            application.logger.error(
                f"Invalidate configuration type: {key}={value}"
            )
            continue 

        config[key]                 = validated_value

    if config:
        application.cache.update(**config)
        application.cache.save()
        application.logger.info(f"Updated configuration with: {config}")
        return
        
    application.logger.warning("No configuration pairs provided.")


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
                                            .with_repository() \
                                            .with_directory() \
                                            .build()

    # Write arguments to cache
    application.logger.debug("Writing command line arguments to cache.")
    update_event                        = False
    arguments                           = vars(application.arguments)
    for k, v in arguments.items():
        if k in application.cache.vars():
            if v is None:
                v                       = application.cache.get(k)

            application.logger.debug(f"Setting {k} = {v}")
            
            update_event                = application.cache.update(**{
                k                       : v
            }) or update_event

    if update_event:
        application.cache.save()
         
    printer.debug(application)
    
    return application


def summarize(application: app.App)     -> app.Output:
    """
    Generate a RestructuredText (RST) summary of a local directory.

    :param app: Application object.
    :type app: `app.App`
    :returns: Data structure containing the directory metadata and contents.
    :rtype: `app.Output`
    """
    summary_vars                        = application.directory.summary()
    return app.Output(
        includes                        = summary_vars
    )


def show(application: app.App)      -> app.Output:
    """
    Generate a RestructuredText (RST) summary of application metadata.

    :param app: Application object.
    :type app: `app.App`
    :returns: Data structure containing application metadata.
    :rtype: `app.Output`
    """
    metadata_vars                       = application.model.vars()
    application.arguments.show          = True
    return app.Output(
        includes                        = metadata_vars
    )


def main()                              -> bool:
    """
    Main function to run the command-line interface.

    :returns: A signal the application has halted.
    :rtype: `bool`
    """
    this_app : app.App                  = init(
        command_line                    = True
    )

    operations : dict                   = {
        # Administrative functions
        "configure"                     : configure,
        "clear"                         : clear,
        "show"                          : show,
        # Application functions
        "summarize"                     : lambda app: app.summarize(),
        "converse"                      : lambda app: app.converse(),
        "review"                        : lambda app: app.review(),
        "request"                       : lambda app: app.request(),
        "tune"                          : lambda app: app.tune(),
        "analyze"                       : lambda app: app.analyze(),
        "metadata"                      : lambda app: app.metadata()
    }

    operation_name                      = this_app.arguments.operation
    arguments                           = vars(this_app.arguments) 

    tty                                 = "interactive" in arguments \
                                            and arguments["interactive"]
    
    if operation_name not in operations:
        return False 
    
    if tty and operation_name == "converse": 
        this_app.arguments.show         = True
        this_app.terminal.interact(
            callable                    = lambda app: app.converse(),
            printer                     = printer.out,
            app                         = this_app
        )
        return
        
    out                                 = operations[operation_name](this_app)
        
    printer.out(
        application                     = this_app,
        output                          = out
    )
    

if __name__ == "__main__":
    main()