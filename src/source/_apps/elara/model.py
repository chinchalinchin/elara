""" # model.py
Wrapper around Google's GenerativeAI library. Provides configuration and default settings.
"""

import os
import google.generativeai as genai

API_KEY = os.environ.get("GEMINI_KEY")
DEFAULT_MODEL = os.environ.setdefault("GEMINI_MODEL", "gemini-1.5-pro")

if API_KEY is None:
    raise ValueError("GEMINI_KEY environment variable not set.")

genai.configure(api_key=API_KEY)

def _model(model_type=DEFAULT_MODEL):
    return genai.GenerativeModel(model_type)

def reply(prompt, model_type=DEFAULT_MODEL):
    return _model(model_type).generate_content(prompt).text