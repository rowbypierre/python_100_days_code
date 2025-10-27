from art import logo


def calculator():
    """Execute calculations.

    Prompts:
        - n1 (float): Number or decimal.
        - n2 (float): Number or decimal.
        - op (str): Math operation.
        - next op (str): Continue or start new calculation, or exit

    Returns:
        None: Print result to terminal.

    Raises:
        ValueError: Invalid prompt input."""
    print(logo)

    use_result = False
    operating = True
    while operating:
        get_values = True
        while get_values:
            try:
                if not use_result:
                    n1 = float(input("Enter value:\t").strip())
                n2 = float(input("Enter value:\t").strip())
                get_values = False
            except ValueError:
                print("One or both inputs not float type.")
            except Exception as error:
                print(f"Error: {error}")

        ops = ["+", "-", "/", "*", "^"]

        get_operand = True
        while get_operand:
            try:
                op = input(f"Enter {ops}:\t").strip()
                if op not in ops:
                    raise ValueError(
                        f"Invalid operation input {op}. Operations include {ops}."
                    )
                else:
                    get_operand = not get_operand
            except Exception as error:
                print(f"Error: {error}")

        op_str = f"{n1} {op.replace('^', '**')} {n2}"
        result = eval(op_str)
        print(f"{op_str}: {result}")

        prompting = True
        while prompting:
            try:
                next_op = (
                    input("\ny - continue" + "\nn - new calculation" + "\nx - exit\n: ")
                    .strip()
                    .lower()
                )
                if next_op not in ["y", "n", "x"]:
                    raise ValueError("Invalid input. Expecting y, n, or x.")
                else:
                    prompting = not prompting
            except Exception as error:
                print(f"Error: {error}")
        if next_op == "y":
            n1 = result
            use_result = True
        elif next_op == "n":
            use_result = False
        elif next_op == "x":
            break


if __name__ == "__main__":
    calculator()
