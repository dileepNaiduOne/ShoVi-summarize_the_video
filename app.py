import giveSummary, extractTextfromPDF
import streamlit as st
from streamlit_option_menu import option_menu

# st.set_page_config(layout="wide")
st.set_page_config(page_title="■■ ShoVi", page_icon="logo.png")

# st.image("https://raw.githubusercontent.com/dileepNaiduOne/ShoVi-summarize_the_video/refs/heads/main/logo.png")
# page_bg_img = """
#     <style>
#         [data-testid="stMain"] 
#             {
#                 background-image: url("https://images.unsplash.com/photo-1728996152930-233c5aca21d7?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
#                 background-size: 180%;
#                 background-position: top left;
#                 background-repeat: no-repeat;
#                 background-attachment: local; 
#             }
#     </style>
# """
# st.html(page_bg_img)

##########################################################################################
# For Spline 3D Eleement 
st.components.v1.html(
    """
        <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.32/build/spline-viewer.js"></script>
        <spline-viewer url="https://prod.spline.design/VdI2sooy4f-DkOs4/scene.splinecode"></spline-viewer>
    """, height=400
)

##########################################################################################
# For Assemble AI API Key
st.header("Enter your :red[Assembly AI API Key] :")
aai_api_key = st.text_input(" ", type='password')


with st.expander(":red-background[Don't have API Key]...Click here to get it for, FREE!"):
    st.write(f"""
    1. Go to Assmeble AI Website https://www.assemblyai.com/dashboard/signup
    2. Signup with your mail and password. Don't want to give your mail,
            use https://temp-mail.org/en/ and get a temporary disposable
            email. And use that!
    3. Now you will be seeing "Welcome to AssemblyAI". On screen there will a variable like
            "aai.settings.api_key = "8b8a**y***43**8rgh*********e*****e817".
            This long alphanumeric word is your api_key.
    4. Now copy and paste this api_key in the above input box.
    """)

##########################################################################################

st.header("", divider="gray")

##########################################################################################

st.header(":red[Summarize]....")

selected = option_menu(
    menu_title = None,
    options = ["Audio/Video", "Text", "Youtube Link"],
    icons = ["camera-reels", "file-text", "youtube"],
    orientation="horizontal",
    default_index=0
)

##########################################################################################
##########################################################################################
if selected == "Audio/Video":
    file_formats_urls = r"https://www.assemblyai.com/docs/Concepts/faq"

    # Checking condition for inputs
    uploaded_audio_file = st.file_uploader(label = "Upload your :red[Audio/Video] File", type = [".mp3", ".mp4", ".wav"])
    if aai_api_key and not uploaded_audio_file:
        st.toast(body="API Key Uploaded", icon="👍") 
    if uploaded_audio_file and not aai_api_key:
        st.toast(body="Audio File Uploaded", icon="👍")

    #-----------------------------------------------------------------------------------------

    st.header("", divider="gray")
    # st.button("Start ShoViazaa...", on_click=start_summary, type="primary", use_container_width=True)

    #-----------------------------------------------------------------------------------------

    if uploaded_audio_file and aai_api_key:
        st.toast(body="Started Processing. Summary will be given soon", icon="🏋️‍♂️")
        # st.header(":red[Summary]")
        got_text = giveSummary.change_audio_to_text(
            uploaded_audio_file, 
            aai_api_key
            )
        
        models_summary = giveSummary.do_summarize(got_text)

        st.write(models_summary)
        if models_summary:
            st.toast(body="Summarized your File", icon="✅")
            with st.expander(":red-background[Click here to read the transcript] of your audio file"):
                st.write(got_text)
##########################################################################################
##########################################################################################
if selected == "Text":
    toggle_on = st.toggle(
        ":red[Manual Input]",
        help="Turn on for 'Text Input', turn off for 'PDF Upload'"
        )
    

    if toggle_on:
        got_text = st.text_area("Type/ Paste your :red[text] :")

        if aai_api_key and not got_text:
            st.toast(body="API Key Uploaded", icon="👍") 
        if got_text and not aai_api_key:
            st.toast(body="Text Uploaded", icon="👍")

#------------------------------------------------------------------------------------------------

        st.header("", divider="gray")

#------------------------------------------------------------------------------------------------

        if got_text and aai_api_key:
            st.toast(body="Started Processing. Summary will be given soon", icon="🏋️‍♂️")

            print(got_text)
            got_text = list(filter(lambda y : len(y)>0, list(map(lambda x : x.strip(), got_text.split(" ")))))[:20_00_000]
            print(got_text)

            words_count = len(got_text)
            print(words_count)

            got_text = " ".join(got_text)
            print(got_text)


            
            
            models_summary = giveSummary.do_summarize(got_text)

            st.write(models_summary)
            st.write(f"This summary is generated using :red[{words_count} words] from your input")

            if models_summary:
                st.toast(body="Summarized your File", icon="✅")
                with st.expander(":red-background[Click here to read the transcript] of your text"):
                    st.write(got_text)

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

    if not toggle_on:
        uploaded_text_file = st.file_uploader(label = "Upload your :red[PDF] File :", type = [".pdf"])

        if aai_api_key and not uploaded_text_file:
            st.toast(body="API Key Uploaded", icon="👍") 
        if uploaded_text_file and not aai_api_key:
            st.toast(body="PDF File Uploaded", icon="👍")

#------------------------------------------------------------------------------------------------

        st.header("", divider="gray")

#------------------------------------------------------------------------------------------------

        if uploaded_text_file and aai_api_key:
            st.toast(body="Started Processing. Summary will be given soon", icon="🏋️‍♂️")

            got_text, words_count = extractTextfromPDF.pullText(uploaded_text_file.read())

            models_summary = giveSummary.do_summarize(got_text)
            st.write(models_summary)
            st.write(f"This summary is generated using :red[{words_count} words] from your input")

            if models_summary:
                st.toast(body="Summarized your File", icon="✅")
                with st.expander(":red-background[Click here to read the transcript] of your PDF file"):
                    st.write(got_text)

