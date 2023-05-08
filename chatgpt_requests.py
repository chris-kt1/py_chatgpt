import requests
import argparse
from openai_apikey import API_key

#Set parameters for interaction with OPENAI API
API_endpoint = 'https://api.openai.com/v1/chat/completions'
AI_model = "gpt-3.5-turbo"

#Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("prompt", type=str, help="Include what you want the AI to generate. Be concise. Example:'Print current date'")
args = parser.parse_args()

# #Ask user for input(Uncomment for user input)
# prompt = input("Ask ChatGPT a question: ")

#Send input to openai
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_key
}
request_body = {
    "model": AI_model,
    "messages": [{"role": "user", "content": f"Write a python script to {args.prompt}. Only Provide code, no text."}]
}
print(request_body)
response = requests.post(API_endpoint, headers= request_headers, json=request_body)


#Receive response from openai
if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
    response_code = response.json()["choices"][0]["message"]["content"]
    with open("chatgpt_pythoncode.py", "w") as f:
        f.write(response_code)
else:
    print(f"Error: {str(response.status_code)}")

