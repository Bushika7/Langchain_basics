import os
import openai
api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(api_key = api_key )


system_message = '''
You are an AI assistant that helps humans by generating tutorials given a text.
You will be provided with a text. 
If the text contains any kind of instructions on how to proceed with something, generate
tutorial in a bullet list. Otherwise, inform the user that the text does not contain any instructions
'''

instructions = '''
The sun is shining and dogs are running on the beach
'''


chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": instructions}
    ]
)

print(chat_completion.choices[0].message.content)
