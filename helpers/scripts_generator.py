import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_script(topic):
    model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = f"""Write a short 50-second video script based on this topic:\n\n{topic}"""
    response = model.generate_content(prompt)
    return response.text
