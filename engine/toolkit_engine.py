# toolkit_engine.py
# Core symbolic transformation engine

def simulate_character(character_path):
    import json
    with open(character_path) as f:
        data = json.load(f)
    print(f"Simulating: {data['name']}")
    for step in data.get("transformation_log", []):
        print(f"Step {step['step']}: {step['event']} → {step['symbol']}")

def load_world(world_path):
    import json
    with open(world_path) as f:
        world = json.load(f)
    print(f"Loaded world: {world['world_name']}")
    print("Traits:", world["world_traits"])
