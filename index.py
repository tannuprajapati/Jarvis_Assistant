import os
import google.generativeai as genai
from main import *
# Set the API key
os.environ['GOOGLE_API_KEY'] = "API_KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Create the model
def create(input_text):
    generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
   }
    safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

    chat_session = model.start_chat(
  history=[]
)

# Replace 'INSERT_INPUT_HERE' with your actual input text
    
    response = chat_session.send_message(input_text)
    print(response.text)
    say(response.text)
    

