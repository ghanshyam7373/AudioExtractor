import moviepy.editor
import streamlit as st

# Method to extract Audio from Video 
def audioFile(vid):
    video = moviepy.editor.VideoFileClip(vid)
    audio = video.audio
    audio.write_audiofile("extractedAudio.mp3")

# UI Code using streamlit 
st.title("Extract Audio From Video")
uploaded_file = st.file_uploader("Choose a video file", type=['mp4'])
if uploaded_file is not None:
    file_name = uploaded_file.name
    with open('InputVideo.mp4', 'wb') as f:
        f.write(uploaded_file.read())

    vid = 'InputVideo.mp4'
    audioFile(vid)
    st.title("Extracted Audio")
    audio_file = open('extractedAudio.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)