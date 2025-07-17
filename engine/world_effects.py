# world_effects.py
# Applies character effects to the symbolic world state

def apply_character_effect_to_world(world_data, character_effect):
    for trait, delta in character_effect.items():
        if trait in world_data["world_traits"]:
            world_data["world_traits"][trait] += delta
            # Clamp value between 0 and 1
            world_data["world_traits"][trait] = max(0.0, min(1.0, world_data["world_traits"][trait]))
    return world_data
