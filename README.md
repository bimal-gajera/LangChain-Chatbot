# LangChain-Chatbot

This project includes two chatbot implementations using LangChain, OpenAI API, and Ollama It integrates **LangSmith** for tracing and tracking enabling monitoring and debugging  of the chatbot’s interactions.

## Overview
This project implements two chatbot applications using the [LangChain](https://www.langchain.com/) framework.


## 1. OpenAI Chatbot (app.py)
- Uses the GPT-4o mini model via the LangChain framework.

## 2. Ollama Chatbot with Llama 3.2:1b (local_llama_app.py)
- Uses the Llama 3.2 model via the `OllamaLLM` class in LangChain.

### Features
- Simple, interactive interface powered by Streamlit.
- **LangSmith Tracking**: Tracks chatbot interactions for monitoring and debugging.

### env setup
To run the code, create a file `.env` in the project folder and write all the API keys in this file.

For reference,
```
LANGCHAIN_API_KEY = "key1"
OPENAI_API_KEY = "key2"
LANGCHAIN_PROJECT = "Name of the project"
```
These variables are accessed in the main code, the .py file.

### Ollama
Ollama allows you to run many open-source models locally on a machine.

### Install Ollama:
Visit [https://ollama.com/](https://ollama.com/)

After installation, run the below command in the terminal to download/run LLM.
```
ollama run llama3.2:1b
```

### Running the App
To run the  chatbot, use the following command:
```
streamlit run app.py
```
```
streamlit run local_llama_app.py
```