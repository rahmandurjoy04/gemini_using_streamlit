from google import genai
from dotenv import load_dotenv
import os

#Loading .env
load_dotenv()
#Loading API key
api_key = os.getenv("gemini_api_key")
#Initializing a client
client = genai.Client(api_key=api_key)

#Note Generator
def note_generator(images):
    prompt = """Summarize the pictures in note format at max 100 words for each image. Make sure to add markdowns to differentiate between sections."""
    response = client.models.generate_content(
        model = 'gemini-3-flash-preview',
        contents = [images, prompt]
    )
    return response.text
#Quiz Generator
def quiz_generator(images,selected_option):
    prompt = f"generate 3 quizes for each image with the given difficulty level: {selected_option}. Also add markdown to show them properly."
    response = client.models.generate_content(
        model = 'gemini-3-flash-preview',
        contents = [images,prompt]
    )
    return response.text