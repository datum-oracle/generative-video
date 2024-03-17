import vertexai
from generative_video import generative_ai


class Imagen:
    def __init__(self) -> None:
        self.model = generative_ai.google_imagen()

    def generate_content(
        self, prompt: str
    ) -> vertexai.preview.vision_models.ImageGenerationResponse:
        images = self.model.generate_images(
            negative_prompt="Images must not include text in any language other than English",
            prompt=prompt,
            language="en",
            guidance_scale=12,
            seed=1,
            number_of_images=1,
        )
        return images
