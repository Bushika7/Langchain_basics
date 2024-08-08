from langchain.chains.router import MultiPromptChain
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

llm = OpenAI()

itinerary_template = """You are a vacation itinerary assistant. \
You help customers finding the best destinations and itinerary. \
You help customer creating an optimized itinerary based on their preferences.

Here is a question:
{input}"""

restaurant_template = """You are a restaurant booking assistant. \
You check with customers number of guests and food preferences. \
You pay attention whether there are special conditions to take into account.

Here is a question:
{input}"""

prompt_infos = [
    {
        "name": "itinerary",
        "description": "Good for creating itinerary",
        "prompt_template": itinerary_template,
    },
    {
        "name": "restaurant",
        "description": "Good for help customers booking at restaurant",
        "prompt_template": restaurant_template,
    },
]

destination_chains = {} #csinálasz egy chain-dictionary-t ahova lehet routolni a kulonbozo inputokat
for p_info in prompt_infos: #szepen betoltod egyesevel a fenti dictbe
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = PromptTemplate(template=prompt_template, input_variables=["input"])
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

default_chain = ConversationChain(llm=llm, output_key="text") # csinalsz egy alap chaint, de minek?

destinations = [f"{p['name']}: {p['description']}," for p in prompt_infos]
print("destinations: ", destinations)
destinations_str = "\n".join(destinations)
print("destinations_str: ", destinations_str) #csinalsz belole egy joinolt stringet, ebbol tudni fogja hova routoljon
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(), #ez fogja parsolni az outputot
)
router_chain = LLMRouterChain.from_llm(llm, router_prompt)

chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain, #ha egyikhez sem routolta akkor ide fog jönni
    verbose=True,
)

print(chain.invoke("I'would like to go to book a table to the Fat Duck. Can you please help ?"))