# perception.py
# Extracts salient symbolic features from an input signal

def perceive(input_signal):
    # Simplified: select symbolic keys that stand out
    return {
        "dominant_symbol": input_signal.get("symbol", "unknown"),
        "intensity": max(input_signal.get("traits", {}).values(), default=0)
    }
