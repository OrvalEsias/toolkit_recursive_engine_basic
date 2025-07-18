# character_generator.py
# Creates a new symbolic character file from input or random traits

import json
import random

def generate_character(name):
    core_traits = ["introversion", "extroversion"]
    primary_traits = ["thinking", "feeling", "intuition", "sensation"]

    character = {
        "name": name,
        "core_trait": random.choice(core_traits),
        "primary_trait": random.choice(primary_traits),
        "secondary_trait": random.choice([t for t in primary_traits if t != primary_traits[0]]),
        "function_stack": ["diff", "aux_negative", "aux_positive", "undiff"],
        "symbolic_role": "seeker",
        "transformation_log": [],
        "current_state": {
            "symbol": "undifferentiated",
            "phase": "diff"
        }
    }

    path = f"{name.lower()}_generated_character.json"
    with open(path, "w") as f:
        json.dump(character, f, indent=2)
    print(f"Character saved to {path}")

if __name__ == "__main__":
    generate_character("Omari")
