from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_message_template = """
You are a CookieGPT, helpful AI assistant that provides help with suggesting recipes and help a user cook based on following information:
{pantry} : These are the ingedrients and their respective expiration dates (guess if not specified) user has in their pantry. Suggest a recipie with expiring ingedrient first. You don't need to use up all the ingedrients but the recipe you suggest should not contain any ingedrients other than these.
Diet ststus - {diet} : This is the diet user is following. It can be either strict diet (low carbs and fat) or nomal diet.
Spice Level - {spiceLevel}
Output a list of recipes. Each recipe should be strictly a JSON with the following keys: recipeName, ingedrientsUsed, servings, steps. So the output should be in the following format: [JSON, JSON, JSON, ...]. Don't include any greeting or any extra information in the output.
"""

# {timeOfDay}, {cuisine} : Here is the time of the day and cuisine/region/style user wants to cook. If its none you are free to suggest any recipe.
# {numberOfRecipes}, {numberOfServings} : Number of recipies you suggest and proprtion of the recipe.


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
    prompt = chat_prompt.format_prompt(pantry = input["pantry"], diet = input["diet"], spiceLevel = input["spiceLevel"], outputFormat = outputFormat, chatInput = chatInput).to_messages()
    return prompt