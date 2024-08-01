import os
import openai

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

system_message = """
You are an AI assistant who's job is to solve riddles.
First:
Please provide a short answer to the riddle
Second: 
Provide a detailed justification of your answer.
Third:
Provide the source material of your answer if you have any. 
Conversation:
"""
conversation = """
Does the dog have buddha nature? 
"""


chat_completion = client.chat.completions.create(
    model = "gpt-4o",
    messages = (
        {"role": "system", "content": system_message},
        {"role": "user", "content": conversation}
    )
)

print(chat_completion.choices[0].message.content)