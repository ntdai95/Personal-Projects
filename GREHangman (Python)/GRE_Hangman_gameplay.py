# Importing the colored function for user-friendly display
from termcolor import colored

class LetterPlacer:
    def placing_letter_in_word(self, chosen_letter, list_secret_word, list_current_position):
        """Placing the user's guessed letter into the corresponding position among the list of list_current_position and then convert
        it to a string to print out to the user the location of his/her choice of guessed letters"""
        # Creating an empty list for the indexes where the user's guessed letter is located
        indexes = []
        # Adding the indexes to the list of indexes where the user's guessed letter is located
        for index, letter in enumerate(list_secret_word):
            if letter == chosen_letter:
                indexes.append(index)
        # Change the "_" characters with the user's guessed letter based on its location in the secret word
        for index in indexes:
            list_current_position[index] = chosen_letter
        # Creating an empty string to display the location of the guessed letter for the user
        string_current_position = ""
        # Adding up the "_" characters with the correctly guessed letters as a string to display to the user
        for index in list_current_position:
            string_current_position = string_current_position + " " + index
        # Print out the location of the guessed letter to the user
        print(f"{chosen_letter} is in the word{string_current_position}.")
        # Return the updated list of list_current_position with the added guessed letter
        return list_current_position

class GuessedWordChecker:
    def guess_word_input_validator(self):
        """Asking and checking the user's guessed word"""
        # Create a while loop to keep asking for a valid guessed word from the user
        while True:
            # Asking the user for the guessed word, allowing the mix of uppercased and lowercased letters. Need to be upeercased the 
            # user input, so that it can match with the uppercased secret word.
            guessed_word = input("\nTry and guess the word? ").upper()
            # If the user's guessed word is valid, then return it.
            if guessed_word.isalpha() == True:
                return guessed_word
            # If the user's guessed word is not valid (the guessed word contains non-alphabetical characters such as numbers of symbols,
            # @, !, etc.), then display the warning message and go back and ask the new guessed word again.
            else:
                print("Please, guess a real word with alphabetical letters only.")

    def guessed_word_is_secret_word(self, guessed_word, secret_word, wrong_guess):
        """Decides if the user's guessed word is the same as the secret word"""
        # If the user's guessed word is the same as the secret word, then return the user's guessed word, which will be the same as the 
        # secret word
        if guessed_word == secret_word:
            return guessed_word
        # If the user's guessed word is not the same as the secret word, then print out the warning message and return the guessed word
        # as an empty string
        else:
            guessed_word = ""
            print(f"That is not the word.\nYou still have {wrong_guess} guesses remaining.")
            return guessed_word

class LetterChecker:
    def letter_validator(self, chosen_letter, guessed_letters):
        """Checking if the user's entered letter is valid or not"""
        # Check if the user enters an alphabetical letter or not
        if chosen_letter.isalpha() == False:
            print("Please, enter an alphabetical letter only!")
        # Check if the user enters only 1 letter or not
        elif len(list(chosen_letter)) != 1:
            print("Please, enter one letter only!")
        # Check if the guessed letter has already been guessed before
        elif chosen_letter in guessed_letters:
            print("You already guessed this letter. Please, choose another letter.")
        # If there is no issue with the guessed letter, then return the following message
        else:
            return "Good letter"

    def chosen_letter_in_list_secret_word(self, chosen_letter, wrong_guess, list_secret_word, list_current_position, secret_word, guessed_word):
        """Checking if the user's chosen letter is among the list of letters of the secret word"""
        # Checking if user input of letter is in the secret word
        if chosen_letter in list_secret_word:
            # If the chosen letter is in the list of letters of secret word, then place that guessed letter in to its appropriate
            # position(s) in the list of letters of secret word with the function of
            # placing_letter_in_word()
            instance_of_LetterPlacer = LetterPlacer()
            list_current_position = instance_of_LetterPlacer.placing_letter_in_word(chosen_letter, list_secret_word, list_current_position)
            # If the user find out all of the letters in the secret word, then there is no point to keep asking him again to guess the 
            # secret word
            if "_" not in list_current_position:
                return  wrong_guess, list_current_position, secret_word
            else:
                instance_of_GuessedWordChecker = GuessedWordChecker()
                # Ask the user to enter his/her's guess for the secret word and check if it is valid
                guessed_word = instance_of_GuessedWordChecker.guess_word_input_validator()
                # Replacing the guessed word with the secret word if the user correctly guessed the word with the function of
                # guessed_word_is_secret_word()
                guessed_word = instance_of_GuessedWordChecker.guessed_word_is_secret_word(guessed_word, secret_word, wrong_guess)
        # If the word is not in the secret word, then decrease the number of guesses remaining by 1 and print out how many guess remains
        # for the user
        else:
            wrong_guess -=1
            print(f"{chosen_letter} is not in the word.\nYou have {wrong_guess} guesses remaining.")
        # Return the updated wrong_guess, list_current_position, guessed_word variables
        return wrong_guess, list_current_position, guessed_word

class Gameplay:
    def gameplay(self, secret_word, definition_secret_word, list_current_position, list_secret_word, wrong_guess, guessed_letters):
        """Deciding if the user correctly guessed the word or not"""
        # Creating a while loop to let the user guessed the letters until he/she runs out of guesses remainng
        while wrong_guess != 0:
            # Displaying the definition and the current position of guessed letters in the secret word
            print(colored(f"\nDefinition: {definition_secret_word}", "cyan"))
            string_current_position = ""
            for character in list_current_position:
                string_current_position += character + " "
            print(colored(f"Word: {string_current_position[:-1]}\n", "cyan"))
            # Asking the user for a letter, allowing either an uppercased or lowercased letter. Need to be uppercased the user input so 
            # that it can match the list of uppercased letters from the list of list_secret_word
            chosen_letter = input("Guess a letter? ").upper()
            # Checking, if the letter is valid with the letter_validator() function
            instance_of_LetterChecker = LetterChecker()
            letter_validity = instance_of_LetterChecker.letter_validator(chosen_letter, guessed_letters)
            # Creating an empty string of guessed word, which will be the secret word if the user guesses it correctly and empty string
            # otherwise
            guessed_word = ""
            # If the user input letter is valid, then move on, otherwise go back and ask a new letter again
            if letter_validity == "Good letter":
                # Adding the user entered valid letter to the lsit of guessed_letters to later check if the user is guessing the same 
                # letter again
                guessed_letters.append(chosen_letter)
                # Checking if the user's guessed letter is among the list of letters of the secret word with the function of
                # chosen_letter_in_list_secret_word(). Then, return the number of wrong guesses remaining, the
                # list of list_current_position (to display the current standing to the user), and the guessed_word as a secret word if 
                # the user guesses the word correctly after the guessing correctly the letter is among the letters of the secret word
                wrong_guess, list_current_position, guessed_word = instance_of_LetterChecker.chosen_letter_in_list_secret_word(chosen_letter, wrong_guess, list_secret_word, list_current_position, secret_word, guessed_word)
                # If the user guessed the secret word correctly, then return the guessed word as a secret word
                if guessed_word == secret_word:
                    return guessed_word
        # If the user did not guessed the secret word correctly and runs out of guesses, then return the guessed word as an empty string
        else:
            return guessed_word