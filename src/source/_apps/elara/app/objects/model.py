""" # objects.model
Object for managing Gemini Model. Essentially, a fancy wrapper around Google's GenerativeAI library to abstract away some of the details. Provides configuration and default settings.
"""

# External Modules 
import google.generativeai as genai

class Model:
    inst = None
    """Singleton instance"""
    model = None 
    """Gemini model"""
    tuning = False
    """Flag for Gemini model tuning"""

    def __init__(
        self,
        api_key : str = None,
        tuning: bool = False
    ):
        """
        Initialize Model object.
        """
        if api_key is None:
            raise ValueError("Gemini API key not provided.")
        
        genai.configure(api_key=api_key)

        self.tuning = tuning

    def _get(
        self,
        model_name,
        system_instruction
    ):
        if model_name in self.base_models():
            return genai.GenerativeModel(
                model_name=model_name,
                system_instruction=system_instruction
            )
        
        return genai.GenerativeModel(
            model_name=model_name
        )

    def base_models(self) -> list:
        return [{
            "path": m.name,
            "version": m.version,
            "input_token_limit": m.input_token_limit,
            "output_token_limit": m.output_token_limit
        } 
            for m 
            in genai.list_models()
            if (
                "gemini" in m.name 
                and 
                "generateContent" in m.supported_generation_methods
            )
        ]
    
    def tuning_models(self) -> list:
        return [{
            "path": m.name,
            "version": m.version,
            "input_token_limit": m.input_token_limit,
            "output_token_limit": m.output_token_limit
        } 
            for m 
            in genai.list_models()
            if (
                "tuning" in m.name 
                and 
                "generateContent" in m.supported_generation_methods
            )
        ]
        
    def tuned_models(self) -> list:
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
        return genai.create_tuned_model(
            display_name=display_name,
            source_model=tuning_model,
            training_data=tuning_data,
            epoch_count=epoch_count,
            batch_size=batch_size,
            learning_rate=learning_rate
        ).result()
    
    def respond(
        self,
        prompt : str, 
        model_name : str,
        generation_config : dict, 
        safety_settings : dict, 
        tools : str, 
        system_instruction: list
    ) -> str:
        self._get(model_name, system_instruction)
        return self._get(
            model_name = model_name,
            system_instruction = system_instruction
        ).generate_content(
            contents = prompt,
            tools = tools,
            generation_config = generation_config,
            safety_settings = safety_settings
        ).text