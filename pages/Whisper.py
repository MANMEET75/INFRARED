import streamlit as st
import whisper
from pytube import YouTube
from htmlTemplates import *
import datetime
import PyPDF2
import os
from fpdf import FPDF

# Set up Streamlit page config
st.set_page_config(
    page_title="Whisper",
    page_icon="https://revoquant.com/assets/img/logo/logo-dark.png"
)
st.write(css, unsafe_allow_html=True)

# Load the Whisper ASR model
model = whisper.load_model('tiny')
st.title("Video to Text Transcription with Whisper")

# Sidebar to select upload option
st.sidebar.header("Upload Option")
upload_option = st.sidebar.radio("Select upload option:", ("Upload Audio", "Upload MP4", "YouTube URL"))

if upload_option == "Upload Audio":
    uploaded_file = st.sidebar.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])
    transcribe_button = st.sidebar.button("Transcribe")

elif upload_option == "Upload MP4":
    uploaded_file = st.sidebar.file_uploader("Upload an MP4 file", type=["mp4"])
    transcribe_button = st.sidebar.button("Transcribe")

elif upload_option == "YouTube URL":
    youtube_url = st.sidebar.text_input("Enter YouTube Video URL:")
    transcribe_button = st.sidebar.button("Transcribe")

# Main content area
if transcribe_button:
    try:
        st.sidebar.info("Fetching audio stream...")
        if upload_option == "Upload Audio":
            audio_filename = "uploaded_audio.mp3"
            with open(audio_filename, "wb") as f:
                f.write(uploaded_file.read())
        elif upload_option == "Upload MP4":
            audio_filename = "uploaded_video.mp4"
            with open(audio_filename, "wb") as f:
                f.write(uploaded_file.read())
        elif upload_option == "YouTube URL":
            st.sidebar.info("Fetching video information...")
            youtube_video = YouTube(youtube_url)
            video_title = youtube_video.title
            st.sidebar.success(f"Video fetched: {video_title}")

            st.sidebar.info("Fetching audio stream...")
            streams = youtube_video.streams.filter(only_audio=True)
            audio_stream = streams.first()
            st.sidebar.success("Audio stream fetched")

            st.sidebar.info("Downloading audio...")
            audio_filename = f"{video_title}.mp4"
            audio_stream.download(filename=audio_filename)
            st.sidebar.success("Audio downloaded")

        st.sidebar.info("Starting transcription...")
        t1 = datetime.datetime.now()
        output = model.transcribe(audio_filename)
        t2 = datetime.datetime.now()
        st.sidebar.success(f"Transcription complete (time elapsed: {t2 - t1})")

        st.sidebar.info("Displaying transcription results:")

        st.write(output['text'])


        

         # Create and save a PDF file with the transcription using fpdf
        pdf_filename = 'transcription_output.pdf'
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, output['text'])
        pdf.output(pdf_filename)
        st.sidebar.info("PDF file generated and saved.")

        # Add a download button for the PDF file
        if os.path.exists(pdf_filename):
            with open(pdf_filename, 'rb') as file:
                st.sidebar.download_button("Download Transcription PDF", file.read(), file_name='transcription_output.pdf')

   


     







    except Exception as e:
        st.sidebar.error(f"An error occurred: {str(e)}")


