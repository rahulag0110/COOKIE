import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "../img2.jpeg"

def img_to_pantry_list(image_path):

# Getting the base64 string
  base64_image = encode_image(image_path)

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
            "text": """ Identify the food ingedrients and take a guess in how many days it will expire in this image. If you have no idea about expiration date leave it blank. in the following format ["ingedrient1 (expiry)", "ingedrient2 (expiry)", ...]. Example: ["carrot (2 days)", "tomato (3 days)"] """
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
  return content

print(type(img_to_pantry_list(image_path)))