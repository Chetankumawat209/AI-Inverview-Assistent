
import os
from google import genai
from dotenv import load_dotenv
       




def generate_response(prompt):
    
    load_dotenv()
    try:
        key=os.getenv("Gemini_API_Key")
        client=genai.Client(api_key=key)
    
    except Exception as e:
        print(e)
        print(f"Error{str(e)}")

    a=0
    while a<5:
        a+=1
        try:
            response=client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            print(response.text,"\n")
            prompt=input("Enter your answer \n")
            
        except Exception as e:
            print(f"Error{str(e)}")
            print("model not found")
            break