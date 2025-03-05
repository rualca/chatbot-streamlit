import streamlit as st
import langchain_openai as ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=api_key)

st.title("LangChain Chatbot")
st.subheader("Powered by OpenAI")

messages = [("system", "You are a usefull chatbot")]

# Create a session state to store the messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get the user input
if prompt := st.chat_input("Escibe tu mensaje..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    messages.append(["human", prompt])
    
    response = llm.invoke(messages).content
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})