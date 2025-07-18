
"""
Logoi Module — Adds recursive symbolic structure to character and world evolution.

Three Logoi:
1. Logos of Perception — filters meaning
2. Logos of Relation — configures narrative tension and polarity
3. Logos of Becoming — governs symbolic transformation across time
"""

def logos_of_perception(symbolic_input, perceptual_mode="archetypal"):
    """Shapes what enters awareness based on perceptual lens."""
    if perceptual_mode == "rational":
        return {k: v for k, v in symbolic_input.items() if isinstance(v, (int, float))}
    elif perceptual_mode == "archetypal":
        return {k: v for k, v in symbolic_input.items() if k in ["shadow", "anima", "mentor"]}
    elif perceptual_mode == "emotive":
        return {k: v for k, v in symbolic_input.items() if v > 0.6}
    else:
        return symbolic_input

def logos_of_relation(agent_traits):
    """Creates symbolic polarity or narrative role alignment."""
    polarity = {}
    for k, v in agent_traits.items():
        if k in ["courage", "dominance"]:
            polarity[k] = "assertive"
        elif k in ["empathy", "sensitivity"]:
            polarity[k] = "receptive"
        else:
            polarity[k] = "neutral"
    return polarity

def logos_of_becoming(current_state, world_flux=0.1):
    """Alters trajectory of transformation based on symbolic gravity."""
    trajectory = {}
    for trait, value in current_state.get("traits", {}).items():
        if value > 0.7:
            trajectory[trait] = "stabilizing"
        elif value < 0.3:
            trajectory[trait] = "disruptive"
        else:
            trajectory[trait] = "in flux"
    trajectory["world_flux"] = world_flux
    return trajectory
