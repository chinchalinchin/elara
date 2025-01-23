"""
app.py
------

Application functions. All application functions require an `app` argument. The format of the `app` argument is given through the `app.App` typed dictionary.
"""
# Standard Library Modules
import main


def analyze(app: main.App) -> dict:
    """
    This function injects the contents of a directory containing only RST documents into the ``data/templates/analysis.rst`` template. It then sends this contextualized prompt to the Gemini mdeol persona of *Axiom*.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated prompt and model response.
    :rtype: dict
    """
    buffer                              = app["CACHE"].vars()
    persona                             = app["PERSONAS"].function("analyze")
    buffer["currentPersona"]            = persona

    analyze_vars                        = {
        **buffer,
        **app["LANGUAGE"].vars(),
        **summarize(app),
        **{ "latex": app["CONFIG"].get("ANALYZE.LATEX_PREAMBLE") }
    }

    parsed_prompt                       = app["TEMPLATES"].render(
        temp                            = "analysis", 
        variables                       = analyze_vars
    )
    
    if app["ARGUMENTS"].render:
        return {
            "prompt"                    : parsed_prompt
        }
    
    response                            = app["MODEL"].respond(
        prompt                          = parsed_prompt,
        model_name                      = app["CACHE"].get("currentModel"),
        generation_config               = app["PERSONAS"].get("generationConfig", persona),
        safety_settings                 = app["PERSONAS"].get("safetySettings", persona),
        tools                           = app["PERSONAS"].get("tools", persona),
        system_instruction              = app["PERSONAS"].get("systemInstruction", persona)
    )
    
    return {
        "prompt"                        : parsed_prompt,
        "response"                      : response
    }

def brainstorm(app: main.App) -> dict:
    # TODO: My idea is to create a new function called 'brainstorm' that Valis oversees. My thought is to remove myself entirely from the conversation. Valis would initiatialize the first prompt based on user input (I am thinking the input will be a list of concept words)  and then Valis picks a persona at random and forwards it to them. I would have the personas return structured output that contains their reply and the persona they are passing to. I would let a conversation develop until it reaches a certain length and kill it and return the 'brainstorm' session. I was thinking of then having Valis summarize and extract the salient points that were 'brainstormed'
    # TODO: need to ensure the brainstorm history doesn't get persisted in individual conversation threads!
    return {}

def converse(app: main.App) -> dict:
    """
    Chat with one of Gemini's personas.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated prompt and model response.
    :rtype: dict
    """
    prompt                              = app["ARGUMENTS"].prompt
    
    if app["CACHE"].get("currentPersona") is None:
        converse_persona                = app["PERSONAS"].function("converse")
        app["CACHE"].update(**{
            "currentPersona"            : converse_persona
        })
        app["CACHE"].save()
        app["PERSONAS"].update(converse_persona)

    persona                             = app["CACHE"].get("currentPersona")
    prompter                            = app["CACHE"].get("currentPrompter")

    app["CONVERSATIONS"].update(
        persona                         = persona, 
        name                            = prompter, 
        msg                             = prompt,
        persist                         = not app["ARGUMENTS"].render
    )
    
    template_vars                       = { 
        **app["CACHE"].vars(), 
        **app["LANGUAGE"].vars(),
        **app["PERSONAS"].vars(persona),
        **app["CONVERSATIONS"].vars(persona)
    }

    if app["ARGUMENTS"].directory is not None:
        app["LOGGER"].info("Injecting file summary into prompt...")
        template_vars.update(summarize(app))

    parsed_prompt                       = app["TEMPLATES"].render(
        temp                            = app["CONFIG"].get("CONVERSE.TEMPLATE"), 
        variables                       = template_vars
    )

    if app["ARGUMENTS"].render:
        return {
            "prompt"                    : parsed_prompt
        }
    
    converse_config                     = app["PERSONAS"].get("generationConfig", persona)
    converse_config.update({
        "response_schema"               : app["CONFIG"].get("CONVERSE.SCHEMA"),
        "response_mime_type"            : "application/json"
    })

    response                            = app["MODEL"].respond(
        prompt                          = parsed_prompt, 
        generation_config               = converse_config,
        model_name                      = app["CACHE"].get("currentModel"),
        safety_settings                 = app["PERSONAS"].get("safetySettings"),
        tools                           = app["PERSONAS"].get("tools"),
        system_instruction              = app["PERSONAS"].get("systemInstruction")
    )
    
    app["CONVERSATIONS"].update(
        persona                         = persona, 
        name                            = persona, 
        msg                             = response.get("response"),
        memory                          = response.get("memory"),
        feedback                        = response.get("feedback")
    )

    return {
        "prompt"                        : parsed_prompt,
        "response"                      : response
    }


def request(app: main.App) -> dict:
    """
    This function halts the application to wait for the user to specify the feature request through Gherkin-style syntax.

    :param app: Dictioanry containing application configuration.
    :type app: dict
    :returns: Dictionary containing templated feature request.
    :rtype: dict
    """
    buffer                              = app["CACHE"].vars()
    persona                             = app["PERSONAS"].function("request")
    buffer["currentPersona"]            = persona

    request_vars                         = { 
        **app["TERMINAL"].gherkin(), 
        **buffer 
    }
    
    parsed_prompt                       = app["TEMPLATES"].render("request", request_vars)
    
    if app["ARGUMENTS"].render:
        return {
            "prompt"                    : parsed_prompt
        }
    
    response                            = app["MODEL"].respond(
        prompt                          = parsed_prompt,
        model_name                      = app["CACHE"].get("currentModel"),
        generation_config               = app["PERSONAS"].get("generationConfig", persona),
        safety_settings                 = app["PERSONAS"].get("safetySettings", persona),
        tools                           = app["PERSONAS"].get("tools", persona),
        system_instruction              = app["PERSONAS"].get("systemInstruction", persona)
    )
    return {
        "prompt"                        : parsed_prompt,
        "response"                      : response
    }


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
    
    review_config                       = app["PERSONAS"].get("generationConfig", persona)
    # @DEVELOPMENT
    #   HEY MILTON! We're testing structured output for your pull request reviews.
    #   What do you think!? Pretty neat, huh!?
    review_config.update({
        "response_schema"               : app["CONFIG"].get("REVIEW.SCHEMA"),
        "response_mime_type"            : "application/json"
    })

    model_res                           = app["MODEL"].respond(
        prompt                          = review_prompt,
        generation_config               = review_config,
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