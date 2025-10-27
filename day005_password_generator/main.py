import random
import os


char_types = {
    "letters": [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ],
    "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "symbols": ["!", "#", "$", "%", "&", "(", ")", "*", "+"],
}


def clear_screen():
    """Clear terminal screen of Unix-like or Windows operating system."""
    os.system("cls" if os.name == "nt" else "clear")


def make_pass():
    """
    Generate password containing letters, numbers, and symbols.

    Prompts:
        - Desired number of letters (int).
        - Desired number of numbers (int).
        - Desired number of symbols (int).

    Returns:
        None: Print new password.

    Raises:
        ValueError: Prompted inputs not contain integer.
    """
    clear_screen()
    print("\nWelcome to the Password Generator!\n")

    new_pass = list()
    for char in char_types:
        get_qty = True
        while get_qty:
            try:
                count = input(f"\nEnter desired number of {char}:\t").strip()
                ve_flag = f"Input {count} is invalid. Whole integer required."
                if not count.isdigit():
                    raise ValueError(ve_flag)
                elif int(count) < 0:
                    raise ValueError(ve_flag)
                else:
                    get_qty = not get_qty
            except Exception as error:
                print(f"Error: {error}")

        new_pass += random.choices(char_types[char], k=int(count))

    random.shuffle(new_pass)
    pass_str = "".join(new_pass)

    clear_screen()
    print(f"New password: {pass_str}")


if __name__ == "__main__":
    make_pass()
