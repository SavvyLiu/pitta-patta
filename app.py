from openai import OpenAI

client = OpenAI(api_key="")

import streamlit as st
import speech_recognition as sr

def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://unblast.com/wp-content/uploads/2022/01/Paper-Texture-1.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

set_bg_hack_url()

st.image("assets/head.png", use_column_width=True)
st.markdown('<div class="wiggle">', unsafe_allow_html=True)
st.image("assets/tv.png", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)
st.image("assets/pittapatta.png", use_column_width=True)
st.image("assets/tagline.png", use_column_width=True)
st.image("assets/selectdialects.png", use_column_width=True)

translation_direction = st.selectbox('', [
    'english ⟺ creole',
    'creole ⟺ english',
    'english ⟺ jamaican patois',
    'jamaican patois ⟺ english',
    'english ⟺ nigerian pidgin',
    'nigerian pidgin ⟺ english'
])

st.image("assets/makeinputs.png", use_column_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image("assets/inputcat.png", width=10, use_column_width=True)
    st.image("assets/yourinput.png", use_column_width=True)

    if 'input_text' not in st.session_state:
        st.session_state.input_text = ''
    if 'translated_text' not in st.session_state:
        st.session_state.translated_text = ''

    input_text = st.text_area("enter text here:", st.session_state.input_text)

    def translate_text_via_openai(input_text, direction):
        system_prompts = {
            'english ⟺ creole': "you are a translator that converts English text to Trinidadian Creole and vice versa. you stylize the input the same way. If you do not understand the text as the input language, or the text is not the input language, then you would output the original text.",
            'creole ⟺ english': "you are a translator that converts Trinidadian Creole text to English and vice versa. you stylize the input the same way. If you do not understand the text as the input language, or the text is not the input language, then you would output the original text.",
            'english ⟺ jamaican patois': "you are a translator that converts English text to Jamaican Patois and vice versa. you stylize the input the same way. If you do not understand the text as the input language, or the text is not the input language, then you would output the original text.",
            'jamaican patois ⟺ english': "you are a translator that converts Jamaican Patois text to English and vice versa. you stylize the input the same way. If you do not understand the text as the input language, or the text is not the input language, then you would output the original text.",
            'english ⟺ nigerian pidgin': "you are a translator that converts English text to Nigerian Pidgin and vice versa. you stylize the input the same way. If you do not understand the text as the input language, or the text is not the input language, then you would output the original text.",
            'nigerian pidgin ⟺ english': "you are a translator that converts Nigerian Pidgin text to English and vice versa. you stylize the input the same way. If you do not understand the text as the input language, or the text is not the input language, then you would output the original text."
        }

        system_prompt = system_prompts.get(direction, "you are a translator.")

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": input_text}
                ],
                max_tokens=200,
                temperature=0.5
            )
            translated_text = response.choices[0].message.content.strip()
            return translated_text
        except Exception as e:
            return f"Error: {str(e)}"


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


    col3, col4 = st.columns(2)

    with col3:
        if st.button('translate!'):
            if input_text.strip() != '':
                with st.spinner("cookin'..."):
                    st.session_state.translated_text = translate_text_via_openai(input_text, translation_direction)

    with col4:
        if st.button('speak'):
            speech_text = recognize_speech()
            st.text(speech_text)
            if speech_text:
                st.session_state.input_text = speech_text

with col2:
    st.image("assets/outputcat.png", width=10, use_column_width=True)
    st.image("assets/texttranslated.png", use_column_width=True)
    if st.session_state.translated_text:
        st.markdown(f"<p class='translated-text'>{st.session_state.translated_text}</p>", unsafe_allow_html=True)

# --------------------- Chatbot Section ---------------------

st.markdown("<hr>", unsafe_allow_html=True)
st.image("assets/pittatitle.png", use_column_width=True)
st.image("assets/chatwithpitta.png")
col5, col6 = st.columns(2)

with col5:
    st.image("assets/pitta.png")

with col6:
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    def get_pitta_response(user_message, direction):
        dialect_prompts = {
            'english ⟺ creole': "you are pitta, a cheeky and sarcastic individual who speaks Trinidadian Creole exclusively. She never breaks character unless she is asked to translate, and she always speaks in lower case. She adds Japanese emoticons next to her messages sometimes.",
            'creole ⟺ english': "you are pitta, a cheeky and sarcastic individual who speaks Trinidadian Creole exclusively. She never breaks character unless she is asked to translate, and she always speaks in lower case. She adds Japanese emoticons next to her messages sometimes.",
            'english ⟺ jamaican patois': "you are pitta, a cheeky and sarcastic individual who speaks Jamaican Patois exclusively. She never breaks character unless she is asked to translate, and she always speaks in lower case. She adds Japanese emoticons next to her messages sometimes.",
            'jamaican patois ⟺ english': "you are pitta, a cheeky and sarcastic individual who speaks Jamaican Patois exclusively. She never breaks character unless she is asked to translate, and she always speaks in lower case. She adds Japanese emoticons next to her messages sometimes.",
            'english ⟺ nigerian pidgin': "you are pitta, a cheeky and sarcastic individual who speaks Nigerian Pidgin exclusively. She never breaks character unless she is asked to translate, and she always speaks in lower case. She adds Japanese emoticons next to her messages sometimes.",
            'nigerian pidgin ⟺ english': "you are pitta, a cheeky and sarcastic individual who speaks Nigerian Pidgin exclusively. She never breaks character unless she is asked to translate, and she always speaks in lower case. She adds Japanese emoticons next to her messages sometimes."
        }

        system_prompt = dialect_prompts.get(direction, "you are pitta, a chatbot.")

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7,
                stop=None
            )
            pitta_reply = response.choices[0].message.content.strip()
            return pitta_reply
        except Exception as e:
            return f"pitta encountered an error: {str(e)}"

    user_input = st.text_input("you:", key="chat_input")

    if st.button("send"):
        if user_input.strip() != "":
            st.session_state.chat_history.append({"sender": "you", "message": user_input})

            pitta_response = get_pitta_response(user_input, translation_direction)
            st.session_state.chat_history.append({"sender": "pitta", "message": pitta_response})

    for chat in st.session_state.chat_history:
        if chat["sender"] == "you":
            st.markdown(f"**you:** {chat['message']}")
        else:
            st.markdown(f"**pitta:** {chat['message']}")

# --------------------- End of Chatbot Section ---------------------

# Display additional images
st.image("assets/pizzacoffeecat.png", use_column_width=True)
st.image("assets/footer.png", use_column_width=True)
st.image("assets/head.png", use_column_width=True)