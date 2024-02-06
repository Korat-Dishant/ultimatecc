from langchain_google_genai import GoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os
from dotenv import load_dotenv
from langchain import OpenAI
import openai
from langchain_community.vectorstores import Milvus
from langchain.chains import RetrievalQA 
from langchain.memory import ConversationBufferWindowMemory
from langchain import PromptTemplate
from langchain.memory import PostgresChatMessageHistory
from dataCreation import get_docs
load_dotenv()

template = """
Use the following context (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the question:
------
<ctx>
{context}
</ctx>
------
<hs>
{history}
</hs>
------
{question}
Answer:
"""
prompt = PromptTemplate(
    input_variables=["history", "context", "question"],
    template=template,
)

# initializing LLM
def initialize_LLM(name):
    global llm
    if (name == "gemini") :
        llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY") , temperature=0.6)
    else : 
        if (name == "OpenAI") :
            openai.api_key = os.getenv('OPENAI_API_KEY')
            llm=OpenAI(temperature=0.5)
        else : 
            print("we currently dont support {}. please try gemini or OpenAI".format(name))
    

# embeddings
def initialize_embeddings():
    try :
        global embeddings
        embeddings = HuggingFaceInferenceAPIEmbeddings(
            api_key=os.getenv("HUGGINGFACE_API_KEY"), model_name="sentence-transformers/all-MiniLM-l6-v2"
        )
    except Exception as e :
        print("probelm accured while creating embeddings \n{}".format(e))

# vector database
def load_vectorDB(collection_name):
    global vector_db
    vector_db = Milvus(
    embeddings,
    collection_name=collection_name,
    connection_args={
    "uri":os.getenv("ZILLIZ_CLOUD_URI") ,
    "user":os.getenv("ZILLIZ_CLOUD_USERNAME") ,
    "password":os.getenv("ZILLIZ_CLOUD_PASSWORD") ,
    # "token": ZILLIZ_CLOUD_API_KEY,  # API key, for serverless clusters which can be used as replacements for user and password
    "secure": True,
    },
)

# create vector database
def create_vectorDB(collection_name):
    docs = get_docs(collection_name)
    initialize_embeddings()
    global vector_db
    vector_db = Milvus.from_documents(
        docs,
        embeddings,
        collection_name=collection_name,
        connection_args={
            "uri":os.getenv("ZILLIZ_CLOUD_URI") ,
            "user":os.getenv("ZILLIZ_CLOUD_USERNAME") ,
            "password":os.getenv("ZILLIZ_CLOUD_PASSWORD") ,
            # "token": ZILLIZ_CLOUD_API_KEY,  # API key, for serverless clusters which can be used as replacements for user and password
            "secure": True,
        },
    )
     
def get_chatmemory(user_id):

    history = PostgresChatMessageHistory(
        connection_string=os.getenv("POSTGRES_CONNECTION_STRING"),
        session_id=user_id,
    )
    memory_postgres = ConversationBufferWindowMemory(k=3 , memory_key="history" , chat_memory= history, input_key="question")
    return memory_postgres

# create vectorDB

def ask_ai(companyName , query):
    # user_memory = get_chatmemory("{}_user_prodTest".format(companyName))
    user_memory = get_chatmemory(companyName)
    load_vectorDB(companyName)
    posgres_qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=vector_db.as_retriever(),
        # verbose=True,
        chain_type_kwargs={
            # "verbose": True,
            "prompt": prompt,
            "memory": user_memory
        }
    )

    res = posgres_qa(query)
    return res["result"]


# if __name__ == "__main__" :
    # main()