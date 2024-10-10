from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assitant. Please write accurate responses for the user queries"),
        ("user", "Question: {question}")
    ]
)

# Strealit framework
st.title("LangChain Chatbot with Ollama and Llama3.2")
input_text = st.text_input("Ask anything...")


llm = OllamaLLM(model="llama3.2:1b")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))