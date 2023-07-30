import os
from typing import List
import textbase
from textbase.message import Message
from textbase import models


# or from environment variable:
models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = "You are chatting with an AI. you can ask or talk about anything you like."


@textbase.chatbot("talking-bot")

def on_message(message_history: List[Message], state: dict = None):
    
    message_history = [{'role':'system','content':"you are a mental health detector bot"},
                       {'role':"user",'content':"i want to know how to manage stress"},
                       {"role":"assitant","content":"""There are many ways by which you can manage stress like 
                        connect with others
                        manage social meadia time
                        do meditation regulary
                        Do excercise"""},
                        {"role":"user","content":"perfect ! thanks for giving me advice"}]
    state : dict = {
        "context":"""you are an mental health chat bot , So always gives the advice which help the user to come out from depression or manage the stress"""
    }
    
    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
        temperature=0.9
    )
    message_history.append(bot_response)

    return bot_response, state