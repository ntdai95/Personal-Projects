# Imorting the random module to randomly select the secret word from the gre_words.txt file and the colored function for user-friendly 
# display
import random
import sys
from termcolor import colored
# Importing the side module needed for the program
from gameplay import Gameplay

class PlayAgain:
    def playing_again(self):
        """Keep asking the user to enter a valid response, either y or n to whether to play again, if he/she loses. Then, return 
        his/her's choice of whether to play again"""
        # Creating a while loop to keep asking until the user enter a valid response of y or n
        while True:
            # Asking the user for his/her response and allowing to enter as an uppercased or lowercased letter of y or n
            play_again = input("Would you like to play again? (type y or n): ").lower()
            # If the user entered the valid response, then return his/her choice
            if play_again == "n" or play_again == "y":
                return play_again
            # If the user did not enter the valid response, print out the warning message and keep asking for a valid user input
            else:
                print("Please make sure to type only y or n!\n")

class SecretWord:
    def secret_word_generator(self):
        """Selecting the secret word needed to be guessed for the hangman game from the list of words in the gre_words.txt file"""
        # Read in and formatting the list of words from the gre_words.txt file
        gre_words_file = open("./gre_words.txt", 'r')
        gre_words_variable = gre_words_file.readlines()
        # Formatting and selecting the random secret word and its definition from the file
        random_number = random.randrange(len(gre_words_variable))
        selected_line = gre_words_variable[random_number]
        list_of_selected_line = selected_line.split(":")
        secret_word = list_of_selected_line[0][:-1].upper()
        definition_secret_word = list_of_selected_line[1][1:-1].capitalize()
        # Returning the secret word and its definition
        return secret_word, definition_secret_word

    def list_empty_space_converter(self, secret_word):
        """Creating the lists of letters of the secret world and "_" characters (based on the length of the secret word) to later
        display the current standing to the user"""
        # Listing out the letters of the secret word
        list_secret_word = list(secret_word)
        # Creating a list of "_" characters (based on the length of the secret word) to later display the current standing to the user
        list_current_position = []
        for _ in range(len(list_secret_word)):
            list_current_position.append("_")
        return list_current_position, list_secret_word

class Main:
    def main(self):
        """The main Hangman function, which decides if the user wins or lose, and then askshim/her to play again"""
        # Displaying welcome message to the user
        print(colored("Welcome to the Hangman Game with the GRE vocabulary!", "yellow"))
        correct_guess = 0
        total_guess = 0
        # Create a while loop to keep asking the user to play again if he/she does not win
        while True:
            instance_of_SecretWord = SecretWord()
            # Generating our secret word that need to be guessed by the user with the secret_word_generator() function
            secret_word, definition_secret_word = instance_of_SecretWord.secret_word_generator()
            # Creating the lists of letters of the secret world and "_" characters () to later
            # display the current standing to the user with the ist_empty_space_converter() function
            list_current_position, list_secret_word = instance_of_SecretWord.list_empty_space_converter(secret_word)
            # Setting the total number of wrong guesses to 5
            wrong_guess = 5
            # Creating an empty list for guessed letters to later check if the user is guessing the same letter again or not
            guessed_letters = []
            # Playing the game with the gameplay() function
            guessed_word = Gameplay().gameplay(secret_word, definition_secret_word, list_current_position, list_secret_word, wrong_guess, guessed_letters)
            # If the user wins, then prints out the congratulory message, and then end the game
            if guessed_word == secret_word:
                print(colored(f"\nCongratulations!\nThe word was {guessed_word}.\n", "green"))
                correct_guess += 1
                total_guess += 1
            # If the user loses, then prints out the "you lost" message and the correct word
            else:
                print(colored(f"\nYou lost.\nThe word was {secret_word}.\n", "red",))
                total_guess += 1
            # If the user does not want to play again, then end the game. Otherwise, go back and start the game again from the beginning
            instance_of_PlayAgain = PlayAgain()
            play_again = instance_of_PlayAgain.playing_again()
            if play_again == "n":
                print(colored(f"You guessed {correct_guess} out of {total_guess} word(s) correctly. Keep up the good work!\n", "yellow"))
                sys.exit()

# For running the module as a standalone program, we need to add the following code below:
if __name__ == "__main__":
    instance_of_Main = Main()
    instance_of_Main.main()