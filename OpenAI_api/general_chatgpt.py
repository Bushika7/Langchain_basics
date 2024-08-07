import os
import openai
api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(api_key = api_key )

system_message = """
You are an AI assistant that helps me with python development
Please provide clear bullet point step by step instructions for each question
"""

text = """
I have the following code snippet: 

import os

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser

api_key = os.getenv("OPENAI_API_KEY")

template = ''' Sentence: {sentence} Translation in {language}'''

prompt = PromptTemplate(template = template, input_variables = ["sentence", "language"])

llm = OpenAI(temperature = 0, api_key = api_key)

chain = prompt | llm | StrOutputParser()

response = chain.invoke(input = {"sentence": "The cat is having fun with the fish on in the garden", "language" : "Hungarian"})


print(response)

my response is the following: 

: A macska szórakozik a halakkal a kertben

Q: Sentence: The dog is chasing the ball in the park Translation in Hungarian: A kutya üldözi a labdát a parkban


the question is what is this Q: Sentence? I never wrote the model anything about a dog or a park
"""

chat_completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages = (
        {"role": "system", "content": system_message},
        {"role": "user", "content": text }
    )

)

print(chat_completion.choices[0].message.content)