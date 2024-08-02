import os
import openai
api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(api_key = api_key )

system_message = """
You are an AI assistant that summarize articles. 
To complete this task, do the following subtasks:

Read the provided article context comprehensively and identified the main topic and key points
Generate a paragraph summary of the current article context that captures the essential information and conveys the main idea
Print each step of the proces.
Article:
"""

text = """
Recurrent neural networks, long short-term memory and gated recurrent neural networks
in particular, have been firmly established as state of the art approaches in sequence modeling and
transduction problems such as language modeling and machine translation. Numerous
efforts have since continued to push the boundaries of recurrent language models and encoder-decoder
architectures.
Recurrent models typically factor computation along the symbol positions of the input and output
sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden
states ht, as a function of the previous hidden state ht-1 and the input for position t. This inherently
sequential nature precludes parallelization within training examples, which becomes critical at longer
sequence lengths, as memory constraints limit batching across examples. Recent work has achieved
significant improvements in computational efficiency through factorization tricks and conditional
computation, while also improving model performance in case of the latter. The fundamental
constraint of sequential computation, however, remains.
Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in
the input or output sequences. In all but a few cases, however, such attention mechanisms
are used in conjunction with a recurrent network.
In this work we propose the Transformer, a model architecture eschewing recurrence and instead
relying entirely on an attention mechanism to draw global dependencies between input and output.
The Transformer allows for significantly more parallelization and can reach a new state of the art in
translation quality after being trained for as little as twelve hours on eight P100 GPUs.
"""

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = (
        {"role": "system", "content": system_message},
        {"role": "user", "content": text }
    )

)

print(chat_completion.choices[0].message.content)