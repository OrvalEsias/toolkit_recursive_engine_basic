# load_symbolic_entities.py
# Utility to load symbolic character/world entities

import json

def load_entity(path):
    with open(path, 'r') as f:
        return json.load(f)
