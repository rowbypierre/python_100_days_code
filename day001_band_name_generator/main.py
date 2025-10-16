import os


def os_cmmd(win_cmmd, unix_cmmd, type="run"):
    """
    Run or read a command depending on the OS (Operating System).

    Parameters:
    win_cmmd (str): Command for Windows.
    unix_cmmd (str): Command for Unix-like systems.
    type (str): 'run' to execute, 'read' to get output.

    Returns:
    str: Output of the command if type is 'read'; otherwise None.

    Raises:
    ValueError: If 'type' is not 'run' or 'read'.
    RuntimeError: If the command fails to execute.
    """
    try:
        cmd = win_cmmd if os.name == "nt" else unix_cmmd

        if type == "run":
            return_code = os.system(command=cmd)
            if not return_code == 0:
                raise RuntimeError(f"Command failed, exit code: {return_code}")
        elif type == "read":
            ouput = os.popen(cmd=cmd).read().strip()
            return ouput
        else:
            raise ValueError("type must be 'run' or 'read'")

    except Exception as error:
        print(f"Error: {error}")


def clear():
    """
    Clear the terminal screen.

    Detects operating system and runs appropriate command to clear the terminal screen:
    - 'cls' for Windows
    - 'clear' for Unix/Linux/ macOs
    """
    os_cmmd(win_cmmd="cls", unix_cmmd="clear", type="run")


def band_name_gen():
    """
    Generate 10 band names from user-input city and pet name.

    Prompts:
        - City name (str)
        - Pet name (str)

    Returns:
        None: Prints generated band names.

    Raises:
        ValueError: If inputs contain non-alphabetic characters.
    """
    try:
        clear()
        user = os_cmmd(win_cmmd="whoami", unix_cmmd="whoami", type="read").upper()
        city = input(f"""\n!!!!!!!!!!!!Band Name Generator!!!!!!!!!!!! 
                    \nWelcome {user} 
                    \nWhat's the name of the city you up in? \n""").strip()
        pet = input("\nEnter a great pet name? \n").strip()

        if not (city.isalpha() & pet.isalpha()):
            raise TypeError("string characters must be alphabetic")

        band_patterns = [
            "The {} Beats of {}",
            "The {} {} Chorus",
            "Velvet {} of {}",
            "Midnight {} in {}",
            "{} {} Rhapsody",
            "Echoing {} of {}",
            "{} {} Ensemble",
            "Groovy {} of {}",
            "Sonic {} Serenade in {}",
        ]

        clear()
        for pattern in band_patterns:
            print(pattern.format(pet.capitalize(), city.capitalize()))

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    band_name_gen()
