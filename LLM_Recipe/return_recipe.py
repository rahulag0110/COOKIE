from LLM_Recipe.prompt_generator import prompt_generator

from langchain.chat_models import ChatOpenAI

def return_recipe(pantry, chat_input):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-3.5-turbo")
    prompt = prompt_generator(pantry, chat_input)
    
    answer = llm(prompt)
    
    return answer