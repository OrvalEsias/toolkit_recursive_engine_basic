# symbolic_utils.py
# Shared symbolic utilities: symbol parsing, trait math, etc.

def normalize_traits(traits):
    total = sum(traits.values())
    if total == 0:
        return traits
    return {k: v / total for k, v in traits.items()}

def describe_symbolic_shift(from_symbol, to_symbol):
    return f"Symbolic transition: {from_symbol} → {to_symbol}"

def describe_phase_shift(from_phase, to_phase):
    return f"Phase shift: {from_phase} → {to_phase}"
