from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    if ingredients.lower() in dark_spell_allowed_ingredients():
        return "VALID"
    return "INVALID"


if __name__ == "__main__":
    pass
