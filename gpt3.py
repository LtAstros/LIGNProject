from config import OPENAI_API_KEY
import openai
import sys
openai.api_key = OPENAI_API_KEY

def try_gpt(json):
    # Get user's question
    with open('prompt_2019_2.txt') as f:
        prompt_text = f.read()
    
    if json == "":
        return

    # Complete the prompt with user question and call OpenAI
    prompt = f'{prompt_text} {json}\Commentary:\n```'
    response = openai.Completion.create(model="text-davinci-002",
                                        prompt=prompt,
                                        temperature=0.75,
                                        max_tokens=512,
                                        stop='```')
    return response["choices"][0]["text"]