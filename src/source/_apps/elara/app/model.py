""" # model.py
Wrapper around Google's GenerativeAI library. Provides configuration and default settings.
"""
# Application Modules
import conf 
import parse
import objects

# External Modules
import google.generativeai as genai

genai.configure(api_key=conf.API_KEY)

def _model(
    model_name=conf.DEFAULTS["MODEL"],
    persona=None
):
    mem = objects.cache.Cache().get()

    base_model_names = [ 
        model["path"] 
        for model in mem["baseModels"]
    ]

    if model_name in base_model_names:
        if persona is None:
            persona = mem["template"]["currentPersona"]

        data = objects.persona.Persona(persona).get()

        return genai.GenerativeModel(
            model_name=model_name,
            system_instruction=data["SYSTEM"]
        )
    
    return genai.GenerativeModel(
        model_name=model_name
    )

def init():
    mem = objects.cache.Cache().get()
    for persona in conf.PERSONAS["ALL"]:
        # Only call tune if the model is not found in cache
        if not any(model["name"] == persona for model in mem["tunedModels"]):
            tune(persona)

def reply(
    prompt, 
    persona=None,
    model_name=None
):
    mem = objects.cache.Cache().get()
    if persona is None:
        persona = mem["template"]["currentPersona"]
    if model_name is None:
        model_name = mem["currentModel"]

    return _model(model_name).generate_content(
        contents=prompt,
        generation_config=conf.MODEL["GENERATION_CONFIG"],
        safety_settings=conf.MODEL["SAFETY_SETTINGS"]
    ).text

def tune(
    persona=None,
    tuning_model=None
):
    """
    Checks if a tuned model with the given display name exists.
    If not, it creates the tuned model using the provided data.

    Args:
        persona: The display name of the tuned model.
        model_type: Base model to use

    Returns:
        The name of the tuned model (either existing or newly created).
    """    
    mem = objects.cache.Cache().get()

    if persona is None:
        persona = mem["template"]["currentPersona"]
         
    if tuning_model is None:
        tuning_model = mem["tuningModel"]
       
    personas = [ 
        model
        for model 
        in mem["tunedModels"] 
        if model["name"] == persona
    ]

    if len(personas) > 0:
        return personas[0]

    for tuned_model in genai.list_tuned_models():
        if tuned_model.display_name == persona:
            buffer = {
                "name": persona,
                "path": tuned_model.name,
                "version": conf.VERSION
            }
            mem["tunedModels"] += [ buffer ]
            objects.cache.Cache().save(mem)
            return buffer

    persona_payload = parse.persona(persona)["TUNING"]

    tune_operation = genai.create_tuned_model(
        display_name=persona,
        source_model=tuning_model,
        training_data=persona_payload,
        epoch_count=1, # TODO: figure out what this does
        batch_size=1, # TODO: figure out if I need batches
        learning_rate=0.001 # TODO: figure out what this does
    )

    mem["tunedModels"] += [{
        "name": persona,
        "version": conf.VERSION,
        "path": tune_operation.result().name
    }]

    objects.cache.Cache().save(mem)

    return tune_operation.result().name
