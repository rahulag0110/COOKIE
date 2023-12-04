from LLM_Recipe.recipe_prompt_generator import recipe_prompt_generator
import json

from langchain.chat_models import ChatOpenAI

def return_recipe(input, chatInput, outputFormat):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-4")
    prompt = recipe_prompt_generator(input, chatInput, outputFormat)
    
    answer = llm(prompt)
    str_form = answer.content
    json_form = json.loads(str_form)
    return json_form