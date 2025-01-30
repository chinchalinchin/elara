"""
app.py
------

Objects for orchestrating the application.
"""
# Standard Library Modules
import logging 
import typing

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


logger                          = logging.getLogger(__name__)


class App:
    """
    Class for managing application objects and functions. `App` has its dependencies injected into it during initialization. 
    
    .. important::

        Generally speaking, the `app.App` should be not instantiated directly. It should be constructed using the `factory.AppFactory` object, which will inject its configuration and dependencies. 

    """
    cache                       : cac.Cache  | None = None
    """Application cache"""
    config                      : conf.Config  | None = None
    """Application configuration"""
    context                     : cont.Context | None = None
    """Application context"""
    conversations               : convo.Conversation | None = None
    """Application conversation history"""
    directory                   : dir.Directory | None = None
    """Application local directory"""
    model                       : mod.Model | None = None
    """Application model"""
    personas                    : per.Persona | None = None
    """Application personas"""
    repository                  : repo.Repo | None = None
    """Application version control repository backend"""
    templates                   : temp.Template | None = None
    """Application prompt and output templates"""
    terminal                    : term.Terminal | None = None
    """Application terminal emulator"""


    # Internal Properties
    _dispatch                   = {}
    # Application Properties
    _prop_analyze_schema        = constants.AppProps.ANALYZE_SCHEMA.value
    _prop_analyze_mime          = constants.AppProps.ANALYZE_MIME.value
    _prop_brainstorm_schema     = constants.AppProps.BRAINSTORM_SCHEMA.value
    _prop_brainstorm_mime       = constants.AppProps.BRAINSTORM_MIME_TYPE.value
    _prop_converse_schema       = constants.AppProps.CONVERSE_SCHEMA.value
    _prop_converse_mime         = constants.AppProps.CONVERSE_MIME_TYPE.value
    _prop_review_schema         = constants.AppProps.REVIEW_SCHEMA.value
    _prop_review_mime           = constants.AppProps.REVIEW_MIME_TYPE.value
    _prop_request_schema        = constants.AppProps.REQUEST_SCHEMA.value
    _prop_request_mime          = constants.AppProps.REQUEST_MIME.value
    ## Special Function Properties
    _prop_analyze_latex         = constants.AppProps.ANALYZE_LATEX.value


    def __init__(self, cache: cac.Cache, config: conf.Config, context: cont.Context,
                 conversations: convo.Conversation, directory: dir.Directory,
                 model: mod.Model, personas: per.Persona, repo: repo.Repo,
                 templates: temp.Template, terminal: term.Terminal) -> None:
        """
        Initialize a new `app.App` object. This constructor can be used to create a new object, however it is recommended instead to use the `factories.AppFactory` object to inject the dependencies into the application rather than using this constructor to create a new `App` object.

        :param cache: Cache object
        :type cache: `objects.cache.Cache`
        :param config: Config object.
        :type config: `objects.config.Config`
        :param context: Context object
        :type context: `objects.context.Context`
        :param conversations: Conversation object
        :type conversations: `objects.conversation.Conversation`
        :param directory: Directory object.
        :type directory: `objects.directory.Directory`
        :param model: Model object
        :type model: `objects.model.Model`
        :param personas: Persona object
        :type personas: `objects.persona.Persona`
        :param templates: Templates object
        :type templates: `objects.template.Template`
        :param terminal: Terminal object
        :type terminal: `objects.terminal.Terminal`
        :returns: Nothing.
        :rtype: `None`
        """
        self._dispatch          = {
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
        self.cache              = cache
        self.config             = config
        self.content            = context
        self.conversations      = conversations
        self.directory          = directory
        self.model              = model
        self.personas           = personas
        self.repo               = repo
        self.templates          = templates
        self.terminal           = terminal


    def _vars(self, func : constants.Functions) -> dict:
        """
        Get templating variables for a given function.

        :param func: Function name for which to retrieve templating variables.
        :type func: `constants.Functions`.
        :returns: Dictionary of template variables.
        :rtype: `dict`
        """
        buffer                  = self.cache.vars().copy()
        buffer.update({constants.CacheProps.CURRENT_PERSONA.value
                                : self.personas.function(func)})

        if func == constants.Functions.ANAYLZE.value:
            persona             = self.personas.function(func)
            context             = self.context.vars(self.personas.context(persona))
            logger.info("Injecting file summary into prompt...")
            return {
                **buffer, 
                **context,
                **self.personas.vars(persona)
                **self.directory.summary(), 
                **{ "latex" : self.config.get(self._prop_analyze_latex)}
            }

        if func == constants.Functions.CONVERSE.value:
            persona             = self.cache.get(constants.CacheProps.CURRENT_PERSONA.value)
            context             = self.context.vars(self.personas.context(persona))
            template_vars       = {
                **context,
                **self.cache.vars(),
                **self.personas.vars(persona),
                **self.conversations.vars(persona)
            }
            if self.directory:
                logger.info("Injecting file summary into prompt...")
                template_vars.update({ "reports" : self.directory.summary()})
            return template_vars 
        
        if func == constants.Functions.REQUEST.value:
            persona             = self.personas.function(func)
            context             = self.context.vars(self.personas.context(persona))
            logger.info("Injecting Gherkin script into prompt...")
            return {
                **buffer,
                **context,
                **self.personas.vars(persona)
                ** { "reports": self.terminal.gherkin() }
            }

        if func == constants.Functions.REVIEW.value:
            persona             = self.personas.function(func)
            context             = self.context.vars(self.personas.context(persona))
            logger.info("Injecting file summary into prompt...")
            return {
                **buffer, 
                **context,
                **self.personas.vars(persona),
                **self.repository.vars(),
                **{ "reports" : self.directory.summary()}
            }
        
        return {}
        

    def _schema(self, schema: constants.AppProps, mime: constants.AppProps, persona: str) -> dict:
        """
        Apply a functional response schema to a persona.

        :param schema: Functional schema to apply.
        :type schema: `constants.AppProps`
        :param mime: Mime type of functional schema.
        :type mime: `constants.AppProps`
        :param persona: Persona that needs a schema.
        :type persona: `str`
        """
        res_schema              = self.config.get(schema)
        res_config              = self.personas.get(
                                    constants.PersonaProps.GENERATION_CONFIG.value, persona)
        res_config.update({
            "response_schema"   : res_schema,
            "response_mime_type": self.config.get(mime)
        })
        return res_config
    

    def _validate(self, arguments: schemas.Arguments, func: constants.Functions) -> typing.Tuple[str, str]:
        """
        Validate application function arguments.

        :param arguments: Application arguments.
        :type arguments: `schemas.Arguments`
        :param func: Application function.
        :type func: `constants.Functions`
        :returns: A tuple ccontaining the current persona and current prompter.
        :rtype: `typing.Tuple[str, str]`
        """
        persona_key             = constants.CacheProps.CURRENT_PERSONA.value
        prompter_key            = constants.CacheProps.CURRENT_PROMPTER.value
        cached_persona          = self.cache.get(persona_key)
        if cached_persona is None:
            if arguments.current_persona is None:
                arguments.current_persona \
                                = self.personas.function(func)
            self.cache.update(**{ persona_key: arguments.current_persona })
            self.personas.update(arguments.current_persona)
            self.cache.save()
        return self.cache.get(persona_key), self.cache.get(prompter_key)


    def analyze(self, arguments: schemas.Arguments) -> schemas.Output:
        """
        This function injects the contents of a directory into the ``data/templates/analysis.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Axiom*.

        :param arguments: Application arguments.
        :type arguments: `schemas.Argument`
        :returns: Data structure containing parsed prompt and response.
        :rtype: `schemas.Output`
        """
        persona                 = self.personas.function(constants.Functions.ANAYLZE.value)

        parsed_prompt           = self.templates.function(
            temp                = constants.Functions.ANAYLZE.value, 
            variables           = self._vars(constants.Functions.ANAYLZE.value)
        )

        if arguments.render:
            return schemas.Output(application=parsed_prompt)
        
        response                = self.model.respond(
            prompt              = parsed_prompt,
            model_name          = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            generation_config   = self.personas.get(constants.PersonaProps.GENERATION_CONFIG.value, persona),
            safety_settings     = self.personas.get(constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools               = self.personas.get(constants.PersonaProps.TOOLS.value, persona),
            system_instruction  = self.personas.get(constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )

        analyze_response            = { constants.Functions.ANAYLZE.value : response }

        return schemas.Output(
            application             = parsed_prompt,
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
        persona, prompter       = self._validate(arguments, constants.Functions.CONVERSE.value)

        self.conversations.update(
            persona             = persona, 
            name                = prompter, 
            msg                 = arguments.prompt,
            persist             = not arguments.render
        )

        parsed_prompt           = self.templates.function(
            template            = constants.Functions.CONVERSE.value, 
            variables           = self._vars(constants.Functions.CONVERSE.value)
        )

        if arguments.render:
            return schemas.Output(application = parsed_prompt)
        
        response_config         = self._schema(self._prop_converse_schema, self._prop_converse_mime)

        response                = self.model.respond(
            prompt              = parsed_prompt, 
            generation_config   = response_config,
            model_name          = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            safety_settings     = self.personas.get(constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools               = self.personas.get(constants.PersonaProps.TOOLS.value, persona),
            system_instruction  = self.personas.get(constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )

        self.conversations.update(
            persona             = persona, 
            name                = persona, 
            msg                 = response.get("response"),
            memory              = response.get("memory"),
        )

        application             = self.templates.function(
            template            = constants.Functions.CONVERSE.value, 
            variables           = self._vars(constants.Functions.CONVERSE.value)
        )
        return schemas.Output(application=application)


    def request(self, arguments: schemas.Arguments) -> schemas.Output:
        """
        This function initiates an input loop and prompt the the user to specify the feature request through Gherkin-style syntax.

        :returns: Object containing the contextualized prompt and model response.
        :rtype: `schemas.Output`
        """
        persona                 = self.personas.function(constants.Functions.REQUEST.value)

        parsed_prompt           = self.templates.function(
            template            = constants.Functions.REQUEST.value, 
            request_vars        = self._vars(constants.Functions.REQUEST.value)
        )
        if arguments.render:
            return schemas.Output(application=parsed_prompt)
        
        # TODO: response schema for request function

        response                = self.model.respond(
            prompt              = parsed_prompt,
            model_name          = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            generation_config   = self.personas.get(constants.PersonaProps.GENERATION_CONFIG.value, persona),
            safety_settings     = self.personas.get(constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools               = self.personas.get(constants.PersonaProps.TOOLS.value, persona),
            system_instruction  = self.personas.get(constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )

        request_response        = { constants.Functions.REQUEST.value: response }
        
        return schemas.Output(
            application         = parsed_prompt,
            response            = request_response
        )


    def review(self, arguments: schemas.Arguments) -> schemas.Output:
        """
        This function injects the contents of a git repository into the ``data/templates/review.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Milton*. *Milton*'s response is then parsed and posted to the remote VCS backend that contains the pull request corresponding to the git repository.

        :returns: Object containing the contextualized prompt, model response and service request metadata.
        :rtype: `schemas.Output`
        """

        # STEP 1. Prepare template variables and then render function template. Render
        #           to screen if applicable.
        persona                 = self.personas.function(constants.Functions.REVIEW.value) 
        review_prompt           = self.templates.function(
            template            = constants.Functions.REVIEW.value, 
            variables           = self._vars(constants.Functions.REVIEW.value)
        )
        if arguments.render:
            return schemas.Output(application = review_prompt)
        
        # STEP 2. Append function response schema to persona's generation configuration 
        #           and post contextualized prompt to model API.
        response_config         = self._schema(self._prop_review_schema, self._prop_review_mime)
        response                = self.model.respond(
            prompt              = review_prompt,
            generation_config   = response_config,
            model_name          = self.cache.get(constants.CacheProps.CURRENT_MODEL.value),
            safety_settings     = self.personas.get(constants.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools               = self.personas.get(constants.PersonaProps.TOOLS.value, persona),
            system_instruction  = self.personas.get(constants.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )

        # STEP 3. Render overall pull request assessment request and post to VCS backend.
        reports                 = { "repository": [ ] }
        if response and response.get("overall"):
            msg                 = self.templates.render(
                temp            = "_services/vcs/comment",
                variables       = response,
                ext             = ".md"
            )
            source_res          = self.repository.comment(
                msg             = msg,
                pr              = arguments.pull,
            )
            reports["repository"].append(source_res)
            
        # STEP 4. Render file specific pull request assessments and post to VCS backend.
        if response and response.get("files"):
            bodies              = []
            for file_data in response.get("files", []):
                comment         = self.templates.render(
                    temp        = "_services/vcs/file",
                    variables   = file_data,
                    ext         = ".md"
                )
                bodies.append({
                    "path"      : file_data.get("path"),
                    "msg"       : comment
                })
            source_res          = self.repository.files(
                pr              = arguments.pull,
                bodies          = bodies
            )
            reports["repository"].append(source_res)

        # STEP 5: Prepare model response for output templating and return
        review_response             = { constants.Functions.REVIEW.value: response}        
        if len(reports) > 0:
            return schemas.Output(
                application         = review_prompt,
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