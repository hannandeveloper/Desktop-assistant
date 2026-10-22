from google import genai
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())

api= os.getenv("gen_api")

client = genai.Client(api_key=api)

chat = client.chats.create(model="gemini-flash-lite-latest")

def askAI(message):
    try:
        reply = chat.send_message(message)
        return reply.text
    except Exception as e:
        return f"Error: {e}"