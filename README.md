# Hangman Guessing Game 🎯

<p align="center">
  <strong>Hangman dalam bahaya! Selamatkan dia dengan menebak kata.</strong>
</p>

<p align="center">
  A terminal word-guessing game written in Python, with four word categories, accounts, scoring and a leaderboard.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Terminal-4D4D4D?style=flat&logo=windowsterminal&logoColor=white" alt="Terminal" />
</p>

<p align="center">
  <a href="#demo">Demo</a> •
  <a href="#features">Features</a> •
  <a href="#how-to-play">How to Play</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#code-overview">Code Overview</a> •
  <a href="#authors">Authors</a>
</p>

---

## What is Hangman?

**Hangman** is a classic word-guessing game that runs in the terminal. The game picks a random word from one of four categories, and the player guesses it one letter at a time. Every correct letter is revealed in the word, while every wrong guess costs a life and draws another part of the hanging man. Guess the word before the seven lives run out to save him.

On top of the classic game, this version adds **accounts, scoring and a leaderboard**, plus a **guest mode** for quick games. The game interface is in Indonesian.

```text
Lobby → Sign Up / Login / Guest → Pick Menu → Guess Letters (7 lives) → Score ±1 → Leaderboard
```

---

## Demo

> Run it in a terminal, guess the word and climb the leaderboard.
<table>
  <tr>
    <td align="center" width="25%">
      <img width="576" height="264" alt="Lobby" src="https://github.com/user-attachments/assets/59bf6b94-03a5-4454-a59f-5c6c571e135c" />
      <sub><strong>Lobby</strong></sub>
    </td>
    <td align="center" width="25%">
      <img width="364" height="310" alt="Guess the word" src="https://github.com/user-attachments/assets/95c5015b-e4ab-4d76-b586-3311d3a6de01" />
      <sub><strong>Guess the word</strong></sub>
    </td>
    <td align="center" width="25%">
      <img width="418" height="403" alt="Leaderboard" src="https://github.com/user-attachments/assets/6209b503-8f05-472b-af48-54d84ded67c4" />
      <sub><strong>Leaderboard</strong></sub>
    </td>
  </tr>
</table>

---

## Features

| Feature            | Description                                                                          |
| ------------------ | ------------------------------------------------------------------------------------ |
| Sign-Up & Login    | Create an account (password of at least 8 characters, confirmed twice) and log in    |
| Guest Mode         | Play instantly without an account; guest games do not affect the score               |
| Word Categories    | Guess words from four categories: fruits, animals, vegetables and countries          |
| Lives & Drawing    | 7 lives, with an ASCII hanging man that is drawn as you lose lives                   |
| Tutorial           | The "Cara Bermain" page explains the rules before you play                           |
| Scoring            | +1 point for every word guessed, -1 point for every loss (never below 0)             |
| Leaderboard        | Ranks players by score and is shown after every round                                |
| Countdown          | A 3-2-1 ASCII countdown before each game starts                                      |

---

## How to Play

1. Start the program and choose **Cara Bermain** to read the rules, or **Mulai Bermain** to start.
2. Choose **Daftar** to sign up, **Login** to sign in, or **Mode Tamu** to play as a guest.
3. After logging in, choose **Mulai** to play or **Leaderboard** to see the ranking.
4. A random word from a random category is selected, and you see it as hidden letters.
5. Type one letter (A-Z) at a time.
   - A **correct** letter is revealed everywhere it appears in the word.
   - A **wrong** letter costs one life and draws another part of the figure.
6. Win by revealing the whole word before your 7 lives run out. Your score changes by +1 for a win and -1 for a loss.

### Game Rules

| Rule                | Value                                                   |
| ------------------- | ------------------------------------------------------- |
| Lives               | 7                                                       |
| Categories          | Buah (fruits), Hewan (animals), Sayur (vegetables), Negara (countries) |
| Words               | Indonesian words; entries with spaces or hyphens are skipped |
| Score on win / loss | +1 / -1 (minimum 0)                                     |
| Password length     | At least 8 characters                                   |

---

## Getting Started

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- No extra libraries: the game only uses the standard library (`random`, `string`, `os`, `time`)
- A Windows terminal, because the game clears the screen with the `cls` command. A modern terminal such as Windows Terminal also displays the emoji and box characters best.

### Run the game

```bash
# 1. Clone
git clone https://github.com/daffmaulana/Hangman.git
cd Hangman

# 2. Run
python "Program Permainan Hangman.py"
```

> Run the program from inside the project folder so it can find `database.txt`.

---

## Code Overview

```text
Hangman/
├── Program Permainan Hangman.py    # The whole game
├── database.txt                    # Accounts, one "username, password" per line
└── README.md
```

| Part                                   | Responsibility                                             |
| -------------------------------------- | ---------------------------------------------------------- |
| `lobby()`, `konsep_permainan()`        | Welcome screen and the "how to play" page                  |
| `mulai_permainan()`                    | Menu for sign up, login and guest mode                     |
| `register()`, `login()`                | Account creation and authentication against `database.txt` |
| `hangman()`, `hangman_guest()`         | Game loop for logged-in players and for guests             |
| `cari_kategori()`, `cari_kata()`       | Pick a random category and a random word                   |
| `sort()`, `leaderboard()`              | Rank players by score and print the table                  |
| `countdown()`                          | 3-2-1 countdown animation                                  |
| `setKata`, `stickman`                  | Word lists per category and the ASCII figure for each stage |

---

## Authors

- Daffa Bagus Maulana [@dffalann](https://www.instagram.com/dffalann)
- Yusuf Martinus Arief [@ymrief_](https://www.instagram.com/ymrief_/)
- Salwa Nafisa [@sal_wanaf](https://www.instagram.com/sal_wanaf/)
- Adinda Rizki Sya'bana Diva [@adindarizki15](https://www.instagram.com/adindarizki15/)
- Dafa Andika Firmansyah [@dafaaaf](https://www.instagram.com/dafaaaf/)

---

<p align="center">
  <strong>Hangman Guessing Game</strong><br>
  One letter at a time.
</p>
