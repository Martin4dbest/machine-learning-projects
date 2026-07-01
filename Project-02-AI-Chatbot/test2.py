# ==========================================
# Project 02 - AI Chatbot
# AI Engineering Bootcamp
# Author: Martin Agoha
# ==========================================

from dotenv import load_dotenv
import os
from google import genai

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file.")

# ==========================================
# Create Gemini Client
# ==========================================

client = genai.Client(api_key=api_key)

# ==========================================
# Start Chat Session
# ==========================================

chat = client.chats.create(
    model="gemini-2.5-flash"
)

# ==========================================
# Welcome Screen
# ==========================================

name = input("👤 Please enter your name: ")

print("\n" + "=" * 70)
print("🤖 MARTIN'S AI ENGINEERING ASSISTANT")
print("=" * 70)
print(f"Welcome, {name}! 👋")
print("I'm powered by Google's Gemini AI.")
print("Ask me anything about:")
print("• Artificial Intelligence")
print("• Machine Learning")
print("• Python Programming")
print("• Software Development")
print("• Or any topic you like!")
print("\n💬 Type 'exit' anytime to quit.")
print("=" * 70)

# ==========================================
# Chat Loop
# ==========================================

while True:

    user_input = input(f"\n{name}: ")

    if user_input.lower() == "exit":
        print(f"\nGoodbye, {name}! 👋")
        print("Thanks for using Martin's AI Engineering Assistant.")
        break

    try:

        response = chat.send_message(user_input)

        print("\n🤖 Gemini:")
        print(response.text)

    except Exception as e:

        print("\n❌ An error occurred.")
        print(e)