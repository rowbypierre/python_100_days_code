import art
import random
import os
import time
import game_data


def clear_screen():
    """Clears termainl screen of Windows or UNIX-like operating systems."""
    os.system("cls" if os.name == "nt" else "clear")


def two_random_celebs():
    """Return (list) two random celebs (dict) from game_data.py"""
    return random.sample(game_data.data, 2)


def guess_correct(celeb_a, celeb_b, guess):
    """Confirms (bool) game players guess."""
    if celeb_a["follower_count"] > celeb_b["follower_count"]:
        popular_celeb = "A"
    else:
        popular_celeb = "B"

    return guess == popular_celeb


def game_display(celeb_list, score):
    """Terminal game layout display."""
    clear_screen()
    print(
        art.logo
        + f"\nSCORE: {score}"
        + f"\nCompare A: {celeb_list[0]['name']}, a {celeb_list[0]['description']}, from {celeb_list[0]['country']}."
        + art.vs
        + f"\nCompare B: {celeb_list[1]['name']}, a {celeb_list[1]['description']}, from {celeb_list[1]['country']}."
    )


def higher_lower():
    """Guess celebrity with greater social media following:

    Prompt:
        - guess (str): A for celeb, A B for celeb B.

    Return:
        None: Print screen and ascii art confirming correct guess.

    Raises:
        ValueError: guess (str) prompt not 'A' or 'B'.
    """
    score = 0
    valid_inputs = ["A", "B"]
    at_play = True
    while at_play:
        celebs = two_random_celebs()
        print(celebs)
        game_display(celebs, score)

        try:
            guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
            if guess not in valid_inputs:
                raise ValueError(f"Guess {guess} is invalid. Expected: {valid_inputs}.")
        except ValueError as ve:
            print(ve)

        if guess_correct(*celebs, guess):
            score += 1
            print(art.right)
        else:
            print(art.wrong)
            at_play = not at_play

        time.sleep(1)


if __name__ == "__main__":
    higher_lower()
