from typing import List, Dict
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OAI_KEY")

def completion(prompt: str, max_tokens: int = 20): 
    response = openai.Completion.create(
        model= "text-davinci-003",
        prompt= prompt,
        max_tokens= max_tokens,
        temperature= 0.7,
        stream=True,
    )    
    return response

def chatCompletion(messages: List[Dict]):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages,
        stream=True,
    )
    return response
