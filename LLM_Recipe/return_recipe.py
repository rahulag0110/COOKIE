from LLM_Recipe.recipe_prompt_generator import recipe_prompt_generator

from langchain.chat_models import ChatOpenAI

def return_recipe(input, outputFormat, chatInput):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-4")
    prompt = recipe_prompt_generator(input, outputFormat, chatInput)
    
    answer = llm(prompt)
    
    return answer