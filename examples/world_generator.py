# world_generator.py
# Creates a symbolic world with default regions and traits

import json

def generate_world(name):
    world = {
        "world_name": name,
        "world_traits": {
            "order": 0.5,
            "chaos": 0.5,
            "faith": 0.5,
            "technology": 0.5
        },
        "regions": [],
        "recent_world_events": []
    }

    path = f"{name.lower().replace(' ', '_')}_world.json"
    with open(path, "w") as f:
        json.dump(world, f, indent=2)
    print(f"World saved to {path}")

if __name__ == "__main__":
    generate_world("Omaria Prime")
