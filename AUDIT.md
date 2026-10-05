# Python Number Checker Programs

A collection of simple Python programs to check whether a given number is **Prime, Armstrong, or Pronic**.

## 📌 Programs Included

### 1. Prime Number Checker
Checks whether the entered number is a prime number.

A **prime number** is a number greater than 1 that has only two factors: `1` and itself.

**Example:**
```text
Enter a number: 17
Prime Number
```

### 2. Armstrong Number Checker
Checks whether the entered number is an Armstrong number.

An **Armstrong number** is a number whose digits raised to the power of the number of digits and added together equal the original number.

**Example:**
```text
Enter a number: 153
Armstrong Number
```

`153 = 1³ + 5³ + 3³ = 153`

### 3. Pronic Number Checker
Checks whether the entered number is a Pronic number.

A **Pronic number** is a number that can be expressed as the product of two consecutive integers.

**Example:**
```text
Enter a number: 20
Pronic Number
```

`20 = 4 × 5`

## 🛠️ Technology Used

- Python 3
- Basic loops
- Conditional statements
- Arithmetic operators

## 📂 Files

```text
.
├── prime.py
├── armstrong.py
├── pronic.py
└── README.md
```

## ▶️ How to Run

Make sure Python 3 is installed, then run any program using:

```bash
python prime.py
```

```bash
python armstrong.py
```

```bash
python pronic.py
```

## 🎯 Purpose

These programs are created for practicing **basic Python programming, loops, conditions, and number-based logic**.

---

**Made with Python 🐍**
# 📊 Program Comparison

| Feature | Factorial | Fibonacci | Prime Checker | Armstrong Checker | Pronic Checker |
|---|---|---|---|---|---|
| **Main Purpose** | Calculate factorial | Generate sequence | Check prime number | Check Armstrong number | Check Pronic number |
| **Input** | One integer | Number of terms | One integer | One integer | One integer |
| **Main Concept** | Multiplication | Sequence generation | Divisibility | Digit manipulation | Consecutive multiplication |
| **Loops Used** | `for` | `for` / `while` | `for` | `while` | `for` |
| **Conditions Used** | `if / elif / else` | Optional | `if / else` | `if / else` | `if / else` |
| **Arithmetic** | Multiplication | Addition | Modulo `%` | Power `**`, modulo `%` | Multiplication |
| **Digit Extraction** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Uses `break`** | ❌ | ❌ | ✅ | ❌ | ✅ |
| **Handles Special Cases** | Negative & zero | Initial terms | ≤ 1 | Zero/single digit cases | Zero/small numbers |
| **Difficulty** | 🟢 Easy | 🟢 Easy | 🟢 Easy | 🟡 Moderate | 🟢 Easy |
| **Core Skill** | Loops & arithmetic | Variables & loops | Logic & divisibility | Mathematical logic | Loop-based logic |
| **Status** | ✅ Pass | ✅ Pass | ✅ Pass | ✅ Pass | ✅ Pass |

## 🏆 Complexity Comparison

| Program | Basic Time Complexity | Space Complexity |
|---|---:|---:|
| Factorial | O(n) | O(1) |
| Fibonacci | O(n) | O(1)* |
| Prime Checker | O(n) | O(1) |
| Armstrong Checker | O(d) | O(1) |
| Pronic Checker | O(n) | O(1) |

> **Note:** `d` represents the number of digits in the number.  
> *For the simple iterative Fibonacci implementation.

## 🎯 Concept Comparison

```text
Factorial
    ↓
Multiplication + Loops

Fibonacci
    ↓
Addition + Variable Updates + Loops

Prime
    ↓
Divisibility + Conditions

Armstrong
    ↓
Digit Extraction + Powers + Loops

Pronic
    ↓
Consecutive Numbers + Multiplication + Loops
```

### Overall Comparison

**Easiest:** Factorial / Fibonacci  
**Logic-focused:** Prime / Pronic  
**Most mathematical:** Armstrong  
**Best for practicing digit manipulation:** Armstrong  
**Best for practicing divisibility:** Prime  
**Best for sequence logic:** Fibonacci
