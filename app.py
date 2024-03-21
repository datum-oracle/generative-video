import sys
import logging
from generative_video.project import Project
from generative_video.models import ProjectRequest

import streamlit as st
from streamlit_tags import st_tags

logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout)], level=logging.INFO)


def create_video(project_name, initial_idea, target_audience):
    project = Project(
        project_request=ProjectRequest(
            project_name=project_name,
            initial_idea=initial_idea,
            target_audience_persona=target_audience,
        )
    )
    with st.spinner("Expanding Idea"):
        project.generate_idea()
    with st.spinner("Writing Script"):
        project.generate_script()
    with st.spinner("Generating Images"):
        project.generate_image_files()
    with st.spinner("Adding Narration Audios"):
        project.generate_audio_files()
    with st.spinner("Creating Video"):
        video = project.generate_video()
    st.success("Video Generated 🔥")
    return video


with st.form(key="ProjectForm"):
    project_name = st.text_input(label="Enter Project Name")
    initial_idea = st.text_area(label="What's your initial idea")
    target_audience = st_tags(
        label="Target Audience:", text="Press enter to add more", maxtags=4, key="1"
    )
    submit = st.form_submit_button(label="Create Video")
    if submit:
        video = create_video(project_name, initial_idea, target_audience)
        st.video(video)
