"""
app.py
------

Objects for orchestrating the application.
"""
# Standard Library Modules
import argparse
import enum
import dataclasses
import logging 

# Application Modules
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
    
class Functions(enum.Enum):
    """Application functions"""
    ANAYLZE                                 = "analyze"
    CONVERSE                                = "converse"
    REVIEW                                  = "review"
    REQUEST                                 = "request"


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
        persona                             = self.personas.function("analyze")
        buffer["currentPersona"]            = persona

        analyze_vars                        = {
            **buffer,
            **self.language.vars(),
            **self.directory.summary(),
            **{ "latex": self.config.get("ANALYZE.LATEX_PREAMBLE") }
        }

        parsed_prompt                       = self.templates.render(
            temp                            = "analysis", 
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
        
        analyze_response                    = {
            Functions.ANAYLZE.VALUE         : response
        }

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
            converse_persona                = self.personas.function("converse")
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

        includes                            = {}
        
        if self.arguments.directory is not None:
            self.logger.info("Injecting file summary into prompt...")
            template_vars.update({
                "includes"                  : self.directory.summary()
            })

        parsed_prompt                       = self.templates.render(
            temp                            = self.config.get("CONVERSE.TEMPLATE"), 
            variables                       = template_vars
        )

        if self.arguments.render:
            return Output(
                prompt                      = parsed_prompt
            )
        
        response_schema                     = self.config.get("CONVERSE.SCHEMA")
        response_config                     = self.personas.get("generationConfig", persona)
        response_config.update({
            "response_schema"               : response_schema,
            "response_mime_type"            : self.config.get("CONVERSE.MIME")
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

        converse_response                   = {
            Functions.CONVERSE.value        : response
        }

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
        persona                             = self.personas.function("request")
        buffer["currentPersona"]            = persona
        
        request                             = self.terminal.gherkin()

        request_vars                         = { 
            **request, 
            **buffer 
        }
        
        parsed_prompt                       = self.templates.render("request", request_vars)
        
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
        
        request_response                    = {
            Functions.REQUEST.value         : response
        }

        return Output(
            prompt                          = parsed_prompt,
            response                        = request_response
        )


    def review(self)                        -> Output:
        """
        This function injects the contents of a git repository into the ``data/templates/review.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Milton*. *Milton*'s response is then parsed and posted to the remote VCS backend that contains the pull request corresponding to the git repository.

        :returns: Object containing the contextualized prompt and model response.
        :rtype: `app.Output`
        """

        buffer                              = self.cache.vars()
        persona                             = self.personas.function("review")
        buffer["currentPersona"]            = persona

        review_variables                    = { 
            **buffer,
            **self.repository.vars(),
            **self.language.vars(),
            **self.directory.summary()
        }

        review_prompt                       = self.templates.render(
            temp                            = self.config.get("REVIEW.TEMPLATE"), 
            variables                       = review_variables
        )

        if self.arguments.render:
            return Output(
                prompt                      = review_prompt
            )
        
        response_config                     = self.personas.get("generationConfig", persona)
        # @DEVELOPMENT
        #   HEY MILTON! We're testing structured output for your pull request reviews.
        #   What do you think!? Pretty neat, huh!?
        response_config.update({
            "response_schema"               : self.config.get("REVIEW.SCHEMA"),
            "response_mime_type"            : self.config.get("REVIEW.MIME")
        })

        response                            = self.model.respond(
            prompt                          = review_prompt,
            generation_config               = response_config,
            model_name                      = self.cache.get("currentModel"),
            safety_settings                 = self.personas.get("safetySettings", persona),
            tools                           = self.personas.get("tools", persona),
            system_instruction              = self.personas.get("systemInstruction", persona)
        )

        # @DEVELOPMENT
        #   Hey Milton, we need to comment out your pull request comments.
        #   The current method is using the /issues endpoint, which appends 
        #   comments at the pull request level. Now that we have structured output
        #   in place, we can allow you to comment on specific files in the pull
        #   request! Aren't you impressed with the Development team!?
        # source_res                          = source.comment(
        #     msg                             = response,
        #     pr                              = self.arguments.pull,
        # )

        review_response                     = {
            Functions.REVIEW.value          : response
        }

        return Output(
            prompt                          = review_prompt,
            response                        = review_response
            # includes                      = "TODO"
        )


    def tune(self)                          -> bool:
        """
        Initialize tuned personas if tuning is enabled through the ``TUNING`` environment variable.

        :returns: A flag to signal if a tuning event occured.
        :rtype: bool
        """
    
        if self.config.get("TUNING.ENABLED"):
            tuned_models = []
            for p in self.personas.all():
                if not self.cache.is_tuned(p):
                    res                     = self.model.tune(
                        display_name        = p,
                        tuning_model        = self.config.get("TUNING.SOURCE"),
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