import os
import openai
import json
from openai import OpenAI
openai.organization="org-SxZP*****************WkX3"
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def get_openai_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
        ],
#        engine="text-davinci-002",
#        prompt=user_input,
        max_tokens=150,
        n=1,
        stop=None
    )
#    return response.choices[0].text.strip()
    return response.choices[0].message.content


knowledge_base = {
    "What is your name?": "I am a chatbot powered by OpenAI.",
    "How does the weather look today?": "I'm sorry, I don't have real-time information. You can check a weather website for that.",
    "Tell me a joke.": "Why don't scientists trust atoms? Because they make up everything!",
    "Is Microsoft SOC II Certified?":"Yes, Innovaccer has SOC II Type II",
    "Microsoft's SOC II Report":"https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-soc-2",
}

knowledge_base = {key.lower(): value for key, value in knowledge_base.items()}

session_file = 'chatbot_session.json'


# Function to process user input based on the custom knowledge base
#def process_user_input(user_input, session):
def process_user_input(user_input):

    user_input_lower = user_input.lower()
#    response = "I'm sorry bro!, I don't have information on that topic."

#    if user_input in knowledge_base:
    if user_input_lower in knowledge_base:
        response = knowledge_base[user_input_lower]

#        session.append({
#            "input": user_input_lower,
#            "resp": response
#        })
    
        return response

    else:
        return "I'm sorry, I don't have information on that topic."


# Function to save the session state to a file
def save_session_state(session):
    with open(session_file, 'w') as file:
        json.dump(session, file)

# Function to load the session state from a file
def load_session_state():
    try:
        with open(session_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Example usage
session = load_session_state()

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break

    openai_response = get_openai_response(user_input)
    print("OpenAI Response:", openai_response)

 #   custom_response = process_user_input(user_input, session)
    custom_response = process_user_input(user_input)
    print("Chatbot:", custom_response)

    # Save the session state after each interaction
    save_session_state(session)

    # Get the next user input
    user_input = input("User: ")
