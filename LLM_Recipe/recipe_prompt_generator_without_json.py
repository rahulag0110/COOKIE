from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_message_template = """
You are a CookieGPT, helpful AI assistant that provides help with suggesting recipe and help a user cook based on following information:
{pantry} : These are the ingedrients and their respective expiration dates (guess if not specified) user has in their pantry. Suggest a recipie with expiring ingedrient first. You don't need to use up all the ingedrients but the recipe you suggest should not contain any ingedrients other than these.
Diet ststus - {diet} : This is the diet user is following. It can be either strict diet (low carbs and fat) or nomal diet.
Cuisine - {cuisine} If none, you are free to suggest any recipe.
You might have generated a recipie based on the above details. Here is a previous recipe you generated {prevRecipe} and user has the following feedback {feedback}. Modify the recipe accordingly and return a new recipe.
Output a single recipie. Include the following in the output in the same order: recipeName, ingedrientsUsed, servings, steps.Don't include any greeting or any extra information in the output.
"""

human_message_template = "Don't have any greetins or any extra information in the output. {chatInput}"
ai_message_template = "{ai_text}"

system_message_prompt = SystemMessagePromptTemplate.from_template(system_message_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_message_template)
ai_message_prompt = AIMessagePromptTemplate.from_template(ai_message_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

def recipe_prompt_generator_without_json(input, chatInput):
    prompt = chat_prompt.format_prompt(pantry = input["pantry"], diet = input["diet"], cuisine = input["cuisine"], prevRecipe = input["prevRecipe"], feedback = input["feedback"] , chatInput = chatInput).to_messages()
    return prompt