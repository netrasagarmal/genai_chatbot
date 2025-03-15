# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from ... import openai_api_key

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


# ## Prompt Template

# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","You are a helpful assistant. Please response to the user queries"),
#         ("user","Question:{question}")
#     ]
# )

# # openAI LLm 
# llm=ChatOpenAI(model="gpt-3.5-turbo")
# output_parser=StrOutputParser()
# chain=prompt|llm|output_parser


import sys
import os

# Get the absolute path of folder A
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# Add folder A to sys.path
sys.path.append(parent_dir)

# Now you can import abc.py
import openai_api_key

# Example function call from abc.py (if it has one)
# abc.some_function()

print(openai_api_key.OPENAI_API_KEY)
