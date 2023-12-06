from LLM_Recipe.recipe_prompt_generator_without_json import recipe_prompt_generator_without_json

from langchain.chat_models import ChatOpenAI

def return_recipe_without_json(input, chatInput):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-4")
    prompt = recipe_prompt_generator_without_json(input, chatInput)
    
    answer = llm(prompt)
    str_form = answer.content
    return str_form