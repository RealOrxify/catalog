import openai
import readline
import os

# Set your OpenAI API key here
openai.api_key = "<YOUR_OPENAI_API_KEY>"

# Initialize the chatbot's conversation history
conversation_history = []

def format_message(message):
    if message['role'] == 'system':
        return f"SYSTEM: {message['content']}"
    elif message['role'] == 'user':
        return f"USER: {message['content']}"
    elif message['role'] == 'assistant':
        return f"AI: {message['content']}"

def print_messages(messages):
    for message in messages:
        print(format_message(message))

def send_message(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        prompt_id=1,
        temperature_decay=0.8,
        prompt_type="user",
        message=conversation_history,
    )

    reply = response.choices[0].message
    conversation_history.append(reply['content'])

    return reply['content']

def main():
    while True:
        user_input = input("USER: ")

        if user_input.lower() == "exit":
            break

        os.system('clear' if os.name == 'posix' else 'cls')

        conversation_history.append({"role": "user", "content": user_input})
        assistant_response = send_message(user_input)
        conversation_history.append({"role": "assistant", "content": assistant_response})

        print_messages(conversation_history)

if __name__ == "__main__":
    main()
