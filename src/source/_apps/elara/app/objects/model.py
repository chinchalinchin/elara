""" 
objects.model
-------------

Object for managing Gemini Model. Essentially, a fancy wrapper around Google's GenerativeAI library to abstract away some of the details. Provides configuration and default settings.
"""
# Standard Library Modulse
import logging
import json

# External Modules 
import google.generativeai as genai

logger = logging.getLogger(__name__)

class Model:
    default_model = None 
    """Default Gemini model"""
    tuning = False
    """Flag for Gemini model tuning"""
    models = None
    """Gemini model metadata cache"""

    def __init__(
        self,
        api_key : str,
        default_model : str,
        tuning: bool = False,
    ):
        """
        Initialize Model object.
        """
        if api_key is None:
            raise ValueError("Gemini API key not provided.")
        
        genai.configure(api_key=api_key)

        self.default_model = default_model
        self.tuning = tuning
        self.models = genai.list_models()

    def _get(
        self,
        system_instruction,
        model_name : str = None
    ) -> genai.GenerativeModel:
        """
        Retrieve system instructions.
        """
        if model_name is not None:
            if model_name in [
                m["path"] for m in self.base_models()
            ]:
                logger.info(f"Appending system instructions to base model: {model_name}")
                return genai.GenerativeModel(
                    model_name=model_name,
                    system_instruction=system_instruction
                )
            else:
                logger.info(f"Retrieving model without system instructions: {model_name}")
                return genai.GenerativeModel(
                    model_name=model_name
                )
        
        logger.warning(f"{model_name} is not defined, using default model.")
        return genai.GenerativeModel(
            model_name=self.default_model,
            system_instruction=system_instruction
        )

    def base_models(self) -> list:
        """
        Retrieve all Gemini models.
        """
        return [{
            "path": m.name,
            "version": m.version,
            "input_token_limit": m.input_token_limit,
            "output_token_limit": m.output_token_limit
        } 
            for m 
            in self.models
            if (
                "gemini" in m.name 
                and 
                "generateContent" in m.supported_generation_methods
            )
        ]
    
    def tuning_models(self) -> list:
        """
        Retrieve all Gemini models that can be tuned.
        """
        return [{
            "path": m.name,
            "version": m.version,
            "input_token_limit": m.input_token_limit,
            "output_token_limit": m.output_token_limit
        } 
            for m 
            in self.models
            if (
                "tuning" in m.name 
                and 
                "generateContent" in m.supported_generation_methods
            )
        ]
        
    def tuned_models(self) -> list:
        """
        Retreive all tuned models
        """
        return genai.list_tuned_models()
    
    def tune(
        self,
        display_name : str,
        tuning_model : str,
        tuning_data : dict,
        # @DEVELOPMENT
        #   The develpoment team is still researching these parameters, Milton.
        #   We are defaulting them to the values that were given in the 
        #   documentation. The devs aren't sure how these values affect Gemini's
        #   model, so they don't want to mess around with them.
        #   If you had any insight into the proper value of these parameters,
        #   the development team would love to hear your opinion, Milton!
        epoch_count : int = 1,
        batch_size : int = 1,
        learning_rate : float = 0.001
    ):
        """
        
        """
        try:
            return genai.create_tuned_model(
                display_name=display_name,
                source_model=tuning_model,
                training_data=tuning_data,
                epoch_count=epoch_count,
                batch_size=batch_size,
                learning_rate=learning_rate
            ).result()
        except Exception as e:
            logger.error(f"Error tuning model {display_name}: {e}")
            raise
    
    def respond(
        self,
        prompt : str, 
        generation_config : dict, 
        safety_settings : dict, 
        tools : str, 
        system_instruction: list,
        model_name : str = None,
    ) -> str:
        """

        """
        try:
            if model_name is not None:
                res = self._get(
                    model_name = model_name,
                    system_instruction = system_instruction
                ).generate_content(
                    contents = prompt,
                    tools = tools,
                    generation_config = generation_config,
                    safety_settings = safety_settings
                )
            else:
                res = self._get(
                    model_name = self.default_model,
                    system_instruction = system_instruction
                ).generate_content(
                    contents = prompt,
                    tools = tools,
                    generation_config = generation_config,
                    safety_settings = safety_settings
                )
        except Exception as e:
            logger.error(f"Error generating content: {e}")
            raise

        print(res)
           
        if "response_schema" in generation_config.keys():
            return json.loads(res.text)
        return res.text