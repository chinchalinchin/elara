"""
app.py
------

Objects for orchestrating the application.
"""
# Standard Library Modules
import logging 

# Application Modules
import constants
import exceptions
import schemas
import objects.cache as cac
import objects.config as conf
import objects.context as cont
import objects.conversation as convo
import objects.directory as dir
import objects.persona as per
import objects.model as mod
import objects.printer as printer
import objects.repository as repo
import objects.template as temp
import objects.terminal as term


logger                              = logging.getLogger(__name__)


class App:
    """
    Class for managing application objects and functions. 
    
    .. important::

        Generally speaking, the `app.App` should be not instantiated directly. It should be constructed using a `factory.AppFactory` to inject its dependencies. 

    `app.App` has its dependencies injected into it during initialization. 
    This object orchestrates the application objects and exposes their functionality through its class methods. The application pulls the ``current_persona``, ``curentPrompter`` and ``currentModel`` fields from the application ``cache``. It will pull the user-provided ``prompt``, ``render`` and ``directory`` fields from the application ``arguments``. In other words, ``cache`` properties persist across application method calls and generally do not need updated, whereas the ``arguments`` properties are dynamic and dependent on the user.
    """
    cache                           : cac.Cache  | None = None
    """Application cache"""
    config                          : conf.Config  | None = None
    """Application configuration"""
    context                         : cont.Context | None = None
    """Application context"""
    conversations                   : convo.Conversation | None = None
    """Application conversation history"""
    directory                       : dir.Directory | None = None
    """Application local directory"""
    model                           : mod.Model | None = None
    """Application model"""
    personas                        : per.Persona | None = None
    """Application personas"""
    repository                      : repo.Repo | None = None
    """Application version control repository backend"""
    templates                       : temp.Template | None = None
    """Application prompt and output templates"""
    terminal                        : term.Terminal | None = None
    """Application terminal emulator"""


    # Internal Properties
    _dispatch                       = {}

    # Application Properties
    _prop_analyze_schema            = constants.AppProps.ANALYZE_SCHEMA.value
    _prop_analyze_mime              = constants.AppProps.ANALYZE_MIME.value
    _prop_brainstorm_schema         = constants.AppProps.BRAINSTORM_SCHEMA.value
    _prop_brainstorm_mime           = constants.AppProps.BRAINSTORM_MIME_TYPE.value
    _prop_converse_schema           = constants.AppProps.CONVERSE_SCHEMA.value
    _prop_converse_mime             = constants.AppProps.CONVERSE_MIME_TYPE.value
    _prop_review_schema             = constants.AppProps.REVIEW_SCHEMA.value
    _prop_review_mime               = constants.AppProps.REVIEW_MIME_TYPE.value
    _prop_request_schema            = constants.AppProps.REQUEST_SCHEMA.value
    _prop_request_mime              = constants.AppProps.REQUEST_MIME.value
    ## Special Properties
    _prop_analyze_latex             = constants.AppProps.ANALYZE_LATEX.value
    ## Nested Object Properties


    def __init__(self):
        """
        Initialize a new application object.
        """
        self._dispatch              = {
            constants.Functions.CONVERSE.value             
                                    : self.converse,
            constants.Functions.REVIEW.value
                                    : self.review,
            constants.Functions.REQUEST.value               
                                    : self.request,
            constants.Functions.TUNE.value                 
                                    : self.tune,
            constants.Functions.ANAYLZE.value              
                                    : self.analyze,
        }


    def _vars(self, func : constants.Functions) -> dict:
        """
        Get templating variables for a given function.

        :param func: Function name for which to retrieve templating variables.
        :type func: `constants.Functions`.
        :returns: Dictionary of template variables.
        :rtype: `dict`
        """
        # Ensure functional persona is used.
        buffer                      = self.cache.vars()
        persona                     = self.personas.function(func)
        buffer.update({
            constants.CacheProps.CURRENT_PERSONA.value
                                    : persona
        })
        context                     = self.context.vars(
                                        self.personas.context(persona))
        # Base level template variables
        template_vars               = { **context, **self.personas.vars(persona) }
        # Function leveltemplate variables
        if func == constants.Functions.ANAYLZE:
            logger.info("Injecting file summary into prompt...")
            template_vars.update(**buffer, **self.directory.summary(), **{
                "latex"             : self.config.get(self._prop_analyze_latex)
            })

        if func == constants.Functions.CONVERSE:
            template_vars.update(**self.cache.vars(), 
                                 **self.conversations.vars(persona))
            if self.directory:
                logger.info("Injecting file summary into prompt...")
                template_vars.update({
                    "reports"       : self.directory.summary()
                })
        
        elif func == constants.Functions.REQUEST.value:
            logger.info("Injecting Gherkin script into prompt...")
            template_vars.update(**buffer, **{
                "reports"               : self.terminal.gherkin()
            })

        elif func == constants.Functions.REVIEW.value:
            logger.info("Injecting file summary into prompt...")
            template_vars.update(**buffer, **self.repository.vars(), **{
                "reports"               : self.directory.summary()
            })
        
        return template_vars
        


    def analyze(self, arguments: schemas.Arguments) -> schemas.Output:
        """
        This function injects the contents of a directory into the ``data/templates/analysis.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Axiom*.

        :param arguments: Application arguments.
        :type arguments: `schemas.Argument`
        :returns: Data structure containing parsed prompt and response.
        :rtype: `schemas.Output`
        """
        persona                     = self.personas.function(constants.Functions.ANAYLZE.value)

        parsed_prompt               = self.templates.function(
            temp                    = constants.Functions.ANAYLZE.value, 
            variables               = self._vars(constants.Functions.ANAYLZE.value)
        )
        if arguments.render:
            return schemas.Output(
                prompt              = parsed_prompt
            )
        response                    = self.model.respond(
            prompt                  = parsed_prompt,
            model_name              = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            generation_config       = self.personas.get(constants.PersonaProps.GENERATION_CONFIG.value, persona),
            safety_settings         = self.personas.get(constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools                   = self.personas.get(constants.PersonaProps.TOOLS.value, persona),
            system_instruction      = self.personas.get(constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )
        analyze_response            = { constants.Functions.ANAYLZE.value : response }
        return schemas.Output(
            prompt                  = parsed_prompt,
            response                = analyze_response
        )


    def converse(self, arguments: schemas.Arguments) -> schemas.Output:
        """
        Chat with one of Gemini's personas.

        :param arguments: Application arguments.
        :type arguments: `schemas.Argument`
        :returns: Object containing the contextualized prompt and model response.
        :rtype: `schemas.Output`
        """
        
        if self.cache.get(constants.CacheProps.CURRENT_PERSONA.value) is None:
            converse_persona        = self.personas.function(constants.Functions.CONVERSE.value)
            self.cache.update(**{
                constants.CacheProps.CURRENT_PERSONA.value
                                    : converse_persona
            })
            self.cache.save()
            self.personas.update(converse_persona)

        persona                     = self.cache.get(constants.CacheProps.CURRENT_PERSONA.value)
        prompter                    = self.cache.get(constants.CacheProps.CURRENT_PROMPTER.value)
        self.conversations.update(
            persona                 = persona, 
            name                    = prompter, 
            msg                     = arguments.prompt,
            persist                 = not arguments.render
        )
        parsed_prompt               = self.templates.function(
            template                = constants.Functions.CONVERSE.value, 
            variables               = self._vars(constants.Functions.CONVERSE.value)
        )

        if arguments.render:
            return schemas.Output(
                prompt              = parsed_prompt
            )
        
        response_schema             = self.config.get(self._prop_converse_schema)
        response_config             = self.personas.get(constants.PersonaProps.GENERATION_CONFIG.value, persona)
        response_config.update({
            "response_schema"       : response_schema,
            "response_mime_type"    : self.config.get(self._prop_converse_mime)
        })

        response                    = self.model.respond(
            prompt                  = parsed_prompt, 
            generation_config       = response_config,
            model_name              = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            safety_settings         = self.personas.get(constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools                   = self.personas.get(constants.PersonaProps.TOOLS.value, persona),
            system_instruction      = self.personas.get(constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )
        self.conversations.update(
            persona                 = persona, 
            name                    = persona, 
            msg                     = response.get("response"),
            memory                  = response.get("memory"),
        )
        converse_response           = { constants.Functions.CONVERSE.value : response }
        return schemas.Output(
            prompt                  = parsed_prompt,
            response                = converse_response
        )


    def request(self, arguments: schemas.Arguments) -> schemas.Output:
        """
        This function initiates an input loop and prompt the the user to specify the feature request through Gherkin-style syntax.

        :returns: Object containing the contextualized prompt and model response.
        :rtype: `schemas.Output`
        """
        persona                     = self.personas.function(constants.Functions.REQUEST.value)

        parsed_prompt               = self.templates.function(
            template                = constants.Functions.REQUEST.value, 
            request_vars            = self._vars(constants.Functions.REQUEST.value)
        )
        if arguments.render:
            return schemas.Output(
                prompt              = parsed_prompt
            )
        response                    = self.model.respond(
            prompt                  = parsed_prompt,
            model_name              = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            generation_config       = self.personas.get(constants.PersonaProps.GENERATION_CONFIG.value, persona),
            safety_settings         = self.personas.get(constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools                   = self.personas.get(constants.PersonaProps.TOOLS.value, persona),
            system_instruction      = self.personas.get(constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )
        request_response            = { constants.Functions.REQUEST.value: response }
        return schemas.Output(
            prompt                  = parsed_prompt,
            response                = request_response
        )


    def review(self, arguments: schemas.Arguments) -> schemas.Output:
        """
        This function injects the contents of a git repository into the ``data/templates/review.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Milton*. *Milton*'s response is then parsed and posted to the remote VCS backend that contains the pull request corresponding to the git repository.

        :returns: Object containing the contextualized prompt, model response and service request metadata.
        :rtype: `schemas.Output`
        """

        # STEP 1. Prepare template variables and then render function template. Render
        #           to screen if applicable.
        persona                     = self.personas.function(constants.Functions.REVIEW.value) 
        review_prompt               = self.templates.function(
            template                = constants.Functions.REVIEW.value, 
            variables               = self._vars(constants.Functions.REVIEW.value)
        )
        if arguments.render:
            return schemas.Output(
                prompt              = review_prompt
            )
        # STEP 2. Append function response schema to persona's generation configuration 
        #           and post contextualized prompt to model API.
        response_config             = self.personas.get(constants.PersonaProps.GENERATION_CONFIG.value, persona)
        response_config.update({
            "response_schema"       : self.config.get(self._prop_review_schema),
            "response_mime_type"    : self.config.get(self._prop_review_mime)
        })
        response                    = self.model.respond(
            prompt                  = review_prompt,
            generation_config       = response_config,
            model_name              = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            safety_settings         = self.personas.get(constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools                   = self.personas.get(constants.PersonaProps.TOOLS.value, persona),
            system_instruction      = self.personas.get(constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )
        # STEP 3. Render overall pull request assessment request and post to VCS backend.
        reports                     = [ ]
        if response and response.get("overall"):
            msg                     = self.templates.render(
                temp                = "_services/vcs/issue",
                variables           = response,
                ext                 = ".md"
            )
            source_res              = self.repository.comment(
                msg                 = msg,
                pr                  = arguments.pull,
            )
            reports                = [ source_res ] 
        # STEP 4. Render file specific pull request assessments and post to VCS backend.
        if response and response.get("files"):
            bodies                  = []
            for file_data in response.get("files", []):
                comment             = self.templates.render(
                    temp            = "_services/vcs/file",
                    variables       = file_data,
                    ext             = ".md"
                )
                bodies.append({
                    "path"          : file_data.get("path"),
                    "msg"           : comment
                })
            source_res              = self.repository.files(
                pr                  = arguments.pull,
                bodies              = bodies
            )
            reports                 = {
                "repository"        : reports + source_res
            }
        # STEP 5: Prepare model response for output templating and return
        review_response             = { constants.Functions.REVIEW.value: response}        
        if len(reports) > 0:
            return schemas.Output(
                prompt                  = review_prompt,
                response                = review_response,
                reports                 = reports 
            )
        return schemas.Output(
            prompt                  = review_prompt,
            response                = review_response
        )


    def tune(self) -> bool:
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
                res                 = self.model.tune(
                    display_name    = p,
                    tuning_data     = self.personas.get(constants.PersonaProps.TUNING.value, p)
                )
                tuned_models.append({
                    constants.ModelProps.NAME.value : p,
                    constants.ModelProps.PATH       : res.name
                })

        if tuned_models:
            self.cache.update(**{
                constants.CacheProps.TUNED_MODELS.value: tuned_models
            })
            self.cache.save()
            return True
            
        return False
    

    def run(self, arguments: schemas.Arguments) -> schemas.Output:
        """
        Dispatch the application arguments. ``printer`` must have function signature,

            printer(application: app.App, output: schemas.Output)

        :param printer: Callable function to print application output during terminal sessions.
        :type printer: `typing.Callable`.
        """
        # Application function dispatch dictionary
        operation_name                  = arguments.operation

        if operation_name not in self._dispatch.keys():
            logger(f"Invalid operation: {operation_name}")
            return schemas.Output()

        return self._dispatch[operation_name](arguments)
    

    def tty(self, arguments: schemas.Arguments, printer: printer.Printer) -> schemas.Output:
        """
        Initiate an interactive terminal

        :param argumnets: Application arguments.
        :type arguments: `schemas.Arguments`
        :param printer: Callable function to print application output during terminal sessions.
        :type printer: `typing.Callable`.
        """
        operation_name                  = arguments.operation
        
        if operation_name not in self._dispatch.keys():
            logger(f"Invalid operation: {operation_name}")
            return schemas.Output()
        
        # @DATA
        #   Only the ``converse`` function supports interactive mode so far. 
        #   The other functions would benefit from interactive modes, but 
        #   in order to implement that interactivity, the templates for those
        #   functions in ``templates/_functions/*`` will need redesigned to
        #   support conversational threads. Some of the functions seem more 
        #   like one-off functions, like ``review`` and ``request``. We need
        #   to brainstorm on which functions require interactive and which ones
        #   are "static".
        #
        #   AI is an interesting problem! Don't you agree, Milton?!
        if operation_name == constants.Functions.CONVERSE.value: 
            arguments.view              = True
            self.terminal.interact(
                callable                = lambda args: self.converse(args),
                printer                 = printer,
                args                    = arguments
            )
            return schemas.Output()
            
        return schemas.Output()
    
    
    def validate(self, arguments: schemas.Arguments = None) -> bool:
        """
        Validate an application object and its arguments.
        
        :param argumnets: Application arguments. Defaults to None.
        :type arguments: `schemas.Arguments`
        :returns: Signal app is valid.
        :rtype: `bool`
        """
        # Evaluate in order of application dependency
        if not self.cache:
            raise exceptions.FactoryError("Cache not initialized!")
        if not self.config:
            raise exceptions.FactoryError("Config not initialized!")
        if not self.templates:
            raise exceptions.FactoryError("Context not initialized!")
        if not self.personas:
            raise exceptions.FactoryError("Personas not initialized!")
        if not self.model:
            raise exceptions.FactoryError("Model not initialized!")
        if not self.terminal:
            raise exceptions.FactoryError("Terminal not initialized!")
        # Conditional objects
        if arguments and arguments.has_vcs_args() and not self.repository:
            raise exceptions.FactoryError("Repository not initalized!")
        if arguments and arguments.directory and not self.directory:
            raise exceptions.FactoryError("Directory not initialized!")
        return True