import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* ==============================
           GLOBAL
        ============================== */

        .stApp {
            background:
                radial-gradient(
                    circle at 50% 0%,
                    rgba(37, 99, 235, 0.12),
                    transparent 35%
                ),
                #0b1220;
            color: #f8fafc;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        #MainMenu {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }


        /* ==============================
           HEADER
        ============================== */

        .brand-badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 999px;
            background: rgba(37, 99, 235, 0.12);
            border: 1px solid rgba(96, 165, 250, 0.25);
            color: #60a5fa;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.4px;
            margin-bottom: 14px;
        }

        .main-title {
            text-align: center;
            font-size: 48px;
            line-height: 1.1;
            font-weight: 800;
            letter-spacing: -1.5px;
            color: #f8fafc;
            margin: 0;
        }

        .sub-title {
            text-align: center;
            color: #94a3b8;
            font-size: 17px;
            margin-top: 12px;
            margin-bottom: 34px;
        }


        /* ==============================
           SECTION TITLES
        ============================== */

        .section-title {
            color: #f8fafc;
            font-size: 21px;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .section-description {
            color: #94a3b8;
            font-size: 14px;
            margin-bottom: 16px;
        }


        /* ==============================
           UPLOAD CARD
        ============================== */

        .upload-card {
            background: rgba(30, 41, 59, 0.82);
            border: 1px solid #334155;
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.25);
        }

        .upload-info {
            color: #64748b;
            font-size: 13px;
            margin-top: 8px;
        }

        [data-testid="stFileUploader"] {
            background: rgba(15, 23, 42, 0.65);
            border: 1px dashed #475569;
            border-radius: 14px;
            padding: 10px;
        }


        /* ==============================
           GENERAL CARD
        ============================== */

        .card {
            background: rgba(30, 41, 59, 0.82);
            border: 1px solid #334155;
            border-radius: 18px;
            padding: 20px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.20);
        }


        /* ==============================
           AUDIO AREA
        ============================== */

        .audio-card {
            background: rgba(30, 41, 59, 0.70);
            border: 1px solid #334155;
            border-radius: 18px;
            padding: 20px;
        }


        /* ==============================
           BUTTON
        ============================== */

        .stButton > button {
            width: 100%;
            height: 52px;
            border: none;
            border-radius: 12px;
            background: linear-gradient(
                135deg,
                #2563eb,
                #3b82f6
            );
            color: white;
            font-size: 16px;
            font-weight: 700;
            transition: all 0.2s ease;
            box-shadow: 0 7px 20px rgba(37, 99, 235, 0.25);
        }

        .stButton > button:hover {
            background: linear-gradient(
                135deg,
                #1d4ed8,
                #2563eb
            );
            transform: translateY(-1px);
            box-shadow: 0 10px 25px rgba(37, 99, 235, 0.35);
        }


        /* ==============================
           RESULT CARDS
        ============================== */

        .real-card {
            background:
                linear-gradient(
                    135deg,
                    rgba(22, 101, 52, 0.95),
                    rgba(20, 83, 45, 0.85)
                );
            border: 1px solid rgba(74, 222, 128, 0.25);
            border-radius: 20px;
            padding: 28px;
            text-align: center;
            box-shadow: 0 12px 30px rgba(22, 101, 52, 0.18);
        }

        .fake-card {
            background:
                linear-gradient(
                    135deg,
                    rgba(127, 29, 29, 0.95),
                    rgba(153, 27, 27, 0.82)
                );
            border: 1px solid rgba(248, 113, 113, 0.25);
            border-radius: 20px;
            padding: 28px;
            text-align: center;
            box-shadow: 0 12px 30px rgba(127, 29, 29, 0.18);
        }

        .prediction-label {
            color: rgba(255, 255, 255, 0.70);
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }

        .prediction-value {
            color: white;
            font-size: 36px;
            font-weight: 800;
            margin: 6px 0;
        }

        .prediction-confidence {
            color: rgba(255, 255, 255, 0.88);
            font-size: 16px;
        }

        .confidence-level {
            color: rgba(255, 255, 255, 0.70);
            font-size: 14px;
            margin-top: 5px;
        }


        /* ==============================
           METRIC CARDS
        ============================== */

        .metric-card {
            background: rgba(30, 41, 59, 0.82);
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 18px 20px;
            min-height: 90px;
        }

        .metric-title {
            color: #94a3b8;
            font-size: 13px;
            margin-bottom: 7px;
        }

        .metric-value {
            color: #f8fafc;
            font-size: 19px;
            font-weight: 700;
            word-break: break-word;
        }


        /* ==============================
           INFO / DISCLAIMER
        ============================== */

        .info-box {
            background: rgba(15, 23, 42, 0.60);
            border: 1px solid #334155;
            border-left: 3px solid #3b82f6;
            border-radius: 12px;
            padding: 14px 16px;
            color: #94a3b8;
            font-size: 13px;
            line-height: 1.6;
            margin-top: 22px;
        }


        /* ==============================
           DIVIDER
        ============================== */

        .custom-divider {
            height: 1px;
            background: #263449;
            margin: 30px 0;
        }


        /* ==============================
           FOOTER
        ============================== */

        .footer {
            text-align: center;
            color: #64748b;
            font-size: 12px;
            margin-top: 42px;
            padding-top: 18px;
            border-top: 1px solid #1e293b;
        }


        /* ==============================
           STREAMLIT PROGRESS BAR
        ============================== */

        [data-testid="stProgressBar"] {
            margin-top: 8px;
            margin-bottom: 4px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )