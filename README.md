# DocumentLoaderRAG

A LangChain and Groq-powered RAG document loading and processing workspace.

## Features
- **Document Loaders**:
  - `TextLoader`: Loading plain text documents with LCEL summarization chains (`textLoader.py`)
  - `WebBaseLoader`: Web scraping and parsing (`webBaseLoader.py`)
  - `DirectoryLoader`: Bulk file extraction from directories (`directory_loader.py`)
  - `PyPDFLoader`: PDF document extraction (`PyPdfLoader.py`)
- **LLM Integration**: Chat models via `langchain-groq` and `init_chat_model` (e.g., `qwen/qwen3.8-27b`, `openai/gpt-oss-120b`).

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prthm45-kanha/DocumentLoaderRAG.git
   cd DocumentLoaderRAG
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirement.txt
   ```
   *Or using `uv`:*
   ```bash
   uv sync
   ```

3. **Configure Environment Variables**:
   Copy `.env.example` to `.env` and set your Groq API key:
   ```bash
   cp .env.example .env
   ```
   Add your API key:
   ```env
   GROQ_API_KEY="your_groq_api_key_here"
   ```

4. **Run Examples**:
   ```bash
   python textLoader.py
   python webBaseLoader.py
   python directory_loader.py
   python PyPdfLoader.py
   ```
