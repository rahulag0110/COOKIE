import json
import os
import io

from prompt_generator import prompt_generator

from langchain.chat_models import ChatOpenAI

def return_recipe(pantry, chat_input):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-3.5-turbo")
    prompt = prompt_generator(pantry, chat_input)
    
    answer = llm(prompt)
    
    return answer

# Imports for the REST API
from flask import Flask, request, jsonify

# Imports for image procesing
# from PIL import Image

# Imports for prediction
# from predict import predict_url

app = Flask(__name__)

# 4MB Max image size limit
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024


@app.route('/')
def index():
    print(return_recipe("[Chicken Breast, onions, tomatoes, chillies, oil, spices]", "I want to something quick and easy but Indian style.").content)
    return jsonify({"test": [return_recipe("[Chicken Breast, onions, tomatoes, chillies, oil, spices]", "I want to something quick and easy but Indian style.").content]})



@app.route('/predict', methods=['POST'])

def predict_url_handler():
    try:
        # image_url = json.loads(request.get_data().decode('utf-8'))['url']
        # results = predict_url(image_url)
        data = json.loads(request.get_data().decode('utf-8'))
        pantry = data['pantry']
        chat_input = data['chat_input']
        results = return_recipe(pantry, chat_input).content
        return jsonify({"result": results})
    except Exception as e:
        print('EXCEPTION:', str(e))
        return 'Error processing data'


if __name__ == '__main__':
    #     # Load and intialize the model
    #     initialize()

    # Run the server
    app.run(host='0.0.0.0', port=4004)