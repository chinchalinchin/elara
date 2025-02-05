"""
app.py
------

Objects for orchestrating the application.
"""
# Standard Library Modules
import logging 
import json
import typing

# Application Modules
import properties
import exceptions
import schemas
import util
import objects.cache as cac
import objects.config as conf
import objects.conversation as convo
import objects.directory as dir
import objects.injection as inject
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
    injections                  : inject.Injection | None = None
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
    _prop_brainstorm_schema     = properties.AppProps.BRAINSTORM_SCHEMA.value
    _prop_brainstorm_mime       = properties.AppProps.BRAINSTORM_MIME_TYPE.value
    _prop_converse_schema       = properties.AppProps.CONVERSE_SCHEMA.value
    _prop_converse_mime         = properties.AppProps.CONVERSE_MIME_TYPE.value
    _prop_formalize_schema      = properties.AppProps.FORMALIZE_SCHEMA.value
    _prop_formalize_mime        = properties.AppProps.FORMALIZE_MIME.value
    _prop_review_schema         = properties.AppProps.REVIEW_SCHEMA.value
    _prop_review_mime           = properties.AppProps.REVIEW_MIME_TYPE.value
    _prop_request_schema        = properties.AppProps.REQUEST_SCHEMA.value
    _prop_request_mime          = properties.AppProps.REQUEST_MIME.value
    ## Special Function Properties
    _prop_latex                 = properties.AppProps.LATEX.value
    _prop_block                 = properties.AppProps.BLOCKS.value
    _prop_reports               = properties.AppProps.REPORTS.value


    def __init__(self, cache: cac.Cache | None = None, config: conf.Config | None = None, 
                injections: inject.Injection | None = None, conversations: convo.Conversation | None = None,
                directory: dir.Directory | None = None, model: mod.Model | None = None, 
                personas: per.Persona | None = None, repo: repo.Repo | None = None,
                templates: temp.Template | None = None, terminal: term.Terminal | None = None) -> None:
        """
        Initialize a new `app.App` object. This constructor can be used to create a new object, however it is recommended instead to use the `factories.AppFactory` object to inject the dependencies into the application rather than using this constructor to create a new `App` object.

        :param cache: Cache object
        :type cache: `objects.cache.Cache`
        :param config: Config object.
        :type config: `objects.config.Config`
        :param injections: Injection object
        :type injections: `objects.injection.Injection`
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
            ## RENDERING FUNCTIONS 
            properties.Functions.SUMMARIZE.value
                                : self.summarize,
            ## ADMINISTRATIVE FUNCTIONS
            properties.Functions.CLEAR.value
                                : self.clear,
            properties.Functions.DEBUG.value
                                : self.debug,
            ## MODEL FUNCTIONS
            properties.Functions.MODELS.value
                                : self.models,
            properties.Functions.TUNE.value                 
                                : self.tune,
            ## GENERATIVE FUNCTIOSN
            properties.Functions.CONVERSE.value             
                                : self.converse,
            properties.Functions.REVIEW.value
                                : self.review,
            properties.Functions.REQUEST.value               
                                : self.request,
            properties.Functions.FORMALIZE.value              
                                : self.formalize,
        }
        self.cache              = cache
        self.config             = config
        self.injections         = injections
        self.conversations      = conversations
        self.directory          = directory
        self.model              = model
        self.personas           = personas
        self.repo               = repo
        self.templates          = templates
        self.terminal           = terminal
    

    def _schema(self, schema: properties.AppProps, mime: properties.AppProps, persona: str) -> dict:
        """
        Apply a functional response schema to a persona.

        :param schema: Functional schema to apply.
        :type schema: `properties.AppProps`
        :param mime: Mime type of functional schema.
        :type mime: `properties.AppProps`
        :param persona: Persona that needs a schema.
        :type persona: `str`
        """
        res_schema              = self.config.get(schema)
        res_config              = self.personas.get(
                                    properties.PersonaProps.GENERATION_CONFIG.value, persona)
        res_config.update({
            "response_schema"   : res_schema,
            "response_mime_type": self.config.get(mime)
        })
        return res_config
    

    def _blocks(self, func: properties.Functions) -> dict:
        """
        Retrieve the block configuration for a function
        """
        path                    = ".".join([ properties.AppProps.FUNCTIONS.value, func, self._prop_block ])
        return { self._prop_block: self.config.get(path)}


    def _vars(self, func : properties.Functions, schema: typing.Union[str | None] = None) -> dict:
        """
        Get templating variables for a given function.

        :param func: Function name for which to retrieve templating variables.
        :type func: `properties.Functions`.
        :param schema: Functional output schema. Defaults to `None`
        :param schema: `typing.Union[str | None]`
        :returns: Dictionary of template variables.
        :rtype: `dict`
        """
        persona_key             = properties.CacheProps.CURRENT_PERSONA.value
        prompter_key            = properties.CacheProps.CURRENT_PROMPTER.value

        if func == properties.Functions.CONVERSE.value:
            persona             = self.cache.get(persona_key)

        else:
            persona             = self.personas.function(func)

        self.personas.populate(self.injections.get(), persona)

        template_vars           = {
            persona_key         : persona, 
            prompter_key        : self.cache.get(prompter_key),
            **self._blocks(func),
            **self.personas.vars(persona),
            **self.config.get(self._prop_latex),
            **self.conversations.vars(persona),
            **{ "function": func, "schema": json.dumps(schema)}
        }

        template_vars["reports"] = {}

        if self.directory:
            logger.info("Injecting file summary into prompt...")
            template_vars["reports"].update(
                self.directory.summary())

        if self.repository:
            logger.info("Injecting repository info into prompt...")
            template_vars.update(self.repository.vars())

        if func == properties.Functions.REQUEST.value:
            logger.info("Injecting Gherkin script into prompt...")
            template_vars["reports"].update(
                self.terminal.gherkin())
            
        return template_vars


    def _validate(self, arguments: schemas.Arguments, func: properties.Functions) -> typing.Tuple[str, str]:
        """
        Validate application function arguments.

        :param arguments: Application arguments.
        :type arguments: `schemas.Arguments`
        :param func: Application function.
        :type func: `properties.Functions`
        :returns: A tuple ccontaining the current persona and current prompter.
        :rtype: `typing.Tuple[str, str]`
        """
        persona_key             = properties.CacheProps.CURRENT_PERSONA.value
        prompter_key            = properties.CacheProps.CURRENT_PROMPTER.value
        cached_persona          = self.cache.get(persona_key)

        if cached_persona is None:
            if arguments.current_persona is None:
                arguments.current_persona \
                                = self.personas.function(func)
                
            self.cache.update(**{ persona_key: arguments.current_persona })
            self.personas.update(arguments.current_persona)
            self.cache.save()

        return self.cache.get(persona_key), self.cache.get(prompter_key)


    def converse(self, arguments: schemas.Arguments) -> str:
        """
        Chat with one of Gemini's personas.

        :param arguments: Application arguments.
        :type arguments: `schemas.Argument`
        :returns: Object containing the contextualized prompt and model response.
        :rtype: `schemas.Output`
        """
        persona, prompter       = self._validate(arguments, properties.Functions.CONVERSE.value)
        response_config         = self._schema(
            schema              = self._prop_converse_schema, 
            mime                = self._prop_converse_mime,
            persona             = persona
        )
        schema                  = response_config["response_schema"]

        self.conversations.update(
            persona             = persona, 
            name                = prompter, 
            message             = arguments.prompt,
            persist             = not arguments.render
        )

        parsed_prompt           = self.templates.render(
                                    self._vars(properties.Functions.CONVERSE.value, schema))

        if arguments.render:
            return parsed_prompt

        response                = self.model.respond(
            prompt              = parsed_prompt, 
            generation_config   = response_config,
            model_name          = self.cache.get(properties.CacheProps.CURRENT_MODEL.value),
            safety_settings     = self.personas.get(properties.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools               = self.personas.get(properties.PersonaProps.TOOLS.value, persona),
            system_instruction  = self.personas.get(properties.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )

        self.conversations.update(
            persona             = persona, 
            name                = persona, 
            message             = response.get("response"),
            memory              = response.get("memory"),
        )

        return self.templates.render(
                                self._vars(properties.Functions.CONVERSE.value, schema))


    def formalize(self, arguments: schemas.Arguments) -> str:
        """
        This function injects the contents of a directory into the ``data/templates/formalize.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Axiom*.

        :param arguments: Application arguments.
        :type arguments: `schemas.Argument`
        :returns: Data structure containing parsed prompt and response.
        :rtype: `schemas.Output`
        """
        persona, prompter       = self._validate(arguments, properties.Functions.FORMALIZE.value)
        response_config         = self._schema(
            schema              = self._prop_formalize_schema, 
            mime                = self._prop_formalize_mime,
            persona             = persona
        )
        schema                  = response_config["response_schema"]

        self.conversations.update(
            persona             = persona, 
            name                = prompter, 
            message             = arguments.prompt,
            persist             = not arguments.render
        )

        parsed_prompt           = self.templates.render(
                                    self._vars(properties.Functions.FORMALIZE.value, schema))

        if arguments.render:
            return parsed_prompt
        
        response                = self.model.respond(
            prompt              = parsed_prompt,
            generation_config   = response_config,
            model_name          = self.cache.get(properties.CacheProps.CURRENT_MODEL.value),
            safety_settings     = self.personas.get(properties.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools               = self.personas.get(properties.PersonaProps.TOOLS.value, persona),
            system_instruction  = self.personas.get(properties.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )

        self.conversations.update(
            persona             = persona, 
            name                = persona, 
            message             = response.get("response"),
            memory              = response.get("memory"),
        )

        variables               = {
            **self._vars(properties.Functions.FORMALIZE.value),
            properties.Functions.FORMALIZE.value: response
        }
        
        return self.templates.render(variables)


    def request(self, arguments: schemas.Arguments) -> str:
        """
        This function initiates an input loop and prompt the the user to specify the feature request through Gherkin-style syntax.

        :returns: Object containing the contextualized prompt and model response.
        :rtype: `schemas.Output`
        """
        persona                 = self.personas.function(properties.Functions.REQUEST.value)
        variables               = self._vars(properties.Functions.REQUEST.value)

        # TODO: response schema for request function

        parsed_prompt           = self.templates.render(variables)

        if arguments.render:
            return parsed_prompt
        

        response                = self.model.respond(
            prompt              = parsed_prompt,
            model_name          = self.cache.get(properties.CacheProps.CURRENT_MODEL.value),
            generation_config   = self.personas.get(properties.PersonaProps.GENERATION_CONFIG.value, persona),
            safety_settings     = self.personas.get(properties.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools               = self.personas.get(properties.PersonaProps.TOOLS.value, persona),
            system_instruction  = self.personas.get(properties.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )

        variables               = {
            **variables,
            properties.Functions.REQUEST.value: response,
        }
        
        application             = self.templates.function(
            template            = properties.Functions.REQUEST.value, 
            request_vars        = variables
        )
        
        return application


    def review(self, arguments: schemas.Arguments) -> str:
        """
        This function injects the contents of a git repository into the ``data/templates/review.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Milton*. *Milton*'s response is then parsed and posted to the remote VCS backend that contains the pull request corresponding to the git repository.

        :returns: Object containing the contextualized prompt, model response and service request metadata.
        :rtype: `schemas.Output`
        """
        persona                 = self.personas.function(properties.Functions.REVIEW.value) 
        response_config         = self._schema(
            schema              = self._prop_review_schema, 
            mime                = self._prop_review_mime,
            persona             = persona
        )
        schema                  = response_config["response_schema"]
        review_prompt           = self.templates.render(
                                    self._vars(properties.Functions.REVIEW.value, schema))

        if arguments.render:
            return review_prompt
        
        response                = self.model.respond(
            prompt              = review_prompt,
            generation_config   = response_config,
            model_name          = self.cache.get(properties.CacheProps.CURRENT_MODEL.value),
            safety_settings     = self.personas.get(properties.PersonaProps.SAFETY_SETTINGS.value, persona),
            tools               = self.personas.get(properties.PersonaProps.TOOLS.value, persona),
            system_instruction  = self.personas.get(properties.PersonaProps.SYSTEM_INSTRUCTION.value, persona)
        )

        vcs_res                 = {  }

        if response and response.get("overall"):
            msg                 = self.templates.service("comment", "vcs", response)
            vcs_res             = self.repository.comment(msg, arguments.pull)
            
        if response and response.get("files"):
            bodies              = []
            for file_data in response.get("files", []):
                comment         = self.templates.service("file", "vcs", file_data,)
                bodies.append({
                    "path"      : file_data.get("path"),
                    "msg"       : comment
                })
            vcs_res             = util.merge(vcs_res,
                                    self.repository.files(arguments.pull, bodies))

        variables               = {
            **self._vars(properties.Functions.REVIEW.value, schema),
            properties.Functions.REVIEW.value: response
        }

        return self.templates.render(variables)


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
                    tuning_data     = self.personas.get(properties.PersonaProps.TUNING.value, p)
                )
                tuned_models.append({
                    properties.ModelProps.NAME.value : p,
                    properties.ModelProps.PATH       : res.name
                })

        if tuned_models:
            self.cache.update(**{
                properties.CacheProps.TUNED_MODELS.value: tuned_models
            })
            self.cache.save()
            return True
            
        return False
    
        
    def summarize(self, arguments: schemas.Arguments) -> str:
        """
        Return a summary of a directory.

        :returns: RST formatted summary of Directory object.
        :rtype: `str`
        """
        if not self.directory:
            logger.error("Directory object not initialized!")
            # TODO: create it with the arguments.
            raise exceptions.ObjectNotInitialized(
                "objects.directory.Directory not initialized!")
        return self.templates.render(
            template            = "application", 
            variables           = self._vars(properties.Functions.SUMMARIZE.value)
        )


    def clear(self, arguments: schemas.Arguments) -> None:
        """
        Wipe persona conversation history.

        :param argumnets: Application arguments.
        :type arguments: `schemas.Arguments`
        """
        for persona in arguments.clear:
            logger.warning(f"Clearing {persona} conversation history...")
            self.conversations.clear(persona)


    def models(self, arguments: schemas.Arguments) -> dict:
        """
        Retrieve model metadata.

        :returns: Dictionary of model metadata.
        :rtype: `dict`
        """
        variables                       = {
            "reports"                   : self.model.vars()
        }
        return self.templates.render(variables)
    

    def run(self, arguments: schemas.Arguments) -> typing.Union[str, None]:
        """
        Dispatch the application arguments. ``printer`` must have function signature,

            printer(application: app.App, output: schemas.Output)

        :param printer: Callable function to print application output during terminal sessions.
        :type printer: `typing.Callable`.
        """
        # Application function dispatch dictionary
        operation_name                  = arguments.operation

        if operation_name not in self._dispatch.keys():
            logger.error(f"Invalid operation: {operation_name}")
            return None

        return self._dispatch[operation_name](arguments)
    

    def tty(self, arguments: schemas.Arguments, printer: printer.Printer) -> bool:
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
            return False
        
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
        if operation_name == properties.Functions.CONVERSE.value: 
            arguments.view              = True
            return self.terminal.interact(
                callable                = lambda args: self.converse(args),
                printer                 = printer,
                args                    = arguments
            )
            
        return False
    
    
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
    

    def debug(self, arguments: schemas.Arguments):
        """
        Get application debug message.
        """
        variables                       = { 
            **self.cache.vars(),
            **arguments.to_dict()
        }
        return self.templates.render(variables, "debug")