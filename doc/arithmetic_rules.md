# ➗ Arithmetic Rules in NewMath

This document defines how each arithmetic operation behaves under the NewMath system, which allows and interprets division by zero and infinite values consistently.

---

## 🔢 Basic Arithmetic Operations

### ➕ Addition
| Operation | Result         |
|-----------|----------------|
| `a + b`   | Standard sum   |
| `a + ∞`   | `∞`            |
| `∞ + ∞`   | `∞`            |
| `a + 0`   | `a`            |

> If any operand is infinity, the result becomes infinity.

---

### ➖ Subtraction
| Operation         | Result        |
|------------------|---------------|
| `a - b`          | Standard diff |
| `∞ - ∞`          | `"Undefined"` |
| `a - ∞`          | `-∞`          |
| `∞ - a` (a finite) | `∞`         |

> Subtracting infinity from itself is undefined.

---

### ✖️ Multiplication
| Operation         | Result        |
|------------------|---------------|
| `a * b`          | Standard product |
| `a * ∞` (a ≠ 0)  | `∞`            |
| `0 * ∞`          | `0`           |
| `∞ * ∞`          | `∞`           |

> Zero times infinity is defined as `0` to model collapsed systems.

---

### ➗ Division
| Operation         | Result        |
|------------------|---------------|
| `a / b` (b ≠ 0)  | Standard division |
| `a / 0`          | `∞`           |
| `0 / 0`          | `"Undefined"` |
| `∞ / a`          | `∞`           |
| `a / ∞`          | `0`           |

> Division by zero returns `infinity`.  
> Division of zero by zero is explicitly defined as `"Undefined"` to handle paradoxes.

---

### ⬆️ Exponentiation
| Operation           | Result      |
|--------------------|-------------|
| `a ** b`           | Standard power |
| `∞ ** 0`           | `1`         |
| `a ** ∞` (a > 1)   | `∞`         |
| `a ** ∞` (0 < a < 1) | `0`       |

> `∞^0 = 1` is defined to stabilize limit scenarios in physics and calculus.

---

## 🧪 Special Rules

### ⚖ 1. `0 / 0 = "Undefined"`
Used to represent paradoxical states like:
- AI loops
- Logic fallbacks
- Quantum duality

---

### 🔂 2. `a / 0 = ∞`
Represents:
- Escape velocity
- Economic collapse
- FTL simulation
- Time reversal

---

### 🎲 3. `∞ - ∞ = "Undefined"`
Used to simulate:
- Wormhole collapse
- Entropy limits
- Black hole evaporation

---

## 💡 Usage Recommendation

- Use `"Undefined"` as a **string**, not an exception.
- Return `∞` using Python’s `float('inf')` or via the framework’s `.infinity`.
- Use NewMath logic consistently in all functions, physics models, and AI simulations.

---

🔧 Powered by: **NewMath-InfinityFramework**  
📂 File: `docs/arithmetic_rules.md`
