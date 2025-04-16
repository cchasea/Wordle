
# Name: Cameron Arruda
# Due Date: April 29, 2024
# Title: Wordle Game
# Project Description: This program is a recreation of Wordle where players guess a five-letter word
# and get feedback through the clues 'G' for a correct letter in the correct position, 'Y' for a correct
# letter in the wrong position, and 'X' if the character is not in the correct word. The game uses algorithms to get random
# words from the file "five-letter-words.csv" that was provided, clue computing based on if the letter is accurate,
# and creates scoring based on guess attempts.


import random
import csv

def load_words(file_path):
    words_list = []  # store words from the CSV file
    # attempts to open file in read mode and automatically closes the file
    # https://stackoverflow.com/questions/30969687/use-python-to-open-a-file-in-read-mode
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                words_list.append(row[0].upper())
        # returns a list of words, or None if the file is not found
        return words_list
    except FileNotFoundError:
        return None

def compute_clue(guess_word, wordle_word):
    clue = ['X'] * 5  # Starts with all letters marked as incorrect
    for i in range(5):
        if guess_word[i] == wordle_word[i]:
            clue[i] = 'G'  # Correct letter in the correct position
        elif guess_word[i] in wordle_word:
            letter_count_in_word = wordle_word.count(guess_word[i])
            letter_count_in_guess = guess_word[:i+1].count(guess_word[i])
            if letter_count_in_guess <= letter_count_in_word:
                clue[i] = 'Y'  # Correct letter but in the wrong position
    return ''.join(clue) # converts the list of characters into a string and returns it.
    # https://www.w3schools.com/python/ref_string_join.asp


def main():
    # Prompt the user to enter the name of the correct file
    file_name_input = input("Please enter a file name: ")
    words_list = load_words(file_name_input)  # creates list of words from the file

    # will only loop until a valid file is loaded
    while words_list is None:
        print("Invalid file name try again...")
        file_name_input = input("Please enter a file name: ")  # ask for file name again
        words_list = load_words(file_name_input)

    continue_playing = True  # controls the game loop
    total_score = 0  # initialize total score

    # game loop. continues as long as the player wants to play
    while continue_playing:
        wordle_word = random.choice(words_list)  # Select a random word from the list
        attempts = 0  # counter for the number of guesses

        # Loop for 6 attempts per game
        while attempts < 6:
            guess = input("Make a guess: ").strip().upper()  # Prompt user for a guess. .strip() to remove blank space and .upper() to put all characters in uppercase
            if guess not in words_list:
                print("Word not in dictionary - try again...")  # if a word guessed is not in the file
                continue  # Skip rest of the loop and ask for another guess
            attempts += 1  # Increment the attempt counter
            clue = compute_clue(guess, wordle_word)  # Generate clue based on the guess
            print(guess)
            print(clue)
            if clue == 'GGGGG':  # Check if guess is correct
                print(f"Congratulations, your wordle score for this game is {attempts}")
                total_score += attempts  # Update total score
                break  # Exit game loop for current game
            if attempts == 6:  # Check if limit of attempts is reached
                print(f"Sorry, you did not guess the word: {wordle_word}")
                total_score += 10

        print(f"Your overall score is {total_score}")
        another_game = input("\nWould you like to play again (Y or N)? ").strip().upper()  # Ask if user wants another game
        continue_playing = another_game == 'Y'

    print("\nThanks for playing!")  # End game message

# Run the main function
if __name__ == "__main__":
    main()