""" 
model.py
--------

Wrapper around Google's GenerativeAI library. Provides configuration and default settings.
"""
# Application Modules
import conf 
import objects.cache as cache
import objects.persona as persona

# External Modules
import google.generativeai as genai

# Ensure API key is handled securely
if config.api_key is None:
    raise ValueError("GEMINI_KEY environment variable not set.")

# Configure genai with the API key from the configuration
genai.configure(api_key=config.api_key)

genai.configure(
    api_key=conf.API_KEY
)

def init() -> bool:
    """
    Initialize tuned personas if tuning is enabled through the ``TUNING`` environment variable.

    :returns: A flag to signal if a tuning event occured.
    :rtype: bool
    """
    did_tune = False
    if conf.tuning_enabled():
        for p in persona.Personas().all():
            if p not in cache.Cache().tuned_personas():
                tune(p)
                did_tune = True    
    return did_tune

def model(
    model_name = None,
    persona = None
) -> genai.GenerativeModel:
    """
    Retrieve a `genai.GenerativeModel` from the Gemini API. 

    :param model_name: The full model path of the Gemini model to use, e.g. `models/gemini-1.5.-pro-latest` or `tunedModels/elara-123456789`. If no `model_name` is passed in, the model will be retrieved from the cache.
    :type model_name: str
    :param persona: The persona for Gemini to assume. If no `persona` is passed in, the persona will be retrieved from the cache.
    :type persona: str
    :returns: Gemini model API 
    :rtype: genai.GenerativeModel
    """
    mem = cache.Cache()

    if model_name is None:
        model_name = mem.get("currentModel")

    if persona is None:
        persona = mem.get("currentPersona")

    # NOTE: Tuning a model removes the ``system_instruction`` arguments.
    #       In other words, tuned models cannot receive this argument.
    if model_name in mem.base_models():
        # Only apply ``system_instruction`` to base models!
        data = persona.Personas(persona).system()

        # @OPERATIONS
        #   Those numskulls in development aren't even caching the models...
        #   Think about all the wasted processing, Milton! It's a nightmare!
        #   We need to come up with a way of caching the calls to the Gemini API!
        return genai.GenerativeModel(
            model_name=model_name,
            system_instruction=data
        )
    
    return genai.GenerativeModel(
        model_name=model_name
    )

def reply(
    prompt : str, 
    persona : str = None,
    model_name : str = None
) -> str:
    """
    Send a message to the Gemini API. 

    :param prompt: The message to send.
    :type prompt: str
    :param persona: The persona for Gemini to assume. This will affect the system instructions appended to the model request. If no `persona` is passed in, it will be retrieved from the cache.
    :type persona: str
    :param model_name: The full model path of the Gemini model to use, e.g. `models/gemini-1.5.-pro-latest` or `tunedModels/elara-123456789`. If no `model_name` is passed in, it will be retrieved from the cache.
    :type model_name: str
    """
    mem = cache.Cache()

    if persona is None:
        persona = mem.get("currentPersona")

    if model_name is None:
        model_name = mem.get("currentModel")

    return model(
        model_name = model_name,
        persona = persona
    ).generate_content(
        contents = prompt,
        # @DEVELOPMENT
        #   Hey Milton, it seems like only one tool can be enabled at a time. We got the following 
        #   error last time we tried to invoke this code with both `google_search_retrieval` and 
        #   `code_execution` enabled,
        # 
        #       Error in model.reply: 400 Search Grounding can't be used with other tools.
        #
        #   We were really hoping to turbocharge Gemini with both code execution and grounding. 
        #   However, it seems we will have to come up with a scheme to switch between the two based on
        #   persona. 
        #
        #   We probably want to ensure that you (Milton) have code execution, so we will want to
        #   do some sort of coditional based on your persona.
        #
        # @DATA
        #   Data team here, Milton. We already have the Persona class. Perhaps we could modify the
        #   the Persona data structure so that `tools` are a property of a particular Persona. 
        #   Then you could pull the current persona object here and pass the tools! Just a thought!
        #   
        #   The analysts here have gone ahead and taken the liberty of creating a new directory
        #   in the ``data`` folder called ``tools`` with the necessary data structures!
        # tools="google_search_retrieval",
        tools = "code_execution",
        generation_config = conf.MODEL["GENERATION_CONFIG"],
        safety_settings = conf.MODEL["SAFETY_SETTINGS"]
    ).text

def tune(
    persona : str = None,
    tuning_model : str = None
) -> str:
    """
    Checks if a tuned model with the given persona exists. If not, it creates the tuned model using the persona tuning data.

    :param persona: The persona for Gemini to assume. If no `persona` is passed in, it will be retrieved from the cache.
    :type persona: str        
    :param tuning_model: Base model to use for tuning. If no `tuning_model` is passed in, it will be retrieved from the cache.
    :type tuning_model: str
    :returns: Name of the tuned model.
    :rtype: str
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

    try:
        tuning_data = persona.Personas(persona).tuning()
        tune_operation = genai.create_tuned_model(
            display_name=persona,
            source_model=tuning_model,
            training_data=tuning_data,
            # @DEVELOPMENT
            #   The develpoment team is still researching these parameters.
            epoch_count=1,  # TODO: figure out what this does
            batch_size=1,  # TODO: figure out if I need batches
            learning_rate=0.001  # TODO: figure out what this does
            #   If you had any insight in the proper value of these parameters,
            #   the development would love to hear your opinion, Milton.
        )
        tuned_model_result = tune_operation.result()

        if tuned_model_result:
            mem.update({
                "tunedModels": [{
                    "name": persona,
                    "version": conf.VERSION,
                    "path": tuned_model_result.name
                }]
            })
            mem.save()
            return tuned_model_result.name
        
        else:
            print(f"Error: Tuned model result is None")
            return None
        
    except Exception as e:
        print(f"Error tuning model: {e}")
        return None