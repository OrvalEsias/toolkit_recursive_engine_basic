import json
import os

def load_entities(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_all_entities(data_dir="data"):
    culture = load_entities(os.path.join(data_dir, "culture_entities.json"))
    gangs = load_entities(os.path.join(data_dir, "gang_entities.json"))
    politics = load_entities(os.path.join(data_dir, "politics_entities.json"))
    characters = load_entities(os.path.join(data_dir, "characters.json"))
    return {
        "culture": culture,
        "gangs": gangs,
        "politics": politics,
        "characters": characters
    }
