import os
from dotenv import load_dotenv 
from openai import OpenAI

# Get API key from environment variable or prompt user
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("OpenAI API key not found in environment variables.")
    api_key = input("Enter your OpenAI API key: ")

client = OpenAI(api_key=api_key)

def chat(user_message):
    """Send a message to ChatGPT and get a response"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

# Main chat loop
print("Chatbot is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    bot_response = chat(user_input)
    print(f"Bot: {bot_response}\n")