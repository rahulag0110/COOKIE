from LLM_Recipe.chat import chat_with_recipe
recipe = [
      "Preheat the oven to 200 degrees Celsius.",
      "Season the chicken drumsticks with crushed garlic, chilli, salt, and pepper.",
      "Place the drumsticks on a baking tray and bake for 25-30 minutes until golden brown and cooked through.",
      "While the chicken is cooking, chop the carrots, green beans, and onions.",
      "Steam the vegetables until they are tender.",
      "Serve the spicy chicken drumsticks with the steamed vegetables on the side."
    ]
chat = chat_with_recipe(recipe, "Can you explain step 3 in more detail?")

print(chat)