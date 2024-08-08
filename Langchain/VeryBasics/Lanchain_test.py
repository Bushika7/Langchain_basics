from langchain.llms import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=api_key)


