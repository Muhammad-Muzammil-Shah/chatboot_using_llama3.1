from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Directly set the OpenAI API key (replace with your actual key)
#api_key = "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"

# Initialize OpenAI LLM with the API key
#llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)
llm=Ollama(model="llama2")
#output_parser=StrOutputParser()
#chain=prompt|llm|output_parser

# Define prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit framework setup
st.title('LangChain Demo With OpenAI API')
input_text = st.text_input("Search the topic you want")

# Initialize output parser
output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Process the input and display the result
if input_text:
    try:
        result = chain.invoke({'question': input_text})
        st.write(result)
    except Exception as e:
        if "insufficient_quota" in str(e):
            st.error("You have exceeded your current quota. Please check your plan and billing details.")
        else:
            st.error(f"An error occurred: {e}")
