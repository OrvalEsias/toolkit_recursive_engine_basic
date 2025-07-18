# expression.py
# Outputs symbolic expression based on internal understanding

def express(understanding_data):
    return {
        "output_symbol": understanding_data["meaning"].upper(),
        "tone": "resonant" if understanding_data["emotional_state"] == "charged" else "muted"
    }
