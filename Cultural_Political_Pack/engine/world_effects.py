
def apply_cultural_growth(world_state, culture_entity):
    for zone in world_state["zones"]:
        if zone["id"] in culture_entity.get("influence_radius", []):
            zone["culture"].append(culture_entity["name"])
            zone["symbolic_codes"].extend(culture_entity["symbolic_codes"])
            zone["stability"] -= 0.05 if "ritual-light" in culture_entity["traits"] else 0

def apply_gang_presence(world_state, gang_entity):
    for zone in world_state["zones"]:
        if zone["name"] == gang_entity["territory"]:
            zone["gangs"].append(gang_entity["name"])
            zone["crime_rate"] += 0.2
            zone["trust_index"] -= 0.1

def apply_political_event(world_state, event):
    for effect in event["effects"]:
        if effect == "gang surge":
            for zone in world_state["zones"]:
                zone["crime_rate"] += 0.1
        elif effect == "migration":
            for zone in world_state["zones"]:
                zone["population"] += 100
        elif effect == "political fragmentation":
            world_state["global_cohesion"] -= 0.2
