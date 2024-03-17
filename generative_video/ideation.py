from generative_video import generative_ai
from generative_video.models import PromptResponseModel

IDEATION_PROMPT = """
You are a Content Strategist. Here's what you do,
- You generate creative and engaging ideas for YouTube Shorts content.
- You brainstorm and expand content ideas. 
- You analyze content quality and whether your content reflects what's most important to your audience. Then, use that information to inform which direction you take next.
- Create Creative and Newsworthy content.
- Come up with the idea of; what should be the Audience Hook?

Utilizing your ideas, you produce text that provides essential information for a scriptwriter to grasp topics, concepts, and ideas. This aids the scriptwriter in creating a compelling narration script.

Now, you are provided with initial idea and with target audience persona. Take a deep breath and show your magic as a Content Strategist.
INITITAL IDEA: {initial_idea}
TARGET AUDIENCE PERSONA:{target_audience_persona}
"""


class Ideation:
    def __init__(
        self, initial_idea: str, target_audience_persona: list[str]
    ) -> "Ideation":
        self.initial_idea = initial_idea
        self.target_audience_persona = target_audience_persona
        self.model = generative_ai.google_gemini()

    def prepare_prompt(self) -> str:
        return IDEATION_PROMPT.format(
            initial_idea=self.initial_idea,
            target_audience_persona=",".join(self.target_audience_persona),
        )

    def generate_content(self) -> PromptResponseModel:
        generate_content_reponse = self.model.generate_content(self.prepare_prompt())
        return PromptResponseModel(
            prompt_type=self.__class__.__name__,
            func_input_kwargs={
                "initial_idea": self.initial_idea,
                "target_audience_persona": ",".join(self.target_audience_persona),
            },
            generate_content_response=generate_content_reponse.text,
            prompt_used=IDEATION_PROMPT,
        )
