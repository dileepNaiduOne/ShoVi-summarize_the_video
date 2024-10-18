import giveSummary
import streamlit as st

# st.set_page_config(layout="wide")

##########################################################################################

st.components.v1.html(
    """
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.32/build/spline-viewer.js"></script>
    <spline-viewer url="https://prod.spline.design/4lVGPqOvqbo2ky9O/scene.splinecode"></spline-viewer>
    """, height=400
)

##########################################################################################
st.header("Enter your :red[Assembly AI API Key :]")
aai_api_key = st.text_input(" ", type='password')

with st.expander(":red-background[Don't have API Key]...Click here to get it for, FREE!"):
    st.write(f"""
    1. Go to Assmeble AI Website https://www.assemblyai.com/dashboard/signup
    2. Signup with your mail and password. Don't want to give your mail,
            use https://temp-mail.org/en/ and get a temporary disposable
            email. And use that!
    3. Now you will be seeing "Welcome to AssemblyAI". On screen there will a variable like
            "aai.settings.api_key = "8b8a**y***43**8rgh*********e*****e817".
            This long alphanumeric word is you api_key.
    4. Now copy and paste this api_key in the ShoVi's homepage.
    """)

##########################################################################################

st.write("")
st.header("", divider="gray")
st.write("")
st.write("")

##########################################################################################
st.header(":red[Upload an audio file : ]")
uploaded_audio_file = st.file_uploader(" ", type=["mp3"])  

##########################################################################################

st.write("")
st.header("", divider="gray")
st.write("")
# st.button("Start ShoViazaa...", on_click=start_summary, type="primary", use_container_width=True)

##########################################################################################

if uploaded_audio_file and aai_api_key:
    st.header(":red[Summary]")
    got_text = giveSummary.change_audio_to_text(
        uploaded_audio_file, 
        aai_api_key
        )

    with st.expander(":red-background[Click here to read the transcript] of your audio file"):
        st.write(got_text)

    
    models_summary = giveSummary.do_summarize(got_text)

    st.write(models_summary)
