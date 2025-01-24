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


def configure(application : factory.App) -> dict:
    """
    Parses and applies configuration settings.

    :param app: Dictionary containing application configuration.
    :type app: dict
    :returns: Dictionary containing the current configuration
    """
    config                              = {}

    if application.arguments.config:
        for item in application.arguments.config:
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
        application.logger.update(**config)
        application.logger.save()
        application.logger.info(f"Updated configuration with: {config}")
        return config
    
    application.logger.warning("No configuration pairs provided.")
    return config


def init()                              -> factory.App:
    """
    Initialize the application.

    :returns: Application configuration.
    :rtype: dict
    """

    application                         = factory.AppFactory() \
                                            .with_logger() \
                                            .with_cli_args() \
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
    application.logger.debug("Writing command line arguments to cache...")
    update_event                        = False
    arguments                           = vars(application.arguments)
    for k, v in arguments.items():
        if k in application.cache.vars():
            if v is None:
                v                       = application.cache.get(k)

            update_event                = application.cache.update(**{
                k                       : v
            }) or update_event

    if update_event:
        application.cache.save()
         
    printer.debug(application)
    
    return application


def main() -> bool:
    """
    Main function to run the command-line interface.
    """
    application                         = init()
    operations                          = {
        # Administrative functions
        "configure"                     : configure,
        # Application functions
        "summarize"                     : app.summarize,
        "converse"                      : app.converse,
        "review"                        : app.review,
        "request"                       : app.request,
        "tune"                          : app.tune,
        "analyze"                       : app.analyze
    }

    operation_name                      = application.arguments.operation
    arguments                           = vars(application.arguments) 

    tty                                 = "interactive" in arguments \
                                            and arguments["interactive"]
    
    if operation_name not in operations:
        return False 
    
    if tty and operation_name == "converse": 
        application.arguments.show   = True
        application.terminal.interact(
            callable                    = app.converse,
            printer                     = printer.out,
            app                         = application
        )
        return
        
    out                                 = operations[operation_name](application)
    typed_out                           = factory.Output(out)
    
    printer.out(
        application                     = application,
        output                          = typed_out,
        suppress_prompt                 = False
    )
    

if __name__ == "__main__":
    main()