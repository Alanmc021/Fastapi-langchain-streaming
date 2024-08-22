# FastAPI LangChain Chat

This project is a real-time chat API built using FastAPI and LangChain, integrated with OpenAI for natural language processing. The application streams responses to user queries, providing dynamic answers based on the context retrieved from a vector store.

## Features

- **FastAPI**: Framework for building the API.
- **LangChain**: Utilized for chaining together prompts and models to generate responses.
- **OpenAI**: Used for embedding and generating context-based answers.
- **Chroma**: Vector store used to retrieve relevant documents based on the input query.
- **Streaming Responses**: Answers are streamed in real-time using `text/event-stream`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-langchain-chat.git
