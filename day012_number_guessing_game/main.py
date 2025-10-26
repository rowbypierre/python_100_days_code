import random
from art import number_ascii, win_acii, lose_ascii

LEVELS = {"easy": 10, "hard": 5}

MAGIC_NUMBER = random.randint(1, 100)


def correct_guess(guess):
    """Confirm (bool) whether guess (str) is correct."""
    return int(guess) == MAGIC_NUMBER


def too_cold(guess):
    """Confirm (bool) whether guess (str) is too low/cold."""
    return int(guess) < MAGIC_NUMBER


print(number_ascii + "\n!NUMBER RANGES FROM 1 TO 100!")

try:
    level = input("Choose diffculty. Type easy or hard: ").strip().lower()
    if level not in LEVELS.keys():
        raise ValueError(f"Input '{level}' is invalid. Expected 'easy' or 'hard'.")

    max_try = LEVELS[level]
    for round in range(1, max_try + 1):
        print(f"ATTEMPT #: {round}")
        # print(MAGIC_NUMBER) # Testing
        guess = input("Make a guess: ").strip()
        if not guess.isnumeric():
            raise ValueError(f"Guess '{guess}' is invalid. Expected integer.")
        else:
            if not correct_guess(guess):
                if round == max_try:
                    print(lose_ascii + f"\n!MAGIC_NUMBER IS {MAGIC_NUMBER}!")
                    break
                elif too_cold(guess):
                    print("TOO COLD")
                elif not too_cold(guess):
                    print("TOO_HOT")
            if correct_guess(guess):
                print(win_acii)
                break

except Exception as error:
    print(error)
