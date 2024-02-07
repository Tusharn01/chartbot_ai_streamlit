import streamlit as st
import random
import time

import random

import FirstMLProject
# Run this application run command - streamlit run StreamlitChartBot.py 


# Streamed response emulator
def response_generator(inputTxt):
    tensePrediction = FirstMLProject.predict_tense_by_given_text(inputTxt)
    response = random.choice(
        [
            tensePrediction
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
    
    #response = inputTxt


st.title("Chatbot for ALM")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})