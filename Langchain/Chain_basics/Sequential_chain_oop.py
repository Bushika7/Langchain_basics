from abc import ABC, abstractmethod
from langchain_openai import OpenAI
from operator import itemgetter
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.globals import set_verbose


class Joke(ABC):

    def __init__(self):
        self.topic = None
        self.language = None
        self.llm = OpenAI()
        self.joketemplate_text = "You are a very funny comedian who's job is to tell a joke given a topic {topic}"
        self.joketemplate = PromptTemplate(template=self.joketemplate_text,input_variables = ["topic"] )
        self.jokechain = self.joketemplate | self.llm | StrOutputParser()
        self.translate_text = "You will be provided a joke {joke}, please translate it to the given language {language}"
        self.ttemplate = PromptTemplate(template = self.translate_text, input_variables = ["language"] )
        self.tchain = (
            {"joke": self.jokechain, "language": itemgetter("language")} |
            self.ttemplate | self.llm | StrOutputParser()
        )
    @abstractmethod
    def set_topic(self, topic: str):
        pass

    @abstractmethod
    def get_joke(self):
        pass


class SpanishJoke(Joke):
    def __init__(self):
        super().__init__()
        self.language ="spanish"

    def set_topic(self, topic: str):
        self.topic = topic

    def get_joke(self):
        spchain = self.jokechain | self.tchain
        here = self.tchain.invoke({"topic":self.topic, "language": self.language})
        print(here)
        return here

class HungarianJoke(Joke):
    def __init__(self):
        super().__init__()
        self.language = 'hungarian'

    def set_topic(self, topic: str):
        self.topic = topic

    def get_joke(self):
        here = self.tchain.invoke({"topic":self.topic, "language": self.language})
        print(here)
        return here

    def get_joke_explain(self):
        text = "Kapni fogsz bemenetként egy viccet {vicc}. 1) Írd le a viccet csupa nagybetűvel, 2) magyarázd el miért vicces"
        eprompt = PromptTemplate(template = text, input_variables = ["vicc"])
        expchain = (
            {"vicc":self.tchain} | eprompt | self.llm | StrOutputParser()
        )
        print(expchain.invoke({"language":self.language, "topic": self.topic}))
        print(expchain.get_graph())
        print(expchain.get_prompts())
class GermanJoke(Joke):
    def __init__(self):
        super().__init__()
        self.language = 'germann'

    def set_topic(self, topic: str):
        self.topic = topic

    def get_joke(self):
        here = self.tchain.invoke({"topic":self.topic, "language": self.language})
        print(here)





hu = HungarianJoke()
hu.set_topic("football")
hu.get_joke_explain()

