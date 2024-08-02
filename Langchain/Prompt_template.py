import os

from langchain import OpenAI
from langchain import PromptTemplate
template = """Sentence: {sentence}
Translation in {language}:
"""
prompt = PromptTemplate(template = template, input_variables=["sentence","language"])


api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(api_key=api_key)

response = llm(prompt.format(sentence = "the cat is on the table", language = "spanish"))
print(prompt.format(sentence = "the cat is on the table", language = "spanish"))

print(response)