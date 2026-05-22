import google.genai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("Gemini_API_Key")
client=genai.Client(api_key=api_key)

prompt="your are a AI interview assistent and give feedback of user response"

response=client.models.generate_content(
    model='gemin-2.5-flash',
    contents=prompt
)