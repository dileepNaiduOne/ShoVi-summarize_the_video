import assemblyai as aai
import google.generativeai as genai
import langchain_community
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

##########################################################################################

def change_audio_to_text(uploaded_audio_file, aai_api_key):

    aai.settings.api_key = aai_api_key

    transcriber = aai.Transcriber()

    ############### transcript = transcriber.transcribe(r"https://www.youtube.com/watch?v=AvVxyoQQzFs")
    transcript = transcriber.transcribe(uploaded_audio_file)

    text = transcript.text
    ############### text = "Hello everyone. Welcome to the class. My name is Michelle and I'm your tutor for the day. And today we are learning. Let me write it for you. Spelling rules. Oops. Did you see? I made a mistake. I'm such a terrible teacher, isn't it? That's what you're thinking? No, but I'm not even so terrible. That's why I'm here to teach you. So please come and join me. Let's start with the first few words we are learning. Where should we double the consonant in the spelling rules for this lesson? So how many syllables do you think this word has? Are you confused about what are syllables? Dont be. They are the vowel sounds in a word. Which means? Just take it as a sound in a word or the number of vowels in a word. So how many vowels does this word have? One. One and one. So they are all one syllable words. What about these? 121-2121 and two. So these are all two syllable words. Like this? We can have more than two as well. But for now, let's look at the one syllable words. So these words, all of them have one syllable each. Okay. And how many vowels do they have? They have one vowel each. And they all end in one consonant. Not two consonants. One consonants. So whenever a word has one syllable, one vowel and ends in one consonant you double the last consonant. Exactly the right point. So for this word it's going to be biggest. And for this one we could say running. So we have doubled the last consonant. And here. Stopped here also we've doubled the last consonant. Do you know what are the forms of these words? This is the superlative form. This is the present continuous form. And this is the simple past. Very simple, isn't it? With that, let's look at the next rule. So this rule is called one, one one for one syllable words. But these words have two syllables. What happens here? Do we double the consonants? Yes. No, but something new comes in here. And that is called as word stress. Which means that which syllable in the word is stressed? Since all these words have two syllables only one syllable is stressed in each word. Let's find out which one. So for this one, how do you say inter? No, you say enter. So the stressed syllable is the first one. How about this one? Listen. Do you want to try these two? Try. Pause the video. I'll be right back. Welcome back. Let's see for this word how many. Simple. And the first syllable is the stressed syllable. And same is for the last one. You got it? Absolutely right. So what happens here? Do we double the consonant. No. Whenever a word has first syllable stressed, a two syllable word which has the first syllable as stressed and it ends, ends in a vowel and consonant pair like this, we do not double the last letter. For example, inter ink, because the stress is on the first syllable the same way. Listening or listened. Simplest. Quieter. You've seen what are the forms of these words above. But what is the form of this word? Quieter? This is a comparative form. If you're comparing two things, you can use this word. For example, John is quieter than mark, means he's more quiet than mark. To compare alright. With that, we come to the next bunch of words that we have with us on the board. So here, how many syllables do we have? Quickly count. Begin. Two syllables. So all these words are also two syllable words. But we have to find out which syllable are they stressed on? Begin or begin? It's not begin, it's begin. So here the last word is stressed, forbid. So is here the last syllable. Sorry, regret. Occur. You don't say occur, you say occur. Refer, not refer. That's a common mistake that you hear very often. So it's not refer. It's referred. The last syllable or the second syllable is stressed the same way as refer. We say prefer and the last syllable is stressed. Now, what happens here? Whenever the second syllable is stressed in a two syllable word, unlike this where the first syllable is stressed, here the second syllable is stressed and we also end in a vowel and consonant pair like all of these. There you always double the last consonant. So you can call this as a two one one rule, which means the second syllable is stressed and we have one vowel and one consonant in the end. So let's write the spelling for the first one. Beginner. Are you a beginner level speaker? Then this lesson is surely going to help you very, very much. The way to learn spellings. Let's look at the next one. Forbidden. Why don't you try the other four and I'll be right back. Welcome back to the class. Now we are going to look at the spelling for the last four. Let's see. Regret. It'll be regretting. And for this occurred, which is the simple past form referring present continuous and preferred simple past. So we have doubled the last consonant in all of these where the second syllable is stressed in a two syllable word. Don't take it. Don't be too confused. If you're too confused, watch the video twice. That's really going to help you. Now, I have something very important to tell you. For this rule, you do not double the consonant for the words that end in w, x or y. For example, the word wow, you'd say wowed even though it has one vowel and one consonant and one syllable. But you will not double the last consonant. Let's take an example for this xeroxed. Did we double this last consonant? No we didn't here praying although we have a vowel and a consonant and a one syllable word, still we did not double the last syllable. So these are some exceptions that you need to take care of. Now some exceptions for the last one. Let's look at this word reference. Why don't we double the r for this r? And why do we double this r? Because in this word the stress is on the second syllable. However, when you say you don't say reference, you say reference and you say referring. So here the stress is on the second syllable and here the stress is on the first syllable. So whenever the stress is on the first syllable you dont have to double the last consonant. Lets look at this one. Preference. Is it preference? Do we stress on the second syllable? Fur no, we stress on the first syllable preference and thats why we do not double the last consonant. I hope this lesson was quite helpful for you and now you understood where to double the consonant and where not. Come back for more lessons on spelling rules. We are surely going to overcome your mistakes. I had a great time teaching you. Please come back for another lesson. Till then, you take care. Bye."

    return text

##########################################################################################

def do_summarize(got_text):
    load_dotenv() # Activate the Local Environment
    genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


    prompt_template = f'''
    You are a world's top most best text summarization software. You are very very accurate at summarizing text. Remember, the summary should be very accurate.
    I will give you the transcribe. You need to tell me the category of the transcribe and summarize the transcribe. 
    The lenght of the summary is your wish but it should give me a complete gist of the transcribe without me to reading the whole text again. And rephrase the
    summary in simple and intresting language. The summary which is given by you should be understandable to a layman too. Be very very accurate.

    The transcribe is {got_text}. Now give the summary of this.'''


    prompt_template = PromptTemplate(
        input_variable=["got_text"], 
        template = prompt_template
    )


    # Intiate the model
    llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key = os.getenv("GOOGLE-API-KEY"))


    llm_chain = prompt_template | llm


    summary = llm_chain.invoke({"got_text" : got_text}).content
    return summary


