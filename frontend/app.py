import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import tempfile

from config import APP_TITLE, APP_SUBTITLE
from api import predict_audio
from styles import load_css
from components import (
    show_header,
    show_prediction,
    show_confidence,
    show_audio_information,
    show_footer
)

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🎵",
    layout="wide"
)

load_css()

show_header(APP_TITLE, APP_SUBTITLE)

# -------------------------------------------------------
# Upload Section
# -------------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3", "flac"]
)

if uploaded_file:

    st.markdown("---")

    col1, col2 = st.columns([1, 1])

    # ---------------------------------------------------
    # Left Side
    # ---------------------------------------------------

    with col1:

        st.subheader("🎵 Audio Preview")

        st.audio(uploaded_file)

        analyze = st.button(
            "🔍 Analyze Audio",
            use_container_width=True
        )

    # ---------------------------------------------------
    # Right Side
    # ---------------------------------------------------

    with col2:

        st.subheader("📈 Waveform")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:

            tmp.write(uploaded_file.getbuffer())

            temp_path = tmp.name

        signal, sr = librosa.load(temp_path, sr=16000)

        fig, ax = plt.subplots(figsize=(8, 3))

        librosa.display.waveshow(
            signal,
            sr=sr,
            ax=ax
        )

        ax.set_xlabel("Time")

        ax.set_ylabel("Amplitude")

        st.pyplot(fig)

    # ---------------------------------------------------
    # Prediction
    # ---------------------------------------------------

    if analyze:

        with st.spinner("Analyzing audio..."):

            success, response = predict_audio(uploaded_file)

        if success:

            result = response["data"]

            st.markdown("---")

            show_prediction(result)

            st.write("")

            show_confidence(result)

            st.write("")

            show_audio_information(uploaded_file, result)

        else:

            st.error(response)

show_footer()