from LLM_Recipe.return_recipe import return_recipe
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
recipe = return_recipe(input, outputFormat, "I want to cook a recipe")

#extracting content from the recipe
answer = recipe.content

print(answer)