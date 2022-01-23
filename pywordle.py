import random
import json


# TODO:
# Handle single letters in guesses when there are multiple in the word.
intro_message = """
###########################################################
Welcome to Wordle, Python-style!

Try to guess the 5-letter word.

Letters from guesses will display as follows:
* Uppercase if contained in word and in correct position (A)
* Lowercase if contained in word but in wrong position (a)
* Flanked by hyphens if not in word (-a-)

You have 6 guesses. Good luck!

All credit to Josh Wardle:
https://www.powerlanguage.co.uk/wordle/
github.com/powerlanguage
###########################################################
"""

def load_dictionary():
    with open("words_dictionary.json") as f:
        word_dictionary = json.load(f)
        return word_dictionary


def create_word_list(word_dictionary):
    word_list = []
    for word in word_dictionary.keys():
        if len(word) == 5:
            if word.isalpha():
                word_list.append(word)
        else:
            pass
    return word_list


def pick_random_word(word_list):
    random_index = random.randint(0, len(word_list) - 1)
    word_to_guess = word_list[random_index]
    return word_to_guess


def wrong_letter(letter, guess, formatted_guess, index=0):
    formatted_guess[guess.index(letter, index)] = f"-{letter}-"


def right_letter(letter, word, guess, formatted_guess, index_1=0, index_2=0):
    if word.index(letter, index_1) == guess.index(letter, index_2):
        formatted_guess[guess.index(letter)] = letter.upper()
    elif word.index(letter, index_1) != guess.index(letter, index_2):
        formatted_guess[guess.index(letter)] = letter.lower()


def main():
    dictionary = load_dictionary()
    word_list = create_word_list(dictionary)


    while True:
        formatted_guess = []
        num_guesses = 0
        print(intro_message)
        word_to_guess = pick_random_word(word_list)
        while num_guesses < 6:
            # print(word_to_guess)
            correct_letters = 0
            guess = input("\nGuess a 5-letter word: ")
            if guess.lower() == "q":
                break
            elif len(guess) != 5:
                print("That's not a 5-letter word!")
                pass
            elif guess.lower() not in word_list:
                print("That's not a real word!")
                pass
            elif guess.lower() in word_list:
                formatted_guess = ["", "", "", "", ""]
                guess = list(guess.lower())
                starting_index_word = 0  # To handle repeat letters.
                starting_index_guess = 0
                times_recurred = 0
                for letter in guess:
                    letter_count = word_to_guess.count(letter)
                    if letter_count == 0:
                        if guess.count(letter) == 1:
                            wrong_letter(letter, guess, formatted_guess)
                        elif guess.count(letter) > 1:
                            times_recurred += 1
                            if times_recurred == 1:
                                wrong_letter(letter, guess, formatted_guess)
                            elif times_recurred > 1:
                                index_nudge = guess.index(letter) + 1
                                wrong_letter(letter, guess, formatted_guess, index=index_nudge)
                    elif letter_count == 1:
                        if guess.count(letter) == letter_count:
                            right_letter(letter, word_to_guess, guess, formatted_guess)
                        elif guess.count(letter) > letter_count:
                            times_recurred += 1
                            print(times_recurred)
                            if times_recurred == 1:
                                right_letter(letter, word_to_guess, guess, formatted_guess)
                            elif times_recurred > 1:
                                index_nudge = guess.index(letter) + 1
                                wrong_letter(letter, guess, formatted_guess, index=index_nudge)
                    elif letter_count > 1:
                        if guess.count(letter) < letter_count:
                            for i in range(letter_count):
                                try:
                                    if word_to_guess.index(letter, starting_index_word) == guess.index(letter, starting_index_guess):
                                        formatted_guess[guess.index(letter, starting_index_guess)] = letter.upper()
                                        starting_index_word = word_to_guess.index(letter) + 1
                                        if guess.index(letter) < 4:
                                            starting_index_guess = guess.index(letter) + 1
                                    elif word_to_guess.index(letter, starting_index_word) != guess.index(letter, starting_index_guess):
                                        formatted_guess[guess.index(letter, starting_index_guess)] = letter.lower()
                                        starting_index_word = word_to_guess.index(letter) + 1
                                        if guess.index(letter) < 4:
                                            starting_index_guess = guess.index(letter) + 1
                                except ValueError:
                                    print(f"{letter} {starting_index_word}")
                                    print(starting_index_guess)
                                    print("Oops value error.")
                                    pass
                        elif guess.count(letter) == letter_count:
                            if word_to_guess.index(letter, starting_index_word) == guess.index(letter, starting_index_guess):
                                formatted_guess[guess.index(letter, starting_index_guess)] = letter.upper()
                                starting_index_word = word_to_guess.index(letter) + 1
                                starting_index_guess = guess.index(letter) + 1
                            elif word_to_guess.index(letter, starting_index_word) != guess.index(letter, starting_index_guess):
                                formatted_guess[guess.index(letter, starting_index_guess)] = letter.lower()
                                starting_index_word = word_to_guess.index(letter) + 1
                                starting_index_guess = guess.index(letter) + 1
                        elif guess.count(letter) > letter_count:
                            times_recurred += 1
                            print(times_recurred)
                            if times_recurred == 1:
                                if word_to_guess.index(letter, starting_index_word) == guess.index(letter, starting_index_guess):
                                    formatted_guess[guess.index(letter, starting_index_guess)] = letter.upper()
                                    starting_index_word = word_to_guess.index(letter) + 1
                                    starting_index_guess = guess.index(letter) + 1
                                elif word_to_guess.index(letter, starting_index_word) != guess.index(letter, starting_index_guess):
                                    formatted_guess[guess.index(letter, starting_index_guess)] = letter.lower()
                                    starting_index_word = word_to_guess.index(letter) + 1
                                    starting_index_guess = guess.index(letter) + 1
                            elif times_recurred > 1:
                                index_nudge = guess.index(letter) + 1
                                if word_to_guess.index(letter, starting_index_word) == guess.index(letter, starting_index_guess):
                                    formatted_guess[guess.index(letter, starting_index_guess)] = letter.upper()
                                    starting_index_word = word_to_guess.index(letter) + 1
                                    starting_index_guess = guess.index(letter) + 1
                                elif word_to_guess.index(letter, starting_index_word) != guess.index(letter, starting_index_guess):
                                    formatted_guess[guess.index(letter, starting_index_guess)] = letter.lower()
                                    starting_index_word = word_to_guess.index(letter) + 1
                                    starting_index_guess = guess.index(letter) + 1
                num_guesses += 1
                starting_index_word = 0
                starting_index_guess = 0
                print(f"{num_guesses}.", end = " ")
                for letter in formatted_guess:
                    print(f"[{letter}]", end=" ")
                    if letter.isupper():
                        correct_letters += 1
            if correct_letters == 5:
                print("Congratulations!")
                break
        if correct_letters != 5:
            print(f"\nThe correct answer was: {word_to_guess.title()}")
        play_again = input("Play again? (Y/N) ")
        if play_again.lower() == "y":
            pass
        elif play_again.lower() == "n":
            print("Hwyl fawr.")
            break
        else:
            print("I'll take that as a yes.")
            break


if __name__ == "__main__":
    main()
