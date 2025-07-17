
# 🧪 How to Use the Basic Recursive Engine

This guide walks you through using the **Symbolic Toolkit** in the `basic-recursive-engine` branch.

---

## 🔧 Requirements

- Python 3.10 or later
- Git (optional, for cloning)
- Recommended: basic familiarity with JSON and Python

---

## 🚀 Quick Start

### 1. **Clone or Download the Toolkit**

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

Or download and unzip the release from GitHub.

---

### 2. **Inspect the Data Folder**

```bash
cd data/
```

This contains:

- `example_character.json` → A symbolic agent you can modify
- `symbolic_triggers.json` → Events that trigger growth
- `world_triggers.json` → Symbolic transformations for environments

---

### 3. **Run the Simulation**

From the root folder:

```bash
python engine/simulation_loop.py
```

You’ll see output showing symbolic transformations such as:

```
[INITIATION] Character: “Sira” → State changed from 'undifferentiated' to 'auxiliary'
```

---

### 4. **Customize the System**

- Change agent traits in `example_character.json`
- Add new events in `symbolic_triggers.json`
- Define new environments in `world_triggers.json`
- Or create new trigger logic in `engine/simulation_loop.py`

---

### 5. **Next Steps (Optional)**

To explore licensing, full recursion logic, or co-evolving world-state logic:

📩 Contact: eric@erbesystem.com  
📄 See `DIFFERENCE.md` and `LICENSE.txt` for terms

---

Enjoy building symbolic beings, worlds, and transformations.
