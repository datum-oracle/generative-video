from langchain_google_genai import GoogleGenerativeAI


def google_generative_ai(model="gemini-pro", **kwargs):
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=None, **kwargs)
    return llm
