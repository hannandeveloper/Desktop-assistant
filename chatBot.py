from google import genai
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())

api= os.getenv("gen_api")

client = genai.Client(api_key=api)

chat = client.chats.create(model="gemini-flash-latest")

while True:
    user = input("you: ")

    if user.lower() == "exit":
        break
    reply = chat.send_message(user)
    print(f"bot: {reply.text}")