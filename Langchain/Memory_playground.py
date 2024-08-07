from langchain.memory import ConversationEntityMemory, ConversationSummaryMemory
from langchain_openai import OpenAI
import os

# re-work everything with non deprecated functions

api_key = os.getenv("OPENAI_API_KEY")


memory = ConversationEntityMemory(llm = OpenAI(api_key = api_key))

_input = {"input": "Deven & Sam are 2 DJ-s making bomb*ss minimal techno. They have occasional shows in western Europe . The grass is green and the girls are pretty. Except Gina who is a bit overweight. Please, be reasonable for once"}
memory.load_memory_variables(_input)
memory.save_context(
    _input,
    {"output": " I dont really like minimal techno. Classical music is my thing. Beethoven is as you phrased: bombass, that music is not"}
)


akki = memory.load_memory_variables({"input": 'Who is Gina?'})

print(akki)