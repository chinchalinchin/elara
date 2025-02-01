""" 
objects.model
-------------

Object for managing Gemini Model. Essentially, a fancy wrapper around Google's GenerativeAI library to abstract away some of the details. Provides configuration and default settings.
"""
# Standard Library Modulse
import logging
import json
import time
import traceback

# Application Modules
import properties
import exceptions as excepts

# External Modules 
import google.generativeai as genai
from google.api_core import retry, exceptions


logger                          = logging.getLogger(__name__)


class Model:
    model_config                : dict  = {}
    """Model configuration"""
    models                      : dict  = {}
    """Model metadata cache"""
    refresh                     : bool = False
    """Flag to populate the cache with model metadata"""


    # Model Properties
    _prop_name                  = properties.ModelProps.NAME.value
    _prop_vers                  = properties.ModelProps.VERSION.value
    _prop_path                  = properties.ModelProps.PATH.value
    _prop_dflt                  = properties.ModelProps.DEFAULT.value
    ## GEMINI PROPERTIES
    _prop_gem                   = properties.ModelProps.GEMINI.value
    _prop_auth                  = properties.ModelProps.API_KEY.value
    _prop_tune                  = properties.ModelProps.TUNING.value
    _prop_src                   = properties.ModelProps.SOURCE.value
    _prop_in                    = properties.ModelProps.INPUT_LIMIT.value
    _prop_out                   = properties.ModelProps.OUTPUT_LIMIT.value
    _prop_gene                  = properties.ModelProps.GENERATE.value
    _prop_meth                  = properties.ModelProps.METHODS.value


    def __init__(self, model_config : dict, cached_models : list = None) -> None:
        """
        Initialize Model object.

        :param model_config: Dictionary of model configuration.
        :type model_config: `dict`
        :param cached_models: List of models. Defaults to None. If not specified, an API call will be made to retrieve the latest list.
        """
        self.model_config       = model_config

        if not self.model_config[self._prop_gem].get(self._prop_auth):
            raise excepts.GeminiAPIKeyError("Gemini API Key not set!")

        genai.configure(
            api_key = self.model_config[self._prop_gem][self._prop_auth])

        if not cached_models:
            self.models         = {
                **self._models(),
                properties.TemplateVars.REPORT_TUNED.value
                                : self._tuned()
            }
            self.refresh        = True    
        else:
            self.models             = cached_models


    def _is_text_model(self, m: dict) -> bool:
        """
        Determine if a model is a text-based model based on the presence of fields in metadata.
        
        :returns: Signal if model is text-based.
        :rtype: `bool`
        """
        return self._prop_gem in m.name and \
            self._prop_gene in m.supported_generation_methods
    

    def _is_tuning_model(self, m) -> bool:
        """
        Determine if a model is a tuning model based on the presence of fields in metadata. 

        :returns: Signal if model supports tunning
        :rtype: `bool`
        """
        return self._prop_tune in m.name and \
            self._prop_gene in m.supported_generation_methods


    @retry.Retry(predicate = retry.if_transient_error, initial = 2.0,
                    maximum = 128.0, multiplier = 2.0, timeout = 150)
    def _models(self)  -> dict:
        """
        Retrieve all Gemini base models.

        :returns: List of Gemini base models.
        :rtype: `list`
        """
        try:
            models = [m for m in genai.list_models()]
            return {
                properties.TemplateVars.REPORT_BASE.value: [{
                    self._prop_path     : m.name,
                    self._prop_vers     : m.version,
                    self._prop_in       : m.input_token_limit,
                    self._prop_out      : m.output_token_limit
                } for m in models if self._is_text_model(m) ],
                properties.TemplateVars.REPORT_TUNING.value:[{
                    self._prop_path     : m.name,
                    self._prop_vers     : m.version,
                    self._prop_in       : m.input_token_limit,
                    self._prop_out      : m.output_token_limit
                } for m in models if self._is_tuning_model(m)]
            }
        except Exception as e:
            logger.error(f"{e}\n\n{traceback.format_exc()}")
            return {}


    @retry.Retry(predicate = retry.if_transient_error, initial = 2.0,
                    maximum = 128.0, multiplier = 2.0, timeout = 150)
    def _tuned(self) -> list:
        """
        Retreive all tuned models
        """
        try:
            return {
                properties.TemplateVars.REPORT_TUNED.value: [{ 
                    self._prop_path : m.name 
                } for m in genai.list_tuned_models()]
            }
        
        except Exception as e:
            logger.error(f"{e}\n\n{traceback.format_exc()}")
            return []
        

    def _get(self, system_instruction: list, model_name: str = None) -> genai.GenerativeModel:
        """
        Retrieve a Gemini Model.

        :param system_instruction: System instructions to append to Gemini model.
        :type system_instruction: `list`
        :param model_name: Full path of the Gemini model to use. Defaults to none, in which case the default model is used.
        :type model_name: `str`
        """
        if model_name is None:
            logger.warning(f"{model_name} is not defined, using default model.")
            model_name          = self.model_config[self._prop_gem][self._prop_dflt]

        base_models             = properties.TemplateVars.REPORT_BASE.value
        base_paths              =  [ m[self._prop_path] for m in self.models[base_models] ]

        if model_name in base_paths:
            logger.info(f"Appending system instructions to base model: {model_name}")
            return genai.GenerativeModel(model_name = model_name,
                                            system_instruction = system_instruction)
        
        logger.info(f"Retrieving model without system instructions: {model_name}")
        return genai.GenerativeModel(model_name = model_name)
        

    def vars(self) -> dict:
        """
        Retrieve Gemini metadata for templating.

        :returns: Dictionary of Gemini metadata.
        :rtype: `dict`
        """
        return { properties.TemplateVars.REPORT_MODELS.value: self.models }
    
    
    
    @retry.Retry(predicate = retry.if_transient_error, initial = 2.0,
                    maximum = 128.0, multiplier = 2.0, timeout = 150)
    def tune(self, display_name : str, tuning_model: str, tuning_data: dict,
        epoch_count: int = 10, batch_size: int = 8, learning_rate: float = 0.01):
        """
        Tune a model.

        :param display_name: Name of the tuned model.
        :type display_name: `str`
        :param tuning_model: Full path of the base model to use for tuning.
        :type tuning_model: `str`
        :param tuning_data: Data for the tuning.
        :type tuning_data: `dict`
        """

        try:
            operation           = genai.create_tuned_model(
                display_name    = display_name,
                source_model    = tuning_model,
                training_data   = tuning_data,
                epoch_count     = epoch_count,
                batch_size      = batch_size,
                learning_rate   = learning_rate
            )
        
            for status in operation.wait_bar():
                logger.info(f"Awaiting tuning results: {status}")
                time.sleep(10)

            return operation.result()
        
        except Exception as e:
            logger.error(f"{e}\n\n{traceback.format_exc()}")
            raise


    @retry.Retry(predicate = retry.if_transient_error, initial = 2.0,
                    maximum = 128.0, multiplier = 2.0, timeout = 150)
    def respond(self, prompt: str, generation_config: dict, safety_settings: dict, 
                tools: str, system_instruction: list, model_name: str = None) -> str:
        """
        Send a prompt and get a response from a LLM model.
        
        :param prompt: Prompt to post to the model API.
        :type prompt: `str`
        :param generation_config: GenerationConfig for the model.
        :type generation_config: `dict`
        :param safety_settings: SafetySettings for the model.
        :type safety_settings: `dict`
        :param tools: Enabled tools for the model.
        "type tools: `str`
        :param system_instruction: List of system instructions for the model.
        :type system_instruction: `list`
        :param model_name: Name of the model to use. Defaults to None, in which case the default model is used.
        :type: `str`
        """
        try:
            if model_name is not None:
                res = self._get(
                    model_name          = model_name,
                    system_instruction  = system_instruction
                ).generate_content(
                    contents = prompt,
                    tools = tools,
                    generation_config   = generation_config,
                    safety_settings     = safety_settings
                )
            else:
                res = self._get(
                    model_name          = self.model_config[self._prop_gem][self._prop_dflt],
                    system_instruction  = system_instruction
                ).generate_content(
                    contents            = prompt,
                    tools               = tools,
                    generation_config   = generation_config,
                    safety_settings     = safety_settings
                )

        except exceptions.BadRequest as e: 
            if "400 Tool use with a response mime type" in str(e):
                logger.warning(f"{model_name} does not support tool use, retrying...")
                return self.respond( 
                    prompt              = prompt, 
                    generation_config   = generation_config, 
                    safety_settings     = safety_settings, 
                    tools               = None, 
                    system_instruction  = system_instruction, 
                    model_name          = model_name)
            
            if "400 Json mode is not enabled" in str(e):
                logger.warning(f"{model_name} does not support response schemas, retrying...")
                generation_config       = {
                    k: v for k,v in generation_config.items()
                    if k not in ["response_schema", "response_mime_type"]
                }
                return self.respond(
                    prompt              = prompt,
                    generation_config   = generation_config,
                    safety_settings     = safety_settings,
                    tools               = tools,
                    system_instruction  = system_instruction,
                    model_name          = model_name
                )
            logger.error(f"BadRequest Error: {e}\n\n{traceback.format_exc()}")
            raise

        except Exception as e:
            logger.error(f"{e}\n\n{traceback.format_exc()}")
            raise

        if "response_schema" in generation_config.keys():
            try:
                return json.loads(res.text)
            
            except json.decoder.JSONDecodeError as e:
                logger.error(f'Error parsing response because Milton sucks:\n\n{res}\n\n{e}')
                return None
            
        return res.text