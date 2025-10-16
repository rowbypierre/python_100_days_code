from os import system, name, popen


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
        cmd = win_cmmd if name == "nt" else unix_cmmd

        if type == "run":
            return_code = system(command=cmd)
            if not return_code == 0:
                raise RuntimeError(f"Command failed, exit code: {return_code}")
        elif type == "read":
            ouput = popen(cmd=cmd).read().strip()
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


def is_float(num):
    """
    Check if value (num) is valid float.

    Parameters:
    num (int): Numeric value (integer or float).

    Returns:
    bool: True If value is valid float.

    Raises:
    ValueError: If 'num' is not valid float.
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


def billSplit():
    """
    Calculate diner split with graditudity.

    Prompts:
        - bill (float)
        - tip_pct (float)
        - diners (integer)

    Returns:
        None: Prints diner split cash value.

    Raises:
        ValueError: Invalid user inputs with respect to -
        bill amount, tip percentage, or total # of diners.
    """
    clear()  # clear terminal (unix or windows)
    try:
        # Get system Username
        user = os_cmmd(
            win_cmmd="whoami", unix_cmmd="whoami", type="read"
        )
        # Welcome, get bill total  
        bill = (
            input(f"""Welcome {user.upper()}
                  \nBill total ($):\t""")
            .replace("$", "")
            .strip()
        )  
        if not is_float(bill) or float(bill) < 1:  # Check bill amount
            raise ValueError("Bill amount invalid, enter numeric value > 1.")

        clear()
        tip_rates = [num for num in range(0, 51, 10)]
        print(f"Common tip rates (%): {tip_rates}")
        tip_pct = input("\nTip rate (%):\t")  # Get tip rate
        if not is_float(tip_pct) or float(tip_pct) < 0:  # Check tip rate
            raise ValueError("Tip rate invalid, enter numeric value > 0.")

        diners = input("\nNumber of diners:\t").strip()  # Get head count
        if not diners.isdigit() or float(diners) < 0:  # Check head count input
            raise ValueError("Number of guest invalid, enter whole number > 0.")

        split = round((float(bill) * (1 + float(tip_pct) / 100)) / int(diners), 2)
        split = "{:.2f}".format(split)

        clear()
        print(f"\nDiner splits: ${split}")  # Print split per diner

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    billSplit()  # Call function
