import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from PIL import Image
#Loading .env
load_dotenv()
#Loading API key
api_key = os.getenv("gemini_api_key")
#Initializing a client
client = genai.Client(api_key=api_key)
images = st.file_uploader(
        "Upload your photo to analyze...",
        type = ['jpeg','png','jpg'],
        accept_multiple_files = True
        )
if images:
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    prompt = """Summarize the pictures in note format at max 100 words. Make sure to add markdowns to differentiate between sections."""
    #Note Generator
    response = client.models.generate_content(
    model = 'gemini-3-flash-preview',
    contents = [pil_images, prompt]
    )
    st.markdown(response.text)