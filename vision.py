from dotenv import load_dotenv
load_dotenv()
## loading teh environment variables

import streamlit as st
import os
import google.generativeai as genai 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


##func to load gemini-vision-pro 
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(image):
    response=model.generate_content(image)
    return response.text