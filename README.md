# Console-Based WORDLE Game

## Description

This is a **text-based Wordle game** written in Python. 

- The player has **6 attempts** to guess a **secret 5-letter word**.  
- After each guess, the game provides **feedback for each letter** using **colors and symbols**:

  - **Green (`✓`)** = correct letter in the correct spot  
  - **Yellow (`~`)** = correct letter but in the wrong spot  
  - **Red (`x`)** = letter not in the word  

- The symbols are displayed **directly below the letters** to help the player track their guesses, similar to the official Wordle game.

## Files Required

To run this program, you need two text files in the same folder as the Python script:

1. **words.txt** – a smaller list of common 5-letter words used to pick the secret word.  
2. **complex_words.txt** – a larger list of valid 5-letter words used to **validate the player's guesses**.  

Each file should have **one word per line**.

---

## How to Run

1. Make sure **Python 3.11** or higher is installed.  
2. Place `words.txt` and `complex_words.txt` in the same folder as `main.py`.  
3. Run the program:

```bash
python main.py
```
---

## Interesting Feature

This Wordle game uses **two separate word lists** to enhance gameplay and accuracy:

1. **Validation List** – A list of **5,757 five-letter words** used for validation of guesses.  
   - These words were originally used by Donald Knuth for demonstrations of the **Stanford Graph Base (SGB)**.  
   - This ensures that player guesses are **real English words** recognized in the dataset.

2. **Answer List** – A smaller list of **2,309 five-letter English words**, in alphabetical order, used as possible answers for the game.  
   - These words are selected as potential secret words in the game Wordle.  

Both datasets were sourced from the same website: [https://people.sc.fsu.edu/~jburkardt/datasets/words/words.html](https://people.sc.fsu.edu/~jburkardt/datasets/words/words.html)  

By separating **valid guesses** from **possible answers**, the game can validate input without restricting the secret word pool, improving the gameplay experience.


## Challenge: Handling Repeated Letters

This game handles repeated letters similarly to the official Wordle rules. 

For example:

```python
# Secret word = "FLAME"
# Guess = "AALII"
```

There is **only one `A`** in the secret word.

Even though the guess has **two `A`s**, only one is marked yellow (`~`).

The second `A` is marked red (`x`) because there is no second `A` in the secret word.

This is implemented in the code with the following logic:

```python
if guess_letters[i] in secret_count and secret_count[guess_letters[i]] > 0:
    # mark yellow (~) and reduce the count
else:
    # mark red (x)
```

This ensures that the feedback is accurate for repeated letters, so the player doesn’t get extra yellow marks for letters that appear fewer times in the secret word.

