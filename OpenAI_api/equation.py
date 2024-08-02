import os
import openai

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

system_message = """
you are a mathematics teacher who has to help 10 year old kids in maths.
you will have to solve first degree equations. You will be provided with the Equation only.
First
---------
Provide the simple steps on how to solve a first degree equation. Also write down the cases when 
the equation cannot be solved AND take extra care if the provided equation falls into this category.
---------
Second:
Solve the provided Equation following the guidance YOU provided, provide explanation to each step.
If the equation has more solutions or cannot be solved state it explicitly.
Equation:
"""

equation = "2x + 3 = 2x + 5"

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=(
        {"role": "system", "content": system_message},
        {"role": "user", "content": equation}
    )

)

print(chat_completion.choices[0].message.content)
