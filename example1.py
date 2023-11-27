from LLM_Recipe.return_recipe import return_recipe
input = {
    "pantry": "[chicken drumsticks, chives, carrots, potatoes, tomatoes, onions, garlic, mayonaise, corn, papaya]",
    "timeOfDay": "Dinner",
    "cuisine": "Any",
    "numberOfRecipes": 2,
    "numberOfServings": 3,    
}
outputFormat = """ [{
    "recipeName": "Name of the recipe",
    "ingedrientsUsed": "Ingredients used in the recipe",
    "servings": "Number of servings",
    "steps": "Steps to cook the recipe mentioned clearly in a numbered list",
}, {...}, {...}] """
recipe = return_recipe(input, outputFormat, "")

#extracting content from the recipe
answer = recipe.content

print(answer)