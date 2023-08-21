import os

### DATA PATHS ###
BASE_PATH = os.getcwd().split("source")[0]
ENCOUNTER_SUBSET_PATH = os.path.join(BASE_PATH, "source/subsets/encounter_subset.json").replace('\\',"/")
PLAYER_SUBSET_PATH = os.path.join(BASE_PATH, "source/subsets/player_subset.json").replace('\\',"/")

### UNIQUE KEYS###
PLAYER_KEYS = [
    "alternate_of",
    "back_flavor",
    "back_link",
    "back_text",
    "bonded_count",
    "bonded_to",
    "clues",
    "code",
    "cost",
    "customization_change",
    "customization_options",
    "customization_text",
    "deck_limit",
    "deck_options",
    "deck_requirements",
    "double_sided",
    "duplicate_of",
    "enemy_damage",
    "enemy_evade",
    "enemy_fight",
    "enemy_horror",
    "errata_date",
    "exceptional",
    "exile",
    "faction2_code",
    "faction3_code",
    "faction_code",
    "flavor",
    "health",
    "hidden",
    "illustrator",
    "is_unique",
    "myriad",
    "name",
    "pack_code",
    "permanent",
    "position",
    "quantity",
    "restrictions",
    "sanity",
    "shroud",
    "skill_agility",
    "skill_combat",
    "skill_intellect",
    "skill_wild",
    "skill_willpower",
    "slot",
    "subname",
    "subtype_code",
    "tags",
    "text",
    "traits",
    "type_code",
    "victory",
    "xp",
]

ENCOUNTER_KEYS = [
    "back_flavor",
    "back_illustrator",
    "back_link",
    "back_name",
    "back_text",
    "back_traits",
    "clues",
    "clues_fixed",
    "code",
    "cost",
    "deck_limit",
    "deck_options",
    "deck_requirements",
    "doom",
    "double_sided",
    "encounter_code",
    "encounter_position",
    "enemy_damage",
    "enemy_evade",
    "enemy_fight",
    "enemy_horror",
    "errata_date",
    "exile",
    "faction_code",
    "flavor",
    "health",
    "health_per_investigator",
    "hidden",
    "illustrator",
    "is_unique",
    "name",
    "pack_code",
    "permanent",
    "position",
    "quantity",
    "sanity",
    "shroud",
    "skill_agility",
    "skill_combat",
    "skill_intellect",
    "skill_wild",
    "skill_willpower",
    "slot",
    "stage",
    "subname",
    "subtype_code",
    "text",
    "traits",
    "type_code",
    "vengeance",
    "victory",
]

### FEATURE KEYS###
FEATURE_ENCOUNTER_DICT = {
    "back_flavor": str,
    "back_link": str,
    "back_name": str,
    "back_text": str,
    "back_traits": str,
    "code": str,
    "cost": int,
    "deck_limit": int,
    "doom": int,
    "encounter_code": str,
    "encounter_position": int,
    "enemy_damage": int,
    "enemy_evade": int,
    "enemy_fight": int,
    "enemy_horror": int,
    "errata_date": str,
    "faction_code": str,
    "flavor": str,
    "health": int,
    "health_per_investigator": bool,
    "hidden": bool,
    "is_unique": bool,
    "name": str,
    "pack_code": str,
    "permanent": bool,
    "quantity": int,
    "sanity": int,
    "shroud": int,
    "skill_agility": int,
    "skill_combat": int,
    "skill_intellect": int,
    "skill_wild": int,
    "skill_willpower": int,
    "slot": str,
    "stage": int,
    "subname": str,
    "subtype_code": str,
    "text": str,
    "traits": str,
    "type_code": str,
    "vengeance": int,
    "victory": int,
}

FEATURE_PLAYER_DICT = {
    "alternate_of": str,
    "back_flavor": str,
    "back_link": str,
    "back_text": str,
    "bonded_count": int,
    "bonded_to": str,
    "code": str,
    "cost": int,
    "customization_change": str,
    "customization_options": list,
    "customization_text": str,
    "deck_limit": int,
    "deck_options": list,
    "deck_requirements": str,
    "double_sided": bool,
    "duplicate_of": str,
    "enemy_damage": int,
    "enemy_evade": int,
    "enemy_fight": int,
    "enemy_horror": int,
    "errata_date": str,
    "exceptional": bool,
    "faction2_code": str,
    "faction3_code": str,
    "faction_code": str,
    "flavor": str,
    "health": int,
    "hidden": bool,
    "is_unique": bool,
    "myriad": bool,
    "name": str,
    "pack_code": str,
    "permanent": bool,
    "quantity": int,
    "restrictions": str,
    "sanity": int,
    "shroud": int,
    "skill_agility": int,
    "skill_combat": int,
    "skill_intellect": int,
    "skill_wild": int,
    "skill_willpower": int,
    "slot": str,
    "subname": str,
    "subtype_code": str,
    "tags": str,
    "text": str,
    "traits": str,
    "type_code": str,
    "victory": int,
    "xp": int,
}