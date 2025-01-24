"""
app.py
------

Application functions. All application functions require an `app` argument. The format of the `app` argument is given through the `app.App` typed dictionary.
"""
# Standard Library Modules
import argparse
import dataclasses
import logging 

# Application Modules
import objects.cache as cache
import objects.config as config
import objects.conversation as conversation
import objects.directory as directory
import objects.language as language
import objects.persona as persona
import objects.model as model
import objects.repo as repo
import objects.template as template
import objects.terminal as terminal

@dataclasses.dataclass
class Output:
    """
    Data structure for managing application output
    """
    prompt : str | None
    response : str | None
    summary: str | None
    vcs : str | None


@dataclasses.dataclass
class App:
    """
    Data structure for managing application objects.
    """
    arguments : argparse.Namespace | None
    cache : cache.Cache  | None
    config : config.Config  | None
    conversations: conversation.Conversation | None
    directory: directory.Directory | None
    language: language.Language  | None
    logger : logging.Logger | None
    model : model.Model | None
    personas : persona.Persona | None
    repository: repo.Repo | None
    templates : template.Template | None
    terminal : terminal.Terminal | None

    
    def analyze(self)                       -> Output:
        """
        This function injects the contents of a directory containing only RST documents into the ``data/templates/analysis.rst`` template. It then sends this contextualized prompt to the Gemini mdeol persona of *Axiom*.

        :param app: Dictioanry containing application configuration.
        :type app: dict
        :returns: Dictionary containing templated prompt and model response.
        :rtype: dict
        """
        buffer                              = self.cache.vars()
        persona                             = self.personas.function("analyze")
        buffer["currentPersona"]            = persona

        analyze_vars                        = {
            **buffer,
            **self.language.vars(),
            **self.summarize(),
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
        
        return Output(
            prompt                          = parsed_prompt,
            response                        = response
        )

    def converse(self)                      -> Output:
        """
        Chat with one of Gemini's personas.

        :param app: Dictioanry containing application configuration.
        :type app: dict
        :returns: Dictionary containing templated prompt and model response.
        :rtype: dict
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

        if self.arguments.directory is not None:
            self.logger.info("Injecting file summary into prompt...")
            template_vars.update(
                self.summarize()
            )

        parsed_prompt                       = self.templates.render(
            temp                            = self.config.get("CONVERSE.TEMPLATE"), 
            variables                       = template_vars
        )

        if self.arguments.render:
            return Output(
                prompt                      = parsed_prompt
            )
        
        response_config                     = self.personas.get("generationConfig", persona)
        response_config.update({
            "response_schema"               : self.config.get("CONVERSE.SCHEMA"),
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

        return Output(
            prompt                          = parsed_prompt,
            response                        = response
        )


    def request(self)                       -> Output:
        """
        This function halts the application to wait for the user to specify the feature request through Gherkin-style syntax.

        :param app: Dictioanry containing application configuration.
        :type app: dict
        :returns: Dictionary containing templated feature request.
        :rtype: dict
        """
        buffer                              = self.cache.vars()
        persona                             = self.personas.function("request")
        buffer["currentPersona"]            = persona

        request_vars                         = { 
            **self.terminal.gherkin(), 
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
        
        return Output(
            prompt                          = parsed_prompt,
            response                        = response
        )


def review(app : main.App) -> dict:
    """
    This function injects the contents of a git repository into the ``data/templates/review.rst`` template. It then sends this contextualized prompt to the Gemini model persona of *Milton*. *Milton*'s response is then parsed and posted to the remote VCS backend that contains the pull request corresponding to the git repository.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated prompt and model response.
    :rtype: dict
    """

    buffer                              = app["CACHE"].vars()
    persona                             = app["PERSONAS"].function("review")
    buffer["currentPersona"]            = persona

    review_variables                    = { 
        **buffer,
        **app["REPO"].vars(),
        **app["LANGUAGE"].vars(),
        **summarize(app)
    }

    review_prompt                       = app["TEMPLATES"].render(
        temp                            = app["CONFIG"].get("REVIEW.TEMPLATE"), 
        variables                       = review_variables
    )

    if app["ARGUMENTS"].render:
        return {
            "prompt"                    : review_prompt
        }
    
    response_config                     = app["PERSONAS"].get("generationConfig", persona)
    # @DEVELOPMENT
    #   HEY MILTON! We're testing structured output for your pull request reviews.
    #   What do you think!? Pretty neat, huh!?
    response_config.update({
        "response_schema"               : app["CONFIG"].get("REVIEW.SCHEMA"),
        "response_mime_type"            : app["CONFIG"].get("REVIEW.MIME")
    })

    model_res                           = app["MODEL"].respond(
        prompt                          = review_prompt,
        generation_config               = response_config,
        model_name                      = app["CACHE"].get("currentModel"),
        safety_settings                 = app["PERSONAS"].get("safetySettings", persona),
        tools                           = app["PERSONAS"].get("tools", persona),
        system_instruction              = app["PERSONAS"].get("systemInstruction", persona)
    )


    # @DEVELOPMENT
    #   Hey Milton, we need to comment out your pull request comments.
    #   The current method is using the /issues endpoint, which appends 
    #   comments at the pull request level. Now that we have structured output
    #   in place, we can allow you to comment on specific files in the pull
    #   request! Aren't you impressed with the Development team!?
    # source_res                          = source.comment(
    #     msg                             = model_res,
    #     pr                              = app["ARGUMENTS"].pull,
    # )

    return {
        "prompt"                        : review_prompt,
        "response"                      : model_res,
        # "vcs"                           : source_res
    }


def summarize(app : main.App) -> dict:
    """
    This function summarizes the contents of a directory and writes the sumamry to an RST file. 

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated summary.
    :rtype: dict
    """
    summary_vars                        = app["DIRECTORY"].summary()

    summary                             = app["TEMPLATES"].render(
        temp                            = app["CONFIG"].get("SUMMARIZE.TEMPLATE"), 
        variables                       = summary_vars
    )
    
    return                              { 
        "summary"                       : summary
    }
    

def tune(app : main.App) -> bool:
    """
    Initialize tuned personas if tuning is enabled through the ``TUNING`` environment variable.

    :returns: A flag to signal if a tuning event occured.
    :rtype: bool
    """
    
    if app["CONFIG"].get("TUNING.ENABLED"):
        tuned_models = []
        for p in app["PERSONAS"].all():
            if not app["CACHE"].is_tuned(p):
                res                     = app["MODEL"].tune(
                    display_name        = p,
                    tuning_model        = app["CONFIG"].get("TUNING.SOURCE"),
                    tuning_data         = app["PERSONA"].tuning(p)
                )
                tuned_models.append({
                    "name"              : p,
                    "version"           : app["CONFIG"].get("VERSION"),
                    "path"              : res.name
                })
        if tuned_models:
            app["CACHE"].update(**{
                "tunedModels"           : tuned_models
            })
            app["CACHE"].save()
            return True
    return False