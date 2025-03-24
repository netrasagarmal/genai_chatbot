from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import sys
import os
import json

# Get the absolute path of folder A
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# Add folder A to sys.path
sys.path.append(parent_dir)

# Now you can import abc.py
import openai_api_key

def create_prompt(system_prompt, user_question)->list:
    """ Create a prompt"""
    
    user_prompt = """
    Please answer the following question given below, if you dont know then simply say no. 
    
    Question: {}
                
    """.format(user_question)

    ## Prompt Template
    prompt=[
            ("system",system_prompt),
            ("user",user_prompt)
        ]
    return list(prompt)


async def get_llm_answer(question:str,
                         max_output_tokens = 1,
                        temperature = 0.0,
                        top_p = 0.50,
                        top_k = 50,
                        penealty = 0.0,
                        system_prompt = "You are a helpful assistant. Please response to the user queries"

)->str:
    """
    Function accepts Question and model parameters, creates prompt and then invokes llm model to get response """

    prompt = create_prompt(system_prompt = system_prompt, user_question = question)

    # openAI LLm 
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=openai_api_key.OPENAI_API_KEY,  # if you prefer to pass api key in directly
    )

    response = llm.invoke(prompt)
    print(response)
    print(type(response))
    # content = json.loads(response.content)
    # return content["content"]
    return "hi"
    
