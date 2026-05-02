from alchemy.elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    string = "Recipe transmuting Lead to Gold: brew"
    return string + f" '{create_air()}' and '{strength_potion()}'"


if __name__ == "__main__":
    pass
