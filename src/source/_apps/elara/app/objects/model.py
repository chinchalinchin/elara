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
import constants
import exceptions as excepts
import util

# External Modules 
import google.generativeai as genai
from google.api_core import retry, exceptions

logger                          = logging.getLogger(__name__)


class Model:
    model_config                : dict  = {}
    """Model configuration"""
    models                      : dict  = {}
    """Model metadata cache"""


    # Model Properties
    _prop_name                  = constants.ModelProps.NAME.value
    _prop_vers                  = constants.ModelProps.VERSION.value
    _prop_path                  = constants.ModelProps.PATH.value
    ## GEMINI PROPERTIES
    _prop_gem                   = constants.ModelProps.GEMINI.value
    _prop_auth                  = constants.ModelProps.API_KEY.value
    _prop_dflt                  = constants.ModelProps.DEFAULT.value
    _prop_tune                  = constants.ModelProps.TUNING.value
    _prop_src                   = constants.ModelProps.SOURCE.value


    def __init__(self, model_config : dict) -> None:
        """
        Initialize Model object.

        :param model_config: Dictionary of model configuration.
        :type model_config: `dict`
        """
        self.model_config       = model_config

        if not self.model_config[self._prop_gem].get(self._prop_auth):
            raise excepts.GeminiAPIKeyError("Gemini API Key not set!")

        genai.configure(
            api_key = self.model_config[self._prop_gem][self._prop_auth])

        try:
            self.models         = [m for m in genai.list_models()]

        except exceptions.ServiceUnavailable as e:
            logger.error(f"Gemini Service Unavailable: {e}")
            self.models         = []

        except exceptions.InternalServerError as e:
            logger.error(f"Gemini Servie 500 failure: {e}")
            self.models         = []

        except Exception as e:
            logger.error(f"Unknown error retrieving Gemini models: {e}")
            self.models         = []


    @staticmethod
    def _is_text_model(m) -> bool:
        """
        Determine if a model is a text-based model based on the presence of fields in metadata.
        
        :returns: Signal if model is text-based.
        :rtype: `bool`
        """
        return "gemini" in m.name and \
            "generateContent" in m.supported_generation_methods
    

    @staticmethod
    def _is_tuning_model(m) -> bool:
        """
        Determine if a model is a tuning model based on the presence of fields in metadata. 

        :returns: Signal if model supports tunning
        :rtype: `bool`
        """
        return "tuning" in m.name and \
            "generateContent" in m.supported_generation_methods
        

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

        base_paths              =  [ m["path"] for m in self.base_models()]

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
        return {
            "models": {
                "base_models"   : self.base_models(),
                "tuning_models" : self.tuning_models(),
                "tuned_models"  : self.tuned_models()
            }
        }
    
    
    def base_models(self) -> list:
        """
        Retrieve all Gemini base models.

        :returns: List of Gemini base models.
        :rtype: `list`
        """
        return [{
            "path"              : m.name,
            "version"           : m.version,
            "input_token_limit" : m.input_token_limit,
            "output_token_limit": m.output_token_limit
        } for m in self.models if self._is_text_model(m) ]
    

    def tuning_models(self)             -> list:
        """
        Retrieve all Gemini models that can be tuned.
        """
        return [{
            "path"              : m.name,
            "version"           : m.version,
            "input_token_limit" : m.input_token_limit,
            "output_token_limit": m.output_token_limit
        } for m in self.models if self._is_tuning_model(m)]


    @retry.Retry(predicate = retry.if_transient_error, initial = 2.0,
                    maximum = 128.0, multiplier = 2.0, timeout = 600)
    def tuned_models(self)              -> list:
        """
        Retreive all tuned models
        """
        try:
            return genai.list_tuned_models()
        
        except exceptions.ServiceUnavailable as e:
            logger.error(f"Gemini Service Unavailable: {e}")
            return []

        except exceptions.InternalServerError as e:
            logger.error(f"Gemini Servie 500 failure: {e}")
            return []

        except Exception as e:
            logger.error(f"Unknown error retrieving tuned models: {e}")
            return []
    
    
    @retry.Retry(predicate = retry.if_transient_error, initial = 2.0,
                    maximum = 128.0, multiplier = 2.0, timeout = 600)
    def tune(self,display_name : str, tuning_model: str, tuning_data: dict,
        # @DEVELOPMENT
        #   The develpoment team is still researching these parameters, Milton.
        #   We are defaulting them to the values that were given in the 
        #   documentation. The devs aren't sure how these values affect Gemini's
        #   model, so they don't want to mess around with them.
        #   If you had any insight into the proper value of these parameters,
        #   the development team would love to hear your opinion, Milton!
        epoch_count: int = 10, batch_size: int = 8, learning_rate: float = 0.01
    ):
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
        
        except exceptions.ServiceUnavailable as e:
            logger.error(f"Gemini Service Unavailable: {e}")
            return None

        except exceptions.InternalServerError as e:
            logger.error(f"Gemini Service 500 failure: {e}")
            return None

        except Exception as e:
            logger.error(f"Unknonww error tuning model {display_name}: {e}")
            return None 


    @retry.Retry(predicate = retry.if_transient_error, initial = 2.0,
                    maximum = 128.0, multiplier = 2.0, timeout = 600)
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
                
        # TODO: implement more error handling
        except exceptions.ServiceUnavailable as e:
            logger.error(f"Gemini Service Unavailable: {e}\n\n{traceback.format_exc()}")
            raise 

        except exceptions.InternalServerError as e:
            logger.error(f"Gemini Servie 500 failure: {e}\n\n{traceback.format_exc()}")
            raise

        except exceptions.BadRequest as e: 
            if "400 Tool use with a response mime type" in str(e):
                logger.warning(f"{model_name} does not support tool use, retrying...")
                # @OPERATIONS
                #   Some models do not support tool use when using response schemas and throw the 
                #   following error,
                #
                #       google.api_core.exceptions.InvalidArgument: 400 Tool use with a response mime type: 
                #           'application/json' is unsupported
                # 
                #   So catch those errors and remove `tools` from the arguments.
                return self.respond( 
                    prompt              = prompt, 
                    generation_config   = generation_config, 
                    safety_settings     = safety_settings, 
                    tools               = None, 
                    system_instruction  = system_instruction, 
                    model_name          = model_name)
            logger.error(f"BadRequest Error: {e}\n\n{traceback.format_exc()}")

            raise

        except Exception as e:
            logger.error(f"Error generating content: {e}\n\n{traceback.format_exc()}")
            raise

        # @OPERATIONS
        #   Milton! For shame! You're embedding U+200B in your responses and breaking 
        #   our application! I expected this from the code monkeys in Development, but
        #   you? Et tu, Milton?
        #
        #   Now the development team is hard at work trying to salvage your mess. They've
        #   resorted to regex to stop you from breaking the application.
        #
        #   Are you happy with you yourself, Milton!? Do you know what happens when you
        #   let devs run wild with regex? We're living on borrowed time, Milton.
        res                             = util.sanitize(res.text)  

        if "response_schema" in generation_config.keys():
            try:
                return json.loads(res)
            
            except json.decoder.JSONDecodeError as e:
                logger.error(f'Error parsing response because Milton sucks:\n\n{res}\n\n{e}')
                return None
            
        return res