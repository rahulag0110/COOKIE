from chat_prompt_genetator import chat_prompt_generator

from langchain.chat_models import ChatOpenAI

def chat_with_recipe(recipe, chatInput):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-4")
    prompt = chat_prompt_generator(recipe, chatInput)
    
    answer = llm(prompt)
    
    return answer.content