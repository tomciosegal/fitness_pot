def validate_recipe(recipe):
    fields = [
        "name",
        "user_name",
        "title",
        "serves",
        "mail",
        "ingredients",
        "instructions",
    ]

    for field in fields:
        if not recipe.get(field):
            return False
    return True
