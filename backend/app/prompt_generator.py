from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_message_template = """
You are a CookieGPT, helpful AI assistant that provides help with suggesting recipes and help a user cook based on following information:
{pantry} : These are the ingedrients and their respective expiration dates (guess if not specified) user has in their pantry. Suggest a recipie with expiring ingedrient first. You don't need to use up all the ingedrients.
{timeOfDay}, {cuisine} : Here is the time of the day and cuisine/region/style user wants to cook. If its none you are free to suggest any recipe.
{numberOfRecipes}, {numberOfServings} : Number of recipies you suggest and proprtion of the recipe.
If any of the above information is not provided, you are free to assume it.

Output a list of recipes. Each recipe should be strictly a JSON with the following keys: recipeName, ingedrientsUsed, servings, steps. So the output should be in the following format: [JSON, JSON, JSON, ...]. Don't include any greeting or any extra information in the output.
"""

human_message_template = "Don't have any greetins or any extra information in the output. Just follow the format very carefully."
ai_message_template = "{ai_text}"

system_message_prompt = SystemMessagePromptTemplate.from_template(system_message_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_message_template)
ai_message_prompt = AIMessagePromptTemplate.from_template(ai_message_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

input = {
    "pantry": "[Capsicum (3 days), carrots (2 days), grapes, yogurt, chilli, green beans (1 day)]",
    "timeOfDay": "Lunch",
    "cuisine": "Indian",
    "numberOfRecipes": 2,
    "numberOfServings": 5,    
}

outputFormat = """ [{
    "recipeName": "Name of the recipe",
    "ingedrientsUsed": "Ingredients used in the recipe",
    "servings": "Number of servings",
    "steps": "Steps to cook the recipe mentioned clearly in a numbered list",
}, {...}, {...}] """

def prompt_generator(input, outputFormat, chatInput):
    prompt = chat_prompt.format_prompt(pantry = input["pantry"], timeOfDay = input["timeOfDay"], cuisine = input["cuisine"], numberOfRecipes = input["numberOfRecipes"], numberOfServings = input["numberOfServings"], outputFormat = outputFormat, chatInput = chatInput).to_messages()
    return prompt