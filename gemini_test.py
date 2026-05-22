import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

api_key = os.getenv("Gemini_API_Key")

client=genai.Client(api_key=api_key)


print("Welcome to AI Interview Assistant! ")
print("-------------------------------------")
question="Tell me about yourself"
print(question)
user_answer=input("Enter your answer")

prompt = f"""
You are an interview coach helping a fresher prepare for jobs.

The interview question was: "{question}"
The candidate answered: "{user_answer}"

Give feedback in this format:
SCORE: X/10
GOOD POINTS: (2 points)
IMPROVE: (2 points)
BETTER ANSWER: (write a better version in 3 sentences)
"""
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)

