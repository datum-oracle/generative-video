import pathlib
from generative_video.models import ProjectRequest


class Project:
    def __init__(self, project_request: ProjectRequest) -> None:
        self.project_request = project_request
        self._setup()

    def _setup(self):
        (pathlib.Path("projects") / self.project_request.project_name).mkdir(
            exist_ok=True, parents=True
        )

    def generate_idea(self):
        pass

    def generate_script(self):
        pass

    def generate_image(self):
        pass

    def generate_audio(self):
        pass

    def generate_video(self):
        pass
