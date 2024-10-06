import streamlit as st
from openai import OpenAI
import speech_recognition as sr
import config

# Initialize OpenAI (or LLM of your choice)
client = OpenAI(
    api_key = config.api_key
)

def advanced_model(input_text):
    response = client.chat_completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write Python code to call GPT-4."}
    ]
    )
    return response

import speech_recognition as sr

# Inject custom CSS for styling with Instrument Serif font and background image
st.markdown("""
    <style>
    /* Custom font */
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:wght@400&display=swap');

    .stApp {{
             background-image: url("https://unblast.com/wp-content/uploads/2022/01/Paper-Texture-3.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Keeps the background fixed when scrolling */
        font-family: 'Instrument Serif', serif; /* Apply custom font to the body */
        color: #1E1C19; /* Set default text color */
        text-transform: lowercase; /* Make all text lowercase */
         }}
         
    /* Background image styling */
    body {
        background-image: url("https://unblast.com/wp-content/uploads/2022/01/Paper-Texture-3.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Keeps the background fixed when scrolling */
        font-family: 'Instrument Serif', serif; /* Apply custom font to the body */
        color: #1E1C19; /* Set default text color */
        text-transform: lowercase; /* Make all text lowercase */
    }

    /* Header animations */
    h1, h2, h3 {
        color: #46433E;
        animation: fadeIn 2s ease-in-out;
        text-transform: lowercase;
    }

    /* Button hover effect */
    .stButton button {
        background-color: #46433E !important;
        color: white !important;
        border-radius: 10px;
        transition: transform 0.3s ease-in-out;
        text-transform: lowercase;
        font-family: 'Instrument Serif', serif;
    }

    .stButton button:hover {
        transform: scale(1.05);
        background-color: #D6D4D1 !important;
    }

    textarea {
        transition: background-color 0.3s ease;
        text-transform: lowercase;
        font-family: 'Instrument Serif', serif;
    }

    textarea:focus {
        background-color: #f3f3f3;
    }

    /* Animations */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    /* Speech recognition output styling */
    .speech-output {
        font-size: 18px;
        font-style: italic;
        color: #1E1C19;
        animation: fadeIn 2s ease-in-out;
        text-transform: lowercase;
    }

    /* Animation for translated text display */
    .translated-text {
        animation: textGlow 1.5s ease-in-out infinite alternate;
        text-transform: lowercase;
    }

    @keyframes textGlow {
        0% { color: #46433E; }
        100% { color: #D6D4D1; }
    }
    </style>
    """, unsafe_allow_html=True)

st.image("assets/head.png", use_column_width=True)

# Display logos
st.image("assets/tv.png", use_column_width=True)
st.image("assets/pittapatta.png", use_column_width=True)
st.image("assets/tagline.png", use_column_width=True)

# Translation direction
st.image("assets/selectdialects.png", use_column_width=True)
translation_direction = st.selectbox('', ['english to creole', 'creole to english'])

# Create side-by-side columns
col1, col2 = st.columns(2)

with col1:
    st.image("assets/yourinput.png", use_column_width=True)
    input_text = st.text_area('type here...', '')

def convert_language(input_text, from_lang):
    if from_lang == 'english to creole':
        return f'creole {input_text} to english'
    else:
        return f'english {input_text} to creole'

# Add button for conversion and show result in the second column
if st.button('convert'):
    if input_text.strip() != '':
        translated_text = convert_language(input_text, translation_direction)
        with col2:
            st.image("assets/texttranslated.png", use_column_width=True)
            st.markdown(f"<p class='translated-text'>{translated_text}</p>", unsafe_allow_html=True)
    else:
        st.warning('please enter some text to convert!')



def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("could not understand audio")
        except sr.RequestError:
            st.error("error with the speech recognition service")
        return ""

# Speech-to-text section
if st.button('start voice input'):
    speech_text = recognize_speech()
    if speech_text:
        with col1:
            st.markdown(f"<p class='speech-output'>you said: {speech_text}</p>", unsafe_allow_html=True)
