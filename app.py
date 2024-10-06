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


def convert_language(input_text, from_lang):
    # Simulate a call to your LLM model
    # Here you'd pass `input_text` to your LLM and specify the conversion language
    if from_lang == 'English to Creole':
        # Replace this with the actual LLM translation logic
        return f'Translating {input_text} to Creole'
    else:
        return f'Translating {input_text} to English'

# Layout of the interface
st.title('Trinidad Creole ↔ English Translator')

st.markdown("""
This app allows you to convert text or speech from **Trinidad Creole** to **English**, or vice versa.
""")

# Select translation direction
translation_direction = st.selectbox('Choose Translation Direction:', ['English to Creole', 'Creole to English'])

# Input area
st.subheader('Enter your text:')
input_text = st.text_area('Type your text here...', '')

# Convert button
if st.button('Convert'):
    if input_text.strip() != '':
        # Perform conversion using the language model
        translated_text = convert_language(input_text, translation_direction)
        st.subheader('Translated Text:')
        st.write(translated_text)
    else:
        st.warning('Please enter some text to convert!')

# Optionally, add a feature for voice input (more advanced, could use libraries like SpeechRecognition)
st.markdown("""
You can also enable voice input by clicking [here](https://pypi.org/project/SpeechRecognition/) for instructions.
""")



def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Could not understand audio")
        except sr.RequestError:
            st.error("Error with the speech recognition service")
        return ""

# Adding speech-to-text input
st.subheader('Or use voice input:')
if st.button('Start Voice Input'):
    speech_text = recognize_speech()
    if speech_text:
        st.write(f'You said: {speech_text}')