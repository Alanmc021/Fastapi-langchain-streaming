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
    ```
2. Navigate to the project directory:
    ```bash
    cd fastapi-langchain-chat
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Create a `.env` file in the root directory with your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your-api-key-here
    ```

## Usage

Start the FastAPI server:
```bash
uvicorn main:app --reload
