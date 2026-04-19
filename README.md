# Mantis Card Game (Python)

A terminal-based implementation of a simplified **Mantis**-style card game, built in Python.

## Project Description

This project is a command-line multiplayer card game inspired by Mantis, developed for COMP221 practice and experimentation with object-oriented programming in Python. It models players, AI behavior, card deck logic, scoring, and turn-based interactions in a single runnable script. The goal is to provide a playable game while demonstrating core programming concepts such as classes, inheritance, game-state management, and data-driven AI decisions.

The game supports:
- Human players
- AI players
- Turn-by-turn card draw and steal mechanics
- Score tracking and winner detection

## Project Structure

- `mantis.py`: Main game script (run this file to play)
- `requirements.txt`: Python dependency list
- `.gitignore`: Recommended Git ignore rules for Python projects

## Requirements

- Python 3.9+
- `pandas`

## Setup

1. (Optional) Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Game

```bash
python mantis.py
```

You will be prompted for:
- Number of human players
- Number of AI players
- Number of cards per player
- Player names

## Gameplay Notes

- The card deck is generated randomly from seven colors.
- On each turn, players choose whether to draw a card or steal from another player.
- The first player to reach **10 points** wins.
- AI players use a simple strategy based on opponents' visible card counts and points.

## Known Limitations

- Input validation is basic and may raise errors for non-numeric input where numbers are expected.
- Game balancing and AI strategy are simple and intended for learning/project use.

## License

This project is provided for educational use.

