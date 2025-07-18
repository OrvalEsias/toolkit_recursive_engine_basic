# main_demo.py
# Combined demo: simulate character arc and apply effect to a world

from engine.toolkit_engine import simulate_character, load_world
from engine.world_effects import apply_character_effect_to_world

# Simulate Maelee
character_path = "character examples/maelee_recursive_simulation.json"
world_path = "world examples/metropolis_verge_world.json"

print("\n=== Simulating Character ===")
simulate_character(character_path)

print("\n=== Loading World ===")
world = load_world(world_path)

# Mock effect from character (normally this would come from simulation logic)
mock_effect = {
    "media_signal": -0.2,
    "spiritual_noise": 0.3
}

print("\n=== Applying Character Effect to World ===")
updated_world = apply_character_effect_to_world(world, mock_effect)

print("\n=== Updated World Traits ===")
for trait, value in updated_world["world_traits"].items():
    print(f"{trait}: {value:.2f}")
