import os
from src.llm_client import generate_response
from src.utils import load_prompt

folder="prompts"
filename="technical_prompt.txt"
path=os.path.join(folder,filename)

prompt=load_prompt(path)
# print(prompt)
response=generate_response(prompt)

