import openai
import os
import openai
import streamlit as st
import requests
from openai import OpenAI

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def translate(text, source_language, target_language):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a sentence in "+ source_language
                +", and your task is to translate it into " + target_language 
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    
    return response.choices[0].message.content