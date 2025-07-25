import streamlit as st
from helpers.news_scraper import get_trending_headlines
from helpers.script_generator import generate_script
from helpers.video_maker import generate_text_video
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'helpers')))


st.set_page_config(page_title="AI Video Generator", layout="centered")
st.title("AI Video Generation Tool")

if st.button("Get Trending News"):
    headlines = get_trending_headlines()
    st.session_state['headlines'] = headlines
    st.write("### Trending Topics")
    for i, h in enumerate(headlines):
        st.markdown(f"**{i+1}.** {h}")

if 'headlines' in st.session_state:
    selected = st.selectbox("Select a Topic", st.session_state['headlines'])
    if st.button("Generate Script"):
        script = generate_script(selected)
        with open("output/script.txt", "w") as f:
            f.write(script)
        st.success("Script generated!")
        st.text_area("Script Preview", script, height=200)

        if st.button("Create Video"):
            script_lines = [line.strip() for line in script.split('.') if line.strip()]
            generate_text_video(script_lines, "output/video.mp4")
            st.success("Video created!")
            st.video("output/video.mp4")
