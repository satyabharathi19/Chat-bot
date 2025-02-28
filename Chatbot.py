import streamlit as st
import google.generativeai as genai
API_KEY="AIzaSyA8sX72KAAwZINkvgrU3LUlGA9XTZBo_CI"
m=genai.GenerativeModel('gemini-1.5-flash')
if "chat" not in st.session_state:
    st.session_state.chat = m.start_chat(history=[])

st.title("Chat-Bot")
st.write('This is a chatbot to answer queries.')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from the model
    response = st.session_state.chat.send_message(prompt)

    # Append response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)
