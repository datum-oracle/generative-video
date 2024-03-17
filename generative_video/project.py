import pathlib
import json
import logging
from generative_video.models import ProjectRequest, PromptResponseModel
from generative_video.ideation import Ideation
from generative_video.narration import Narration
from generative_video.imagen import Imagen
from generative_video.audio import Audio
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


class Project:
    def __init__(self, project_request: ProjectRequest) -> None:
        self.project_request = project_request
        self._setup()

    def _setup(self):
        (pathlib.Path("projects") / self.project_request.project_name).mkdir(
            exist_ok=True, parents=True
        )

    def generate_idea(self):
        ideation_response = Ideation(
            initial_idea=self.project_request.initial_idea,
            target_audience_persona=self.project_request.target_audience_persona,
        ).generate_content()
        pathlib.Path(
            f"projects/{self.project_request.project_name}/ideation.json"
        ).write_text(ideation_response.model_dump_json())
        logging.info("Ideation phase complete")
        return self

    def generate_script(self):
        ideation_response = PromptResponseModel.model_validate_json(
            pathlib.Path(
                f"projects/{self.project_request.project_name}/ideation.json"
            ).read_text()
        )
        naration_response = Narration(
            source_material=ideation_response.generate_content_response
        ).generate_content()
        pathlib.Path(
            f"projects/{self.project_request.project_name}/narration.json"
        ).write_text(naration_response.model_dump_json())
        logging.info("Narration phase complete")
        return self

    def generate_image_files(self):
        narration_response = PromptResponseModel.model_validate_json(
            pathlib.Path(
                f"projects/{self.project_request.project_name}/narration.json"
            ).read_text()
        )
        scenes = json.loads(narration_response.generate_content_response)
        imagen = Imagen()
        image_folder = pathlib.Path(
            f"projects/{self.project_request.project_name}/images"
        )
        image_folder.mkdir(exist_ok=True, parents=True)
        for i, scene in enumerate(scenes, start=1):
            images = imagen.generate_content(scene["image_description"])
            for image in images:
                image_path = image_folder / f"{i}.jpg"
                image.save(location=str(image_path), include_generation_parameters=True)
                logging.info(f'Image content written to file "{image_path}"')
        return self

    def generate_audio_files(self):
        narration_response = PromptResponseModel.model_validate_json(
            pathlib.Path(
                f"projects/{self.project_request.project_name}/narration.json"
            ).read_text()
        )
        scenes = json.loads(narration_response.generate_content_response)
        audio = Audio()
        audio_folder = pathlib.Path(
            f"projects/{self.project_request.project_name}/audio"
        )
        audio_folder.mkdir(exist_ok=True, parents=True)
        for i, scene in enumerate(scenes, start=1):
            audio_response = audio.generate_content(scene["narration"])
            audio_path = audio_folder / f"{i}.mp3"
            with open(audio_path, "wb") as out:
                out.write(audio_response.audio_content)
                logging.info(f'Audio content written to file "{audio_path}"')

    def generate_video(self):
        clips = []
        for i in range(1, 7):
            audio_clip = AudioFileClip(
                f"projects/{self.project_request.project_name}/audio/{i}.mp3"
            )
            image_clip = ImageClip(
                f"projects/{self.project_request.project_name}/images/{i}.jpg"
            ).set_duration(audio_clip.duration + 2)
            image_clip = image_clip.set_audio(audio_clip)
            clips.append(image_clip.crossfadein(2))
        concat_clip = concatenate_videoclips(clips, method="compose", padding=-2)
        concat_clip.write_videofile(
            f"projects/{self.project_request.project_name}/{self.project_request.project_name}.mp4",
            fps=30,
        )
        return f"projects/{self.project_request.project_name}/{self.project_request.project_name}.mp4"
