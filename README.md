# daily-python-practice
# 🐍 Daily Python Practice

Welcome to my Python learning repository! Here, I document core concepts, handy cheat sheets, and practical mini-projects as I build my programming skills step-by-step.

---

## 🎲 Python `random` Module Cheat Sheet

The `random` module is built into Python and used to generate random numbers, make random selections, or shuffle data.

### 1. Generating Numbers
- **`random.randint(a, b)`**: Pick a random whole number between `a` and `b` (inclusive).
  ```python
  dice = random.randint(1, 6)

- **random.uniform(a, b):** Pick a random decimal number between a and b
  ```python
   rating = random.uniform(1.0, 5.0)
 
- **random.random():** Generates a random decimal number between 0.0 and 1.0. 
  ```python
   chance = random.random()
  
- **random.choice(my_list):** Picks one single item randomly from a list or sequence.
  ```python
  color = random.choice(["Red", "Green", "Blue"])

- **random.shuffle(my_list):** Reorders the items inside a list randomly (modifies the list directly).
 ```python
   cards = ["Ace", "King", "Queen", "Jack"]
   random.shuffle(cards)
 


 
