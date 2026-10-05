#importing standard libraries
from google import genai


#import functions from different files
from config import get_gemini_key
from prompts import get_system_prompt

#constant declare here
gemini_key = get_gemini_key() #this constants hold the gemini key value
system_prompt =  get_system_prompt() #this constant hold the system prompts value

def llm_model_call(prompt):
    client = genai.Client(api_key=gemini_key)
    
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents=prompt,
        config = {
            "system_instruction" : system_prompt
        }
    )
    return response.text