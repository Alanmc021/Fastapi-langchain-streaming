# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware 
# from app.controllers import agent
# from app.controllers import gerar_pecas_controller
# from app.controllers import analizar_imagens_controller
# from app.controllers import analizar_imagens
# from app.controllers import stream_chat

# app = FastAPI(
#     title="LangChain Server",
#     version="1.0",
#     description="API server with multiple endpoints for legal document creation",
# )

# # Configuração do CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Permite todas as origens; ajuste conforme necessário
#     allow_credentials=True,
#     allow_methods=["*"],  # Permite todos os métodos; ajuste conforme necessário
#     allow_headers=["*"],  # Permite todos os cabeçalhos; ajuste conforme necessário

# )

# # Incluir as rotas de cada endpoint
# app.include_router(agent.router) 
# app.include_router(gerar_pecas_controller.router) 
# app.include_router(analizar_imagens_controller.router) 
# app.include_router(analizar_imagens.router) 
# # app.include_router(stream_chat.router) 

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)
 
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

embedding_function = OpenAIEmbeddings()

docs = [
    Document(
        page_content="the dog loves to eat pizza", metadata={"source": "animal.txt"}
    ),
    Document(
        page_content="the cat loves to eat lasagna", metadata={"source": "animal.txt"}
    ),
]

db = Chroma.from_documents(docs, embedding_function)
retriever = db.as_retriever()


template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI(temperature=0, streaming=True)

retrieval_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

app = FastAPI()

async def generate_chat_responses(message):
    async for chunk in retrieval_chain.astream(message):
        content = chunk.replace("\n", "<br>")
        yield f"data: {content}\n\n"


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.get("/chat_stream/{message}")
async def chat_stream(message: str):
    return StreamingResponse(generate_chat_responses(message=message), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
 