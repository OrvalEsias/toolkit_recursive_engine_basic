# god_interaction.py
# Simulates a symbolic omnipotent god altering world traits and characters

import json
from engine.world_effects import apply_character_effect_to_world
from engine.toolkit_engine import load_world

def act_of_god(world_path, divine_will):
    world = load_world(world_path)
    updated = apply_character_effect_to_world(world, divine_will)

    print("🌩️ Act of God applied:")
    for trait, value in updated["world_traits"].items():
        print(f"  {trait}: {round(value, 2)}")

if __name__ == "__main__":
    god_effect = {
        "order": +0.2,
        "chaos": -0.2,
        "faith": +0.4
    }
    act_of_god("world examples/metropolis_verge_world.json", god_effect)
