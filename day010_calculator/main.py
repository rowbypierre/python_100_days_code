import os, math
from art import logo

def add(number1, number2):
    """
    Args:
        number1 (integer): First of two integers to be added.
        number2 (integer): Second of two integers to be added.

    Returns:
        integer: Summation of number1 and number2.
    """
    return number1 + number2

def subtract(number1, number2):
    """
    Args:
        number1 (integer): First of two integers to be subtracted.
        number2 (integer): Second of two integers to be subtracted.

    Returns:
        integer: Result of number1 minus number2.
    """
    return number1 - number2

def divide(number1, number2):
    """
    Args:
        number1 (integer): First of two integers to be divided.
        number2 (integer): Second of two integers to be divided.

    Returns:
        integer: Result of number1 divided number2.
    """
    return number1 / number2

def multiply(number1, number2):
    """
    Args:
        number1 (integer): First of two integers to be multiplied.
        number2 (integer): Second of two integers to be multiplied.

    Returns:
        integer: Result of number1 multiplied number2.
    """
    return number1 * number2

def power(number1, number2):
    """
    Args:
        number1 (integer): Base number.
        number2 (integer): Power which base number is raised.

    Returns:
        integer: Result of number1 raised to the power of number2.
    """
    return number1 ** number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "`": "square root"
}

def calculator():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)
    
    iteration = 1
    while iteration > 0:
        if iteration == 1:
            number1 = float(input("\nEnter numeric value: \n> "))
        else:
            number1 = answer

        print("\nOperators:")
        for option in operations:
            print(option)
        option = input("\nEnter operator from above: \n> ")
        if option == '`':
            answer = math.sqrt(number1)
            print(f"{number1} ** -2 = {answer}")
        else:
            number2 = float(input("\nEnter another numeric value: \n> "))

            calculation_function = operations[option]
            answer = calculation_function(number1, number2)
            print(f"\n{number1} {option} {number2} = {answer}")
        
        continuation = input("\nEnter 'y' to continue \nEnter 'z' to restart \nEnter 'n' to exit: \n> ")
        if continuation ==  "y":
            iteration += 1
        elif continuation == "z":
            calculator()
        elif continuation == "n":
            break
        
if __name__ == "__main__":
    calculator()
