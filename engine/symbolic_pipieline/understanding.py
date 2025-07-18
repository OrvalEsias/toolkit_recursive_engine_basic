# understanding.py
# Transforms experiences into structured internal models

def understand(experience_data):
    # Simplified meaning assignment
    return {
        "meaning": f"pattern recognized in {experience_data['encounter']}",
        "emotional_state": experience_data["emotional_tag"]
    }
