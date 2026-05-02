from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion() -> str:
    __string = "Healing potion brewed with"
    return __string + f"'{create_earth()}' and '{create_air()}"


def strength_potion() -> str:
    __string = "Strength potion brewed with"
    return __string + f" '{create_fire()}' and '{create_water()}'"


if __name__ == "__main__":
    pass
