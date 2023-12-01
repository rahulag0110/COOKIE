import json
import os
import io

from image_read import img_to_pantry_list

from langchain.chat_models import ChatOpenAI
from recipe_prompt_generator import recipe_prompt_generator
import json

def return_recipe(input, outputFormat, chatInput):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-4")
    prompt = recipe_prompt_generator(input, outputFormat, chatInput)
    
    answer = llm(prompt)
    str_form = answer.content
    json_form = json.loads(str_form)
    return json_form

# Imports for the REST API
from flask import Flask, request, jsonify

# Imports for image procesing
# from PIL import Image

# Imports for prediction
# from predict import predict_url

app = Flask(__name__)

# 4MB Max image size limit
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024


@app.route('/',  methods=['POST'])
def index():

    return jsonify({"recipeName": "test", 
                    "ingredientsUsed": ["chicken", "pork", "oil"],
                    "steps": ["1. test", "2. test2", "3. test3"]})



@app.route('/predict', methods=['POST'])

def predict_url_handler():
    try:
        # image_url = json.loads(request.get_data().decode('utf-8'))['url']
        # results = predict_url(image_url)
        input = {
            "pantry": "",
            "timeOfDay": "Lunch",
            "cuisine": "Asian",
            "numberOfRecipes": 1,
            "numberOfServings": 5,    
        }

        outputFormat = """ [{
            "recipeName": "Name of the recipe",
            "ingedrientsUsed": "Ingredients used in the recipe",
            "servings": "Number of servings",
            "steps": "Steps to cook the recipe mentioned clearly in a numbered list",
        }, {...}, {...}] """

        data = json.loads(request.get_data().decode('utf-8'))
        input["pantry"] = data['pantry']
        chat_input = data['chat_input']

        results = return_recipe(input, outputFormat, chat_input).content
        return results
    except Exception as e:
        print('EXCEPTION:', str(e))
        return 'Error processing data'
    
@app.route('/image', methods=['POST'])

def get_pantries_from_image():
    try:
        data = json.loads(request.get_data().decode('utf-8'))
        imagebase64 = data['image']
        result = img_to_pantry_list(imagebase64)
        return jsonify({"result": result})
    except Exception as e:
        print("EXCEPTION: ", str(e))
        return 'Error processing image'



if __name__ == '__main__':
    #     # Load and intialize the model
    #     initialize()

    # Run the server
    app.run(host='0.0.0.0', port=4004)