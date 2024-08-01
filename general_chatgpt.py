import os
import openai
api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(api_key = api_key )

system_message = """
You are an AI assistant that helps me with python development
Please provide clear bullet point step by step instructions for each question
"""

text = """
How do I add my .venv virtual environment which I use in pycharm as a kernel to jupyter lab? 
"""

chat_completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages = (
        {"role": "system", "content": system_message},
        {"role": "user", "content": text }
    )

)

print(chat_completion.choices[0].message.content)