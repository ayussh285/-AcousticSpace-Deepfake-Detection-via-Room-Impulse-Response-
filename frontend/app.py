import os
import tempfile

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import streamlit as st

from config import APP_TITLE, APP_SUBTITLE
from api import predict_audio
from styles import load_css

from components import (
    show_header,
    show_upload_header,
    show_prediction,
    show_confidence,
    show_audio_information,
    show_disclaimer,
    show_footer,
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AcousticAI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()


# =========================================================
# HEADER
# =========================================================

show_header(
    APP_TITLE,
    APP_SUBTITLE
)


# =========================================================
# UPLOAD SECTION
# =========================================================

show_upload_header()

uploaded_file = st.file_uploader(
    "Choose an audio file",
    type=["wav", "mp3", "flac"],
    label_visibility="collapsed",
)

st.html(
    """
    <div class="upload-info">
        Supported formats: WAV, MP3, FLAC
        &nbsp;•&nbsp;
        Recommended duration: 1–300 seconds
    </div>
    """
)


# =========================================================
# EMPTY STATE
# =========================================================

if uploaded_file is None:

    st.html(
        """
        <div style="
            text-align:center;
            padding:55px 20px 35px 20px;
            color:#64748b;
        ">

            <div style="
                font-size:48px;
                margin-bottom:12px;
            ">
                🎙️
            </div>

            <div style="
                font-size:20px;
                font-weight:700;
                color:#cbd5e1;
            ">
                Ready to analyze audio
            </div>

            <div style="
                font-size:14px;
                margin-top:8px;
            ">
                Upload an audio recording above to begin.
            </div>

        </div>
        """
    )

    show_footer()

    st.stop()


# =========================================================
# TEMPORARY FILE
# =========================================================

file_extension = os.path.splitext(
    uploaded_file.name
)[1]

temp_file = tempfile.NamedTemporaryFile(
    delete=False,
    suffix=file_extension
)

temp_file.write(
    uploaded_file.getbuffer()
)

temp_file.close()

temp_path = temp_file.name


try:

    # =====================================================
    # LOAD AUDIO
    # =====================================================

    audio_signal, sampling_rate = librosa.load(
        temp_path,
        sr=16000,
        mono=True
    )

    duration = librosa.get_duration(
        y=audio_signal,
        sr=sampling_rate
    )


    # =====================================================
    # AUDIO + WAVEFORM
    # =====================================================

    st.divider()

    preview_col, waveform_col = st.columns(
        [0.9, 1.1],
        gap="large"
    )


    # -----------------------------------------------------
    # AUDIO PREVIEW
    # -----------------------------------------------------

    with preview_col:

        st.html(
            """
            <div class="section-title">
                🎧 Audio Preview
            </div>
            """
        )

        st.html(
            f"""
            <div class="section-description">
                {uploaded_file.name}
                &nbsp;•&nbsp;
                {duration:.2f} seconds
            </div>
            """
        )

        st.audio(
            uploaded_file.getvalue(),
            format=uploaded_file.type
        )

        st.write("")

        analyze = st.button(
            "🔍  Analyze Audio",
            use_container_width=True
        )


    # -----------------------------------------------------
    # WAVEFORM
    # -----------------------------------------------------

    with waveform_col:

        st.html(
            """
            <div class="section-title">
                〽️ Waveform
            </div>
            """
        )

        st.html(
            """
            <div class="section-description">
                Time-domain representation of the uploaded signal.
            </div>
            """
        )

        fig, ax = plt.subplots(
            figsize=(8, 3.2)
        )

        fig.patch.set_facecolor("#0b1220")
        ax.set_facecolor("#0b1220")

        librosa.display.waveshow(
            audio_signal,
            sr=sampling_rate,
            ax=ax,
            color="#60a5fa"
        )

        ax.set_xlabel(
            "Time (seconds)",
            color="#cbd5e1"
        )

        ax.set_ylabel(
            "Amplitude",
            color="#cbd5e1"
        )

        ax.tick_params(
            colors="#94a3b8"
        )

        for spine in ax.spines.values():
            spine.set_color("#334155")

        fig.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


    # =====================================================
    # MEL SPECTROGRAM
    # =====================================================

    st.divider()

    st.html(
        """
        <div class="section-title">
            🎛️ Mel Spectrogram
        </div>
        """
    )

    st.html(
        """
        <div class="section-description">
            Frequency representation of the audio signal used
            for acoustic analysis.
        </div>
        """
    )


    mel = librosa.feature.melspectrogram(
        y=audio_signal,
        sr=sampling_rate,
        n_mels=128
    )

    mel_db = librosa.power_to_db(
        mel,
        ref=np.max
    )


    fig, ax = plt.subplots(
        figsize=(12, 3.8)
    )

    fig.patch.set_facecolor("#0b1220")
    ax.set_facecolor("#0b1220")

    img = librosa.display.specshow(
        mel_db,
        sr=sampling_rate,
        x_axis="time",
        y_axis="mel",
        ax=ax,
        cmap="magma"
    )

    ax.set_xlabel(
        "Time",
        color="#cbd5e1"
    )

    ax.set_ylabel(
        "Frequency",
        color="#cbd5e1"
    )

    ax.tick_params(
        colors="#94a3b8"
    )

    for spine in ax.spines.values():
        spine.set_color("#334155")

    colorbar = fig.colorbar(
        img,
        ax=ax,
        format="%+2.0f dB"
    )

    colorbar.ax.tick_params(
        colors="#cbd5e1"
    )

    fig.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


    # =====================================================
    # MODEL ANALYSIS
    # =====================================================

    if analyze:

        st.divider()

        st.html(
            """
            <div class="section-title">
                🧠 Detection Result
            </div>
            """
        )

        with st.spinner(
            "Analyzing audio and running the detection model..."
        ):

            success, response = predict_audio(
                uploaded_file
            )


        if success:

            result = response.get("data")

            if result is None:

                st.error(
                    "The backend returned an invalid response."
                )

            else:

                show_prediction(result)

                show_confidence(result)

                show_audio_information(
                    uploaded_file,
                    result
                )

                show_disclaimer()

        else:

            st.error(
                f"Prediction failed: {response}"
            )


finally:

    # =====================================================
    # DELETE TEMPORARY FILE
    # =====================================================

    if os.path.exists(temp_path):

        os.remove(temp_path)


# =========================================================
# FOOTER
# =========================================================

show_footer()