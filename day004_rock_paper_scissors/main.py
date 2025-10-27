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

arsenal = {1: rock, 2: paper, 3: scissors}
arsenal_key_str = [str(opt) for opt in arsenal.keys()]

prompts = {
    "welcome": "Rock, paper, scissors VS the Computer.",
    "choices": ["Enter 1 for rock.", "\nEnter 2 for paper.", "\nEnter 3 for scissors."],
}

game_on = True
while game_on:
    clear_print(prompts["welcome"], delay=1)
    clear_print(prompts["choices"], delay=1)

    get_input = True
    while get_input:
        try:
            user_weapon = input("\nEnter choice: ").strip()
            if user_weapon not in arsenal_key_str:
                raise ValueError(
                    f"Invalid input: {user_weapon}\nValid inputs include: {arsenal_key_str}"
                )
            else:
                get_input = False
        except Exception as error:
            print("Error: " + str(error))
            pause(1)

    user_weapon = arsenal[int(user_weapon)]
    computer_weapon = arsenal[random.randint(1, 3)]

    print(f"\nYour choice: {user_weapon} \nComputer's choice: {computer_weapon}")

    if (
        computer_weapon == rock
        and user_weapon == scissors
        or computer_weapon == scissors
        and user_weapon == paper
        or computer_weapon == paper
        and user_weapon == rock
    ):
        print("\nXXXTHE COMPUTER WINSXXX")
        game_on = False
    elif computer_weapon == user_weapon:
        print("\nWE HAVE A TIE. Try again.")
    else:
        print("\n!!!YOU WIN!!!")

    pause(1)
