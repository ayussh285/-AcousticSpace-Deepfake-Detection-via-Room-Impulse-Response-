import streamlit as st


# ----------------------------
# Header
# ----------------------------

def show_header(title, subtitle):

    st.markdown(
        f"""
        <div class="main-title">{title}</div>
        <div class="sub-title">{subtitle}</div>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------
# Prediction Card
# ----------------------------

def show_prediction(result):

    prediction = result["prediction"]

    if prediction == "Real":
        card_class = "real-card"
        icon = "🟢"
    else:
        card_class = "fake-card"
        icon = "🔴"

    st.markdown(
        f"""
        <div class="{card_class}">
            <h2>{icon} {prediction}</h2>
            <h4>Confidence : {result["confidence"]*100:.2f}%</h4>
            <p>{result["confidence_level"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------
# Confidence Bar
# ----------------------------

def show_confidence(result):

    st.markdown("### Confidence")

    st.progress(float(result["confidence"]))

    st.write(f"**{result['confidence']*100:.2f}%**")


# ----------------------------
# Audio Information
# ----------------------------

def show_audio_information(uploaded_file, result):

    st.markdown("### Audio Information")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="card">
            <div class="metric-title">File Name</div>
            <div class="metric-value">{uploaded_file.name}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="card">
            <div class="metric-title">Duration</div>
            <div class="metric-value">{result["duration"]:.2f} sec</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            f"""
            <div class="card">
            <div class="metric-title">Sampling Rate</div>
            <div class="metric-value">{result["sampling_rate"]} Hz</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="card">
            <div class="metric-title">Model</div>
            <div class="metric-value">{result["model"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ----------------------------
# Footer
# ----------------------------

def show_footer():

    st.markdown(
        """
        <div class="footer">
        AcousticAI © 2026 | Deepfake Audio Detection using Machine Learning
        </div>
        """,
        unsafe_allow_html=True,
    )