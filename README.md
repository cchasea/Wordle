# Wordle Game (Python)

A command-line Worlde word guessing game written in Python 

## Features

- Provided 5 letter word list from the '.csv' file
- Validates guesses to ensure they are 5-letter words from the list
- Provides clue feedback (correct letter in correct position returns 'G', correct letter in incorrect position returns 'Y')
- Tracks total score and allows replaying
- Handles invalid input and missing files

  ## Example Run
Please enter a file name: five-letter-words.csv

Make a guess: games

GAMES

XXGYX

Make a guess: bumpy

BUMPY

XXGXX

Make a guess: comet

COMET

XYGYX


Make a guess: lemon
LEMON

XGGGX

Make a guess: 

DEMOI

GGGGG

Congratulations, your wordle score for this game is 5

Your overall score is 5


Would you like to play again (Y or N)? n


Thanks for playing!

## Future Improvements
-Add GUI
