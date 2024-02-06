from fastapi import FastAPI , Header
from typing import Annotated, List, Union

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from helper import ask_ai , initialize_embeddings , initialize_LLM , create_vectorDB
from clearBuffer import clearMemory
import os 
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(title="Customized Chatbot", description="Customized Chatbot API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# initialize_query_engines()

# @app.post("/extract", summary="pass value using param", tags=["Chatbot"])
# def extract(data: str) -> str:
#     return str(ask_ai(data))


initialize_LLM("gemini")
initialize_embeddings()

@app.post("/ask" ,  summary="pass value using header")
async def read_items(user_query:str , company_name:str):
    return {"response": str(ask_ai(companyName = company_name , query= user_query)) }


@app.post("/updateIndex" ,  summary="update or create index ")
async def read_items(companyName:str  ):
    create_vectorDB(companyName)


@app.post("/clearBuffer" ,  summary="clear chat history buffer ")
async def read_items(buffer_Name:str  ):
    clearMemory(buffer_Name)



# get available companies name 


@app.get("/")
async def index():
    return {"message": "Hello World use //extract for api"}


# if __name__ == "__main__":
#     print(ask_ai("what is my name ?"))
