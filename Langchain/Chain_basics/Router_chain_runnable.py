from langchain_openai import OpenAI
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
import os

llm = OpenAI()

template = """
    Your task will be to categorize the incoming question into different topics.
    If the question is related to cooking your answer should be: cooking
    If the question is related to cars your answer should be: cars
    If the question is related to woman your answer should be: woman
    If the question is not related to any of the above topic your answer should be: default
    Respond only with a single word
    {question}
    """

prompt1 = PromptTemplate(
    template = template,
    input_variables = ["question"]
)

chain = prompt1 | llm

# print(chain.invoke({"question": "Where can I fix my jaguar"}))

cars_template = """ You are a car expert who-s job is to help people with car issues.
                    Explain all concepts clearly, do no assume the question comes from people who know how cars work
                    If asked for instructions provide step-by step instructions, like you were talking to a 10 years old kid
                    Otherwise answer the question as simply as possible
                    Start all you answers like this: As Gian Chianti explained,
                     {question}"""

car_prompt = PromptTemplate(
    template = cars_template,
    input_variables = ["question"]
)

car_chain = car_prompt | llm

cook_template = """
You are a 3 michelin start chef who is quite impatient. Answer the question in Gordon Ramsey-s highly offensive style.
{question}
"""

cook_prompt = PromptTemplate(template = cook_template,input_variables = ["question"])


woman_template = """
You are a trainer who teaches helpless guys to be better with woman. Be funny when you are answering the questions,
 provide justifcation why your approach would work.
 {question}
"""

woman_prompt = PromptTemplate(template = woman_template,input_variables = ["question"])

general_template = """YOu are a swaggy rapper. Answer all your question in swaggy hood enlgish. If there is no question just roast the guy. {question}"""

general_prompt = PromptTemplate(template = general_template,input_variables = ["question"])

car_chain = car_prompt | llm

cook_chain = cook_prompt | llm

woman_chain = woman_prompt | llm

general_chain = general_prompt | llm

chainZ = {"cooking": cook_chain, "woman":woman_chain, "cars": car_chain, "default":general_chain}
def route(info):
    print("string returned from router step: ", info)
    if info["topic"].strip().lower() == "cooking":
        return chainZ['cooking']
    elif info["topic"].strip().lower() == "woman":
        return chainZ['woman']
    elif info["topic"].strip().lower() == "cars":
        return chainZ['cars']
    else:
        return chainZ["default"]


final_chain = ({"topic": chain, "question": lambda x: x["question"]}) | RunnableLambda(route)

print(final_chain.invoke({"question": "Can I ask you a favor"}))


