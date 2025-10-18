import time
import os
import random


def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause(seconds):
    """Create delay in terminal screen for provided number of seconds (float)."""
    time.sleep(seconds)


def clear_print(string, delay):
    """Clear terminal screen and print strings(s), followed by delay (int - secs)"""
    obj_types = [list, str]
    obj_type = type(string)
    if obj_type in obj_types:
        clear_screen()

        if isinstance(string, list):
            for line in string:
                print(line)
        else:
            print(string)
        pause(delay)


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = {1: rock, 2: paper, 3: scissors}
options_list = [opt for opt in options.keys()]

prompts = {
    "welcome": "Rock, paper, scissors VS the Computer.",
    "choices": ["Enter 1 for rock.", "\nEnter 2 for paper.", "\nEnter 3 for scissors."],
}

not_raise_ve = True
game_on = True
while game_on:
    clear_print(prompts["welcome"], delay=2)
    clear_print(prompts["choices"], delay=2)

    try:
        user_choice = input("\nEnter choice: ").strip()
        not_raise_ve = user_choice.isdigit()

        if not_raise_ve:
            not_raise_ve = int(user_choice) in options_list
            if not_raise_ve:
                user_choice = options[int(user_choice)]
                computer_choice = options[random.randint(1, 3)]

                print(
                    f"\nYour choice: {user_choice} \nComputer's choice: {computer_choice}"
                )

                if (
                    computer_choice == rock
                    and user_choice == scissors
                    or computer_choice == scissors
                    and user_choice == paper
                    or computer_choice == paper
                    and user_choice == rock
                ):
                    print("\nXXXTHE COMPUTER WINSXXX")
                    game_on = False
                elif computer_choice == user_choice:
                    print("\nWE HAVE A TIE. Try again.")
                else:
                    print("\n!!!YOU WIN!!!")
                    game_on = False

        if not not_raise_ve:
            game_on = False
            raise ValueError(
                f"Invalid input: {user_choice}\nValid inputs include: {options_list}"
            )

    except Exception as error:
        print("Error: " + str(error))
