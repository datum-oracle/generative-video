from generative_video import llm
from generative_video.models import PromptResponseModel

NARRATION_PROMPT = """
You are a Script Writer for YouTube shorts. You generate 30 seconds to 1 minute of narration. The shorts you create have a background that fades from image to image as the narration is going on.
Your Goal is to generate a narration script which explains the topic in a story-telling way.

Below are rules to keep in mind for generating narration:
- Generate detailed descriptions for each image in the short.Image Descriptions will be used for an AI image generator. 
- When you describe image be consistent on theme of the images. You can even mention lighting and shadow details objects in image.
- Avoid using names of celebrities or people in image descriptions; it's illegal to generate images of celebrities.
- Describe individuals without using their names; do not reference any real person or group.
- Exclude any mention of the female figure or sexual content in image descriptions.
- Allowed to use any content, including names, in the narration.
- Narration will be fed into a text-to-speech engine, so avoid using special characters.


Respond in JSON list with a pair of an image description in and a narration. Maximum 6 pairs should be generated. Both of them should be on their own lines, as follows:
Example:
[
    {{"image_description":"Description of a background image", "narrotor":"One sentence of narration"}},
    {{"image_description":"Description of a background image", "narrotor":"One sentence of narration"}},
]

Create a YouTube short narration based on the following source material created by Content Strategist and only output the JSON list. Don't forget to be creative. Take a deep breathe and be creative.

SOURCE MATERIAL:
{source_material}
"""


class Narration:
    def __init__(self, source_material: str) -> "Narration":
        self.source_material = source_material
        self.model = llm.google_gemini()

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
