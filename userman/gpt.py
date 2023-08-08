import os
import openai
import json
from .prompt import prompts
openai.api_key = "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"

def curriculum_generator(user_data):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
        {"role": "system", "content": prompts["curriculum_steps"]},
        {"role": "user", "content": json.dumps(user_data)}
    ]
    )
    print("curriculum created!")
    return completion.choices[0].message["content"]

def pathway_builder(curriculum_text):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
        {"role": "system", "content": "You are an expert learning pathway creator from 'Team Pathway'. You build learning pathway document for our customers based on the analysed curriculum requirements. This document is for them to keep, revisit and stay motivated."},
        {"role":"user", "content": prompts["document_create"]},
        {"role": "user", "content": curriculum_text}
    ]
    )
    print("Journey created!")
    return(completion.choices[0].message["content"])



def system_message_decorator(func):
    def wrapper(*args, **kwargs):
        user_data = kwargs['user_data']
        system_message = {"role": "system", 
                          "content": f"You are an amazingly helpful language model AI developed by OpenAI, and you're currently assisting an application called Pathway. Pathway creates personalized learning journeys for individuals. It crafts a curriculum and sends motivational and progress-tracking messages to users, helping them achieve their learning goals. The user's name is '{user_data['name']}', and their learning goal is '{user_data['learning_goal']}' with focus on '{user_data['sub_skills']}. They are set to reach this goal by {user_data['target_date']}'."}
        user_message = func(*args, **kwargs)
        messages = [system_message, user_message]
        return messages
    return wrapper

@system_message_decorator
def introductory_message(user_data):
    message = {"role": "user", 
               "content": prompts["intro_notification"]}
    print(message)
    return(message)


def generate_introductory_message(user_data):
    message = introductory_message(user_data=user_data)
    print(message)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=message
    
    )
    return(completion.choices[0].message["content"])

@system_message_decorator
def daily_plan_builder(user_journey, user_data):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
        {"role": "system", "content": "Here's the learning journey created for the user:\n"+user_journey},
        {"role":"user", "content": prompts["daily_plan_generator"]},
    ]
    )
    print("Journey created!")
    return(completion.choices[0].message["content"])