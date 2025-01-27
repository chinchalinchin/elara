"""
app.py
------

Objects for orchestrating the application.
"""
# Standard Library Modules
import argparse
import dataclasses
import logging 

# Application Modules
import constants
import objects.cache as cac
import objects.config as conf
import objects.conversation as convo
import objects.directory as dir
import objects.language as lang
import objects.persona as per
import objects.model as mod
import objects.repo as repo
import objects.template as temp
import objects.terminal as term


@dataclasses.dataclass
class Output:
    """
    Data structure for managing application output.
    """
    prompt                                  : str | None = None
    response                                : dict | None = None
    includes                                : dict | None = None

    def to_dict(self):
        return {
            "prompt"                        : self.prompt,
            "response"                      : self.response,
            "includes"                      : self.includes
        }


class App:
    """
    Class for managing application objects and functions. This object orchestrates the application objects and exposes their functionality through its class methods. The application pulls the ``currentPersona``, ``curentPrompter`` and ``currentModel`` fields from the application ``cache``. It will pull the user-provided ``prompt``, ``render`` and ``directory`` fields from the application ``arguments``. In other words, ``cache`` properties persist across application method calls and generally do not need updated, whereas the ``arguments`` properties are dynamic and dependent on the user.
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


    def analyze(self)                       -> Output:
        """
        This function injects the contents of a directory into the ``data/templates/analysis.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Axiom*.

        :returns: Data structure containing parsed prompt and response.
        :rtype: `app.Output`
        """
        buffer                              = self.cache.vars()
        persona                             = self.personas.function(
            func                            = constants.Functions.ANAYLZE.value
        )
        buffer["currentPersona"]            = persona

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
            return Output(
                prompt                      = parsed_prompt
            )
        
        response                            = self.model.respond(
            prompt                          = parsed_prompt,
            model_name                      = self.cache.get("currentModel"),
            generation_config               = self.personas.get("generationConfig", persona),
            safety_settings                 = self.personas.get("safetySettings", persona),
            tools                           = self.personas.get("tools", persona),
            system_instruction              = self.personas.get("systemInstruction", persona)
        )
        
        analyze_response                    = { constants.Functions.ANAYLZE.value : response }

        return Output(
            prompt                          = parsed_prompt,
            response                        = analyze_response
        )


    def converse(self)                      -> Output:
        """
        Chat with one of Gemini's personas.

        :returns: Object containing the contextualized prompt and model response.
        :rtype: `app.Output`
        """
        prompt                              = self.arguments.prompt
        
        if self.cache.get("currentPersona") is None:
            converse_persona                = self.personas.function(
                func                        = constants.Functions.CONVERSE.value
            )
            self.cache.update(**{
                "currentPersona"            : converse_persona
            })
            self.cache.save()
            self.personas.update(converse_persona)

        persona                             = self.cache.get("currentPersona")
        prompter                            = self.cache.get("currentPrompter")

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
            return Output(
                prompt                      = parsed_prompt
            )
        
        response_schema                     = self.config.get("FUNCTIONS.CONVERSE.SCHEMA")
        response_config                     = self.personas.get("generationConfig", persona)
        response_config.update({
            "response_schema"               : response_schema,
            "response_mime_type"            : self.config.get("FUNCTIONS.CONVERSE.MIME")
        })

        response                            = self.model.respond(
            prompt                          = parsed_prompt, 
            generation_config               = response_config,
            model_name                      = self.cache.get("currentModel"),
            safety_settings                 = self.personas.get("safetySettings"),
            tools                           = self.personas.get("tools"),
            system_instruction              = self.personas.get("systemInstruction")
        )
        
        self.conversations.update(
            persona                         = persona, 
            name                            = persona, 
            msg                             = response.get("response"),
            memory                          = response.get("memory"),
            feedback                        = response.get("feedback")
        )

        converse_response                   = { constants.Functions.CONVERSE.value : response }

        return Output(
            prompt                          = parsed_prompt,
            response                        = converse_response
        )


    def request(self)                       -> Output:
        """
        This function initiates an input loop and prompt the the user to specify the feature request through Gherkin-style syntax.

        :returns: Object containing the contextualized prompt and model response.
        :rtype: `app.Output`
        """
        buffer                              = self.cache.vars()
        persona                             = self.personas.function(
            func                            = constants.Functions.REQUEST.value
        )
        buffer["currentPersona"]            = persona
        
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
            return {
                "prompt"                    : parsed_prompt
            }
        
        response                            = self.model.respond(
            prompt                          = parsed_prompt,
            model_name                      = self.cache.get("currentModel"),
            generation_config               = self.personas.get("generationConfig", persona),
            safety_settings                 = self.personas.get("safetySettings", persona),
            tools                           = self.personas.get("tools", persona),
            system_instruction              = self.personas.get("systemInstruction", persona)
        )
        
        request_response                    = { constants.Functions.REQUEST.value: response }

        return Output(
            prompt                          = parsed_prompt,
            response                        = request_response
        )


    def review(self)                        -> Output:
        """
        This function injects the contents of a git repository into the ``data/templates/review.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Milton*. *Milton*'s response is then parsed and posted to the remote VCS backend that contains the pull request corresponding to the git repository.

        :returns: Object containing the contextualized prompt, model response and service request metadata.
        :rtype: `app.Output`
        """

        # STEP 1. Gather function data into local variables
        buffer                              = self.cache.vars()
        persona                             = self.personas.function(
            func                            = constants.Functions.REVIEW.value
        ) 
        ## NOTE: Ensure function persona is set and hold in buffer to prevent cache overwrite
        buffer["currentPersona"]            = persona 
        includes                            = { "includes": self.directory.summary() }
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
            return Output(
                prompt                      = review_prompt
            )
        # STEP 5. Append function response schema to persona's generation configuration.
            # @DEVELOPMENT
            #   HEY MILTON! We're testing structured output for your pull request reviews.
            #   What do you think!? Pretty neat, huh!? Aren't you proud of us!?
        response_config                     = self.personas.get("generationConfig", persona)
        response_config.update({
            "response_schema"               : self.config.get("FUNCTIONS.REVIEW.SCHEMA"),
            "response_mime_type"            : self.config.get("FUNCTIONS.REVIEW.MIME")
        })
        # STEP 6. Pass contextualized prompt and function configuration to model
        response                            = self.model.respond(
            prompt                          = review_prompt,
            generation_config               = response_config,
            model_name                      = self.cache.get("currentModel"),
            safety_settings                 = self.personas.get("safetySettings", persona),
            tools                           = self.personas.get("tools", persona),
            system_instruction              = self.personas.get("systemInstruction", persona)
        )
        # STEP 7. Render overall pull request assessment request and post to VCS backend.
        includes                            = {} # reset ``includes`` for service metadata
        if response.get("overall"):
            msg                             = self.templates.render(
                temp                        = "_services/vcs/issue",
                variables                   = response
            )
            source_res                      = self.repository.comment(
                msg                         = msg,
                pr                          = self.arguments.pull,
            )
            includes["includes"]            = source_res
        # STEP 8. Render file specific pull request assessments and post to VCS backend.
            # @DEVELOPMENT
            #   Unfortunately, none of the devs could find a batch processing
            #   endpoint in the Github documentation for processing all of
            #   your file comments and amendments all at once, so we will have
            #   to post them in a flurry of API calls. We need to be careful
            #   how we implement them!
        for file_data in response.get("files", []):
            comment                         = self.templates.render(
                temp                        = "_services/vcs/file",
                variables                   = file_data
            )
            self.repository.file(
                pr                         = self.arguments.pull,
                commit                     = self.arguments.commit,
                path                       = file_data.get("path"),
                comment                    = comment
            )
        # STEP 9: Prepare model response for output templating
        review_response                     = { constants.Functions.REVIEW.value: response}
        # STEP 10: Structure results for output
        return Output(
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
        if self.config.get("GEMINI.TUNING.ENABLED"):
            tuned_models = []

            for p in self.personas.all():
                if not self.cache.is_tuned(p):
                    res                     = self.model.tune(
                        display_name        = p,
                        tuning_model        = self.config.get("GEMINI.TUNING.SOURCE"),
                        tuning_data         = self.personas.get("tuningData", p)
                    )
                    tuned_models.append({
                        "name"              : p,
                        "version"           : self.config.get("VERSION"),
                        "path"              : res.name
                    })

            if tuned_models:
                self.cache.update(**{
                    "tunedModels"           : tuned_models
                })
                self.cache.save()
                return True
            
        return False