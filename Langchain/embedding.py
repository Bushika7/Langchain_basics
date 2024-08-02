import os

from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

api_key = os.getenv("OPENAI_API_KEY")
# Load the document, split it into chunks, embed each chunk and load it into the vector store.
raw_documents = TextLoader('../../dialogue.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=0, separator = "\n",)
documents = text_splitter.split_documents(raw_documents)
db = FAISS.from_documents(documents, OpenAIEmbeddings(openai_api_key = api_key))

query = "Greeting"
docs = db.similarity_search(query)
print(docs[0].page_content)

