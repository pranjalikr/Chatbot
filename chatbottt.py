import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Groq Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, content in st.session_state.messages:
    st.chat_message(role).write(content)

user_input = st.chat_input("Say something")

if user_input:
    st.session_state.messages.append(("user", user_input))
    st.chat_message("user").write(user_input)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # 👈 working model
        messages=[{"role": r, "content": c} for r,c in st.session_state.messages]
    )

    bot_reply = response.choices[0].message.content
    st.session_state.messages.append(("assistant", bot_reply))
    st.chat_message("assistant").write(bot_reply)
