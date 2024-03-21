Generative Video
---

This is a quick POC of generating a video from still images (Generative Images) and audio (text to speech api) with help of Gemini as the language model.

Requirements
---

1. Install ffmpeg
2. Install the python requirements
```bash
pip install -r requirements.txt
```
3. Gemini API
4. Google Imagen2 Access
5. Service Account with aiplatform.endpoints.predict permission
6. .env file
```
DS_GOOGLE_API_KEY=your-gemini-api-key
DS_PROJECT_ID=your-project-id
DS_LOCATION=us-central1
```

How to run
---

1. Export the GOOGLE_APPLICATION_CREDENTIALS
2. Run below command
```bash
streamlit run app.py
```

