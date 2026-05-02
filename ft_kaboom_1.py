from alchemy.grimoire.dark_spellbook import dark_spell_record


print("=== Kaboom 1 ===")
ing = "Sugar, spice and everything nice"
spell_name = "Abra Kadabra"
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
print(f"Testing record dark spell: {dark_spell_record(spell_name, ing)}")
