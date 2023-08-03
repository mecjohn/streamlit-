import streamlit as st
from embedchain import OpenSourceApp
app = OpenSourceApp()

app.add("web_page", "https://www.gutenberg.org/cache/epub/1430/pg1430-images.html")

st.set_page_config(page_title='Beautiful Stories from Shakespeare')

st.write('Beautiful Stories from Shakespeare Chatbot')

user_input = st.text_input('Ask the Chatbot')
if st.button('Ask'):
    # Get the chatbot's response to the user's input
    response = app.chat(user_input)
    st.write(response)