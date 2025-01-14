""" # model.py
Wrapper around Google's GenerativeAI library. Provides configuration and default settings.
"""
import conf 
import parse

import google.generativeai as genai
import google.ai.generativelanguage as glm

genai.configure(api_key=conf.API_KEY)

def _model(
    model_name=conf.DEFAULTS["MODEL"]
):
    return genai.GenerativeModel(model_name=model_name)

def init():
    for persona in parse.personas():
        tune(persona, conf.DEFAULTS["MODEL"])
        
def reply(
    prompt, 
    model_name=conf.DEFAULTS["MODEL"]
):
    return _model(model_name).generate_content(
        contents=prompt,
        config=conf.MODEL["generation_config"]
    ).text

def tune(
    persona=conf.DEFAULTS["PERSONA"],
    source_model=conf.DEFAULTS["MODEL"]
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

    for tuned_model in genai.list_tuned_models():
        if tuned_model.display_name == persona:
            return tuned_model.name

    data = parse.training_data(persona)
    
    # Model does not exist, so create it
    tune_operation = genai.create_tuned_model(
        display_name=persona,
        source_model=source_model,
        training_data=data,
        epoch_count=1,
        batch_size=1,
        learning_rate=0.001 
    )
    tuned_model_name = tune_operation.result().name

    return tuned_model_name
