import streamlit as st


def load_css():
    st.markdown(
        """
<style>

/* ----------------------------
   Hide Streamlit Default UI
----------------------------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ----------------------------
   Main Page
----------------------------- */

.stApp{
    background:#0f172a;
    color:white;
}

/* ----------------------------
   Title
----------------------------- */

.main-title{
    text-align:center;
    font-size:46px;
    font-weight:700;
    color:white;
    margin-top:10px;
    margin-bottom:0px;
}

.sub-title{
    text-align:center;
    font-size:18px;
    color:#94a3b8;
    margin-bottom:35px;
}

/* ----------------------------
   Cards
----------------------------- */

.card{
    background:#1e293b;
    padding:22px;
    border-radius:18px;
    border:1px solid #334155;
    box-shadow:0px 5px 18px rgba(0,0,0,.35);
    margin-top:20px;
}

/* ----------------------------
   Prediction Cards
----------------------------- */

.real-card{
    background:#14532d;
    padding:20px;
    border-radius:16px;
    text-align:center;
    color:white;
}

.fake-card{
    background:#7f1d1d;
    padding:20px;
    border-radius:16px;
    text-align:center;
    color:white;
}

/* ----------------------------
   Buttons
----------------------------- */

.stButton>button{

    width:100%;

    height:55px;

    border:none;

    border-radius:12px;

    background:#2563eb;

    color:white;

    font-size:18px;

    font-weight:600;

    transition:.3s;
}

.stButton>button:hover{

    background:#1d4ed8;

    transform:scale(1.02);

}

/* ----------------------------
   File Uploader
----------------------------- */

[data-testid="stFileUploader"]{

    background:#1e293b;

    border-radius:15px;

    padding:12px;

}

/* ----------------------------
   Metrics
----------------------------- */

.metric-title{

    color:#94a3b8;

    font-size:15px;

}

.metric-value{

    font-size:23px;

    font-weight:700;

    color:white;

}

/* ----------------------------
   Footer
----------------------------- */

.footer{

    text-align:center;

    color:#64748b;

    font-size:13px;

    margin-top:40px;

}

</style>
""",
        unsafe_allow_html=True,
    )