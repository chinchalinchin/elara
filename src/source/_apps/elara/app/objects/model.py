""" 
objects.model
-------------

Object for managing Gemini Model. Essentially, a fancy wrapper around Google's GenerativeAI library to abstract away some of the details. Provides configuration and default settings.
"""
# Standard Library Modulse
import logging
import json
import traceback

# External Modules 
import google.generativeai as genai
from google.api_core import retry, exceptions

logger                                  = logging.getLogger(__name__)


class Model:
    default_model                       : str | None = None 
    """Default Gemini model"""
    tuning                              : bool = False
    """Flag for Gemini model tuning"""
    models                              : dict | None = None
    """Gemini model metadata cache"""


    def __init__(
        self,
        api_key                         : str,
        default_model                   : str,
        tuning                          : bool = False,
    ):
        """
        Initialize Model object.

        :param api_key: Gemini API key.
        :type api_key: str
        :param default_model: Full path of the default model.
        :type default_model: str
        :param tuning: Flag to enable tuning.
        :type tuning: bool
        """
        if api_key is None:
            raise ValueError("Gemini API key not provided.")
        
        genai.configure(
            api_key                     = api_key
        )

        self.default_model              = default_model
        self.tuning                     = tuning
        try:
            self.models                 = [m for m in genai.list_models()]

        except exceptions.ServiceUnavailable as e:
            logger.error(f"Gemini Service Unavailable: {e}")
            self.models                 = []

        except exceptions.InternalServerError as e:
            logger.error(f"Gemini Servie 500 failure: {e}")
            self.models                 = []

        except Exception as e:
            logger.error(f"Unknown error retrieving Gemini models: {e}")
            self.models                 = []


    def _get(
        self,
        system_instruction              : list,
        model_name                      : str = None
    )                                   -> genai.GenerativeModel:
        """
        Retrieve a Gemini Model.

        :param system_instruction: System instructions to append to Gemini model.
        :type system_instruction: list
        :param model_name: Full path of the Gemini model to use. Defaults to none, in which case the default model is used.
        :type model_name: str
        """
        if model_name is not None:
            if model_name in [
                m["path"] 
                for m 
                in self.base_models()
            ]:
                logger.info(f"Appending system instructions to base model: {model_name}")
                return genai.GenerativeModel(
                    model_name          = model_name,
                    system_instruction  = system_instruction
                )
            else:
                logger.info(f"Retrieving model without system instructions: {model_name}")
                return genai.GenerativeModel(
                    model_name          = model_name
                )
        
        logger.warning(f"{model_name} is not defined, using default model.")

        return genai.GenerativeModel(
            model_name                  = self.default_model,
            system_instruction          = system_instruction
        )


    @staticmethod
    def _is_text_model(m)               -> bool:
        """
        Determine if a model is a text-based model based on the presence of fields in metadata.
        """
        return "gemini" in m.name and \
            "generateContent" in m.supported_generation_methods
    

    @staticmethod
    def _is_tuning_model(m):
        """
        Determine if a model is a tuning model based on the presence of fields in metadata. 
        """
        return "tuning" in m.name and \
            "generateContent" in m.supported_generation_methods
        

    def vars(self)                      -> dict:
        """
        Retrieve Gemini metadata for templating.

        :returns: Dictionary of Gemini metadata.
        :rtype: `dict`
        """
        return {
            "models": {
                "base_models": self.base_models(),
                "tuning_models": self.tuning_models(),
                "tuned_models": self.tuned_models()
            }
        }
    
    
    def base_models(self)               -> list:
        """
        Retrieve all Gemini base models.

        :returns: List of Gemini base models.
        :rtype: `list`
        """
        return [{
            "path"                      : m.name,
            "version"                   : m.version,
            "input_token_limit"         : m.input_token_limit,
            "output_token_limit"        : m.output_token_limit
        } for m in self.models if self._is_text_model(m) ]
    

    def tuning_models(self)             -> list:
        """
        Retrieve all Gemini models that can be tuned.
        """
        return [{
            "path"                      : m.name,
            "version"                   : m.version,
            "input_token_limit"         : m.input_token_limit,
            "output_token_limit"        : m.output_token_limit
        } for m in self.models if self._is_tuning_model(m)]


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
    

    def tune(
        self,
        display_name                    : str,
        tuning_model                    : str,
        tuning_data                     : dict,
        # @DEVELOPMENT
        #   The develpoment team is still researching these parameters, Milton.
        #   We are defaulting them to the values that were given in the 
        #   documentation. The devs aren't sure how these values affect Gemini's
        #   model, so they don't want to mess around with them.
        #   If you had any insight into the proper value of these parameters,
        #   the development team would love to hear your opinion, Milton!
        epoch_count                     : int = 10,
        batch_size                      : int = 8,
        learning_rate                   : float = 0.01
    ):
        """
        Tune a model.

        :param display_name: Name of the tuned model.
        :type display_name: str
        :param tuning_model: Full path of the base model to use for tuning.
        :type tuning_model: sr
        :param tuning_data: Data for the tuning.
        :type tuning_data: dict
        """

        try:
            return genai.create_tuned_model(
                display_name            = display_name,
                source_model            = tuning_model,
                training_data           = tuning_data,
                epoch_count             = epoch_count,
                batch_size              = batch_size,
                learning_rate           = learning_rate
            ).result()
        
        except exceptions.ServiceUnavailable as e:
            logger.error(f"Gemini Service Unavailable: {e}")
            return None

        except exceptions.InternalServerError as e:
            logger.error(f"Gemini Service 500 failure: {e}")
            return None

        except Exception as e:
            logger.error(f"Unknonww error tuning model {display_name}: {e}")
            return None 


    @retry.Retry(
        predicate                       = retry.if_transient_error,
        initial                         = 2.0,
        maximum                         = 128.0,
        multiplier                      = 2.0,
        timeout                         = 600,
    )
    def respond(
        self,
        prompt                          : str, 
        generation_config               : dict, 
        safety_settings                 : dict, 
        tools                           : str, 
        system_instruction              : list,
        model_name                      : str = None,
    )                                   -> str:
        """
        Send a prompt and get a response from a Gemini model.
        
        :param prompt: Prompt to pass to Gemini API.
        :type prompt: str
        :param generation_config: GenerationConfig for the model.
        :type generation_config: dict
        :param safety_settings: SafetySettings for the model.
        :type safety_settings: dict
        :param tools: Enabled tools for the model.
        "type tools: str
        :param system_instruction: List of system instructions for the model.
        :type system_instruction: list
        :param model_name: Name of the model to use. Defaults to None, in which case the default model is used.
        :type: str
        """
        try:
            if model_name is not None:
                res = self._get(
                    model_name          = model_name,
                    system_instruction  = system_instruction
                ).generate_content(
                    contents = prompt,
                    # @OPERATIONS
                    #   Milton, we've discovered there is an undocumented interaction
                    #   between model versions, response schemas and supported tools.
                    # 
                    #   For example, models/gemini-exp-1206 does not support 
                    #  `code_execution` tool if using a a structured output schema!
                    #  
                    #   Of course, the knuckleheads in Development forgot to capture
                    #   the error logs, so we don't have the response code or exception
                    #   that is being thrown. Now that operations is aware of the problem,
                    #   we'll be sure to capture the error log for you next time it pops 
                    #   up! 
                    # tools = tools,
                    generation_config   = generation_config,
                    safety_settings     = safety_settings
                )
            else:
                res = self._get(
                    model_name          = self.default_model,
                    system_instruction  = system_instruction
                ).generate_content(
                    contents            = prompt,
                    tools               = tools,
                    generation_config   = generation_config,
                    safety_settings     = safety_settings
                )
                
        # TODO: implement error handling
        except exceptions.ServiceUnavailable as e:
            logger.error(f"Gemini Service Unavailable: {e}\n\n{traceback.format_exc()}")
            raise 

        except exceptions.InternalServerError as e:
            logger.error(f"Gemini Servie 500 failure: {e}\n\n{traceback.format_exc()}")
            raise

        except exceptions.BadRequest as e: 
            logger.error(f"BadRequest Error: {e}\n\n{traceback.format_exc()}")
            raise

        except Exception as e:
            logger.error(f"Error generating content: {e}\n\n{traceback.format_exc()}")
            raise
                   
        if "response_schema" in generation_config.keys():
            try:
                return json.loads(res.text)
            
            except json.decoder.JSONDecodeError as e:
                logger.error(f'Error encountered parsing response: \n{res.text}')
                logger.error(e)
                return None
            
        return res.text