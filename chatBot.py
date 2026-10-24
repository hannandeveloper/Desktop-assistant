from google import genai
from dotenv import load_dotenv,find_dotenv
import os

import sys, os
from dotenv import load_dotenv

def baseDir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(baseDir(), ".env"))

api= os.getenv("gen_api")

client = genai.Client(api_key=api)

chat = client.chats.create(model="gemini-flash-lite-latest")

def askAI(message):
    try:
        reply = chat.send_message(message)
        return reply.text
    except Exception as e:
        return f"Error: {e}"

    #  python -m PyInstaller --noconfirm --onedir --windowed --name DesktopAssistant --collect-all customtkinter GUI.py