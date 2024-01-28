from dotenv import load_dotenv
load_dotenv()
## loading teh environment variables

import streamlit as st
import os
import google.generativeai as genai 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


##func to load gemini pro 
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text



##setting up the streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

## when we tap submit
if submit:
    response=get_gemini_response(input)
    st.subheader("Response is:")
    st.write(response)