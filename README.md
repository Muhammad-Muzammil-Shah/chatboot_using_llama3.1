# Chatbot Using Llama2 (Langchain + Streamlit)

## Overview
This project is a simple chatbot web app built with Python, Streamlit, and Langchain. It uses the Llama2 language model (via Ollama) to answer user questions interactively. The app demonstrates how to integrate LLMs with a prompt template and a user-friendly interface.


# Chatbot Using Llama2 (Langchain + Streamlit)

## Overview
This project is a simple chatbot web app built with Python, Streamlit, and Langchain. It uses the Llama2 language model (via Ollama) to answer user questions interactively. The app demonstrates how to integrate LLMs with a prompt template and a user-friendly interface.

---

## 🚀 How It Works
- Uses Langchain's prompt template to structure user queries
- Integrates Llama2 model via Ollama for generating responses
- Streamlit provides a web interface for user input and displaying answers
- Environment variables are loaded using `python-dotenv` for API keys and configuration

---

## 📦 Main Files
- `app.py`: Streamlit app for chatbot interface and Llama2 integration
- `main.py`: Additional logic or entry point (if present)
- `requirements.txt`: List of required Python packages

---

## 🛠️ Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Enter your question in the input box and get answers from Llama2

---

## 💡 Example Code
```python
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search the topic you want")
llm = Ollama(model="llama2")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input_text:
    st.write(chain.invoke({"question": input_text}))
```

---

## ✨ Features
- Interactive chatbot using Llama2
- Prompt engineering with Langchain
- Web UI with Streamlit
- Easy to extend for other LLMs or prompt templates

---

## 📃 License
MIT License
