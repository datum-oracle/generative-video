from functools import cache
from generative_video.config import settings
import google.generativeai as genai
import logging


@cache
def google_gemini(
    model_name="models/gemini-1.0-pro-latest", **kwargs
) -> genai.GenerativeModel:
    logging.info("Initialising Gemini....")
    genai.configure(api_key=settings.GOOGLE_API_KEY.get_secret_value())
    model = genai.GenerativeModel(model_name=model_name, **kwargs)
    return model
