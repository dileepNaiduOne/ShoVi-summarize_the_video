import giveSummary
import streamlit as st



st.title("ShoVi - Shorten the Video")

st.components.v1.html(
    """
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.32/build/spline-viewer.js"></script>
    <spline-viewer url="https://prod.spline.design/4lVGPqOvqbo2ky9O/scene.splinecode"></spline-viewer>
    """, height=400
)

uploaded_audio_file = st.file_uploader("Upload an audio file", type=["mp3"])
aai_api_key = "c323ab05a7bc4302ac1246aaec21416c"

got_text = giveSummary.change_audio_to_text(
    uploaded_audio_file, 
    aai_api_key
    )

models_summary = giveSummary.do_summarize(got_text)

st.write(models_summary)