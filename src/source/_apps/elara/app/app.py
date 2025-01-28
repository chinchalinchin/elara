"""
app.py
------

Objects for orchestrating the application.
"""
# Standard Library Modules
import argparse
import logging 
import typing

# Application Modules
import constants
import schemas
import util
import objects.cache as cac
import objects.config as conf
import objects.conversation as convo
import objects.directory as dir
import objects.language as lang
import objects.persona as per
import objects.model as mod
import objects.repository as repo
import objects.template as temp
import objects.terminal as term


class App:
    """
    Class for managing application objects and functions. This object orchestrates the application objects and exposes their functionality through its class methods. The application pulls the ``current_persona``, ``curentPrompter`` and ``currentModel`` fields from the application ``cache``. It will pull the user-provided ``prompt``, ``render`` and ``directory`` fields from the application ``arguments``. In other words, ``cache`` properties persist across application method calls and generally do not need updated, whereas the ``arguments`` properties are dynamic and dependent on the user.
    """
    arguments                               : argparse.Namespace | None = None 
    """Application arguments"""
    cache                                   : cac.Cache  | None = None
    """Application cache"""
    config                                  : conf.Config  | None = None
    """Application configuration"""
    conversations                           : convo.Conversation | None = None
    """Application conversation history"""
    directory                               : dir.Directory | None = None
    """Application local directory"""
    language                                : lang.Language  | None = None
    """Application language modules"""
    logger                                  : logging.Logger | None = None
    """Application logger"""
    model                                   : mod.Model | None = None
    """Application model"""
    personas                                : per.Persona | None = None
    """Application personas"""
    repository                              : repo.Repo | None = None
    """Application version control repository backend"""
    templates                               : temp.Template | None = None
    """Application prompt and output templates"""
    terminal                                : term.Terminal | None = None
    """Application terminal emulator"""


    def analyze(self)                       -> schemas.Output:
        """
        This function injects the contents of a directory into the ``data/templates/analysis.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Axiom*.

        :returns: Data structure containing parsed prompt and response.
        :rtype: `schemas.Output`
        """
        buffer                              = self.cache.vars()
        persona                             = self.personas.function(
                                                constants.Functions.ANAYLZE.value)
        buffer[constants.CacheProps.CURRENT_PERSONA.value] \
                                            = persona

        latex_preamble                      = { 
            "latex"                         : self.config.get("FUNCTIONS.ANALYZE.LATEX_PREAMBLE") 
        }

        analyze_vars                        = {
            **buffer,
            **latex_preamble
            **self.language.vars(),
            **self.directory.summary(),
        }

        parsed_prompt                       = self.templates.render(
            temp                            = constants.Functions.ANAYLZE.value, 
            variables                       = analyze_vars
        )
        
        if self.arguments.render:
            return schemas.Output(
                prompt                      = parsed_prompt
            )
        
        response                            = self.model.respond(
            prompt                          = parsed_prompt,
            model_name                      = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            generation_config               = self.personas.get(
                                                constants.PersonaProps.GENERATION_CONFIG.value, persona),
            safety_settings                 = self.personas.get(
                                                constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools                           = self.personas.get(
                                                constants.PersonaProps.TOOLS.value, persona),
            system_instruction              = self.personas.get(
                                                constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )
        
        analyze_response                    = { constants.Functions.ANAYLZE.value : response }

        return schemas.Output(
            prompt                          = parsed_prompt,
            response                        = analyze_response
        )


    def converse(self)                      -> schemas.Output:
        """
        Chat with one of Gemini's personas.

        :returns: Object containing the contextualized prompt and model response.
        :rtype: `schemas.Output`
        """
        prompt                              = self.arguments.prompt
        
        if self.cache.get(constants.CacheProps.CURRENT_PERSONA.value) is None:
            converse_persona                = self.personas.function(
                                                constants.Functions.CONVERSE.value)
            self.cache.update(**{
                constants.CacheProps.CURRENT_PERSONA.value
                                            : converse_persona
            })
            self.cache.save()
            self.personas.update(converse_persona)

        persona                             = self.cache.get(
                                                constants.CacheProps.CURRENT_PERSONA.value)
        prompter                            = self.cache.get(
                                                constants.CacheProps.CURRENT_PROMPTER.value)

        self.conversations.update(
            persona                         = persona, 
            name                            = prompter, 
            msg                             = prompt,
            persist                         = not self.arguments.render
        )
        
        template_vars                       = { 
            **self.cache.vars(), 
            **self.language.vars(),
            **self.personas.vars(persona),
            **self.conversations.vars(persona)
        }
        
        if self.arguments.directory is not None:
            self.logger.info("Injecting file summary into prompt...")
            template_vars.update({
                "includes"                  : self.directory.summary()
            })

        parsed_prompt                       = self.templates.render(
            temp                            = self.config.get("FUNCTIONS.CONVERSE.TEMPLATE"), 
            variables                       = template_vars
        )

        if self.arguments.render:
            return schemas.Output(
                prompt                      = parsed_prompt
            )
        
        response_schema                     = self.config.get("FUNCTIONS.CONVERSE.SCHEMA")
        response_config                     = self.personas.get(
                                                constants.PersonaProps.GENERATION_CONFIG.value, persona)
        response_config.update({
            "response_schema"               : response_schema,
            "response_mime_type"            : self.config.get("FUNCTIONS.CONVERSE.MIME")
        })

        response                            = self.model.respond(
            prompt                          = parsed_prompt, 
            generation_config               = response_config,
            model_name                      = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            safety_settings                 = self.personas.get(
                                                constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools                           = self.personas.get(
                                                constants.PersonaProps.TOOLS.value, persona),
            system_instruction              = self.personas.get(
                                                constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )
        
        self.conversations.update(
            persona                         = persona, 
            name                            = persona, 
            msg                             = response.get("response"),
            memory                          = response.get("memory"),
        )

        converse_response                   = { constants.Functions.CONVERSE.value : response }

        return schemas.Output(
            prompt                          = parsed_prompt,
            response                        = converse_response
        )


    def request(self)                       -> schemas.Output:
        """
        This function initiates an input loop and prompt the the user to specify the feature request through Gherkin-style syntax.

        :returns: Object containing the contextualized prompt and model response.
        :rtype: `schemas.Output`
        """
        buffer                              = self.cache.vars()
        persona                             = self.personas.function(constants.Functions.REQUEST.value)
        buffer[constants.CacheProps.CURRENT_PERSONA.value] \
                                            = persona
        
        request                             = self.terminal.gherkin()

        request_vars                         = { 
            **request, 
            **buffer 
        }
        
        parsed_prompt                       = self.templates.render(
            temp                            = constants.Functions.REQUEST.value, 
            request_vars                    = request_vars
        )
        
        if self.arguments.render:
            return schemas.Output(
                prompt                      = parsed_prompt
            )
        
        response                            = self.model.respond(
            prompt                          = parsed_prompt,
            model_name                      = self.cache.get(
                                                constants.CacheProps.CURRENT_MODEL.value),
            generation_config               = self.personas.get(
                                                constants.PersonaProps.GENERATION_CONFIG.value, persona),
            safety_settings                 = self.personas.get(
                                                constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools                           = self.personas.get(
                                                constants.PersonaProps.TOOLS.value, persona),
            system_instruction              = self.personas.get(
                                                constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )
        
        request_response                    = { constants.Functions.REQUEST.value: response }

        return schemas.Output(
            prompt                          = parsed_prompt,
            response                        = request_response
        )


    def review(self)                        -> schemas.Output:
        """
        This function injects the contents of a git repository into the ``data/templates/review.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Milton*. *Milton*'s response is then parsed and posted to the remote VCS backend that contains the pull request corresponding to the git repository.

        :returns: Object containing the contextualized prompt, model response and service request metadata.
        :rtype: `schemas.Output`
        """

        # STEP 1. Gather function data into local variables
        buffer                              = self.cache.vars()
        persona                             = self.personas.function(
                                                constants.Functions.REVIEW.value) 
        ## NOTE: Ensure function persona is set and hold in buffer to prevent cache overwrite
        buffer[constants.CacheProps.CURRENT_PERSONA.value] \
                                            = persona 
        includes                            = { 
            "includes"                      : self.directory.summary() 
        }
        # STEP 2. Merge function template variables
        review_variables                    = { 
            **includes,
            **buffer,
            **self.repository.vars(),
            **self.language.vars(),
        }
        # STEP 3. Render function template
        review_prompt                       = self.templates.render(
            temp                            = self.config.get("FUNCTIONS.REVIEW.TEMPLATE"), 
            variables                       = review_variables
        )
        # STEP 4. Halt function if executing with dry-run ``self.arguments.render`` flag.
        ## NOTE: This corresponds to the CLI argument ``--render``.
        if self.arguments.render:
            return schemas.Output(
                prompt                      = review_prompt
            )
        # STEP 5. Append function response schema to persona's generation configuration.
        response_config                     = self.personas.get(
                                                constants.PersonaProps.GENERATION_CONFIG.value, persona)
        response_config.update({
            "response_schema"               : self.config.get("FUNCTIONS.REVIEW.SCHEMA"),
            "response_mime_type"            : self.config.get("FUNCTIONS.REVIEW.MIME")
        })
        # STEP 6. Pass contextualized prompt and function configuration to model
        response                            = self.model.respond(
            prompt                          = review_prompt,
            generation_config               = response_config,
            model_name                      = self.cache.get(
                                                constants.CacheProps.CURRENT_MODEL.value),
            safety_settings                 = self.personas.get(
                                                constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools                           = self.personas.get(
                                                constants.PersonaProps.TOOLS.value, persona),
            system_instruction              = self.personas.get(
                                                constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )
        # STEP 7. Render overall pull request assessment request and post to VCS backend.
        if response and response.get("overall"):
            msg                             = self.templates.render(
                temp                        = "_services/vcs/issue",
                variables                   = response,
                ext                         = ".md"
            )
            source_res                      = self.repository.comment(
                msg                         = msg,
                pr                          = self.arguments.pull,
            )
            includes                        = [ source_res ] 
        # STEP 8. Render file specific pull request assessments and post to VCS backend.
        if response and response.get("files"):
            bodies                          = []
            for file_data in response.get("files", []):
                comment                     = self.templates.render(
                    temp                    = "_services/vcs/file",
                    variables               = file_data,
                    ext                     = ".md"
                )
                bodies.append({
                    "path"                  : file_data.get("path"),
                    "msg"                   : comment
                })
            source_res                      = self.repository.files(
                pr                          = self.arguments.pull,
                bodies                      = bodies
            )
            includes                        = {
                "repository"                : includes + source_res
            }
            print("\n includes \n",includes)
        # STEP 9: Prepare model response for output templating
        review_response                     = { constants.Functions.REVIEW.value: response}
        # STEP 10: Structure results for output
        return schemas.Output(
            prompt                          = review_prompt,
            response                        = review_response,
            includes                        = includes 
        )


    def tune(self)                          -> bool:
        """
        Initialize tuned personas if tuning is enabled through the ``TUNING`` environment variable.

        :returns: A flag to signal if a tuning event occured.
        :rtype: bool
        """
    
        # @DEVELOPMENT
        #   Hey, Milton! It seems like this function should go into `objects/model.py`, don't you think?
        #   Problem is, this function uses the cache, and we would prefer to keep the model and cache
        #   decoupled...
        tuned_models = []

        for p in self.personas.all():
            if not self.cache.is_tuned(p):
                res                     = self.model.tune(
                    display_name        = p,
                    tuning_model        = self.config.get("GEMINI.TUNING.SOURCE"),
                    tuning_data         = self.personas.get(
                                            constants.PersonaProps.TUNING.value, p)
                )
                tuned_models.append({
                    constants.ModelProps.NAME.value
                                        : p,
                    constants.ModelProps.VERSION.value           
                                        : self.config.get("VERSION"),
                    constants.ModelProps.PATH
                                        : res.name
                })

        if tuned_models:
            self.cache.update(**{
                constants.CacheProps.TUNED_MODELS.value \
                                        : tuned_models
            })
            self.cache.save()
            return True
            
        return False
    

    def run(self, printer: typing.Callable) -> schemas.Output:
        """
        Dispatch the application arguments. ``printer`` must have function signature,

            printer(application: app.App, output: schemas.Output)

        :param printer: Callable function to print application output during terminal sessions.
        :type printer: `typing.Callable`.
        """
        # Application function dispatch dictionary
        operations : dict                   = {
            "converse"                      : self.converse,
            "review"                        : self.review,
            "request"                       : self.request,
            "tune"                          : self.tune,
            "analyze"                       : self.analyze,
        }

        operation_name                      = self.arguments.operation
        arguments                           = vars(self.arguments) 

        tty                                 = "terminal" in arguments \
                                                and arguments["terminal"]
        
        if operation_name not in operations:
            return schemas.Output()
        
        if tty and operation_name == "converse": 
            self.arguments.view             = True
            self.terminal.interact(
                callable                    = self.converse,
                printer                     = printer.out,
                app                         = self
            )
            return schemas.Output()
            
        return operations[operation_name]()