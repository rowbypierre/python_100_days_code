from hangman_misc import word_list, hangmans, logo
import random
import os
import time


def clear():
    """ "Clear terminal screen of Window or Unix-like system."""
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec=2):
    """Pause before performing next action for provided second(s) (sec: int)."""
    time.sleep(sec)


def hangman():
    """
    Guess randomly selected word and hanging the man.

    Prompts:
        - guess (str): Single alphabet character.

    Returns:
        - None: Confirmation with correct guess, evolving hangman ascii drawing
                with incorrect guesses.

    Raises:
        - ValueError: guess (str) input has numbers, spaces, or special characters.
    """
    clear()
    prompts = [
        logo + "\nEnjoy this hangman game.",
        "\nA random word has been selected.",
    ]
    for prompt in prompts:
        print(prompt)
        pause()

    life = len(hangmans)
    bad_guess = 1
    game_word = random.choice(word_list).lower()
    word_index = [(index, letter) for index, letter in enumerate(game_word)]
    word_shell = ["_" for _ in range(len(game_word))]

    game_on = True
    try:
        while game_on:
            clear()
            if "".join(word_shell) == game_word:
                print(f"""!!!YOU WON!!!
                    \n{game_word.capitalize()} was the mysyterious word.""")
                pause()
                break
            else:
                life_prompt = f"\nYou have {life - bad_guess} chance(s) remaining."
                print(str(word_shell) + "\n" + life_prompt)
                guess = input("\nGuess a letter: ").lower().strip()
                if not guess.isalpha() or len(guess) > 1:
                    raise ValueError(f"Expecting 1 character, recieved: {guess}")
                elif guess in game_word and guess not in word_shell:
                    print('\nCorrect, "{}" exist in the chosen word.'.format(guess))
                    pause()

                    for index, letter in word_index:
                        if guess == letter:
                            word_shell[index] = guess

                    print(f"\n{word_shell}")
                elif guess in word_shell:
                    print('\nYou have already entered the letter "{}".'.format(guess))
                    pause()
                else:
                    print(hangmans[life - bad_guess])
                    pause()
                    game_on = bad_guess != life
                    if game_on:
                        bad_guess += 1
                        print(
                            '\nIncorrect, "{}" does not exist in the word.'.format(
                                guess
                            )
                        )
                    else:
                        print("\n!!!YOU WERE HUNG!!!")
                        print(f"\n{game_word.upper()} was the mysyterious word.")
    except Exception as error:
        print(f"Error: {error}")
