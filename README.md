# 🎯 Number Guessing Game

A simple command-line Number Guessing Game built with Python. Test your luck and logical thinking by guessing a randomly generated number based on the selected difficulty level.

## 📌 Features

* Three difficulty levels:

  * 🟢 Easy (1 - 50)
  * 🟡 Medium (1 - 100)
  * 🔴 Hard (1 - 500)
* Random number generation using Python's `random` module.
* Score calculation based on the number of attempts.
* Helpful hints (`Too High` / `Too Low`).
* Play again option.
* Input validation and error handling.
* Graceful exit using `Ctrl + C`.

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python --version
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/basantjangra79/Project-2-Number-Guessing-Game.git
```

Navigate to the project directory:

```bash
cd number-guessing-game
```

---

## ▶️ Run the Game

Execute the following command:

```bash
python main.py
```

---

## 🎮 How to Play

1. Launch the game.
2. Select a difficulty level:

   * `1` → Easy
   * `2` → Medium
   * `3` → Hard
3. The game generates a random secret number.
4. Enter your guesses.
5. The game will tell you whether your guess is:

   * Too High
   * Too Low
6. Keep guessing until you find the correct number.
7. Your score will be displayed after winning.
8. Choose whether to play again.

---

## 🏆 Scoring System

The score is calculated using:

```python
score = (max_score - attempts) / 5
```

Fewer attempts result in a higher score.

---

## 📂 Project Structure

```text
number-guessing-game/
│
├── main.py
└── README.md
```

---

## 🛠 Built With

* Python 3
* random
* time

---

## 📷 Example

```text
Welcome to Number Guessing Game!

1 - Easy
2 - Medium
3 - Hard

Enter a Number to Proceed: 1

You Chosed: Easy Level!, Guess The Number from 1 to 50

Guess the Number: 25
Too High..

Guess the Number: 12
Too Low..

Guess the Number: 18

You Win! Yes, You Guess the Right Number: 18
You Score: 8.6
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Basant Jangra**

GitHub: https://github.com/your-github-username
