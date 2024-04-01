import os
import openai

# Set your OpenAI API key here directly
API_KEY = "YOUR_API_KEY"
openai.api_key = API_KEY

# Instantiate the OpenAI client
client = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "What is geopolitics?",
        }
    ]
)

# Retrieve the completion
print(client.choices[0].message['content'])
