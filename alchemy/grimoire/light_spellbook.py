def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str): #jnjel em tyope hint-y haskanalu hamar sxal ira uzac outputy chi tpum
    from .light_validator import validate_ingredients

    val = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({ingredients} - {val})"


if __name__ == "__main__":
    pass
