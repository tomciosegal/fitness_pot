def validate_recipe(recipe):
    fields = [
        "category",
        "title",
        "serves",
        "image_url",
        "ingredients",
        "instructions",
    ]

    for field in fields:
        if not recipe.get(field):
            print("could not validate field = ", field)
            return False
    return True
