import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI


load_dotenv()

st.set_page_config(page_title="Python Chatbot", page_icon="🤖")
st.title("Python Chatbot")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY is missing. Add it to your .env file.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = [
        AIMessage(content="Hi! I am your chatbot. Ask me anything.")
    ]

for msg in st.session_state.messages:
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

prompt = st.chat_input("Type your message...")
if prompt:
    user_msg = HumanMessage(content=prompt)
    st.session_state.messages.append(user_msg)
    with st.chat_message("user"):
        st.markdown(prompt)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, api_key=api_key)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(st.session_state.messages)
            st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))
