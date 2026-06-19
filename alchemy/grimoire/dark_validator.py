from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    foo = dark_spell_allowed_ingredients()
    if ingredients.lower() in foo:
        return f"{ingredients} VALID"
    return f"{ingredients} INVALID"


if __name__ == "__main__":
    pass
