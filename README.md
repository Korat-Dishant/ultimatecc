
# UltimateCC

this is a RAG (Retrieval augmented generation) applicatoin. using this application you can create customized chatbot which would answer to queries base on your provided data.

## Architecture

- creating index

![Frame 37](https://github.com/Korat-Dishant/ultimatecc/assets/86142546/b37bd6ac-504e-4044-bb0c-88bfc1c86b6d)

- first of all you have to create a company on CMS and add products for this company.
- after creating the new data or updating data for any company call the backend on updateindex and provide company name.
- after sending the api to update index the backend would fetch data from CMS and then create the vectors of this data using milvus hosted on zilliz. (for this purpose it uses huggingface inference API to create embeddings)
  

- answering queries

 ![Frame 39](https://github.com/Korat-Dishant/ultimatecc/assets/86142546/acd938bc-4ec7-40fb-82d5-19619778a8b8)

 - when you send your query and company name on /ask, the backend would retrive previous chat history and perform similarity search on vector data stored on zilliz.
 - after getting the context and history the backend would call the llm to generate human like response. (currently this application is using gemini-pro)
 - this response is stored in postgres database as chat history.


## Swagger Docs

<img width="884" alt="image" src="https://github.com/Korat-Dishant/ultimatecc/assets/86142546/5bd72da0-a993-44e6-a84f-d41e4dcf66b2">

<img width="725" alt="image" src="https://github.com/Korat-Dishant/ultimatecc/assets/86142546/6c63be37-5276-4f1e-ae6a-b038f2917999">


## Note 
some times while asking questions about previously asked question you might receive something like this "I do not have related data to answer this question". the reason for this is reasoning capabities of LLM. changing LLM to Open-AI model gpt-3.5-turbo-instruct I have found the accuracy of response to be increased. but both the model have their pros and cons I am not blaming gemini as its currently free and still better than many LLMs but i am waiting to try gemini-ultra.

## Strapi 
snapshots of CMS
<img width="914" alt="image" src="https://github.com/Korat-Dishant/ultimatecc/assets/86142546/44b0601d-47b1-462c-b3ee-bb9cb922ec43">

<img width="764" alt="image" src="https://github.com/Korat-Dishant/ultimatecc/assets/86142546/dda0deb6-024e-4f4b-8495-76fd1e1ead40">

<img width="757" alt="image" src="https://github.com/Korat-Dishant/ultimatecc/assets/86142546/6cb9548b-f240-4a34-a11e-1618ae73481d">


- you can checkout the github repo of CMS for this project (strapi) [here](https://github.com/Korat-Dishant/ultimatecc-CMS)


## Server

this entire project is hosted on render.

<img width="733" alt="image" src="https://github.com/Korat-Dishant/ultimatecc/assets/86142546/d6cdec32-f166-44bb-b21a-d053d4403066">



## Links 
- Swagger Docs of chatbot API : [ultimatecc-backend](https://ultimatecc-backend.onrender.com/docs)
- CMS url : [strapi](https://ultimatecc-strapi.onrender.com/)

Note : currently you can only access the swagger docs for this project. but if you need to add product data of your own company and want the chatbot to respond based on your organization's data you can contact me via :
- [gmail](mailto:koratdishant536631@gmail.com)
- [Linkedin](https://www.linkedin.com/in/dishant-korat-297246228/)



