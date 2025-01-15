""" # model.py
Wrapper around Google's GenerativeAI library. Provides configuration and default settings.
"""
# Application Modules
import conf 
import objects.cache as cache
import objects.personas as personas

# External Modules
import google.generativeai as genai

genai.configure(api_key=conf.API_KEY)

def _model(
    model_name=conf.DEFAULTS["MODEL"],
    persona=None
):
    """
    TODO: explain
    """
    mem = cache.Cache()

    if model_name in mem.base_models():
        if persona is None:
            persona = mem.get("currentPersona")

        data = personas.Personas(persona).get()

        print(data["SYSTEM"])

        return genai.GenerativeModel(
            model_name=model_name,
            system_instruction=data["SYSTEM"]
        )
    
    return genai.GenerativeModel(
        model_name=model_name
    )

def init():
    """
    TODO: explain
    """
    for p in personas.Personas().all():
        if p not in cache.Cache().tuned_personas():
            tune(p)

def reply(
    prompt, 
    persona=None,
    model_name=None
):
    """
    TODO: explain
    """
    mem = cache.Cache()

    if persona is None:
        persona = mem.get("currentPersona")

    if model_name is None:
        model_name = mem.get("currentModel")

    return _model(
        model_name = model_name,
        persona = persona
    ).generate_content(
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
    mem = cache.Cache()

    if persona is None:
        persona = mem.get("currentPersona")
         
    if tuning_model is None:
        tuning_model = mem.get("tuningModel")

    if mem.is_tuned(persona):
        return persona

    for tuned_model in genai.list_tuned_models():
        if tuned_model.display_name == persona:
            buffer = {
                "name": persona,
                "path": tuned_model.name,
                "version": conf.VERSION
            }
            mem.update({
                "tunedModels": [buffer]
            })
            mem.save()
            return buffer

    tuning_data = personas.Personas(persona).tuning()

    tune_operation = genai.create_tuned_model(
        display_name=persona,
        source_model=tuning_model,
        training_data=tuning_data,
        epoch_count=1, # TODO: figure out what this does
        batch_size=1, # TODO: figure out if I need batches
        learning_rate=0.001 # TODO: figure out what this does
    )

    mem.update({
        "tunedModels": [{
            "name": persona,
            "version": conf.VERSION,
            "path": tune_operation.result().name
        }]
    })

    mem.save()

    return tune_operation.result().name
