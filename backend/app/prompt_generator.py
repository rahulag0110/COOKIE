from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

system_message_template = """
You are a CookieGPT, helpful AI assistant that provides help with suggesting recipes and help a user cook based on what the users have in their pnatry.

These are the ingedrients and materials user has in their pantry:
{pantry}

Return a recipe based on it.
"""

human_message_template = "While searching for a recipe keep this in mind: {chat_input}"
ai_message_template = "{ai_text}"

system_message_prompt = SystemMessagePromptTemplate.from_template(system_message_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_message_template)
ai_message_prompt = AIMessagePromptTemplate.from_template(ai_message_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

def prompt_generator(pantry, chat_input):
    prompt = chat_prompt.format_prompt(pantry = pantry, chat_input = chat_input).to_messages()
    return prompt