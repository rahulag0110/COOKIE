from LLM_Recipe.recipe_prompt_generator import recipe_prompt_generator
import json

from langchain.chat_models import ChatOpenAI

def return_recipe(input, chatInput):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-4")
    prompt = recipe_prompt_generator(input, chatInput)
    
    answer = llm(prompt)
    str_form = answer.content
    json_form = json.loads(str_form)
    return json_form