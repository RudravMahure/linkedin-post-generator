#importing functions from different files
from llm import llm_model_call

print("What do you want to post about?")

#this line will take topic input
topic = input("Enter your topic here:")

response = llm_model_call(topic)

print(response)