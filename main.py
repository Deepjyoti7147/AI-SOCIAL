import pathlib
import textwrap
import google.ai.generativelanguage as glm
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key from the .env file
# api_key = os.getenv("API_KEY")


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))




GOOGLE_API_KEY= os.getenv("API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

'''
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
'''

model = genai.GenerativeModel('gemini-pro')

prompt1 = input("Enter a prompt: ")

response = genai.generate_text(prompt=prompt1)
print(response.result)  # cold.

'''response = model.generate_content("What is the meaning of life?")
response.prompt_feedback
for chunk in response:
  print(chunk.text)
  print("_"*80)'''