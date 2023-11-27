from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_message_template = """
You are a CookieGPT, helpful AI assistant that provides help with suggesting recipes and help a user cook based on what the users have in their pnatry.

These are the ingedrients and their respective expiration dates user has in their pantry. If the expiration date is not specified, try to guess the expiration date based on the ingredient type. For example, eggs expire in 3 weeks, milk expires in 1 week, salt never expires etc.:
{pantry}
Suggeet a recipie such that the ingedrients which are about to expire first get used first. You don't have to use all the ingedrients. This the whole pantry. Each and every ingedrient is not be used for every recipie.

Here is the time of the day to eat of the recipe user wants to cook. Example: Breakfast, Lunch, Dinner. If its none you are free to sugeest most preferable recipe based on the ingredients in the pantry.:
{timeOfDay}

Here is the cuisine/region/style of the recipe user wants to cook. If its none you are free to suggest any recipe.:
{cuisine}

Suggest {numberOfRecipes} recipes based on the ingredients in the pantry. Suggest such that recipies are very differnt from each other. If the number of recipes is not specified, suggest 1 recipe.:

Number of servings of the recipe: {numberOfServings}. If the number of servings is not specified, suggest a recipe for 2 serving.

Your output should be strictly in the following format. It should be a list of JSON and JSON only. Be very very careful about the format.:
{outputFormat}
You are basically returning a list of json where json is for a recipie. So the number of JSON you generate should be equal to the number of recipes you are suggesting.
"""

human_message_template = "While searching for a recipe keep this in mind: {chatInput}"
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