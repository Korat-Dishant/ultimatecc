import os
from langchain.memory import PostgresChatMessageHistory




def clearMemory(id):
    history = PostgresChatMessageHistory(
    connection_string=os.getenv("POSTGRES_CONNECTION_STRING"),
    session_id=id,)
    history.clear()
