from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import sys
import os

# Get the absolute path of folder A
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# Add folder A to sys.path
sys.path.append(parent_dir)

# Now you can import abc.py
import openai_api_key



# print(openai_api_key.OPENAI_API_KEY)

question = "Hi, how are you?"
## Prompt Template

prompt=[
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]

# openAI LLm 
llm=ChatOpenAI(model="gpt-4o", api_key=openai_api_key.OPENAI_API_KEY)

response = llm.invoke(prompt)
print(response)
