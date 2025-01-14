""" # model.py
Wrapper around Google's GenerativeAI library. Provides configuration and default settings.
"""
import conf 

import google.generativeai as genai

genai.configure(api_key=conf.API_KEY)

def _model(model_type=conf.DEFAULTS["MODEL"]):
    return genai.GenerativeModel(model_type)

def reply(prompt, model_type=conf.DEFAULTS["MODEL"]):
    return _model(model_type).generate_content(prompt).text