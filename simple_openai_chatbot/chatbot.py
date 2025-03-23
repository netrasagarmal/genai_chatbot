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

async def get_llm_answer(question:str):

    user_prompt = """
    Please answer the following question given below, if you dont know then simply say no. 
    
    Question: {question}
                
    """

    ## Prompt Template
    prompt=[
            ("system","You are a helpful assistant. Please response to the user queries"),
            ("user",)
        ]

    # openAI LLm 
    # llm = ChatOpenAI(
    #     model="gpt-3.5-turbo",
    #     api_key=openai_api_key.OPENAI_API_KEY,  # if you prefer to pass api key in directly
    # )

    # response = llm.invoke(prompt)
    return "hi"
    
