from chat_prompt_genetator import chat_prompt_generator

from langchain.chat_models import ChatOpenAI

def chat_with_recipe(recipe, chatInput):

    llm = ChatOpenAI(openai_api_key="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", temperature = 0, model = "gpt-4")
    prompt = chat_prompt_generator(recipe, chatInput)
    
    answer = llm(prompt)
    
    return answer.content