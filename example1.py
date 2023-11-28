from LLM_Recipe.return_recipe import return_recipe
input = {
    "pantry": "[chicken drumsticks, chives, carrots, potatoes, tomatoes, onions, garlic, mayonaise, corn, papaya]",
    "diet": "strict diet",
    "spiceLevel": "medium"   
}
outputFormat = """ [
{"recipeName": "Name of the recipe", "ingedrientsUsed": "Ingredients used in the recipe", "servings": "Number of servings", "steps": "Steps to cook the recipe mentioned clearly in a numbered list"},
{...},
{...}
] """
recipe = return_recipe(input, outputFormat, "I want something easy and quick to make.")

#extracting content from the recipe
answer = recipe.content

with open("example1.txt", 'w') as file:
    file.write(answer)
print(answer)