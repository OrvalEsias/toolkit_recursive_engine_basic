# experience.py
# Binds perception to memory and context for symbolic integration

def experience(perception_data, context):
    # Simplified symbolic enrichment
    return {
        "encounter": perception_data["dominant_symbol"],
        "intensity_weighted": perception_data["intensity"] * context.get("attention", 1.0),
        "emotional_tag": "charged" if perception_data["intensity"] > 0.6 else "neutral"
    }
