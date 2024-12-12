from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_openai import OpenAIEmbeddings
from config import KEY
from openai import OpenAI


def get_embedding_function(): # This is where you can get embeddings, u will probably want an API and pay just a lil
    embeddings = OpenAIEmbeddings(openai_api_key='')

    # embeddings = OllamaEmbeddings(model="nomic-embed-text") # This is an embedding you could easily run locally, doesn't perform super well tho
    return embeddings
