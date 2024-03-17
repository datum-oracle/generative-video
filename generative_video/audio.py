from google.cloud import texttospeech
from google.cloud.texttospeech_v1.types import cloud_tts


class Audio:
    def __init__(self) -> None:
        self.client = texttospeech.TextToSpeechClient()

    def generate_content(self, narration) -> cloud_tts.SynthesizeSpeechResponse:
        input_text = texttospeech.SynthesisInput(text=narration)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Studio-O",
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16, speaking_rate=1
        )
        response = self.client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )
        return response
