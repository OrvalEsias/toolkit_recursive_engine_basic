
# 🌌 Symbolic Toolkit: Recursive Identity & World Simulation

This toolkit is a lightweight, modular subset of the **ErbeSystem**, built for symbolic modeling of identity, growth, and world evolution.

It provides a non-commercial, open-access engine for simulating **recursive transformation** — enabling agents and environments to evolve through symbolic states.

---

## ✨ What’s Included

### 🧠 Symbolic Character Engine
- Recursive identity states: `undifferentiated → auxiliary → differentiated`
- Agent traits based on:
  - Big Five (Introversion/Extroversion, + 2 trait focus)
  - Function Types (Thinking, Feeling, Sensation, Intuition)
- Transformations triggered by symbolic events like `mentor_contact`, `initiation`, `betrayal`, `rebirth`

### 🌍 Symbolic World-State Triggers
- Worlds evolve symbolically through events like:
  - `plague_spread`: `fertile → withered`
  - `veil_thinned`: `mundane → haunted`
  - `sun_returned`: `withered → blooming`
- Define world environments and tie them to character states

### 📁 Files & Structure

```
symbolic-toolkit/
├── data/
│   ├── example_character.json        # Sample character with traits and growth path
│   ├── world_triggers.json          # Symbolic world transformation rules
│   └── symbolic_triggers.json       # Agent transformation triggers
├── engine/
│   ├── simulation_loop.py           # Core simulation logic (lightweight)
│   └── load_types.py                # Loaders for triggers and symbolic files
├── LICENSE.txt                      # Non-commercial use license
├── DIFFERENCE.md                    # What’s in this toolkit vs. the full system
└── README.md                        # You are here
```

---

## 🚀 How to Use

1. Clone the repository
2. Create or edit characters in `data/example_character.json`
3. Trigger character/world updates using `simulation_loop.py`
4. Modify `symbolic_triggers.json` and `world_triggers.json` to shape transformations

---

## 💡 Example Growth Triggers (Character)

- `mentor_contact`
- `initiation`
- `ego_shattered`
- `symbol_reversed`
- `truth_revealed`
- `sacrifice_made`

## 🌱 Example World Triggers

- `hero_departed`: `blessed → forsaken`
- `artifact_unearthed`: `forgotten → remembered`
- `myth_rewritten`: `static → emergent`

---

## 🔐 License

This toolkit is free for personal, educational, and non-commercial use.  
**Commercial use requires a license.** See `LICENSE.txt` for details.

---

## 📬 Want More?

This toolkit is a symbolic seed.

The **full ErbeSystem** includes:
- Advanced recursion logic
- Full symbolic co-evolution engine
- Integration with AI and immersive simulations

📧 Contact: eric@erbesystem.com  
📄 See `DIFFERENCE.md` for a full comparison
