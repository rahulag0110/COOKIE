from LLM_Recipe.return_recipe_whitout_json import return_recipe_without_json
input = {
    "pantry": "[chicken drumsticks, chives, carrots, potatoes, tomatoes, onions, garlic, mayonaise, corn, papaya, grapes, yogurt, chilli, green beans]",
    "diet": "strict diet",
    "cuisine": "indian or korean",
    "prevRecipe": "",
    "feedback": ""   
}

recipe = return_recipe_without_json(input,"I want something delicious and good looking for a dinner party.")

print(recipe)

input["prevRecipe"] = recipe
input["feedback"] = "I don't want to use chicken today. Can you suggest something else? Maybe something not indian"

recipe = return_recipe_without_json(input,"I want something delicious and good looking for a dinner party.")
print(recipe)
