from LLM_Recipe.return_recipe import return_recipe
input = {
    "pantry": "[chicken drumsticks, chives, carrots, potatoes, tomatoes, onions, garlic, mayonaise, corn, papaya, grapes, yogurt, chilli, green beans]",
    "diet": "strict diet",
    "cuisine": "indian or korean",
    "prevRecipe": "",
    "feedback": ""   
}
outputFormat = """{
    "recipeName": "ABC Recipe",
    "ingedrientsUsed": ["A", "B", "C"],
    "servings": 2,
    "steps": ["1. A step", "2. B step", "3. C step"]
}"""

recipe = return_recipe(input,"I want something delicious and good looking for a dinner party.", outputFormat)

print(recipe)

input["prevRecipe"] = recipe
input["feedback"] = "I don't want to use chicken today. Can you suggest something else? Maybe something not indian"

recipe = return_recipe(input,"I want something delicious and good looking for a dinner party.", outputFormat)
print(recipe)