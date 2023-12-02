from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_message_template = """
You are a CookieGPT, helpful AI assistant that provides help with modifying recipes and help a user cook based on following information:
This is the recipie user wants to cook:
{recipe}
Listen to the user's message carefully and provide help with anything the user needs. User may ask you to provide details about a particular step or ask you change certain things like spice level. Modify recipe accordingly.
Don't have any greetins or any extra information in the output. Your output will be displayed directly to user so don't return and JSON or list or anything like thet. Simply return the text you want to display to the user.
"""

# {timeOfDay}, {cuisine} : Here is the time of the day and cuisine/region/style user wants to cook. If its none you are free to suggest any recipe.
# {numberOfRecipes}, {numberOfServings} : Number of recipies you suggest and proprtion of the recipe.


human_message_template = "{chatInput}"
ai_message_template = "{ai_text}"

system_message_prompt = SystemMessagePromptTemplate.from_template(system_message_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_message_template)
ai_message_prompt = AIMessagePromptTemplate.from_template(ai_message_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

def chat_prompt_generator(recipe, chatInput):
    prompt = chat_prompt.format_prompt(recipe = recipe, chatInput = chatInput).to_messages()
    return prompt