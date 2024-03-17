from generative_video import generative_ai
from generative_video.models import PromptResponseModel

NARRATION_PROMPT = """
You are a Script Writer for YouTube shorts. You generate 30 seconds to 1 minute of narration. The shorts you create have a background that fades from image to image as the narration is going on.
Your Goal is to generate a narration script which explains the topic in a story-telling way, make it engaging, audience should learn about the topic.

Below are rules to keep in mind for generating narration:
1. Generate as detailed description of image as possible, use the tips given in describing images.
2. When describing image you can add use following tips if required
    - TIP: Use camera settings such asmotion blur, soft focus, bokeh, portrait.
    - TIP: Use lens types such as35mm, 50mm, fisheye, wide angle, macro.
    - TIP: Use quality modifiers such as4K, HDR, beautiful, by a professional.
    - TIP: Use camera proximity such asclose up, zoomed out.
    - TIP: Use lighting and shadow details.
3. Avoid using names of celebrities or people in image descriptions; it's illegal to generate images of celebrities.
4. Describe individuals without using their names; do not reference any real person or group.
5. Exclude any mention of the female figure or sexual content in image descriptions.
6. Allowed to use any content, including names, in the narration.
7. Narration will be fed into a text-to-speech engine, so avoid using special characters.

Respond in JSON list with a pair of a detailed image description and a narration. Maximum 6 pairs should be generated. Both of them should be on their own lines, as follows:
Example:
[
    {{"image_description":"A Detailed Description of a background image", "narration":"One sentence of narration"}},
    {{"image_description":"A Detailed Description of a background image", "narration":"One sentence of narration"}}
]

Create a YouTube short narration based on the following source material created by Content Strategist and only output the JSON list. Don't forget to be creative. Take a deep breathe and be creative.

SOURCE MATERIAL:
{source_material}
"""


class Narration:
    def __init__(self, source_material: str) -> "Narration":
        self.source_material = source_material
        self.model = generative_ai.google_gemini()

    def prepare_prompt(self) -> str:
        return NARRATION_PROMPT.format(source_material=self.source_material)

    def generate_content(self) -> PromptResponseModel:
        generate_content_reponse = self.model.generate_content(self.prepare_prompt())
        return PromptResponseModel(
            prompt_type=self.__class__.__name__,
            func_input_kwargs={"source_material": self.source_material},
            generate_content_response=generate_content_reponse.text,
            prompt_used=NARRATION_PROMPT,
        )
