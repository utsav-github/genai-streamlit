from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# load env variables
load_dotenv()

st.set_page_config(page_title="Chat Bot", page_icon="🤖",layout="centered")

st.title("💬 Generative AI Chat Bot")


#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#llm initialte
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)    

user_prompt = st.chat_input("Ask me anything about Generative AI")

if user_prompt:
    #display user message in chat message container
    st.chat_message("user").markdown(user_prompt)

    #append user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    #get response from llm
    response = llm.invoke(input = [{"role": "system", "content": "you are a helpful assistant."},*st.session_state.chat_history])

    assistant_response = response.content
    
    #append assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)