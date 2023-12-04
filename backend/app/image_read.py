import base64
import requests
import ast

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
# image_path = "img2.jpeg"

def img_to_pantry_list(base64_image):

# Getting the base64 string

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": """ Identify the food ingedrients and return in the following format ["ingedrient1", ingedriernt2, ...]. Only return the list of ingedrients that are in the image. If you can't identify any ingedrients return []. Also just reutrn th ingedrients list and nothing else. I don't want any other text"""
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  content = response.json()["choices"][0]["message"]["content"]
  converted_list = ast.literal_eval(content)
  return converted_list

# print(type(img_to_pantry_list(image_path)))