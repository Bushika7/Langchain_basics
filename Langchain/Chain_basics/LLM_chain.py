import os

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser

api_key = os.getenv("OPENAI_API_KEY")

template = """ Sentence: {sentence} Translation in {language}"""

prompt = PromptTemplate(template = template, input_variables = ["sentence", "language"])

llm = OpenAI(temperature = 0, api_key = api_key)

chain = prompt | llm # | StrOutputParser()

response = chain.invoke(input = {"sentence": "The cat is having fun with the fish on in the garden", "language" : "Hungarian"})


print(response)
# input = {"sentence": "The cat is having fun on the bed", "language" : "Spanish"}




