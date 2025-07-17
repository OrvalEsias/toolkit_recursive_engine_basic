from engine.world_effects import apply_cultural_growth, apply_gang_presence, apply_political_event
from engine.load_symbolic_entities import load_all_entities

# Example world state
world_state = {
    "zones": [
        {"id": 1, "name": "South Sink", "culture": [], "gangs": [], "crime_rate": 0.1, "trust_index": 0.9, "symbolic_codes": [], "population": 500},
        {"id": 2, "name": "Spire Markets", "culture": [], "gangs": [], "crime_rate": 0.05, "trust_index": 0.95, "symbolic_codes": [], "population": 1000},
        {"id": 3, "name": "Central District", "culture": [], "gangs": [], "crime_rate": 0.02, "trust_index": 0.97, "symbolic_codes": [], "population": 2000}
    ],
    "global_cohesion": 1.0
}

entities = load_all_entities("data")

# Apply effects
for culture in entities["culture"]:
    apply_cultural_growth(world_state, culture)

for gang in entities["gangs"]:
    apply_gang_presence(world_state, gang)

for event in entities["politics"]:
    if event["type"] == "political_event":
        apply_political_event(world_state, event)

# Debug output
import pprint
pprint.pprint(world_state)
