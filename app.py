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
    # For Assemble AI API Key
    # st.header("Enter your :red[Assembly AI API Key] :")
    aai_api_key = st.text_input("Enter your :red[Assembly AI API Key] :", type='password')


    with st.expander(":red-background[Don't have API Key]...:red[Click here] to get it for, FREE!"):
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

    #-----------------------------------------------------------------------------------------

    st.write(" ")
    st.markdown("---")
    # st.header("", divider="gray")
    st.write(" ")

    #-----------------------------------------------------------------------------------------

    file_formats_urls = r"https://www.assemblyai.com/docs/Concepts/faq"

    # Checking condition for inputs

    uploaded_audio_file = st.file_uploader(label = "Upload your :red[Audio/Video] File :", type = [".mp3", ".mp4", ".wav"])
    st.write(" ")
    st.write(" ")
    st.write(" ")
    butt1 = st.button("ShoVizzaa", type='primary', use_container_width=True)

    
    if aai_api_key and not uploaded_audio_file:
        st.toast(body="API Key Uploaded", icon="👍")
    elif uploaded_audio_file and not aai_api_key:
        st.toast(body="File Uploaded", icon="👍")
    elif uploaded_audio_file and aai_api_key:
        st.toast(body="API Key & File Uploaded", icon="👍")

    #-----------------------------------------------------------------------------------------
    if butt1:

        if uploaded_audio_file and aai_api_key:

            st.write(" ")
            st.markdown("---")
            # st.header("", divider="gray")

            st.toast(body="Started Processing. Summary will be given :red[very soon]", icon="🏋️‍♂️")
            st.header(":red[ShoVizzaa]....")
            got_text = giveSummary.change_audio_to_text(
                uploaded_audio_file, 
                aai_api_key
                )
            
            models_summary = giveSummary.do_summarize(got_text)

            st.write(models_summary)
            st.write(f"This summary is generated using :red[{len(got_text.split(" "))} words] from your input")
            if models_summary:
                st.toast(body="Summarized your File", icon="✅")
                with st.expander(":red-background[Click here to read the transcript] of your audio file"):
                    st.write(got_text)

    st.write(" ")
    st.markdown("---")
    # st.header("", divider="gray")
    st.write(" ")
##########################################################################################
##########################################################################################
if selected == "Text":
    c1, c2, c3 = st.columns([0.38, 0.24, 0.38], vertical_alignment="center")

    with c2:
        st.write(" ")
        toggle_on = st.toggle(":red[Manual Input]")

    st.markdown("---")
    st.write(" ")
    if toggle_on:
        got_text = st.text_area("Type/ Paste your :red[text] :")
        st.write(":red-background[Note]: As this app uses an LLM to summarize content, so only the :red[first 15,000 words of input will be processed] to the LLM. Remaining words will be dumped")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        butt2 = st.button("ShoVizzaa", type='primary', use_container_width=True)
        

        if got_text:
            st.toast(body="Text Uploaded", icon="👍")

#------------------------------------------------------------------------------------------------
        if butt2:
            if got_text:
                st.write(" ")
                st.markdown("---")
                # st.header("", divider="gray")


                st.toast(body="Started Processing. Summary will be given :red[very soon]", icon="🏋️‍♂️")
                st.header(":red[ShoVizzaa]....")

                got_text = list(filter(lambda y : len(y)>0, list(map(lambda x : x.replace("\n", "").strip().replace("{", "(").replace("}", ")"), got_text.split(" ")))))[:15_000]
                words_count = len(got_text)
                got_text = " ".join(got_text)
                
                models_summary = giveSummary.do_summarize(got_text)

                st.write(models_summary)
                st.caption(f"This summary is generated using :red[{words_count} words] from your input")

                if models_summary:
                    st.toast(body="Summarized your File", icon="✅")
                    with st.expander(":red-background[Click here to read the transcript] of your text"):
                        st.write(got_text)

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

    if not toggle_on:
        uploaded_text_file = st.file_uploader(label = "Upload your :red[PDF] File :", type = [".pdf"])
        st.write(":red-background[Note]: As this app uses an LLM to summarize content, so only the :red[first 15,000 words of input will be processed] to the LLM. Remaining words will be dumped")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        butt3 = st.button("ShoVizzaa", type='primary', use_container_width=True)
        
        if uploaded_text_file:
            st.toast(body="File Uploaded", icon="👍")
#------------------------------------------------------------------------------------------------
        if butt3:
            if uploaded_text_file:
                st.write(" ")
                st.markdown("---")
                # st.header("", divider="gray")

                st.toast(body="Started Processing. Summary will be given :red[very soon]", icon="🏋️‍♂️")
                st.header(":red[ShoVizzaa]....")

                got_text, words_count = extractTextfromPDF.pullText(uploaded_text_file)
                # print(words_count)
                

                models_summary = giveSummary.do_summarize(got_text)
                st.write(models_summary)
                st.caption(f"This summary is generated using :red[{words_count} words] from your input")

                if models_summary:
                    st.toast(body="Summarized your File", icon="✅")
                    with st.expander(":red-background[Click here to read the transcript] of your PDF file"):
                        st.write(got_text)

    st.write(" ")
    st.markdown("---")
    # st.header("", divider="gray")
    st.write(" ")

##########################################################################################
##########################################################################################
if selected == "Youtube Link":
    st.write(" ")
    st.write(" ")
    st.write("""
             Due to YouTube's Terms and Conditions, Can't able to get the Youtube Video's Data. You can :red[download the YouTube video and upload that in Video/Audio Section] 
             1. :red-background[YouTube] Video to :red-background[audio] downlaoder  ---  https://ezmp3.cc/
             2. :red-background[YouTube] Video to :red-background[video] downlaoder  ---  https://en1.savefrom.net/2ol/
             """)
    st.write(" ")
    st.markdown("---")
    # st.header("", divider="gray")
    st.write(" ")
##########################################################################################
##########################################################################################

col1, col2, col3, col4 = st.columns([0.6, 0.15,0.15,0.1])
with col1:
    st.caption(":red[Caution] : All the above summaries are AI-Generated by Gemini 1.5 Pro. The odds of an LLM slip-up are super low, but hey, always stay sharp!!!")
with col3:
    st.caption("Wanna have a chat with me...")
with col4:
    st.markdown("""
        <a href="https://www.linkedin.com/in/dileepnaidu/" target="_blank">
            <img src="https://img.icons8.com/3d-fluency/100/linkedin.png" alt="LinkedIn Profile" width="50" height="50">
        </a>
        """, unsafe_allow_html=True)